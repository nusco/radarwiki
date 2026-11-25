- **Blip:** [Post-quantum cryptography](https://www.thoughtworks.com/radar/techniques/post-quantum-cryptography)
- **Time:** ~2 hours 45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Techniques
- **Ring:** Adopt
- **Updated:** 2026-11-25
- **Status:** #undone

---

## Current state (late 2026)

No quantum computer can break today's encryption yet, but the expected date keeps moving closer. In 2024 NIST published the first post-quantum standards: ML-KEM for key exchange, and ML-DSA and SLH-DSA for signatures. In 2025 and early 2026, new papers cut the estimated size of a machine that could break RSA and elliptic curves by orders of magnitude, and some cryptographers now treat 2030 as a realistic risk. Key exchange is already mostly migrated on the web: major browsers and CDNs use hybrid ML-KEM by default. Signatures and certificates are the hard, slow part, and that's where the work is now. The Radar first covered the topic as [Java post-quantum cryptography](https://www.thoughtworks.com/radar/languages-and-frameworks/java-post-quantum-cryptography) in 2025, and in November 2026 it puts the general technique straight into *Adopt*.

## Level 1 — Why it matters now (~1 hour)

Understand the threat, and why data that's encrypted today is already at risk.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/techniques/post-quantum-cryptography) (~2 min) — note why key exchange comes first: "harvest now, decrypt later".
- [ ] **~55 min** · Watch: [How Quantum Computers Break The Internet... Starting Now](https://www.youtube.com/watch?v=-UrdExQW0cs) (Veritasium, Apr 2023, ~24 min) — a well-researched explanation of why Shor's algorithm breaks RSA, and why attackers collect encrypted data today. You don't need to follow every step of the math. The timelines in it are from 2023, and Level 3 updates them.

## Level 2 — The migration (~1 hour)

Learn what's being migrated, in what order, and check where your own systems stand.

- [ ] **~30 min** · Read: [State of the post-quantum Internet in 2025](https://blog.cloudflare.com/pq-2025) (Bas Westerbaan, Cloudflare, Oct 2025, ~22 min) — the best overview of the migration, by an engineer who works on it. Read "The quantum threat", "Mitigating the quantum threat: two migrations" and "What you can do today", and skip the rest. You'll understand why key agreement is easy to migrate and signatures are not.
- [ ] **~30 min** · **Do:** Find out how post-quantum your own world is. In Chrome's DevTools, open the Security tab on five sites you use, including one of your company's, and note which use a key exchange with `MLKEM` in its name. Then check whether the language and TLS library of a project you work on support ML-KEM, and from which version (for Java, it's JDK 24). Write down one system that would still be exposed to "harvest now, decrypt later".

## Level 3 — How urgent is it? (~45 min)

Form your own view of the timeline, as the people closest to the problem see it in 2026.

- [ ] **~30 min** · Read: [A Cryptography Engineer's Perspective on Quantum Computing Timelines](https://words.filippo.io/crqc-timeline) (Filippo Valsorda, Apr 2026, ~10 min) — a well-known cryptography engineer, formerly the lead of Go's crypto libraries, explains why two March 2026 papers changed his mind, and what he thinks should ship now. It's opinionated, which makes it useful.
- [ ] **~15 min** · Skim: [Cloudflare targets 2029 for full post-quantum security](https://blog.cloudflare.com/post-quantum-roadmap) (Bas Westerbaan, Cloudflare, Apr 2026, ~13 min) — read "Why now" and "What we recommend". It shows how a large company turned the new estimates into a plan with dates, now focused on authentication.

## Wrap-up

This plan is enough for a generalist. For hands-on work in a specific language, see [[Java post-quantum cryptography]] for Java.

## Review the blip

- [ ] **~5 min** · Re-read [Post-quantum cryptography](https://www.thoughtworks.com/radar/techniques/post-quantum-cryptography) now that you know the topic.

## Related blips

- **[[Java post-quantum cryptography]]**: the blip's example of a mainstream platform with native post-quantum support, since JDK 24.
