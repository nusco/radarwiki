- **Blip:** [Enterprise harness](https://www.thoughtworks.com/radar/techniques/enterprise-harness)
- **Time:** ~1 hour 30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Once several teams in a company use coding agents, the same questions come up in every team: which skills, which MCP servers, which rules on security and architecture? An "enterprise harness" is the shared, organization-wide answer, maintained collectively, like an internal developer platform but for agents. Thoughtworks started talking about it in mid-2026, and the blip is new in November 2026. There's no consensus on how to build one yet: some companies build their own coding agent, while Thoughtworks recommends open standards and a plugin marketplace. Its advice is to keep the enterprise harness thin and federated.

## Level 1 — What it is (~10 min)

The organization-wide layer of what coding agents use: skills, tools, connectors to internal knowledge, approved technologies, decision records, hooks and security policies.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/enterprise-harness) (~2 min) — list what it includes, and note the advice: thin, federated, and harvesting what works in teams.

## Level 2 — How to build one (~1 hour 20 minutes)

Hear how practitioners think about the layers of a harness, and sketch one for an organization you know.

- [ ] **~1 hour** · Listen: [Scaling the enterprise harness](https://www.thoughtworks.com/insights/podcasts/technology-podcasts/scaling-the-enterprise-harness--how-to-achieve-ai-agent-controll) (Ken Mugrage with Thomas Squeo and Matt Kamelman, Thoughtworks, Aug 2026, 45 min) — the podcast the blip links to. Its four layers (the model, the builder's harness, the user's harness, organizational governance) are a useful map. Listen for how they balance central control with team autonomy.
- [ ] **~20 min** · **Do:** For an organization you know, sort ten things that coding agents use into three columns: enterprise (shared by everyone), team, and personal. Include skills, MCP servers, security rules, architecture decisions and instruction files. For each enterprise item, write how it would reach every team, for example through a plugin marketplace.

Distributing the shared assets is covered in [[Agent plugin marketplace]].

## Wrap-up

This plan covers it, as far as anyone knows today. The building blocks have their own plans: [[Curated shared instructions for software teams]], [[Lightweight Architecture Decision Records]] and [[OpenCode]].

## Review the blip

- [ ] **~5 min** · Re-read [Enterprise harness](https://www.thoughtworks.com/radar/techniques/enterprise-harness) now that you know the topic.

## Related blips

- **[[Agent plugin marketplace]]**: the recommended way to distribute an enterprise harness.
- **[[OpenCode]]**: some organizations build a custom coding agent on top of it instead.
- **[[Lightweight Architecture Decision Records]]**: decision records are part of what an enterprise harness shares.
- **[[Curated shared instructions for software teams]]**: the team-level instructions that the enterprise harness complements.
