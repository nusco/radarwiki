- **Blip:** [agentgateway](https://www.thoughtworks.com/radar/platforms/agentgateway)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[LiteLLM]], which covers AI gateways for model calls.

---

## Current state (late 2026)

AI gateways started as proxies for model calls. agentgateway, an open-source project hosted by the Linux Foundation, also handles the other kinds of agent traffic: MCP tool calls and agent-to-agent (A2A) messages, with routing, budgets, guardrails and OpenTelemetry tracing in one place. It runs standalone or on Kubernetes. On Kubernetes it can route model requests using GPU metrics, for example to the replica that already holds the right context in its cache. The blip is new in November 2026, aimed mainly at organizations running their own inference.

## Level 1 — What it is (~10 min)

One gateway for model calls, MCP and agent-to-agent traffic.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/agentgateway) (~2 min) — note why Thoughtworks is most interested in the Kubernetes version.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Follow the [LLM quickstart](https://agentgateway.dev/docs/standalone/latest/documentation/quickstart/llm/) (agentgateway docs) to run it locally with one model provider, and send a request through it. Then add an MCP server behind the same gateway, and compare what you can control for tool calls with what [[LiteLLM]] offers for model calls.

## Wrap-up

This plan covers it. The protocol for agent-to-agent traffic has its own plan, [[Agent-to-Agent (A2A) Protocol]].

## Review the blip

- [ ] **~5 min** · Re-read [agentgateway](https://www.thoughtworks.com/radar/platforms/agentgateway) now that you know the topic.

## Related blips

- **[[Agent-to-Agent (A2A) Protocol]]**: one of the kinds of traffic agentgateway governs.
- **[[OpenTelemetry]]**: how agentgateway reports what passes through it.
