- **Blip:** [Coding harness for general-purpose agents](https://www.thoughtworks.com/radar/techniques/coding-harness-for-general-purpose-agents)
- **Time:** ~1.5 hours
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you've used a coding agent such as Claude Code, and that you know what [[Agent Skills]] are.

---

## Current state (late 2026)

In September 2025 Anthropic renamed the Claude Code SDK to the Claude Agent SDK, to say that the harness behind its coding agent could power any kind of agent. Other coding agents followed: Codex, OpenCode and [[Pi]] all expose their runtime as an SDK or server. In 2026, teams building agents for work that isn't coding, like document processing or operations support, started to build on these harnesses instead of assembling an agent loop from a framework. The blip is new in November 2026. The choice between a coding harness and an agent framework is still open, and depends on how much control you need.

## Level 1 — What it is (~45 min)

A mature coding agent already solves the hard parts of any agent, like context compaction, sessions, tools and skills, so you can reuse it for agents that don't write code.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/coding-harness-for-general-purpose-agents) (~2 min) — note the two warnings: the built-in prompts push agents toward writing code, and coding-agent loops use many tokens.
- [ ] **~40 min** · Read: [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) (Thariq Shihipar, Anthropic, Sep 2025, 14 min) — the post that started the trend. Its main idea is "give your agents a computer", and it describes the agent loop (gather context, act, verify) through an example email agent. Read it as a design guide, not as a product announcement.

## Level 2 — Build one (~45 min)

Turn a coding harness into an agent for a non-coding task.

- [ ] **~45 min** · **Do:** Follow the [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview) to its quickstart, and get the example agent running. Then change it into an agent for a task that isn't coding, such as "read the meeting notes in this folder and write a list of open decisions". Change the system prompt and the allowed tools, and note what the coding defaults did that you didn't want. If you prefer a minimal harness, do the same with Pi's SDK (see [[Pi]]).

## Wrap-up

This plan covers the technique. The alternative, building on an agent framework, gives you more control at the cost of more work, and each framework has its own blip.

I left out OpenAI's "Codex as a platform" post, which the blip links to: it's mostly a product pitch, and the Anthropic post covers the same idea in more depth.

## Review the blip

- [ ] **~5 min** · Re-read [Coding harness for general-purpose agents](https://www.thoughtworks.com/radar/techniques/coding-harness-for-general-purpose-agents) now that you know the topic.

## Related blips

- **[[Agent Skills]]**: a coding harness runs the same skills headless as in interactive sessions.
