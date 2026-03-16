#!/usr/bin/env python3
"""
validate_catalog.py

Validate Eco Rules catalog integrity against registry files.

Checks:
- category exists in categories.json
- family exists in families.json
- family.category matches rule.category
- category_code matches categories registry
- family_code matches families registry
- id matches derived value: ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ>
- canonical_id matches id
- legacy_id is optional
- id uniqueness
- canonical_id uniqueness
- optional checks for tier / severity / layer

Python: 3.6+

Usage:
  python tools/validate_catalog.py \
    --catalog master.json \
    --categories ontology/categories.json \
    --families ontology/families.json

  python tools/validate_catalog.py \
    --catalog master.json \
    --categories ontology/categories.json \
    --families ontology/families.json \
    --strict

Exit codes:
  0 = OK
  1 = Validation errors
  2 = Invalid input / runtime error
"""

import argparse
import json
import re
import sys
from collections import Counter

VALID_SEVERITIES = {
    "note", "warning", "error", "info",
    "low", "medium", "high", "critical"
}

VALID_LAYERS = {
    "Code", "Runtime", "Data", "Network",
    "Architecture", "AI/ML", "Organizational"
}

NEW_ID_PATTERN = re.compile(r"^ECO-[A-Z]{3}-[A-Z0-9]{2,6}-\d{3}$")
LEGACY_ID_PATTERN = re.compile(r"^ECO-[A-Z0-9]+-\d{3}$")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_category_lookup(categories):
    by_name = {}
    by_code = {}
    for c in categories:
        name = c.get("name")
        code = c.get("code")
        if name:
            by_name[name] = c
        if code:
            by_code[code] = c
    return by_name, by_code


def build_family_lookup(families):
    by_name = {}
    by_code = {}
    for f in families:
        name = f.get("name")
        code = f.get("code")
        if name:
            by_name[name] = f
        if code:
            by_code[code] = f
    return by_name, by_code


def extract_sequence(rule_id):
    """
    From:
      ECO-PY-001          -> 001
      ECO-CMP-PY-001      -> 001
      ECO-NET-HTTP-005    -> 005
    """
    if not isinstance(rule_id, str):
        return None

    parts = rule_id.split("-")
    if not parts:
        return None

    seq = parts[-1]
    if re.match(r"^\d+$", seq):
        return seq

    return None


def derive_primary_id(rule):
    seq = extract_sequence(rule.get("id")) or extract_sequence(rule.get("legacy_id"))
    category_code = rule.get("category_code")
    family_code = rule.get("family_code")

    if not seq or not category_code or not family_code:
        return None

    return "ECO-{}-{}-{}".format(category_code, family_code, seq)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True, help="Path to master.json")
    ap.add_argument("--categories", required=True, help="Path to ontology/categories.json")
    ap.add_argument("--families", required=True, help="Path to ontology/families.json")
    ap.add_argument("--strict", action="store_true", help="Enable stricter checks on tier/severity/layer")
    args = ap.parse_args()

    try:
        catalog = load_json(args.catalog)
        categories = load_json(args.categories)
        families = load_json(args.families)
    except Exception as e:
        print("ERROR: failed to load input files: {}".format(e))
        return 2

    rules = catalog.get("rules")
    if not isinstance(rules, list):
        print("ERROR: catalog['rules'] must be a list")
        return 2

    if not isinstance(categories, list):
        print("ERROR: categories.json must be a list")
        return 2

    if not isinstance(families, list):
        print("ERROR: families.json must be a list")
        return 2

    category_by_name, category_by_code = build_category_lookup(categories)
    family_by_name, family_by_code = build_family_lookup(families)

    errors = []
    warnings = []

    def add_error(rule_id, msg):
        errors.append({"rule_id": rule_id, "message": msg})

    def add_warning(rule_id, msg):
        warnings.append({"rule_id": rule_id, "message": msg})

    # ------------------------------------------------------------------
    # Registry integrity
    # ------------------------------------------------------------------
    category_names = [c.get("name") for c in categories if c.get("name")]
    category_codes = [c.get("code") for c in categories if c.get("code")]
    family_names = [f.get("name") for f in families if f.get("name")]
    family_codes = [f.get("code") for f in families if f.get("code")]

    for name, count in Counter(category_names).items():
        if count > 1:
            errors.append({
                "rule_id": "__registry__",
                "message": "Duplicate category name: {}".format(name)
            })

    for code, count in Counter(category_codes).items():
        if count > 1:
            errors.append({
                "rule_id": "__registry__",
                "message": "Duplicate category code: {}".format(code)
            })

    for name, count in Counter(family_names).items():
        if count > 1:
            errors.append({
                "rule_id": "__registry__",
                "message": "Duplicate family name: {}".format(name)
            })

    for code, count in Counter(family_codes).items():
        if count > 1:
            errors.append({
                "rule_id": "__registry__",
                "message": "Duplicate family code: {}".format(code)
            })

    for fam in families:
        fam_name = fam.get("name", "UNKNOWN")
        fam_category = fam.get("category")
        if fam_category not in category_by_name:
            errors.append({
                "rule_id": "__registry__",
                "message": "Family '{}' references unknown category '{}'".format(
                    fam_name, fam_category
                )
            })

    # ------------------------------------------------------------------
    # Uniqueness checks
    # ------------------------------------------------------------------
    rule_ids = [r.get("id") for r in rules if r.get("id")]
    canonical_ids = [r.get("canonical_id") for r in rules if r.get("canonical_id")]
    legacy_ids = [r.get("legacy_id") for r in rules if r.get("legacy_id")]

    for rid, count in Counter(rule_ids).items():
        if count > 1:
            errors.append({
                "rule_id": "__catalog__",
                "message": "Duplicate rule id: {}".format(rid)
            })

    for cid, count in Counter(canonical_ids).items():
        if count > 1:
            errors.append({
                "rule_id": "__catalog__",
                "message": "Duplicate canonical_id: {}".format(cid)
            })

    # legacy_id uniqueness is useful but maybe warning, not error
    for lid, count in Counter(legacy_ids).items():
        if count > 1:
            warnings.append({
                "rule_id": "__catalog__",
                "message": "Duplicate legacy_id: {}".format(lid)
            })

    # ------------------------------------------------------------------
    # Per-rule validation
    # ------------------------------------------------------------------
    for rule in rules:
        rid = rule.get("id", "UNKNOWN")

        category = rule.get("category")
        category_code = rule.get("category_code")
        family = rule.get("family")
        family_code = rule.get("family_code")
        canonical_id = rule.get("canonical_id")
        legacy_id = rule.get("legacy_id")

        # Category / family existence
        if not category:
            add_error(rid, "Missing category")
        elif category not in category_by_name:
            add_error(rid, "Unknown category '{}'".format(category))

        if not family:
            add_error(rid, "Missing family")
        elif family not in family_by_name:
            add_error(rid, "Unknown family '{}'".format(family))

        # category_code match
        if category in category_by_name:
            expected_category_code = category_by_name[category].get("code")
            if category_code != expected_category_code:
                add_error(
                    rid,
                    "category_code mismatch: expected '{}', found '{}'".format(
                        expected_category_code, category_code
                    )
                )

        # family_code + category match
        if family in family_by_name:
            expected_family_code = family_by_name[family].get("code")
            expected_family_category = family_by_name[family].get("category")

            if family_code != expected_family_code:
                add_error(
                    rid,
                    "family_code mismatch: expected '{}', found '{}'".format(
                        expected_family_code, family_code
                    )
                )

            if category and expected_family_category != category:
                add_error(
                    rid,
                    "Family/category mismatch: family '{}' belongs to '{}', but rule category is '{}'".format(
                        family, expected_family_category, category
                    )
                )

        # New primary id format
        if not isinstance(rid, str) or not NEW_ID_PATTERN.match(rid):
            add_error(
                rid,
                "Primary id must match ECO-<CATEGORY_CODE>-<FAMILY_CODE>-<SEQ>, found '{}'".format(rid)
            )

        # legacy_id optional, but if present should look like an old-style ID
        if legacy_id is not None:
            if not isinstance(legacy_id, str) or not LEGACY_ID_PATTERN.match(legacy_id):
                add_warning(
                    rid,
                    "legacy_id does not look like a legacy ECO id: '{}'".format(legacy_id)
                )

        # Derived primary id check
        expected_primary_id = derive_primary_id(rule)
        if expected_primary_id:
            if rid != expected_primary_id:
                add_error(
                    rid,
                    "id mismatch: expected '{}', found '{}'".format(
                        expected_primary_id, rid
                    )
                )
        else:
            add_warning(rid, "Could not derive expected primary id")

        # canonical_id should equal id in the new model
        if canonical_id != rid:
            add_error(
                rid,
                "canonical_id mismatch: expected '{}', found '{}'".format(
                    rid, canonical_id
                )
            )

        # Optional stricter checks
        if args.strict:
            tier = rule.get("tier")
            if not isinstance(tier, int):
                add_error(rid, "tier must be an integer")
            elif tier < 1 or tier > 4:
                add_error(rid, "tier must be between 1 and 4")

            severity = rule.get("severity")
            if severity and severity not in VALID_SEVERITIES:
                add_error(rid, "Unknown severity '{}'".format(severity))

            layer = rule.get("layer")
            if layer and layer not in VALID_LAYERS:
                add_warning(
                    rid,
                    "Layer '{}' is not in canonical layer vocab".format(layer)
                )

    # ------------------------------------------------------------------
    # Print summary
    # ------------------------------------------------------------------
    print("")
    print("Eco Rules Catalog Validation")
    print("Catalog: {}".format(args.catalog))
    print("Rules: {}".format(len(rules)))
    print("Errors: {}".format(len(errors)))
    print("Warnings: {}".format(len(warnings)))
    print("")

    max_list = 200

    if errors:
        print("Errors:")
        for e in errors[:max_list]:
            print("- {}: {}".format(e["rule_id"], e["message"]))
        if len(errors) > max_list:
            print("  ...and {} more".format(len(errors) - max_list))
        print("")

    if warnings:
        print("Warnings:")
        for w in warnings[:max_list]:
            print("- {}: {}".format(w["rule_id"], w["message"]))
        if len(warnings) > max_list:
            print("  ...and {} more".format(len(warnings) - max_list))
        print("")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
