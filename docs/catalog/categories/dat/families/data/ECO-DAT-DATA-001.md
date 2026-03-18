# ECO-DAT-DATA-001 — Duplicate stored data

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** warning
- **Tags:** storage, duplication
- **Legacy ID:** ECO-DATA-001

## Summary

Redundant data increases storage footprint and cost.

## Rationale

Duplication silently accumulates and multiplies downstream processing.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often found in pipelines and analytics copies.",
  "type": "storage"
}
```

## Detection

```json
{
  "languages": [
    "database",
    "infra"
  ],
  "method": "query"
}
```

## Remediation

```json
{
  "guidance": "Deduplicate; normalize; define canonical sources.",
  "tradeoffs": "Migration effort."
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
