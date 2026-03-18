# ECO-ARC-ARCH-002 — Always-on low-traffic service

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** scale-to-zero, serverless
- **Legacy ID:** ECO-ARCH-002

## Summary

Services running 24/7 with low utilization create baseline waste.

## Rationale

Idle systems still consume energy and operational attention.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "High if many services are idle.",
  "type": "carbon"
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
  "guidance": "Evaluate scale-to-zero, serverless, or consolidation.",
  "tradeoffs": "Cold starts / architecture changes."
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
