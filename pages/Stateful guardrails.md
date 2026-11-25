- **Blip:** [Stateful guardrails](https://www.thoughtworks.com/radar/techniques/stateful-guardrails)
- **Time:** ~1 hour
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Guardrails for LLM applications usually check one message at a time: the user's input, or the model's output. In 2024 researchers at Microsoft showed a jailbreak called Crescendo, which escalates slowly over many harmless-looking turns, and per-message checks miss it by design. Since then, defenses have moved toward judging the whole conversation. In 2026 a research framework gave the idea a name and a benchmark, and Thoughtworks teams used it in a production assistant. The blip is new in November 2026, and the technique is still young: thresholds need tuning, and every check adds latency and cost.

## Level 1 — What it is (~10 min)

Check the recent conversation, not just the latest message, and remember strikes across the session.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/stateful-guardrails) (~2 min) — note where the check runs (as a gate before the agent acts, next to the usual input and output guardrails) and the costs it lists.

## Level 2 — Why per-message checks fail (~50 min)

Understand the attack that makes stateful guardrails necessary, and design one for an assistant.

- [ ] **~25 min** · Read: [How Microsoft discovers and mitigates evolving attacks against AI guardrails](https://www.microsoft.com/en-us/security/blog/2024/04/11/how-microsoft-discovers-and-mitigates-evolving-attacks-against-ai-guardrails/) (Mark Russinovich, Microsoft, Apr 2024, 7 min) — read "Mitigating multiturn threats": Crescendo, the attack that works because no single message looks harmful, and the conversation-level filter Microsoft built against it. It's a vendor blog, but by the researcher who led the work.
- [ ] **~10 min** · Skim: [Stateful Guardrails for Multi-Turn LLM Systems](https://arxiv.org/abs/2607.19361) (Sanjay Mishra, Divya Chukkapalli and Ganesh R. Naik, Jun 2026) — the paper the blip links to. Read only the abstract, for the three patterns it tracks across turns: drifting intent, harmful instructions split into fragments, and sensitive information building up.
- [ ] **~15 min** · **Do:** Pick an assistant you know or could build, like a support bot with access to customer accounts. Write three short conversations in which every message passes a per-message check, but the conversation as a whole should be stopped. Then write the policy a stateful guardrail would apply: what it looks at, when it gives a strike, and what happens after how many strikes.

## Wrap-up

This plan covers the technique. Single-message guardrails are covered in [[LLM Guardrails]], and tracing guardrail decisions in [[Langfuse]].

## Review the blip

- [ ] **~5 min** · Re-read [Stateful guardrails](https://www.thoughtworks.com/radar/techniques/stateful-guardrails) now that you know the topic.

## Related blips

- **[[Langfuse]]**: Thoughtworks teams traced their stateful guardrails' decisions in it.
- **[[LLM Guardrails]]**: the single-turn guardrails that stateful guardrails extend.
