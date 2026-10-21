**Time:** ~1 hour · **Source:** [Thoughtworks Radar – MCP Apps (Assess, April 2026)](https://www.thoughtworks.com/radar/platforms/mcp-apps)

*Series: after [[FastMCP]] · next: [[MCP by default]].*

---

## Layer 1 — What MCP Apps are (0:00–0:20, ~20 min)

**Goal:** Explain how an MCP tool can show an interactive UI inside the chat, and why that's the first official MCP extension.

- [ ] Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/mcp-apps) — short. `ui://` resources, sandboxed iframes, and a text fallback. It also asks whether the extra complexity is worth it.
- [ ] Read: [MCP Apps – Bringing UI capabilities to MCP clients](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) (official MCP blog, Jan 2026) — the announcement.

## Layer 2 — How they work, and one example (0:20–1:00, ~40 min)

**Goal:** Know the flow (the tool declares a UI, the host fetches and sandboxes it, the app calls tools back), and see a working app.

- [ ] Read: [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview) — read "How MCP Apps work" and "When to use MCP Apps". You can skip the parts about building clients.
- [ ] **Do:** Pick a small example from the [ext-apps examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), such as `qr-server` or `basic-server-vanillajs`. Run it as its README explains, and connect it to Claude Desktop. Use it, and notice what you see compared with what the model sees. Then answer the blip's question for `radar-progress`: would a progress-bar UI be worth it, or is text enough? If the setup takes too long, stop at the one-hour mark and just read the example's code.

---

## If you have extra time

- [ ] Skim the [build guide](https://modelcontextprotocol.io/extensions/apps/build) to see what adding a UI to your own server would take.

---

## Current state of the topic

MCP Apps grew out of the community project MCP-UI and OpenAI's similar work for ChatGPT apps. It became the first official MCP extension in January 2026, with Anthropic and OpenAI developing it together. It's already supported by Claude, ChatGPT, VS Code Copilot, Goose and others, and FastMCP supports it too. It's still young: the Radar puts it in *Assess*, and host support differs from client to client. It's the clearest example of something only MCP can do, which makes it a useful counterpoint to [[MCP by default]].

---

## Recommendation for future learning

This plan covers it for a generalist. If you build agent products with a UI, also look at AG-UI, the competing approach that the blip compares it with.

**Related topics in Thoughtworks Radar:**

- [ ] [Model Context Protocol (MCP)](https://www.thoughtworks.com/radar/platforms/model-context-protocol-mcp) (Apr 2025, Nov 2025)
- [ ] [AG-UI Protocol](https://www.thoughtworks.com/radar/platforms/ag-ui-protocol) (Nov 2025, Apr 2026)
- [ ] [MCP by default](https://www.thoughtworks.com/radar/techniques/mcp-by-default) (Apr 2026)
