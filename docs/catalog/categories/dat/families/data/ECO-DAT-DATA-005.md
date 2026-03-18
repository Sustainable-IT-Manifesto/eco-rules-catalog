# ECO-DAT-DATA-005 — Full table scans without index

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** warning
- **Tags:** database, query-plans
- **Legacy ID:** ECO-DATA-005

## Summary

Full scans increase CPU, IO, and latency for queries.

## Rationale

Scans scale poorly and waste compute as data grows.

## Impact

```json
{
  "confidence": 0.75,
  "notes": "Often visible in query plans.",
  "type": "io"
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
  "guidance": "Add appropriate indexes; rewrite queries; partition large tables.",
  "tradeoffs": "Index/storage tradeoffs."
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
