- **Blip:** [CALM](https://www.thoughtworks.com/radar/languages-and-frameworks/calm)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Architecture diagrams and documents drift away from the systems they describe. "Architecture as code" tries to fix that by describing architecture in files that live with the code and can be checked. CALM (Common Architecture Language Model) is an open specification for that, from FINOS, the open-source foundation of the financial industry: a JSON schema for describing systems, their components and connections, in a way tools can validate. The blip is new in November 2026, and contrasts it with Mermaid: Mermaid draws diagrams from code, CALM gives a machine-readable model to check compliance and governance against.

## Level 1 — What it is (~10 min)

A standard, machine-readable way to describe software architecture, so it can be validated like code.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/calm) (~1 min) — note the use in large enterprises: decentralized architecture work, with a unified view when needed.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** Follow the first beginner tutorial on [calm.finos.org](https://calm.finos.org/) (Setup & CLI) to install the CLI, then the next one to describe your first node. Describe two parts of a system you know and the connection between them. Then decide what rule you'd want to validate automatically, such as "every database connection uses TLS".

## Wrap-up

This plan covers it. Diagrams as code are covered in [[Mermaid]].

## Review the blip

- [ ] **~5 min** · Re-read [CALM](https://www.thoughtworks.com/radar/languages-and-frameworks/calm) now that you know the topic.

## Related blips

- **[[Mermaid]]**: supports diagrams as code, where CALM provides a model to validate against.
