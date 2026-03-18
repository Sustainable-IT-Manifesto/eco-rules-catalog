# ECO-ARC-ARCH-006 — Unbounded message queues

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** error
- **Tags:** queues, backpressure
- **Legacy ID:** ECO-ARCH-006

## Summary

Queues without bounds hide backpressure and create runaway cost.

## Rationale

Unbounded queues become time bombs: cost, latency, and failure cascades.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "High propagation under partial failures.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Add backpressure, caps, DLQs, and shedding strategies.",
  "tradeoffs": "Must define loss/priority behavior."
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
