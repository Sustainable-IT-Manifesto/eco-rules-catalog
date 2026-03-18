# ECO-ORG-PROC-001 — No performance budget defined

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** governance, budgets
- **Legacy ID:** ECO-PROC-001

## Summary

Without explicit budgets, performance and efficiency drift.

## Rationale

Budgets make efficiency intentional instead of accidental.

## Impact

```json
{
  "confidence": 0.9,
  "notes": "Systemic driver.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Define performance budgets per service and user journey.",
  "tradeoffs": "Requires measurement agreement."
}
```

## Ontology

```json
{
  "system_layers": [
    "process"
  ]
}
```
