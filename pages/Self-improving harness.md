- **Blip:** [Self-improving harness](https://www.thoughtworks.com/radar/techniques/self-improving-harness)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on [[Feedback flywheel]], where people decide how to improve the harness.

---

## Current state (late 2026)

The "harness" is everything around the model: prompts, context strategy, workflows, skills, tools and memory. In 2026 research moved from optimizing prompts automatically to letting agents improve the harness code itself, using execution traces and evaluation results. At the same time, harnesses became easier to change: [[Pi]] has extensions, and Claude Code has mods. The blip is new in November 2026, and it's cautious: the gains need checking, and humans should still set the goals and the limits.

## Level 1 — What it is (~10 min)

Let agents read the traces and evaluation results of past runs, and propose or make improvements to their own harness.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/self-improving-harness) (~3 min) — note the two requirements, observability and programmability, and the advice to run bounded experiments with regression tests.

## Level 2 — How it works (~1 hour)

Learn the main approaches from the overview the blip links to, then try one improvement cycle on your own setup.

- [ ] **~30 min** · Read: [Harness Engineering for Self-Improvement](https://lilianweng.github.io/posts/2026-07-04-harness/) (Lilian Weng, Jul 2026, 31 min for the whole post) — the overview the blip cites, by a well-known AI researcher. Read the introduction, the "Self-Improving Harness" section, and "Future Challenges" (~10 min). The rest is a detailed survey, useful only if you want the research.
- [ ] **~30 min** · **Do:** Collect a few recent sessions with your coding agent where something went wrong. Give them to the agent, and ask it to propose up to three changes to your harness (instructions, a skill, a hook), each with a quick check that would show whether it helped. Apply one change, run the check, and decide whether to keep it. That's one turn of the loop, with you in the role the blip reserves for humans.

## Wrap-up

This plan covers the technique for a generalist. The harnesses that make it possible have their own plans: [[Pi]], [[Claude Code]] and [[DeepSeek Harness (DSH)]].

The blip also links to two research papers, Meta-Harness and VERSE. Weng's overview covers the same ideas, so I left them out.

## Review the blip

- [ ] **~5 min** · Re-read [Self-improving harness](https://www.thoughtworks.com/radar/techniques/self-improving-harness) now that you know the topic.

## Related blips

- **[[DeepSeek Harness (DSH)]]**: one of the harnesses designed to be extended and changed, which makes self-improvement possible.
- **[[Pi]]**: its extensions let agents inspect and change their own harness.
- **[[Feedback flywheel]]**: the human-run version of the same loop.
- **[[Claude Code]]**: its mods are another example of a programmable harness.
