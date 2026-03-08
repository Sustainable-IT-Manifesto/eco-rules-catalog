#!/usr/bin/env python3
import argparse, json, os, subprocess, sys
from datetime import datetime

def run(cmd, label):
    print("\n==> {}".format(label))
    print("    {}".format(" ".join(cmd)))
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print("\nERROR: step failed: {}".format(label))
        return result.returncode
    return 0

def ensure_parent_dir(path):
    if not path:
        return
    parent = os.path.dirname(os.path.abspath(path))
    if parent and not os.path.isdir(parent):
        os.makedirs(parent)

def write_report(path, report):
    ensure_parent_dir(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2, sort_keys=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", required=True)
    ap.add_argument("--categories", default="ontology/categories.json")
    ap.add_argument("--families", default="ontology/families.json")
    ap.add_argument("--human-out", default="eco_catalog_human")
    ap.add_argument("--site-index-out", default="docs-site/docs/catalog/_data/catalog_index.json")
    ap.add_argument("--examples-dir", default=None)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--skip-update", action="store_true")
    ap.add_argument("--skip-validate", action="store_true")
    ap.add_argument("--skip-human", action="store_true")
    ap.add_argument("--skip-site-assets", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--report-out", default=None)
    ap.add_argument("--python", default=sys.executable)
    args = ap.parse_args()

    report = {
        "generated_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "catalog": args.catalog,
        "categories": args.categories,
        "families": args.families,
        "human_out": args.human_out,
        "site_index_out": args.site_index_out,
        "examples_dir": args.examples_dir,
        "steps": [],
        "success": False,
    }

    py = args.python

    if not args.skip_update:
        cmd = [py, "tools/update_rules.py", "--catalog", args.catalog, "--categories", args.categories, "--families", args.families, "--fill-system-layer", "--normalize-ontology"]
        if args.write: cmd.append("--write")
        else: cmd.extend(["--out", args.catalog + ".updated.json"])
        rc = run(cmd, "Update rules")
        report["steps"].append({"name":"update_rules","returncode":rc})
        if rc != 0:
            if args.report_out: write_report(args.report_out, report)
            return rc

    if not args.skip_validate:
        cmd = [py, "tools/validate_ontology.py", "--in", args.catalog, "--require-ontology"]
        if args.strict: cmd.append("--strict")
        rc = run(cmd, "Validate ontology")
        report["steps"].append({"name":"validate_ontology","returncode":rc})
        if rc != 0:
            if args.report_out: write_report(args.report_out, report)
            return rc
        cmd = [py, "tools/validate_catalog.py", "--catalog", args.catalog, "--categories", args.categories, "--families", args.families]
        if args.strict: cmd.append("--strict")
        rc = run(cmd, "Validate catalog")
        report["steps"].append({"name":"validate_catalog","returncode":rc})
        if rc != 0:
            if args.report_out: write_report(args.report_out, report)
            return rc

    if not args.skip_human:
        cmd = [py, "generate_human_catalog.py", "--in", args.catalog, "--out", args.human_out]
        if args.examples_dir: cmd.extend(["--examples-dir", args.examples_dir])
        rc = run(cmd, "Generate human-readable catalog")
        report["steps"].append({"name":"generate_human_catalog","returncode":rc})
        if rc != 0:
            if args.report_out: write_report(args.report_out, report)
            return rc

    if not args.skip_site_assets:
        cmd = [py, "tools/build_site_assets.py", "--in", args.catalog, "--out", args.site_index_out]
        rc = run(cmd, "Build site assets")
        report["steps"].append({"name":"build_site_assets","returncode":rc})
        if rc != 0:
            if args.report_out: write_report(args.report_out, report)
            return rc

    report["success"] = True
    print("\nPublish pipeline completed successfully.")
    if args.report_out:
        write_report(args.report_out, report)
        print("Wrote report: {}".format(args.report_out))
    return 0

if __name__ == "__main__":
    sys.exit(main())
