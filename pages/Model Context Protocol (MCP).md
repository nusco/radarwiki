- **Time:** ~6 hours
- **Radar edition:** November 2025
- **Blip:** [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp)
- **Quadrant:** Platforms
- **Ring:** Trial
- **Created:** 2026-10-19

*Assumption: you use Claude Code (or a similar agent) and can read and write a little Python.*

---

## Current state of the topic (as of 2026-11-15)

Anthropic released MCP in November 2024. By November 2025, OpenAI, Google, Microsoft, JetBrains and Apple had adopted it, and in December 2025 Anthropic donated it to the Linux Foundation's Agentic AI Foundation, so it's now a vendor-neutral standard. The protocol is still changing fast: the newest spec (`2026-07-28`) makes it stateless, with no more session handshake, and adds official extensions such as [[MCP Apps]] and *Tasks* (long-running work). Some tutorials from 2025 describe the older session-based protocol, but the official docs in this plan describe the current one. MCP has also lost some of its novelty. The April 2026 Radar doesn't list MCP itself any more, and puts [[MCP by default]] in *Caution*: a good CLI or an Agent Skill is often simpler and works better. So learn MCP as one option among several, not as the default.

---

## Level 1 — What MCP is (0:00–0:45, ~45 min)

**Goal:** Explain in two sentences what MCP is and what problem it solves.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) — Thoughtworks' take: wide adoption, but gaps in architecture and security.
- [ ] **~15 min** · Read: [What is MCP?](https://modelcontextprotocol.io/docs/getting-started/intro) — the official one-page intro. It's short.
- [ ] **~25 min** · Read: [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) (Anthropic, Nov 2024) — the original announcement, with the reasons for creating MCP.

## Level 2 — How it works (0:45–2:30, ~105 min)

**Goal:** Know the parts (host, client, server), the three server primitives (tools, resources, prompts) and the two transports (stdio and Streamable HTTP).

- [ ] **~45 min** · Read: [Architecture overview](https://modelcontextprotocol.io/docs/learn/architecture) — the key page. Read the concepts carefully. You can skim the JSON-RPC examples.
- [ ] **~30 min** · Read: [Server concepts](https://modelcontextprotocol.io/docs/learn/server-concepts) — when to use a tool, a resource, or a prompt, and who controls each one (the model, the app, or the user).
- [ ] **~30 min** · Read: [The Model Context Protocol: Getting beneath the hype](https://www.thoughtworks.com/insights/blog/generative-ai/model-context-protocol-beneath-hype) (Thoughtworks, ~8 min) — linked from the blip. It weighs the benefits against the drawbacks.

## Level 3 — Build a server (2:30–4:45, ~135 min)

**Goal:** Write a small MCP server, test it on its own, and use it from your agent.

- [ ] **~45 min** · Read: [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) — the official quickstart. Follow the Python version.
- [ ] **~15 min** · Skim: [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) — a tool to call your server by hand, with no LLM in between. Skim the page, then launch the Inspector and click around for a few minutes. You'll use it properly in the exercise below.
- [ ] **~10 min** · Skim: [FastMCP](https://gofastmcp.com/) — the framework the Radar mentions. The official Python SDK's high-level API grew out of it. [[FastMCP]] has its own plan.
- [ ] **~65 min** · **Do:** Write a `radar-progress` MCP server with one tool. The tool takes a Radar edition (for example `2025-november`) and returns how many items in `Thoughtworks Radar/thoughtworks-radar-<edition>.md` are ticked and how many aren't. Call it with the Inspector first. Then add it to Claude Code with `claude mcp add` and ask, in plain words, "how far along am I with the November 2025 Radar?"

## Level 4 — Use it safely (4:45–6:00, ~75 min)

**Goal:** Understand why the Radar says to apply scrutiny, and know how to check the servers you install.

### How agents get attacked

- [ ] **~25 min** · Read: [Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/) (Simon Willison) — tool poisoning, rug pulls and tool shadowing, explained clearly.
- Why some *combinations* of servers are dangerous, the Radar's "toxic flows", is covered in [[Toxic flow analysis for AI]].

### Checking what you install

- [ ] **~15 min** · Read: [Introducing the MCP Registry](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/) (official MCP blog, Sep 2025, ~4 min) — linked from the blip. The official catalog of public MCP servers, still in preview. Notice what it checks (who published a server) and what it leaves to others (whether the server is safe).
- [ ] **~35 min** · **Do:** Run `claude mcp list` to see which servers you have. Besides your new `radar-progress` server, the list may include connectors from your claude.ai account. Pick one server you didn't write, or `radar-progress` if it's the only one, and skim a handful of its tool descriptions in the `/mcp` menu as an attacker would: a description that tells the model what to *do*, rather than what the tool does, is a red flag. Then look up a well-known server in the registry (for example, `curl "https://registry.modelcontextprotocol.io/v0.1/servers?search=filesystem"`). Is it there, and does its namespace match the people you think wrote it?
  - Mapping the trifecta across your whole setup is covered in [[Toxic flow analysis for AI]], and automated scanning in [[Agent Scan]].

---

## If you have extra time

- [ ] **~2 hours** · [Introduction to Model Context Protocol (MCP)](https://www.pluralsight.com/courses/introduction-model-context-protocol-mcp) (Pluralsight, Tony Alicea, 43 min, updated Jan 2026): covers the same ground as Levels 1–2 as video. Watch it if the reading didn't quite stick.
- [ ] **~6 hours** · [MCP: Build Rich-Context AI Apps with Anthropic](https://www.deeplearning.ai/short-courses/mcp-build-rich-context-ai-apps-with-anthropic/) (DeepLearning.AI, free, 1h58): builds servers *and* a client app from scratch. A good next step after Level 3.
- [ ] **~30 min** · [The 2026-07-28 release candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/) (official MCP blog): what changed in the latest spec, and why.
- [ ] **~30 min** · [Why MCP's disregard for 40 years of RPC best practices will burn enterprises](https://julsimon.medium.com/why-mcps-disregard-for-40-years-of-rpc-best-practices-will-burn-enterprises-8ef85ce5bc9b) (Julien Simon): the critique the Radar quotes. It's on Medium, so it might be behind the paywall.

---

## Recommendation for future learning

These 6 hours are enough to understand the blip, judge MCP servers, and write simple local ones. If you want to **build and run remote MCP servers in production**, plan another ~12 hours on Streamable HTTP, the [authorization spec](https://modelcontextprotocol.io/docs/tutorials/security/authorization) (OAuth), and deployment. Start that day with the DeepLearning.AI course above, then take [Model Context Protocol in Practice](https://www.pluralsight.com/courses/model-context-protocol-practice) (Pluralsight, Kamran Ayub, 1h40). It covers local and remote servers and securing them with OAuth. MCP security and A2A have their own plans, listed below.

---

## Related topics

- [[Naive API-to-MCP conversion]] (Nov 2025)
- [[FastMCP]] (Nov 2025)
- [[MCP Apps]] (Apr 2026)
- [[MCP by default]] (Apr 2026)
- [[Agent Skills]] (Apr 2026): an alternative to MCP for many use cases
- [[Context engineering]] (Nov 2025, Apr 2026)
- [[Context7]] (Nov 2025)
- [[Serena]] (Nov 2025)
- [[Toxic flow analysis for AI]] (Nov 2025, Apr 2026)
- [[Agent Scan]] (Apr 2026), formerly MCP-Scan (Nov 2025)
- [[Agent-to-Agent (A2A) Protocol]] (Nov 2025)

---

- [ ] **~10 min** · **Close:** [Review the blip](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
