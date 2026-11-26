- **Blip:** [Safe Chain](https://www.thoughtworks.com/radar/tools/safe-chain)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Tools
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

In September 2025 the "Shai-Hulud" worm spread through hundreds of npm packages, stealing credentials and publishing infected versions of the packages it reached. Attacks like it spread within hours, so one simple defense is to avoid installing anything published very recently. Most package managers now have a "minimum release age" setting. Safe Chain, a free tool from the security company Aikido, wraps npm, pnpm, Bun, pip, uv and others, blocks versions younger than 48 hours, and checks packages against Aikido's malware feed. The blip is new in November 2026. Safe Chain is AGPL or commercially licensed, and relies on one vendor's feed.

## Level 1 — Why it matters (~25 min)

Block brand-new and known-malicious packages before they reach your machine.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/tools/safe-chain) (~2 min) — note what Safe Chain adds to a package manager's own age setting, like one-off `npx` commands outside a project, and its limits.
- [ ] **~20 min** · Read: [Widespread Supply Chain Compromise Impacting npm Ecosystem](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) (CISA, Sep 2025, ~4 min) — the official alert on Shai-Hulud, the attack the blip cites. It shows how fast a compromised package spreads, and why a short delay gives scanners time to catch it.

## Level 2 — Protect your machine (~20 min)

- [ ] **~20 min** · **Do:** First set the minimum release age in your own package manager, if it has one (for example, in pnpm or uv). Then install Safe Chain following its [README](https://github.com/AikidoSec/safe-chain), and check it with `npm safe-chain-verify`. Try installing a package version published today, and see what happens. Decide whether the age setting alone would be enough for you.

## Wrap-up

This plan covers it. Package managers with good security defaults have their own plans: [[pnpm]] and [[uv]].

## Review the blip

- [ ] **~5 min** · Re-read [Safe Chain](https://www.thoughtworks.com/radar/tools/safe-chain) now that you know the topic.

## Related blips

- **[[pnpm]]**: one of the package managers Safe Chain wraps.
- **[[uv]]**: another.
- **[[Bun]]**: another.
- **[[Node.js]]**: the ecosystem whose package managers Safe Chain covers, with Python.
