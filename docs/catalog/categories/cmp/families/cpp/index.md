# C++ (CPP)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-CPP-001 — Avoidable copies of large objects](../../../../ECO-CMP-CPP-001.md)

Passing, returning, or assigning large containers and objects by value when moves or references would avoid copying.

- Layer: **code**

### [ECO-CMP-CPP-002 — Heap allocation in tight loops](../../../../ECO-CMP-CPP-002.md)

Allocating with new, make_unique, vector growth, or temporary containers repeatedly in hot loops.

- Layer: **code**

### [ECO-CMP-CPP-003 — Missing vector reserve before bulk insertion](../../../../ECO-CMP-CPP-003.md)

Growing std::vector or similar containers without reserving when size is known or bounded.

- Layer: **code**

### [ECO-CMP-CPP-004 — Synchronous blocking on futures or async results](../../../../ECO-CMP-CPP-004.md)

Blocking threads while waiting for asynchronous work in request or event-loop paths.

- Layer: **code**

### [ECO-CMP-CPP-005 — Expensive logging or stream formatting](../../../../ECO-CMP-CPP-005.md)

Using iostream formatting, stringstream construction, or full object logging in hot paths.

- Layer: **code**

### [ECO-CMP-CPP-006 — Inefficient string concatenation](../../../../ECO-CMP-CPP-006.md)

Repeated std::string concatenation without capacity planning for large outputs.

- Layer: **code**

### [ECO-CMP-CPP-007 — Shared pointer overuse](../../../../ECO-CMP-CPP-007.md)

Using std::shared_ptr where unique ownership, references, or values would be sufficient.

- Layer: **code**

### [ECO-CMP-CPP-008 — Lock contention in hot paths](../../../../ECO-CMP-CPP-008.md)

Holding mutexes around expensive work or high-frequency shared state updates.

- Layer: **code**

### [ECO-CMP-CPP-009 — Per-item remote calls](../../../../ECO-CMP-CPP-009.md)

Making database, RPC, or HTTP calls inside loops over collections.

- Layer: **code**

### [ECO-CMP-CPP-010 — Template or dependency bloat in build-critical paths](../../../../ECO-CMP-CPP-010.md)

Heavy template instantiation or broad dependencies causing excessive compile time and binary growth.

- Layer: **code**
