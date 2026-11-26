- **Blip:** [Open Data Contract Standard (ODCS)](https://www.thoughtworks.com/radar/languages-and-frameworks/open-data-contract-standard-odcs)
- **Time:** ~1 hour 30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Adopt
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what a data product is, roughly as in data mesh.

---

## Current state (late 2026)

A data contract describes a dataset the way an API specification describes a service: its schema, quality rules, service levels, owners and terms of use, in a form that tools can check. The idea spread in the early 2020s, with several competing formats. ODCS, a YAML standard that started at PayPal and is now developed by the Linux Foundation's Bitol project, has become the leading one: the maintainers of Data Contract CLI are dropping their own format in favor of it. The blip is new in November 2026, straight into *Adopt*. One reason for the interest is AI: a declarative contract is easy for agents to read, check and work with.

## Level 1 — What a data contract is (~50 min)

An agreed, machine-checkable description of a dataset: what's in it, how good it is, who owns it, and how you may use it.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/open-data-contract-standard-odcs) (~1 min) — note the companion standard for data products, ODPS.
- [ ] **~45 min** · Read: [Data Contracts](https://martinfowler.com/articles/data-contracts.html) (Simon Harrer and Arif Wider, martinfowler.com, Nov 2026, ~35 min) — a thorough introduction, with a running example in ODCS. Read "Why We Need Data Contracts" and "What's in a Data Contract" closely, and skim the rest. Note that the lead author sits on the ODCS steering committee and runs a company in this space.

## Level 2 — Write one (~40 min)

- [ ] **~40 min** · **Do:** Pick a dataset you know, such as a table your team publishes. Using the [ODCS specification](https://bitol-io.github.io/open-data-contract-standard/latest/) and its full example as a guide, write a short contract for it: the schema, two quality rules, an owner and a freshness guarantee. Then ask a coding agent to check a sample of the data against your contract, and see what it finds.

## Wrap-up

This plan is enough for a generalist. Testing and enforcing contracts automatically is covered in [[Data Contract CLI]].

## Review the blip

- [ ] **~5 min** · Re-read [Open Data Contract Standard (ODCS)](https://www.thoughtworks.com/radar/languages-and-frameworks/open-data-contract-standard-odcs) now that you know the topic.

## Related blips

- **[[Data Contract CLI]]**: its maintainers are deprecating their own format in favor of ODCS.
