- **Blip:** [Blanket frontier model usage](https://www.thoughtworks.com/radar/techniques/blanket-frontier-model-usage)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Most developers set their coding agent to the most capable model and never change it. As token prices went up in 2026, that habit got expensive: routine work like exploring code, simple edits and summaries doesn't need a frontier model, and smaller or [[Open-weight models|open-weight]] models do it faster and cheaper. Harnesses now make switching easier, with per-subagent models and modes that plan with one model and implement with another. The blip is new in November 2026, and it comes with a caveat: a stronger model sometimes finishes with fewer tokens, so measure.

## Level 1 — What it is (~5 min)

Defaulting every task to the most capable model, whatever its cost, speed and the capability the task actually needs.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/blanket-frontier-model-usage) (~2 min) — note the advice to switch models at natural boundaries, like a new session, a subagent, or the step from planning to implementation, because each model has its own prompt cache.

## Level 2 — Choose models deliberately (~40 min)

Learn how your agent lets you mix models, and try one setup.

- [ ] **~10 min** · Skim: [Model configuration](https://code.claude.com/docs/en/model-config) (Claude Code docs) — look for the `opusplan` alias (plan with Opus, implement with Sonnet), and how to give a subagent a smaller model with the `model` field in its definition.
- [ ] **~30 min** · **Do:** Pick a routine task you do often, like exploring an unfamiliar part of a codebase. Run it once with your usual model, and once with a cheaper one, either by switching with `/model` or with a subagent on a smaller model. Compare the result and `/usage` for each. Decide which kinds of task you'll move to the cheaper model.

Measuring whether a switch actually saves anything is covered in [[Context profiling]].

## Wrap-up

This plan covers it. Running cheaper models yourself is covered in [[Local coding models]].

## Review the blip

- [ ] **~5 min** · Re-read [Blanket frontier model usage](https://www.thoughtworks.com/radar/techniques/blanket-frontier-model-usage) now that you know the topic.

## Related blips

- **[[Subagents for better context management]]**: subagents are a natural place to use a smaller model.
- **[[Open-weight models]]**: often a better fit for routine work than a frontier model.
- **[[Context profiling]]**: the way to check that switching models actually saves tokens.
