- **Blip:** [Local coding models](https://www.thoughtworks.com/radar/techniques/local-coding-models)
- **Time:** ~1 hour 20 minutes
- **Radar edition:** April 2025 and November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on [[Small language models]] and [[Open-weight models]], and reuses the local model runner from the Small language models exercise.

---

## Current state (late 2026)

In April 2025 the Radar put "local coding assistants" on *Hold*: models small enough for a laptop couldn't handle real coding work, and most couldn't call tools at all. That changed in 2026, when open-weight mixture-of-experts models in the 25–35B range (Qwen, Gemma) became good enough to drive a coding agent on a well-equipped laptop. The November 2026 blip moves to *Assess*, but for a narrow role: not replacing frontier models, but handling the tasks that don't need one, like indexing code, parsing logs, first drafts and reviewing diffs. The early reports agree: it works for small, well-specified tasks, and tool calling is still the weak point.

## Level 1 — What it is (~10 min)

Run a coding model on your own machine, for the workloads that don't need a frontier model.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/local-coding-models) (~2 min) — read both versions. April 2025 explains why it was on *Hold*, and November 2026 lists the tasks where local models now pay off.

## Level 2 — How far they get (~1 hour 10 minutes)

Learn from two careful experiments, then run your own.

- [ ] **~20 min** · Read: [LLMs running on my laptop can drive coding agents now](https://simonpcouch.com/blog/2026-04-16-local-agents-2/) (Simon P. Couch, Apr 2026, ~6 min) — a developer reruns his small agent benchmark and finds local models jumping from 0% to about 90% in four months. Note the hardware, and his caveat that the eval is one task.
- [ ] **~30 min** · Read: [Experiences with local models for coding](https://martinfowler.com/articles/exploring-gen-ai/local-models-for-coding-experiences.html) (Birgitta Böckeler, martinfowler.com, 2026, ~10 min) — four weeks of agentic coding with local models, by a Thoughtworks engineer. It's more sobering: simple tasks sometimes worked, harder ones often failed, and tool calling was unreliable. Read it for the "viability funnel", the steps to decide whether local models fit your setup.
- [ ] **~20 min** · **Do:** In the runner from [[Small language models]], download a local coding model that fits your machine's memory, and connect a coding agent that supports local models, such as OpenCode or [[Pi]]. Give it one of the blip's tasks: review the diff of your last commit, or summarize a log file. Compare it with your usual model, and decide whether this task could move to your laptop.

## Wrap-up

This plan covers it. What models to use for which task is the theme of [[Blanket frontier model usage]].

## Review the blip

- [ ] **~5 min** · Re-read [Local coding models](https://www.thoughtworks.com/radar/techniques/local-coding-models) now that you know the topic.

## Related blips

- **[[Blanket frontier model usage]]**: local models are a way to stop using a frontier model for everything.
- **[[Open-weight models]]**: local coding models are open-weight models that fit on a developer's machine.
