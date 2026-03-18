# ECO-CMP-PY-012 — CPU-bound work in request thread

- **Category:** Computation (CMP)
- **Family:** Python (PY)
- **Layer:** Code
- **Tier:** 2
- **Severity:** warning
- **Tags:** python, throughput, latency
- **Legacy ID:** ECO-PY-012

## Summary

CPU-heavy work in request handlers reduces throughput and increases latency.

## Rationale

Requests should stay I/O bound when possible; CPU spikes reduce concurrency.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often visible as p95/p99 regression.",
  "type": "latency"
}
```

## Detection

```json
{
  "languages": [
    "python"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Offload CPU work to background jobs or optimize/compile hotspots.",
  "tradeoffs": "Added system complexity."
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
