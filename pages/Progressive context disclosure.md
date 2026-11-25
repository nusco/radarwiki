- **Blip:** [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure)
- **Time:** ~1 hour 10 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you've done Levels 1 and 2 of [[Context engineering]], so you know why a smaller context often works better than a bigger one (context rot).

A subtopic usually gets less time than its parent, and most of this technique's mechanisms already have their own pages, so this plan is short.

---

## Current state (late 2026)

The idea is older than LLMs: "progressive disclosure" is a user interface pattern from the 1980s and 1990s, which shows the essentials first and the rest on request. In 2025 it became a design principle for agents, most visibly in [[Agent Skills]], which load only a skill's description until the skill is needed. By late 2026 almost every serious agent setup uses it in some form, which is why it moved from *Trial* to *Adopt* in six months. What's still changing is the tooling around it, not the idea.

## Level 1 — What it is (~20 min)

Instead of putting everything in the context up front, give the model a short map, and let it load the details when it needs them.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) (~2 min) — read both versions. The November 2026 one lists the main forms: a lean AGENTS.md that links to docs, deferred loading of MCP tools and skills, and RAG.
- [ ] **~15 min** · Read: [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) (Jakob Nielsen, NN/g, Dec 2006, ~5 min) — where the name comes from: a classic article on interface design. Its two rules carry over to agents almost unchanged: split what's always needed from what's rarely needed, and make the path to the details obvious. Its warning against more than two levels applies to agents too.

## Level 2 — Apply it (~50 min)

Recognize the technique in the tools you use, and apply it to your own instruction files.

- [ ] **~5 min** · Read: [Your CLAUDE.md should be a map, not your entire product context](https://contra.com/community/HDedmzbW-your-claudemd-should-be-a-map) (Sebastian Avelar, Aug 2026, ~2 min) — a short practitioner post with the simplest form of the technique: the root instruction file becomes an index of small docs.
- [ ] **~45 min** · **Do:** Take the instruction file of a project you work on (`CLAUDE.md` or `AGENTS.md`), or the one you wrote in [[AGENTS.md]]. Move every section that only matters for some tasks into its own file, and replace it with one line that says when to read that file. Run `/context` before and after, and compare. Then give the agent a task that needs one of the moved files, and check that it finds it.

The other forms of the technique have their own pages: skills in [[Agent Skills]], deferred MCP tools in [[MCP by default]], and the risks of letting instruction files grow in [[Agent instruction bloat]].

## Wrap-up

This plan covers it: the technique is simple, and the depth is in the mechanisms that apply it. Retrieval-based forms, [[Retrieval-augmented generation (RAG)]] and [[GraphRAG]], are big topics of their own.

## Review the blip

- [ ] **~5 min** · Re-read [Progressive context disclosure](https://www.thoughtworks.com/radar/techniques/progressive-context-disclosure) now that you know the topic.

## Related blips

- **[[Context engineering]]**: the blip calls progressive disclosure a context engineering technique.
- **[[AGENTS.md]]**: a lean AGENTS.md that links to more detailed docs is one of the blip's examples.
- **[[Agent Skills]]**: skills load only their descriptions up front, and their bodies on demand.
- **[[Retrieval-augmented generation (RAG)]]**: retrieves only the relevant documents at query time, a retrieval-based form of the technique.
- **[[GraphRAG]]**: the same, with retrieval guided by a knowledge graph.
