# ECO-DAT-DATA-008 — Storing ephemeral data permanently

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 4
- **Severity:** warning
- **Tags:** retention
- **Legacy ID:** ECO-DATA-008

## Summary

Ephemeral data kept forever becomes waste by default.

## Rationale

Temporary data should expire; permanence requires justification.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often caused by missing TTLs.",
  "type": "storage"
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
  "guidance": "Add TTL/expiration and lifecycle policies.",
  "tradeoffs": "Risk if used unexpectedly later."
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
