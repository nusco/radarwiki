- **Blip:** [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default)
- **Time:** ~2 hours 45 minutes
- **Radar edition:** April 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you know what an MCP server is and how to add one to Claude Code, from [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

This entry reflects the backlash against MCP that started in late 2025, when single servers (GitHub's is the usual example) were shown to use up much of the context before the agent did anything. Since then, the *context cost* argument has weakened: Claude Code now uses tool search by default, so it loads MCP tool definitions only when they're needed. The *abstraction tax* argument still holds. The consensus in 2026: choose for each integration, and focus on tool design more than on the protocol. Use MCP for remote access, OAuth and governance. Use a CLI or a skill for local work by a single developer. [[Context7]] shows the trend: it now offers a CLI-plus-skill mode alongside its MCP server. The November 2026 Radar doesn't repeat the entry.

## Level 1 — The argument (~75 min)

Explain in two sentences why the Radar warns against making MCP the default way to connect agents to systems.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (~2 min) — MCP is worth it for structured contracts, OAuth boundaries and governed multi-tenant access. Otherwise, a CLI with clear help text and JSON output is often better.
- [ ] **~45 min** · Read: [What if you don't need MCP at all?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/) (Mario Zechner, Nov 2025, ~15 min) — a concrete case. He replaces browser MCP servers with a few small scripts: about 225 tokens of instructions, instead of 13,000–18,000 tokens of tool definitions.
- [ ] **~25 min** · Read: [The MCP abstraction tax](https://justin.poehnelt.com/posts/mcp-abstraction-tax/) (Justin Poehnelt, Mar 2026, ~7 min) — cited by the blip. Every layer between the agent and the API loses some detail.

## Level 2 — The alternatives (~45 min)

Know the two main alternatives: a CLI plus instructions, and code execution against MCP servers.

- [ ] **~15 min** · Read: [Claude Skills are awesome, maybe a bigger deal than MCP](https://simonwillison.net/2025/Oct/16/claude-skills/#skills-compared-to-mcp) (Simon Willison, Oct 2025, ~5 min from that section) — also cited by the blip. Start at "Skills compared to MCP". [[Agent Skills]] has its own plan.
- [ ] **~30 min** · Read: [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (Adam Jones and Conor Kelly, Anthropic, Nov 2025, ~10 min) — a middle path: keep the servers, but let the agent write code that calls them, so intermediate data never enters the context.

## Level 3 — Try it (~45 min)

See the difference between the two approaches on your own task.

- [ ] **~45 min** · **Do:** Ask Claude Code to build the same small capability twice: count how many items in `Thoughtworks Radar/<volume>-thoughtworks-radar-<edition>.md` are ticked and how many aren't. First as a one-tool MCP server, added with `claude mcp add`. Then as a CLI script (`radar-progress 2025-november`) with `--help` and JSON output, plus a minimal `~/.claude/skills/radar-progress/SKILL.md` (a name, a description, and three lines on how to run the script). Ask "how far along am I with the November 2025 Radar?" twice: once with only the MCP server enabled, and once with only the skill. Run `/context` after each and compare.

## If you have extra time

- [ ] **~45 min** · Read: [MCP is dead, long live MCP](https://chrlschn.dev/blog/2026/03/mcp-is-dead-long-live-mcp/) (Charles Chen, Mar 2026, ~15 min) — the other side of the argument, from a practitioner who defends MCP for teams. CLIs win for tools the model already knows, like `git` or `gh`, but remote MCP servers give an organization central auth, telemetry and shared prompts. It's combative in places, but it's the clearest case for the uses the blip still accepts.
- [ ] **~10 min** · Read: [Scale with MCP tool search](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search) (Claude Code docs, ~3 min for this section) — the strongest answer to "MCP wastes context".

## Wrap-up

Small, and covered here. It's a design judgment, not a technology. The ideas continue in [[Agent Skills]] and [[Context engineering]].

## Review the blip

- [ ] **~10 min** · Re-read [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: the protocol this blip warns against using where a simpler option, such as a CLI, would do.
