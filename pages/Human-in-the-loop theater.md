- **Blip:** [Human-in-the-loop theater](https://www.thoughtworks.com/radar/techniques/human-in-the-loop-theater)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

"Keep a human in the loop" became the standard answer to AI risk. In practice, as agents produce more actions and diffs than anyone can check, the human often clicks "approve" without being able to judge what they approve. The blip, new in November 2026, calls that theater, and borrows the idea of an "accountability sink" from Dan Davies's 2024 book *The Unaccountability Machine*: a structure where a decision has no real owner. It comes with a *Trial* twin, [[Risk-tiered human oversight]], which describes the way out.

## Level 1 — What it is (~20 min)

A human approval step that isn't a real check: the human can't evaluate what they approve, so nobody really owns the decision.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/human-in-the-loop-theater) (~1 min) — note the alternatives it lists for what humans can't review: mutation testing, property-based testing, formal models and semantic review.
- [ ] **~15 min** · Read: [Accountability sinks](https://aworkinglibrary.com/writing/accountability-sinks) (Mandy Brown, Oct 2024, ~5 min) — a reading note on Davies's idea, which the blip uses. It explains how a sink cuts the link between a decision and the people it affects, and argues that AI makes existing sinks worse.

## Level 2 — Find your own theater (~25 min)

- [ ] **~25 min** · **Do:** List the approval steps you take with coding agents in a typical week: permission prompts, plan approvals, diff reviews, merges. For each one, be honest: could you really catch a problem at that step? Mark the ones that are theater. For each, pick a replacement: a deterministic check, a test technique like [[Mutation testing]], a risk tier that removes the step, or a deeper review where it really matters.

Deciding which changes deserve real human review is covered in [[Risk-tiered human oversight]].

## Wrap-up

This plan covers it. The techniques that replace theater have their own plans: [[Mutation testing]], [[Property-based unit testing]], [[TLA+]], [[Quint]] and [[Semantic review of AI-edited prose]].

## Review the blip

- [ ] **~5 min** · Re-read [Human-in-the-loop theater](https://www.thoughtworks.com/radar/techniques/human-in-the-loop-theater) now that you know the topic.

## Related blips

- **[[Meat proxy]]**: the same failure as fake authorship instead of fake approval.
- **[[TLA+]]**: a formal model that steers the system instead of reviewing each change.
- **[[Risk-tiered human oversight]]**: reserves human review for changes a human can really judge.
- **[[Mutation testing]]**: checks tests that no human could review one by one.
- **[[Semantic review of AI-edited prose]]**: agent-assisted review of documents too long to review by hand.
- **[[Quint]]**: another formal modeling language the blip recommends.
