**Time:** ~3 hours 15 minutes
**Radar edition:** April 2026
**Blip:** [Agent Skills](https://www.thoughtworks.com/radar/techniques/agent-skills)
**Quadrant:** Techniques
**Ring:** Trial
**Created:** 2026-10-21

*Assumption: you use one non-trivial skill yourself: the one that writes these plans.*

---

## Level 1 — What a skill is, and why (0:00–0:45, ~45 min)

**Goal:** Explain what a skill is (a folder with a `SKILL.md`), and why *progressive disclosure* makes it cheap until it's needed.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-skills) (~1 min) — an open standard that spread fast, with a warning about third-party skills.
- [ ] **~10 min** · **Do:** Open `.claude/skills/learning-plan/SKILL.md`, the skill that writes these plans. Notice the two parts: the frontmatter (a name and a description that the agent always sees), and the body (instructions that load only when the skill is used).
- [ ] **~30 min** · Read: [Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) (Anthropic, Oct 2025, ~8 min) — the original post, by the people who designed skills. It explains why skills are folders, and the three levels of progressive disclosure: metadata, body, linked files.

## Level 2 — How to write a good one (0:45–2:15, ~90 min)

**Goal:** Write a well-structured skill with scripts and references, and review one you already use.

- [ ] **~10 min** · Skim: [The specification](https://agentskills.io/specification) (~4 min) — skim the frontmatter fields and the optional `scripts/`, `references/` and `assets/` folders. You'll use them in the exercise below.
- [ ] **~30 min** · Read: [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) (Anthropic docs, ~10 min for these sections) — read "Core principles", "Writing effective descriptions" and "Progressive disclosure patterns". It's the most concrete advice on what makes a skill work, especially how to write a description that triggers the skill.
- [ ] **~50 min** · **Do:** Build a full `radar-progress` skill in `.claude/skills/radar-progress/` that answers "how far along am I with a Radar edition?" (Claude Code can help). If you did the exercise in [[MCP by default]], start from the minimal skill you wrote there. Otherwise, start from scratch. Put the script that counts ticked and unticked items in `Thoughtworks Radar/thoughtworks-radar-<edition>.md` into `scripts/`, and add a `references/` file that describes the Radar file format. Write the description so that it says *when* to use the skill, and check that it triggers when you ask a plain-language question. Then review `learning-plan` against the best practices: does its description say when to use it, and does it load anything that it rarely needs?

## Level 3 — The risks of other people's skills (2:15–3:15, ~60 min)

**Goal:** Know why you shouldn't install other people's skills without reading them, and what to look for.

- [ ] **~30 min** · Read: [ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (Snyk, Feb 2026, ~10 min without the IOC tables) — cited by the blip. 13% of nearly 4,000 public skills had critical issues, and 76 were confirmed malicious. That's a supply-chain problem like the early days of npm. The numbers come from a vendor's own scanner, so read them as claims, and don't install anything from the lists of malicious skills.
- [ ] **~30 min** · **Do:** Pick a third-party skill you might want, for example from [Anthropic's skills repository](https://github.com/anthropics/skills) or a plugin marketplace (the blip mentions marketplaces as the way skills get shared and versioned). Before you install it, read its `SKILL.md` and every script it ships. Write down what it can read, what it runs, and whether it can send data anywhere.

---

## If you have extra time

- [ ] **~45 min** · Watch: [Don't Build Agents, Build Skills Instead](https://www.ai.engineer/talks/CEvIs9y1uog-agent-skills) (Barry Zhang & Mahesh Murag, Anthropic, AI Engineer Code Summit, 16 min) — the case for skills as packaged expertise, and how they relate to MCP.
- [ ] **~1 hour** · Watch: [Building Great Agent Skills: The Missing Manual](https://www.ai.engineer/talks/UNzCG3lw6O0-building-great-agent-skills) (Matt Pocock, AI Engineer World's Fair 2026, 21 min) — a practitioner's way to judge a skill: who should invoke it (the model or you), separating steps from references, steering with wording, and pruning instructions that do nothing. It picks up where the best practices leave off, and it's a good lens for reviewing `learning-plan`.
- [ ] **~25 min** · Read: [Evaluating skill output quality](https://agentskills.io/skill-creation/evaluating-skills) (~8 min) — cited by the blip. It shows how to tell whether a skill actually helps: run test cases with and without the skill, and grade the outputs.

---

## Current state of the topic

Anthropic introduced skills in October 2025 and published them as an open standard in December 2025. By the April 2026 Radar, many coding agents and assistants had adopted the format, and skills were shared through plugin marketplaces. Skills are a big part of why the Radar now cautions against [[MCP by default]].

The open problems are quality, since there's little evidence of how well skills work, and security. A skill can carry hidden instructions or scripts, so [[Toxic flow analysis for AI]] and [[Agent Scan]] now cover skills as well as MCP servers.

The blip page now says that Agent Skills isn't in the current Radar edition (a November 2026 edition is out, but it isn't in the `Thoughtworks Radar` folder yet). For a technique that's this widely adopted, dropping off the Radar more likely means it's no longer news than that it has faded.

---

## Recommendation for future learning

This plan covers it for a generalist. Since you already maintain a skill, the best way to go deeper is to keep improving `learning-plan`, perhaps with the skill-creator's evals, rather than to study more.

Related Radar topics:

- [[MCP by default]] (Apr 2026)
- [[Context engineering]] (Nov 2025, Apr 2026)
- [[Toxic flow analysis for AI]] (Nov 2025, Apr 2026)
- [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) (Apr 2026)
- [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (Apr 2026)
- [Skills as executable onboarding documentation](https://www.thoughtworks.com/radar/techniques/skills-as-executable-onboarding-documentation) (Apr 2026)
- [Claude Code plugin marketplace](https://www.thoughtworks.com/radar/tools/claude-code-plugin-marketplace) (Apr 2026)
- [OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) (Apr 2026)

---

- [ ] **~10 min** · **Close:** [Review the blip](https://www.thoughtworks.com/radar/techniques/agent-skills) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
