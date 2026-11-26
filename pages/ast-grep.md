- **Blip:** [ast-grep](https://www.thoughtworks.com/radar/tools/ast-grep)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Text search like `grep` can't tell code apart from comments or strings, and can't match a structure like "a function call with any arguments". Tools that search the syntax tree have existed for years (the Radar featured Comby in 2021), but ast-grep, written in Rust on top of tree-sitter, became the popular one. Coding agents made it more relevant: it gives them precise, structural search and custom lint rules without the setup of a language server or an index. Developers can use it without agents too.

## Level 1 — What it is (~10 min)

Search, lint and rewrite code with patterns that look like code, matched against the syntax tree instead of the text.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/ast-grep) (~1 min) — note how one team used ast-grep rules as checks inside an agent harness.
- [ ] **~5 min** · Read: [What is ast-grep?](https://ast-grep.github.io/guide/introduction.html) (ast-grep docs, ~3 min) — read the motivation, with its `console.log` example. It calls the tool "a hybrid of grep, eslint and codemod".

## Level 2 — Use it (~40 min)

Search and rewrite with patterns, then write a rule an agent can check its code against.

- [ ] **~15 min** · Read: [Quick Start](https://ast-grep.github.io/guide/quick-start.html) (ast-grep docs, ~4 min) — install it and follow the example: find `$PROP && $PROP()` in a real codebase, and rewrite it to optional chaining. Note the advice to single-quote patterns.
- [ ] **~25 min** · **Do:** In a project of yours, pick a pattern you'd like to ban, such as a deprecated API or a risky call. Find every occurrence with `ast-grep -p`, then turn it into a YAML lint rule with a message that explains what to use instead. Ask your coding agent to run the rule after each change, and check that it fixes what the rule reports.

## Wrap-up

This plan covers it. Structured code access through language servers is covered in [[Serena]], and turning lint results into guidance for agents in [[Habit Hooks]].

## Review the blip

- [ ] **~5 min** · Re-read [ast-grep](https://www.thoughtworks.com/radar/tools/ast-grep) now that you know the topic.

## Related blips

- **[[Code intelligence as agentic tooling]]**: ast-grep is a low-friction version of the same idea, with no index or language server.
- **[[Comby]]**: an older tool that covers much of the same ground.
