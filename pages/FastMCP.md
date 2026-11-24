- **Blip:** [FastMCP](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp)
- **Time:** ~1.5 hours
- **Radar edition:** November 2025
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you know what MCP tools and resources are, from [[Model Context Protocol (MCP)]], and can read a little Python.

---

## Current state (late 2026)

The blip asks you to watch for FastMCP 2.0, but the framework has moved far beyond it. FastMCP 3.0 (February 2026) kept the public API mostly the same, but rebuilt the internals around providers and transforms (filesystem, OpenAPI, proxy and skills providers), and added support for MCP Apps. Releases have kept coming fast since: by November 2026, FastMCP is at version 4.2. The project moved from its author's personal account to PrefectHQ, and Prefect sells a hosted gateway for running FastMCP servers. FastMCP isn't in the April 2026 or November 2026 Radars. That's not a bad sign: it's an established framework now, not news.

## Level 1 — Two FastMCPs (~30 min)

Explain the difference between the "FastMCP" inside the official SDK and the standalone FastMCP framework.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) (~1 min) — FastMCP 1.0 became part of the official SDK, and the standalone project kept going on its own.
- [ ] **~15 min** · **Do:** Put the server example at the top of the [FastMCP welcome page](https://gofastmcp.com/getting-started/welcome), which imports the standalone framework (`from fastmcp import FastMCP`), side by side with the first example in the [official SDK's README](https://github.com/modelcontextprotocol/python-sdk). The code is almost the same. The SDK's version is FastMCP 1.0, and the newest SDK calls it `MCPServer`.
- [ ] **~10 min** · Read: [FastMCP welcome page](https://gofastmcp.com/getting-started/welcome) (FastMCP docs, ~4 min) — what the standalone framework adds on top of the SDK, mainly clients and apps.

## Level 2 — Go beyond the SDK (~60 min)

Use standalone FastMCP features that the SDK doesn't have, starting with its Python client.

- [ ] **~15 min** · Read: [Quickstart](https://gofastmcp.com/getting-started/quickstart) (FastMCP docs, ~5 min) — servers, and the Python `Client` for calling them.
- [ ] **~45 min** · **Do:** Write a small server with standalone FastMCP (Claude Code can help). Give it one tool that takes a Radar edition (for example `2025-november`) and returns how many items in `Thoughtworks Radar/<volume>-thoughtworks-radar-<edition>.md` are ticked and how many aren't, and one resource that lists the available editions. Then write a small Python script that uses FastMCP's `Client` to read the resource and call the tool, with no LLM involved.

## If you have extra time

- [ ] **~15 min** · Skim: [OpenAPI integration](https://gofastmcp.com/integrations/openapi) (FastMCP docs, ~15 min in full) — note the tip recommending curated servers over converted ones (see [[Naive API-to-MCP conversion]]).
- [ ] **~10 min** · Skim: [FastMCP updates](https://gofastmcp.com/updates) (FastMCP docs) — the changelog. Skim the newest entries, to see where the framework is going.

## Wrap-up

This plan covers it for a generalist. Go deeper only if you build Python MCP servers for real. In that case, the [DeepLearning.AI MCP course](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) recommended in the MCP plan is the next step.

## Review the blip

- [ ] **~10 min** · Re-read [FastMCP](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) now that you know the topic.

## Related Radar topics

- [[Model Context Protocol (MCP)]]
- [[Naive API-to-MCP conversion]]
- [[MCP Apps]]
