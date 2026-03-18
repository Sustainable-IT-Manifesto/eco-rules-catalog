# ECO-CMP-JAVA-003 — Thread pool misconfiguration

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Architecture
- **Tier:** 2
- **Severity:** warning
- **Tags:** java, threads, latency
- **Legacy ID:** ECO-JAVA-003

## Summary

Incorrect thread pool sizing can waste CPU or cause latency collapse.

## Rationale

Too many threads = contention; too few = underutilization and queues.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Tune to workload and downstream limits.",
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
  "guidance": "Tune pools; add backpressure; align with DB/HTTP limits.",
  "tradeoffs": "Requires measurement."
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
