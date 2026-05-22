# Flask (FLASK)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-FLASK-001 — Database query in request loop](../../../../ECO-CMP-FLASK-001.md)

A Flask route performs repeated database queries while iterating over records.

- Layer: **code**

### [ECO-CMP-FLASK-002 — Expensive work during app startup](../../../../ECO-CMP-FLASK-002.md)

Flask application startup performs network calls, migrations, model loading, or large filesystem scans.

- Layer: **code**

### [ECO-CMP-FLASK-003 — Uncached template fragment rendering](../../../../ECO-CMP-FLASK-003.md)

Frequently rendered Flask templates recompute stable fragments on every request.

- Layer: **code**

### [ECO-CMP-FLASK-004 — Session payload bloat](../../../../ECO-CMP-FLASK-004.md)

Flask session data stores large objects or repeated state in client-side cookies or backing stores.

- Layer: **code**

### [ECO-CMP-FLASK-005 — Repeated configuration lookup per request](../../../../ECO-CMP-FLASK-005.md)

Request handlers repeatedly load configuration, secrets, or environment-dependent metadata.

- Layer: **code**

### [ECO-CMP-FLASK-006 — Unbounded background task submission](../../../../ECO-CMP-FLASK-006.md)

Flask endpoints enqueue background work without idempotency, rate limits, or queue bounds.

- Layer: **code**

### [ECO-CMP-FLASK-007 — Debug logging in production request paths](../../../../ECO-CMP-FLASK-007.md)

Flask handlers emit verbose logs or full payloads for every request.

- Layer: **code**

### [ECO-CMP-FLASK-008 — Synchronous external calls in hot routes](../../../../ECO-CMP-FLASK-008.md)

Flask routes synchronously call external APIs for data that could be cached or pre-fetched.

- Layer: **code**

### [ECO-CMP-FLASK-009 — Large response serialization without pagination](../../../../ECO-CMP-FLASK-009.md)

Flask routes serialize large result sets into JSON without pagination or field selection.

- Layer: **code**

### [ECO-CMP-FLASK-010 — Per-request object allocation in middleware](../../../../ECO-CMP-FLASK-010.md)

Flask before/after request hooks allocate expensive objects or clients on every request.

- Layer: **code**
