#!/usr/bin/env python3
"""
check_all.py

Run the full Eco Rules Catalog validation chain:

1. JSON Schema validation
2. Normalization drift check
3. Ontology validation
4. Cross-registry catalog validation

Python: 3.6+

Usage:
  python tools/check_all.py

  python tools/check_all.py --strict

  python tools/check_all.py \
    --catalog master.json \
    --categories ontology/categories.json \
    --families ontology/families.json
"""

import argparse
import subprocess
import sys


def run_step(name, cmd):
    print("")
    print("==> {}".format(name))
    print("    {}".format(" ".join(cmd)))
    result = subprocess.run(cmd)
    return result.returncode


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--python", default=sys.executable)
    ap.add_argument("--catalog", default="master.json")
    ap.add_argument("--categories", default="ontology/categories.json")
    ap.add_argument("--families", default="ontology/families.json")
    ap.add_argument("--schema-catalog", default="schema/schema-catalog.json")
    ap.add_argument("--schema-categories", default="schema/schema-categories.json")
    ap.add_argument("--schema-families", default="schema/schema-families.json")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    py = args.python
    failures = []

    steps = [
        (
            "Schema validation: catalog",
            [py, "tools/validate_schema.py", "--schema", args.schema_catalog, "--data", args.catalog],
        ),
        (
            "Schema validation: categories",
            [py, "tools/validate_schema.py", "--schema", args.schema_categories, "--data", args.categories],
        ),
        (
            "Schema validation: families",
            [py, "tools/validate_schema.py", "--schema", args.schema_families, "--data", args.families],
        ),
        (
            "Normalization drift check",
            [py, "tools/normalize_ontology.py", "--in", args.catalog, "--check", "--fill-system-layer"],
        ),
        (
            "Ontology validation",
            [py, "tools/validate_ontology.py", "--in", args.catalog, "--require-ontology"]
            + (["--strict"] if args.strict else []),
        ),
        (
            "Cross-registry catalog validation",
            [
                py,
                "tools/validate_catalog.py",
                "--catalog",
                args.catalog,
                "--categories",
                args.categories,
                "--families",
                args.families,
            ]
            + (["--strict"] if args.strict else []),
        ),
    ]

    for name, cmd in steps:
        rc = run_step(name, cmd)
        if rc != 0:
            failures.append((name, rc))

    print("")
    print("========================================")
    print("Check summary")
    print("========================================")

    if not failures:
        print("All checks passed.")
        return 0

    print("Failed steps: {}".format(len(failures)))
    for name, rc in failures:
        print("- {} (exit code {})".format(name, rc))

    return 1


if __name__ == "__main__":
    sys.exit(main())
