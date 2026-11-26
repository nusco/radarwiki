- **Blip:** [OpenSpec](https://www.thoughtworks.com/radar/tools/openspec)
- **Time:** ~1 hour 30 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Spec-driven development (SDD) became a trend in 2025: instead of prompting an agent directly, you agree on a written spec first, then let the agent implement it. Tools appeared fast, such as GitHub Spec Kit, Amazon's Kiro and BMAD, and critics noticed that they produce a lot of Markdown to review. OpenSpec is a lightweight, tool-agnostic alternative. Each change is a small set of "deltas" against a persistent spec, which makes it a better fit for existing codebases. It moved from *Assess* to *Trial* in November 2026, after several Thoughtworks teams used it successfully. It's evolving fast, and its docs don't always agree on command names.

## Level 1 — What spec-driven development is (~45 min)

Agree with the agent on what to build, in a spec, before it writes code. And know the trade-offs of doing so.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/openspec) (~2 min) — read both versions. Note what sets OpenSpec apart (deltas against a spec that stays current) and the usual warning about documentation sprawl.
- [ ] **~40 min** · Read: [Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) (Birgitta Böckeler, martinfowler.com, Oct 2025, ~14 min) — linked from the blip. It sorts SDD into three levels (spec-first, spec-anchored, spec-as-source), and is frank about the costs. OpenSpec isn't in the article, but its distinctions tell you where OpenSpec sits: spec-anchored.

## Level 2 — Use OpenSpec (~45 min)

Make one change to an existing codebase with OpenSpec's propose, apply and archive cycle.

- [ ] **~10 min** · Skim: [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) (OpenSpec docs, ~13 min) — read "Specs", "Changes" and "Delta specs" (added, modified, removed requirements). Check the README for the current command names, because this page uses older ones.
- [ ] **~35 min** · **Do:** Install OpenSpec from the [README](https://github.com/Fission-AI/OpenSpec) in an existing project, and make a small change with it: propose it, review the delta spec, apply it, and archive it. Then look at what's left in the repository. Was the spec worth reviewing, compared with reviewing the code? Note that OpenSpec sends telemetry by default, and the README explains how to opt out.

## Wrap-up

This plan covers OpenSpec, and gives a first look at spec-driven development. The technique has its own plan, [[Spec-driven development]], and the heavier alternative its own in [[GitHub Spec Kit]].

## Review the blip

- [ ] **~5 min** · Re-read [OpenSpec](https://www.thoughtworks.com/radar/tools/openspec) now that you know the topic.

## Related blips

- **[[AI-driven documentation sprawl]]**: OpenSpec generates Markdown specs, which need discipline to keep current.
- **[[Spec-driven development]]**: the technique OpenSpec implements.
- **[[GitHub Spec Kit]]**: a better-known spec-driven development tool, more suited to greenfield projects.
