- **Blip:** [VictoriaLogs](https://www.thoughtworks.com/radar/platforms/victorialogs)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[VictoriaMetrics]], from the same team.

---

## Current state (late 2026)

Log platforms tend to fall at one of two extremes: search engines like Elasticsearch, powerful but heavy to run, or label-based stores like Grafana Loki, light but dependent on careful label design. VictoriaLogs, from the makers of VictoriaMetrics, sits between them: it stores log fields compactly in blocks, skips unnecessary scans with Bloom filters, and lets you search any field without planning labels up front. It accepts logs in OpenTelemetry, Elasticsearch and Loki formats, so applications don't need to change. The blip is new in November 2026, after a Thoughtworks team used it for an AI cloud platform.

## Level 1 — What it is (~10 min)

A log database that's cheap to run and fast to search, even across arbitrary fields.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/victorialogs) (~2 min) — note the comparison with Elasticsearch and Loki, and the LogsQL query language.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** Follow [Quick Start](https://docs.victoriametrics.com/victorialogs/quickstart/) (VictoriaLogs docs, "Try it locally"): run the binary, send some JSON log lines, and query them in the UI with LogsQL. Then pipe in real logs (the quick start shows how with `journalctl`), and search by a field you'd normally have to grep for.

## Wrap-up

This plan covers it. The label-based alternative is covered in [[Grafana Loki]].

## Review the blip

- [ ] **~5 min** · Re-read [VictoriaLogs](https://www.thoughtworks.com/radar/platforms/victorialogs) now that you know the topic.

## Related blips

- **[[VictoriaMetrics]]**: the metrics database from the same team.
- **[[Grafana Loki]]**: needs more careful label design for high-cardinality logs.
- **[[Grafana]]**: VictoriaLogs integrates with it for exploration and alerting.
- **[[OpenTelemetry]]**: one of the ingestion protocols VictoriaLogs accepts.
