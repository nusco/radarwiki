**Time:** ~45 minutes
**Radar edition:** November 2025
**Blip:** [Context7](https://www.thoughtworks.com/radar/tools/context7)
**Quadrant:** Tools
**Ring:** Trial
**Created:** 2026-10-21

*Series: after [[Context engineering]] · next: [[Serena]].*

---

## Layer 1 — What it is (0:00–0:15, ~15 min)

**Goal:** Explain how Context7 reduces hallucinated code: it fetches current, version-specific library docs into the context when the agent needs them.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/context7) — short.
- [ ] **Do:** Go to [context7.com](https://context7.com), search for FastMCP, and look at the documentation snippets it serves. That's what Context7 would put into your agent's context.

## Layer 2 — Try it (0:15–0:45, ~30 min)

**Goal:** Use it once, and notice that it's now available as both an MCP server and a CLI with a skill.

- [ ] Skim: [The Context7 README](https://github.com/upstash/context7) — the two modes and how to invoke it.
- [ ] **Do:** Run `npx ctx7 setup --claude` (it needs Node.js 22.13 or later and a free sign-up), and choose the *CLI + Skills* mode. Ask Claude Code "How do I add a resource to a FastMCP 3 server? use context7". Compare the answer with what you wrote in [[FastMCP]].

---

## Current state of the topic

Context7 is one of the most popular MCP servers for coding agents. It isn't in the April 2026 Radar. It now offers a CLI-plus-skill mode next to its MCP server, which is a good example of the shift described in [[MCP by default]]. One thing to watch for: the docs it brings in are third-party content entering your agent's context, so think of it as an untrusted input in [[Toxic flow analysis for AI]].

---

## Recommendation for future learning

This plan covers it.

**Related topics in Thoughtworks Radar:**

- [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering) (Nov 2025, Apr 2026)
- [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) (Apr 2025, Nov 2025)
- [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (Apr 2026)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/tools/context7) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
