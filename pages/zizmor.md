- **Blip:** [zizmor](https://www.thoughtworks.com/radar/tools/zizmor)
- **Time:** ~50 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know GitHub Actions.

---

## Current state (late 2026)

GitHub Actions workflows are code with access to secrets, and misconfigured ones have become a favorite target. In March 2026 attackers used a risky `pull_request_target` workflow in the Trivy repository to steal a token, then moved the tags of its popular GitHub Action, so that every pipeline using those tags ran their code. zizmor is a free, open-source static analyzer for workflows (and Dependabot and pre-commit configs) that finds exactly these problems: template injection, broad permissions, mutable tags, risky triggers. The blip is new in November 2026. Its only real limit is scope: GitHub Actions only.

## Level 1 — Why it matters (~25 min)

See how a workflow misconfiguration became a supply-chain attack.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/zizmor) (~2 min) — note the value of a deterministic tool for this job, and that coding agents can run it on the pipelines they write.
- [ ] **~20 min** · Read: [What We Can Learn About GitHub Actions Security from the Trivy Breach](https://www.endorlabs.com/learn/github-actions-security-lessons-from-trivy) (Robert Haynes, Endor Labs, Mar 2026, ~10 min) — linked from the blip. Read "What happened" through "three checks", and skip the product table. Note its caveat: even pinning actions to commit hashes doesn't cover everything.

## Level 2 — Scan your workflows (~25 min)

- [ ] **~25 min** · **Do:** Install zizmor following its [quickstart](https://docs.zizmor.sh/quickstart/), and run it on the `.github/workflows` of a repository you work on. For each finding, decide whether it's a real risk. Fix one, for example by pinning an action to a commit hash or narrowing `permissions`, and run zizmor again. Then add it as a pre-commit hook.

## Wrap-up

This plan covers it. Running workflows locally before pushing is covered in [[Act]], and the wider approach in [[Zero trust security for CI/CD]].

## Review the blip

- [ ] **~5 min** · Re-read [zizmor](https://www.thoughtworks.com/radar/tools/zizmor) now that you know the topic.

## Related blips

- **[[Zero trust security for CI/CD]]**: the blip recommends evaluating zizmor alongside it.
- **[[GitHub Actions]]**: the only CI platform zizmor covers.
- **[[Wiz]]**: a commercial tool covering some of the same ground.
- **[[Snyk]]**: another commercial alternative.
- **[[Dependabot]]**: zizmor also checks its configuration.
- **[[Trivy]]**: the project whose compromised workflow the blip uses as its example.
- **[[GitHub]]**: the platform where these workflows run.
