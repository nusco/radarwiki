- **Blip:** [Grilling](https://www.thoughtworks.com/radar/techniques/grilling)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know what [[Agent Skills]] are, and how to install one.

---

## Current state (late 2026)

Grilling became popular in early 2026 through Matt Pocock's `grill-me` skill, a few lines long, which went viral and has been installed over a million times. Many other skill libraries now have their own version. The skill has changed since then: what was a single instruction ("interview me relentlessly") is now a `grilling` skill that asks questions in rounds, and `grill-me` only calls it. Older posts show the earlier text. The technique itself doesn't depend on any skill: you can ask any agent to grill you.

## Level 1 — What it is (~15 min)

Before the agent acts on a plan, it interviews you until no assumption is left unspoken.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/grilling) (~1 min) — note the two benefits: the agent guesses less, and you understand your own plan better.
- [ ] **~10 min** · Read: [My "Grill Me" Skill Went Viral](https://aihero.dev/my-grill-me-skill-has-gone-viral) (Matt Pocock, Mar 2026, ~2 min) — the original skill, and how its author uses it, also outside coding. The line that asks the agent to recommend an answer for each question is what makes sessions fast.

## Level 2 — Get grilled (~45 min)

See how the current skill structures the interview, and use it on a real plan.

- [ ] **~10 min** · Read: [grilling/SKILL.md](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) (Matt Pocock, ~2 min) — the current version, short enough to read in full. Notice the "frontier" (only the questions you can answer now), and the split between facts, which the agent looks up itself, and decisions, which are yours.
- [ ] **~35 min** · **Do:** Install the skill (`npx skills@latest add mattpocock/skills --skill=grill-me --skill=grilling`), or paste its text into your agent. Then run `/grill-me` on a change you're about to make. When the agent says you've reached a shared understanding, write down two assumptions it surfaced that you hadn't stated, and one decision you changed because of a question.

## If you have extra time

- [ ] **~45 min** · Watch: [AI Skills with Matt Pocock](https://newsletter.pragmaticengineer.com/p/ai-skills-with-matt-pocock) (Gergely Orosz, The Pragmatic Engineer, Sep 2026, ~15 min for this part) — start at "Building reusable skills for AI coding agents" (30:32) and stop after "The wayfinder skill". Pocock explains how he uses grilling and related skills to plan and steer agent work.

## Wrap-up

This plan covers it. The library that popularized the technique has its own plan, [[mattpocock-skills|mattpocock/skills]].

## Review the blip

- [ ] **~5 min** · Re-read [Grilling](https://www.thoughtworks.com/radar/techniques/grilling) now that you know the topic.

## Related blips

- **[[mattpocock-skills|mattpocock/skills]]**: the skills library with the best-known grilling skill.
- **[[Codebase cognitive debt]]**: grilling helps counter it, because you keep understanding the plan that the agent implements.
