- **Blip:** [Temporal](https://www.thoughtworks.com/radar/platforms/temporal)
- **Time:** ~1 hour 20 minutes
- **Radar edition:** March 2022 and November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Temporal started in 2019 as a fork of Cadence, Uber's open-source workflow engine, by Cadence's original authors. It popularized "durable execution": code that survives crashes, restarts and long waits, because the platform records every step and can replay it. The Radar first covered it in 2022 (*Assess*), cautiously, as a tool for the rare cases where distributed transactions can't be avoided. In November 2026 it moves to *Trial*, with a new use: control planes for AI infrastructure, where many long provisioning tasks need retries and reconciliation. It's available as open source to self-host, or as a managed cloud service. Restate fills a similar role (see [[Restate]]).

## Level 1 — What it is (~35 min)

Write long-running business processes as ordinary code, and let the platform make them survive failures.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/temporal) (~1 min) — read both versions. Notice the change in tone, from "only if you really need distributed transactions" (2022) to concrete use cases (2026).
- [ ] **~30 min** · Read: [The definitive guide to Durable Execution](https://temporal.io/blog/what-is-durable-execution) (Tom Wheeler, Temporal, May 2025, 10 min) — an explanation of durable execution with a worked failure example, by a Temporal engineer. It's written by the vendor, so it doesn't discuss the trade-offs: workflow code must be deterministic, and you run (or pay for) one more platform.

## Level 2 — See a workflow survive a crash (~45 min)

- [ ] **~45 min** · **Do:** Install the Temporal CLI and start a local server with `temporal server start-dev`. Follow Temporal's getting-started tutorial for a language you know, and run a workflow with two activities and a sleep between them. While it sleeps, kill the worker process, then start it again, and watch in the web UI how the workflow picks up where it stopped. Note what code you didn't have to write.

## Wrap-up

This plan is enough for a generalist. Distributed transactions in general, and the Saga pattern that Temporal is often used for, are worth their own study if you build microservices.

## Review the blip

- [ ] **~5 min** · Re-read [Temporal](https://www.thoughtworks.com/radar/platforms/temporal) now that you know the topic.
