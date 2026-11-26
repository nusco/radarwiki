- **Blip:** [Microsoft Copilot Retrieval API](https://www.thoughtworks.com/radar/platforms/microsoft-copilot-retrieval-api)
- **Time:** ~30 minutes
- **Radar edition:** November 2026
- **Quadrant:** Platforms
- **Ring:** Trial
- **Updated:** 2026-11-26
- **Status:** #undone

This plan assumes that you know what retrieval-augmented generation (RAG) is.

---

## Current state (late 2026)

Building RAG over company documents usually means copying them into a vector store, chunking and indexing them, keeping them in sync, and reproducing who can see what. For organizations whose knowledge lives in Microsoft 365, the Copilot Retrieval API skips all of that: it returns relevant text extracts from SharePoint, OneDrive and Copilot connectors, using the index Microsoft already maintains for Copilot, and only what the calling user is allowed to see. The blip is new in November 2026, after a positive experience at Thoughtworks. The API has tight limits on query size, results and request rates, and needs Copilot licensing.

## Level 1 — What it is (~10 min)

RAG over Microsoft 365 content, with indexing and permissions handled by Microsoft.

- [ ] **~10 min** · Read: [The Radar blip](https://www.thoughtworks.com/radar/platforms/microsoft-copilot-retrieval-api) (~1 min) — note what you no longer have to build: chunking, indexing, syncing and access control.

## Level 2 — Know its limits (~20 min)

- [ ] **~20 min** · Read: [Microsoft 365 Copilot Retrieval API Overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/overview) (Microsoft Learn, Aug 2026, ~7 min) — read "Capabilities", "Licensing" and "Known limitations" carefully (query length, at most 25 results, 200 requests per user per hour, no images). Then decide whether one use case you know could live within them.

## Wrap-up

This plan is enough unless you build on Microsoft 365. RAG itself is covered in [[Retrieval-augmented generation (RAG)]].

## Review the blip

- [ ] **~5 min** · Re-read [Microsoft Copilot Retrieval API](https://www.thoughtworks.com/radar/platforms/microsoft-copilot-retrieval-api) now that you know the topic.

## Related blips

- **[[Retrieval-augmented generation (RAG)]]**: the technique the API supports, without your own retrieval pipeline.
