# ECO-DAT-DATA-012 — Unbounded analytics queries

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** warning
- **Tags:** analytics, cost
- **Legacy ID:** ECO-DATA-012

## Summary

Unbounded queries cause runaway compute and unpredictable cost.

## Rationale

Analytics engines will happily burn money unless bounded.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Common in BI and ad-hoc SQL.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra",
    "database"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Add quotas, limits, and guardrails; require partition filters.",
  "tradeoffs": "May restrict ad-hoc exploration."
}
```

## Ontology

```json
{
  "system_layers": [
    "data"
  ]
}
```
