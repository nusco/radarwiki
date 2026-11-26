- **Blip:** [Restate](https://www.thoughtworks.com/radar/platforms/restate)
- **Time:** ~45 minutes
- **Radar edition:** April 2025, November 2025 and November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Temporal]], which explains durable execution.

---

## Current state (late 2026)

Restate is a durable execution platform from the original creators of Apache Flink, written in Rust and deployed as a single binary. Like Temporal, it records every step of a process so that a failed service resumes where it left off, but its programming model is different: you write services, stateful "virtual objects" and workflows, and Restate sits between them like a proxy. The Radar assessed it in 2025 on a large insurance system, where it's now a core part, and moved it to *Trial* in November 2026. Its SDKs are MIT licensed, but the server uses the Business Source License, which forbids offering it to others as a managed service.

## Level 1 — What it is (~10 min)

A lightweight durable execution platform that journals each step of your services.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/restate) (~1 min per version) — read all three versions. Note the three service types, and the use cases from the insurance project: long processes that wait for people, or retry against legacy systems.

## Level 2 — Compare it with Temporal (~35 min)

- [ ] **~35 min** · **Do:** Run Restate locally following the quickstart on [restate.dev](https://restate.dev/), and rebuild the workflow from the [[Temporal]] exercise: two steps with a wait in between. Kill the service mid-way and restart it. Then compare the two: how much code each needed, how you deploy each, and what the licenses allow.

## Wrap-up

This plan covers it. I left out Restate's own "What is durable execution?" guide: it's mostly marketing, and the Temporal plan already covers the concept.

## Review the blip

- [ ] **~5 min** · Re-read [Restate](https://www.thoughtworks.com/radar/platforms/restate) now that you know the topic.

## Related blips

- **[[Temporal]]**: fills the same role, and moves to *Trial* in the same edition.
