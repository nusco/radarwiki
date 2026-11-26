- **Blip:** [Hindsight](https://www.thoughtworks.com/radar/languages-and-frameworks/hindsight)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Agents forget everything between sessions unless something stores what they learned. Memory systems for agents became a category in 2025, with Mem0 as one of the first. Hindsight, open source from Vectorize, goes further: an LLM extracts facts, entities and dates from conversations into Postgres, recall combines several kinds of search, and a "reflect" step consolidates memories into observations that evolve as new evidence arrives. It can be self-hosted or used as a cloud service. The blip is new in November 2026. Hindsight's benchmark results are its own, and coding agents already have their own memory, so it's most useful for custom-built agents.

## Level 1 — What it is (~10 min)

Long-term memory for agents, which consolidates what it learns instead of just storing facts.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/hindsight) (~2 min) — note the advice: compare it with Mem0, and measure whether the extra LLM calls are worth it.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** Follow the [Quick Start](https://hindsight.vectorize.io/developer/api/quickstart) (Hindsight docs, ~4 min) to run the server locally and use the Python client. Store a few facts about a fictional user over several calls, including one that contradicts an earlier fact. Then recall, and run reflect. Did it notice the contradiction? Note how many LLM calls each step made.

## Wrap-up

This plan covers it. The simpler alternative has its own plan, [[Mem0]].

## Review the blip

- [ ] **~5 min** · Re-read [Hindsight](https://www.thoughtworks.com/radar/languages-and-frameworks/hindsight) now that you know the topic.

## Related blips

- **[[Claude Code]]**: Hindsight has plugins for it, though it already has its own memory across sessions.
- **[[Mem0]]**: a memory system that only extracts and stores facts, without consolidating them.
