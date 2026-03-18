# ECO-DAT-DATA-011 — Lack of compression in object storage

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 3
- **Severity:** warning
- **Tags:** compression, object-storage
- **Legacy ID:** ECO-DATA-011

## Summary

Uncompressed objects waste storage and bandwidth.

## Rationale

Compression reduces stored bytes and transfer cost.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Especially strong for text/structured data.",
  "type": "storage"
}
```

## Detection

```json
{
  "languages": [
    "infra"
  ],
  "method": "trace"
}
```

## Remediation

```json
{
  "guidance": "Compress at write; enforce content-encoding where appropriate.",
  "tradeoffs": "CPU overhead at read/write."
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
