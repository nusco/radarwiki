- **Blip:** [Apple Core AI](https://www.thoughtworks.com/radar/languages-and-frameworks/apple-core-ai)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Small language models]], which covers the models that fit on a device.

---

## Current state (late 2026)

Apple has let developers run machine learning models on its devices since 2017, with Core ML. Core AI, released with Apple's 2026 operating systems, is its successor for modern AI models: a Swift framework that runs them on the device's CPU, GPU and Neural Engine, with tools to convert models from PyTorch, profile them in Xcode and debug them. Data stays on the device, features work offline, and there's no cost per request. The blip is new in November 2026, and singles out the Evaluations framework, which lets you test generative AI features inside Xcode's own testing tools. Core ML remains for older model types, like decision trees.

## Level 1 — What it is (~10 min)

Apple's framework for running AI models in your app, on the device.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/apple-core-ai) (~1 min) — note the Evaluations framework, for testing generative features with datasets, metrics and a model as judge.
- [ ] **~5 min** · Skim: [Core AI](https://developer.apple.com/documentation/coreai) (Apple docs) — the overview: the framework, the tools around it, and where Core ML still fits.

## Level 2 — How an app uses it (~25 min)

- [ ] **~25 min** · Read: [Integrating on-device AI models in your app with Core AI](https://developer.apple.com/documentation/coreai/integrating-on-device-ai-models-in-your-app-with-core-ai) (Apple docs, ~8 min) — the steps from a model file to running inference in Swift. If you build iOS apps, follow along in Xcode with a model from Apple's catalog. If you don't, note which steps would be new to you compared with calling a cloud API.

## Wrap-up

This plan is enough unless you build for Apple platforms.

## Review the blip

- [ ] **~5 min** · Re-read [Apple Core AI](https://www.thoughtworks.com/radar/languages-and-frameworks/apple-core-ai) now that you know the topic.
