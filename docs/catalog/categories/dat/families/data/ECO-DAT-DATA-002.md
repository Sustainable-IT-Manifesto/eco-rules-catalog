# ECO-DAT-DATA-002 — Missing retention policy

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 4
- **Severity:** warning
- **Tags:** retention, governance
- **Legacy ID:** ECO-DATA-002

## Summary

No TTL/lifecycle policy causes unbounded data growth.

## Rationale

Without retention, storage becomes the default memory of the organization.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "Systemic; large long-term cost driver.",
  "type": "storage"
}
```

## Detection

```json
{
  "languages": [
    "infra",
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Define retention tiers and lifecycle automation.",
  "tradeoffs": "Compliance alignment required."
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
