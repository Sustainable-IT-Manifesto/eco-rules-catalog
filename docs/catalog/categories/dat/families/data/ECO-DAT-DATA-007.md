# ECO-DAT-DATA-007 — No partitioning for large tables

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** warning
- **Tags:** partitioning
- **Legacy ID:** ECO-DATA-007

## Summary

Large tables without partitioning lead to expensive queries and maintenance.

## Rationale

Partitioning reduces scan scope and improves manageability.

## Impact

```json
{
  "confidence": 0.65,
  "notes": "Strong when datasets grow.",
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
  "guidance": "Partition by time/key; enforce pruning; archive older partitions.",
  "tradeoffs": "Migration complexity."
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
