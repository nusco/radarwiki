- **Blip:** [Cube Core](https://www.thoughtworks.com/radar/tools/cube-core)
- **Time:** ~55 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know SQL, and roughly what a BI tool does.

---

## Current state (late 2026)

When every dashboard and query defines "revenue" its own way, the numbers drift apart. A semantic layer fixes that by defining metrics, dimensions, joins and access rules once, as code, for every consumer. The idea is old (BI tools have had one built in for decades), and it came back in 2025–2026 because AI agents query data too, and an agent writing SQL against raw tables gets business rules wrong. Cube is one of the main standalone semantic layers, next to dbt's MetricFlow and the warehouses' own semantic views. Cube Core is its open-source (Apache 2.0) version. The company also sells a hosted Cube Cloud, so much of its documentation leads there first.

## Level 1 — What it is (~10 min)

An open-source semantic layer: metrics and their rules defined once as code, served the same way to BI tools, applications and AI agents.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/cube-core) (~1 min) — the problem it solves, duplicated metric definitions and drift.
- [ ] **~5 min** · Read: [Semantic layer](https://www.thoughtworks.com/radar/techniques/semantic-layer) (Radar, Apr 2026, ~2 min) — the technique behind the tool. Note the warning that naive text-to-SQL gets wrong answers when business rules live outside the schema, and the advice to start with one domain.

## Level 2 — Try it (~45 min)

- [ ] **~45 min** · **Do:** Follow [Create a project](https://docs.cube.dev/cube-core/getting-started/create-a-project.md) (Cube Core docs, ~3 min) to start Cube in Docker, and connect it to a small database you have, or a sample one. Define one measure the way your business would (for example, net revenue as amount minus refunds) and one dimension. Query it from the Playground, and look at the SQL that Cube generates. Note the warning in the docs: development mode has no authentication, so keep it on your machine.

## Wrap-up

This plan covers the tool for a generalist. The broader technique has its own plan, [[Semantic layer]].

## Review the blip

- [ ] **~5 min** · Re-read [Cube Core](https://www.thoughtworks.com/radar/tools/cube-core) now that you know the topic.

## Related blips

- **[[Semantic layer]]**: the technique that Cube Core implements.
