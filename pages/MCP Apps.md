- **Time:** ~1.5 hours
- **Radar edition:** April 2026
- **Blip:** [MCP Apps](https://www.thoughtworks.com/radar/platforms/mcp-apps)
- **Quadrant:** Platforms
- **Ring:** Assess
- **Created:** 2026-10-21

---

## Current state of the topic (as of 2026-11-15)

MCP Apps grew out of the community project MCP-UI and OpenAI's similar work for ChatGPT apps. It became the first official MCP extension in January 2026, with Anthropic and OpenAI developing it together. It's already supported by Claude, ChatGPT, VS Code Copilot, Goose and others, and FastMCP supports it too. It's still young: the Radar puts it in *Assess*, and host support differs from client to client. It's the clearest example of something only MCP can do, which makes it a useful counterpoint to [[MCP by default]].

---

## Level 1 — What MCP Apps are, and why (0:00–0:30, ~30 min)

**Goal:** Explain how an MCP tool can show an interactive UI inside the chat, and why that was worth the first official MCP extension.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/mcp-apps) (~1 min) — `ui://` resources, sandboxed iframes, and a text fallback. It also asks whether the extra complexity is worth it.
- [ ] **~10 min** · **Do:** In Claude (even on the free plan), add an interactive connector for a tool you already use, such as Figma, Canva, Slack or Asana, and ask it to show you something. Notice what's interactive and what's plain text. If you don't use any of those tools, read [the announcement](https://claude.com/blog/interactive-tools-in-claude) (Anthropic, Jan 2026, ~4 min) instead, which describes what each one shows.
- [ ] **~15 min** · Read: [MCP Apps – Bringing UI capabilities to MCP clients](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/) (official MCP blog, Jan 2026, ~8 min) — the announcement of the extension, and where it came from.

## Level 2 — How they work (0:30–1:30, ~60 min)

**Goal:** Know the flow (the tool declares a UI, the host fetches and sandboxes it, the app calls tools back), and see it in a working app.

- [ ] **~20 min** · Read: [MCP Apps are here: Rendering interactive UIs in AI clients](https://workos.com/blog/2026-01-27-mcp-apps) (Maria Paktiti, WorkOS, Jan 2026, ~6 min) — the flow, with short code samples, and when a UI beats plain text.
- [ ] **~40 min** · **Do:** Pick a small example from the [ext-apps examples](https://github.com/modelcontextprotocol/ext-apps/tree/main/examples), such as `qr-server` or `basic-server-vanillajs`. Run it as its README explains, and connect it to Claude Desktop. Find the three steps of the flow in its code. Then answer the blip's question for a small tool you might write, such as one that tells you how far along you are with a Radar edition: would a progress-bar UI be worth it, or is text enough? If the setup takes more than 30 minutes, stop and just read the example's code.

---

## If you have extra time

- [ ] **~20 min** · Read: [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview) (official docs, ~6 min) — the page the blip links to. It's the full reference, and longer than you need if the WorkOS article was clear.
- [ ] **~15 min** · Skim the [build guide](https://modelcontextprotocol.io/extensions/apps/build) (~10 min) to see what adding a UI to your own server would take.

---

## Recommendation for future learning

This plan covers it for a generalist. If you build agent products with a UI, also look at AG-UI, the competing approach that the blip compares it with.

Related Radar topics:

- [[Model Context Protocol (MCP)]]
- [AG-UI Protocol](https://www.thoughtworks.com/radar/platforms/ag-ui-protocol)
- [[MCP by default]]

---

- [ ] **~10 min** · **Close:** [Review the blip](https://www.thoughtworks.com/radar/platforms/mcp-apps) — reread it now that you know the topic. Check that you understand every point it makes, and whether you agree with its ring.
