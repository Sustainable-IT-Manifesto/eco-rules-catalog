# Java (JAVA)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-JAVA-001 — Excessive object creation in hot path](../../../../ECO-CMP-JAVA-001.md)

High allocation rates increase GC pressure and CPU cost.

- Layer: **code**

### [ECO-CMP-JAVA-002 — Unbounded cache growth](../../../../ECO-CMP-JAVA-002.md)

Caches without limits grow until they become the problem.

- Layer: **code**

### [ECO-CMP-JAVA-003 — Thread pool misconfiguration](../../../../ECO-CMP-JAVA-003.md)

Incorrect thread pool sizing can waste CPU or cause latency collapse.

- Layer: **architecture**

### [ECO-CMP-JAVA-004 — Reflection in hot path](../../../../ECO-CMP-JAVA-004.md)

Reflection adds overhead and can inflate latency and CPU usage.

- Layer: **code**

### [ECO-CMP-JAVA-005 — N+1 ORM query pattern](../../../../ECO-CMP-JAVA-005.md)

ORM queries inside loops multiply DB calls.

- Layer: **code**

### [ECO-CMP-JAVA-006 — Missing connection pooling](../../../../ECO-CMP-JAVA-006.md)

No pooling increases connection churn and DB overhead.

- Layer: **architecture**

### [ECO-CMP-JAVA-007 — Blocking calls in reactive pipeline](../../../../ECO-CMP-JAVA-007.md)

Blocking in reactive code collapses concurrency and throughput.

- Layer: **code**

### [ECO-CMP-JAVA-008 — Excessive synchronization contention](../../../../ECO-CMP-JAVA-008.md)

Over-synchronization creates contention and wastes CPU.

- Layer: **code**

### [ECO-CMP-JAVA-009 — Large heap allocation spikes](../../../../ECO-CMP-JAVA-009.md)

Heap spikes increase GC pauses and tail latency.

- Layer: **architecture**

### [ECO-CMP-JAVA-010 — Debug logging in production hot path](../../../../ECO-CMP-JAVA-010.md)

Verbose logs in hot paths waste CPU and I/O.

- Layer: **code**
