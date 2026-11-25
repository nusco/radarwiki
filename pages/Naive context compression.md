- **Blip:** [Naive context compression](https://www.thoughtworks.com/radar/techniques/naive-context-compression)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on [[Context profiling]], which measures where your agent's tokens go.

---

## Current state (late 2026)

As token prices rose in 2026, tools appeared that shrink what goes into an agent's context: proxies that compress prompts, and filters that cut command output. Some are very popular. The blip, new in November 2026, warns against using them without measuring. The main trap is prompt caching: most of an agent's input is a cached prefix that's cheap to resend, and a tool that rewrites that prefix can break the cache and raise the bill while lowering the token count.

## Level 1 — What it is (~10 min)

Shrinking the context with tools, without checking what happens to caching, accuracy and latency.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/naive-context-compression) (~2 min) — note the three problems (broken caching, lost information, extra LLM calls), and what to prefer instead: compress tool outputs while keeping references to the raw data, and prune history only at task boundaries.

## Level 2 — Why caching changes the math (~35 min)

Understand how prompt caching works, and check a compression tool against it.

- [ ] **~15 min** · Read: [Prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) (Claude docs, ~5 min for these sections) — read "How prompt caching works" and the table on what invalidates the cache. The key point: the cache matches a prefix, so any change near the start invalidates everything after it. That's why a tool that edits early parts of the context can cost more.
- [ ] **~20 min** · **Do:** Skim the README of [RTK](https://github.com/rtk-ai/rtk), one of the tools the blip names, which filters command output before the agent reads it. Decide where it sits in the context (at the start, or in new tool outputs at the end), and whether it can break the cache. Note its own caveat: cutting command output by 90% isn't cutting cost by 90%. If you try it, compare `/usage` for a session with and without it.

## Wrap-up

This plan covers it. Measuring before you optimize is covered in [[Context profiling]].

## Review the blip

- [ ] **~5 min** · Re-read [Naive context compression](https://www.thoughtworks.com/radar/techniques/naive-context-compression) now that you know the topic.

## Related blips

- **[[Context profiling]]**: the measurement to do before adopting any compression tool.
