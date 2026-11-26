- **Blip:** [Deepsec](https://www.thoughtworks.com/radar/tools/deepsec)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Agent-powered vulnerability scanners appeared in 2026: instead of matching known patterns, they let a coding agent read the code and reason about attacks. They find real issues, but they can be expensive. Deepsec, an open-source tool from Vercel Labs, tries to cut that cost: a fast deterministic scan picks the risky files first, and agents investigate only those. The blip is new in November 2026. Its own README warns that a scan of a large codebase can still cost thousands of dollars, and that it runs with the same power as a coding agent with shell access.

## Level 1 — What it is, and its costs (~15 min)

A vulnerability scanner that maps a codebase, then sends AI agents to inspect only the high-risk areas.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/deepsec) (~1 min).
- [ ] **~10 min** · Skim: [deepsec](https://github.com/vercel-labs/deepsec) (Vercel Labs, README, ~5 min) — read "Get started" and "Security model of deepsec itself". Note the cost and time caps, and the warning about prompt injection from vendored code.

## Level 2 — Try it (~15 min)

Run a capped scan, and judge one finding.

- [ ] **~15 min** · **Do:** On a small codebase you own, run `npx deepsec init` with a low cost cap (for example, `--max-cost-usd 5`) in a sandbox. Read one finding, and decide whether it's a real problem. If you'd rather not spend money, write down how you'd set limits and isolation before running it on a real project.

## Wrap-up

This plan covers it. Running tools like this safely is covered in [[Agent sandboxing]].

## Review the blip

- [ ] **~5 min** · Re-read [Deepsec](https://www.thoughtworks.com/radar/tools/deepsec) now that you know the topic.
