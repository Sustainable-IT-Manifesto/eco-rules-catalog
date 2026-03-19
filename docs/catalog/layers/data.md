# Data rules

**Total rules:** 15

- [Back to Human Catalog](../index.md)
- [Back to Rule Browser](../../rule-browser.md)

## Rules

### [ECO-DAT-DATA-001 — Duplicate stored data](../ECO-DAT-DATA-001.md)

Redundant data increases storage footprint and cost.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-002 — Missing retention policy](../ECO-DAT-DATA-002.md)

No TTL/lifecycle policy causes unbounded data growth.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-003 — Large unused indexes](../ECO-DAT-DATA-003.md)

Unused indexes waste storage and slow writes.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-004 — Logs stored indefinitely](../ECO-DAT-DATA-004.md)

Indefinite log retention increases storage and cost without clear value.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-005 — Full table scans without index](../ECO-DAT-DATA-005.md)

Full scans increase CPU, IO, and latency for queries.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-006 — Excessive replication factor](../ECO-DAT-DATA-006.md)

High replication increases storage and write amplification.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-007 — No partitioning for large tables](../ECO-DAT-DATA-007.md)

Large tables without partitioning lead to expensive queries and maintenance.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-008 — Storing ephemeral data permanently](../ECO-DAT-DATA-008.md)

Ephemeral data kept forever becomes waste by default.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-009 — No archival tier strategy](../ECO-DAT-DATA-009.md)

Lack of archival tiering keeps costs and energy higher than necessary.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-010 — Overly aggressive replication across regions](../ECO-DAT-DATA-010.md)

Cross-region replication can add cost and complexity beyond needs.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-011 — Lack of compression in object storage](../ECO-DAT-DATA-011.md)

Uncompressed objects waste storage and bandwidth.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-012 — Unbounded analytics queries](../ECO-DAT-DATA-012.md)

Unbounded queries cause runaway compute and unpredictable cost.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-013 — No data lifecycle governance](../ECO-DAT-DATA-013.md)

Lack of lifecycle governance leads to perpetual growth and shadow datasets.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-014 — Stale feature flags accumulating](../ECO-DAT-DATA-014.md)

Feature flags left indefinitely add complexity and runtime overhead.

- Category: **DAT**
- Family: **DATA**

### [ECO-DAT-DATA-015 — Shadow data stores outside governance](../ECO-DAT-DATA-015.md)

Unofficial copies create duplicated storage and compliance risk.

- Category: **DAT**
- Family: **DATA**
