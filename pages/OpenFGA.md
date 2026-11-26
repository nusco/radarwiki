- **Blip:** [OpenFGA](https://www.thoughtworks.com/radar/languages-and-frameworks/openfga)
- **Time:** ~55 minutes
- **Radar edition:** November 2026
- **Quadrant:** Languages & Frameworks
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Role-based access control (RBAC) works until permissions depend on relationships: "Alice can edit this document because she's in the team that owns the folder it's in". In 2019 Google described Zanzibar, the system behind permissions in Drive, YouTube and other products, which stores relationships between users and objects and answers permission checks from them. Several open-source systems copied the model. OpenFGA, which started at Auth0 and is now a CNCF project, is one of the main ones, next to SpiceDB. The blip is new in November 2026, after production use with a sidecar deployment for fast checks.

## Level 1 — What it is (~15 min)

Fine-grained authorization based on relationships, in the style of Google's Zanzibar.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/languages-and-frameworks/openfga) (~1 min) — note when to reach for it: when RBAC isn't enough.
- [ ] **~10 min** · Read: [What is Google Zanzibar?](https://openfga.dev/docs/learn/zanzibar) (OpenFGA docs, ~3 min) — what the Zanzibar paper described, and how OpenFGA maps to it and differs from it.

## Level 2 — Model some permissions (~40 min)

- [ ] **~40 min** · **Do:** Run OpenFGA locally with `openfga run`, which starts its [Playground](https://openfga.dev/docs/getting-started/setup-openfga/playground) at `localhost:3000/playground`. Model a small app you know, such as documents in folders, owned by teams, with viewers and editors. Write a few relationships, and check questions like "can Bob edit this document?" and "which documents can Alice see?". Note which rules would have been awkward in plain RBAC.

## Wrap-up

This plan covers it for a generalist. Running it in production needs more: choosing a storage backend, and deciding where checks happen.

## Review the blip

- [ ] **~5 min** · Re-read [OpenFGA](https://www.thoughtworks.com/radar/languages-and-frameworks/openfga) now that you know the topic.
