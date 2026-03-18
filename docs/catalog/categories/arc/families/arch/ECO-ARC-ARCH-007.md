# ECO-ARC-ARCH-007 — Batch jobs run too frequently

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** batch, scheduling
- **Legacy ID:** ECO-ARCH-007

## Summary

Over-scheduling batch jobs wastes compute and increases cost.

## Rationale

Many batch workloads run far more often than the business needs.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Good target for quick savings.",
  "type": "cost"
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
  "guidance": "Right-size schedules; trigger on events; add change-detection.",
  "tradeoffs": "More complex orchestration."
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
