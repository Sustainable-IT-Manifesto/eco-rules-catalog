# ECO-DAT-DATA-010 — Overly aggressive replication across regions

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** note
- **Tags:** cross-region
- **Legacy ID:** ECO-DATA-010

## Summary

Cross-region replication can add cost and complexity beyond needs.

## Rationale

Replication should follow RPO/RTO requirements, not defaults.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Validate DR needs.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Right-size DR and replication strategies.",
  "tradeoffs": "Risk if requirements wrong."
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
