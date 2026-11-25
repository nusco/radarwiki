- **Blip:** [Path-to-production mapping](https://www.thoughtworks.com/radar/techniques/path-to-production-mapping)
- **Time:** ~2 hours
- **Radar edition:** October 2022 and November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

The technique is as old as Continuous Delivery, and Thoughtworks has used it for well over a decade. It reached the Radar only in 2022, straight into *Adopt*, and the November 2026 edition brings it back for a new reason: coding agents write code much faster, so the slow parts of delivery are now elsewhere, like review, testing, approvals and deployment. Mapping the path is how you find the new bottleneck. The workshop itself hasn't changed, so the older material is still valid.

## Level 1 — What it is (~10 min)

A path-to-production map is a picture of every step, person and tool that a code change goes through, from a developer's laptop to production.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/path-to-production-mapping) (~2 min) — read both versions. The 2022 one describes the workshop, and the 2026 one says why it matters more now.
- [ ] **~5 min** · Read: [Path to Production](https://caroli.org/en/path-to-production/) (Paulo Caroli, Sep 2020, ~2 min) — linked from the blip. A former Thoughtworker's three-step recipe, as short as it gets.

## Level 2 — Run the workshop (~1 hour)

Learn how to run the workshop, then map a path you know.

- [ ] **~30 min** · Read: [Path to Production Mapping](https://hamvocke.com/blog/path-to-production) (Ham Vocke, Mar 2023, ~10 min) — the most complete practitioner guide, by a former Thoughtworks consultant: who to invite, how to lay out the canvas, and how to analyze the map. It also explains how it differs from value-stream mapping.
- [ ] **~30 min** · **Do:** Map the path to production of a project you work on, on paper or a whiteboard, following Vocke's canvas. Include every step, wait, handoff and tool, with rough times. Then mark the three biggest pain points, and circle the step where changes wait the longest.

## Level 3 — Why it matters more with AI (~45 min)

See why faster coding moves the bottleneck, and use your map to find where it moves.

- [ ] **~25 min** · Read: [Value-Stream Mapping Is Your Missing AI Superpower](https://www.lean.org/the-lean-post/articles/value-stream-mapping-is-your-missing-ai-superpower/) (Steve Pereira, Lean Enterprise Institute, Feb 2026, ~8 min) — the argument behind the 2026 blip, from a flow consultant who draws on the DORA 2025 report: AI amplifies whatever system it lands in, so map the flow before you speed up one step. Focus on the list of dysfunctions.
- [ ] **~15 min** · Read: [Code review isn't your bottleneck, even with AI](https://octopus.com/blog/code-review-not-bottleneck-even-with-ai) (Steve Fenton, Octopus Deploy, Jul 2026, ~5 min) — a contrarian take: neither coding nor review is the real constraint, and the size of the batches that reach users shows where it is. Read it against your map.
- [ ] **~5 min** · **Do:** Go back to your Level 2 map, and imagine that coding takes half the time it takes now. Which step becomes the bottleneck? Write down one change to that step that you'd propose to your team.

## If you have extra time

- [ ] **~10 min** · Read: [Path to Production Mapping](https://blogs.vmware.com/tanzu/path-to-production-mapping/) (VMware Tanzu Team, Jan 2024, ~3 min) — an alternative format, adapted from Event Storming, with a sample agenda and prompts. Useful if you'll facilitate the workshop with a larger group.

## Wrap-up

This plan covers the technique. The practice it comes from, Continuous Delivery, deserves its own study: the 2010 book by Jez Humble and David Farley, which the blip links to, is still the reference.

## Review the blip

- [ ] **~5 min** · Re-read [Path-to-production mapping](https://www.thoughtworks.com/radar/techniques/path-to-production-mapping) now that you know the topic.
