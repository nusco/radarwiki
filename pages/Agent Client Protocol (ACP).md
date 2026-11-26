- **Blip:** [Agent Client Protocol (ACP)](https://www.thoughtworks.com/radar/platforms/agent-client-protocol-acp)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

The Zed editor introduced the Agent Client Protocol in August 2025, with Google's Gemini CLI as the first agent to support it. The idea is the same as the Language Server Protocol's: instead of writing a plugin for every pair of editor and agent, both speak one protocol, so any agent works in any editor. JetBrains joined as co-developer, and Claude Code, Codex and others now work through it. It complements MCP: MCP connects an agent to its tools, ACP connects a client (an editor, a terminal, a pipeline) to the agent. Support for remote agents is still in progress. The blip is new in November 2026.

## Level 1 — What it is (~20 min)

A standard protocol between editors and coding agents, so you can swap either one.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/agent-client-protocol-acp) (~1 min) — note the division of labor with MCP.
- [ ] **~10 min** · Read: [Bring Your Own Agent to Zed](https://zed.dev/blog/bring-your-own-agent-to-zed) (Nathan Sobo, Zed, Aug 2025, ~3 min) — the launch post, by Zed's cofounder. Read it for the design: a small set of JSON-RPC messages, with the agent running as a subprocess, instead of scraping a terminal.
- [ ] **~5 min** · Read: [Introduction](https://agentclientprotocol.com/) (ACP site, ~2 min) — the official overview, including what's still unfinished.

## Level 2 — Try it (~20 min)

- [ ] **~20 min** · **Do:** In an editor that supports ACP, such as Zed or a JetBrains IDE, connect the coding agent you use in the terminal. Do the same small task in the editor and in the terminal, and note what the editor integration adds: inline diffs, permission prompts, following the agent through files.

## Wrap-up

This plan covers it. A layer that drives several agents through ACP is covered in [[Omnigent]].

## Review the blip

- [ ] **~5 min** · Re-read [Agent Client Protocol (ACP)](https://www.thoughtworks.com/radar/platforms/agent-client-protocol-acp) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: handles agent-to-tool integration, while ACP handles client-to-agent control.
- **[[Language Server Protocol]]**: the model for ACP, which did the same for editors and language tooling.
