- **Blip:** [Claude Managed Agents](https://www.thoughtworks.com/radar/platforms/claude-managed-agents)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Managed agents runtime]], the technique this service implements.

---

## Current state (late 2026)

Anthropic launched Claude Managed Agents as a public beta in April 2026: a hosted service where you define an agent (model, prompt, tools, MCP servers, skills) and Anthropic runs it, with the agent loop, sandbox, scheduling and observability. Agents run on a schedule or when your application starts a session. It's still in beta in late 2026. One Thoughtworks team chose it over other platforms because it was easier to understand. The limits: it only runs Anthropic's harness and Claude models, it charges for runtime on top of tokens, and because it stores sessions it isn't eligible for zero data retention.

## Level 1 — What it is (~20 min)

Anthropic's hosted runtime for general-purpose agents: you define the agent, it runs everything else.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/claude-managed-agents) (~2 min) — note the trade-offs: Claude only, runtime fees, and data handling.
- [ ] **~15 min** · Read: [Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview) (Claude docs, ~6 min) — the four concepts (agent, environment, session, events), how it compares with calling the Messages API yourself, and the availability notes.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Using the console, create an agent for a small recurring task, such as summarizing new issues in a repository every morning. Run one session by hand, and read its events. Then write down what you'd store in files and apply through CI, as the blip suggests, and what it would cost per month at your expected usage.

## Wrap-up

This plan covers it. Running agents on your own infrastructure instead is part of [[Managed agents runtime]].

## Review the blip

- [ ] **~5 min** · Re-read [Claude Managed Agents](https://www.thoughtworks.com/radar/platforms/claude-managed-agents) now that you know the topic.

## Related blips

- **[[Managed agents runtime]]**: the technique this service implements, hosted by Anthropic.
- **[[Amazon Bedrock AgentCore]]**: a comparable service that supports more harnesses and models.
