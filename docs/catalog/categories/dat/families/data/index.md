# Data (DATA)

- [Back to Data (DAT)](../../index.md)

**Total rules:** 15

## Rules

### [ECO-DAT-DATA-001 — Duplicate stored data](../../../../ECO-DAT-DATA-001.md)

Redundant data increases storage footprint and cost.

- Layer: **data**

### [ECO-DAT-DATA-002 — Missing retention policy](../../../../ECO-DAT-DATA-002.md)

No TTL/lifecycle policy causes unbounded data growth.

- Layer: **data**

### [ECO-DAT-DATA-003 — Large unused indexes](../../../../ECO-DAT-DATA-003.md)

Unused indexes waste storage and slow writes.

- Layer: **data**

### [ECO-DAT-DATA-004 — Logs stored indefinitely](../../../../ECO-DAT-DATA-004.md)

Indefinite log retention increases storage and cost without clear value.

- Layer: **data**

### [ECO-DAT-DATA-005 — Full table scans without index](../../../../ECO-DAT-DATA-005.md)

Full scans increase CPU, IO, and latency for queries.

- Layer: **data**

### [ECO-DAT-DATA-006 — Excessive replication factor](../../../../ECO-DAT-DATA-006.md)

High replication increases storage and write amplification.

- Layer: **data**

### [ECO-DAT-DATA-007 — No partitioning for large tables](../../../../ECO-DAT-DATA-007.md)

Large tables without partitioning lead to expensive queries and maintenance.

- Layer: **data**

### [ECO-DAT-DATA-008 — Storing ephemeral data permanently](../../../../ECO-DAT-DATA-008.md)

Ephemeral data kept forever becomes waste by default.

- Layer: **data**

### [ECO-DAT-DATA-009 — No archival tier strategy](../../../../ECO-DAT-DATA-009.md)

Lack of archival tiering keeps costs and energy higher than necessary.

- Layer: **data**

### [ECO-DAT-DATA-010 — Overly aggressive replication across regions](../../../../ECO-DAT-DATA-010.md)

Cross-region replication can add cost and complexity beyond needs.

- Layer: **data**

### [ECO-DAT-DATA-011 — Lack of compression in object storage](../../../../ECO-DAT-DATA-011.md)

Uncompressed objects waste storage and bandwidth.

- Layer: **data**

### [ECO-DAT-DATA-012 — Unbounded analytics queries](../../../../ECO-DAT-DATA-012.md)

Unbounded queries cause runaway compute and unpredictable cost.

- Layer: **data**

### [ECO-DAT-DATA-013 — No data lifecycle governance](../../../../ECO-DAT-DATA-013.md)

Lack of lifecycle governance leads to perpetual growth and shadow datasets.

- Layer: **data**

### [ECO-DAT-DATA-014 — Stale feature flags accumulating](../../../../ECO-DAT-DATA-014.md)

Feature flags left indefinitely add complexity and runtime overhead.

- Layer: **data**

### [ECO-DAT-DATA-015 — Shadow data stores outside governance](../../../../ECO-DAT-DATA-015.md)

Unofficial copies create duplicated storage and compliance risk.

- Layer: **data**
