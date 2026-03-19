# Architecture rules

**Total rules:** 26

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-ARC-ARCH-001 — Over-provisioned compute](../ECO-ARC-ARCH-001.md)

Sustained low utilization suggests oversized instances or replicas.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-002 — Always-on low-traffic service](../ECO-ARC-ARCH-002.md)

Services running 24/7 with low utilization create baseline waste.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-003 — Long synchronous dependency chain](../ECO-ARC-ARCH-003.md)

Synchronous call chains amplify latency and failure propagation.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-004 — No autoscaling policy](../ECO-ARC-ARCH-004.md)

Without scaling policies, systems drift into waste or fragility.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-005 — No resource limits in containers](../ECO-ARC-ARCH-005.md)

Missing CPU/memory limits causes noisy-neighbor waste and instability.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-006 — Unbounded message queues](../ECO-ARC-ARCH-006.md)

Queues without bounds hide backpressure and create runaway cost.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-007 — Batch jobs run too frequently](../ECO-ARC-ARCH-007.md)

Over-scheduling batch jobs wastes compute and increases cost.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-008 — Hot storage used for cold data](../ECO-ARC-ARCH-008.md)

Keeping cold data in hot tiers wastes storage spend and energy.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-009 — Duplicate services performing the same work](../ECO-ARC-ARCH-009.md)

Duplicate services increase operational load and waste compute.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-010 — No observability on utilization](../ECO-ARC-ARCH-010.md)

Without utilization metrics, waste is invisible and persistent.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-011 — Excessive replica counts](../ECO-ARC-ARCH-011.md)

Too many replicas increase baseline waste.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-012 — No graceful degradation strategy](../ECO-ARC-ARCH-012.md)

Without degradation, overload becomes failure and waste.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-013 — No caching layer for high-read workloads](../ECO-ARC-ARCH-013.md)

High-read systems without caching waste CPU and DB capacity.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-014 — Stateful services blocking scaling](../ECO-ARC-ARCH-014.md)

Stateful designs make scaling expensive and fragile.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-015 — Tight coupling across bounded contexts](../ECO-ARC-ARCH-015.md)

Coupling increases coordination cost and failure propagation.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-016 — Multi-tenant workloads without isolation](../ECO-ARC-ARCH-016.md)

Lack of isolation causes noisy-neighbor waste and instability.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-017 — Inefficient container image size](../ECO-ARC-ARCH-017.md)

Large images increase pull time and wasted storage/transfer.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-018 — No cold-start optimization](../ECO-ARC-ARCH-018.md)

Cold starts inflate latency and may force overprovisioning.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-019 — Overly aggressive autoscaling thresholds](../ECO-ARC-ARCH-019.md)

Aggressive scaling can cause thrash and wasted churn.

- Category: **ARC**
- Family: **ARCH**

### [ECO-ARC-ARCH-020 — Underutilized GPU/accelerator resources](../ECO-ARC-ARCH-020.md)

Accelerators running idle waste significant power and cost.

- Category: **ARC**
- Family: **ARCH**

### [ECO-CMP-JAVA-003 — Thread pool misconfiguration](../ECO-CMP-JAVA-003.md)

Incorrect thread pool sizing can waste CPU or cause latency collapse.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-006 — Missing connection pooling](../ECO-CMP-JAVA-006.md)

No pooling increases connection churn and DB overhead.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-009 — Large heap allocation spikes](../ECO-CMP-JAVA-009.md)

Heap spikes increase GC pauses and tail latency.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-PY-016 — No connection pooling](../ECO-CMP-PY-016.md)

Lack of pooling increases connection churn, latency, and DB load.

- Category: **CMP**
- Family: **PY**

### [ECO-INF-DOCKER-002 — Oversized base image](../ECO-INF-DOCKER-002.md)

Heavy base images increase transfer, storage, and patching footprint without improving runtime value.

- Category: **Infrastructure**
- Family: **Docker**

### [ECO-INF-K8S-004 — Heavy or redundant sidecars](../ECO-INF-K8S-004.md)

Sidecars add useful capabilities, but they also add CPU, memory, storage, and network overhead.

- Category: **Infrastructure**
- Family: **Kubernetes**
