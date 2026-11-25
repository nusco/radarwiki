- **Blip:** [Graph-grounded codebase reasoning](https://www.thoughtworks.com/radar/techniques/graph-grounded-codebase-reasoning)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on [[Serena]], which gives agents structured access to code through a language server.

---

## Current state (late 2026)

Coding agents mostly find their way around code with text search, like `grep`. In April 2026 the Radar's [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) blip suggested giving them structure instead, through language servers and AST tools. This blip, new in November 2026, goes one step further: turn code, documentation and their relationships into a graph, and let the agent query the parts it needs. Tools like Graphify became very popular in 2026. The evidence is mixed: graphs can save tokens and reveal hidden dependencies, but research also found cases where agents did worse with a graph than with plain `grep`. That's why the Radar asks teams to try it and measure.

## Level 1 — What it is (~10 min)

Represent the codebase as a graph of entities and relationships, so the agent retrieves a relevant subgraph instead of whole files.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/graph-grounded-codebase-reasoning) (~1 min), then its predecessor, [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (~1 min) — note the step from structured lookups (find references, rename) to a whole graph of the code and its docs.

## Level 2 — Measure it (~40 min)

Try a graph tool on code you know, and find out whether it helps.

- [ ] **~10 min** · Skim: [Graphify](https://github.com/Graphify-Labs/graphify) (Graphify Labs) — the tool the blip names. Skim the README up to the outputs: code is parsed locally into a graph, docs get an optional LLM pass, and every edge says whether it was extracted or inferred. Its benchmark numbers are its own.
- [ ] **~30 min** · **Do:** Run Graphify on a repository you know well. Then ask your agent the same two questions in two fresh sessions, one with the graph and one without: a "where is X used?" question, and a "what would break if I changed Y?" question. Compare the answers you know to be right, and the context each session used (`/context`). Decide whether you'd keep the graph for this repository.

## Wrap-up

This plan covers it. The blip's research link, a paper on a deterministic architecture graph for code assistants, is research-level: the exercise tests the same question on your own code.

## Review the blip

- [ ] **~5 min** · Re-read [Graph-grounded codebase reasoning](https://www.thoughtworks.com/radar/techniques/graph-grounded-codebase-reasoning) now that you know the topic.

## Related blips

- **[[Code intelligence as agentic tooling]]**: the earlier technique this one builds on.
