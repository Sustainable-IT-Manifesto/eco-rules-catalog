# ECO-NET-NET-005 — Missing timeouts

- **Category:** Networking (NET)
- **Family:** Network (NET)
- **Layer:** Network
- **Tier:** 2
- **Severity:** error
- **Tags:** timeouts, reliability
- **Legacy ID:** ECO-NET-005

## Summary

Missing timeouts remove a critical reliability boundary for network calls.

## Rationale

Timeouts prevent hangs from turning into cascading failures.

## Impact

```json
{
  "confidence": 0.85,
  "notes": "High propagation during partial outages.",
  "type": "reliability"
}
```

## Detection

```json
{
  "languages": [
    "python",
    "javascript",
    "java",
    "infra"
  ],
  "method": "hybrid"
}
```

## Remediation

```json
{
  "guidance": "Set explicit connect/read timeouts; standardize defaults.",
  "tradeoffs": "Endpoint tuning required."
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
