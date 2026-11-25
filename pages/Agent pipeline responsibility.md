- **Blip:** [Agent pipeline responsibility](https://www.thoughtworks.com/radar/techniques/agent-pipeline-responsibility)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know the classic Continuous Integration rule: don't push on a red build. [[Path-to-production mapping]] covers the wider pipeline.

---

## Current state (late 2026)

Teams have long agreed to keep the build green, and not to push while it's broken. Coding agents now push much more often, but usually can't see the build: when it breaks, a human copies the failure logs into the agent's chat, becoming what the Radar calls a [[Meat proxy]]. The blip is new in November 2026, and it's in *Assess*. Its advice is simple and needs no new tools: let the agent see the build, and enforce the important rules with gates instead of instructions.

## Level 1 — What it is (~10 min)

Make coding agents part of the team's agreement to keep the build green: they see the build state, read the failures, and help fix them.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-pipeline-responsibility) (~2 min) — note the three recommendations: build state in the agent's context, pipeline status and logs as tools, and mechanical gates for the rules that matter.

## Level 2 — Try it (~30 min)

Give your agent eyes on the pipeline, and a gate it can't talk its way past.

- [ ] **~30 min** · **Do:** In a repository with a CI pipeline, add a line to your agent's instructions: check the latest pipeline run before pushing, and read the failure logs if it's red. On GitHub, the agent can use `gh run list` and `gh run view --log-failed`. Then add a pre-push hook that refuses to push when the last run on the branch failed. Break the build on purpose, and watch what the agent does.

## Wrap-up

This plan covers it. The same idea, applied to production instead of the build, is in [[Production-aware coding agents]]. How much human review each change needs is covered in [[Risk-tiered human oversight]].

## Review the blip

- [ ] **~5 min** · Re-read [Agent pipeline responsibility](https://www.thoughtworks.com/radar/techniques/agent-pipeline-responsibility) now that you know the topic.

## Related blips

- **[[Path-to-production mapping]]**: the blip suggests including agents' role in build policy when you map the path.
- **[[Meat proxy]]**: what a human becomes when they relay build failures to an agent that can't see them.
- **[[Risk-tiered human oversight]]**: one way teams are rethinking build discipline as agents commit more often.
