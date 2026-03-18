# ECO-ORG-PROC-011 — No decommissioning workflow

- **Category:** Organizational (ORG)
- **Family:** Process (PROC)
- **Layer:** Process
- **Tier:** 4
- **Severity:** warning
- **Tags:** decommissioning
- **Legacy ID:** ECO-PROC-011

## Summary

Without decommissioning, dead systems stay alive and waste resources.

## Rationale

Zombie services are pure waste: cost, risk, and attention.

## Impact

```json
{
  "confidence": 0.8,
  "notes": "Common in mature orgs too.",
  "type": "cost"
}
```

## Detection

```json
{
  "languages": [
    "org"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Create a decommission playbook and ownership model.",
  "tradeoffs": "Cross-team coordination."
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
