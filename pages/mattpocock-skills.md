- **Blip:** [mattpocock/skills](https://www.thoughtworks.com/radar/tools/mattpocock-skills)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Grilling]], which covers the library's best-known skill, and assumes that you know [[Agent Skills]].

---

## Current state (late 2026)

Matt Pocock, a well-known TypeScript educator, published his collection of agent skills in early 2026 as "Skills For Real Engineers". It became one of the most popular skill libraries, mostly thanks to `grill-me`. The skills are deliberately small and composable, and they encode classic engineering practices: align on the plan first, write specs and tickets, test-driven development, code review, and regular architecture cleanups. The blip is new in November 2026. It recommends the library, with a warning: don't adopt any skill library wholesale without reading it.

## Level 1 — What it is (~15 min)

A collection of small agent skills that bring sound engineering practice into agentic coding.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/mattpocock-skills) (~1 min) — note the warning about [[Agent skill cognitive surrender]].
- [ ] **~10 min** · Read: [Skills For Real Engineers](https://github.com/mattpocock/skills) (Matt Pocock, README, ~8 min) — read "Why These Skills Exist", the four ways agentic coding goes wrong and the skill for each, then skim the list of skills.

## Level 2 — Use a few (~45 min)

Adopt the skills one at a time, reading each one first.

- [ ] **~45 min** · **Do:** Pick a small feature. Before installing anything, read the `SKILL.md` of `to-spec`, `tdd` and `code-review`. Install only those (plus `grilling`, if you did the [[Grilling]] plan), and take the feature from a spec to reviewed code with them. Afterwards, decide which skill you'd keep, which you'd adapt to your project, and which you don't need.

## Wrap-up

This plan covers it. Whether to keep using a skill as models improve is part of [[Agent instruction bloat]].

## Review the blip

- [ ] **~5 min** · Re-read [mattpocock/skills](https://www.thoughtworks.com/radar/tools/mattpocock-skills) now that you know the topic.

## Related blips

- **[[Grilling]]**: the technique behind the library's most popular skill.
- **[[Agent skill cognitive surrender]]**: the risk of adopting a whole library like this one without evaluating it.
- **[[Agent Skills]]**: the format the library uses.
