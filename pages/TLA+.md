- **Blip:** [TLA+](https://www.thoughtworks.com/radar/languages-and-frameworks/tla)
- **Time:** ~2 hours 15 minutes
- **Radar edition:** November 2015 and November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

TLA+ is a language for specifying how a system behaves, created by Leslie Lamport in the 1990s. A model checker then explores every possible ordering of events to find states that break your rules, the kind of concurrency bug that tests rarely catch. In 2015 Amazon described how it used TLA+ to find subtle bugs in DynamoDB and other services, and the Radar listed it that year as worth it only for critical systems. It returns in November 2026 because coding agents changed the economics: they can write and update specifications, so the learning curve matters less, and agent-written code needs stronger checks. It's part of a wider trend of "polyglot verification", with [[Mutation testing]] and [[Property-based unit testing]].

## Level 1 — What it is, and why it works (~50 min)

Describe a system's possible behaviors precisely, and let a model checker find the orderings that break it.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/tla) (~2 min) — read both versions. Note why the cost-benefit changed between 2015 and 2026.
- [ ] **~45 min** · Read: [How Amazon Web Services Uses Formal Methods](https://cacm.acm.org/research/how-amazon-web-services-uses-formal-methods/) (Chris Newcombe and others, Communications of the ACM, Apr 2015, ~25 min) — the classic paper, by the AWS engineers who did it. Read the introduction, "First Big Success at Amazon", "What Formal Specification Is Not Good For" and the conclusion. It explains what kind of bugs TLA+ finds, and how they convinced skeptical engineers.

## Level 2 — Write a specification (~1 hour 20 minutes)

Learn how a specification and a model checker work, then find a race condition yourself.

- [ ] **~25 min** · Read: [Conceptual Overview](https://learntla.com/intro/conceptual-overview.html) (Hillel Wayne, Learn TLA+, ~8 min) — from the best free guide to TLA+, by a formal methods consultant. It walks through a bank transfer with a race condition: the spec, the invariant, and how the model checker finds the bug.
- [ ] **~55 min** · **Do:** Install the TLA+ tools (the VS Code extension is the easiest way), and write the bank-transfer example from the overview. Run the model checker and watch it find the race. Then fix the spec and check that the invariant holds. If you get stuck on syntax, ask a coding agent to help, as the blip suggests, but read every line it writes.

## If you have extra time

- [ ] **~1.5 hours** · Read: the "Core" chapters of [Learn TLA+](https://learntla.com/) (Hillel Wayne) — the next step if you want to specify a real system. The guide is free, and goes from the basics to advanced topics.

## Wrap-up

This plan gives you a working grasp of TLA+. Using it on real systems takes more practice, and is worth it only for systems where concurrency bugs are expensive. A friendlier language on the same foundations is covered in [[Quint]].

## Review the blip

- [ ] **~5 min** · Re-read [TLA+](https://www.thoughtworks.com/radar/languages-and-frameworks/tla) now that you know the topic.

## Related blips

- **[[Quint]]**: based on the same logic as TLA+, with friendlier syntax and tooling.
- **[[Mutation testing]]**: another part of the "polyglot verification" trend the blip describes.
- **[[Property-based unit testing]]**: likewise.
