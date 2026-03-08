# Eco Rules Catalog — Rule Authoring Guide

This guide explains how to author new rules for the **Eco Rules Catalog**, including structure, taxonomy alignment, and validation requirements.

Rules represent **patterns of software inefficiency** that waste compute resources, increase cost, or increase environmental impact.

Each rule must fit into the catalog’s taxonomy and ontology so that it can be:

* analyzed automatically
* surfaced in tools
* mapped to sustainability impact
* understood consistently across ecosystems

---

# 1. Rule Identity Model

Each rule is uniquely identified using a **category-aware ID**.

```
ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ>
```

Example:

```
ECO-CMP-PY-010
```

Meaning:

| Component | Meaning                |
| --------- | ---------------------- |
| ECO       | Eco Rules Catalog      |
| CMP       | Category (Computation) |
| PY        | Family (Python)        |
| 010       | Sequence number        |

---

## Legacy IDs

Older rules used:

```
ECO-<FAMILY>-<SEQ>
```

Example:

```
ECO-PY-010
```

These are preserved as:

```
legacy_id
```

Example:

```json
"legacy_id": "ECO-PY-010"
```

---

# 2. Taxonomy Structure

Rules follow a strict hierarchy:

```
Category
   → Family
       → Rule
```

Example:

```
Computation
   → Python
       → ECO-CMP-PY-010
```

---

## Categories

Defined in:

```
ontology/categories.json
```

Examples:

| Category       | Code |
| -------------- | ---- |
| Computation    | CMP  |
| Data           | DAT  |
| Networking     | NET  |
| Infrastructure | INF  |
| AI/ML          | AIM  |
| Organizational | ORG  |

---

## Families

Defined in:

```
ontology/families.json
```

Examples:

| Family     | Code | Category       |
| ---------- | ---- | -------------- |
| Python     | PY   | Computation    |
| JavaScript | JS   | Computation    |
| SQL        | SQL  | Data           |
| HTTP       | HTTP | Networking     |
| Kubernetes | K8S  | Infrastructure |
| Process    | PROC | Organizational |

---

# 3. Rule Structure

Each rule must conform to the schema defined in:

```
schema/schema-rule.json
```

### Required Fields

```json
{
  "id": "ECO-CMP-PY-010",
  "canonical_id": "ECO-CMP-PY-010",

  "category": "Computation",
  "category_code": "CMP",

  "family": "Python",
  "family_code": "PY",

  "title": "Repeated string concatenation in loops",

  "summary": "Building strings inside loops creates excessive allocations and CPU overhead.",

  "layer": "Code",

  "tier": 1,

  "severity": "medium"
}
```

---

# 4. Rule Explanation Fields

Rules should include explanatory content for human readers.

## Summary

Short description of the inefficiency.

```
1–2 sentences
```

Example:

```
Building strings repeatedly inside loops creates unnecessary allocations and CPU overhead.
```

---

## Rationale

Explains **why the inefficiency matters**.

Example:

```
Repeated string concatenation causes repeated memory allocations and copying, increasing CPU usage and memory pressure.
```

---

## Impact

Explains the sustainability and cost implications.

Example:

```json
"impact": {
  "performance": "moderate",
  "cost": "low",
  "energy": "low"
}
```

---

# 5. Ontology Block

The ontology block links the rule to the sustainability model.

```json
"ontology": {
  "resource_impacts": ["CPU", "Memory"],
  "mechanisms": ["Excessive Allocation"],
  "system_layers": ["Code"],
  "detection_methods": ["Static Analysis"],
  "remediation_patterns": ["Algorithmic Improvement"]
}
```

---

## Ontology Dimensions

### Resource Impacts

What resources are wasted.

Examples:

```
CPU
Memory
Network
Storage
Energy
Latency
Infrastructure Cost
Developer Time
```

---

### Mechanisms

The **technical cause** of inefficiency.

Examples:

```
Redundant Computation
Excessive Allocation
Serialization Overhead
Network Amplification
Polling
Cache Misuse
Unbounded Growth
Resource Contention
Over-Provisioning
```

---

### System Layers

Where the inefficiency occurs.

Examples:

```
Code
Runtime
Data
Network
Architecture
AI/ML
Organizational
```

---

### Detection Methods

How the rule can be detected.

Examples:

```
Static Analysis
Runtime Profiling
Query Analysis
Network Trace Analysis
Log Pattern Detection
CI Pipeline Inspection
```

---

### Remediation Patterns

Typical solution approaches.

Examples:

```
Algorithmic Improvement
Caching
Batching
Resource Reuse
Event-Driven Design
Data Reduction
Infrastructure Right-Sizing
```

---

# 6. Severity

Severity reflects **impact and likelihood**, not just technical correctness.

| Severity | Meaning                  |
| -------- | ------------------------ |
| note     | informational            |
| info     | small inefficiency       |
| warning  | meaningful waste         |
| error    | significant inefficiency |
| critical | severe system impact     |

---

# 7. Tier

Tier reflects rule maturity and detection reliability.

| Tier | Meaning                        |
| ---- | ------------------------------ |
| 1    | strongly detectable            |
| 2    | pattern-based                  |
| 3    | contextual                     |
| 4    | architectural / organizational |

---

# 8. Validation Requirements

Every rule must pass:

```
make validate-schema
make validate-catalog
make validate-ontology
```

Or:

```
python tools/check_all.py --strict
```

Validation ensures:

* schema compliance
* taxonomy alignment
* ID correctness
* ontology vocabulary correctness

---

# 9. Authoring Workflow

### Step 1

Create a new rule entry in:

```
master.json
```

---

### Step 2

Run the normalization script:

```
python tools/update_rules.py --write
```

This automatically:

* fills category codes
* fills family codes
* generates canonical IDs
* adds legacy IDs

---

### Step 3

Validate the catalog.

```
python tools/check_all.py --strict
```

---

### Step 4

Create rule documentation.

```
rules/<rule-id>.md
```

Example:

```
rules/ECO-CMP-PY-010.md
```

---

# 10. Naming Guidelines

Titles should be:

* specific
* technical
* concise

Good:

```
Repeated string concatenation in loops
```

Bad:

```
Inefficient string handling
```

---

# 11. Writing Guidelines

Rules should:

* describe **patterns**, not incidents
* focus on **root causes**
* include **clear remediation guidance**

Avoid:

* vendor marketing
* opinionated style rules
* language-specific quirks without broader relevance

---

# 12. Example Rule

```json
{
  "id": "ECO-CMP-PY-010",
  "canonical_id": "ECO-CMP-PY-010",
  "legacy_id": "ECO-PY-010",

  "category": "Computation",
  "category_code": "CMP",

  "family": "Python",
  "family_code": "PY",

  "title": "Repeated string concatenation in loops",

  "summary": "Building strings inside loops causes repeated allocations.",

  "layer": "Code",
  "tier": 1,
  "severity": "medium",

  "ontology": {
    "resource_impacts": ["CPU", "Memory"],
    "mechanisms": ["Excessive Allocation"],
    "system_layers": ["Code"],
    "detection_methods": ["Static Analysis"],
    "remediation_patterns": ["Algorithmic Improvement"]
  }
}
```

---

# 13. Philosophy of the Catalog

The Eco Rules Catalog is not just a lint rule set.

It exists to make **software inefficiency visible and measurable**.

Every rule should help answer:

```
Where does software waste resources?
Why does it happen?
How can we fix it?
```

By structuring inefficiencies as rules, the catalog enables:

* automated analysis
* sustainability reporting
* engineering education
* system optimization

