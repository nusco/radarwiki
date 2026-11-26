- **Blip:** [OpenResearch CLI (orx)](https://www.thoughtworks.com/radar/tools/openresearch-cli-orx)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what an agent harness is, from [[Coding harness for general-purpose agents]].

---

## Current state (late 2026)

Research papers often report results that don't hold up in a company's own context, and reproducing them takes time. OpenResearch CLI (orx), from alphaXiv, is an open-source harness that turns coding agents like Claude Code into research agents: each experiment runs in its own Git worktree, with the same run command and a frozen snapshot of the code, on compute you choose. The blip is new in November 2026, as a promising example of a domain-specific harness. Its official builds send usage analytics unless you turn them off.

## Level 1 — What it is (~10 min)

A harness that lets coding agents run reproducible, parallel research experiments.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/openresearch-cli-orx) (~1 min) — note the use case: reproducing a paper's method in your own setting.
- [ ] **~5 min** · Skim: [OpenResearch](https://github.com/alphaXiv/OpenResearch) (alphaXiv, README, ~4 min) — "Get started" and "How it works". Note the telemetry setting.

## Level 2 — Try it (~20 min)

- [ ] **~20 min** · **Do:** Install orx, turn off telemetry if you prefer (`orx telemetry off`), and start it with `orx up`. Pick a simple claim from a paper or blog post in your field, such as "technique X speeds up Y", and set up two experiments that test it. Look at how orx isolates and records each run.

## Wrap-up

This plan covers it. Harnesses built for one domain are part of the trend covered in [[Coding harness for general-purpose agents]].

## Review the blip

- [ ] **~5 min** · Re-read [OpenResearch CLI (orx)](https://www.thoughtworks.com/radar/tools/openresearch-cli-orx) now that you know the topic.

## Related blips

- **[[Claude Code]]**: one of the coding agents orx turns into a research agent.
