# ECO-ORG-PROC-006 — No lifecycle data policy

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** data, lifecycle
- **Legacy ID:** ECO-PROC-006

## Summary

Missing lifecycle policies cause unbounded storage and compliance risk.

## Rationale

Lifecycle policies keep data intentional and bounded.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "Systemic.",
  "type": "storage"
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
  "guidance": "Define retention/archival/deletion policies and owners.",
  "tradeoffs": "Org alignment work."
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
