- **Blip:** [Feedback flywheel](https://www.thoughtworks.com/radar/techniques/feedback-flywheel)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you use a coding agent with an instruction file, such as `CLAUDE.md` or [[AGENTS.md]].

---

## Current state (late 2026)

The term comes from a series of articles on martinfowler.com in early 2026, about reducing friction when working with AI. It describes something many developers already did alone: fix the agent's instructions when it gets something wrong. The flywheel turns that into a team habit. The technique moved from *Assess* to *Trial* in November 2026, because editing the harness (instructions, skills, checks) has become routine. Since then, tools have appeared that propose edits from past sessions, and research is trying to let agents run the loop on their own (see [[Self-improving harness]]).

## Level 1 — What it is (~10 min)

After each session with an agent, ask what should change in the team's shared setup, so that lessons compound instead of staying with one developer.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/feedback-flywheel) (~3 min) — read both versions. April 2026 introduces the idea as a retrospective for the harness, and November 2026 adds the warning that the flywheel must remove things, not only add them.

## Level 2 — Make it a team habit (~1 hour)

Learn the practice from the article that named it, and try it on your own sessions.

- [ ] **~35 min** · Read: [Feedback Flywheel](https://martinfowler.com/articles/reduce-friction-ai/feedback-flywheel.html) (Rahul Garg, martinfowler.com, Apr 2026, ~11 min) — the article the blip links to. It sorts the signals from a session into four types, and suggests when to act on each: after a session, at standup, at the retro, and periodically. Notice the advice against building a dashboard.
- [ ] **~25 min** · **Do:** Add one line to your instruction file that asks the agent, at the end of each session, to suggest one change to the shared setup. Use it for your next three sessions. Then review the suggestions: which would you accept, which would you reject, and which existing line would you delete?

Turning the most frequent failures into automatic checks is covered in [[Feedback sensors for coding agents]], and deleting rules that no longer earn their place in [[Agent instruction bloat]].

## If you have extra time

- [ ] **~15 min** · Skim: [backpass](https://github.com/kunchenguid/backpass) (kunchenguid, ~5 min for the opening and "How It Works") — one of the tools the blip mentions. It reads your past session transcripts and proposes edits to your instruction file, with quotes from the sessions as evidence, and changes nothing until you approve. Read its "Limitations" section too.

## Wrap-up

This plan covers it: the technique is a habit, and the rest comes from practice.

## Review the blip

- [ ] **~5 min** · Re-read [Feedback flywheel](https://www.thoughtworks.com/radar/techniques/feedback-flywheel) now that you know the topic.

## Related blips

- **[[Agent instruction bloat]]**: a flywheel that only adds rules ends up with bloated instructions, so it must also delete them.
- **[[Context profiling]]**: shows whether the flywheel's edits make each session load more context.
- **[[Self-improving harness]]**: has an agent run the loop, where the flywheel keeps people choosing which changes to make.
- **[[Agent suggestion box]]**: collects the problems that agents report, as one input to the flywheel.
- **[[Feedback sensors for coding agents]]**: show which checks keep failing, another input to the flywheel.
- **[[AGENTS.md]]**: one of the shared files the flywheel keeps updating.
