**Time:** ~1.5 hours
**Radar edition:** November 2025
**Blip:** [FastMCP](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp)
**Quadrant:** Languages & Frameworks
**Ring:** Trial
**Created:** 2026-10-21

*Assumption: you know what MCP tools and resources are, from [[Model Context Protocol (MCP)]], and can read a little Python.*

---

## Layer 1 — Two FastMCPs (0:00–0:30, ~30 min)

**Goal:** Explain the difference between the "FastMCP" inside the official SDK and the standalone FastMCP framework.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) — short. FastMCP 1.0 became part of the official SDK, and the standalone project kept going on its own.
- [ ] **Do:** Put the server example at the top of the [FastMCP welcome page](https://gofastmcp.com/getting-started/welcome), which imports the standalone framework (`from fastmcp import FastMCP`), side by side with the first example in the [official SDK's README](https://github.com/modelcontextprotocol/python-sdk). The code is almost the same. The SDK's version is FastMCP 1.0, and the newest SDK calls it `MCPServer`.
- [ ] Read: [FastMCP welcome page](https://gofastmcp.com/getting-started/welcome) — what the standalone framework adds on top of the SDK: clients, auth, apps, and deployment.

## Layer 2 — Go beyond the SDK (0:30–1:30, ~60 min)

**Goal:** Use standalone FastMCP features that the SDK doesn't have, starting with its Python client.

- [ ] Read: [Quickstart](https://gofastmcp.com/getting-started/quickstart) — servers, and the Python `Client` for calling them.
- [ ] **Do:** Write a small server with standalone FastMCP (Claude Code can help). Give it one tool that takes a Radar edition (for example `2025-november`) and returns how many items in `Thoughtworks Radar/thoughtworks-radar-<edition>.md` are ticked and how many aren't, and one resource that lists the available editions. Then write a small Python script that uses FastMCP's `Client` to read the resource and call the tool, with no LLM involved.

---

## If you have extra time

- [ ] Skim: [OpenAPI integration](https://gofastmcp.com/integrations/openapi) — note the tip recommending curated servers over converted ones (see [[Naive API-to-MCP conversion]]).
- [ ] Skim the [FastMCP changelog](https://gofastmcp.com/updates) for the 3.0 release, to see where the framework is going.

---

## Current state of the topic

FastMCP 3.0 has been stable since February 2026. Its public API is mostly the same as before, but internally it has a new provider/transform design (filesystem, OpenAPI, proxy and skills providers) and it supports MCP Apps. The project moved from its author's personal account to PrefectHQ, and Prefect sells a hosted gateway (Horizon) for running FastMCP servers. FastMCP isn't in the April 2026 Radar. That's not a bad sign: it's an established framework now, not news.

---

## Recommendation for future learning

This plan covers it for a generalist. Go deeper only if you build Python MCP servers for real. In that case, the [DeepLearning.AI MCP course](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) listed in the MCP plan is the next step.

---

## Related topics

- [[Model Context Protocol (MCP)]] (Apr 2025, Nov 2025)
- [[Naive API-to-MCP conversion]] (Nov 2025)
- [[MCP Apps]] (Apr 2026)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
