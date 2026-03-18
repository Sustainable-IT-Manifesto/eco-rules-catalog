# ECO-CMP-JAVA-001 — Excessive object creation in hot path

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 1
- **Severity:** warning
- **Tags:** java, gc, allocations
- **Legacy ID:** ECO-JAVA-001

## Summary

High allocation rates increase GC pressure and CPU cost.

## Rationale

Allocation churn increases GC frequency and tail latency.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often shows up as p99 spikes.",
  "type": "cpu"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Reduce allocations; reuse objects; optimize parsing.",
  "tradeoffs": "May reduce readability."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```
