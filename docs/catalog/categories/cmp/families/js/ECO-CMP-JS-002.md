# ECO-CMP-JS-002 — Polling instead of events

- **Category:** Computation (CMP)
- **Family:** JavaScript (JS)
- **Layer:** Network
- **Tier:** 2
- **Severity:** warning
- **Tags:** javascript, polling, network
- **Legacy ID:** ECO-JS-002

## Summary

Polling increases unnecessary network traffic and compute.

## Rationale

Polling wastes cycles when nothing changes; push shifts work to when it matters.

## Impact

```json
{
  "confidence": 0.7,
  "notes": "Often significant at scale.",
  "type": "network"
}
```

## Detection

```json
{
  "languages": [
    "javascript"
  ],
  "method": "regex"
}
```

## Remediation

```json
{
  "guidance": "Use webhooks, SSE, websockets, or event-driven patterns.",
  "tradeoffs": "More moving parts."
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
