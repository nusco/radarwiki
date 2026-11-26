- **Blip:** [Promptfoo](https://www.thoughtworks.com/radar/languages-and-frameworks/promptfoo)
- **Time:** ~1 hour 10 minutes
- **Radar edition:** September 2023 and November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Promptfoo started as a command-line tool for testing prompts against test cases written in YAML, and the Radar put it in *Assess* in 2023. Since then it has grown in two directions: evaluations of whole agents, including their tool calls and CI gates, and red teaming, where it generates attacks against your application and grades the responses. In November 2026 it moves to *Trial* for both. OpenAI now owns Promptfoo, but it stays MIT licensed and works with any model. Some of its advanced attacks run through its hosted service, so check what data leaves your organization.

## Level 1 — What it is (~10 min)

Test your prompts and agents with repeatable evaluations, and attack them before others do.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/promptfoo) (~1 min per version) — read both versions. Note how it complements [[Stateful guardrails]]: guardrails are the runtime control, Promptfoo tests that they hold.

## Level 2 — Evaluate and red-team (~1 hour)

Write an evaluation, then run a red-team scan against an app.

- [ ] **~25 min** · **Do:** Follow [Getting started](https://www.promptfoo.dev/docs/getting-started/) (Promptfoo docs): run the example, then change it to test a prompt of yours against three test cases with assertions. Run it on two models and compare in the web view.
- [ ] **~35 min** · **Do:** Follow the [red team quickstart](https://www.promptfoo.dev/docs/red-team/quickstart/) (Promptfoo docs) against a small app or prompt you control, describing its purpose so the attacks are relevant. Read the report, and pick one failure to fix. Then rerun the scan, as the blip's team did after every fix.

## Wrap-up

This plan covers it. The runtime protections that red teaming checks are covered in [[Stateful guardrails]].

## Review the blip

- [ ] **~5 min** · Re-read [Promptfoo](https://www.thoughtworks.com/radar/languages-and-frameworks/promptfoo) now that you know the topic.

## Related blips

- **[[Stateful guardrails]]**: the runtime control that Promptfoo's red teaming tests.
