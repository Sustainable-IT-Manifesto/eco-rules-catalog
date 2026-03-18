# ECO-DAT-DATA-009 — No archival tier strategy

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** note
- **Tags:** archival, tiering
- **Legacy ID:** ECO-DATA-009

## Summary

Lack of archival tiering keeps costs and energy higher than necessary.

## Rationale

Archival tiers align cost with access patterns.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often easy win.",
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
  "guidance": "Adopt tiering and retrieval policies.",
  "tradeoffs": "Retrieval latency/cost."
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
