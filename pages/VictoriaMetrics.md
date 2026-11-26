- **Blip:** [VictoriaMetrics](https://www.thoughtworks.com/radar/platforms/victoriametrics)
- **Time:** ~1 hour
- **Radar edition:** October 2022 and November 2026
- **Quadrant:** Platforms
- **Ring:** Adopt
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what Prometheus does.

---

## Current state (late 2026)

Prometheus became the standard for metrics, but it struggles at large scale: millions of time series ("high cardinality") use a lot of memory, and long retention is costly. VictoriaMetrics is an open-source time-series database that speaks Prometheus's protocols and query language, so it can replace or extend Prometheus without changing instrumentation or dashboards. It comes as a single binary or as a cluster with separate ingestion, query and storage. The Radar put it in *Trial* in 2022 and moves it to *Adopt* in November 2026, after projects handling millions of samples per second. Its sibling for logs is [[VictoriaLogs]].

## Level 1 — Why teams switch (~15 min)

A Prometheus-compatible metrics database that copes with high cardinality and long retention at lower cost.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/victoriametrics) (~1 min) — read both versions. Note the two ways to use it: as long-term storage behind Prometheus, or as the whole metrics stack.
- [ ] **~10 min** · Read: [Prezi's Journey from Prometheus to VictoriaMetrics](https://www.infoq.com/news/2025/02/prezi-prometheus-victoriametrics) (Aditya Kulkarni, InfoQ, Feb 2025, 3 min) — a real migration at about 5 million active series. Note the lesson about clustering across availability zones, which raised costs.

## Level 2 — Try it (~45 min)

- [ ] **~45 min** · **Do:** Follow [Quick start](https://docs.victoriametrics.com/victoriametrics/quick-start/) (VictoriaMetrics docs, "Try it locally"): run the single binary, open its UI, and add a scrape of `node_exporter`. Write a PromQL query you'd use in Prometheus, and check it works unchanged. Then look at memory and disk use after an hour, if you leave it running.

## If you have extra time

- [ ] **~20 min** · Read: [Scaling Observability: Why TiDB Moved from Prometheus to VictoriaMetrics](https://www.pingcap.com/blog/tidb-observability-migrating-prometheus-victoriametrics) (Jack Ma, PingCAP, Jul 2025, ~6 min) — a staged migration with exact settings. It's a company blog, and its performance table isn't a controlled comparison, but the migration steps are useful.

## Wrap-up

This plan covers it for a generalist. Instrumenting applications in a vendor-neutral way is covered in [[OpenTelemetry]].

## Review the blip

- [ ] **~5 min** · Re-read [VictoriaMetrics](https://www.thoughtworks.com/radar/platforms/victoriametrics) now that you know the topic.

## Related blips

- **[[OpenTelemetry]]**: VictoriaMetrics can ingest OpenTelemetry metrics natively.
- **[[Prometheus]]**: VictoriaMetrics supports its APIs, and copes better with high cardinality.
