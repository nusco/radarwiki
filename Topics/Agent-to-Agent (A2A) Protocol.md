**Time:** ~2 hours
**Radar edition:** November 2025
**Blip:** [Agent-to-Agent (A2A) Protocol](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol)
**Quadrant:** Platforms
**Ring:** Assess
**Created:** 2026-10-21

*Assumption: you know MCP from [[Model Context Protocol (MCP)]].*

---

## Layer 1 — What A2A is for (0:00–0:45, ~45 min)

**Goal:** Explain in two sentences what A2A does and why it complements MCP rather than competing with it.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol) — short. Agent Cards, long-running tasks, and streaming. MCP connects an agent to its tools, and A2A connects agents to each other.
- [ ] Read: [Announcing the Agent2Agent Protocol (A2A)](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) (Google, Apr 2025) — the launch post. Start with its concrete example, "A real-world example: candidate sourcing", where a hiring agent hands work to other agents. Then read the rest for why Google made A2A, and its design principles.

## Layer 2 — How it works (0:45–1:35, ~50 min)

**Goal:** Know the main concepts (Agent Card, Task, Message, Part, Artifact) and how agents interact.

- [ ] Read: [Core concepts](https://a2a-protocol.org/latest/topics/key-concepts/) — the key page. The blip links to the [GitHub repository](https://github.com/a2aproject/A2A) instead, but the repository points to this documentation site, which is easier to read.
- [ ] Read: [A2A and MCP](https://a2a-protocol.org/latest/topics/a2a-and-mcp/) — the official comparison, with a car repair shop example.

## Layer 3 — Design an agent card (1:35–2:05, ~30 min)

**Goal:** Practice thinking about what an agent exposes to other agents, compared with what it keeps as its own tools.

- [ ] **Do:** Write the Agent Card (JSON) for an imagined "Radar study buddy" agent that other agents could ask to make or check learning plans. Choose its skills. Then sort its capabilities: which ones would be A2A skills that other agents see, and which would be internal MCP tools or Agent Skills, such as a script that counts your progress through a Radar edition, or the `learning-plan` skill?

---

## If you have extra time

- [ ] [A2A: The Agent2Agent Protocol](https://www.deeplearning.ai/short-courses/a2a-the-agent2agent-protocol/) (DeepLearning.AI with Google Cloud and IBM, 1h27, partly paid) — build A2A servers and clients with code. More than a generalist needs, but it's the best next step if you want hands-on practice.

---

## Current state of the topic

Google launched A2A in April 2025 and gave it to the Linux Foundation two months later. IBM's competing ACP protocol merged into it in August 2025. Version 1.0, the first stable release, came out in early 2026. By April 2026, the Linux Foundation counted more than 150 supporting organizations and integrations in the big cloud platforms. Still, A2A gets much less attention than MCP. It isn't in the April 2026 Radar, and many multi-agent systems still connect their agents inside a single framework instead of over a protocol. A2A matters most where agents from different vendors or teams need to work together.

---

## Recommendation for future learning

This plan covers it for a generalist. It's not worth more time unless you build multi-agent systems that cross organizational boundaries. In that case, take the DeepLearning.AI course above.

---

## Related topics

- [[Model Context Protocol (MCP)]] (Apr 2025, Nov 2025)
- [AG-UI Protocol](https://www.thoughtworks.com/radar/platforms/ag-ui-protocol) (Nov 2025, Apr 2026)
- [Agent Development Kit (ADK)](https://www.thoughtworks.com/radar/languages-and-frameworks/agent-development-kit-adk) (Nov 2025, Apr 2026)
- [Team of coding agents](https://www.thoughtworks.com/radar/techniques/team-of-coding-agents) (Nov 2025, Apr 2026)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/platforms/agent-to-agent-a2a-protocol) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
