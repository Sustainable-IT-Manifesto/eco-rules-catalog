# Eco Rules Catalog

A structured catalog of **software inefficiency patterns** that waste compute, energy, network bandwidth, memory, and engineering time.

The Eco Rules Catalog provides:

• **Machine-readable rules** for static analysis tools
• **Human-readable documentation** explaining each inefficiency
• **Remediation guidance** for developers
• **Examples** showing inefficient vs improved code

The goal is simple:

> Make software inefficiency visible so it can be fixed.

---

# Why This Matters

Modern software systems waste enormous resources through small inefficiencies.

Examples include:

* repeated string concatenation
* unbounded network retries
* unnecessary serialization
* oversized data payloads
* inefficient query patterns
* excessive logging or polling

Individually these look harmless.

Across millions of executions they become:

* higher cloud costs
* increased latency
* unnecessary energy usage
* larger environmental footprint

The Eco Rules Catalog helps identify these patterns.

---

# Repository Contents

```
master.json
generate_human_catalog.py
requirements.txt

examples/
families/
eco_catalog_human/
```

| File                        | Purpose                                 |
| --------------------------- | --------------------------------------- |
| `master.json`               | canonical machine-readable rule catalog |
| `generate_human_catalog.py` | documentation generator                 |
| `examples/`                 | optional rule examples                  |
| `eco_catalog_human/`        | generated human documentation           |

---

# Rule Structure

Each rule contains structured metadata.

Example:

```json
{
  "id": "ECO-PY-001",
  "title": "Repeated String Concatenation in Loops",
  "family": "python",
  "layer": "code",
  "tier": 1,
  "severity": "medium"
}
```

Rules also include:

* rationale
* impact
* detection guidance
* remediation guidance

---

# Rule Dimensions

Rules are categorized by three dimensions.

### Family

Technology ecosystem.

Examples:

* Python
* JavaScript
* Java
* Network
* Data
* AI
* Architecture

---

### Layer

Where the inefficiency occurs.

Examples:

* code
* data
* network
* architecture
* ai
* organizational

---

### Tier

Complexity level.

| Tier | Meaning                      |
| ---- | ---------------------------- |
| 1    | common inefficiencies        |
| 2    | structural inefficiencies    |
| 3    | architectural inefficiencies |
| 4    | system-level inefficiencies  |

---

# Generate Human Documentation

Install dependencies:

```
pip install -r requirements.txt
```

Generate documentation:

```
python generate_human_catalog.py \
  --in master.json \
  --out eco_catalog_human
```

---

# Adding Examples

Examples make rules easier to understand.

Create files:

```
examples/ECO-PY-001.md
examples/ECO-NET-002.md
```

Example:

```
## Bad

for item in items:
    s += item

## Better

s = "".join(items)
```

Generate documentation with examples:

```
python generate_human_catalog.py \
  --in master.json \
  --out eco_catalog_human \
  --examples-dir examples
```

---

# Example Stub Generation

Create empty templates for all rules:

```
python generate_human_catalog.py \
  --in master.json \
  --out eco_catalog_human \
  --examples-template examples
```

---

# Intended Uses

The catalog can power:

• static analyzers
• CI/CD enforcement
• sustainability audits
• engineering education
• performance reviews

---

# Relationship to Sustainable IT

This catalog supports the **Sustainable IT Manifesto** by helping organizations move through the maturity pathway:

Aware → Conscious → Enabled → Empowered

---

# Contributing

See `RULE_AUTHORING_GUIDE.md`.

## Suggested Contributor Quickstart

```
make venv
make install
make install-dev

make normalize
make validate
make docs
```


---

# License

MIT License

Copyright (c) 2026 Sustainable IT Manifesto

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


