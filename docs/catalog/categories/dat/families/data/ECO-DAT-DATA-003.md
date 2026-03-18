# ECO-DAT-DATA-003 — Large unused indexes

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** note
- **Tags:** indexes
- **Legacy ID:** ECO-DATA-003

## Summary

Unused indexes waste storage and slow writes.

## Rationale

Indexes are not free; they multiply storage and write cost.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Validate via usage stats.",
  "type": "storage"
}
```

## Detection

```json
{
  "languages": [
    "database"
  ],
  "method": "query"
}
```

## Remediation

```json
{
  "guidance": "Drop truly unused indexes; reassess queries.",
  "tradeoffs": "Risk if usage stats incomplete."
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
