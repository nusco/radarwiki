**Time:** ~3 hours
**Source:** [Thoughtworks Radar – Agent Skills (Trial, April 2026)](https://www.thoughtworks.com/radar/techniques/agent-skills)
**Created:** 2026-10-21

*Series: after [[MCP by default]] · next: [[Context engineering]]. Assumption: you've written the minimal `radar-progress` skill from the MCP by default plan. You also use one non-trivial skill yourself: `learning-plan`.*

---

## Layer 1 — What a skill is (0:00–0:45, ~45 min)

**Goal:** Explain what a skill is (a folder with a `SKILL.md`) and how *progressive disclosure* keeps it cheap until it's needed.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-skills) — short. An open standard that spread fast, with a warning about third-party skills.
- [ ] **Do:** Open `.claude/skills/learning-plan/SKILL.md` in this repository, the skill that writes these plans. Notice the two parts: the frontmatter (a name and a description that the agent always sees), and the body (instructions that load only when the skill is used).
- [ ] Read: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic, Oct 2025, ~10 min) — the original post, by the people who designed skills: why they work this way, and how progressive disclosure keeps them cheap.

## Layer 2 — Write a good one (0:45–2:00, ~75 min)

**Goal:** Turn a quick skill into a well-structured one.

- [ ] Skim: [The specification](https://agentskills.io/specification) — frontmatter fields, and the optional `scripts/`, `references/` and `assets/` folders. You'll use them in the exercise below.
- [ ] Skim: [Extend Claude with skills](https://code.claude.com/docs/en/skills) (Claude Code docs) — read "Configure skills", especially supporting files and who can invoke a skill.
- [ ] **Do:** Improve the `radar-progress` skill. Move the CLI into `scripts/`. Add a `references/` file that describes the Radar file format. Rewrite the description so it says *when* to use the skill. Check that it triggers when you ask a plain-language question. Then review your `learning-plan` skill against the spec: does its description say when to use it, and is anything in it loaded but rarely needed?

## Layer 3 — The risks of other people's skills (2:00–3:00, ~60 min)

**Goal:** Know why you shouldn't install other people's skills without reading them, and what to look for.

- [ ] Read: [ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (Snyk, Feb 2026) — cited by the blip. 13% of nearly 4,000 public skills had critical issues. That's a supply chain problem like the early days of npm.
- [ ] **Do:** Pick a third-party skill you might want, for example from [Anthropic's skills repository](https://github.com/anthropics/skills) or a plugin marketplace. Before installing it, read its `SKILL.md` and every script it ships. Write down what it can read, what it runs, and whether it can send data anywhere.

---

## If you have extra time

- [ ] Watch: [Don't Build Agents, Build Skills Instead](https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills) (Barry Zhang & Mahesh Murag, Anthropic, AI Engineer Code Summit, 16 min).
- [ ] Read: [Evaluating skills](https://agentskills.io/skill-creation/evaluating-skills) — cited by the blip, on how to tell whether a skill actually helps.

---

## Current state of the topic

Anthropic introduced skills in October 2025 and published them as an open standard in December 2025. By the April 2026 Radar, many coding agents and assistants had adopted the format, and skills were shared through plugin marketplaces. Skills are a big part of why the Radar now cautions against [[MCP by default]]. The open problems are quality, since there's little evidence on how well skills work, and security. A skill can carry hidden instructions or scripts, so [[Toxic flow analysis for AI]] and [[Agent Scan]] now cover skills as well as MCP servers.

---

## Recommendation for future learning

This plan covers it for a generalist. Since you already maintain a skill, the best way to go deeper is to keep improving `learning-plan`, perhaps with the skill-creator's evals, rather than to study more.

**Related topics in Thoughtworks Radar:**

- [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (Apr 2026)
- [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) (Apr 2026)
- [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (Apr 2026)
- [Skills as executable onboarding documentation](https://www.thoughtworks.com/radar/techniques/skills-as-executable-onboarding-documentation) (Apr 2026)
- [Claude Code plugin marketplace](https://www.thoughtworks.com/radar/tools/claude-code-plugin-marketplace) (Apr 2026)
- [OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) (Apr 2026)
- [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) (Nov 2025, Apr 2026)
- [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering) (Nov 2025, Apr 2026)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/techniques/agent-skills) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
