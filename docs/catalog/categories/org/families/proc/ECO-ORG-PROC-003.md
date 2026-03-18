# ECO-ORG-PROC-003 — No cost observability

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** finops, cost
- **Legacy ID:** ECO-PROC-003

## Summary

Without cost attribution, waste persists unmanaged.

## Rationale

If teams can’t see cost per service, they can’t act on it.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "Systemic.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Implement cost allocation, tagging, and service-level chargeback/showback.",
  "tradeoffs": "Org/process change."
}
```

## Ontology

```json
{
  "system_layers": [
    "process"
  ]
}
```
