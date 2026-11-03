**Time:** ~1.5 hours
**Source:** [Thoughtworks Radar – Naive API-to-MCP conversion (Hold, November 2025)](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion)
**Created:** 2026-10-21

*Series: after [[Model Context Protocol (MCP)]] · next: [[FastMCP]]. Assumption: you've built the `radar-progress` server from the MCP plan.*

---

## Layer 1 — The anti-pattern (0:00–0:30, ~30 min)

**Goal:** Explain why turning an existing API into MCP tools, one endpoint per tool, gives agents a bad interface.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) — short. APIs are designed for human developers, with many small actions. Agents that chain these actions waste tokens and can reach dangerous operations.
- [ ] Skim: [The FastAPI-MCP README](https://github.com/tadata-org/fastapi_mcp) — one of the converters the blip names. Look at how little code it takes to turn a whole API into MCP tools. That's the temptation.
- [ ] Read: [Stop converting your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp) (Jeremiah Lowin, Jul 2025, ~4 min) — from the author of FastMCP, a framework that itself can do this conversion. Use it to get started quickly, then design curated tools.

## Layer 2 — What a good agent tool looks like (0:30–1:30, ~60 min)

**Goal:** Know the main rules for designing tools for agents, and apply them to your own server.

- [ ] Read: [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (Anthropic, Sep 2025, ~15 min) — linked from the [[Context engineering]] blip. Combine many small operations into a few tools, return information that's meaningful to the agent, keep outputs token-efficient, and write descriptions the way you'd write a prompt.
- [ ] **Do:** Imagine the naive version of `radar-progress`: a file-system API turned into MCP, with `list_files` and `read_file` tools. Write down the calls and tokens an agent would need to answer "how far along am I with the November 2025 Radar?". Then check your real server against Anthropic's rules, and fix one thing. For example, make the error for an unknown edition list the valid ones.

---

## If you have extra time

- [ ] Skim the README of [MCP Link](https://github.com/automation-ai-labs/mcp-link), the other converter the blip names. It turns any OpenAPI spec into an MCP server, even as a hosted service.

---

## Current state of the topic

This entry appeared once, as *Hold*, in November 2025. It isn't in the April 2026 Radar, but its ideas live on in [[MCP by default]], which takes them further: sometimes the best MCP server is no MCP server at all. Converters are still common. FastMCP 3 still includes an OpenAPI provider, but its docs say LLMs work better with curated servers than with converted ones.

---

## Recommendation for future learning

Small, and fully covered here. The design rules are more important than the anti-pattern itself, and they come back in [[Context engineering]].

**Related topics in Thoughtworks Radar:**

- [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) (Apr 2025, Nov 2025)
- [FastMCP](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) (Nov 2025)
- [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (Apr 2026)
- [GraphQL as data access pattern for LLMs](https://www.thoughtworks.com/radar/techniques/graphql-as-data-access-pattern-for-llms) (Nov 2025)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
