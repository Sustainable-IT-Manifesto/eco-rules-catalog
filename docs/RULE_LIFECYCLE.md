# Eco Rules Catalog — Rule Lifecycle

This document describes how rules evolve within the Eco Rules Catalog.

Rules are not static. They move through a lifecycle as the community
gains confidence in their detection accuracy, impact, and applicability.

The lifecycle ensures that the catalog remains:

- technically credible
- stable for tools
- adaptable to new knowledge

---

## Rule States

```text
Draft → Candidate → Accepted → Stable → Deprecated → Retired
```

---

## Draft

A **Draft rule** represents an idea for an inefficiency pattern.

Characteristics:

* preliminary description
* detection strategy may be incomplete
* ontology classification may change
* sequence number may change

Draft rules are not included in production catalogs.

Location:

```
rules/draft/
```

---

## Candidate

A **Candidate rule** is technically defined but still under evaluation.

Characteristics:

* rule definition complete
* detection approach proposed
* ontology defined
* impact model defined

However:

* detection accuracy may still be uncertain
* false positives may exist
* remediation guidance may still evolve

Candidate rules may be included in experimental toolchains.

---

## Accepted

An **Accepted rule** has demonstrated:

* clear inefficiency pattern
* reliable detection
* clear remediation path
* meaningful resource impact

Accepted rules become part of the **official catalog**.

---

## Stable

A **Stable rule** has demonstrated:

* broad applicability
* reliable automated detection
* stable taxonomy placement
* long-term usefulness

Stable rules are expected to remain unchanged across catalog versions.

---

## Deprecated

A rule becomes **Deprecated** when:

* a better rule replaces it
* detection proves unreliable
* the inefficiency pattern becomes obsolete

Deprecated rules remain in the catalog but should not be used for new analysis.

---

## Retired

A **Retired rule** is removed from the active catalog.

Reasons include:

* invalidated pattern
* superseded by architecture evolution
* no longer relevant

Retired rules remain documented for historical reference.

---

## Lifecycle Transitions

Typical progression:

```
Draft
   ↓
Candidate
   ↓
Accepted
   ↓
Stable
```

Occasionally:

```
Accepted → Deprecated → Retired
```

---

## Versioning

Catalog versions follow semantic versioning principles:

```
MAJOR.MINOR.PATCH
```

Changes:

| Version Change | Meaning                           |
| -------------- | --------------------------------- |
| MAJOR          | breaking taxonomy or ID changes   |
| MINOR          | new rules added                   |
| PATCH          | documentation or metadata updates |

---

## Rule Stability Guarantees

Once a rule becomes **Stable**:

* its **primary ID must not change**
* taxonomy placement should not change
* ontology tags should remain stable

Breaking changes require a new rule ID.


