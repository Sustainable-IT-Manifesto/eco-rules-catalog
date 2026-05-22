# Ruby on Rails (RAILS)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-RAILS-001 — ActiveRecord N+1 query in controller or view](../../../../ECO-CMP-RAILS-001.md)

Rails code loads associated records lazily while rendering a collection.

- Layer: **code**

### [ECO-CMP-RAILS-002 — Callback performs heavy side effects](../../../../ECO-CMP-RAILS-002.md)

ActiveRecord callbacks perform network calls, file work, or expensive computation during save/update flows.

- Layer: **code**

### [ECO-CMP-RAILS-003 — View partial renders expensive helpers repeatedly](../../../../ECO-CMP-RAILS-003.md)

Rails views call expensive helpers or render partials repeatedly across large collections.

- Layer: **code**

### [ECO-CMP-RAILS-004 — Missing fragment cache for stable Rails content](../../../../ECO-CMP-RAILS-004.md)

Stable page sections are recomputed for every Rails request.

- Layer: **code**

### [ECO-CMP-RAILS-005 — Unbounded ActiveJob enqueue from request](../../../../ECO-CMP-RAILS-005.md)

Rails requests enqueue many jobs without bounds, deduplication, or idempotency.

- Layer: **code**

### [ECO-CMP-RAILS-006 — Inefficient count queries in hot paths](../../../../ECO-CMP-RAILS-006.md)

Rails code uses repeated count queries or collection counting patterns in request paths.

- Layer: **code**

### [ECO-CMP-RAILS-007 — Large serialized JSON responses](../../../../ECO-CMP-RAILS-007.md)

Rails endpoints serialize full ActiveRecord objects or large associations without field selection.

- Layer: **code**

### [ECO-CMP-RAILS-008 — Per-request service/client construction](../../../../ECO-CMP-RAILS-008.md)

Rails controllers or middleware construct expensive clients or configuration objects on every request.

- Layer: **code**

### [ECO-CMP-RAILS-009 — Verbose Rails logging in production](../../../../ECO-CMP-RAILS-009.md)

Rails logs SQL binds, payloads, or debug details at high volume in production.

- Layer: **code**

### [ECO-CMP-RAILS-010 — Asset pipeline ships unused JavaScript or CSS](../../../../ECO-CMP-RAILS-010.md)

Rails asset configuration ships unused bundles or duplicate dependencies to many pages.

- Layer: **code**
