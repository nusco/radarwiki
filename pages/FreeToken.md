- **Blip:** [FreeToken](https://www.thoughtworks.com/radar/tools/freetoken)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Local coding models]], and assumes that you have an NVIDIA GPU if you want to try it.

---

## Current state (late 2026)

Many of the strongest open-weight models in 2026 are mixture-of-experts (MoE) models: hundreds of billions of parameters, but only a small part of them active for each token. Their weights don't fit in a consumer GPU's memory. FreeToken is an open-source inference engine, from an academic team, that runs them anyway: it keeps the active experts on the GPU and swaps the others in from system memory as needed. The blip is new in November 2026. General runners like llama.cpp (and Ollama, which uses it) are adding similar offloading, so FreeToken's advantage may shrink.

## Level 1 — What it is (~5 min)

Run very large MoE models on consumer hardware, by caching the active experts on the GPU.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/freetoken) (~1 min) — note how it differs from general-purpose local runners.

## Level 2 — Try it (~25 min)

Run a model too big for your GPU, or work out why you'd need to.

- [ ] **~25 min** · **Do:** If you have a recent NVIDIA GPU, install [FreeToken](https://github.com/FlashML-org/FreeToken) and run one of the MoE models it supports, then compare its speed with the same model in Ollama or llama.cpp. If you don't, look up the total and active parameters of two MoE models you've heard of, and work out roughly how much memory each needs with and without expert offloading.

## Wrap-up

This plan covers it. I didn't use FreeToken's README as reading material: it's mostly marketing, with no benchmark numbers. General local runners are covered in [[Ollama]].

## Review the blip

- [ ] **~5 min** · Re-read [FreeToken](https://www.thoughtworks.com/radar/tools/freetoken) now that you know the topic.

## Related blips

- **[[Ollama]]**: a general-purpose local runner that's gaining similar offloading through llama.cpp.
