- **Blip:** [GLM](https://www.thoughtworks.com/radar/tools/glm)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Open-weight models]].

---

## Current state (late 2026)

GLM is a family of open-weight models from Z.ai, a Chinese AI company. Its 2026 versions became some of the strongest open-weight models for coding, close to proprietary frontier models on many benchmarks. GLM-5.3, from mid-2026, is a mixture-of-experts model with about 750 billion parameters, much too large for a single consumer machine, so most people use it through hosted providers. The blip is new in November 2026. Thoughtworks teams found that it sometimes overthinks simple prompts, so they tune its reasoning effort to the task.

## Level 1 — What it is (~10 min)

One of the strongest open-weight model families for coding, from Z.ai.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/glm) (~1 min) — note where the gains come from (post-training, not just scale), and the advice on reasoning effort.
- [ ] **~5 min** · Skim: [GLM-5.3](https://huggingface.co/zai-org/GLM-5.3) (Z.ai, model card) — the size, the ways to serve it, and the notes on reasoning settings. The benchmarks are self-reported.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Use GLM through a hosted provider or a coding agent that supports it, such as [[OpenCode]]. Give it one simple task and one hard one. Try the simple task at the default reasoning effort and at a low one, and compare time, cost and result.

## Wrap-up

This plan covers it. Open-weight models in general are covered in [[Open-weight models]].

## Review the blip

- [ ] **~5 min** · Re-read [GLM](https://www.thoughtworks.com/radar/tools/glm) now that you know the topic.
