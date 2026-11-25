- **Blip:** [Threat modeling](https://www.thoughtworks.com/radar/techniques/threat-modeling)
- **Time:** ~3.5 hours
- **Radar edition:** May 2015, November 2015, April 2016, November 2016, October 2022, April 2025 and November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

Threat modeling is one of the Radar's longest-running blips: it reached *Adopt* in November 2015 and has stayed there. What changed is the reason it keeps coming back. In 2022 the point was to repeat it regularly instead of doing it once. Since 2025 the point is AI: LLMs and agents add new attack paths, like prompt injection and over-privileged tools, that classic models miss. The November 2026 version asks for regular, human-led sessions, with agents helping but not leading. The method itself hasn't changed much in a decade, so older material is still valid.

## Level 1 — What it is, and why (~35 min)

Threat modeling means thinking about what can go wrong with a system while you can still change its design.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/threat-modeling) (~2 min for the current version) — then skim the older versions, to see how the advice moved from "do it" (2015) to "keep doing it" (2022) to "especially for AI" (2025–2026).
- [ ] **~5 min** · Watch: [The Four Question Framework for Threat Modeling](https://youtu.be/Yt0PhyEdZXU) (Adam Shostack, ~1 min) — the four questions most practitioners use to frame the whole activity, from the author of the standard book on threat modeling. Learn them by heart: everything else in this plan answers one of them.
- [ ] **~20 min** · Read: [Threat Modeling Manifesto](https://threatmodelingmanifesto.org/) (Shostack, Tarandach, Wuyts and others, ~7 min) — a short statement of values, patterns and anti-patterns by fifteen practitioners. Stop at "About". The anti-patterns, like the "Hero Threat Modeler", are the part you'll recognize from real teams.

## Level 2 — Run a session (~2 hours)

Run a lightweight threat modeling session on a real system, with dataflows and STRIDE.

- [ ] **~1.25 hours** · Read: [Threat Modeling Guide for Software Teams](https://martinfowler.com/articles/agile-threat-modelling.html) (Gayathri Mohan and Jim Gumbley, martinfowler.com, May 2025, ~25 min) — the article the blip links to, by Thoughtworks security practitioners. It's the most concrete guide to the "little and often" style the Radar recommends: start from dataflows, use STRIDE to spot threats, and keep sessions short. Read "Breaking Down the Fundamentals" and "Quick Team Threat Modeling" closely, and skim the platform workshop.
- [ ] **~45 min** · **Do:** Threat model one feature of a system you know, following the guide's "Quick Team Threat Modeling" steps. Draw its dataflow diagram with trust boundaries, walk STRIDE across each boundary, and list at least six threats. Then pick the three that matter most and write one fix for each. Keep the diagram: Level 3 extends it.

## Level 3 — Threat modeling AI systems (~1 hour)

See where LLMs and agents move the trust boundaries, and extend your model to cover them.

- [ ] **~25 min** · Read: [Threat Modelling for AI — Changing the way you view Trust Boundaries](https://nazneen-rupawalla.gitbook.io/learn-write-share/security-bits/threat-modelling-for-ai-changing-the-way-you-view-trust-boundaries) (Nazneen Rupawalla, ~8 min) — linked from the blip. It explains why an LLM blurs trust boundaries, then turns each item of the OWASP Top 10 for LLMs into questions to ask in a session. Use those questions as a checklist for the exercise below.
- [ ] **~35 min** · **Do:** Add an LLM feature to your Level 2 diagram, such as a chatbot that reads customer data, or an agent that can call your APIs. Mark the new trust boundaries (prompts, retrieved documents, tool calls), run the checklist from the article, and add the new threats. Then answer the question the blip asks: for each threat, is the model's nondeterministic behavior acceptable here, or do you need a deterministic guardrail?

Mapping the flows between an agent's tools in detail is covered in [[Toxic flow analysis for AI]], and the catalog of real attacks on AI systems in [[MITRE ATLAS]].

## If you have extra time

- [ ] **~20 min** · Read: [The Four Question Framework (README)](https://github.com/adamshostack/4QuestionFrame) (Adam Shostack, ~2 min) — Shostack's notes on why the questions are worded the way they are, and how organizations use them. Follow one link from "In the real world" to see the framework in a company's own process.

## Wrap-up

This plan covers the practice for a generalist. If you'll lead threat modeling sessions yourself, read Adam Shostack's *Threat Modeling: Designing for Security* (Wiley, 2014): it's still the standard reference.

The blip also links to an AWS post on threat modeling generative AI workloads, and to CSA's MAESTRO framework. I left out the AWS post because it walks through the same method with AWS's own tooling, and MAESTRO because its write-up reads as generated: a template of layers and categories with few real examples. The Fowler guide and Rupawalla's checklist cover the same ground.

## Review the blip

- [ ] **~10 min** · Re-read [Threat modeling](https://www.thoughtworks.com/radar/techniques/threat-modeling) now that you know the topic.

## Related blips

- **[[MITRE ATLAS]]**: the blip suggests starting from known threats, and ATLAS catalogs the known attacks on AI systems.
- **[[Toxic flow analysis for AI]]**: applies threat modeling to the data flows between an agent's tools.
