- **Blip:** [Programmatic tool calling](https://www.thoughtworks.com/radar/techniques/programmatic-tool-calling)
- **Time:** ~1 hour 20 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan assumes that you know how agents call tools through [[Model Context Protocol (MCP)]].

---

## Current state (late 2026)

The idea appeared in late 2025, almost at the same time at Cloudflare ("Code Mode") and Anthropic ("code execution with MCP"): instead of calling tools one at a time, with every result passing through the model, the model writes a small program that calls the tools, and only the final result comes back. In 2026 it spread fast, under different names. Anthropic's API calls it programmatic tool calling, [[Pi]] 1.0 built MCP support on a "Codemode" sandbox, and [[DeepSeek Harness (DSH)]] has a "PTC Mode". The blip is new in November 2026. The open questions are where the code runs (at the model provider, in the agent harness, or in an MCP server), and how to keep fine-grained approvals when many tool calls hide inside one program.

## Level 1 — What it is (~35 min)

Let the model write code that calls tools, loops and filters, so that intermediate results never enter its context.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/programmatic-tool-calling) (~2 min) — note the three places the code can run, and the warning about approvals.
- [ ] **~30 min** · Read: [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) (Adam Jones and Conor Kelly, Anthropic, Nov 2025, ~10 min) — the clearest explanation of the benefits: the agent loads only the tool definitions it needs, filters large data before it reaches the model, and can keep data private. It also admits the cost: you now need a sandbox to run the code.

## Level 2 — How it's built (~45 min)

See a full implementation, and the API version of the same idea.

- [ ] **~35 min** · Read: [Code Mode: the better way to use MCP](https://blog.cloudflare.com/code-mode/) (Kenton Varda and Sunil Pai, Cloudflare, Sep 2025, ~12 min) — the other origin of the technique. It turns an MCP server's tools into a TypeScript API, and runs the model's code in a sandbox with no internet access. Read it for the design: why models are better at writing code than at calling tools, and how the sandbox reaches the tools. It's a product launch, so it's light on numbers.
- [ ] **~10 min** · Skim: [Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) (Claude docs) — read "How programmatic tool calling works" and "Core concepts", to see how the technique looks when the model provider runs the code for you.

## Wrap-up

This plan is enough for a generalist. The approval problem the blip mentions is a security question, covered more broadly in [[Agent sandboxing]].

## Review the blip

- [ ] **~5 min** · Re-read [Programmatic tool calling](https://www.thoughtworks.com/radar/techniques/programmatic-tool-calling) now that you know the topic.

## Related blips

- **[[Pi]]**: calls the technique Code Mode, and uses it for its built-in MCP support.
- **[[DeepSeek Harness (DSH)]]**: offers a closely related PTC Mode.
