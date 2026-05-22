# Kubernetes (K8S)

- [Back to Infrastructure (INF)](../../index.md)

**Total rules:** 5

## Rules

### [ECO-INF-K8S-001 — Missing or mis-sized CPU and memory requests and limits](../../../../ECO-INF-K8S-001.md)

Containers without realistic requests and limits create waste, contention, or throttling.

- Layer: **process**

### [ECO-INF-K8S-002 — Missing HPA for horizontally scalable workloads](../../../../ECO-INF-K8S-002.md)

Workloads that can scale horizontally but do not use autoscaling can waste cluster capacity or under-serve demand.

- Layer: **process**

### [ECO-INF-K8S-003 — Overly aggressive health probes](../../../../ECO-INF-K8S-003.md)

Very frequent probes create unnecessary traffic and container work, especially at scale.

- Layer: **process**

### [ECO-INF-K8S-004 — Heavy or redundant sidecars](../../../../ECO-INF-K8S-004.md)

Sidecars add useful capabilities, but they also add CPU, memory, storage, and network overhead.

- Layer: **architecture**

### [ECO-INF-K8S-005 — Unpinned images using latest or floating tags](../../../../ECO-INF-K8S-005.md)

Floating tags make deployments less predictable and can increase repeated pulls and churn.

- Layer: **process**
