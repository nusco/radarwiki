- **Blip:** [MCP Apps](https://www.thoughtworks.com/radar/platforms/mcp-apps)
- **Time:** ~1.5 hours
- **Radar edition:** April 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-24
- **Status:** #undone

---

## Current state (late 2026)

MCP Apps grew out of the community project MCP-UI and OpenAI's similar work for ChatGPT apps. It became the first official MCP extension in January 2026, with Anthropic and OpenAI developing it together. It's already supported by Claude, ChatGPT, VS Code Copilot, Goose and others, and FastMCP supports it too. It's still young: the April 2026 Radar put it in *Assess*, the November 2026 Radar doesn't list it, and host support differs from client to client. It's the clearest example of something only MCP can do, which makes it a useful counterpoint to [[MCP by default]].

## Level 1 — What MCP Apps are, and why (~30 min)

Explain how an MCP tool can show an interactive UI inside the chat, and why that was worth the first official MCP extension.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/mcp-apps) (~1 min) — `ui://` resources, sandboxed iframes, and a text fallback. It also asks whether the extra complexity is worth it.
- [ ] **~10 min** · **Do:** In Claude (even on the free plan), add an interactive connector for a tool you already use, such as Figma, Canva, Slack or Asana, and ask it to show you something. Notice what's interactive and what's plain text. If you don't use any of those tools, read [the announcement](https://claude.com/blog/interactive-tools-in-claude) (Anthropic, Jan 2026, 4 min) instead, which describes what each one shows.
- [ ] **~15 min** · Read: [MCP Apps – Bringing UI capabilities to MCP clients](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) (MCP Core Maintainers, official MCP blog, Jan 2026, 9 min) — the announcement of the extension, and where it came from.

## Level 2 — How they work (~60 min)

Know the flow (the tool declares a UI, the host fetches and sandboxes it, the app calls tools back), and see it in a working app.

- [ ] **~20 min** · Read: [MCP Apps are here: Rendering interactive UIs in AI clients](https://workos.com/blog/2026-01-27-mcp-apps) (WorkOS, Jan 2026, ~7 min) — the flow, with short code samples, and when a UI beats plain text.
- [ ] **~40 min** · **Do:** Pick a small example from the [ext-apps examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), such as `qr-server` or `basic-server-vanillajs`. Run it as its README explains, and connect it to Claude Desktop. Find the three steps of the flow in its code. Then answer the blip's question for a small tool you might write, such as one that tells you how far along you are with a Radar edition: would a progress-bar UI be worth it, or is text enough? If the setup takes more than 30 minutes, stop and just read the example's code.

## If you have extra time

- [ ] **~25 min** · Read: [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview) (MCP docs, ~8 min) — the page the blip links to. It's the full reference, and longer than you need if the WorkOS article was clear.
- [ ] **~15 min** · Skim: [Build an MCP App](https://modelcontextprotocol.io/extensions/apps/build) (MCP docs, ~10 min) — to see what adding a UI to your own server would take.

## Wrap-up

This plan covers it for a generalist. If you build agent products with a UI, also look at AG-UI, the competing approach that the blip compares it with.

## Review the blip

- [ ] **~10 min** · Re-read [MCP Apps](https://www.thoughtworks.com/radar/platforms/mcp-apps) now that you know the topic.
