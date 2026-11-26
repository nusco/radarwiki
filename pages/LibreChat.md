- **Blip:** [LibreChat](https://www.thoughtworks.com/radar/platforms/librechat)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what [[Model Context Protocol (MCP)]] servers are.

---

## Current state (late 2026)

Many companies want to give all their staff access to AI models, without each team signing up for its own tools. LibreChat is an open-source, self-hosted chat platform for that: one interface to models from many providers, with single sign-on, roles and document search. What sets it apart, says the blip, is agents: administrators decide which MCP servers are available, and people outside engineering can build and share agents on them without code. ClickHouse acquired LibreChat in November 2025, and it stays MIT licensed. The blip is new in November 2026, and presents it as an answer to [[AI-accelerated shadow IT]].

## Level 1 — What it is (~10 min)

A self-hosted AI chat platform for a whole organization, with no-code agents built on approved tools.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/librechat) (~2 min) — note the client example: MCP servers for internal systems, and staff in sales and operations building their own agents.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** Run LibreChat with Docker following the [Quick Start](https://www.librechat.ai/docs/quick_start) (LibreChat docs, ~5 minutes to set up), and connect one model provider. Add one MCP server you already use, then build a small agent on it without code, as a non-developer would. Decide what an administrator would need to control before opening it to a whole company.

## Wrap-up

This plan covers it. The similar Open WebUI has its own plan, [[Open WebUI]].

## Review the blip

- [ ] **~5 min** · Re-read [LibreChat](https://www.thoughtworks.com/radar/platforms/librechat) now that you know the topic.

## Related blips

- **[[AI-accelerated shadow IT]]**: LibreChat gives people outside engineering a controlled alternative.
- **[[ClickHouse]]**: the company that acquired LibreChat.
- **[[Open WebUI]]**: a similar self-hosted chat platform.
- **[[Grafana]]**: one of the systems the client example connected through MCP.
- **[[Model Context Protocol (MCP)]]**: how LibreChat's agents reach other systems.
