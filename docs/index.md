# Eco Rules Catalog

The Eco Rules Catalog defines **detectable patterns of software inefficiency**.

Each rule describes:

* what the inefficiency is
* why it matters
* how to detect it
* how to fix it

Rules are structured so they can be used by:

* static analysis tools
* CI/CD pipelines
* engineering audits
* developer education platforms

---

# Structure

Rules are categorized by:

• Family (technology)
• Layer (system location)
• Tier (complexity)

Example:

```
ECO-PY-001
Family: Python
Layer: Code
Tier: 1
```

---

# Documentation

Generate human-readable docs:

```
python generate_human_catalog.py \
  --in master.json \
  --out eco_catalog_human
```

---

# Philosophy

Small inefficiencies accumulate.

The goal is to make them **visible and fixable**.

