- **Blip:** [Open-weight models](https://www.thoughtworks.com/radar/techniques/open-weight-models)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

"Open weight" means that anyone can download a model's trained weights and run it, which is less than fully open source: the training data and code usually stay private. Meta's Llama made the idea popular in 2023, and DeepSeek's R1 made it impossible to ignore in early 2025. Since then the strongest open-weight models have come mostly from Chinese labs (DeepSeek, Qwen, GLM, Kimi, MiniMax), usually under MIT-style licenses. Through 2026 they stayed roughly six months behind the closed frontier, and closer than that on coding. The blip is new in November 2026, and its message is that these models are no longer just a cheap fallback. The model names in this plan will date quickly, but the trade-offs won't.

## Level 1 — What it is, and where it stands (~35 min)

Learn what open weights give you beyond a lower price, and how far behind the closed frontier they are.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/open-weight-models) (~2 min) — list the benefits beyond cost: deployment flexibility, no vendor lock-in, data sovereignty, right-sizing, private fine-tuning.
- [ ] **~30 min** · Read: [Open models in perpetual catch-up](https://www.interconnects.ai/p/open-models-in-perpetual-catch-up) (Nathan Lambert, Interconnects, Feb 2026, ~8 min for the free part) — a researcher who builds open models explains the six-month gap, why benchmarks overstate open models, and where they can win. The end is paywalled: stop there.

## Level 2 — Try one on your own work (~40 min)

Form your own opinion, by running an open-weight model on a task you'd normally give a frontier model.

- [ ] **~40 min** · **Do:** Pick a recent model from one of the families the blip names (DeepSeek, GLM or Kimi), and use it through a hosted API or a coding agent that supports it. Give it two real tasks you did recently with your usual model, such as fixing a bug or writing a module with tests. Compare the results, the speed and the price, and write one sentence on which of your tasks you'd move to an open-weight model.

## If you have extra time

- [ ] **~15 min** · Read: [My bets on open models, mid-2026](https://www.interconnects.ai/p/my-bets-on-open-models-mid-2026) (Nathan Lambert, Interconnects, Apr 2026, ~5 min) — thirteen short predictions on where open models are going, including funding trouble at Chinese labs and calls to restrict open weights. Read it to see the risks behind the blip's optimism.

## Wrap-up

This plan is enough for a generalist. Running models yourself is a topic of its own, and smaller models are covered in [[Small language models]].

## Review the blip

- [ ] **~5 min** · Re-read [Open-weight models](https://www.thoughtworks.com/radar/techniques/open-weight-models) now that you know the topic.

## Related blips

- **[[GLM]]**: one of the open-weight model families that Thoughtworks teams evaluated with good results.
- **[[Blanket frontier model usage]]**: the habit of using the most powerful model for everything, which open-weight models help break.
