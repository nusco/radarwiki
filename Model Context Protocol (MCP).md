**Time:** ~2 hours · **Source:** [Thoughtworks Radar – Model Context Protocol (MCP) (Trial, November 2025)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp)

*Assumption: you use Claude Code (or a similar agent) and can read and write a little Python.*

---

## Layer 1 — What MCP is (0:00–0:15, ~15 min)

**Goal:** Explain in two sentences what MCP is and what problem it solves.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) — Thoughtworks' take: wide adoption, but gaps in architecture and security.
- [ ] Read: [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) — the official one-page intro. It's short.
- [ ] Read: [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (Anthropic, Nov 2024) — the original announcement, with the reasons for creating MCP.

## Layer 2 — How it works (0:15–0:50, ~35 min)

**Goal:** Know the parts (host, client, server), the three server primitives (tools, resources, prompts) and the two transports (stdio and Streamable HTTP).

- [ ] Read: [Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) — the key page. Read the concepts carefully. You can skim the JSON-RPC examples.
- [ ] Read: [Server concepts](https://modelcontextprotocol.io/docs/learn/server-concepts) — when to use a tool, a resource, or a prompt, and who controls each one (the model, the app, or the user).
- [ ] Read: [The Model Context Protocol: Getting beneath the hype](https://www.thoughtworks.com/insights/blog/generative-ai/model-context-protocol-beneath-hype) (Thoughtworks, ~8 min) — linked from the blip. It weighs the benefits against the drawbacks.

## Layer 3 — Build a server (0:50–1:35, ~45 min)

**Goal:** Write a small MCP server, test it on its own, and use it from your agent.

- [ ] Read: [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) — the official quickstart. Follow the Python version.
- [ ] Read: [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) — a tool to call your server by hand, with no LLM in between.
- [ ] Skim: [FastMCP](https://gofastmcp.com/) — the framework the Radar mentions. The official Python SDK's high-level API grew out of it.
- [ ] **Do:** Write a `radar-progress` MCP server with one tool. The tool takes a Radar edition (for example `2025-november`) and returns how many items in `Thoughtworks Radar/thoughtworks-radar-<edition>.md` are ticked and how many aren't. Call it with the Inspector first. Then add it to Claude Code with `claude mcp add` and ask, in plain words, "how far along am I with the November 2025 Radar?"

## Layer 4 — Use it safely (1:35–2:05, ~30 min)

**Goal:** Understand why the Radar says to apply scrutiny, and know how to check an MCP setup.

- [ ] Read: [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) (Simon Willison) — tool poisoning, rug pulls and tool shadowing, explained clearly.
- [ ] Read: [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Simon Willison) — private data plus untrusted content plus a way to send data out. This is the idea behind the Radar's "toxic flows".
- [ ] Skim: [Security best practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) — the official list of attacks and how to prevent them.
- [ ] **Do:** Run [Snyk Agent Scan](https://github.com/snyk/agent-scan) (formerly MCP-Scan, the tool the Radar names) on your agent configuration, including your new `radar-progress` server. Then list every MCP server you have installed and mark which legs of the lethal trifecta each one gives your agent.

---

## If you have extra time

- [ ] [Introduction to Model Context Protocol (MCP)](https://www.pluralsight.com/courses/introduction-model-context-protocol-mcp) (Pluralsight, Tony Alicea, 43 min, updated Jan 2026): covers the same ground as Layers 1–2 as video. Watch it if the reading didn't quite stick.
- [ ] [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) (DeepLearning.AI, free, 1h38): builds servers *and* a client app from scratch. A good next step after Layer 3.
- [ ] [The 2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) (official MCP blog): what changed in the latest spec, and why.
- [ ] [Why MCP's disregard for 40 years of RPC best practices will burn enterprises](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b) (Julien Simon): the critique the Radar quotes. It's on Medium, so it might be behind the paywall.

---

## Current state of MCP

Anthropic released MCP in November 2024. By the time of this blip (November 2025), OpenAI, Google, Microsoft, JetBrains and Apple had adopted it, and it had a preview registry for finding servers. In December 2025, Anthropic donated MCP to the Linux Foundation's Agentic AI Foundation, so it's now a vendor-neutral standard.

The protocol is still changing fast. The newest spec (`2026-07-28`) is the biggest revision so far. It makes the protocol stateless: there's no more session handshake, so remote servers can run behind ordinary load balancers. It also adds official extensions such as *MCP Apps* (interactive UIs inside the chat) and *Tasks* (long-running work), and it brings authorization closer to standard OAuth. Some tutorials from 2025 describe the older session-based protocol. The official docs linked above describe the current one.

MCP has also lost some of its novelty. The April 2026 Radar doesn't list MCP itself any more. Instead, it puts **MCP by default** in *Caution*: it says MCP is often an unnecessary layer, and that a good CLI or an Agent Skill is often simpler and works better. So learn MCP, but treat it as one option among several, not as the default.

---

## Recommendation for future learning

These 2 hours are enough to understand the blip, judge MCP servers, and write simple local ones. If you want to **build and run remote MCP servers in production**, plan another half day (~4 hours) on Streamable HTTP, the [authorization spec](https://modelcontextprotocol.io/docs/tutorials/security/authorization) (OAuth), and deployment. Start that half day with the DeepLearning.AI course above, then take [Model Context Protocol in Practice](https://www.pluralsight.com/courses/model-context-protocol-practice) (Pluralsight, Kamran Ayub, 1h40). It covers local and remote servers and securing them with OAuth. MCP security and A2A are each big enough to study as separate topics.

**Related topics in Thoughtworks Radar:**

- [ ] [Naive API-to-MCP conversion](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) (Nov 2025)
- [ ] [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (Apr 2026)
- [ ] [MCP Apps](https://www.thoughtworks.com/radar/platforms/mcp-apps) (Apr 2026)
- [ ] [FastMCP](https://www.thoughtworks.com/radar/languages-and-frameworks/fastmcp) (Nov 2025)
- [ ] [MCP-Scan](https://www.thoughtworks.com/radar/tools/mcp-scan) (Nov 2025) → [Agent Scan](https://www.thoughtworks.com/radar/tools/agent-scan) (Apr 2026)
- [ ] [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) (Nov 2025, Apr 2026)
- [ ] [Agent-to-Agent (A2A) Protocol](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol) (Nov 2025)
- [ ] [Agent Skills](https://www.thoughtworks.com/radar/techniques/agent-skills) (Apr 2026): an alternative to MCP for many use cases
- [ ] [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering) (Nov 2025, Apr 2026)
- [ ] [Context7](https://www.thoughtworks.com/radar/tools/context7) and [Serena](https://www.thoughtworks.com/radar/tools/serena) (Nov 2025): two popular MCP servers for coding agents
