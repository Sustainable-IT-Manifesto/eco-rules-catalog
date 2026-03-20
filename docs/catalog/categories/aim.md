# AI/ML rules

**Category code:** `AIM`

**Total rules:** 15

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-AIM-AI-001 — Oversized model selection](../ECO-AIM-AI-001.md)

Using larger models than needed increases inference cost and emissions.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-002 — No inference batching](../ECO-AIM-AI-002.md)

No batching increases per-request overhead and lowers throughput.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-003 — Re-embedding unchanged data](../ECO-AIM-AI-003.md)

Recomputing embeddings for unchanged inputs wastes compute.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-004 — No prompt caching](../ECO-AIM-AI-004.md)

Repeated prompts without caching waste tokens and compute.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-005 — Always-on inference endpoints](../ECO-AIM-AI-005.md)

Always-on endpoints waste baseline compute when idle.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-006 — Unbounded context window usage](../ECO-AIM-AI-006.md)

Excessive context increases token cost and latency.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-007 — No model quantization](../ECO-AIM-AI-007.md)

Failure to quantize when appropriate wastes inference compute.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-008 — Re-training without drift detection](../ECO-AIM-AI-008.md)

Training without drift checks wastes compute and introduces risk.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-009 — No evaluation before scaling model](../ECO-AIM-AI-009.md)

Scaling without evaluation wastes resources and can degrade outcomes.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-010 — Overly frequent fine-tuning cycles](../ECO-AIM-AI-010.md)

Frequent tuning without clear value wastes compute.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-011 — Storing all embeddings indefinitely](../ECO-AIM-AI-011.md)

Embedding stores without retention grow unbounded and expensive.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-012 — Large model in low-SLA workload](../ECO-AIM-AI-012.md)

Using high-cost models where latency/quality needs are modest wastes resources.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-013 — No GPU utilization monitoring](../ECO-AIM-AI-013.md)

Without GPU utilization metrics, accelerator waste stays invisible.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-014 — Inefficient feature preprocessing pipelines](../ECO-AIM-AI-014.md)

Preprocessing waste increases training and inference cost.

- Family: **AI**
- Layer: **ai**

### [ECO-AIM-AI-015 — No batching of vector search queries](../ECO-AIM-AI-015.md)

Unbatched vector queries increase overhead and reduce throughput.

- Family: **AI**
- Layer: **ai**
