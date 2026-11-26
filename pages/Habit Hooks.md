- **Blip:** [Habit Hooks](https://www.thoughtworks.com/radar/tools/habit-hooks)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

When a coding agent gets a raw linter error, it often makes the smallest change that silences the rule, without fixing the problem behind it. Habit Hooks is an open-source tool, released in 2026, that runs your existing linters and analyzers, maps each finding to a code smell, and gives the agent guidance on the underlying design problem, deterministically, without an LLM. It's one way to build [[Feedback sensors for coding agents]]. The blip is new in November 2026. The project's claim that it works much better than raw linter output rests on one small study, and it's looking for co-maintainers.

## Level 1 — What it is (~10 min)

Turn linter findings into coaching that steers agents toward fixing the real design problem.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/habit-hooks) (~1 min).
- [ ] **~5 min** · Skim: [Habit Hooks](https://github.com/habit-hooks/habit-hooks) (README, ~11 min in full) — read "Why", "Does it actually work?" and "Sample output". Note that it brings no detectors of its own: it runs the ones you have.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** In a Python or TypeScript project with a linter, install Habit Hooks and run `habit-hooks init`. Plant a code smell, such as a long function or duplicated code, and ask your coding agent to fix the linter warning twice: once with the raw linter output, and once with Habit Hooks' guidance. Compare the two fixes.

## Wrap-up

This plan covers it. The technique it implements has its own plan, [[Feedback sensors for coding agents]].

## Review the blip

- [ ] **~5 min** · Re-read [Habit Hooks](https://www.thoughtworks.com/radar/tools/habit-hooks) now that you know the topic.

## Related blips

- **[[Feedback sensors for coding agents]]**: Habit Hooks is a practical implementation of them.
- **[[Ruff]]**: one of the linters it runs.
- **[[ESLint]]**: another linter it runs.
