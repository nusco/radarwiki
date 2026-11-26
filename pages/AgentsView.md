- **Blip:** [AgentsView](https://www.thoughtworks.com/radar/tools/agentsview)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Context profiling]], the technique that AgentsView supports.

---

## Current state (late 2026)

Coding agents leave session transcripts on disk, but few people look at them. AgentsView is an open-source, local-first tool, released in 2026, that imports those transcripts from dozens of agents into a local database, and shows what each session did and what it cost. The blip is new in November 2026. Thoughtworks likes that it keeps everything on the developer's machine, which makes it easy to adopt in security-conscious organizations. Some features, like recall across sessions, are still experimental.

## Level 1 — What it is (~10 min)

Browse, search and profile your past coding-agent sessions, on your own machine.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/agentsview) (~1 min) — note the contrast with [[Entire CLI]]: AgentsView is local and private by default.
- [ ] **~5 min** · Skim: [AgentsView](https://www.agentsview.io/) (product page) — the sections on recording, cost accounting and feeding results back to agents.

## Level 2 — Profile your sessions (~25 min)

- [ ] **~25 min** · **Do:** Install AgentsView and import your recent sessions. Find your three most expensive sessions, and look at what used the tokens: long contexts, cache misses, big tool outputs? Compare with what you found by hand in the [[Context profiling]] exercise, and note one thing AgentsView showed that `/usage` didn't.

## Wrap-up

This plan covers it. Sharing sessions with a team instead is covered in [[Entire CLI]].

## Review the blip

- [ ] **~5 min** · Re-read [AgentsView](https://www.thoughtworks.com/radar/tools/agentsview) now that you know the topic.

## Related blips

- **[[OpenAI Codex]]**: one of the coding agents whose sessions AgentsView imports.
- **[[OpenCode]]**: another supported agent.
- **[[Pi]]**: another supported agent.
- **[[Context profiling]]**: the technique AgentsView supports, with cost and cache analysis.
- **[[Claude Code]]**: another supported agent.
