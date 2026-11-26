- **Blip:** [Presidio](https://www.thoughtworks.com/radar/languages-and-frameworks/presidio)
- **Time:** ~45 minutes
- **Radar edition:** April 2025, November 2025 and November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Before sending text to an LLM, companies often need to find and remove personal data: names, phone numbers, credit cards, addresses. Presidio is an open-source toolkit for that, started at Microsoft, which detects personal data with a mix of named-entity recognition, regular expressions and rules, and then masks, replaces or redacts it. It's been on the Radar since April 2025, in *Trial* since November 2025. In 2026 it moved from Microsoft to a community-owned home (Data Privacy Stack), so old links to `microsoft.github.io/presidio` redirect. Every version of the blip repeats the same warning: it's not foolproof, and will miss or mislabel some data.

## Level 1 — What it is (~10 min)

Find and anonymize personal data in text before it reaches an LLM or leaves your systems.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/presidio) (~1 min per version) — read all three versions. Note the use case: strict data-sharing controls when integrating with LLMs.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** Work through the [Presidio Basic Usage Notebook](https://presidio.dataprivacystack.org/samples/python/presidio_notebook/) (Presidio docs): detect personal data in a sentence, add a custom recognizer, and anonymize with different operators. Then run it on a realistic sample, such as a few fake support tickets you write, and count what it missed and what it flagged by mistake.

## Wrap-up

This plan covers it. Protecting conversations with LLMs in other ways is covered in [[Stateful guardrails]].

## Review the blip

- [ ] **~5 min** · Re-read [Presidio](https://www.thoughtworks.com/radar/languages-and-frameworks/presidio) now that you know the topic.
