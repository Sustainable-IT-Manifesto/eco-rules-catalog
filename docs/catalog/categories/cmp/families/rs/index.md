# Rust (RS)

- [Back to Computation (CMP)](../../index.md)

**Total rules:** 10

## Rules

### [ECO-CMP-RS-001 — Unnecessary clone in hot paths](../../../../ECO-CMP-RS-001.md)

Calling clone() where borrowing, moving, or Copy semantics would avoid allocation and memory traffic.

- Layer: **code**

### [ECO-CMP-RS-002 — Collecting iterators before immediate iteration](../../../../ECO-CMP-RS-002.md)

Using collect() to materialize an intermediate Vec when the iterator could be consumed lazily.

- Layer: **code**

### [ECO-CMP-RS-003 — Blocking work inside async tasks](../../../../ECO-CMP-RS-003.md)

Running blocking file, network, CPU, or sleep operations inside async executors without isolation.

- Layer: **code**

### [ECO-CMP-RS-004 — Unbounded channel growth](../../../../ECO-CMP-RS-004.md)

Using unbounded channels where producer speed can exceed consumer capacity.

- Layer: **code**

### [ECO-CMP-RS-005 — Mutex held across await](../../../../ECO-CMP-RS-005.md)

Holding a Mutex, RwLock, or guard across an await point.

- Layer: **code**

### [ECO-CMP-RS-006 — Repeated regex compilation](../../../../ECO-CMP-RS-006.md)

Compiling regular expressions repeatedly instead of reusing compiled patterns.

- Layer: **code**

### [ECO-CMP-RS-007 — Large debug formatting in production paths](../../../../ECO-CMP-RS-007.md)

Using debug formatting or broad tracing of large structures in hot paths.

- Layer: **code**

### [ECO-CMP-RS-008 — Inefficient string construction](../../../../ECO-CMP-RS-008.md)

Repeated format! or push_str patterns that allocate avoidably while building large strings.

- Layer: **code**

### [ECO-CMP-RS-009 — Per-item database or network calls](../../../../ECO-CMP-RS-009.md)

Issuing database or HTTP calls inside collection loops instead of batching or joining.

- Layer: **code**

### [ECO-CMP-RS-010 — Oversized dependency feature sets](../../../../ECO-CMP-RS-010.md)

Enabling broad crate features or default features that pull unnecessary code, build work, or runtime behavior.

- Layer: **code**
