- **Blip:** [Pi](https://www.thoughtworks.com/radar/tools/pi)
- **Time:** ~2 hours
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you use a coding agent such as Claude Code every day, and you know the basics of [[Agent Skills]] and [[Model Context Protocol (MCP)]].

A single tool would usually get an hour or less, but Pi has become a foundation that other agents are built on (OpenClaw among them), and it's best learned by extending it, which takes time.

---

## Current state (late 2026)

Pi moved from Assess to Trial in November 2026, mostly because other tools now run on it. In April 2026 its creator joined Earendil, which now owns Pi: the repo moved from `badlogic/pi-mono` to `earendil-works/pi`, and the packages from `@mariozechner/...` to `@earendil-works/...`, so older posts show old install commands. Earendil keeps the core MIT-licensed and plans paid add-ons that it hasn't built yet. Pi 1.0 (October 2026) reversed one of Pi's founding choices: MCP is now built in, through a JavaScript sandbox called Codemode. So the blip's "leaves out MCP" is already out of date, while sub-agents and plan mode are still left to extensions. The project still moves fast, and it auto-closes issues and pull requests from new contributors.

## Level 1 — What it is (~20 min)

Run Pi and see how little it ships with.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/pi) (~2 min). Read both versions: April 2026 (Assess) and November 2026 (Trial).
- [ ] **~15 min** · **Do:** Follow [pi.dev](https://pi.dev/)'s instructions to install Pi and connect a model you have access to. In this repo, ask it to explain `Thoughtworks Radar/download-script/radar_to_todo.py`. Done when you've noticed what's missing compared with your usual agent: no permission prompts, no plan mode, no to-do list.

## Level 2 — Why so little (~30 min)

Explain why Pi leaves out the features other agents compete on.

- [ ] **~30 min** · Read: [What I learned building an opinionated and minimal coding agent](https://www.mariozechner.at/posts/2025-11-30-pi-coding-agent/) (Mario Zechner, Nov 2025, ~10 of 25 min) — Pi's creator on why he built it. Read the introduction and the "pi-coding-agent" section, from "Minimal system prompt" to "No sub-agents": that's where he argues against MCP, plan mode, to-dos and permission prompts ("YOLO by default"). Skip the pi-ai and pi-tui sections, unless you're curious how one API can cover many model providers.

## Level 3 — Make it yours (~40 min)

Extend Pi by asking Pi to write the extension.

- [ ] **~15 min** · Read: [Pi: The Minimal Agent Within OpenClaw](https://lucumr.pocoo.org/2026/1/31/pi/) (Armin Ronacher, Jan 2026, ~10 min) — how a heavy user extends Pi: extensions that Pi writes itself, and sessions as trees, so a side quest doesn't pollute the main context. Also explains where OpenClaw fits.
- [ ] **~25 min** · **Do:** Ask Pi to write a project-local extension in `.pi/extensions/` that adds a `/radar <name>` command, which lists the editions in `Thoughtworks Radar` that mention a blip. Point it to the [Quick Start in the extensions docs](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md#quick-start) if it needs an example. Trust the project when Pi asks (project-local extensions load only then), run `/reload`, and try `/radar Pi`. Done when the command works and you've read the code Pi wrote.

## Level 4 — Pi as a foundation (~30 min)

Know how other tools build on Pi, and who now stands behind it.

- [ ] **~10 min** · Read: [I've sold out](https://mariozechner.at/posts/2026-04-08-ive-sold-out/) (Mario Zechner, Apr 2026, ~4 of 15 min) — read only "What does this all mean for pi?": what changed in the ownership, license and governance that the April blip worried about.
- [ ] **~10 min** · Skim: [RPC Mode](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/rpc.md) (Pi docs, ~5 min) — how other programs drive Pi as a subprocess, one of the two ways to embed it (the other is the SDK). Skim the page, then run its minimal Python client to send Pi one prompt.
- [ ] **~10 min** · Skim: [Oh My Pi](https://github.com/can1357/oh-my-pi) (Stencil Labs, README, ~10 min) — the popular fork that adds what Pi leaves out: language servers, a debugger, sub-agents. Skim the feature list, and compare it with what you learned in Level 2.

## If you have extra time

- [ ] **~55 min** · Watch: [Building pi in a World of Slop](https://www.youtube.com/watch?v=RjfbvDXpFls) (Mario Zechner, AI Engineer Europe 2026, 19 min) — the Level 2 argument in talk form, plus what happened to his open-source project once agents started sending it pull requests.
- [ ] **~1 hour** · Watch: [A Piece of Pi – Embedding The OpenClaw Coding Agent In Your Product](https://www.youtube.com/watch?v=vAIDdLKB6-w) (Matthias Luebken, AI Engineer Europe 2026, 21 min) — builds a small business agent on Pi's packages, step by step. Watch it if you'd like to embed an agent in a product of your own.
- [ ] **~20 min** · Read: [You Said No MCP!](https://earendil.com/posts/you-said-no-mcp/) (Earendil Engineering, Sep 2026, ~7 min) — why Pi 1.0 added MCP after all, and what Codemode is. Read it after [[MCP by default]] if you've done that plan.

## Wrap-up

This plan covers Pi for a generalist. If you want more, the closest next step is a plan on a full-featured agent: OpenCode, which the blip suggests for enterprise use, or Claude Code.

**Left out from the blip:** the April version compares Pi with agent frameworks (ADK, LangGraph and Mastra). They're about building agents from scratch, not about Pi, so this plan leaves them out.

## Review the blip

- [ ] **~10 min** · Re-read [Pi](https://www.thoughtworks.com/radar/tools/pi) now that you know the topic.

## Related blips

- **[[OpenCode]]**: another open-source terminal coding agent, which the Radar prefers over Pi as an enterprise coding harness.
