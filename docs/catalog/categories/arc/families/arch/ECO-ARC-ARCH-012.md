# ECO-ARC-ARCH-012 — No graceful degradation strategy

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** reliability, degradation
- **Legacy ID:** ECO-ARCH-012

## Summary

Without degradation, overload becomes failure and waste.

## Rationale

Graceful degradation prevents overload collapse and retry storms.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "High in distributed systems.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "org",
    "infra"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Define shedding, fallbacks, and priority paths.",
  "tradeoffs": "Product decisions required."
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
