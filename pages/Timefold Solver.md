- **Blip:** [Timefold Solver](https://www.thoughtworks.com/radar/tools/timefold-solver)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Planning problems like vehicle routing, staff rosters and maintenance schedules have too many possible solutions to try them all. For years the open-source answer in Java was OptaPlanner, a Red Hat project. In 2023 its creators forked it as Timefold Solver, and founded a company around it. It's "AI" in the old sense: no training data and no learned model, just heuristic search over constraints you write as code. The blip is new in November 2026, after Thoughtworks used it in production for supply chain planning. A Python version exists too, though it runs on the JVM under the hood, and some advanced features are commercial.

## Level 1 — What it is (~15 min)

A constraint optimization engine: you describe the planning problem and its rules as code, and it searches for the best plan.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/timefold-solver) (~1 min) — note the difference between hard constraints (rules a plan can't break) and soft constraints (targets to optimize).
- [ ] **~10 min** · Read: [Introduction](https://docs.timefold.ai/timefold-solver/latest/introduction) (Timefold docs, ~2 min) — what a planning problem is, and how hard, medium and soft constraints add up to a score.

## Level 2 — See it on a real problem (~45 min)

See how a planning problem becomes code, and model one of your own.

- [ ] **~15 min** · Read: [Optimize routing and scheduling in Python](https://timefold.ai/blog/new-open-source-solver-python) (Geoffrey De Smet, Timefold, ~4 min) — the cofounder shows how an employee schedule and a vehicle route are modeled as classes, with constraints as code that you can unit test. It's a launch post: skip the cost-saving claims, and read the code.
- [ ] **~30 min** · **Do:** Pick a small planning problem you know, like a team's on-call rota or a weekly class timetable. Write down its planning entities, what the solver changes, and its constraints, sorted into hard and soft. If you want to go further, run one of Timefold's quickstart examples and add one of your constraints to it.

## Wrap-up

This plan is enough for a generalist. Constraint solving is a field of its own (operations research), worth a separate study if you work on logistics or scheduling.

## Review the blip

- [ ] **~5 min** · Re-read [Timefold Solver](https://www.thoughtworks.com/radar/tools/timefold-solver) now that you know the topic.
