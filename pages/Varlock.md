- **Blip:** [Varlock](https://www.thoughtworks.com/radar/tools/varlock)
- **Time:** ~35 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

Coding agents read the files in a project, including `.env` files full of secrets. Varlock, an open-source tool from the makers of dmno, replaces informal `.env` conventions with a committed `.env.schema`: it describes each variable's name, type and validation, while the actual secrets are loaded at runtime from a vault such as 1Password or AWS Secrets Manager. When an agent must call an authenticated service, a credential proxy gives it a placeholder and swaps in the real value only at the network boundary. The blip is new in November 2026.

## Level 1 — What it is (~10 min)

Keep the configuration contract in the repository, and the secrets out of the agent's reach.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/varlock) (~1 min) — note the credential proxy, the same idea as in the external sandboxes from [[Agent sandboxing]].
- [ ] **~5 min** · Skim: [varlock](https://github.com/dmno-dev/varlock) (README, ~5 min) — the example `.env.schema`, and the section on AI-safe configuration.

## Level 2 — Try it (~25 min)

- [ ] **~25 min** · **Do:** In a project with a `.env` file, run `npx varlock init` to create a schema, and move one secret into a vault or password manager you use. Run the app with `varlock run`. Then ask your coding agent what secrets the project needs, and check that it can see their names and types but not their values.

## Wrap-up

This plan covers it.

## Review the blip

- [ ] **~5 min** · Re-read [Varlock](https://www.thoughtworks.com/radar/tools/varlock) now that you know the topic.
