- **Blip:** [Mutation testing](https://www.thoughtworks.com/radar/techniques/mutation-testing)
- **Time:** ~3 hours
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Mutation testing is an old idea, from the 1970s, that stayed academic for decades because it was too slow. Tools like [[Pitest]] (Java) and [[Stryker]] (JavaScript, C#, Scala) made it practical in the 2010s, and Google runs it in code review on changed lines only. What pushed it onto the Radar in 2026 is AI: agents write a lot of tests that pass and raise coverage, but don't check much. Mutation testing measures whether a test suite would notice a bug, so it catches those tests. The technique moved from *Trial* to *Adopt* in six months. Agents can now run it themselves, and use the surviving mutants to write better tests.

## Level 1 — What it is (~20 min)

Mutation testing tests your tests: it plants small bugs in the code, and checks that some test fails.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/mutation-testing) (~2 min) — read both versions. April 2026 explains why coverage isn't enough, and November 2026 adds agents and the cost problem.
- [ ] **~15 min** · Read: [What is mutation testing?](https://stryker-mutator.io/docs/) (Stryker docs, ~5 min) — a short introduction from the Stryker team, with one worked example of mutants, the survivors and the mutation score. It's the clearest short explanation of the vocabulary.

## Level 2 — How it works in practice (~2 hours)

See how mutation testing became fast enough to use, then run it on your own code.

- [ ] **~1.25 hours** · Watch: [How mutation testing got practical](https://archive.fosdem.org/2024/schedule/event/fosdem-2024-2486-how-mutation-testing-got-practical/) (Jan-Jelle Kester, FOSDEM 2024, ~25 min) — a Stryker maintainer on why the technique was impractical for forty years, and the tricks that fixed it, like running only the tests that cover each mutant. The video links are on the page.
- [ ] **~45 min** · **Do:** Run a mutation tool on a small project of yours that has tests: [[Stryker]] for JavaScript or TypeScript, [[Pitest]] for Java, or [[cargo-mutants]] for Rust. Limit the run to one module, so it finishes in minutes. Compare the mutation score with the line coverage, and pick three surviving mutants: for each, decide whether a test is missing, an assertion is too weak, or the mutant doesn't change behavior.

## Level 3 — Mutation testing with AI agents (~45 min)

Use mutation testing as the check on tests that an agent writes, as the November 2026 blip suggests.

- [ ] **~15 min** · Read: [Coverage Lied. Mutation Testing Told the Truth.](https://dev.to/newellpaul/coverage-lied-mutation-testing-told-the-truth-4f8g) (Paul Newell, ~5 min) — a QA engineer runs mutation testing on an AI-written test suite with full coverage, finds 27 survivors out of 95, and has the agent fix them. Pay attention to the section on when the human still has to judge.
- [ ] **~30 min** · **Do:** Take the survivors from Level 2, and ask your coding agent to write tests that kill them. Run the tool again. Did the score go up? Read the new tests: does each one check behavior that matters, or does it only target the mutant?

## If you have extra time

- [ ] **~2.5 hours** · Listen: [SE Radio 632: Goran Petrović on Mutation Testing at Google](https://se-radio.net/2024/09/se-radio-632-goran-petrovic-on-mutation-testing-at-google/) (Gregory M. Kapfhammer, Sep 2024, ~55 min) — how Google made mutation testing work at scale: mutants only on changed lines, shown in code review, with heuristics that drop unproductive mutants. It's the best answer to the blip's worry about cost.
- [ ] **~15 min** · Read: [Introducing LLM-powered bug catchers](https://engineering.fb.com/2025/02/05/security/revolutionizing-software-testing-llm-powered-bug-catchers-meta-ach/) (Mark Harman and others, Meta, Feb 2025, ~5 min) — Meta turns it around: an LLM generates realistic mutants for a specific class of bug, then generates tests that catch them. It's a company announcement, so it's light on numbers.

## Wrap-up

This plan covers the technique. The tools themselves have their own blips, and a tool's plan is the place to go deeper into its configuration.

## Review the blip

- [ ] **~5 min** · Re-read [Mutation testing](https://www.thoughtworks.com/radar/techniques/mutation-testing) now that you know the topic.
