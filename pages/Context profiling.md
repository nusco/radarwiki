- **Blip:** [Context profiling](https://www.thoughtworks.com/radar/techniques/context-profiling)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you've done Level 3 of [[Context engineering]], where you used `/context` to see what fills your agent's context.

---

## Current state (late 2026)

In 2025 many developers burned tokens freely, and some even competed on how many they used ("tokenmaxxing"). In 2026 prices went up and budgets got tighter, and teams started to ask where their tokens actually go. The answer is often surprising: in long sessions, most of the cost is the same context sent again on every turn, not the code the agent writes. The blip is new in November 2026, and it's in *Assess* because mature tools are still missing. For now, profiling means reading your agent's own usage reports and session logs.

## Level 1 — What it is (~10 min)

Measure where your agent's tokens go before you try to save them, like profiling code before optimizing it.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/context-profiling) (~2 min) — note where the biggest savings usually come from: clearing sessions at the right time, tuning the cache, and quieting chatty build scripts.

## Level 2 — Profile your own sessions (~40 min)

Learn what your agent reports about token use, then find the biggest consumer in your own work.

- [ ] **~10 min** · Skim: [Manage costs effectively](https://code.claude.com/docs/en/costs) (Claude Code docs) — read "Track your costs" and "Why usage climbs in a long session". Note the four kinds of tokens in `/usage` (input, output, cache read, cache write), and why cache reads grow with every turn.
- [ ] **~30 min** · **Do:** At the end of your next three sessions with Claude Code, run `/usage` and `/context`, and note the totals and what filled the context. Find the biggest consumer: a long session that should have been cleared, a chatty tool output, a large file read again and again, or an MCP server you don't use. Make one simple change, and compare the next session.

## Wrap-up

This plan covers it. The fixes that profiling often points to are covered in [[Subagents for better context management]] and [[Blanket frontier model usage]]. What to avoid is in [[Naive context compression]], and tools for deeper analysis in [[Entire CLI]] and [[AgentsView]].

## Review the blip

- [ ] **~5 min** · Re-read [Context profiling](https://www.thoughtworks.com/radar/techniques/context-profiling) now that you know the topic.

## Related blips

- **[[Blanket frontier model usage]]**: model choice is one of the factors that makes intuition a poor guide to cost.
- **[[Entire CLI]]**: one of the tools whose data teams can analyze to profile sessions.
- **[[AgentsView]]**: another source of session data for profiling.
- **[[Naive context compression]]**: a complex fix that developers often reach for without measuring it.
