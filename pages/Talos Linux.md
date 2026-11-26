- **Blip:** [Talos Linux](https://www.thoughtworks.com/radar/platforms/talos-linux)
- **Time:** ~45 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know the basics of Kubernetes.

---

## Current state (late 2026)

Talos Linux is a minimal Linux distribution made only to run Kubernetes: no SSH, no package manager, no shell. You configure nodes through an API with `talosctl`, and upgrades replace the whole OS image, so every node is a replaceable appliance, the old idea of [[Immutable servers]] applied to Kubernetes nodes. Most teams use managed Kubernetes and never see the node OS, so Talos is mainly for teams that run their own clusters, for example on bare metal for AI infrastructure. In 2026 Yardi acquired Sidero Labs, Talos's developer. Talos stays open source (MPL-2.0), but the Radar suggests watching the new owner.

## Level 1 — What it is (~10 min)

An immutable, API-managed operating system for Kubernetes nodes.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/talos-linux) (~2 min) — note who it's for (teams running their own nodes), and the alternatives it names, Bottlerocket and Flatcar.

## Level 2 — Try it (~35 min)

- [ ] **~35 min** · **Do:** Follow Talos's [Getting Started](https://docs.siderolabs.com/talos/v1.14/getting-started/getting-started.md) guide (Sidero docs, ~6 min) in one or two local VMs: install `talosctl`, generate a config, apply it, and bootstrap a one-node cluster. Then try to change something on the node the way you would on Ubuntu, and see how Talos makes you do it through the API instead.

## Wrap-up

This plan covers it, unless you run your own Kubernetes nodes.

## Review the blip

- [ ] **~5 min** · Re-read [Talos Linux](https://www.thoughtworks.com/radar/platforms/talos-linux) now that you know the topic.

## Related blips

- **[[AWS]]**: Bottlerocket, a similar approach, runs there.
- **[[Kubernetes]]**: the only thing Talos is made to run.
- **[[Immutable servers]]**: the idea Talos applies to Kubernetes nodes.
