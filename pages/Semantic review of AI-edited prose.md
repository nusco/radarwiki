- **Blip:** [Semantic review of AI-edited prose](https://www.thoughtworks.com/radar/techniques/semantic-review-of-ai-edited-prose)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know how to write a simple skill, from [[Agent Skills]].

---

## Current state (late 2026)

Coding agents now write and rewrite specifications, plans and decision records much faster than people can review them. A text diff doesn't help much: an agent that rewords a document produces a diff full of noise, and the one changed requirement hides in it. The blip is new in November 2026, and in *Assess*. It doesn't point to any tool or article: it's a practice that Thoughtworks teams built themselves, usually as a skill that runs whenever an agent edits a document. So this plan is mostly hands-on.

## Level 1 — What it is (~5 min)

Add a layer on top of the text diff: an LLM that reports what changed in meaning, such as facts, scope, acceptance criteria and contradictions.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/semantic-review-of-ai-edited-prose) (~1 min) — note the kinds of change it looks for: altered facts, conflicting statements, redefined acceptance criteria, changes in scope.

## Level 2 — Build one (~35 min)

Write a semantic review skill, and test it on a real document change.

- [ ] **~35 min** · **Do:** Write a small skill that compares two versions of a document (for example, `git diff` of a Markdown file), and reports only changes in meaning, in four lists: facts changed, scope changed, acceptance criteria changed, and new contradictions. Test it on a page of this wiki or a spec of yours: ask your agent to "improve the wording" of it, then run the skill on the result. Did the rewording change any meaning? Would you have noticed in the plain diff?

## Wrap-up

This plan covers it. The technique responds to a wider problem, covered in [[AI-driven documentation sprawl]].

## Review the blip

- [ ] **~5 min** · Re-read [Semantic review of AI-edited prose](https://www.thoughtworks.com/radar/techniques/semantic-review-of-ai-edited-prose) now that you know the topic.
