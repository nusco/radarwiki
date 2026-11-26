- **Blip:** [Kagent](https://www.thoughtworks.com/radar/languages-and-frameworks/kagent)
- **Time:** ~45 minutes
- **Radar edition:** November 2025 and November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know the basics of Kubernetes.

---

## Current state (late 2026)

Kagent is an open-source framework and platform for running AI agents on Kubernetes, as standard custom resources: teams deploy, scale and secure agents with the same GitOps pipelines as everything else. It started as a CNCF sandbox project focused on operational agents, which diagnose and fix cluster problems, and the Radar put it in *Assess* in November 2025, warning about the risks of giving an LLM operational powers. In November 2026 it moves to *Trial*, after production use, with sandboxing, OpenTelemetry, memory and built-in MCP and A2A support. Its resource model has changed in recent versions, so older guides may not match.

## Level 1 — What it is (~10 min)

Agents as Kubernetes resources, managed like any other workload.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/kagent) (~2 min per version) — read both versions. Note the client example in 2026: an orchestrator agent with specialists, talking over A2A.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** On a local cluster, install kagent and follow [Your first agent](https://kagent.dev/docs/kagent/1.x/get-started/your-first-agent) (kagent docs, ~5 min): create the resources, start a session and send the agent a task. Then look at the agent's YAML, and decide what you'd need to review before letting an agent like this touch a real cluster. [[Toxic flow analysis for AI]] is a good lens.

## Wrap-up

This plan covers it. The protocols kagent uses have their own plans: [[Model Context Protocol (MCP)]] and [[Agent-to-Agent (A2A) Protocol]].

## Review the blip

- [ ] **~5 min** · Re-read [Kagent](https://www.thoughtworks.com/radar/languages-and-frameworks/kagent) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: kagent integrates MCP natively.
- **[[Agent-to-Agent (A2A) Protocol]]**: kagent's agents talk to each other with it.
- **[[OpenTelemetry]]**: built into kagent's runtime.
- **[[GitOps]]**: how teams deploy kagent's agents.
- **[[Kubernetes]]**: kagent turns agents into its custom resources.
