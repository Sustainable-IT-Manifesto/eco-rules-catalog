# Docker Compose (COMPOSE)

- [Back to Infrastructure (INF)](../../index.md)

**Total rules:** 2

## Rules

### [ECO-INF-COMPOSE-001 — Overprovisioned default Compose stack](../../../../ECO-INF-COMPOSE-001.md)

Starting every service by default in local or default compose profiles wastes local compute and encourages unnecessary background activity.

- Layer: **process**

### [ECO-INF-COMPOSE-002 — Unbounded restart loops for noncritical services](../../../../ECO-INF-COMPOSE-002.md)

Restarting noncritical services aggressively can create needless churn and repeated work.

- Layer: **process**
