# ECO-ARC-ARCH-016 — Multi-tenant workloads without isolation

- **Category:** Architecture (ARC)
- **Family:** Architecture (ARCH)
- **Layer:** Architecture
- **Tier:** 3
- **Severity:** warning
- **Tags:** multi-tenant
- **Legacy ID:** ECO-ARCH-016

## Summary

Lack of isolation causes noisy-neighbor waste and instability.

## Rationale

Without isolation you overprovision to avoid incidents.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Structural waste driver.",
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
  "guidance": "Add isolation, quotas, and per-tenant limits.",
  "tradeoffs": "Complexity."
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
