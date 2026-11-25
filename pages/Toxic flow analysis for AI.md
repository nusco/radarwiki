- **Blip:** [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai)
- **Time:** ~2 hours
- **Radar edition:** November 2025, April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you know how prompt injection attacks MCP servers, from Level 4 of [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

Invariant Labs introduced the term in mid-2025, along with a tool that automates it (now [[Agent Scan]], which has the tool's history). In November 2026 the technique moved from *Assess* to *Trial*, because Thoughtworks teams have used it successfully, with tools like Agent Scan. Prompt injection itself is still unsolved: no filter reliably stops it. That's why rules that limit capabilities, like the trifecta and the Rule of Two, are the best defense. Since April 2026 the concern covers skills too, after studies such as Snyk's ToxicSkills (see [[Agent Skills]]).

## Level 1 — What it is, and why (~45 min)

Explain toxic flow analysis: mapping the paths through an agent's tools where untrusted content, private data and an outbound channel meet.

- [ ] **~8 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) (~2 min) — read all three versions. In April 2026 it extends from MCP servers to Agent Skills, and in November 2026 it moves to Trial.
- [ ] **~15 min** · Read: [Toxic flows in agentic systems](https://invariantlabs.ai/blog/toxic-flow-analysis) (Luca Beurer-Kellner, Marco Milanta and Marc Fischer, Invariant Labs, Jul 2025, ~5 min) — the post that introduced the term, with the GitHub MCP exploit as its example.
- [ ] **~22 min** · Read: [The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/) (Simon Willison, Jun 2025, ~7 min) — private data plus untrusted content plus a way to send data out. Toxic flow analysis is the search for paths that combine all three.

## Level 2 — Apply it to your setup (~75 min)

Find the toxic flows in your own agent setup, and know a simple rule for removing them.

- [ ] **~40 min** · Read: [Agents Rule of Two](https://ai.meta.com/blog/practical-ai-agent-security/) (Meta, Oct 2025, 14 min) — a practical rule that follows from the lethal trifecta: in a session, an agent should have no more than two of untrusted input, sensitive data, and the ability to change things or communicate outside.
- [ ] **~35 min** · **Do:** Draw the flow graph of your Claude Code setup by hand. List each MCP server, skill and built-in tool (web fetch, shell, file access), and mark which part of the trifecta it provides. For example, [[Context7]] brings in untrusted content, file reads can reach private data, and web fetch can send data out. Find one path that connects all three, and decide which leg you'd cut. Automated scanning is covered in [[Agent Scan]].

## If you have extra time

- [ ] **~5 min** · Read: [OpenClaw](https://www.thoughtworks.com/radar/tools/openclaw) (Radar, Apr 2026, ~2 min) — the "permission-hungry" agent the April 2026 version uses as its example.

## Wrap-up

This plan is enough for a generalist. If you ever deploy agents for other people, study agent security more broadly as its own topic (~3 hours): sandboxing, permissions, and prompt injection defenses.

## Review the blip

- [ ] **~10 min** · Re-read [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) now that you know the topic.

## Related blips

- **[[Threat modeling]]**: the broader practice: toxic flow analysis applies it to the data flows of agentic systems.
- **[[Agent Skills]]**: malicious skills can create toxic flows, just as MCP servers can.
- **[[Agent Scan]]**: a scanner that helps find toxic flows in an agent's MCP servers and skills.
