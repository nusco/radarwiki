- **Blip:** [Act](https://www.thoughtworks.com/radar/tools/act)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know GitHub Actions, and builds on [[Agent pipeline responsibility]].

---

## Current state (late 2026)

Act runs GitHub Actions workflows locally, and the Radar mentioned it back in 2021, in its GitHub Actions blip. It gets its own blip in November 2026 because of coding agents: they push so often that CI gets congested, and an agent that can run the workflow locally finds failures before it pushes. Act runs each job in a Docker container that imitates GitHub's runners. It's close but not identical: some features are ignored, and the default images lack some tools.

## Level 1 — What it is (~10 min)

Run your GitHub Actions workflows on your own machine, instead of committing, pushing and waiting.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/act) (~1 min) — note the limits (default images, concurrency, permissions, environment secrets) and the pairing with [[zizmor]].
- [ ] **~5 min** · Skim: [act](https://github.com/nektos/act) (README) — how it works: it reads `.github/workflows` and runs each job in a container.

## Level 2 — Use it (~35 min)

Run a real workflow locally, and know where act differs from GitHub.

- [ ] **~5 min** · Skim: [Unsupported functionality](https://nektosact.com/not_supported.html) (act user guide) — the list of what act ignores. Keep it in mind when a workflow passes locally and fails on GitHub.
- [ ] **~30 min** · **Do:** Install act (it needs Docker), and run the workflow of a repository you work on with `act`, or a single job with `act -j <job>`. Then break the workflow on purpose and see how fast you get the failure, compared with pushing. Finally, add a line to your agent's instructions: run `act` before pushing any change to `.github/workflows`.

## Wrap-up

This plan covers it. Checking workflows for security problems is covered in [[zizmor]].

## Review the blip

- [ ] **~5 min** · Re-read [Act](https://www.thoughtworks.com/radar/tools/act) now that you know the topic.

## Related blips

- **[[zizmor]]**: static checks for workflows, which complement running them locally.
- **[[Agent pipeline responsibility]]**: act brings CI into the agent's loop, so it can keep the build green.
- **[[GitHub Actions]]**: the CI platform whose workflows act runs.
