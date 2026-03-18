# ECO-NET-NET-008 — Over-fetching API fields

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 1
- **Severity:** note
- **Tags:** api, payload
- **Legacy ID:** ECO-NET-008

## Summary

Returning unnecessary fields increases payload size and processing.

## Rationale

Extra bytes multiply across calls and users.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Often easy wins.",
  "type": "network"
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
  "guidance": "Use sparse fieldsets; avoid sending unused data.",
  "tradeoffs": "API contract changes."
}
```

## Ontology

```json
{
  "system_layers": [
    "network"
  ]
}
```
