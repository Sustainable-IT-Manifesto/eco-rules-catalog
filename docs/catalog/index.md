# Eco Rules Catalog (Human Readable)

**Generated at:** 2026-03-18T23:29:52Z
**Total rules:** 125

## Categories

- [AI/ML (AIM)](categories/aim/index.md) (15 rules)
- [Architecture (ARC)](categories/arc/index.md) (20 rules)
- [Computation (CMP)](categories/cmp/index.md) (45 rules)
- [Data (DAT)](categories/dat/index.md) (15 rules)
- [Networking (NET)](categories/net/index.md) (15 rules)
- [Organizational (ORG)](categories/org/index.md) (15 rules)

## Rule Index

| ID | Title | Category | Family | Layer | Severity |
|---|---|---|---|---|---|
| [ECO-AIM-AI-001](categories/aim/families/ai/ECO-AIM-AI-001.md) | Oversized model selection | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-002](categories/aim/families/ai/ECO-AIM-AI-002.md) | No inference batching | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-003](categories/aim/families/ai/ECO-AIM-AI-003.md) | Re-embedding unchanged data | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-004](categories/aim/families/ai/ECO-AIM-AI-004.md) | No prompt caching | AI/ML | AI | Ai | note |
| [ECO-AIM-AI-005](categories/aim/families/ai/ECO-AIM-AI-005.md) | Always-on inference endpoints | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-006](categories/aim/families/ai/ECO-AIM-AI-006.md) | Unbounded context window usage | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-007](categories/aim/families/ai/ECO-AIM-AI-007.md) | No model quantization | AI/ML | AI | Ai | note |
| [ECO-AIM-AI-008](categories/aim/families/ai/ECO-AIM-AI-008.md) | Re-training without drift detection | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-009](categories/aim/families/ai/ECO-AIM-AI-009.md) | No evaluation before scaling model | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-010](categories/aim/families/ai/ECO-AIM-AI-010.md) | Overly frequent fine-tuning cycles | AI/ML | AI | Ai | note |
| [ECO-AIM-AI-011](categories/aim/families/ai/ECO-AIM-AI-011.md) | Storing all embeddings indefinitely | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-012](categories/aim/families/ai/ECO-AIM-AI-012.md) | Large model in low-SLA workload | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-013](categories/aim/families/ai/ECO-AIM-AI-013.md) | No GPU utilization monitoring | AI/ML | AI | Ai | warning |
| [ECO-AIM-AI-014](categories/aim/families/ai/ECO-AIM-AI-014.md) | Inefficient feature preprocessing pipelines | AI/ML | AI | Ai | note |
| [ECO-AIM-AI-015](categories/aim/families/ai/ECO-AIM-AI-015.md) | No batching of vector search queries | AI/ML | AI | Ai | note |
| [ECO-ARC-ARCH-001](categories/arc/families/arch/ECO-ARC-ARCH-001.md) | Over-provisioned compute | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-002](categories/arc/families/arch/ECO-ARC-ARCH-002.md) | Always-on low-traffic service | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-003](categories/arc/families/arch/ECO-ARC-ARCH-003.md) | Long synchronous dependency chain | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-004](categories/arc/families/arch/ECO-ARC-ARCH-004.md) | No autoscaling policy | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-005](categories/arc/families/arch/ECO-ARC-ARCH-005.md) | No resource limits in containers | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-006](categories/arc/families/arch/ECO-ARC-ARCH-006.md) | Unbounded message queues | Architecture | Architecture | Architecture | error |
| [ECO-ARC-ARCH-007](categories/arc/families/arch/ECO-ARC-ARCH-007.md) | Batch jobs run too frequently | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-008](categories/arc/families/arch/ECO-ARC-ARCH-008.md) | Hot storage used for cold data | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-009](categories/arc/families/arch/ECO-ARC-ARCH-009.md) | Duplicate services performing the same work | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-010](categories/arc/families/arch/ECO-ARC-ARCH-010.md) | No observability on utilization | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-011](categories/arc/families/arch/ECO-ARC-ARCH-011.md) | Excessive replica counts | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-012](categories/arc/families/arch/ECO-ARC-ARCH-012.md) | No graceful degradation strategy | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-013](categories/arc/families/arch/ECO-ARC-ARCH-013.md) | No caching layer for high-read workloads | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-014](categories/arc/families/arch/ECO-ARC-ARCH-014.md) | Stateful services blocking scaling | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-015](categories/arc/families/arch/ECO-ARC-ARCH-015.md) | Tight coupling across bounded contexts | Architecture | Architecture | Architecture | note |
| [ECO-ARC-ARCH-016](categories/arc/families/arch/ECO-ARC-ARCH-016.md) | Multi-tenant workloads without isolation | Architecture | Architecture | Architecture | warning |
| [ECO-ARC-ARCH-017](categories/arc/families/arch/ECO-ARC-ARCH-017.md) | Inefficient container image size | Architecture | Architecture | Architecture | note |
| [ECO-ARC-ARCH-018](categories/arc/families/arch/ECO-ARC-ARCH-018.md) | No cold-start optimization | Architecture | Architecture | Architecture | note |
| [ECO-ARC-ARCH-019](categories/arc/families/arch/ECO-ARC-ARCH-019.md) | Overly aggressive autoscaling thresholds | Architecture | Architecture | Architecture | note |
| [ECO-ARC-ARCH-020](categories/arc/families/arch/ECO-ARC-ARCH-020.md) | Underutilized GPU/accelerator resources | Architecture | Architecture | Architecture | warning |
| [ECO-CMP-JAVA-001](categories/cmp/families/java/ECO-CMP-JAVA-001.md) | Excessive object creation in hot path | Computation | Java | Code | warning |
| [ECO-CMP-JAVA-002](categories/cmp/families/java/ECO-CMP-JAVA-002.md) | Unbounded cache growth | Computation | Java | Code | error |
| [ECO-CMP-JAVA-003](categories/cmp/families/java/ECO-CMP-JAVA-003.md) | Thread pool misconfiguration | Computation | Java | Architecture | warning |
| [ECO-CMP-JAVA-004](categories/cmp/families/java/ECO-CMP-JAVA-004.md) | Reflection in hot path | Computation | Java | Code | note |
| [ECO-CMP-JAVA-005](categories/cmp/families/java/ECO-CMP-JAVA-005.md) | N+1 ORM query pattern | Computation | Java | Code | warning |
| [ECO-CMP-JAVA-006](categories/cmp/families/java/ECO-CMP-JAVA-006.md) | Missing connection pooling | Computation | Java | Architecture | error |
| [ECO-CMP-JAVA-007](categories/cmp/families/java/ECO-CMP-JAVA-007.md) | Blocking calls in reactive pipeline | Computation | Java | Code | error |
| [ECO-CMP-JAVA-008](categories/cmp/families/java/ECO-CMP-JAVA-008.md) | Excessive synchronization contention | Computation | Java | Code | warning |
| [ECO-CMP-JAVA-009](categories/cmp/families/java/ECO-CMP-JAVA-009.md) | Large heap allocation spikes | Computation | Java | Architecture | warning |
| [ECO-CMP-JAVA-010](categories/cmp/families/java/ECO-CMP-JAVA-010.md) | Debug logging in production hot path | Computation | Java | Code | note |
| [ECO-CMP-JS-001](categories/cmp/families/js/ECO-CMP-JS-001.md) | Synchronous filesystem calls in request path | Computation | JavaScript | Code | error |
| [ECO-CMP-JS-002](categories/cmp/families/js/ECO-CMP-JS-002.md) | Polling instead of events | Computation | JavaScript | Network | warning |
| [ECO-CMP-JS-003](categories/cmp/families/js/ECO-CMP-JS-003.md) | Large unoptimized bundles | Computation | JavaScript | Code | warning |
| [ECO-CMP-JS-004](categories/cmp/families/js/ECO-CMP-JS-004.md) | Memory leaks via event listeners | Computation | JavaScript | Code | warning |
| [ECO-CMP-JS-005](categories/cmp/families/js/ECO-CMP-JS-005.md) | Blocking crypto in event loop | Computation | JavaScript | Code | warning |
| [ECO-CMP-JS-006](categories/cmp/families/js/ECO-CMP-JS-006.md) | Over-fetching API responses | Computation | JavaScript | Network | note |
| [ECO-CMP-JS-007](categories/cmp/families/js/ECO-CMP-JS-007.md) | Missing HTTP caching headers (client-side) | Computation | JavaScript | Network | warning |
| [ECO-CMP-JS-008](categories/cmp/families/js/ECO-CMP-JS-008.md) | Excessive DOM reflow | Computation | JavaScript | Code | warning |
| [ECO-CMP-JS-009](categories/cmp/families/js/ECO-CMP-JS-009.md) | Unbounded promise chains | Computation | JavaScript | Code | note |
| [ECO-CMP-JS-010](categories/cmp/families/js/ECO-CMP-JS-010.md) | Missing request timeout | Computation | JavaScript | Network | error |
| [ECO-CMP-JS-011](categories/cmp/families/js/ECO-CMP-JS-011.md) | Inefficient array transformations (multi-pass) | Computation | JavaScript | Code | note |
| [ECO-CMP-JS-012](categories/cmp/families/js/ECO-CMP-JS-012.md) | Redundant API calls in component lifecycle | Computation | JavaScript | Network | warning |
| [ECO-CMP-JS-013](categories/cmp/families/js/ECO-CMP-JS-013.md) | Uncompressed static assets | Computation | JavaScript | Network | warning |
| [ECO-CMP-JS-014](categories/cmp/families/js/ECO-CMP-JS-014.md) | Client-side heavy computation without workers | Computation | JavaScript | Code | warning |
| [ECO-CMP-JS-015](categories/cmp/families/js/ECO-CMP-JS-015.md) | Recreating large objects per render | Computation | JavaScript | Code | note |
| [ECO-CMP-PY-001](categories/cmp/families/py/ECO-CMP-PY-001.md) | String concatenation in loops | Computation | Python | Code | warning |
| [ECO-CMP-PY-002](categories/cmp/families/py/ECO-CMP-PY-002.md) | Unbounded list growth | Computation | Python | Code | warning |
| [ECO-CMP-PY-003](categories/cmp/families/py/ECO-CMP-PY-003.md) | Repeated invariant computation inside loop | Computation | Python | Code | note |
| [ECO-CMP-PY-004](categories/cmp/families/py/ECO-CMP-PY-004.md) | Blocking I/O inside async context | Computation | Python | Code | error |
| [ECO-CMP-PY-005](categories/cmp/families/py/ECO-CMP-PY-005.md) | N+1 database query pattern | Computation | Python | Code | warning |
| [ECO-CMP-PY-006](categories/cmp/families/py/ECO-CMP-PY-006.md) | Missing network timeout | Computation | Python | Network | error |
| [ECO-CMP-PY-007](categories/cmp/families/py/ECO-CMP-PY-007.md) | Loading entire file into memory | Computation | Python | Code | warning |
| [ECO-CMP-PY-008](categories/cmp/families/py/ECO-CMP-PY-008.md) | Excessive logging in hot path | Computation | Python | Code | note |
| [ECO-CMP-PY-009](categories/cmp/families/py/ECO-CMP-PY-009.md) | Repeated regex compilation | Computation | Python | Code | note |
| [ECO-CMP-PY-010](categories/cmp/families/py/ECO-CMP-PY-010.md) | Inefficient data structure choice | Computation | Python | Code | note |
| [ECO-CMP-PY-011](categories/cmp/families/py/ECO-CMP-PY-011.md) | Repeated JSON serialization cycles | Computation | Python | Code | warning |
| [ECO-CMP-PY-012](categories/cmp/families/py/ECO-CMP-PY-012.md) | CPU-bound work in request thread | Computation | Python | Code | warning |
| [ECO-CMP-PY-013](categories/cmp/families/py/ECO-CMP-PY-013.md) | Inefficient pandas row iteration | Computation | Python | Code | warning |
| [ECO-CMP-PY-014](categories/cmp/families/py/ECO-CMP-PY-014.md) | Redundant environment variable lookups | Computation | Python | Code | note |
| [ECO-CMP-PY-015](categories/cmp/families/py/ECO-CMP-PY-015.md) | Recreating database connections per request | Computation | Python | Code | error |
| [ECO-CMP-PY-016](categories/cmp/families/py/ECO-CMP-PY-016.md) | No connection pooling | Computation | Python | Architecture | warning |
| [ECO-CMP-PY-017](categories/cmp/families/py/ECO-CMP-PY-017.md) | Large object retained in global scope | Computation | Python | Code | warning |
| [ECO-CMP-PY-018](categories/cmp/families/py/ECO-CMP-PY-018.md) | Recursive algorithm without safeguards | Computation | Python | Code | note |
| [ECO-CMP-PY-019](categories/cmp/families/py/ECO-CMP-PY-019.md) | Excessive thread spawning | Computation | Python | Code | warning |
| [ECO-CMP-PY-020](categories/cmp/families/py/ECO-CMP-PY-020.md) | Synchronous subprocess invocation in hot path | Computation | Python | Code | warning |
| [ECO-DAT-DATA-001](categories/dat/families/data/ECO-DAT-DATA-001.md) | Duplicate stored data | Data | Data | Data | warning |
| [ECO-DAT-DATA-002](categories/dat/families/data/ECO-DAT-DATA-002.md) | Missing retention policy | Data | Data | Data | warning |
| [ECO-DAT-DATA-003](categories/dat/families/data/ECO-DAT-DATA-003.md) | Large unused indexes | Data | Data | Data | note |
| [ECO-DAT-DATA-004](categories/dat/families/data/ECO-DAT-DATA-004.md) | Logs stored indefinitely | Data | Data | Data | warning |
| [ECO-DAT-DATA-005](categories/dat/families/data/ECO-DAT-DATA-005.md) | Full table scans without index | Data | Data | Data | warning |
| [ECO-DAT-DATA-006](categories/dat/families/data/ECO-DAT-DATA-006.md) | Excessive replication factor | Data | Data | Data | note |
| [ECO-DAT-DATA-007](categories/dat/families/data/ECO-DAT-DATA-007.md) | No partitioning for large tables | Data | Data | Data | warning |
| [ECO-DAT-DATA-008](categories/dat/families/data/ECO-DAT-DATA-008.md) | Storing ephemeral data permanently | Data | Data | Data | warning |
| [ECO-DAT-DATA-009](categories/dat/families/data/ECO-DAT-DATA-009.md) | No archival tier strategy | Data | Data | Data | note |
| [ECO-DAT-DATA-010](categories/dat/families/data/ECO-DAT-DATA-010.md) | Overly aggressive replication across regions | Data | Data | Data | note |
| [ECO-DAT-DATA-011](categories/dat/families/data/ECO-DAT-DATA-011.md) | Lack of compression in object storage | Data | Data | Data | warning |
| [ECO-DAT-DATA-012](categories/dat/families/data/ECO-DAT-DATA-012.md) | Unbounded analytics queries | Data | Data | Data | warning |
| [ECO-DAT-DATA-013](categories/dat/families/data/ECO-DAT-DATA-013.md) | No data lifecycle governance | Data | Data | Data | warning |
| [ECO-DAT-DATA-014](categories/dat/families/data/ECO-DAT-DATA-014.md) | Stale feature flags accumulating | Data | Data | Data | note |
| [ECO-DAT-DATA-015](categories/dat/families/data/ECO-DAT-DATA-015.md) | Shadow data stores outside governance | Data | Data | Data | warning |
| [ECO-NET-NET-001](categories/net/families/net/ECO-NET-NET-001.md) | Missing HTTP caching headers | Networking | Network | Network | warning |
| [ECO-NET-NET-002](categories/net/families/net/ECO-NET-NET-002.md) | No gzip/brotli compression | Networking | Network | Network | warning |
| [ECO-NET-NET-003](categories/net/families/net/ECO-NET-NET-003.md) | Chatty microservice communication | Networking | Network | Network | warning |
| [ECO-NET-NET-004](categories/net/families/net/ECO-NET-NET-004.md) | Redundant authentication calls | Networking | Network | Network | note |
| [ECO-NET-NET-005](categories/net/families/net/ECO-NET-NET-005.md) | Missing timeouts | Networking | Network | Network | error |
| [ECO-NET-NET-006](categories/net/families/net/ECO-NET-NET-006.md) | No connection reuse (keep-alive disabled) | Networking | Network | Network | warning |
| [ECO-NET-NET-007](categories/net/families/net/ECO-NET-NET-007.md) | Excessive retry storms | Networking | Network | Network | error |
| [ECO-NET-NET-008](categories/net/families/net/ECO-NET-NET-008.md) | Over-fetching API fields | Networking | Network | Network | note |
| [ECO-NET-NET-009](categories/net/families/net/ECO-NET-NET-009.md) | Under-fetching causing follow-up calls | Networking | Network | Network | note |
| [ECO-NET-NET-010](categories/net/families/net/ECO-NET-NET-010.md) | Large payloads without pagination | Networking | Network | Network | warning |
| [ECO-NET-NET-011](categories/net/families/net/ECO-NET-NET-011.md) | No CDN usage for static content | Networking | Network | Network | warning |
| [ECO-NET-NET-012](categories/net/families/net/ECO-NET-NET-012.md) | No HTTP/2 or HTTP/3 where applicable | Networking | Network | Network | note |
| [ECO-NET-NET-013](categories/net/families/net/ECO-NET-NET-013.md) | Excessive polling intervals | Networking | Network | Network | warning |
| [ECO-NET-NET-014](categories/net/families/net/ECO-NET-NET-014.md) | Synchronous cross-region calls | Networking | Network | Network | warning |
| [ECO-NET-NET-015](categories/net/families/net/ECO-NET-NET-015.md) | Missing circuit breaker patterns | Networking | Network | Network | warning |
| [ECO-ORG-PROC-001](categories/org/families/proc/ECO-ORG-PROC-001.md) | No performance budget defined | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-002](categories/org/families/proc/ECO-ORG-PROC-002.md) | No baseline measurement | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-003](categories/org/families/proc/ECO-ORG-PROC-003.md) | No cost observability | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-004](categories/org/families/proc/ECO-ORG-PROC-004.md) | No carbon awareness | Organizational | Process | Process | note |
| [ECO-ORG-PROC-005](categories/org/families/proc/ECO-ORG-PROC-005.md) | Feature shipped without load testing | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-006](categories/org/families/proc/ECO-ORG-PROC-006.md) | No lifecycle data policy | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-007](categories/org/families/proc/ECO-ORG-PROC-007.md) | No energy-aware CI/CD metrics | Organizational | Process | Process | note |
| [ECO-ORG-PROC-008](categories/org/families/proc/ECO-ORG-PROC-008.md) | No architectural review gate | Organizational | Process | Process | note |
| [ECO-ORG-PROC-009](categories/org/families/proc/ECO-ORG-PROC-009.md) | No dependency lifecycle management | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-010](categories/org/families/proc/ECO-ORG-PROC-010.md) | No hardware refresh sustainability policy | Organizational | Process | Process | note |
| [ECO-ORG-PROC-011](categories/org/families/proc/ECO-ORG-PROC-011.md) | No decommissioning workflow | Organizational | Process | Process | warning |
| [ECO-ORG-PROC-012](categories/org/families/proc/ECO-ORG-PROC-012.md) | No SLO-based scaling validation | Organizational | Process | Process | note |
| [ECO-ORG-PROC-013](categories/org/families/proc/ECO-ORG-PROC-013.md) | No capacity planning cadence | Organizational | Process | Process | note |
| [ECO-ORG-PROC-014](categories/org/families/proc/ECO-ORG-PROC-014.md) | No energy-efficient coding standards | Organizational | Process | Process | note |
| [ECO-ORG-PROC-015](categories/org/families/proc/ECO-ORG-PROC-015.md) | No sustainability accountability owner | Organizational | Process | Process | warning |
