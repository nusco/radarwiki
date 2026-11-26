- **Blip:** [AWS DevOps Agent](https://www.thoughtworks.com/radar/platforms/aws-devops-agent)
- **Time:** ~25 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

AWS DevOps Agent is a managed AWS service, generally available since March 2026, that investigates incidents. When an alarm, ticket or chat message triggers it, it maps the affected resources, correlates telemetry with recent deployments and code changes, tests hypotheses, and proposes likely root causes and fixes for an engineer to act on. It connects to the usual monitoring and ticketing tools, and to custom systems through MCP. Thoughtworks teams are trying it on live alarms with promising results. The main worry is cost: it charges per second of agent time, which is hard to predict.

## Level 1 — What it is (~10 min)

A managed agent that investigates production incidents and proposes root causes.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/aws-devops-agent) (~2 min) — note the three safeguards it recommends: a human validates every finding, tight control over what triggers an investigation, and active cost tracking.

## Level 2 — Decide where it fits (~15 min)

- [ ] **~15 min** · **Do:** Think of the last production incident you were involved in. Write down the steps of the investigation, and mark which ones an agent like this could have done, which needed a person, and which data it would have needed access to. Then write the rule you'd use to decide which alarms may trigger an investigation.

## Wrap-up

This plan is enough unless you run on AWS. The general technique, agents with access to production data, is covered in [[Production-aware coding agents]]. I didn't add AWS's product page, which is marketing.

## Review the blip

- [ ] **~5 min** · Re-read [AWS DevOps Agent](https://www.thoughtworks.com/radar/platforms/aws-devops-agent) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: how the agent reaches monitoring tools and custom systems.
