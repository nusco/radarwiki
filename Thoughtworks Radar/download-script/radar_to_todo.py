#!/usr/bin/env python3
"""Download Thoughtworks Technology Radar blips into Markdown todo lists.

Lists the published Radar volumes, asks which ones to download, and writes
one file per volume, e.g. "thoughtworks-radar-2026-april.md".

Data sources:
- The Radar archive page, for the list of volumes and their dates.
- The Coveo search index behind https://www.thoughtworks.com/radar/search,
  which lists every blip, with its *latest* appearance only.
- Each blip page's history timeline, for all its appearances.

The two sources occasionally disagree, so a blip is included in a volume if
either of them says it belongs there.

Blip histories are cached in .radar-cache.json next to this script, because
the site blocks clients that read too many pages in a short time.
"""

import calendar
import json
import re
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SITE = "https://www.thoughtworks.com"
USER_AGENT = "Mozilla/5.0 (radar-to-todo script)"
CACHE_FILE = Path(__file__).with_name(".radar-cache.json")
PARALLEL_REQUESTS = 4

QUADRANTS = {
    "techniques": "Techniques",
    "tools": "Tools",
    "platforms": "Platforms",
    "languages-and-frameworks": "Languages & Frameworks",
}
# The outermost ring was called "Hold" until it was renamed "Caution" in April 2026.
RINGS = ["Adopt", "Trial", "Assess", "Hold", "Caution"]


class Blocked(Exception):
    pass


def fetch(url, data=None, headers=None):
    headers = {"User-Agent": USER_AGENT, **(headers or {})}
    request = urllib.request.Request(url, data=data, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as error:
            # Retrying when the site is rate-limiting us only prolongs the block.
            if error.code in (403, 429):
                raise Blocked(f"{error.code} from {url}") from error
            if attempt == 2 or error.code < 500:
                raise
        except OSError:
            if attempt == 2:
                raise
        time.sleep(2 ** (attempt + 1))


def list_volumes():
    """Return [(volume_number, year, month)], oldest first, from the archive page."""
    html = fetch(f"{SITE}/radar/archive")
    found = re.findall(r"/radar/(\d{4})/(\d{2})/tr_technology_radar_vol_(\d+)_en", html)
    volumes = {int(vol): (int(year), int(month)) for year, month, vol in found}
    return [(vol, *volumes[vol]) for vol in sorted(volumes)]


def fetch_all_blips():
    """Return every blip in the search index, with its latest appearance."""
    config = json.loads(fetch(f"{SITE}/rest/search/config"))
    org = config["ORGANIZATION_ID"]
    url = f"https://{org}.org.coveo.com/rest/search/v2?organizationId={org}"
    headers = {
        "Authorization": f"Bearer {config['RADAR_SEARCH_TOKEN']}",
        "Content-Type": "application/json",
    }
    # Results come in no guaranteed order, so paging could skip some blips and repeat
    # others. Instead, ask for everything in one request, and check that we got it all.
    query = {
        "q": "",
        "searchHub": config["RADAR_SEARCH_HUB"],
        "pipeline": config["RADAR_PIPELINE"],
        "locale": "en",
        "context": {"countryLocale": "en-global"},
        "aq": '@tw_country_locale=="en-global"',
        "numberOfResults": 5000,
    }
    response = json.loads(fetch(url, json.dumps(query).encode(), headers))
    blips = [{
        "name": result["raw"].get("tw_radar_display_name") or result["title"],
        "url": result["clickUri"],
        "quadrant": result["raw"].get("tw_radar_quadrant", ""),
        "ring": result["raw"].get("tw_radar_ring_label", "").capitalize(),
        "volume_date": result["raw"].get("tw_radar_volume_date", ""),
    } for result in response["results"]]

    distinct = len({b["url"] for b in blips})
    if distinct != response["totalCount"]:
        raise CheckFailed(f"the search index reports {response['totalCount']} blips, "
                          f"but only {distinct} distinct ones were downloaded.")
    return blips


class CheckFailed(Exception):
    pass


def timeline_label(volume_date):
    """Turn an index date like "2025-11" into a timeline label like "Nov 2025"."""
    year, month = volume_date.split("-")
    return f"{calendar.month_abbr[int(month)]} {year}"


def read_timeline(blip):
    """Read the blip page's history timeline, as {"Nov 2025": "Assess", ...}."""
    html = fetch(blip["url"])
    entries = re.findall(
        r'cmp-blip-timeline__item--time">\s*([^<]*?)\s*</div>\s*'
        r'<div class="cmp-blip-timeline__item--ring[^"]*">\s*<span>\s*([^<]*?)\s*</span>',
        html)
    return dict(entries)


def load_cache():
    try:
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=1, sort_keys=True), encoding="utf-8")


def read_all_timelines(all_blips, volumes):
    """Read every blip's history, and check that it can be trusted.

    A history only changes when a new volume is published, so a cached history is
    reused unless a new volume has come out since it was read, or the search index
    shows a newer appearance than it did then. (The index alone isn't enough: it
    can lag behind the page.) Raises CheckFailed if the pages look different from
    what this script expects, and Blocked if the site starts refusing requests.
    """
    _, year, month = volumes[-1]
    newest_volume = f"{year}-{month:02d}"
    cache = load_cache()

    def is_fresh(blip):
        entry = cache.get(blip["url"])
        return (entry is not None and entry["newest_volume"] == newest_volume
                and entry["index_volume_date"] == blip["volume_date"])

    stale = [b for b in all_blips if not is_fresh(b)]
    fetched = {}
    if stale:
        print(f"Reading the history of {len(stale)} blips "
              f"({len(all_blips) - len(stale)} cached)...", flush=True)
        pool = ThreadPoolExecutor(max_workers=PARALLEL_REQUESTS)
        try:
            futures = {pool.submit(read_timeline, b): b for b in stale}
            for future in as_completed(futures):
                blip = futures[future]
                fetched[blip["url"]] = future.result()
                if fetched[blip["url"]]:  # Never cache a page that came back without history.
                    cache[blip["url"]] = {"newest_volume": newest_volume,
                                          "index_volume_date": blip["volume_date"],
                                          "timeline": fetched[blip["url"]]}
        finally:
            # Keep what was read so far, so a run that gets blocked can resume later.
            pool.shutdown(cancel_futures=True)
            save_cache(cache)
    timelines = [fetched[b["url"]] if b["url"] in fetched else cache[b["url"]]["timeline"]
                 for b in all_blips]

    known_labels = {timeline_label(f"{year}-{month:02d}") for _, year, month in volumes}
    problems = []
    for blip, timeline in zip(all_blips, timelines):
        if not timeline:
            problems.append(f"{blip['name']} ({blip['url']}): no history found on the page")
        for label in set(timeline) - known_labels:
            problems.append(f"{blip['name']} ({blip['url']}): history date '{label}' "
                            "doesn't match any Radar in the archive")
    if problems:
        raise CheckFailed("blip pages don't look as expected, so files could be incomplete:\n  "
                          + "\n  ".join(problems))

    for blip, timeline in zip(all_blips, timelines):
        if timeline_label(blip["volume_date"]) not in timeline:
            print(f"  Note: {blip['name']} is in the {timeline_label(blip['volume_date'])} "
                  f"Radar according to the search index, but not according to its page "
                  f"({', '.join(timeline)}). It will be included in both.")
    return timelines


def blips_for_volume(all_blips, timelines, year, month):
    """A blip is in a volume if its page history or the search index says so."""
    volume_date = f"{year}-{month:02d}"
    label = timeline_label(volume_date)
    in_volume = []
    for blip, timeline in zip(all_blips, timelines):
        if label in timeline:
            in_volume.append({**blip, "ring": timeline[label]})
        elif blip["volume_date"] == volume_date:
            in_volume.append(blip)
    return in_volume


def render(blips, year, month):
    # Unexpected quadrants and rings get sections of their own, so no blip is ever dropped.
    blips = [{**b, "ring": b["ring"] or "Unknown status"} for b in blips]
    unknown_quadrants = sorted({b["quadrant"] for b in blips} - set(QUADRANTS))
    lines = [f"# Thoughtworks Radar, {calendar.month_name[month]} {year}"]
    for quadrant_key in list(QUADRANTS) + unknown_quadrants:
        in_quadrant = [b for b in blips if b["quadrant"] == quadrant_key]
        if not in_quadrant:
            continue
        quadrant_name = QUADRANTS.get(quadrant_key) or quadrant_key or "Unknown category"
        lines += ["", f"## {quadrant_name}"]
        unknown_rings = sorted({b["ring"] for b in in_quadrant} - set(RINGS))
        for ring in RINGS + unknown_rings:
            in_ring = sorted((b for b in in_quadrant if b["ring"] == ring),
                             key=lambda b: b["name"].lower())
            if not in_ring:
                continue
            lines += ["", f"### {ring}", ""]
            lines += [f"- [ ] [{b['name']}]({b['url']})" for b in in_ring]
    return "\n".join(lines) + "\n"


def parse_selection(text, volume_numbers):
    """Parse input like "1, 3-5" into a sorted list of volume numbers.

    Every number typed must be a published volume. A range selects the
    published volumes within it.
    """
    selected = set()
    for part in text.replace(" ", "").split(","):
        if not part:
            continue
        start, _, end = part.partition("-")
        first, last = int(start), int(end or start)
        if first > last or first not in volume_numbers or last not in volume_numbers:
            raise ValueError(part)
        selected.update(v for v in volume_numbers if first <= v <= last)
    return sorted(selected)


def main():
    print("Looking up published Radars...")
    volumes = list_volumes()
    for vol, year, month in volumes:
        print(f"Vol {vol:2} - {calendar.month_name[month]} {year}")
    volumes_by_number = {vol: (year, month) for vol, year, month in volumes}
    missing = sorted(set(range(1, max(volumes_by_number) + 1)) - set(volumes_by_number))
    if missing:
        print(f"\nWarning: the archive is missing volume{'s' if len(missing) > 1 else ''} "
              f"{', '.join(map(str, missing))}.")

    while True:
        try:
            answer = input("\nWhich volumes? (e.g. 34 or 30,34 or 31-34): ")
        except EOFError:
            return
        try:
            selection = parse_selection(answer, volumes_by_number)
            if selection:
                break
        except ValueError:
            pass
        print("Please enter volume numbers from the list.")

    print("Fetching the blip index...")
    try:
        all_blips = fetch_all_blips()
        timelines = read_all_timelines(all_blips, volumes)
    except CheckFailed as error:
        sys.exit(f"Nothing written: {error}")

    for vol in selection:
        year, month = volumes_by_number[vol]
        blips = blips_for_volume(all_blips, timelines, year, month)
        filename = f"thoughtworks-radar-{year}-{calendar.month_name[month].lower()}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(render(blips, year, month))
        print(f"Vol {vol} ({calendar.month_name[month]} {year}): "
              f"wrote {len(blips)} blips to {filename}")


if __name__ == "__main__":
    try:
        main()
    except Blocked as error:
        sys.exit(f"Nothing written: the site is refusing requests ({error}), probably "
                 "because too many were made recently. Try again later: pages already "
                 "read are cached and won't be read again.")
