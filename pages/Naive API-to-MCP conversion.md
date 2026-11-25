- **Blip:** [Naive API-to-MCP conversion](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion)
- **Time:** ~1.5 hours
- **Radar edition:** November 2025
- **Quadrant:** Techniques
- **Ring:** Hold
- **Updated:** 2026-11-24
- **Status:** #undone

This plan assumes that you know how MCP tools work, from [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

This entry appeared once, as *Hold*, in November 2025. It isn't in the April 2026 or November 2026 Radars, but its ideas live on in [[MCP by default]], which takes them further: sometimes the best MCP server is no MCP server at all. Converters are still common. FastMCP still includes an OpenAPI provider, but its docs say LLMs work better with curated servers than with converted ones.

## Level 1 — The anti-pattern (~30 min)

Explain why turning an existing API into MCP tools, one endpoint per tool, gives agents a bad interface.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) (~2 min) — APIs are designed for human developers, with many small actions. Agents that chain these actions waste tokens and can reach dangerous operations.
- [ ] **~10 min** · Skim: [The FastAPI-MCP README](https://github.com/tadata-org/fastapi_mcp) (Tadata) — one of the converters the blip names. Look at how little code it takes to turn a whole API into MCP tools. That's the temptation.
- [ ] **~15 min** · Read: [Stop converting your REST APIs to MCP](https://www.jlowin.dev/blog/stop-converting-rest-apis-to-mcp) (Jeremiah Lowin, Jul 2025, ~5 min) — from the author of FastMCP, a framework that itself can do this conversion. Use it to get started quickly, then design curated tools.

## Level 2 — What a good agent tool looks like (~60 min)

Know the main rules for designing tools for agents, and apply them to your own server.

- [ ] **~30 min** · Read: [Writing effective tools for agents — with agents](https://www.anthropic.com/engineering/writing-tools-for-agents) (Ken Aizawa, Anthropic, Sep 2025, ~15 min) — linked from the [[Context engineering]] blip. Combine many small operations into a few tools, return information that's meaningful to the agent, keep outputs token-efficient, and write descriptions the way you'd write a prompt.
- [ ] **~30 min** · **Do:** Imagine two MCP servers that answer "how far along am I with the November 2025 Radar?" from the files in `Thoughtworks Radar`. The naive one is a file-system API turned into MCP, with `list_files` and `read_file` tools. The curated one has a single `radar_progress(edition)` tool that returns the ticked and unticked counts. Write down the calls an agent would need with the naive server, and estimate the tokens they return (bytes ÷ 4 is close enough; `wc -c` gives the bytes). Compare with the one call to the curated server. Then design the curated tool against Anthropic's rules: write its description, and the error it returns for an unknown edition (for example, one that lists the valid editions).

## If you have extra time

- [ ] **~10 min** · Skim: [The MCP Link README](https://github.com/automation-ai-labs/mcp-link) (Automation AI Labs) — the other converter the blip names. It turns any OpenAPI spec into an MCP server, which you can run yourself or as a hosted service.

## Wrap-up

Small, and fully covered here. The design rules are more important than the anti-pattern itself, and they come back in [[Context engineering]].

## Review the blip

- [ ] **~10 min** · Re-read [Naive API-to-MCP conversion](https://www.thoughtworks.com/radar/techniques/naive-api-to-mcp-conversion) now that you know the topic.

## Related blips

- **[[Model Context Protocol (MCP)]]**: the protocol this blip is about: design MCP servers for agents instead of mirroring existing APIs.
