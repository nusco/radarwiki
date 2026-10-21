**Time:** ~30 minutes · **Source:** [Thoughtworks Radar – Agent Scan (Assess, April 2026)](https://www.thoughtworks.com/radar/tools/agent-scan), formerly [MCP-Scan (November 2025)](https://www.thoughtworks.com/radar/tools/mcp-scan)

*Series: after [[Toxic flow analysis for AI]] · next: [[Agent-to-Agent (A2A) Protocol]]. Assumption: you ran a first scan in Layer 4 of [[Model Context Protocol (MCP)]].*

---

## Layer 1 — What changed (0:00–0:10, ~10 min)

**Goal:** Know what Agent Scan checks today (MCP servers *and* skills), and the blip's caveats.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/agent-scan) — short. It's useful for an inventory, but it sends metadata to Snyk, and you should check its false positives yourself before making it a mandatory gate.

## Layer 2 — Scan, and compare with your own analysis (0:10–0:30, ~20 min)

**Goal:** See how an automated scan compares with your hand-drawn toxic flow graph.

- [ ] Skim: [The Agent Scan README](https://github.com/snyk/agent-scan) — read the section on what data it sends to Snyk.
- [ ] **Do:** Run `uvx snyk-agent-scan@latest inspect` to list what it finds without analyzing it. Then run a full scan, which now includes your skills, like the `radar-progress` skill from [[Agent Skills]]. Compare the findings with the graph you drew in [[Toxic flow analysis for AI]]. What did the scanner find that you missed, and what did you find that it missed?

---

## Current state of the topic

MCP-Scan started at Invariant Labs. It became Agent Scan after Snyk acquired the company, and it now covers skills and agent configurations, not just MCP servers. It's one of the few tools for inventorying an agent's supply chain, but it's still in *Assess*: the analysis runs in Snyk's cloud, and its signal quality isn't proven yet.

---

## Recommendation for future learning

This plan covers it.

**Related topics in Thoughtworks Radar:**

- [ ] [MCP-Scan](https://www.thoughtworks.com/radar/tools/mcp-scan) (Nov 2025)
- [ ] [Toxic flow analysis for AI](https://www.thoughtworks.com/radar/techniques/toxic-flow-analysis-for-ai) (Nov 2025, Apr 2026)
- [ ] [Agent Skills](https://www.thoughtworks.com/radar/techniques/agent-skills) (Apr 2026)
