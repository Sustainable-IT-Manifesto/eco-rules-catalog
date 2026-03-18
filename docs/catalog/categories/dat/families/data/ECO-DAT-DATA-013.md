# ECO-DAT-DATA-013 — No data lifecycle governance

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 4
- **Severity:** warning
- **Tags:** governance
- **Legacy ID:** ECO-DATA-013

## Summary

Lack of lifecycle governance leads to perpetual growth and shadow datasets.

## Rationale

Without governance, retention becomes accidental and expensive.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "Systemic.",
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
  "guidance": "Define lifecycle owners, policies, and audits.",
  "tradeoffs": "Org change work."
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
