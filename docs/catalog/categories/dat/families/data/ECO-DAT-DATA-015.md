# ECO-DAT-DATA-015 — Shadow data stores outside governance

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 4
- **Severity:** warning
- **Tags:** shadow-it
- **Legacy ID:** ECO-DATA-015

## Summary

Unofficial copies create duplicated storage and compliance risk.

## Rationale

Shadow stores multiply cost and make lifecycle impossible to enforce.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often discovered during audits.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Inventory data stores; establish canonical sources and policies.",
  "tradeoffs": "Political and organizational effort."
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
