# Eco Rule Template

This template should be used when authoring a new rule for the Eco Rules Catalog.

Rules describe **patterns of software inefficiency** that waste resources such as CPU, memory, network bandwidth, storage, infrastructure capacity, or developer time.

Follow the structure below when writing a new rule.

---

# Rule Metadata

| Field | Description |
|---|---|
| ID | ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ> |
| Category | High-level inefficiency domain |
| Family | Technology or pattern grouping |
| Layer | System layer where inefficiency occurs |
| Tier | Rule maturity / detection reliability |
| Severity | Expected impact |

---

# Title

Provide a short, precise description of the inefficiency pattern.

Good examples:

Repeated string concatenation in loops  
N+1 database query pattern  
Polling instead of event-driven updates

Avoid vague titles such as:

Poor performance  
Bad queries

---

# Summary

Provide a short description of the inefficiency.

Length guideline:

1–2 sentences

Example:

Repeated string concatenation inside loops causes unnecessary memory allocations and copying operations.

---

# Rationale

Explain **why the inefficiency matters**.

Describe:

- the mechanism
- the resource impact
- why the pattern appears

Example:

Repeated concatenation forces the runtime to allocate and copy memory repeatedly, increasing CPU usage and memory pressure.

---

# Impact

Describe the types of resources affected.

Examples:

- CPU overhead
- memory pressure
- network amplification
- infrastructure cost
- energy consumption

---

# Detection

Describe how the inefficiency can be detected.

Possible methods:

- static analysis
- runtime profiling
- query analysis
- CI inspection
- log analysis

---

# Remediation

Describe how the inefficiency can be fixed.

Prefer **design guidance** rather than strict prescriptions.

Example:

Use buffering or builder patterns to reduce repeated allocations.

---

# Example

Provide a minimal example that demonstrates the inefficiency.

Bad example:

```

result = ""
for item in items:
result += item

```

Better example:

```

parts = []
for item in items:
parts.append(item)

result = "".join(parts)

```

---

# Ontology Classification

Fill out the ontology fields so the rule can be analyzed across systems.

Resource impacts:

CPU  
Memory  
Network  
Storage  
Energy  
Latency  
Infrastructure Cost  
Developer Time

Mechanisms:

Redundant Computation  
Excessive Allocation  
Serialization Overhead  
Network Amplification  
Polling  
Cache Misuse  
Unbounded Growth  
Resource Contention  
Over-Provisioning

System layers:

Code  
Runtime  
Data  
Network  
Architecture  
AI/ML  
Organizational

Detection methods:

Static Analysis  
Runtime Profiling  
Query Analysis  
Network Trace Analysis  
Log Pattern Detection  
CI Pipeline Inspection

Remediation patterns:

Algorithmic Improvement  
Resource Reuse  
Caching  
Batching  
Event-Driven Design  
Data Reduction  
Infrastructure Right-Sizing

---

# Rule Quality Checklist

Before submitting a rule, verify:

- The inefficiency is **real and repeatable**
- The rule describes a **pattern**, not a single bug
- The rule provides **clear remediation guidance**
- The taxonomy classification is correct
- The ontology classification is complete
