# Data rules

**Code:** `DAT`

**Total rules:** 18

- [Back to Human Catalog](../index.md)

## Rules

### [ECO-DAT-CACHE-001 — Missing cache for repeated expensive lookup](../ECO-DAT-CACHE-001.md)

The same expensive query, API call, or computation is performed repeatedly when results could be safely cached.

- Category: **Data**
- Family: **Caching**
- Layer: **data**

### [ECO-DAT-CACHE-002 — Cache stampede risk](../ECO-DAT-CACHE-002.md)

Many workers may recompute the same expired value simultaneously, amplifying load during bursts.

- Category: **Data**
- Family: **Caching**
- Layer: **architecture**

### [ECO-DAT-DATA-001 — Duplicate stored data](../ECO-DAT-DATA-001.md)

Redundant data increases storage footprint and cost.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-002 — Missing retention policy](../ECO-DAT-DATA-002.md)

No TTL/lifecycle policy causes unbounded data growth.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-003 — Large unused indexes](../ECO-DAT-DATA-003.md)

Unused indexes waste storage and slow writes.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-004 — Logs stored indefinitely](../ECO-DAT-DATA-004.md)

Indefinite log retention increases storage and cost without clear value.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-005 — Full table scans without index](../ECO-DAT-DATA-005.md)

Full scans increase CPU, IO, and latency for queries.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-006 — Excessive replication factor](../ECO-DAT-DATA-006.md)

High replication increases storage and write amplification.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-007 — No partitioning for large tables](../ECO-DAT-DATA-007.md)

Large tables without partitioning lead to expensive queries and maintenance.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-008 — Storing ephemeral data permanently](../ECO-DAT-DATA-008.md)

Ephemeral data kept forever becomes waste by default.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-009 — No archival tier strategy](../ECO-DAT-DATA-009.md)

Lack of archival tiering keeps costs and energy higher than necessary.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-010 — Overly aggressive replication across regions](../ECO-DAT-DATA-010.md)

Cross-region replication can add cost and complexity beyond needs.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-011 — Lack of compression in object storage](../ECO-DAT-DATA-011.md)

Uncompressed objects waste storage and bandwidth.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-012 — Unbounded analytics queries](../ECO-DAT-DATA-012.md)

Unbounded queries cause runaway compute and unpredictable cost.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-013 — No data lifecycle governance](../ECO-DAT-DATA-013.md)

Lack of lifecycle governance leads to perpetual growth and shadow datasets.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-014 — Stale feature flags accumulating](../ECO-DAT-DATA-014.md)

Feature flags left indefinitely add complexity and runtime overhead.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-DATA-015 — Shadow data stores outside governance](../ECO-DAT-DATA-015.md)

Unofficial copies create duplicated storage and compliance risk.

- Category: **Data**
- Family: **Data**
- Layer: **data**

### [ECO-DAT-SER-001 — Repeated serialization/deserialization chain](../ECO-DAT-SER-001.md)

Data is repeatedly converted between formats within the same request or processing path.

- Category: **Data**
- Family: **Serialization**
- Layer: **data**
