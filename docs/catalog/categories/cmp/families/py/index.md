# Python (PY)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 20

## Rules

### [ECO-CMP-PY-001 — String concatenation in loops](../../../../ECO-CMP-PY-001.md)

Repeated string concatenation in a loop increases allocations and CPU.

- Layer: **code**

### [ECO-CMP-PY-002 — Unbounded list growth](../../../../ECO-CMP-PY-002.md)

Collections that grow without bounds increase memory pressure and GC churn.

- Layer: **code**

### [ECO-CMP-PY-003 — Repeated invariant computation inside loop](../../../../ECO-CMP-PY-003.md)

Recomputing values that do not change inside a loop wastes CPU cycles.

- Layer: **code**

### [ECO-CMP-PY-004 — Blocking I/O inside async context](../../../../ECO-CMP-PY-004.md)

Blocking calls inside async functions reduce concurrency and inflate latency.

- Layer: **code**

### [ECO-CMP-PY-005 — N+1 database query pattern](../../../../ECO-CMP-PY-005.md)

Queries executed inside iteration multiply round trips and load.

- Layer: **code**

### [ECO-CMP-PY-006 — Missing network timeout](../../../../ECO-CMP-PY-006.md)

Network calls without explicit timeouts can hang and cascade failures.

- Layer: **network**

### [ECO-CMP-PY-007 — Loading entire file into memory](../../../../ECO-CMP-PY-007.md)

Reading large files fully into memory increases peak RAM and risk of OOM.

- Layer: **code**

### [ECO-CMP-PY-008 — Excessive logging in hot path](../../../../ECO-CMP-PY-008.md)

Logging in tight loops or request hot paths adds CPU and I/O overhead.

- Layer: **code**

### [ECO-CMP-PY-009 — Repeated regex compilation](../../../../ECO-CMP-PY-009.md)

Compiling regex repeatedly wastes CPU; compile once and reuse.

- Layer: **code**

### [ECO-CMP-PY-010 — Inefficient data structure choice](../../../../ECO-CMP-PY-010.md)

Using lists for membership tests instead of sets/dicts increases CPU time.

- Layer: **code**

### [ECO-CMP-PY-011 — Repeated JSON serialization cycles](../../../../ECO-CMP-PY-011.md)

Serializing/deserializing repeatedly wastes CPU and increases latency.

- Layer: **code**

### [ECO-CMP-PY-012 — CPU-bound work in request thread](../../../../ECO-CMP-PY-012.md)

CPU-heavy work in request handlers reduces throughput and increases latency.

- Layer: **code**

### [ECO-CMP-PY-013 — Inefficient pandas row iteration](../../../../ECO-CMP-PY-013.md)

Row-wise pandas iteration is slow compared to vectorized operations.

- Layer: **code**

### [ECO-CMP-PY-014 — Redundant environment variable lookups](../../../../ECO-CMP-PY-014.md)

Repeated env lookups in hot code paths add overhead and noise.

- Layer: **code**

### [ECO-CMP-PY-015 — Recreating database connections per request](../../../../ECO-CMP-PY-015.md)

Creating DB connections per request increases latency and resource churn.

- Layer: **code**

### [ECO-CMP-PY-016 — No connection pooling](../../../../ECO-CMP-PY-016.md)

Lack of pooling increases connection churn, latency, and DB load.

- Layer: **architecture**

### [ECO-CMP-PY-017 — Large object retained in global scope](../../../../ECO-CMP-PY-017.md)

Long-lived globals can cause persistent memory bloat.

- Layer: **code**

### [ECO-CMP-PY-018 — Recursive algorithm without safeguards](../../../../ECO-CMP-PY-018.md)

Recursion without depth safeguards risks overhead and runtime errors.

- Layer: **code**

### [ECO-CMP-PY-019 — Excessive thread spawning](../../../../ECO-CMP-PY-019.md)

Creating many threads increases overhead and contention.

- Layer: **code**

### [ECO-CMP-PY-020 — Synchronous subprocess invocation in hot path](../../../../ECO-CMP-PY-020.md)

Blocking subprocess calls increase latency and consume resources.

- Layer: **code**
