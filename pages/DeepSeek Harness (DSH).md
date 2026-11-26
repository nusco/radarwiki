- **Blip:** [DeepSeek Harness (DSH)](https://www.thoughtworks.com/radar/tools/deepseek-harness-dsh)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what an agent harness is, from [[Coding harness for general-purpose agents]].

---

## Current state (late 2026)

DeepSeek, the Chinese AI lab known for its open-weight models, released its own open-source agent runtime in 2026. DeepSeek Harness is built on a plugin framework called Cordis: the model adapter, the tool registry, the session log and even the agent loop are all plugins, which you combine and override in YAML. Every interaction is recorded in an append-only log, so runs can be inspected, resumed, forked and replayed. The blip is new in November 2026. The project is a developer preview, and its README warns of breaking changes.

## Level 1 — What it is (~10 min)

An agent runtime where everything, including the agent loop, is a replaceable plugin, and every step is logged.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/deepseek-harness-dsh) (~2 min) — note why it could suit [[Enterprise harness|enterprise]] and [[Self-improving harness|self-improving]] harnesses: composable plugins and full observability.
- [ ] **~5 min** · Skim: [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness) (DeepSeek, README) — how to run it, and the developer-preview warning.

## Level 2 — Try it (~20 min)

Run a task, and read everything the session log recorded.

- [ ] **~20 min** · **Do:** Run it with `npx @deepseek-ai/dsh web`, give it a small task, and then look at the session log: can you see every prompt, context injection and tool call? Compare with what your usual agent lets you see.

## Wrap-up

This plan covers it, for now: the project is young. Its PTC mode is covered in [[Programmatic tool calling]].

## Review the blip

- [ ] **~5 min** · Re-read [DeepSeek Harness (DSH)](https://www.thoughtworks.com/radar/tools/deepseek-harness-dsh) now that you know the topic.

## Related blips

- **[[Self-improving harness]]**: DSH's composable, observable design could be a foundation for one.
- **[[Enterprise harness]]**: likewise, for domain-specific enterprise harnesses.
