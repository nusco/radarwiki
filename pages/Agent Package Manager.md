- **Blip:** [Agent Package Manager](https://www.thoughtworks.com/radar/tools/agent-package-manager)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan builds on [[Agent plugin marketplace]], which covers sharing agent assets through Git repositories.

---

## Current state (late 2026)

Agent Package Manager (APM) is an open-source tool from Microsoft, released in 2026. It treats the files that shape a coding agent (skills, instructions, prompts, hooks, plugins, MCP servers) like code dependencies: a manifest declares them, a lock file pins their exact versions and hashes, and a policy file limits where they can come from. It also scans them for hidden Unicode characters that could hijack an agent. It's pre-1.0 and community-driven, and the Radar expects competitors to follow, hence *Trial*. Thoughtworks uses it to publish versioned skills from a central repository.

## Level 1 — What it is (~10 min)

A dependency manager for agent configuration, with the supply-chain controls of a normal package manager.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/agent-package-manager) (~1 min) — note the parallel with code dependencies: lock files, SBOMs, drift audits, policies.
- [ ] **~5 min** · Skim: [Agent Package Manager](https://github.com/microsoft/apm) (Microsoft, README, ~6 min) — read "Why APM" and "The three promises" (manifest, lock file, policy). Note its own caveats: the policy isn't a sandbox, and the scan looks for hidden characters, not for intent.

## Level 2 — Use it (~35 min)

Manage one skill with APM, and see what the lock file buys you.

- [ ] **~35 min** · **Do:** Install APM and create an `apm.yml` for a project that declares one skill, for example the one from the marketplace you built in [[Agent plugin marketplace]]. Run `apm install`, and look at the files it writes and at `apm.lock.yaml`. Then change the skill at its source, and check how APM tells you about the drift. Decide whether your team would need this, or whether a plugin marketplace alone is enough.

## Wrap-up

This plan covers it. The general supply-chain ideas behind it are covered in [[Software Bill of Materials]].

## Review the blip

- [ ] **~5 min** · Re-read [Agent Package Manager](https://www.thoughtworks.com/radar/tools/agent-package-manager) now that you know the topic.

## Related blips

- **[[Agent plugin marketplace]]**: one of the sources APM installs from.
- **[[Agent Plugins]]**: one of the kinds of asset APM manages.
- **[[Enterprise harness]]**: APM makes an enterprise harness reproducible and governed.
- **[[CycloneDX]]**: one of the SBOM formats APM exports.
- **[[Software Bill of Materials]]**: APM exports SBOMs for agent context, as for code.
