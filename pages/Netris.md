- **Blip:** [Netris](https://www.thoughtworks.com/radar/platforms/netris)
- **Time:** ~15 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Assess
- **Updated:** 2026-11-26
- **Status:** #undone

This is a specialist platform for teams building their own AI data centers, so it gets a short plan.

---

## Current state (late 2026)

Public clouds give every customer its own virtual private network on shared hardware. Companies building their own GPU clouds need the same thing on physical switches. Netris is commercial software that automates data center networks and splits them between tenants: it turns switch configuration into cloud-style constructs (VPCs, virtual networks, access lists, load balancers), managed declaratively through a UI, an API, Kubernetes resources or Terraform. It also handles the specialized networking of AI clusters. Its controller runs outside the data path, so traffic keeps flowing if the controller goes down. The blip is new in November 2026.

## Level 1 — What it is (~5 min)

Cloud-style, multi-tenant networking for physical data centers and GPU clusters.

- [ ] **~5 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/netris) (~2 min) — note the advice to check compatibility with your switch operating system.

## Level 2 — Place it (~10 min)

- [ ] **~10 min** · **Do:** Write down how a public cloud gives your team an isolated network (a VPC, subnets, security groups), and which part of that Netris would recreate for a company running its own hardware. That's enough to recognize when it's relevant.

## Wrap-up

This plan is enough unless you build AI data centers. Netris's own site is marketing, so I didn't add it.

## Review the blip

- [ ] **~5 min** · Re-read [Netris](https://www.thoughtworks.com/radar/platforms/netris) now that you know the topic.

## Related blips

- **[[Kubernetes]]**: Netris can be driven through Kubernetes resources.
- **[[Terraform]]**: and through Terraform.
