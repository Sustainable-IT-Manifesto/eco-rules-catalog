# JavaScript (JS)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 15

## Rules

### [ECO-CMP-JS-001 — Synchronous filesystem calls in request path](../../../../ECO-CMP-JS-001.md)

Sync FS calls block the event loop and reduce concurrency.

- Layer: **code**

### [ECO-CMP-JS-002 — Polling instead of events](../../../../ECO-CMP-JS-002.md)

Polling increases unnecessary network traffic and compute.

- Layer: **network**

### [ECO-CMP-JS-003 — Large unoptimized bundles](../../../../ECO-CMP-JS-003.md)

Large bundles increase transfer size, parse time, and energy use.

- Layer: **code**

### [ECO-CMP-JS-004 — Memory leaks via event listeners](../../../../ECO-CMP-JS-004.md)

Unremoved listeners retain objects and increase memory over time.

- Layer: **code**

### [ECO-CMP-JS-005 — Blocking crypto in event loop](../../../../ECO-CMP-JS-005.md)

CPU-heavy crypto blocks the event loop and inflates latency.

- Layer: **code**

### [ECO-CMP-JS-006 — Over-fetching API responses](../../../../ECO-CMP-JS-006.md)

Returning unused fields increases payload size and wasted processing.

- Layer: **network**

### [ECO-CMP-JS-007 — Missing HTTP caching headers (client-side)](../../../../ECO-CMP-JS-007.md)

Missing cache headers causes repeated downloads and wasted bandwidth.

- Layer: **network**

### [ECO-CMP-JS-008 — Excessive DOM reflow](../../../../ECO-CMP-JS-008.md)

Layout thrashing increases CPU and drains battery.

- Layer: **code**

### [ECO-CMP-JS-009 — Unbounded promise chains](../../../../ECO-CMP-JS-009.md)

Long or recursive promise chains can leak work and increase memory usage.

- Layer: **code**

### [ECO-CMP-JS-010 — Missing request timeout](../../../../ECO-CMP-JS-010.md)

Requests without timeouts hang and create cascading latency.

- Layer: **network**

### [ECO-CMP-JS-011 — Inefficient array transformations (multi-pass)](../../../../ECO-CMP-JS-011.md)

Multiple passes over arrays increases CPU and GC overhead.

- Layer: **code**

### [ECO-CMP-JS-012 — Redundant API calls in component lifecycle](../../../../ECO-CMP-JS-012.md)

Repeated fetches on rerender waste network and CPU.

- Layer: **network**

### [ECO-CMP-JS-013 — Uncompressed static assets](../../../../ECO-CMP-JS-013.md)

Serving assets without compression increases bandwidth and energy use.

- Layer: **network**

### [ECO-CMP-JS-014 — Client-side heavy computation without workers](../../../../ECO-CMP-JS-014.md)

Heavy CPU work on main thread harms responsiveness and drains battery.

- Layer: **code**

### [ECO-CMP-JS-015 — Recreating large objects per render](../../../../ECO-CMP-JS-015.md)

Allocating large objects repeatedly increases GC churn and CPU.

- Layer: **code**
