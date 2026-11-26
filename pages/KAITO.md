- **Blip:** [KAITO](https://www.thoughtworks.com/radar/platforms/kaito)
- **Time:** ~25 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[KServe]], the broader alternative.

---

## Current state (late 2026)

Self-hosting an open-weight model on Kubernetes usually means configuring GPU nodes, drivers and model servers by hand. KAITO (Kubernetes AI Toolchain Operator), a CNCF sandbox project that started at Microsoft in 2023, automates that: you declare a model and a GPU type, and it provisions matching nodes, estimates memory, and serves the model with vLLM behind an OpenAI-compatible endpoint. Its scope is narrow: node provisioning and model deployment, not the whole inference stack. It works best on Azure's AKS, and only supports recent NVIDIA GPUs and models hosted on Hugging Face. The blip is new in November 2026.

## Level 1 — What it is (~10 min)

Declare the model you want, and let an operator provision the GPU nodes and serve it.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/kaito) (~2 min) — note the use case (cheaper, faster small models on AKS) and how it differs from [[KServe]].

## Level 2 — How it works (~15 min)

- [ ] **~15 min** · Skim: [KAITO](https://github.com/kaito-project/kaito) (README) — the architecture, with the `Workspace` resource, and the stated limits. Then write down what you'd need to run one model with KAITO in your environment, and what KServe would add.

## Wrap-up

This plan is enough unless you self-host models on AKS. Small models, the blip's main use case, are covered in [[Small language models]].

## Review the blip

- [ ] **~5 min** · Re-read [KAITO](https://www.thoughtworks.com/radar/platforms/kaito) now that you know the topic.

## Related blips

- **[[Small language models]]**: teams use KAITO to host them at lower cost and latency.
- **[[KServe]]**: more mature for the broader inference stack.
- **[[vLLM]]**: the engine KAITO serves models with.
- **[[Karpenter]]**: provisions KAITO's GPU nodes.
- **[[Ollama]]**: what teams ran by hand on GPU machines before.
- **[[Kubernetes]]**: KAITO manages models with the same manifests as other workloads.
