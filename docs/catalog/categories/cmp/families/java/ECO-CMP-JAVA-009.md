# ECO-CMP-JAVA-009 — Large heap allocation spikes

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** warning
- **Tags:** java, gc, latency
- **Legacy ID:** ECO-JAVA-009

## Summary

Heap spikes increase GC pauses and tail latency.

## Rationale

Large allocations correlate strongly with p99 issues and waste.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Common in parsing/serialization bursts.",
  "type": "latency"
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
  "guidance": "Reduce allocations; stream processing; tune GC when needed.",
  "tradeoffs": "Measurement required."
}
```

## Ontology

```json
{
  "system_layers": [
    "architecture"
  ]
}
```
