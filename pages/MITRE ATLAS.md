- **Blip:** [MITRE ATLAS](https://www.thoughtworks.com/radar/techniques/mitre-atlas)
- **Time:** ~45 minutes
- **Radar edition:** April 2026 and November 2026
- **Quadrant:** Techniques
- **Ring:** Assess
- **Updated:** 2026-11-25
- **Status:** #undone

This plan builds on Level 3 of [[Threat modeling]], where you threat-modeled an LLM feature.

---

## Current state (late 2026)

ATLAS started in 2020 as the "Adversarial ML Threat Matrix", a collaboration between MITRE and Microsoft, and became ATLAS in 2021. It's the AI-focused sibling of MITRE ATT&CK, the standard catalog of attacker tactics and techniques in security. For years it covered mostly attacks on machine learning models, like poisoning and model theft. Since late 2025 it has grown fast in the direction of agents, with techniques such as poisoned agent tools and prompt injection through tools, and case studies of real incidents. It releases new versions several times a year, so counts and IDs in older articles are out of date.

## Level 1 — What it is (~10 min)

ATLAS is a shared vocabulary of how attackers target AI systems, grounded in real incidents, that you can use during threat modeling.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/mitre-atlas) (~2 min) — the April and November 2026 versions are the same. Note the problem it solves: without a shared vocabulary, AI security becomes a checkbox exercise.

## Level 2 — Use it (~35 min)

Find your way around the matrix, and use it to check a threat model.

- [ ] **~15 min** · Skim: [MITRE ATLAS](https://atlas.mitre.org/) (MITRE) — open the matrix: tactics are the columns (the attacker's goals), techniques the cells. Click "LLM Prompt Injection" and read its description and one linked case study. The site renders in the browser, so it may not load in a text-only reader.
- [ ] **~20 min** · **Do:** Take the threats you listed for the LLM feature in Level 3 of [[Threat modeling]]. Map each one to an ATLAS technique, and look for techniques in the matrix that your list missed. Add the ones that apply.

## Wrap-up

This plan covers it: ATLAS is a reference to use during threat modeling, not something to study on its own. Google's [[SAIF]] is a complementary framework of controls, where ATLAS describes threats.

## Review the blip

- [ ] **~5 min** · Re-read [MITRE ATLAS](https://www.thoughtworks.com/radar/techniques/mitre-atlas) now that you know the topic.

## Related blips

- **[[SAIF]]**: a control framework that ATLAS naturally complements, by describing the threats.
