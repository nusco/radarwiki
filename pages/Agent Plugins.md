- **Blip:** [Agent Plugins](https://www.thoughtworks.com/radar/platforms/agent-plugins)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know [[Agent Skills]] and [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

By 2026 every coding agent had its own way to package extensions: Claude Code plugins, Codex plugins, Cursor's, and more. Agent Plugins is an open, vendor-neutral standard for one portable package: a directory with a manifest, skills and MCP server definitions, plus room for agent-specific extensions. Its first version (1.0) came from a collaboration including Amazon, Microsoft, OpenAI, Cursor and Vercel. The spec is deliberately minimal. The blip is new in November 2026, and Thoughtworks found it easy to turn an existing skills repository into a plugin.

## Level 1 — What it is (~10 min)

A standard package format for agent skills and MCP servers, that works across coding agents.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/agent-plugins) (~1 min).
- [ ] **~5 min** · Read: [Agent Plugins](https://agent-plugins.org/) (spec site, ~2 min) — the package layout: `plugin.json`, a `skills/` folder and `mcp.json`.

## Level 2 — Make one (~20 min)

- [ ] **~20 min** · **Do:** Take a skill you've written, such as the one from the [[Agent Skills]] exercises, and package it as an Agent Plugin following the spec's layout. Install it in two different coding agents, and note what each needed beyond the standard.

## Wrap-up

This plan covers it. Sharing plugins across a company is covered in [[Agent plugin marketplace]], and managing them as dependencies in [[Agent Package Manager]].

## Review the blip

- [ ] **~5 min** · Re-read [Agent Plugins](https://www.thoughtworks.com/radar/platforms/agent-plugins) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: MCP servers are one of the two things a plugin packages.
- **[[Agent Skills]]**: skills are the other, and a skills repository can double as a plugin.
