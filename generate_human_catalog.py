#!/usr/bin/env python3
"""
Family-first human-readable rendering of the Eco Rules JSON catalog.
Supports optional examples and HTML output.
"""
import argparse
import datetime
import json
import os
import re
import shutil
from collections import defaultdict

def slugify(s):
    s = (s or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "item"

def safe_filename(name):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", name or "UNKNOWN")

def md_escape(s):
    if s is None:
        return ""
    return str(s).replace("\r\n", "\n").replace("\r", "\n")

def relpath(from_path, to_path):
    return os.path.relpath(to_path, os.path.dirname(from_path)).replace("\\", "/")

def render_examples(rule, examples_dir=None):
    parts = []
    ex = None
    for k in ("examples","example","demo","demonstration"):
        if k in rule:
            ex = rule.get(k)
            break
    if ex:
        if isinstance(ex, list):
            for item in ex:
                if isinstance(item, dict):
                    parts.append("```json\n" + json.dumps(item, ensure_ascii=False, indent=2, sort_keys=True) + "\n```")
                else:
                    parts.append(str(item))
        elif isinstance(ex, dict):
            parts.append("```json\n" + json.dumps(ex, ensure_ascii=False, indent=2, sort_keys=True) + "\n```")
        else:
            parts.append(str(ex))
    if examples_dir:
        path = os.path.join(examples_dir, safe_filename(rule.get("id","UNKNOWN")) + ".md")
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as f:
                parts.append(f.read().strip())
    return "\n\n".join([p for p in parts if p and str(p).strip()])

def rule_md(rule, rel_root_index, examples_dir=None):
    rid = rule.get("id","UNKNOWN")
    title = rule.get("title","")
    summary = rule.get("summary","")
    category = rule.get("category","Uncategorized")
    family = rule.get("family","Uncategorized")
    layer = rule.get("layer","Uncategorized")
    tier = rule.get("tier","")
    severity = rule.get("severity","")
    enabled = rule.get("enabled_by_default", None)
    tags = rule.get("tags", [])
    rationale = rule.get("rationale","")
    impact = rule.get("impact", {})
    detection = rule.get("detection", {})
    remediation = rule.get("remediation", {})

    lines=[]
    lines.append("# {} — {}".format(md_escape(rid), md_escape(title)).strip())
    lines.append("")
    lines.append("- **Category:** {}".format(md_escape(category)))
    lines.append("- **Family:** {}".format(md_escape(family)))
    lines.append("- **Layer:** {}".format(md_escape(layer)))
    if tier != "":
        lines.append("- **Tier:** {}".format(md_escape(tier)))
    if severity:
        lines.append("- **Severity:** {}".format(md_escape(severity)))
    if enabled is not None:
        lines.append("- **Enabled by default:** {}".format(str(enabled).lower()))
    if tags:
        lines.append("- **Tags:** {}".format(", ".join([md_escape(t) for t in tags])))
    lines.append("")

    if summary:
        lines.append("## Summary\n")
        lines.append(md_escape(summary).strip() + "\n")

    if rationale:
        lines.append("## Rationale\n")
        lines.append(md_escape(rationale).strip() + "\n")

    if impact:
        lines.append("## Impact (raw)\n")
        lines.append("```json")
        lines.append(json.dumps(impact, ensure_ascii=False, indent=2, sort_keys=True))
        lines.append("```\n")

    if detection:
        lines.append("## Detection (raw)\n")
        lines.append("```json")
        lines.append(json.dumps(detection, ensure_ascii=False, indent=2, sort_keys=True))
        lines.append("```\n")

    if remediation:
        lines.append("## Remediation (raw)\n")
        lines.append("```json")
        lines.append(json.dumps(remediation, ensure_ascii=False, indent=2, sort_keys=True))
        lines.append("```\n")

    examples_text = render_examples(rule, examples_dir=examples_dir)
    if examples_text:
        lines.append("## Example\n")
        lines.append(examples_text.strip() + "\n")

    lines.append("---\n")
    lines.append("Back to catalog index: [index.md]({})\n".format(rel_root_index))
    return "\n".join(lines)

def write_example_stubs(rules, examples_template_dir):
    os.makedirs(examples_template_dir, exist_ok=True)
    created = 0
    skipped = 0
    for r in rules:
        rid = r.get("id","UNKNOWN")
        fp = os.path.join(examples_template_dir, safe_filename(rid) + ".md")
        if os.path.exists(fp):
            skipped += 1
            continue
        title = r.get("title","")
        category = r.get("category","Uncategorized")
        family = r.get("family","Uncategorized")
        layer = r.get("layer","Uncategorized")
        tier = r.get("tier","")
        severity = r.get("severity","")
        stub = []
        stub.append("# Example: {} — {}".format(rid, title).strip())
        stub.append("")
        stub.append("- Category: {}".format(category))
        stub.append("- Family: {}".format(family))
        stub.append("- Layer: {}".format(layer))
        if tier != "":
            stub.append("- Tier: {}".format(tier))
        if severity:
            stub.append("- Severity: {}".format(severity))
        stub.append("")
        stub.append("Write a short paragraph and/or a code snippet demonstrating the rule.")
        stub.append("")
        stub.append("## Bad")
        stub.append("")
        stub.append("```")
        stub.append("# add a minimal 'bad' example here")
        stub.append("```")
        stub.append("")
        stub.append("## Better")
        stub.append("")
        stub.append("```")
        stub.append("# add a minimal 'better' example here")
        stub.append("```")
        stub.append("")
        with open(fp, "w", encoding="utf-8") as f:
            f.write("\n".join(stub))
        created += 1
    return created, skipped

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="in_path", required=True)
    ap.add_argument("--out", dest="out_dir", required=True)
    ap.add_argument("--examples-dir", dest="examples_dir", default=None, help="Folder containing <RULE_ID>.md example snippets to append")
    ap.add_argument("--examples-template", dest="examples_template_dir", default=None, help="Create stub example files at <dir>/<RULE_ID>.md (does not overwrite)")
    ap.add_argument("--html", action="store_true", help="Also render HTML for each Markdown file using python-markdown")
    args = ap.parse_args()

    with open(args.in_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    rules = catalog.get("rules", [])
    if args.examples_template_dir:
        created, skipped = write_example_stubs(rules, args.examples_template_dir)
        print("Example stubs: created={}, skipped_existing={}".format(created, skipped))

    out_root = args.out_dir
    if os.path.isdir(out_root):
        shutil.rmtree(out_root)
    os.makedirs(out_root, exist_ok=True)

    by_category = defaultdict(list)
    for r in rules:
        by_category[r.get("category","Uncategorized")].append(r)

    categories_dir = os.path.join(out_root, "categories")
    os.makedirs(categories_dir, exist_ok=True)

    root_index_path = os.path.join(out_root, "index.md")
    generated_at = catalog.get("generated_at") or datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    catalog_version = catalog.get("catalog_version","")
    publisher = catalog.get("publisher", {})
    publisher_name = publisher.get("name","")
    publisher_url = publisher.get("url","")

    root_lines=[]
    root_lines.append("# Eco Rules Catalog (Human Readable)\n")
    if catalog_version:
        root_lines.append("**Catalog version:** {}\n".format(catalog_version))
    root_lines.append("**Generated at:** {}\n".format(generated_at))
    if publisher_name:
        root_lines.append("**Publisher:** {}{}\n".format(publisher_name, (" ("+publisher_url+")") if publisher_url else ""))
    root_lines.append("**Total rules:** {}\n".format(len(rules)))
    root_lines.append("## Categories\n")
    for cat in sorted(by_category.keys(), key=lambda s: s.lower()):
        cat_slug = slugify(cat)
        root_lines.append("- [{}](categories/{}/index.md) ({} rules)".format(cat, cat_slug, len(by_category[cat])))
    root_lines.append("")
    root_lines.append("## Rule Index\n")
    root_lines.append("| ID | Title | Category | Family | Layer | Tier | Severity |")
    root_lines.append("|---|---|---|---|---|---:|---|")
    def sort_id(r): return r.get("id","")
    for r in sorted(rules, key=sort_id):
        rid = r.get("id","")
        title = r.get("title","")
        cat = r.get("category","Uncategorized")
        fam = r.get("family","Uncategorized")
        layer = r.get("layer","Uncategorized")
        tier = r.get("tier","")
        severity = r.get("severity","")
        cat_slug = slugify(cat)
        fam_slug = slugify(fam)
        rule_rel = "categories/{}/families/{}/{}.md".format(cat_slug, fam_slug, safe_filename(rid))
        root_lines.append("| [{}]({}) | {} | {} | {} | {} | {} | {} |".format(rid, rule_rel, title, cat, fam, layer, tier, severity))
    with open(root_index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(root_lines))

    for cat, cat_rules in by_category.items():
        cat_slug = slugify(cat)
        cat_path = os.path.join(categories_dir, cat_slug)
        os.makedirs(cat_path, exist_ok=True)

        by_family = defaultdict(list)
        for r in cat_rules:
            by_family[r.get("family","Uncategorized")].append(r)

        cat_index_path = os.path.join(cat_path, "index.md")
        cat_lines=[]
        cat_lines.append("# {} Category\n".format(cat))
        cat_lines.append("- **Category:** {}".format(cat))
        cat_lines.append("- **Total rules:** {}\n".format(len(cat_rules)))
        cat_lines.append("Back to root index: [index.md]({})\n".format(relpath(cat_index_path, root_index_path)))
        cat_lines.append("## Families\n")
        for fam in sorted(by_family.keys(), key=lambda s: s.lower()):
            fam_slug = slugify(fam)
            cat_lines.append("- [{}](families/{}/index.md) ({} rules)".format(fam, fam_slug, len(by_family[fam])))
        cat_lines.append("")
        with open(cat_index_path, "w", encoding="utf-8") as f:
            f.write("\n".join(cat_lines))

        fam_root = os.path.join(cat_path, "families")
        os.makedirs(fam_root, exist_ok=True)

        for fam, fam_rules in by_family.items():
            fam_slug = slugify(fam)
            fam_path = os.path.join(fam_root, fam_slug)
            os.makedirs(fam_path, exist_ok=True)

            fam_index_path = os.path.join(fam_path, "index.md")
            lines=[]
            lines.append("# {} / {}\n".format(cat, fam))
            lines.append("- **Category:** {}".format(cat))
            lines.append("- **Family:** {}".format(fam))
            lines.append("- **Total rules:** {}\n".format(len(fam_rules)))
            lines.append("Back to category index: [index.md]({})\n".format(relpath(fam_index_path, cat_index_path)))
            lines.append("## Rules (grouped by tier)\n")
            tier_groups = defaultdict(list)
            for r in fam_rules:
                tier_groups[r.get("tier", 99)].append(r)
            for tier in sorted(tier_groups.keys(), key=lambda x: x if isinstance(x,int) else 99):
                lines.append("### Tier {}\n".format(tier))
                for r in sorted(tier_groups[tier], key=sort_id):
                    rid = r.get("id","")
                    title = r.get("title","")
                    rule_file = os.path.join(fam_path, safe_filename(rid)+".md")
                    lines.append("- [{} — {}]({})".format(rid, title, relpath(fam_index_path, rule_file)))
                lines.append("")
            with open(fam_index_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))

            for r in fam_rules:
                rid = r.get("id","UNKNOWN")
                rule_file = os.path.join(fam_path, safe_filename(rid)+".md")
                md = rule_md(r, relpath(rule_file, root_index_path), examples_dir=args.examples_dir)
                with open(rule_file, "w", encoding="utf-8") as f:
                    f.write(md)

    if args.html:
        try:
            import markdown
        except Exception as e:
            raise SystemExit("python-markdown is required for --html. Install from requirements.txt") from e

        for root, dirs, files in os.walk(out_root):
            for fn in files:
                if fn.endswith(".md"):
                    md_path = os.path.join(root, fn)
                    html_path = md_path[:-3] + ".html"
                    with open(md_path, "r", encoding="utf-8") as f:
                        md_text = f.read()
                    html = markdown.markdown(md_text, extensions=["tables", "toc", "fenced_code"])
                    doc = "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'><title>{}</title></head><body>{}</body></html>".format(fn, html)
                    with open(html_path, "w", encoding="utf-8") as f:
                        f.write(doc)

if __name__ == "__main__":
    main()
