# Model Context Protocol (MCP)

**Time:** ~2 hours · **Source:** [Thoughtworks Radar – Model Context Protocol (MCP) (Trial, November 2025)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp)

*Assumption: you use Claude Code (or a similar agent) and can read and write a little Python.*

*Note: the blip dates from November 2025, but MCP has kept changing since. The current spec (`2026-07-28`) makes the protocol stateless and deprecates sampling. The official docs below describe the current version.*

---

## Layer 1 — What MCP is (0:00–0:15, ~15 min)

**Goal:** Explain in two sentences what MCP is and what problem it solves.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) — Thoughtworks' take: wide adoption, but rough edges in architecture and security.
- [ ] Read: [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) — the official one-page intro. It's short.
- [ ] Read: [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (Anthropic, Nov 2024) — the original announcement, with the reasons for creating MCP.

## Layer 2 — How it works (0:15–0:50, ~35 min)

**Goal:** Know the parts (host, client, server), the three server primitives (tools, resources, prompts) and the two transports (stdio and Streamable HTTP).

- [ ] Read: [Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) — the key page. Read the concepts carefully. You can skim the JSON-RPC examples.
- [ ] Read: [Server concepts](https://modelcontextprotocol.io/docs/learn/server-concepts) — when to use a tool, a resource, or a prompt, and who controls each one (the model, the app, or the user).
- [ ] Read: [The Model Context Protocol: Getting beneath the hype](https://www.thoughtworks.com/insights/blog/generative-ai/model-context-protocol-beneath-hype) (Karrtik Iyer, Thoughtworks, ~8 min) — linked from the blip. It balances the benefits with the drawbacks.

## Layer 3 — Build a server (0:50–1:35, ~45 min)

**Goal:** Write a small MCP server, test it on its own, and use it from your agent.

- [ ] Read: [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) — the official quickstart. Follow the Python version.
- [ ] Read: [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) — a tool to call your server by hand, with no LLM in between.
- [ ] Skim: [FastMCP](https://gofastmcp.com/) — the framework the Radar mentions (also a [Trial blip](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp)). The official Python SDK's high-level API grew out of it.
- [ ] **Do:** Write a `radar-progress` MCP server with one tool. The tool takes a Radar edition (for example `2025-november`) and returns how many items in `Thoughtworks Radar/thoughtworks-radar-<edition>.md` are ticked and how many aren't. Call it with the Inspector first. Then add it to Claude Code with `claude mcp add` and ask, in plain words, "how far along am I with the November 2025 Radar?"

## Layer 4 — Use it safely (1:35–2:05, ~30 min)

**Goal:** Understand why the Radar says "apply scrutiny", and know how to check an MCP setup.

- [ ] Read: [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) (Simon Willison) — tool poisoning, rug pulls and tool shadowing, explained clearly.
- [ ] Read: [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Simon Willison) — private data plus untrusted content plus a way to send data out. This is the idea behind the Radar's "toxic flows".
- [ ] Skim: [Security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) — the official list of attacks and how to prevent them.
- [ ] **Do:** Run [Snyk Agent Scan](https://github.com/snyk/agent-scan) (this is what used to be MCP-Scan, the tool the Radar names) on your machine's agent configuration, including your new `radar-progress` server. Then list every MCP server you have installed and mark which legs of the lethal trifecta each one gives your agent.

---

## If you have extra time

- [Building Agents with Model Context Protocol – Mahesh Murag, Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg) (1h44, AI Engineer Summit 2025): the full workshop. Watch the first 30–40 minutes for the design ideas behind MCP.
- [Why MCP's disregard for 40 years of RPC best practices will burn enterprises](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b) (Julien Simon): the critique the Radar quotes. It's on Medium, so it might be behind the paywall.
- [Introducing the MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) and [Registry overview](https://modelcontextprotocol.io/registry/about): how clients find servers.
- [Invariant Labs – Tool poisoning attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks): the original research behind the security warnings.
- Related Radar blips: *FastMCP*, *MCP-Scan*, *Agent-to-Agent (A2A) Protocol*, [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai), *Agent Skills* (you studied this one already: it's an alternative to MCP for a lot of use cases).

---

## Recommendation for future learning

These 2 hours are enough to understand the blip, judge MCP servers, and write simple local ones. If you want to **build and run remote MCP servers in production**, plan another half day (~4 hours) on Streamable HTTP, the [authorization spec](https://modelcontextprotocol.io/docs/tutorials/security/authorization) (OAuth), and deployment. MCP security and A2A are both big enough to study as separate topics.
