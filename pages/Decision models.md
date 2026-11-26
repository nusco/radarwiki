- **Blip:** [Decision models](https://www.thoughtworks.com/radar/platforms/decision-models)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

LLMs are often used for jobs that only need a structured answer: yes or no, one of a few categories, or a score. "Decision models" are a new class of model, which appeared in the second half of 2026, built for exactly that. The first, TypeSafe's Jev, calls itself a "system one" model: it returns probabilities instead of text, quickly and cheaply, and is trained to be well calibrated, so a 70% means it's right about 70% of the time. Others followed, including open-source ones. The blip is new in November 2026. The claims so far come mostly from the vendors' own evaluations.

## Level 1 — What it is (~25 min)

Models that answer structured questions with calibrated probabilities, instead of generating text.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/decision-models) (~2 min) — note the three question types (yes/no, choice, score) and the use cases: judging, routing, policy gates, bulk labeling.
- [ ] **~20 min** · Read: [Introducing System One Models & Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev) (Diogo Almeida, TypeSafe, Sep 2026, ~8 min) — the founder's launch post. Read it for the idea, and the "Nuance" notes where he admits the limits of his own evaluations. Skip the speed and cost multipliers, which are self-measured, and the claim that it "can't hallucinate".

## Level 2 — Decide where it fits (~15 min)

- [ ] **~15 min** · **Do:** List three places where you, or a system you know, use an LLM to classify or decide something: routing a request, judging an output, labeling data. For each, write the structured question a decision model would answer, and how you'd test it against your current LLM before switching, as the blip recommends.

## Wrap-up

This plan covers it, for a very new category. Using LLMs where they don't belong is covered in [[Overenthusiastic LLM use]].

## Review the blip

- [ ] **~5 min** · Re-read [Decision models](https://www.thoughtworks.com/radar/platforms/decision-models) now that you know the topic.

## Related blips

- **[[LLM as a judge]]**: one of the uses where a decision model could replace an LLM.
- **[[Overenthusiastic LLM use]]**: decision models are one way to avoid it for classification.
