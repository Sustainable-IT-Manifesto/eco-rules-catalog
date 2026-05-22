# Go (GO)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-GO-001 — Goroutine leak from missing cancellation](../../../../ECO-CMP-GO-001.md)

Starting goroutines without a clear cancellation, timeout, or lifecycle owner.

- Layer: **code**

### [ECO-CMP-GO-002 — Unbounded goroutine fan-out](../../../../ECO-CMP-GO-002.md)

Launching one goroutine per item without concurrency limits.

- Layer: **code**

### [ECO-CMP-GO-003 — Missing HTTP client timeout](../../../../ECO-CMP-GO-003.md)

Using http.Client or default clients without explicit timeouts.

- Layer: **code**

### [ECO-CMP-GO-004 — Repeated regexp compilation](../../../../ECO-CMP-GO-004.md)

Compiling regular expressions repeatedly instead of reusing compiled patterns.

- Layer: **code**

### [ECO-CMP-GO-005 — String concatenation in loops](../../../../ECO-CMP-GO-005.md)

Building large strings with repeated + or fmt.Sprintf in loops.

- Layer: **code**

### [ECO-CMP-GO-006 — Inefficient slice growth](../../../../ECO-CMP-GO-006.md)

Appending many items without preallocating capacity when size is known or bounded.

- Layer: **code**

### [ECO-CMP-GO-007 — Defers inside hot loops](../../../../ECO-CMP-GO-007.md)

Using defer inside high-iteration loops where immediate cleanup is possible.

- Layer: **code**

### [ECO-CMP-GO-008 — Per-item database or network calls](../../../../ECO-CMP-GO-008.md)

Calling database, RPC, or HTTP clients inside loops over collections.

- Layer: **code**

### [ECO-CMP-GO-009 — Excessive JSON marshal/unmarshal churn](../../../../ECO-CMP-GO-009.md)

Repeatedly marshaling and unmarshaling the same data or using JSON as an internal handoff format.

- Layer: **code**

### [ECO-CMP-GO-010 — Ticker or timer leak](../../../../ECO-CMP-GO-010.md)

Creating time.Ticker or timers without stopping them when lifecycle ends.

- Layer: **code**
