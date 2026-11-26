- **Blip:** [LiteLLM](https://www.thoughtworks.com/radar/platforms/litellm)
- **Time:** ~55 minutes
- **Radar edition:** April 2024, October 2024, November 2025, April 2026 and November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

---

## Current state (late 2026)

LiteLLM started as a Python library that let you call any LLM provider through the OpenAI API format. Over five Radar editions it grew into a full AI gateway: a proxy that adds routing, failover, budgets, keys, logging and guardrails for a whole organization. In November 2026 the Radar moved it from Languages & Frameworks to Platforms, because teams now treat it as infrastructure. Its proxy core is being rewritten in Rust. It stays in *Trial* because of security: more than 25 vulnerabilities were reported in 2026 alone, so teams must patch promptly. Hiding providers behind one API also has a cost: provider-specific features get lost, sometimes silently.

## Level 1 — What it is (~15 min)

One gateway between your applications and all your model providers, with governance in one place.

- [ ] **~15 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/litellm) (~2 min per version) — read the five versions, oldest first, to see the library become a gateway. Note the warnings in April 2026 about provider-specific features and `drop_params`.

## Level 2 — Run the gateway (~40 min)

- [ ] **~40 min** · **Do:** Follow the [CLI Quick Start](https://docs.litellm.ai/docs/proxy/quick_start) (LiteLLM docs, ~5 min) to run the proxy with a `config.yaml` that lists two providers you have keys for. Call it with the OpenAI SDK, then switch models by changing only the model name. Then try one feature that only one provider has, and see what the gateway does with it. Check the current version for known vulnerabilities before you run it anywhere but your laptop.

## Wrap-up

This plan covers it. Governing MCP and agent-to-agent traffic too is covered in [[agentgateway]].

## Review the blip

- [ ] **~5 min** · Re-read [LiteLLM](https://www.thoughtworks.com/radar/platforms/litellm) now that you know the topic.

## Related blips

- **[[agentgateway]]**: the blip suggests combining the two, to govern MCP and agent-to-agent traffic too.
