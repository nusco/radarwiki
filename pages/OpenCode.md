- **Blip:** [OpenCode](https://www.thoughtworks.com/radar/tools/opencode)
- **Time:** ~1 hour 10 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Adopt
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you use another coding agent, such as Claude Code, and focuses on what's different about OpenCode.

---

## Current state (late 2026)

OpenCode is an open-source (MIT), terminal-first coding agent from the team behind SST, the Serverless Stack framework. It became one of the most popular coding agents in 2025–2026, mostly because it works with almost any model: hosted frontier models, existing subscriptions, self-hosted endpoints and local models. The Radar put it in *Assess* in April 2026 and moved it straight to *Adopt* in November 2026, as more teams paired it with open-weight models. Version 2 arrived in 2026, with a new install path, so older guides show outdated commands and configuration. Its weak spot is collaboration: sharing sessions lags behind other harnesses.

## Level 1 — What it is (~15 min)

An open-source coding agent with a strong terminal experience, any model you like, and a server mode that makes it a base for your own harness.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/opencode) (~2 min) — read both versions. Note what the November version values: customizability, and a headless server mode for building an [[Enterprise harness]].
- [ ] **~10 min** · Read: [OpenCode: an Open-source AI Coding Agent Competing with Claude Code and Copilot](https://www.infoq.com/news/2026/02/opencode-coding-agent) (Sergio De Simone, InfoQ, Feb 2026, 2 min) — a short overview of what sets it apart: dozens of model providers, language servers, MCP, and editor integrations. It's a news piece, so read it for the map, not for an evaluation.

## Level 2 — Use it (~55 min)

Install OpenCode, connect a model your other agent can't use, and run it headless.

- [ ] **~10 min** · Skim: [OpenCode docs](https://opencode.ai/docs/) (OpenCode, intro) — the install options and how to connect a provider. Use the v2 instructions on this page, not older guides.
- [ ] **~45 min** · **Do:** Install OpenCode in a repository that has an `AGENTS.md`, and connect a model you don't normally use, such as an open-weight model from [[Open-weight models]] or a local one from [[Local coding models]]. Give it a small, well-defined task. Then run the same task headless from a script, the way a team would build it into a pipeline. Compare it with your usual agent: where does the model matter, and where does the harness?

## Wrap-up

This plan covers it for someone who already uses a coding agent. The blip also mentions Oh My OpenCode, a more opinionated add-on with teams of agents. Start with plain OpenCode before deciding you need it. A minimal alternative to OpenCode is covered in [[Pi]].

## Review the blip

- [ ] **~5 min** · Re-read [OpenCode](https://www.thoughtworks.com/radar/tools/opencode) now that you know the topic.

## Related blips

- **[[Enterprise harness]]**: OpenCode's customizability and server mode make it a foundation for one.
- **[[Pi]]**: an emerging alternative that the blip recommends evaluating too.
- **[[Open-weight models]]**: OpenCode is a popular way to use them with a coding agent.
- **[[Local coding models]]**: likewise, for models running on your own machine.
