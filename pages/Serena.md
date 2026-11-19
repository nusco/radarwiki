- **Time:** ~50 minutes
- **Radar edition:** November 2025
- **Blip:** [Serena](https://www.thoughtworks.com/radar/tools/serena)
- **Quadrant:** Tools
- **Ring:** Assess
- **Created:** 2026-10-21

---

## Current state of the topic (as of 2026-11-15)

Serena isn't in the April 2026 Radar on its own. Instead, the Radar now has a broader technique, *Code intelligence as agentic tooling*, that covers Serena alongside LSP integrations in Claude Code and OpenCode, the JetBrains MCP server, and OpenRewrite. Serena itself has reached version 2, with a new interface. For a generalist, the lesson is the technique more than the tool: deterministic tools that understand code save tokens and avoid broken edits. That's [[Context engineering]] applied to code.

---

## Level 1 — What it is, and why (0:00–0:20, ~20 min)

**Goal:** Explain why coding agents benefit from working with symbols (functions, classes, references) instead of searching and replacing text.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/serena) (~1 min).
- [ ] **~15 min** · Skim: [Serena's tools](https://oraios.github.io/serena/01-about/035_tools.html) (~10 min) — the list the blip links to, which has since moved from the README to the docs. Look at `find_symbol`, `find_referencing_symbols` and `insert_after_symbol`, and compare them with the "read file" and "replace text" tools your agent uses by default.

## Level 2 — How it works (0:20–0:40, ~20 min)

**Goal:** Know that Serena's tools run on language servers, the same Language Server Protocol (LSP) that gives your editor "go to definition", and try LSP-based code intelligence yourself.

- [ ] **~20 min** · Skim: [Code intelligence plugins](https://code.claude.com/docs/en/plugins/code-intelligence) (Claude Code docs, ~6 min) — Claude Code's built-in way to give the agent a language server. Serena does the same through MCP. Skim the page, then install the Python plugin and ask Claude Code to find every caller of a function in `Thoughtworks Radar/download-script/radar_to_todo.py`.

## Level 3 — From a tool to a technique (0:40–0:50, ~10 min)

**Goal:** Know where the idea went next.

- [ ] **~10 min** · Read: [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Radar, Apr 2026, ~2 min) — a general technique, with Serena as one of several tools, next to the LSP support you just tried.

---

## If you have extra time

- [ ] **~30 min** · If you work on a large codebase, install Serena (`uv tool install -p 3.13 serena-agent`, then `serena init`) and try a cross-file rename with it. Its advantage is small on small projects.

---

## Recommendation for future learning

This plan covers it.

Related Radar topics:

- [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Apr 2026)
- [[Context engineering]] (Nov 2025, Apr 2026)
- [[Model Context Protocol (MCP)]] (Apr 2025, Nov 2025)

---

- [ ] **~10 min** · **Close:** [Review the blip](https://www.thoughtworks.com/radar/tools/serena) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
