- **Blip:** [Context7](https://www.thoughtworks.com/radar/tools/context7)
- **Time:** ~45 minutes
- **Radar edition:** November 2025
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-24
- **Status:** #undone

---

## Current state (late 2026)

Context7 is one of the most popular MCP servers for coding agents. It isn't in the April 2026 or November 2026 Radars. It now offers a CLI-plus-skill mode next to its MCP server, which is a good example of the shift described in [[MCP by default]]. One thing to watch for: the docs it brings in are third-party content entering your agent's context, so think of it as an untrusted input in [[Toxic flow analysis for AI]].

## Level 1 — What it is, and why (~15 min)

Context7 reduces hallucinated code: it fetches current, version-specific library docs into the context when the agent needs them.

- [ ] **~3 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/context7) (~1 min).
- [ ] **~12 min** · **Do:** Go to [context7.com](https://context7.com), search for FastMCP, and look at the documentation snippets it serves. That's what Context7 would put into your agent's context.

## Level 2 — How to use it (~30 min)

Use Context7 once, and notice that it's now available as both an MCP server and a CLI with a skill.

- [ ] **~10 min** · Skim: [The Context7 README](https://github.com/upstash/context7) (~5 min) — the two modes and how to invoke it.
- [ ] **~20 min** · **Do:** Run `npx ctx7 setup --claude` (it needs Node.js 22.13 or later, and signs you in to Context7 to create a free API key), and choose the *CLI + Skills* mode. Ask Claude Code "How do I add a resource to a FastMCP 3 server? use context7". Then ask the same question in a new session without "use context7", and compare the two answers. Does the one without Context7 use an outdated API?

## If you have extra time

- [ ] **~20 min** · Read: [Introducing Context7](https://upstash.com/blog/context7-llmtxt-cursor) (Enes Akar, Upstash, Mar 2025, 6 min) — the launch post. It explains how Context7 parses and ranks docs into snippets, from before it had an MCP server.

## Wrap-up

This plan covers it.

## Review the blip

- [ ] **~10 min** · Re-read [Context7](https://www.thoughtworks.com/radar/tools/context7) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: Context7 is an MCP server, so any agent that speaks MCP can use it.
