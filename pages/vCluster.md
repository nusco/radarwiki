- **Blip:** [vCluster](https://www.thoughtworks.com/radar/platforms/vcluster)
- **Time:** ~40 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know the basics of Kubernetes.

---

## Current state (late 2026)

Sharing a Kubernetes cluster between teams or customers usually means choosing between namespaces, which share cluster-wide APIs and custom resources, and separate clusters, which cost more to run. vCluster, from Loft Labs, sits in between: each tenant gets its own virtual control plane (API server, controllers, data store, RBAC and custom resources) running as a lightweight workload in a host cluster. Tenants use normal tools like `kubectl`, Helm and GitOps against their own virtual cluster. The blip is new in November 2026, in *Trial* after production use, especially for AI platforms where each customer needs its own GPU operators and schedulers.

## Level 1 — What it is (~10 min)

Virtual Kubernetes clusters inside a real one, each with its own control plane.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/vcluster) (~2 min) — note the isolation trade-off: shared nodes for trusted workloads, dedicated nodes for customers.

## Level 2 — Try it (~30 min)

- [ ] **~30 min** · **Do:** On a local cluster (kind or minikube), install the `vcluster` CLI from the [vCluster docs](https://www.vcluster.com/docs) and create a virtual cluster. Install a custom resource definition inside it, and check that the host cluster doesn't see it. Then look at what actually runs in the host cluster for your virtual one.

## Wrap-up

This plan covers it, unless you build multi-tenant platforms.

## Review the blip

- [ ] **~5 min** · Re-read [vCluster](https://www.thoughtworks.com/radar/platforms/vcluster) now that you know the topic.

## Related blips

- **[[GitOps]]**: tenants can manage their virtual clusters with GitOps controllers.
- **[[Helm]]**: works against each virtual cluster as usual.
- **[[Kubernetes]]**: vCluster virtualizes its control plane.
