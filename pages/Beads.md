- **Blip:** [Beads](https://www.thoughtworks.com/radar/tools/beads)
- **Time:** ~1 hour 30 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Steve Yegge released Beads in October 2025, as a replacement for the Markdown to-do lists that coding agents write and then lose when their context is compacted. It's an issue tracker made for agents: tasks and their dependencies live in the repository, so agents keep their plans across sessions and can claim work without colliding. It spread fast, and many developers now use it by default, which moved it from *Assess* to *Trial* in November 2026. It also grew heavier: it reached 1.0, moved to the Gas Town Hall organization, and now stores everything in Dolt, a SQL database with Git-like versioning. Versions can't share a store, so teams have to pin one.

## Level 1 — What it is (~1 hour)

A Git-backed issue tracker that agents share, so their plans and discovered tasks survive across sessions.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/beads) (~2 min) — read both versions. November 2026 explains how Beads sits below a team tracker like [[Linear]], and warns about versions and the instructions it writes into `AGENTS.md`.
- [ ] **~55 min** · Read: [Introducing Beads: A coding agent memory system](https://steve-yegge.medium.com/introducing-beads-a-coding-agent-memory-system-637d7d92514a) (Steve Yegge, Oct 2025, 20 min) — the post that launched it, by its author. It's long and chatty, but it explains the problem well: agents lose track of work in Markdown plans, and a dependency graph of issues fixes it. Skim the opening story, and read from where he describes the problem with Markdown plans.

## Level 2 — Use it (~30 min)

Use Beads with your agent across two sessions.

- [ ] **~30 min** · **Do:** Install Beads following the [README](https://github.com/gastownhall/beads) (Quick Start, ~5 min), run `bd init` in a project, and set it up for your agent with `bd setup claude` (or your agent's equivalent). Ask the agent to plan a small feature as Beads issues with dependencies, then work through them across two sessions, clearing the context in between. Check that the second session picks up where the first stopped. Read what Beads added to your `AGENTS.md`.

## Wrap-up

This plan covers it. Planning the work at team level, above Beads, is covered in [[Linear]].

## Review the blip

- [ ] **~5 min** · Re-read [Beads](https://www.thoughtworks.com/radar/tools/beads) now that you know the topic.

## Related blips

- **[[Linear]]**: holds the work a team plans, while Beads holds the finer tasks agents create.
- **[[AGENTS.md]]**: Beads writes instructions into it, which you should review.
