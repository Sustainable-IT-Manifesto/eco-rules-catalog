# Rule Authoring Guide

This guide explains how to add new rules to the Eco Rules Catalog.

---

# Rule Philosophy

A rule should identify a **repeatable inefficiency pattern**.

Good rules are:

• observable
• detectable
• actionable
• technology-agnostic when possible

---

# Rule ID Format

```
ECO-<FAMILY>-NNN
```

Examples:

```
ECO-PY-001
ECO-JS-014
ECO-NET-003
```

---

# Required Fields

| Field    | Description                         |
| -------- | ----------------------------------- |
| id       | unique rule identifier              |
| title    | short description                   |
| summary  | explanation of inefficiency         |
| family   | technology ecosystem                |
| layer    | system layer                        |
| tier     | complexity level                    |
| severity | informational / low / medium / high |

---

# Optional Fields

| Field       | Description            |
| ----------- | ---------------------- |
| rationale   | why the rule exists    |
| tags        | keywords               |
| impact      | type of resource waste |
| detection   | detection approach     |
| remediation | suggested improvement  |

---

# Impact Object

Example:

```json
"impact": {
  "type": "cpu",
  "confidence": 0.8,
  "notes": "creates excessive memory allocations"
}
```

---

# Detection Object

Example:

```json
"detection": {
  "method": "AST",
  "pattern": "string concatenation inside loop"
}
```

---

# Remediation Object

Example:

```json
"remediation": {
  "guidance": "Use join() instead of repeated concatenation"
}
```

---

# Example Snippets

Each rule should ideally include an example.

Add files:

```
examples/<RULE_ID>.md
```

Example structure:

```
## Bad

<inefficient code>

## Better

<improved code>
```

---

# Good Rule Characteristics

A strong rule:

• detects a real inefficiency
• avoids false positives
• has clear remediation

---

# Poor Rule Characteristics

Avoid rules that:

• are purely stylistic
• cannot be detected automatically
• lack clear remediation


# Checklist

A checklist for rules is in `docs/ontology/checklist.md`
