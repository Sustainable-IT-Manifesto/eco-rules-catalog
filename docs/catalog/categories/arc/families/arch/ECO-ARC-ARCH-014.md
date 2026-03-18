# ECO-ARC-ARCH-014 — Stateful services blocking scaling

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** state, scaling
- **Legacy ID:** ECO-ARCH-014

## Summary

Stateful designs make scaling expensive and fragile.

## Rationale

State creates coupling that increases baseline and peak waste.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often structural.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Externalize state; use managed stores; reduce coupling.",
  "tradeoffs": "Migration cost."
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
