# Process rules

**Total rules:** 25

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-INF-COMPOSE-001 — Overprovisioned default Compose stack](../ECO-INF-COMPOSE-001.md)

Starting every service by default in local or default compose profiles wastes local compute and encourages unnecessary background activity.

- Category: **Infrastructure**
- Family: **Docker Compose**

### [ECO-INF-COMPOSE-002 — Unbounded restart loops for noncritical services](../ECO-INF-COMPOSE-002.md)

Restarting noncritical services aggressively can create needless churn and repeated work.

- Category: **Infrastructure**
- Family: **Docker Compose**

### [ECO-INF-DOCKER-001 — Missing multi-stage builds](../ECO-INF-DOCKER-001.md)

Single-stage Docker builds often ship build tooling and temporary artifacts into runtime images, increasing image size and transfer cost.

- Category: **Infrastructure**
- Family: **Docker**

### [ECO-INF-DOCKER-003 — Missing or too-permissive .dockerignore](../ECO-INF-DOCKER-003.md)

Large build contexts increase build time, cache churn, and unnecessary transfer to the Docker daemon.

- Category: **Infrastructure**
- Family: **Docker**

### [ECO-INF-DOCKER-004 — Package manager caches left in image layers](../ECO-INF-DOCKER-004.md)

Leaving package indexes and caches behind increases image size with no runtime benefit.

- Category: **Infrastructure**
- Family: **Docker**

### [ECO-INF-DOCKER-005 — Build tooling shipped in runtime image](../ECO-INF-DOCKER-005.md)

Runtime images should not carry compilers, package managers, or build-only tooling that is not needed after build.

- Category: **Infrastructure**
- Family: **Docker**

### [ECO-INF-K8S-001 — Missing or mis-sized CPU and memory requests and limits](../ECO-INF-K8S-001.md)

Containers without realistic requests and limits create waste, contention, or throttling.

- Category: **Infrastructure**
- Family: **Kubernetes**

### [ECO-INF-K8S-002 — Missing HPA for horizontally scalable workloads](../ECO-INF-K8S-002.md)

Workloads that can scale horizontally but do not use autoscaling can waste cluster capacity or under-serve demand.

- Category: **Infrastructure**
- Family: **Kubernetes**

### [ECO-INF-K8S-003 — Overly aggressive health probes](../ECO-INF-K8S-003.md)

Very frequent probes create unnecessary traffic and container work, especially at scale.

- Category: **Infrastructure**
- Family: **Kubernetes**

### [ECO-INF-K8S-005 — Unpinned images using latest or floating tags](../ECO-INF-K8S-005.md)

Floating tags make deployments less predictable and can increase repeated pulls and churn.

- Category: **Infrastructure**
- Family: **Kubernetes**

### [ECO-ORG-PROC-001 — No performance budget defined](../ECO-ORG-PROC-001.md)

Without explicit budgets, performance and efficiency drift.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-002 — No baseline measurement](../ECO-ORG-PROC-002.md)

Without baseline data, improvements can’t be validated.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-003 — No cost observability](../ECO-ORG-PROC-003.md)

Without cost attribution, waste persists unmanaged.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-004 — No carbon awareness](../ECO-ORG-PROC-004.md)

Without carbon signals, teams can’t optimize responsibly.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-005 — Feature shipped without load testing](../ECO-ORG-PROC-005.md)

Skipping load tests creates risk and often forces wasteful overprovisioning.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-006 — No lifecycle data policy](../ECO-ORG-PROC-006.md)

Missing lifecycle policies cause unbounded storage and compliance risk.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-007 — No energy-aware CI/CD metrics](../ECO-ORG-PROC-007.md)

Build/test pipelines can waste large amounts of compute when unmeasured.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-008 — No architectural review gate](../ECO-ORG-PROC-008.md)

Without review gates, high-propagation waste slips in unnoticed.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-009 — No dependency lifecycle management](../ECO-ORG-PROC-009.md)

Unmanaged dependencies increase security, compute, and maintenance waste.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-010 — No hardware refresh sustainability policy](../ECO-ORG-PROC-010.md)

Hardware lifecycle without sustainability policy increases e-waste risk.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-011 — No decommissioning workflow](../ECO-ORG-PROC-011.md)

Without decommissioning, dead systems stay alive and waste resources.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-012 — No SLO-based scaling validation](../ECO-ORG-PROC-012.md)

Scaling without SLO validation often leads to overprovisioning or fragility.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-013 — No capacity planning cadence](../ECO-ORG-PROC-013.md)

Without planning, teams overbuy or get surprised and scramble.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-014 — No energy-efficient coding standards](../ECO-ORG-PROC-014.md)

Without standards, teams repeat avoidable inefficiencies.

- Category: **ORG**
- Family: **PROC**

### [ECO-ORG-PROC-015 — No sustainability accountability owner](../ECO-ORG-PROC-015.md)

Without ownership, sustainability work becomes optional and inconsistent.

- Category: **ORG**
- Family: **PROC**
