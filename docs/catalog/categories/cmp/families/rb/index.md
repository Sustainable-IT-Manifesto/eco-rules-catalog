# Ruby (RB)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-RB-001 — String concatenation in loops](../../../../ECO-CMP-RB-001.md)

Repeated string concatenation in a loop can create avoidable object churn and CPU overhead.

- Layer: **code**

### [ECO-CMP-RB-002 — Eager materialization of large collections](../../../../ECO-CMP-RB-002.md)

Creating large arrays with map/select before consuming results increases memory pressure and GC work.

- Layer: **code**

### [ECO-CMP-RB-003 — Repeated regular expression compilation](../../../../ECO-CMP-RB-003.md)

Compiling equivalent regular expressions repeatedly in hot paths wastes CPU and allocations.

- Layer: **code**

### [ECO-CMP-RB-004 — N+1 ActiveRecord queries](../../../../ECO-CMP-RB-004.md)

Loading associated records one row at a time amplifies database traffic and latency.

- Layer: **code**

### [ECO-CMP-RB-005 — Inefficient ActiveRecord count usage](../../../../ECO-CMP-RB-005.md)

Using count, length, or size without understanding query/materialization behavior can create unnecessary database work or memory usage.

- Layer: **code**

### [ECO-CMP-RB-006 — Unbounded memoization or class-level caches](../../../../ECO-CMP-RB-006.md)

Memoization and class-level caches without bounds can leak memory over time.

- Layer: **code**

### [ECO-CMP-RB-007 — Blocking external calls inside request loops](../../../../ECO-CMP-RB-007.md)

Making sequential HTTP/API calls inside loops increases latency, ties up workers, and amplifies downstream load.

- Layer: **code**

### [ECO-CMP-RB-008 — Excessive object allocation in hot paths](../../../../ECO-CMP-RB-008.md)

Allocating short-lived hashes, arrays, strings, or objects in tight loops increases GC pressure.

- Layer: **code**

### [ECO-CMP-RB-009 — Loading full ActiveRecord objects for scalar data](../../../../ECO-CMP-RB-009.md)

Fetching complete model objects when only IDs or scalar fields are needed wastes memory, CPU, and database bandwidth.

- Layer: **code**

### [ECO-CMP-RB-010 — Per-record writes instead of batched operations](../../../../ECO-CMP-RB-010.md)

Saving or updating records one at a time can create excessive database round trips and transaction overhead.

- Layer: **code**
