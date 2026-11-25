- **Blip:** [Stacked pull requests](https://www.thoughtworks.com/radar/techniques/stacked-pull-requests)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Stacked changes are old: Facebook's Phabricator and Google's Gerrit worked with chains of small dependent changes long before GitHub. On GitHub they needed third-party tools, until GitHub added native stacked pull requests in 2026. AI coding made them popular, because agents produce large changes fast, and a stack splits them into reviewable pieces. The blip is new in November 2026, and it's in *Caution* not because stacking is bad, but because it often hides a planning problem: work that should have been split into independent pieces in the first place.

## Level 1 — What it is (~20 min)

Split a large change into an ordered chain of small pull requests, each one built on the one below it.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/stacked-pull-requests) (~1 min) — note the reason for *Caution*: stacking doesn't create decomposition problems, it exposes them.
- [ ] **~15 min** · Read: [In Praise of Stacked PRs](https://benjamincongdon.me/blog/2022/07/17/In-Praise-of-Stacked-PRs/) (Ben Congdon, Jul 2022, 4 min) — a short case for stacking from a practitioner: smaller reviews, authors who don't wait, and explicit dependencies.

## Level 2 — Try it, then question it (~30 min)

- [ ] **~30 min** · **Do:** Install GitHub's [gh-stack](https://github.com/github/gh-stack) extension, and use it to split a change of yours (or one your agent wrote) into a stack of two or three pull requests, following the README's quick start. Then ask the blip's question: could these have been independent pull requests, each merged on its own? If yes, write down how you'd have split the work up front.

## If you have extra time

- [ ] **~45 min** · Read: [Stacked Diffs Versus Pull Requests](https://jg.gg/2018/09/29/stacked-diffs-versus-pull-requests/) (Jackson Gabbard, Sep 2018, ~15 min) — the classic argument for stacked diffs, from a former Facebook engineer, with case studies. It's opinionated and long, and it predates AI, but it explains why people who used stacked workflows rarely go back.

## Wrap-up

This plan covers it.

## Review the blip

- [ ] **~5 min** · Re-read [Stacked pull requests](https://www.thoughtworks.com/radar/techniques/stacked-pull-requests) now that you know the topic.
