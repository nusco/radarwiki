- **Blip:** [KServe](https://www.thoughtworks.com/radar/platforms/kserve)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[llm-d]], which explains inference-aware routing.

---

## Current state (late 2026)

KServe started in 2019 as KFServing, part of the Kubeflow project, and is now a CNCF incubating project. It's a Kubernetes operator for serving models: it doesn't run models itself, but manages the inference engines that do (vLLM, SGLang, NVIDIA Triton) through custom resources. In 2026 it added a second resource for large language models, built on [[llm-d]], with multi-node inference, prefill/decode disaggregation and KV-cache-aware routing. The blip is new in November 2026, in *Trial*: several Thoughtworks clients run it in production, and it's the team's preferred base for in-house inference platforms. The LLM resource is newer, and still evolving.

## Level 1 — What it is (~10 min)

A Kubernetes operator that manages model serving as declarative resources, for classic ML models and LLMs.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/kserve) (~2 min) — note the two resources: `InferenceService` for conventional models and simple LLMs, `LLMInferenceService` for advanced LLM serving.

## Level 2 — Try it (~40 min)

- [ ] **~40 min** · **Do:** On a local cluster, follow the [Quickstart Guide](https://kserve.github.io/website/docs/getting-started/quickstart-guide) (KServe docs, for experiments only). Deploy a small model as an `InferenceService`, send it a request, and look at what KServe created underneath. Then read the YAML of an `LLMInferenceService` example, and note which llm-d features it exposes. You don't need a GPU for the first part.

## Wrap-up

This plan covers it for a generalist. A narrower operator for self-hosting open-weight models is covered in [[KAITO]].

## Review the blip

- [ ] **~5 min** · Re-read [KServe](https://www.thoughtworks.com/radar/platforms/kserve) now that you know the topic.

## Related blips

- **[[llm-d]]**: KServe's LLM resource is built on it.
- **[[SGLang]]**: one of the serving runtimes KServe orchestrates.
- **[[vLLM]]**: another.
- **[[Knative]]**: provides KServe's optional scale-to-zero.
