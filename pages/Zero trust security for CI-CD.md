- **Blip:** [Zero trust security for CI/CD](https://www.thoughtworks.com/radar/techniques/zero-trust-security-for-ci-cd)
- **Time:** ~1.5 hours
- **Radar edition:** April 2023 and September 2023
- **Quadrant:** Techniques
- **Ring:** Trial
- **Updated:** 2026-11-27
- **Status:** #undone

This plan assumes that you know a CI/CD platform, such as GitHub Actions. The examples use GitHub Actions, but the ideas apply to any platform.

---

## Current state (late 2026)

The blip appeared in 2023, right after attackers stole every customer secret stored in CircleCI. It moved from Assess to Trial within the year, then dropped out of the Radar, but not because it got less relevant: pipelines have only become a bigger target. In March 2026 a risky workflow in the Trivy repository let attackers take over its popular GitHub Action (the story is in [[zizmor]]). The techniques in the blip are now the standard advice, and GitHub, GitLab and the major clouds all support short-lived, federated credentials for pipelines.

## Level 1 — Why pipelines are a target (~25 min)

Your pipeline holds your source code and the keys to production, so it's worth attacking.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/zero-trust-security-for-ci-cd) (~2 min) — read both versions. Note the list of techniques: you'll come back to it in the exercise.
- [ ] **~20 min** · Read: [CircleCI Jan 4, 2023 security incident report](https://circleci.com/blog/jan-4-2023-incident-report/) (Rob Zuber, CircleCI, Jan 2023, ~13 min) — the breach behind the blip, told by CircleCI's CTO. Read "What happened?" and "What we learned from this incident and what we will do next", and skim the rest. Notice how one stolen session on one laptop became every customer's secrets.

## Level 2 — Identity instead of secrets (~30 min)

Replace the long-lived cloud keys in your pipeline with short-lived tokens tied to the job.

- [ ] **~10 min** · Read: [Secure deployments with OpenID Connect & GitHub Actions now generally available](https://github.blog/security/supply-chain-security/secure-deployments-openid-connect-github-actions-generally-available/) (Usha Narayanabhatta, GitHub, Nov 2021, ~2 min) — the shortest explanation of the idea. Focus on the four steps in "How it works".
- [ ] **~20 min** · Read: [OpenID Connect](https://docs.github.com/en/actions/concepts/security/openid-connect) (GitHub Docs, ~6 min for the sections below) — read from "Overview of OpenID Connect" to "Understanding the OIDC token". Note how the cloud provider's trust policy checks the token's claims, such as `sub`: that's where least privilege lives. The OIDC technique has its own blip, [[OIDC for GitHub Actions]].

## Level 3 — Least privilege and ephemeral runners (~40 min)

Give every job only what it needs, and don't let one job leave anything behind for the next.

- [ ] **~15 min** · Skim: [Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) (GitHub Docs) — a long reference, so read just two parts: the advice on `GITHUB_TOKEN` permissions under "Use secrets for sensitive information", and "Hardening for self-hosted runners", including just-in-time runners. Note the caveat that auto-destroying runners is weaker than it sounds.
- [ ] **~25 min** · **Do:** Audit one pipeline you work on against the blip's list. Write down which long-lived secrets it holds, what permissions its token gets, whether its runners are reused between jobs, how old its runner software is, and whether anyone would notice unusual activity in its audit log. Pick the one change with the biggest payoff, such as moving a cloud deployment to OIDC or setting `permissions: contents: read` by default, and make it.

## If you have extra time

- [ ] **~15 min** · Skim: [OWASP Top 10 CI/CD Security Risks](https://owasp.org/www-project-top-10-ci-cd-security-risks/) (Daniel Krivelevich, Omer Gil and others, OWASP) — the list of risks, each with its own page. Use it as a checklist once your pipeline covers the basics.

## Wrap-up

This plan covers it. The wider idea of never trusting a network or a workload by default has its own blip, [[Zero trust architecture]]. Static checks for GitHub Actions workflows are covered in [[zizmor]], and running workflows locally in [[Act]].

## Review the blip

- [ ] **~5 min** · Re-read [Zero trust security for CI/CD](https://www.thoughtworks.com/radar/techniques/zero-trust-security-for-ci-cd) now that you know the topic.
