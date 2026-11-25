- **Blip:** [AI-driven documentation sprawl](https://www.thoughtworks.com/radar/techniques/ai-driven-documentation-sprawl)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Spec-driven development tools (like Spec Kit and BMAD) and coding agents made it trivial to generate polished documentation: specs, plans, decision records. Unlike code, documentation rarely goes through tests or quality gates, so it piles up, goes stale and contradicts itself. The blip is new in November 2026, and it adds a twist: agents read this documentation as context, so outdated specs don't just waste people's time, they lead agents astray.

## Level 1 — What it is, and what to do (~30 min)

Generated documentation that nobody prunes becomes a "big ball of documentation mud", and agents read it as if it were true.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/ai-driven-documentation-sprawl) (~1 min) — note the advice: treat Markdown as a first-class artifact, and spend deliberate human effort to prune and consolidate it.
- [ ] **~25 min** · **Do:** In a repository where agents have written documentation, list every Markdown file outside the README. For each one, decide: still true, outdated, or duplicated elsewhere? Delete or merge two of them. Then ask your agent a question that one of the outdated files would have answered wrongly, and check that it gets it right now.

Checking what an agent changed in a document is covered in [[Semantic review of AI-edited prose]], and keeping a shared knowledge base healthy in [[Agent-maintained knowledge bases]].

## Wrap-up

This plan covers it.

## Review the blip

- [ ] **~5 min** · Re-read [AI-driven documentation sprawl](https://www.thoughtworks.com/radar/techniques/ai-driven-documentation-sprawl) now that you know the topic.

## Related blips

- **[[Semantic review of AI-edited prose]]**: helps reviewers see what actually changed when agents rewrite documents.
