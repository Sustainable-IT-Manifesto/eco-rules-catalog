# Canonical vocab

## ResourceImpact

Use these exact values:

* `CPU`
* `Memory`
* `Network`
* `Storage`
* `Energy`
* `Latency`
* `Infrastructure Cost`
* `Developer Time`

## Mechanism

Use these exact values:

* `Redundant Computation`
* `Excessive Allocation`
* `Inefficient Data Structures`
* `Serialization Overhead`
* `Network Amplification`
* `Polling`
* `Cache Misuse`
* `Unbounded Growth`
* `Resource Contention`
* `Over-Provisioning`

## SystemLayer

Use these exact values:

* `Code`
* `Runtime`
* `Data`
* `Network`
* `Architecture`
* `AI/ML`
* `Organizational`

## DetectionMethod

Use these exact values:

* `Static Analysis`
* `Runtime Profiling`
* `Query Analysis`
* `Network Trace Analysis`
* `Log Pattern Detection`
* `CI Pipeline Inspection`

## RemediationPattern

Use these exact values:

* `Algorithmic Improvement`
* `Resource Reuse`
* `Caching`
* `Batching`
* `Event-Driven Design`
* `Data Reduction`
* `Infrastructure Right-Sizing`

---

## How to use the vocab in rules

In each rule’s JSON, you can either:

**Option A: keep current fields and add an `ontology` block** (recommended; non-breaking)

```json
{
  "id": "ECO-PY-001",
  "title": "Repeated String Concatenation in Loops",
  "family": "python",
  "layer": "code",
  "tier": 1,
  "severity": "medium",
  "ontology": {
    "resource_impacts": ["CPU", "Memory", "Energy"],
    "mechanisms": ["Excessive Allocation"],
    "system_layers": ["Code"],
    "detection_methods": ["Static Analysis"],
    "remediation_patterns": ["Resource Reuse"]
  }
}
```

