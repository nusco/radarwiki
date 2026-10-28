**Time:** ~45 minutes · **Source:** [Thoughtworks Radar – Serena (Assess, November 2025)](https://www.thoughtworks.com/radar/tools/serena)

*Series: after [[Context7]] · next: [[Toxic flow analysis for AI]].*

---

## Layer 1 — What it is (0:00–0:20, ~20 min)

**Goal:** Explain why coding agents benefit from working with symbols (functions, classes, references) instead of searching and replacing text.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/serena) — short.
- [ ] Skim: [Serena's tools](https://oraios.github.io/serena/01-about/035_tools.html) — the list the blip links to, which has since moved from the README to the docs. Look at `find_symbol`, `find_referencing_symbols` and `insert_after_symbol`, and compare them with the "read file" and "replace text" tools your agent uses by default.

## Layer 2 — From a tool to a technique (0:20–0:45, ~25 min)

**Goal:** Know where the idea went next, and how it compares with Claude Code's own language-server support.

- [ ] Read: [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Radar, Apr 2026) — a general technique, with Serena as one of several tools.
- [ ] Skim: [Code intelligence plugins](https://code.claude.com/docs/en/plugins/code-intelligence) (Claude Code docs) — the built-in alternative, based on the Language Server Protocol (LSP). If you like, install the Python plugin and ask Claude Code to find every caller of a function in `radar_progress.py`.

---

## If you have extra time

- [ ] If you work on a large codebase, install Serena (`uv tool install -p 3.13 serena-agent`, then `serena init`) and try a cross-file rename with it. Its advantage is small on small projects.

---

## Current state of the topic

Serena isn't in the April 2026 Radar on its own. Instead, the Radar now has a broader technique, *Code intelligence as agentic tooling*, that covers Serena alongside LSP integrations in Claude Code and OpenCode, the JetBrains MCP server, and OpenRewrite. Serena itself has reached version 2, with a new interface. For a generalist, the lesson is the technique more than the tool: deterministic tools that understand code save tokens and avoid broken edits. That's [[Context engineering]] applied to code.

---

## Recommendation for future learning

This plan covers it.

**Related topics in Thoughtworks Radar:**

- [ ] [Code intelligence as agentic tooling](https://www.thoughtworks.com/radar/techniques/code-intelligence-as-agentic-tooling) (Apr 2026)
- [ ] [Context engineering](https://www.thoughtworks.com/radar/techniques/context-engineering) (Nov 2025, Apr 2026)
- [ ] [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) (Apr 2025, Nov 2025)

---

- [ ] **Close:** [Review the blip](https://www.thoughtworks.com/radar/tools/serena) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
