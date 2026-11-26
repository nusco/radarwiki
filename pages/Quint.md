- **Blip:** [Quint](https://www.thoughtworks.com/radar/languages-and-frameworks/quint)
- **Time:** ~55 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[TLA+]].

---

## Current state (late 2026)

Quint is a specification language from Informal Systems, built on the same logic as TLA+ but with a TypeScript-like syntax and modern tooling: a type checker, a REPL, and a simulator that runs random executions cheaply and can generate test traces for your implementation. Its syntax is easier to review, which matters when agents write the specs. The blip is new in November 2026, and Thoughtworks teams found the choice between Quint and TLA+ a close call: better tooling against more maturity. Informal Systems also sells a commercial product, Quint Studio, but the language and CLI are open source.

## Level 1 — What it is (~5 min)

TLA+'s ideas with a developer-friendly syntax and tools.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/quint) (~1 min) — note the trade-off with TLA+.

## Level 2 — Try it (~50 min)

Install Quint, then compare it with the TLA+ spec you wrote.

- [ ] **~20 min** · Read: [Getting started](https://quint.sh/docs/getting-started) (Quint docs, ~6 min) — installing with npm, a small bank spec, and the three commands: `quint run` to simulate, `--mbt` for model-based testing, and `quint verify` for full checking.
- [ ] **~30 min** · **Do:** Rewrite the bank-transfer spec from the [[TLA+]] exercise in Quint, with the same invariant. Find the race with `quint run`, then fix it. Compare the two specs: which would you rather review in a pull request?

## Wrap-up

This plan covers it. For more, Quint's docs have a series of lessons that start from a simple state machine.

## Review the blip

- [ ] **~5 min** · Re-read [Quint](https://www.thoughtworks.com/radar/languages-and-frameworks/quint) now that you know the topic.

## Related blips

- **[[TLA+]]**: the language whose logic Quint is based on.
