- **Blip:** [Agent plugin marketplace](https://www.thoughtworks.com/radar/techniques/agent-plugin-marketplace)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know what [[Agent Skills]] are, and that you use Claude Code.

---

## Current state (late 2026)

Anthropic introduced plugins and plugin marketplaces for Claude Code in late 2025: a plugin bundles skills, subagents, hooks and MCP servers, and a marketplace is a Git repository that lists plugins. In 2026 the plugin format spread to other coding agents (see [[Agent Plugins]]), and hosted registries and big community collections appeared. This blip, new in November 2026, is about the organizational side: once several teams use coding agents, they need a way to publish, find and update shared assets, and copying files between repositories doesn't scale.

## Level 1 — What it is (~15 min)

A team or company keeps its shared agent assets as plugins in one Git repository, which every developer's agent can install from and update.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-plugin-marketplace) (~2 min) — note the problem it solves (sharing skills, instructions and MCP servers across teams) and the examples, from Anthropic's original marketplace to hosted registries.
- [ ] **~10 min** · Skim: [wshobson/agents](https://github.com/wshobson/agents) (Seth Hobson) — the community marketplace the blip names, with about ninety plugins. Skim the README and the plugin list to see what a large marketplace looks like, and how one source generates plugins for several agents.

## Level 2 — Build one (~35 min)

Build a small marketplace, and install a plugin from it.

- [ ] **~35 min** · **Do:** Follow [Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace) (Claude Code docs, ~10 min) to build a marketplace in a local folder with one plugin. Put a skill you already use in it, such as the one from the [[Agent Skills]] exercises. Add the marketplace with `/plugin marketplace add`, install the plugin, and check that the skill works. Then change the skill, run `/plugin marketplace update`, and check that the change arrives. That's the update loop a team would rely on.

## Wrap-up

This plan covers the technique. The format and the tools have their own plans: [[Agent Plugins]], [[Claude Code plugin marketplace]] and [[Agent Package Manager]]. What a company would put in its marketplace is the topic of [[Enterprise harness]].

## Review the blip

- [ ] **~5 min** · Re-read [Agent plugin marketplace](https://www.thoughtworks.com/radar/techniques/agent-plugin-marketplace) now that you know the topic.

## Related blips

- **[[Agent Plugins]]**: the plugin format that the marketplace distributes.
- **[[Agent Package Manager]]**: manages plugins from a marketplace as dependencies.
- **[[Enterprise harness]]**: a marketplace is a practical way to make an enterprise harness available across an organization.
- **[[Claude Code plugin marketplace]]**: the implementation that popularized the pattern.
