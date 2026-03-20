# Infrastructure rules

**Category code:** `INF`

**Total rules:** 12

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-INF-COMPOSE-001 — Overprovisioned default Compose stack](../ECO-INF-COMPOSE-001.md)

Starting every service by default in local or default compose profiles wastes local compute and encourages unnecessary background activity.

- Family: **Docker Compose**
- Layer: **process**

### [ECO-INF-COMPOSE-002 — Unbounded restart loops for noncritical services](../ECO-INF-COMPOSE-002.md)

Restarting noncritical services aggressively can create needless churn and repeated work.

- Family: **Docker Compose**
- Layer: **process**

### [ECO-INF-DOCKER-001 — Missing multi-stage builds](../ECO-INF-DOCKER-001.md)

Single-stage Docker builds often ship build tooling and temporary artifacts into runtime images, increasing image size and transfer cost.

- Family: **Docker**
- Layer: **process**

### [ECO-INF-DOCKER-002 — Oversized base image](../ECO-INF-DOCKER-002.md)

Heavy base images increase transfer, storage, and patching footprint without improving runtime value.

- Family: **Docker**
- Layer: **architecture**

### [ECO-INF-DOCKER-003 — Missing or too-permissive .dockerignore](../ECO-INF-DOCKER-003.md)

Large build contexts increase build time, cache churn, and unnecessary transfer to the Docker daemon.

- Family: **Docker**
- Layer: **process**

### [ECO-INF-DOCKER-004 — Package manager caches left in image layers](../ECO-INF-DOCKER-004.md)

Leaving package indexes and caches behind increases image size with no runtime benefit.

- Family: **Docker**
- Layer: **process**

### [ECO-INF-DOCKER-005 — Build tooling shipped in runtime image](../ECO-INF-DOCKER-005.md)

Runtime images should not carry compilers, package managers, or build-only tooling that is not needed after build.

- Family: **Docker**
- Layer: **process**

### [ECO-INF-K8S-001 — Missing or mis-sized CPU and memory requests and limits](../ECO-INF-K8S-001.md)

Containers without realistic requests and limits create waste, contention, or throttling.

- Family: **Kubernetes**
- Layer: **process**

### [ECO-INF-K8S-002 — Missing HPA for horizontally scalable workloads](../ECO-INF-K8S-002.md)

Workloads that can scale horizontally but do not use autoscaling can waste cluster capacity or under-serve demand.

- Family: **Kubernetes**
- Layer: **process**

### [ECO-INF-K8S-003 — Overly aggressive health probes](../ECO-INF-K8S-003.md)

Very frequent probes create unnecessary traffic and container work, especially at scale.

- Family: **Kubernetes**
- Layer: **process**

### [ECO-INF-K8S-004 — Heavy or redundant sidecars](../ECO-INF-K8S-004.md)

Sidecars add useful capabilities, but they also add CPU, memory, storage, and network overhead.

- Family: **Kubernetes**
- Layer: **architecture**

### [ECO-INF-K8S-005 — Unpinned images using latest or floating tags](../ECO-INF-K8S-005.md)

Floating tags make deployments less predictable and can increase repeated pulls and churn.

- Family: **Kubernetes**
- Layer: **process**
