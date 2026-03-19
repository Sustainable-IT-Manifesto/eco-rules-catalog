# Code rules

**Total rules:** 34

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-CMP-JAVA-001 — Excessive object creation in hot path](../ECO-CMP-JAVA-001.md)

High allocation rates increase GC pressure and CPU cost.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-002 — Unbounded cache growth](../ECO-CMP-JAVA-002.md)

Caches without limits grow until they become the problem.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-004 — Reflection in hot path](../ECO-CMP-JAVA-004.md)

Reflection adds overhead and can inflate latency and CPU usage.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-005 — N+1 ORM query pattern](../ECO-CMP-JAVA-005.md)

ORM queries inside loops multiply DB calls.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-007 — Blocking calls in reactive pipeline](../ECO-CMP-JAVA-007.md)

Blocking in reactive code collapses concurrency and throughput.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-008 — Excessive synchronization contention](../ECO-CMP-JAVA-008.md)

Over-synchronization creates contention and wastes CPU.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JAVA-010 — Debug logging in production hot path](../ECO-CMP-JAVA-010.md)

Verbose logs in hot paths waste CPU and I/O.

- Category: **CMP**
- Family: **JAVA**

### [ECO-CMP-JS-001 — Synchronous filesystem calls in request path](../ECO-CMP-JS-001.md)

Sync FS calls block the event loop and reduce concurrency.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-003 — Large unoptimized bundles](../ECO-CMP-JS-003.md)

Large bundles increase transfer size, parse time, and energy use.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-004 — Memory leaks via event listeners](../ECO-CMP-JS-004.md)

Unremoved listeners retain objects and increase memory over time.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-005 — Blocking crypto in event loop](../ECO-CMP-JS-005.md)

CPU-heavy crypto blocks the event loop and inflates latency.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-008 — Excessive DOM reflow](../ECO-CMP-JS-008.md)

Layout thrashing increases CPU and drains battery.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-009 — Unbounded promise chains](../ECO-CMP-JS-009.md)

Long or recursive promise chains can leak work and increase memory usage.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-011 — Inefficient array transformations (multi-pass)](../ECO-CMP-JS-011.md)

Multiple passes over arrays increases CPU and GC overhead.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-014 — Client-side heavy computation without workers](../ECO-CMP-JS-014.md)

Heavy CPU work on main thread harms responsiveness and drains battery.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-JS-015 — Recreating large objects per render](../ECO-CMP-JS-015.md)

Allocating large objects repeatedly increases GC churn and CPU.

- Category: **CMP**
- Family: **JS**

### [ECO-CMP-PY-001 — String concatenation in loops](../ECO-CMP-PY-001.md)

Repeated string concatenation in a loop increases allocations and CPU.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-002 — Unbounded list growth](../ECO-CMP-PY-002.md)

Collections that grow without bounds increase memory pressure and GC churn.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-003 — Repeated invariant computation inside loop](../ECO-CMP-PY-003.md)

Recomputing values that do not change inside a loop wastes CPU cycles.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-004 — Blocking I/O inside async context](../ECO-CMP-PY-004.md)

Blocking calls inside async functions reduce concurrency and inflate latency.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-005 — N+1 database query pattern](../ECO-CMP-PY-005.md)

Queries executed inside iteration multiply round trips and load.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-007 — Loading entire file into memory](../ECO-CMP-PY-007.md)

Reading large files fully into memory increases peak RAM and risk of OOM.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-008 — Excessive logging in hot path](../ECO-CMP-PY-008.md)

Logging in tight loops or request hot paths adds CPU and I/O overhead.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-009 — Repeated regex compilation](../ECO-CMP-PY-009.md)

Compiling regex repeatedly wastes CPU; compile once and reuse.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-010 — Inefficient data structure choice](../ECO-CMP-PY-010.md)

Using lists for membership tests instead of sets/dicts increases CPU time.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-011 — Repeated JSON serialization cycles](../ECO-CMP-PY-011.md)

Serializing/deserializing repeatedly wastes CPU and increases latency.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-012 — CPU-bound work in request thread](../ECO-CMP-PY-012.md)

CPU-heavy work in request handlers reduces throughput and increases latency.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-013 — Inefficient pandas row iteration](../ECO-CMP-PY-013.md)

Row-wise pandas iteration is slow compared to vectorized operations.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-014 — Redundant environment variable lookups](../ECO-CMP-PY-014.md)

Repeated env lookups in hot code paths add overhead and noise.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-015 — Recreating database connections per request](../ECO-CMP-PY-015.md)

Creating DB connections per request increases latency and resource churn.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-017 — Large object retained in global scope](../ECO-CMP-PY-017.md)

Long-lived globals can cause persistent memory bloat.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-018 — Recursive algorithm without safeguards](../ECO-CMP-PY-018.md)

Recursion without depth safeguards risks overhead and runtime errors.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-019 — Excessive thread spawning](../ECO-CMP-PY-019.md)

Creating many threads increases overhead and contention.

- Category: **CMP**
- Family: **PY**

### [ECO-CMP-PY-020 — Synchronous subprocess invocation in hot path](../ECO-CMP-PY-020.md)

Blocking subprocess calls increase latency and consume resources.

- Category: **CMP**
- Family: **PY**
