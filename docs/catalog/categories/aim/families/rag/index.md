# Retrieval-Augmented Generation (RAG)

- [Back to AI/ML (AIM)](../../index.md)

**Total rules:** 2

## Rules

### [ECO-AIM-RAG-001 — Embedding regeneration without change detection](../../../../ECO-AIM-RAG-001.md)

Embeddings are regenerated for unchanged content, wasting compute and increasing pipeline latency.

- Layer: **ai**

### [ECO-AIM-RAG-002 — Excessive retrieval fan-out](../../../../ECO-AIM-RAG-002.md)

RAG retrieval queries too many sources, chunks, or indexes before ranking, increasing latency and inference context.

- Layer: **ai**
