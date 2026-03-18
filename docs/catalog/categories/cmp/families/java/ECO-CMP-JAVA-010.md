# ECO-CMP-JAVA-010 — Debug logging in production hot path

- **Category:** Computation (CMP)
- **Family:** Java (JAVA)
- **Layer:** Code
- **Tier:** 1
- **Severity:** note
- **Tags:** java, logging
- **Legacy ID:** ECO-JAVA-010

## Summary

Verbose logs in hot paths waste CPU and I/O.

## Rationale

Logging can become a dominant cost under high throughput.

## Impact

```json
{
  "confidence": 0.6,
  "notes": "Worse with sync appenders.",
  "type": "io"
}
```

## Detection

```json
{
  "languages": [
    "java"
  ],
  "method": "config"
}
```

## Remediation

```json
{
  "guidance": "Lower verbosity; sample; avoid heavy string formatting unless enabled.",
  "tradeoffs": "Less detail unless sampled."
}
```

## Ontology

```json
{
  "system_layers": [
    "code"
  ]
}
```
