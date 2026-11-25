- **Blip:** [Agent-to-Agent (A2A) Protocol](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol)
- **Time:** ~2 hours
- **Radar edition:** November 2025
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you know MCP, from [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

Google launched A2A in April 2025 and gave it to the Linux Foundation two months later. IBM's competing ACP protocol merged into it in August 2025. Version 1.0, the first stable release, came out in early 2026. By April 2026, the Linux Foundation counted more than 150 supporting organizations and integrations in the big cloud platforms. Still, A2A gets much less attention than MCP. It isn't in the April 2026 or November 2026 Radars, and many multi-agent systems still connect their agents inside a single framework instead of over a protocol. A2A matters most where agents from different vendors or teams need to work together.

## Level 1 — What A2A is for (~45 min)

Explain in two sentences what A2A does and why it complements MCP rather than competing with it.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol) (~1 min) — Agent Cards, long-running tasks, and streaming. MCP connects an agent to its tools, and A2A connects agents to each other.
- [ ] **~40 min** · Read: [Announcing the Agent2Agent Protocol (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) (Rao Surapaneni and others, Google, Apr 2025, ~15 min) — the launch post. Start with its concrete example, "A real-world example: candidate sourcing", where a hiring agent hands work to other agents. Then read the rest for why Google made A2A, and its design principles.

## Level 2 — How it works (~30 min)

Know the main concepts (Agent Card, Task, Message, Part, Artifact) and how agents interact.

- [ ] **~15 min** · Read: [Core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) (A2A docs, ~4 min) — the key page. The blip links to the [GitHub repository](https://github.com/a2aproject/A2A) instead, but the repository points to this documentation site, which is easier to read.
- [ ] **~15 min** · Read: [A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/) (A2A docs, ~5 min) — the official comparison, with a car repair shop example.

## Level 3 — Design an agent card (~45 min)

Practice thinking about what an agent exposes to other agents, compared with what it keeps as its own tools.

- [ ] **~15 min** · Read: [Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/) (A2A docs, ~4 min) — start with "The Role of the Agent Card", which lists what a card contains. Then read the three ways other agents find a card: a well-known URL, a curated registry, or direct configuration.
- [ ] **~30 min** · **Do:** Write the Agent Card (JSON) for an imagined "Radar study buddy" agent that other agents could ask to make or check learning plans. Choose its skills. Then sort its capabilities: which ones would be A2A skills that other agents see, and which would be internal MCP tools or Agent Skills, such as a script that counts your progress through a Radar edition, or the `learning-plan` skill?

## If you have extra time

- [ ] **~4.5 hours** · Watch: [A2A: The Agent2Agent Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) (Holt Skinner, Ivan Nardini and Sandi Besen, DeepLearning.AI with Google Cloud and IBM, updated Apr 2026, 1h27, partly paid) — build A2A servers and clients with code. More than a generalist needs, but it's the best next step if you want hands-on practice.

## Wrap-up

This plan covers it for a generalist. It's not worth more time unless you build multi-agent systems that cross organizational boundaries. In that case, take the DeepLearning.AI course above.

## Review the blip

- [ ] **~10 min** · Re-read [Agent-to-Agent (A2A) Protocol](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: the complementary protocol: MCP connects an agent to tools and data, while A2A connects agents to each other.
