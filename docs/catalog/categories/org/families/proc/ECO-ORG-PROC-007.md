# ECO-ORG-PROC-007 — No energy-aware CI/CD metrics

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** note
- **Tags:** cicd, waste
- **Legacy ID:** ECO-PROC-007

## Summary

Build/test pipelines can waste large amounts of compute when unmeasured.

## Rationale

CI is often a hidden always-on compute bill.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Depends on org scale.",
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
  "guidance": "Measure build minutes, cache hits, and pipeline efficiency; reduce waste.",
  "tradeoffs": "Instrumentation effort."
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
