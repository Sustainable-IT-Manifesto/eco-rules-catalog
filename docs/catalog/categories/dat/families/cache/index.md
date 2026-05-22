# Caching (CACHE)

- [Back to Data (DAT)](../../index.md)

**Total rules:** 2

## Rules

### [ECO-DAT-CACHE-001 — Missing cache for repeated expensive lookup](../../../../ECO-DAT-CACHE-001.md)

The same expensive query, API call, or computation is performed repeatedly when results could be safely cached.

- Layer: **data**

### [ECO-DAT-CACHE-002 — Cache stampede risk](../../../../ECO-DAT-CACHE-002.md)

Many workers may recompute the same expired value simultaneously, amplifying load during bursts.

- Layer: **architecture**
