- **Blip:** [Tests as data over tests as code](https://www.thoughtworks.com/radar/techniques/tests-as-data-over-tests-as-code)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

The idea is old. Data-driven and table-driven tests are common practice, Go made table-driven tests idiomatic, and BDD tools like Cucumber express tests as structured text. What's new in this November 2026 blip is the reason: coding agents now write many of the tests, and test cases written as data against a fixed schema are easier to generate and much easier to review than pages of test code. Teams have also used it in legacy modernization, running the same test data against the old and the new system. Thoughtworks hasn't applied it widely yet, hence *Assess*.

## Level 1 — What it is (~15 min)

Write test cases as structured data (YAML, JSON, a table), and keep the code in a small project-specific harness that runs them.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/tests-as-data-over-tests-as-code) (~2 min) — note the two benefits: a schema constrains what an agent can generate, and swapping the harness lets the same tests run against two implementations.
- [ ] **~10 min** · Read: [Go Wiki: TableDrivenTests](https://go.dev/wiki/TableDrivenTests) (Go project, ~5 min) — the simplest form of the idea: test cases as a table of inputs and expected outputs, and one loop that runs them. You don't need to know Go to follow the first example.

## Level 2 — Move the data out of the code (~45 min)

Take the next step, with test cases in files, and apply it to your own tests.

- [ ] **~15 min** · Read: [File-driven testing in Go](https://eli.thegreenplace.net/2022/file-driven-testing-in-go/) (Eli Bendersky, Feb 2022, ~4 min) — test cases move into files, and the test discovers them automatically. This is the shape the blip describes: a harness that reads data and runs the code.
- [ ] **~30 min** · **Do:** Pick a test file in one of your projects with many similar tests. Ask your coding agent to turn it into a YAML file of cases plus a small harness that runs them. Then ask it for five new edge cases, as YAML only. Compare reviewing those five cases with reviewing five new test functions: what's easier to spot in the data, and what got harder?

## Wrap-up

This plan covers it. BDD tools such as Cucumber take the idea further, with test cases that non-developers can read and write.

## Review the blip

- [ ] **~5 min** · Re-read [Tests as data over tests as code](https://www.thoughtworks.com/radar/techniques/tests-as-data-over-tests-as-code) now that you know the topic.
