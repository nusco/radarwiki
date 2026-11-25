- **Blip:** [Subagents for better context management](https://www.thoughtworks.com/radar/techniques/subagents-for-better-context-management)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you've done Levels 1 and 2 of [[Context engineering]], so you know why what stays in the context matters.

---

## Current state (late 2026)

Most coding agents have supported subagents since 2025, and people first used them to run tasks in parallel, or to build "teams" of specialized agents. This blip, new in November 2026, points to a quieter benefit: a subagent keeps its exploration, tool output and retries in its own context, and hands the main agent only a short summary. The evidence is still anecdotal, with no careful token accounting, which is why it's in *Trial*. The same model also behaves differently with subagents in different harnesses.

## Level 1 — What it is (~10 min)

A subagent is a disposable context: send it to do the noisy work, and keep only its conclusion.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/subagents-for-better-context-management) (~2 min) — note the two rules of thumb: two to four subagents at a time, and keep work that needs the same understanding of the code in one agent.
- [ ] **~5 min** · Skim: [Subagents](https://code.claude.com/docs/en/sub-agents) (Claude Code docs, ~3 min for the opening) — read only up to the built-in subagents, to see how a subagent gets its own context window and returns a summary.

## Level 2 — The orchestrator's tax (~1 hour)

Learn why the main agent's context is the scarce resource, and protect it in your own sessions.

- [ ] **~40 min** · Read: [The Orchestrator's Tax](https://martinfowler.com/articles/orchestrator-tax.html) (Rahul Garg, martinfowler.com, Jul 2026, ~14 min) — the article the blip links to. It dissects one real session where checking on background agents flooded the main context with their transcripts, and turns the lesson into four short rules for an instruction file. Note how honest it is about the missing measurements.
- [ ] **~20 min** · **Do:** Pick a task that needs research first, like "find every place this project handles errors from the network, then propose one improvement". Run it twice in a fresh session: once in the main agent, and once telling the agent to send the research to a subagent. Run `/context` at the end of each, and compare how much of the main context the research took.

Measuring the context more carefully is covered in [[Context profiling]], and using cheaper models for subagents in [[Blanket frontier model usage]].

## Wrap-up

This plan covers it. Subagents for parallel work and specialized roles are a separate topic, in [[Team of coding agents]].

## Review the blip

- [ ] **~5 min** · Re-read [Subagents for better context management](https://www.thoughtworks.com/radar/techniques/subagents-for-better-context-management) now that you know the topic.

## Related blips

- **[[Context profiling]]**: the way to check whether subagents actually shrink the orchestrator's context.
- **[[Blanket frontier model usage]]**: subagents on narrow tasks can run on cheaper models instead of a frontier one.
- **[[Context engineering]]**: the blip calls subagents for context protection a form of context engineering.
- **[[Team of coding agents]]**: the more common use of subagents, as a team of agents with different roles.
