# ECO-NET-NET-009 — Under-fetching causing follow-up calls

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 1
- **Severity:** note
- **Tags:** api, chattiness
- **Legacy ID:** ECO-NET-009

## Summary

Responses missing needed data cause extra round trips.

## Rationale

Follow-up calls are hidden multiplicative cost.

## Impact

```json
{
  "confidence": 0.55,
  "notes": "Context-dependent.",
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
  "guidance": "Batch endpoints; design responses around common usage.",
  "tradeoffs": "Bigger payloads in some cases."
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
