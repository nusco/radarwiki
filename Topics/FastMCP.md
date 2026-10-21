**Time:** ~1 hour · **Source:** [Thoughtworks Radar – FastMCP (Trial, November 2025)](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp)

*Series: after [[Naive API-to-MCP conversion]] · next: [[MCP Apps]]. Assumption: you've built the `radar-progress` server from [[Model Context Protocol (MCP)]] with the official Python SDK.*

---

## Layer 1 — Two FastMCPs (0:00–0:20, ~20 min)

**Goal:** Explain the difference between the "FastMCP" inside the official SDK and the standalone FastMCP framework.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) — short. FastMCP 1.0 became part of the official SDK, and the standalone project kept going on its own.
- [ ] Read: [FastMCP welcome page](https://gofastmcp.com/getting-started/welcome) — what the standalone framework adds on top of the SDK: clients, auth, apps, and deployment.

## Layer 2 — Port your server (0:20–1:00, ~40 min)

**Goal:** Move `radar-progress` to standalone FastMCP and use one feature the SDK doesn't have.

- [ ] Read: [Quickstart](https://gofastmcp.com/getting-started/quickstart) — servers, and the Python `Client` for calling them.
- [ ] Skim: [OpenAPI integration](https://gofastmcp.com/integrations/openapi) — note the tip recommending curated servers over converted ones (see [[Naive API-to-MCP conversion]]).
- [ ] **Do:** Port `radar-progress` to standalone FastMCP (for most servers, you only change the import). Add a resource that lists the available Radar editions. Then write a small Python script that uses FastMCP's `Client` to read the resource and call the tool, with no LLM involved.

---

## If you have extra time

- [ ] Skim the [FastMCP changelog](https://gofastmcp.com/updates) for the 3.0 release, to see where the framework is going.

---

## Current state of the topic

FastMCP 3.0 has been stable since February 2026. Its public API is mostly the same as before, but internally it has a new provider/transform design (filesystem, OpenAPI, proxy and skills providers) and it supports MCP Apps. The project moved from its author's personal account to PrefectHQ, and Prefect sells a hosted gateway (Horizon) for running FastMCP servers. FastMCP isn't in the April 2026 Radar. That's not a bad sign: it's an established framework now, not news.

---

## Recommendation for future learning

This plan covers it for a generalist. Go deeper only if you build Python MCP servers for real. In that case, the [DeepLearning.AI MCP course](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) listed in the MCP plan is the next step.

**Related topics in Thoughtworks Radar:**

- [ ] [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) (Apr 2025, Nov 2025)
- [ ] [Naive API-to-MCP conversion](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) (Nov 2025)
- [ ] [MCP Apps](https://www.thoughtworks.com/radar/platforms/mcp-apps) (Apr 2026)
