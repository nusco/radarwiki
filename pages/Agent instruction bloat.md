- **Blip:** [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat)
- **Time:** ~55 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Caution
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on [[AGENTS.md]], where you wrote and pruned an instruction file.

---

## Current state (late 2026)

Instruction files for coding agents, like `AGENTS.md`, `CLAUDE.md` and process skills, tend to grow: every mistake adds a rule, and teams import rule sets from the internet. In April 2026 the Radar warned that long instruction files get ignored and contradict themselves. In November 2026 it added a new argument: newer models follow instructions so well that many old rules aren't needed anymore. Anthropic reported removing over 80% of Claude Code's own system prompt for its latest models, with no measurable loss. So the advice now is to re-check your instructions against every new model, and delete what it doesn't need.

## Level 1 — What it is (~25 min)

Instructions that only grow become long, contradictory and stale, and the agent follows them less.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) (~2 min) — read both versions. Note the November 2026 advice: turn what you can into deterministic hooks or checks, then re-test the rest against each new model ("progression testing").
- [ ] **~20 min** · Read: [The new rules of context engineering for Claude 5 generation models](https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/) (Thariq Shihipar, Anthropic, Jul 2026, 7 min) — the post behind the "over 80%" figure. It shows how Anthropic replaced rules with judgment in its own prompts, and suggests doing the same in `CLAUDE.md` files and skills. It's a vendor post, but with real examples from Claude Code's prompt.

## Level 2 — Prune your instructions (~30 min)

Shrink an instruction file you use, without losing what matters.

- [ ] **~30 min** · **Do:** Take your largest instruction file. For each rule, decide: can a hook, linter or test enforce it instead? Move those. For the rest, delete the rule and see whether your current model still does the right thing in a session where it matters. Put back only what you really need. Note how many lines you started with, and how many are left.

Loading the remaining instructions only when they're needed is covered in [[Progressive context disclosure]], and keeping the file in shape over time in [[Feedback flywheel]].

## Wrap-up

This plan covers it. The blip also links to a 2026 study comparing handwritten and generated `AGENTS.md` files. A similar study is covered in Level 3 of [[AGENTS.md]], so I left it out.

## Review the blip

- [ ] **~5 min** · Re-read [Agent instruction bloat](https://www.thoughtworks.com/radar/techniques/agent-instruction-bloat) now that you know the topic.

## Related blips

- **[[Progressive context disclosure]]**: keeps the remaining instructions out of the context until they're needed.
- **[[Agent skill cognitive surrender]]**: importing external instruction sets wholesale makes bloat worse.
- **[[Harness quality evaluation]]**: the way to re-evaluate instructions against each new model.
- **[[Claude Code]]**: Anthropic removed most of its system prompt for newer models.
- **[[AGENTS.md]]**: one of the instruction files that tends to bloat.
