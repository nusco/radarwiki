- **Blip:** [llm-d](https://www.thoughtworks.com/radar/platforms/llm-d)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know the basics of Kubernetes, and roughly how LLM inference works (a model server like vLLM).

---

## Current state (late 2026)

A normal web service scales by adding identical replicas behind a load balancer. LLM inference doesn't work that way: each request builds a key-value (KV) cache, and sending a follow-up request to the replica that already holds the right cache is much cheaper. llm-d is an open-source stack, a CNCF sandbox project since March 2026, that runs model servers like vLLM and SGLang across many Kubernetes nodes with inference-aware routing. It also supports prefill/decode disaggregation: the compute-heavy first pass over the prompt runs on one set of GPUs, and the memory-bound token generation on another. It reached 1.0 in October 2026. The blip is new in November 2026.

## Level 1 — What it is (~10 min)

A distributed inference stack for Kubernetes that routes requests by cache and load, not round-robin.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/llm-d) (~2 min) — note why LLM inference is stateful, and what the routing takes into account (cache affinity, queue depth, predicted latency).

## Level 2 — The ideas behind it (~35 min)

Understand prefill/decode disaggregation, the stack's most distinctive idea, and where llm-d fits.

- [ ] **~20 min** · Read: [Prefill-decode disaggregation](https://handbook.modular.com/inference-optimization/prefill-decode-disaggregation/) (Modular, LLM Inference Handbook, ~6 min) — linked from the blip. It explains why prefill and decode compete when they share a GPU, why splitting them helps, and when it doesn't (small workloads, short prompts).
- [ ] **~15 min** · Skim: [llm-d](https://github.com/llm-d/llm-d) (README) — the capabilities and the architecture diagram. Its performance numbers come from partner blogs, so treat them as claims.

## Wrap-up

This plan is enough unless you build GPU inference platforms. The operator that uses llm-d underneath is covered in [[KServe]], and the model server in [[vLLM]].

## Review the blip

- [ ] **~5 min** · Re-read [llm-d](https://www.thoughtworks.com/radar/platforms/llm-d) now that you know the topic.

## Related blips

- **[[SGLang]]**: one of the model servers llm-d coordinates.
- **[[vLLM]]**: the other.
- **[[Kubernetes]]**: llm-d is built around it and its Gateway API Inference Extension.
