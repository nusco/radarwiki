- **Blip:** [Agent suggestion box](https://www.thoughtworks.com/radar/techniques/agent-suggestion-box)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

When an agent hits a broken tool or a missing dependency, it usually works around the problem in silence, and the next session hits it again. In 2026 a few teams started giving agents a place to complain: Lovable published how its agent "vents" to a Slack channel, and small open-source kits appeared for coding agents. The blip is new in November 2026, and it's in *Assess* because Thoughtworks has used it with only one agent so far. The early numbers are encouraging, but also show that many reports are noise.

## Level 1 — What it is (~20 min)

Give a running agent somewhere to report the problems it runs into, so that someone fixes them instead of every session working around them.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-suggestion-box) (~2 min) — note the difference from memory: memory helps the agent avoid a broken tool, a suggestion box gets the tool fixed.
- [ ] **~15 min** · Read: [We Gave Our Agent a Vent Tool](https://lovable.dev/blog/we-gave-our-agent-a-vent-tool) (Benjamin Verbeek, Lovable, May 2026, 5 min) — the example the blip cites, in production at scale. Note the honest numbers: about ten fixes merged a day, but half of the fixes its triage agent proposes are false positives.

## Level 2 — Try it (~25 min)

Give your own agent a suggestion box, and see what it reports.

- [ ] **~25 min** · **Do:** Add a short instruction to your coding agent's instruction file: when a tool, script or piece of documentation gets in its way, append one line to `agent-feedback.md` saying what happened and what it did instead, and keep going. Use it for a few days of normal work. Then read the file: which reports point to something worth fixing, and which are noise? Fix one.

What to do with the suggestions over time is covered in [[Feedback flywheel]].

## Wrap-up

This plan covers it. The blip also mentions [agents-feedback](https://github.com/TechSpokes/agents-feedback), a ready-made folder structure for the same idea. It's a very young project, so the exercise above uses a single file instead.

## Review the blip

- [ ] **~5 min** · Re-read [Agent suggestion box](https://www.thoughtworks.com/radar/techniques/agent-suggestion-box) now that you know the topic.

## Related blips

- **[[Feedback flywheel]]**: the team habit that turns the box's reports into changes to the shared setup.
- **[[Self-improving harness]]**: lets agents act on the suggestions themselves.
