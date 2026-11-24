- **Blip:** [Serena](https://www.thoughtworks.com/radar/tools/serena)
- **Time:** ~50 minutes
- **Radar edition:** November 2025
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-24
- **Status:** #undone

---

## Current state (late 2026)

Serena isn't in the April 2026 or November 2026 Radars on its own. Instead, the April 2026 Radar has a broader technique, *Code intelligence as agentic tooling*, that covers Serena alongside LSP integrations in Claude Code and OpenCode, the JetBrains MCP server, and OpenRewrite. Serena itself has reached version 2, with a new interface. For a generalist, the lesson is the technique more than the tool: deterministic tools that understand code save tokens and avoid broken edits. That's [[Context engineering]] applied to code.

## Level 1 — What it is, and why (~20 min)

Explain why coding agents benefit from working with symbols (functions, classes, references) instead of searching and replacing text.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/serena) (~1 min).
- [ ] **~15 min** · Skim: [Serena's tools](https://oraios.github.io/serena/01-about/035_tools.html) (Serena docs, ~10 min) — the list the blip links to, which has since moved from the README to the docs. Look at `find_symbol`, `find_referencing_symbols` and `insert_after_symbol`, and compare them with the "read file" and "replace text" tools your agent uses by default.

## Level 2 — How it works (~20 min)

Know that Serena's tools run on language servers, the same Language Server Protocol (LSP) that gives your editor "go to definition", and try LSP-based code intelligence yourself.

- [ ] **~20 min** · Skim: [Code intelligence plugins](https://code.claude.com/docs/en/plugins/code-intelligence) (Claude Code docs, ~7 min) — Claude Code's built-in way to give the agent a language server. Serena does the same through MCP. Skim the page, then install the Python plugin and ask Claude Code to find every caller of a function in `Thoughtworks Radar/download-script/radar_to_todo.py`.

## Level 3 — From a tool to a technique (~10 min)

Know where the idea went next.

- [ ] **~10 min** · Read: [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Radar, Apr 2026, ~2 min) — a general technique, with Serena as one of several tools, next to the LSP support you just tried.

## If you have extra time

- [ ] **~30 min** · **Do:** If you work on a large codebase, install Serena (`uv tool install -p 3.13 serena-agent`, then `serena init`) and try a cross-file rename with it. Its advantage is small on small projects.

## Wrap-up

This plan covers it.

## Review the blip

- [ ] **~10 min** · Re-read [Serena](https://www.thoughtworks.com/radar/tools/serena) now that you know the topic.

## Related Radar topics

- [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling)
- [[Context engineering]]
- [[Model Context Protocol (MCP)]]
