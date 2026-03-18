# ECO-ARC-ARCH-008 — Hot storage used for cold data

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** storage, tiering
- **Legacy ID:** ECO-ARCH-008

## Summary

Keeping cold data in hot tiers wastes storage spend and energy.

## Rationale

Tiering aligns cost and energy with access patterns.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often large savings.",
  "type": "storage"
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
  "guidance": "Introduce lifecycle policies and cold tiers.",
  "tradeoffs": "Retrieval latency and costs."
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
