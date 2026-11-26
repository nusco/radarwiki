- **Blip:** [OpenWiki](https://www.thoughtworks.com/radar/tools/openwiki)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Agent-maintained knowledge bases]], the technique that OpenWiki automates for a codebase.

---

## Current state (late 2026)

OpenWiki is an open-source command-line tool from LangChain that writes and maintains a linked Markdown wiki for a codebase, for agents to use as context. It ties each claim in the wiki back to the source code, so when code changes, it updates only the pages affected. It can run inside a coding agent, standalone, or on a schedule in CI, and it works with local models. The blip is new in November 2026, in *Trial* while Thoughtworks evaluates it on real projects. Other agent-maintained wikis cover anything, while OpenWiki focuses on code.

## Level 1 — What it is (~15 min)

Generate a wiki for a codebase, grounded in the code, and keep it current automatically.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/openwiki) (~1 min) — note the checkpoints that track when each page was last generated.
- [ ] **~10 min** · Skim: [OpenWiki](https://github.com/langchain-ai/openwiki) (LangChain, README) — read the quick start and "How it works", where claims are grounded in evidence from the code.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** Run OpenWiki on a repository you know well (`openwiki --init`, which replaces any wiki it generated before). Open the visualizer, and read three pages about parts of the code you know. Are they right? Then change one function, run an update, and check which pages changed. Decide whether you'd trust it as context for your agent.

## Wrap-up

This plan covers it. Keeping a generated wiki from becoming clutter is covered in [[AI-driven documentation sprawl]], and anchoring agents to a maintained source of conventions in [[Anchoring coding agents to a reference application]].

## Review the blip

- [ ] **~5 min** · Re-read [OpenWiki](https://www.thoughtworks.com/radar/tools/openwiki) now that you know the topic.
