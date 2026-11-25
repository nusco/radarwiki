- **Blip:** [Small language models](https://www.thoughtworks.com/radar/techniques/small-language-models)
- **Time:** ~1 hour 15 minutes
- **Radar edition:** October 2024, April 2025, November 2025, April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Small language models (SLMs) have been on every Radar since late 2024, and their ring has moved back and forth between *Trial* and *Assess* as the argument shifted. In 2024 the point was privacy and edge devices. In 2025 it became agents: most agent steps are narrow and repetitive, so a small model can do them cheaper and faster. Small models keep getting better, mostly through better training data, distillation from large models, and quantization. There's no fixed size limit, but "small" usually means a few billion parameters or less, small enough to run on a laptop or phone. In November 2026 the blip is back in *Trial*, as teams use SLMs for summarization, extraction, classification and basic coding.

## Level 1 — What it is, and why now (~30 min)

Use the smallest model that does the job, and keep large models for tasks that need multi-step reasoning or reliable tool calling.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/small-language-models) (~2 min per version) — read the November 2026 version, then skim the older ones to see the argument move from privacy and edge devices (2024) to agents (2025–2026).
- [ ] **~20 min** · Read: [How Small Language Models Are Key to Scalable Agentic AI](https://developer.nvidia.com/blog/how-small-language-models-are-key-to-scalable-agentic-ai) (Peter Belcak, NVIDIA, Aug 2025, ~7 min) — a summary of the position paper "Small Language Models are the Future of Agentic AI", by its first author. The core argument is that agents split work into narrow subtasks, and a fine-tuned small model handles each one well. It's an NVIDIA blog, so skip the product mentions and the cost figures, which aren't backed up.

## Level 2 — Run one (~45 min)

See what a small model can and can't do, on your own machine.

- [ ] **~45 min** · **Do:** Install a local model runner (Ollama or LM Studio) and download a model under 4 billion parameters, such as a small Qwen, Gemma or Phi model. Give it the four kinds of task from the blip: summarize a long email, extract fields from an invoice into JSON, classify ten support requests by intent, and write a small function. Run the same prompts on a frontier model, and mark which tasks the small model handled well enough to use.

## If you have extra time

- [ ] **~45 min** · Read: [SmolLM - blazingly fast and remarkably powerful](https://huggingface.co/blog/smollm) (Loubna Ben Allal, Anton Lozhkov and Elie Bakouch, Hugging Face, Jul 2024, ~10 min) — how a team trained models as small as 135M parameters, with the data curation that the blip credits for progress. Read the data and evaluation sections.

## Wrap-up

This plan is enough for a generalist. How large models teach small ones is covered in [[Model distillation]], and running models on Apple devices in [[Apple Core AI]].

## Review the blip

- [ ] **~5 min** · Re-read [Small language models](https://www.thoughtworks.com/radar/techniques/small-language-models) now that you know the topic.

## Related blips

- **[[Apple Core AI]]**: runs small foundation models directly on Apple devices, the blip's example of SLMs at the edge.
- **[[Model distillation]]**: one of the main ways to make small models capable.
