- **Blip:** [Harness quality evaluation](https://www.thoughtworks.com/radar/techniques/harness-quality-evaluation)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know what [[Agent Skills]] and [[AGENTS.md]] are, and that you've used hooks or other checks with a coding agent.

---

## Current state (late 2026)

By 2026 most teams that use coding agents have built a harness around them: instructions, skills, plugins, hooks and checks that keep the agent on track. Those pieces are code, and like any code they can be broken without anyone noticing: a hook that never fires, or a skill that never triggers. The blip is new in November 2026. It splits the problem in two: deterministic parts (hooks, linters, checks) can be tested like any code, while non-deterministic parts (skills, instructions) need evaluations. Tools for both are only starting to appear.

## Level 1 — What it is (~10 min)

Test your agent's harness, so you know that each guardrail actually works.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/harness-quality-evaluation) (~2 min) — note the two kinds of harness components, and the advice to run evaluations on a schedule, nightly or with CI.

## Level 2 — Prove a guardrail can fail (~40 min)

Learn how to test a deterministic guardrail, and test one of yours.

- [ ] **~10 min** · Skim: [Redproof](https://github.com/schalermthai/redproof) (schalermthai) — the test suite tool the blip links to. Skim the README for its core idea: for each guardrail, plant a deliberate violation and check that the guardrail catches it ("red"), and check that clean code passes ("green").
- [ ] **~30 min** · **Do:** Pick one deterministic guardrail in your setup, such as a hook that blocks edits to certain files, a linter rule, or a pre-commit check. Plant a violation that it should catch, and check that it does. Then plant one that's slightly different, like a renamed file or a different syntax, and see whether it still catches it. Write down one guardrail you trusted that turned out weaker than you thought, or note that all of them held.

## If you have extra time

- [ ] **~15 min** · Skim: [PluginEval](https://github.com/wshobson/agents/blob/main/docs/plugin-eval.md) (wshobson/agents, ~12 min in full) — the tool the blip uses for the non-deterministic half: it scores skills and plugins with a static lint, an LLM judge and a simulation. Read the opening and "Status of each layer". Its own docs are candid: the lint is deterministic, while the LLM judge and the simulation are experimental and not yet validated against human judgment.

## Wrap-up

This plan covers the deterministic half well. Evaluating skills and plugins is still immature, as PluginEval's own docs admit. PluginEval is part of the [wshobson/agents](https://github.com/wshobson/agents) collection, which is covered in [[Agent plugin marketplace]].

## Review the blip

- [ ] **~5 min** · Re-read [Harness quality evaluation](https://www.thoughtworks.com/radar/techniques/harness-quality-evaluation) now that you know the topic.

## Related blips

- **[[Agent Skills]]**: one of the non-deterministic parts of a harness that need evaluating.
- **[[AGENTS.md]]**: another part of the harness whose effect should be checked, not assumed.
