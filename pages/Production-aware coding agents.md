- **Blip:** [Production-aware coding agents](https://www.thoughtworks.com/radar/techniques/production-aware-coding-agents)
- **Time:** ~1 hour 25 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Coding agents usually see only the code, the tests and the build. In 2026 observability vendors started giving them access to production data too, through MCP servers and integrations, so an agent can check how code behaves in production before changing it, and investigate incidents. The blip is new in November 2026, and the tooling is young and mostly vendor-driven. The idea behind it isn't new: developers who know how their code runs in production write better code, and observability advocates have said so for years.

## Level 1 — What it is (~10 min)

Give coding agents appropriate access to production observability, so they can plan changes, check the impact of deployed ones, and help investigate issues.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/production-aware-coding-agents) (~1 min) — note how it extends the agent's feedback: from checks during a session, to the build pipeline, to production.

## Level 2 — Production as feedback (~1 hour 15 minutes)

Understand why production is the real feedback loop for AI-written code, and give your agent a first look at it.

- [ ] **~45 min** · Listen: [Observability for AI with Charity Majors](https://oreilly.com/radar/podcast/generative-ai-in-the-real-world-observability-for-ai-with-charity-majors/) (Ben Lorica with Charity Majors, O'Reilly, Oct 2026, 37 min, ~26 min for this part) — the cofounder of Honeycomb on why cheap code moves the work to understanding how it runs, and why she prefers "owner on the loop" to "human in the loop". Listen from the start, and stop at the takeaway on different telemetry strategies (26:00).
- [ ] **~30 min** · **Do:** Pick a service you work on, and give your coding agent read-only access to one source of production data: a log query CLI, your observability tool's MCP server, or just a log file you download. Ask it to investigate a recent error, and to suggest a fix based on what it finds. Note what the production data told it that the code alone couldn't, and what access you'd be comfortable giving it permanently.

## Wrap-up

This plan covers the technique. The step before production, letting agents see the build, is covered in [[Agent pipeline responsibility]].

I left out the vendor announcement the blip links to as an example of the tooling: it's a press release with little technical content.

## Review the blip

- [ ] **~5 min** · Re-read [Production-aware coding agents](https://www.thoughtworks.com/radar/techniques/production-aware-coding-agents) now that you know the topic.

## Related blips

- **[[Agent pipeline responsibility]]**: a similar recommendation, one step earlier: giving agents the state of the build.
- **[[Feedback sensors for coding agents]]**: the in-session checks that production awareness extends.
