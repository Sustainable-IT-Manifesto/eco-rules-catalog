# ECO-DAT-DATA-004 — Logs stored indefinitely

- **Category:** Data (DAT)
- **Family:** Data (DATA)
- **Layer:** Data
- **Tier:** 4
- **Severity:** warning
- **Tags:** logs, retention
- **Legacy ID:** ECO-DATA-004

## Summary

Indefinite log retention increases storage and cost without clear value.

## Rationale

Logging without boundaries is a storage leak at organizational scale.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Often a top cost line item.",
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
  "guidance": "Set retention and tiering; sample where appropriate.",
  "tradeoffs": "Less historical detail unless archived."
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
