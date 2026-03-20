# Architecture rules

**Category code:** `ARC`

**Total rules:** 20

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-ARC-ARCH-001 — Over-provisioned compute](../ECO-ARC-ARCH-001.md)

Sustained low utilization suggests oversized instances or replicas.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-002 — Always-on low-traffic service](../ECO-ARC-ARCH-002.md)

Services running 24/7 with low utilization create baseline waste.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-003 — Long synchronous dependency chain](../ECO-ARC-ARCH-003.md)

Synchronous call chains amplify latency and failure propagation.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-004 — No autoscaling policy](../ECO-ARC-ARCH-004.md)

Without scaling policies, systems drift into waste or fragility.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-005 — No resource limits in containers](../ECO-ARC-ARCH-005.md)

Missing CPU/memory limits causes noisy-neighbor waste and instability.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-006 — Unbounded message queues](../ECO-ARC-ARCH-006.md)

Queues without bounds hide backpressure and create runaway cost.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-007 — Batch jobs run too frequently](../ECO-ARC-ARCH-007.md)

Over-scheduling batch jobs wastes compute and increases cost.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-008 — Hot storage used for cold data](../ECO-ARC-ARCH-008.md)

Keeping cold data in hot tiers wastes storage spend and energy.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-009 — Duplicate services performing the same work](../ECO-ARC-ARCH-009.md)

Duplicate services increase operational load and waste compute.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-010 — No observability on utilization](../ECO-ARC-ARCH-010.md)

Without utilization metrics, waste is invisible and persistent.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-011 — Excessive replica counts](../ECO-ARC-ARCH-011.md)

Too many replicas increase baseline waste.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-012 — No graceful degradation strategy](../ECO-ARC-ARCH-012.md)

Without degradation, overload becomes failure and waste.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-013 — No caching layer for high-read workloads](../ECO-ARC-ARCH-013.md)

High-read systems without caching waste CPU and DB capacity.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-014 — Stateful services blocking scaling](../ECO-ARC-ARCH-014.md)

Stateful designs make scaling expensive and fragile.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-015 — Tight coupling across bounded contexts](../ECO-ARC-ARCH-015.md)

Coupling increases coordination cost and failure propagation.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-016 — Multi-tenant workloads without isolation](../ECO-ARC-ARCH-016.md)

Lack of isolation causes noisy-neighbor waste and instability.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-017 — Inefficient container image size](../ECO-ARC-ARCH-017.md)

Large images increase pull time and wasted storage/transfer.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-018 — No cold-start optimization](../ECO-ARC-ARCH-018.md)

Cold starts inflate latency and may force overprovisioning.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-019 — Overly aggressive autoscaling thresholds](../ECO-ARC-ARCH-019.md)

Aggressive scaling can cause thrash and wasted churn.

- Family: **ARCH**
- Layer: **architecture**

### [ECO-ARC-ARCH-020 — Underutilized GPU/accelerator resources](../ECO-ARC-ARCH-020.md)

Accelerators running idle waste significant power and cost.

- Family: **ARCH**
- Layer: **architecture**
