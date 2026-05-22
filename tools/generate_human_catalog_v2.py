#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MASTER = ROOT / "catalog" / "master.json"
DEFAULT_REGISTRY = ROOT / "catalog" / "registry.json"
DEFAULT_OUT_DIR = ROOT / "docs" / "catalog"
DEFAULT_EXAMPLES_DIR = ROOT / "examples"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def get_rules(catalog: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted(catalog.get("rules", []), key=lambda r: r.get("id", ""))


def ensure_out(out: Path, clean: bool = False) -> None:
    if clean and out.exists():
        shutil.rmtree(out)
    for sub in ["", "layers", "categories", "examples"]:
        (out / sub).mkdir(parents=True, exist_ok=True)


def slug(code: str) -> str:
    return str(code).strip().lower()


def rule_name(rule: dict[str, Any]) -> str:
    return rule.get("name") or rule.get("title") or rule.get("id", "UNKNOWN")


def category_name(rule: dict[str, Any]) -> str:
    return str(rule.get("category") or rule.get("ontology", {}).get("category") or rule.get("category_code", ""))


def family_name(rule: dict[str, Any]) -> str:
    return str(rule.get("family") or rule.get("ontology", {}).get("family") or rule.get("family_code", ""))


def rule_link(rule: dict[str, Any]) -> str:
    return f"{rule.get('id', 'UNKNOWN')}.md"


def summary_text(rule: dict[str, Any]) -> str:
    for key in ("summary", "description", "rationale"):
        if rule.get(key):
            text = " ".join(str(rule[key]).split())
            return text[:220] + ("…" if len(text) > 220 else "")
    return "No summary provided."


def fmt_value(v: Any) -> str:
    if isinstance(v, bool):
        return "Yes" if v else "No"
    if isinstance(v, list):
        return ", ".join(f"`{x}`" for x in v) if v else "None listed"
    if isinstance(v, dict):
        return ", ".join(f"**{k}:** {fmt_value(val)}" for k, val in v.items()) if v else "None listed"
    return str(v)


def add_kv_section(lines: list[str], title: str, data: Any) -> None:
    if not data:
        return
    lines += [f"## {title}", ""]
    if isinstance(data, dict):
        for k, v in data.items():
            lines.append(f"- **{k}:** {fmt_value(v)}")
    elif isinstance(data, list):
        for item in data:
            lines.append(f"- {item}")
    else:
        lines.append(str(data))
    lines.append("")


def render_examples_block(items: list[Any], empty: str) -> list[str]:
    if not items:
        return [empty, ""]
    lines: list[str] = []
    for item in items:
        if isinstance(item, dict):
            lines += [f"### {item.get('title', 'Untitled example')}", "", str(item.get("description", "")).strip(), ""]
        else:
            lines += [f"- {item}", ""]
    return lines


def render_rule(rule: dict[str, Any], examples_dir: Path) -> str:
    rid = rule.get("id", "UNKNOWN")
    ontology = rule.get("ontology", {})
    cat = slug(rule.get("category_code", "unc"))
    fam = slug(rule.get("family_code", "gen"))
    lines = [
        f"# {rid}",
        "",
        f"**Name:** {rule_name(rule)}",
        "",
        f"**Category:** {category_name(rule)}",
        "",
        f"**Family:** {family_name(rule)}",
        "",
        f"**Primary layer:** `{rule.get('layer', 'unknown')}`",
        "",
        f"**System layers:** {fmt_value(ontology.get('system_layers', []))}",
        "",
        "## Description",
        "",
        rule.get("description") or rule.get("summary") or "No description provided.",
        "",
    ]
    add_kv_section(lines, "Impact", rule.get("impact"))
    add_kv_section(lines, "Detection", rule.get("detection"))
    add_kv_section(lines, "Remediation", rule.get("remediation"))
    add_kv_section(lines, "Cost Dimensions", rule.get("cost_dimensions"))
    add_kv_section(lines, "Amplification", rule.get("amplification"))
    add_kv_section(lines, "Temporal Behavior", rule.get("temporal_behavior"))
    add_kv_section(lines, "Runtime Evidence", rule.get("runtime_evidence"))
    if rule.get("sustainability_priority") is not None:
        lines += ["## Sustainability Priority", "", f"**Priority:** {rule.get('sustainability_priority')} / 5", ""]
    examples = rule.get("examples", {})
    if isinstance(examples, dict):
        lines += ["## Pattern examples", ""] + render_examples_block(examples.get("pattern", []), "No pattern examples provided.")
        lines += ["## Remediation examples", ""] + render_examples_block(examples.get("remediation", []), "No remediation examples provided.")
    if (examples_dir / f"{rid}.md").exists():
        lines += ["## Detailed example walkthrough", "", f"- [Open detailed example](examples/{rid}.md)", ""]
    add_kv_section(lines, "Metadata", rule.get("metadata"))
    lines += [
        "## Navigation",
        "",
        "- [Back to Human Catalog](index.md)",
        f"- [Back to {category_name(rule)} category](categories/{cat}/index.md)",
        f"- [Back to {family_name(rule)} family](categories/{cat}/families/{fam}/index.md)",
        "- [Back to Rule Browser](../rule-browser.md)",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def group(rules: list[dict[str, Any]], keyfn):
    d: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for r in rules:
        d[keyfn(r)].append(r)
    return {k: sorted(v, key=lambda r: r.get("id", "")) for k, v in d.items()}


def registry_categories(registry: dict[str, Any], rules_by_cat: dict[str, list[dict[str, Any]]]) -> list[tuple[str, str]]:
    cats = registry.get("categories", {}) if isinstance(registry, dict) else {}
    out: list[tuple[str, str]] = []
    if isinstance(cats, dict):
        for code, item in cats.items():
            if code in rules_by_cat:
                out.append((code, item.get("name", code)))
    for code in sorted(set(rules_by_cat) - {c for c, _ in out}):
        name = category_name(rules_by_cat[code][0]) if rules_by_cat[code] else code
        out.append((code, name))
    return out


def registry_families_for_category(registry: dict[str, Any], cat_code: str, rules_by_family: dict[str, list[dict[str, Any]]]) -> list[tuple[str, str]]:
    fams = registry.get("families", {}) if isinstance(registry, dict) else {}
    out: list[tuple[str, str]] = []
    if isinstance(fams, dict):
        for code, item in fams.items():
            if item.get("category_code") == cat_code and code in rules_by_family:
                out.append((code, item.get("name", code)))
    for code in sorted(set(rules_by_family) - {c for c, _ in out}):
        name = family_name(rules_by_family[code][0]) if rules_by_family[code] else code
        out.append((code, name))
    return out


def render_index(rules: list[dict[str, Any]], catalog: dict[str, Any], registry: dict[str, Any]) -> str:
    by_cat = group(rules, lambda r: str(r.get("category_code", "UNC")).upper())
    lines = [
        "# Eco Rules Catalog",
        "",
        f"**Catalog version:** {catalog.get('catalog_version', catalog.get('version', 'unknown'))}",
        "",
        f"**Total rules:** {len(rules)}",
        "",
        "## Categories",
        "",
    ]
    for code, name in registry_categories(registry, by_cat):
        lines.append(f"- [{name} ({code})](categories/{slug(code)}/index.md) ({len(by_cat.get(code, []))} rules)")
    lines += ["", "## All rules", ""]
    for r in rules:
        lines.append(f"- [{r.get('id', 'UNKNOWN')} — {rule_name(r)}]({rule_link(r)})")
    lines.append("")
    return "\n".join(lines)


def render_category_index(cat_code: str, cat_name: str, cat_rules: list[dict[str, Any]], registry: dict[str, Any]) -> str:
    by_family = group(cat_rules, lambda r: str(r.get("family_code", "GEN")).upper())
    lines = [
        f"# {cat_name} ({cat_code})",
        "",
        "- [Back to catalog index](../../index.md)",
        "",
        "## Families",
        "",
    ]
    for fam_code, fam_name in registry_families_for_category(registry, cat_code, by_family):
        count = len(by_family.get(fam_code, []))
        lines.append(f"- [{fam_name} ({fam_code})](families/{slug(fam_code)}/index.md) ({count} rules)")
    lines.append("")
    return "\n".join(lines)


def render_flat_category_index(cat_code: str, cat_name: str, cat_rules: list[dict[str, Any]], registry: dict[str, Any]) -> str:
    # Backward-compatible flat page for older links such as categories/cmp.md.
    nested = render_category_index(cat_code, cat_name, cat_rules, registry)
    return nested.replace("../../index.md", "../index.md").replace("families/", f"{slug(cat_code)}/families/")


def render_family_index(cat_code: str, cat_name: str, fam_code: str, fam_name: str, fam_rules: list[dict[str, Any]]) -> str:
    lines = [
        f"# {fam_name} ({fam_code})",
        "",
        f"- [Back to {cat_name} ({cat_code})](../../index.md)",
        "",
        f"**Total rules:** {len(fam_rules)}",
        "",
        "## Rules",
        "",
    ]
    for r in fam_rules:
        lines += [
            f"### [{r.get('id', 'UNKNOWN')} — {rule_name(r)}](../../../../{rule_link(r)})",
            "",
            summary_text(r),
            "",
            f"- Layer: **{r.get('layer', '')}**",
            "",
        ]
    return "\n".join(lines)


def render_layer_index(layer: str, layer_rules: list[dict[str, Any]]) -> str:
    lines = [
        f"# {layer.title()} rules",
        "",
        f"**Total rules:** {len(layer_rules)}",
        "",
        "- [Back to catalog index](../index.md)",
        "",
        "## Rules",
        "",
    ]
    for r in layer_rules:
        lines += [
            f"### [{r.get('id', 'UNKNOWN')} — {rule_name(r)}](../{rule_link(r)})",
            "",
            summary_text(r),
            "",
            f"- Category: **{category_name(r)}**",
            f"- Family: **{family_name(r)}**",
            "",
        ]
    return "\n".join(lines)


def render_examples_index(rules: list[dict[str, Any]], examples_dir: Path) -> str:
    lines = ["# Examples index", "", "Rules with detailed example walkthroughs.", ""]
    found = False
    for r in rules:
        rid = r.get("id", "UNKNOWN")
        if (examples_dir / f"{rid}.md").exists():
            found = True
            lines.append(f"- [{rid} — {rule_name(r)}]({rid}.md)")
    if not found:
        lines.append("No detailed examples are currently available.")
    lines.append("")
    return "\n".join(lines)


def copy_examples(rules: list[dict[str, Any]], out: Path, examples_dir: Path) -> None:
    for r in rules:
        rid = r.get("id", "UNKNOWN")
        src = examples_dir / f"{rid}.md"
        if src.exists():
            (out / "examples" / f"{rid}.md").write_text(src.read_text(encoding="utf-8"), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate human-readable Markdown catalog pages, category pages, and family pages.")
    ap.add_argument("--in", dest="in_path", default=str(DEFAULT_MASTER))
    ap.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    ap.add_argument("--out", dest="out_dir", default=str(DEFAULT_OUT_DIR))
    ap.add_argument("--examples-dir", default=str(DEFAULT_EXAMPLES_DIR))
    ap.add_argument("--clean", action="store_true", help="Remove generated output directory before regenerating")
    args = ap.parse_args()

    catalog = load_json(Path(args.in_path))
    registry = load_json(Path(args.registry)) if Path(args.registry).exists() else {}
    rules = get_rules(catalog)
    out = Path(args.out_dir)
    examples = Path(args.examples_dir)

    ensure_out(out, clean=args.clean)

    for r in rules:
        (out / rule_link(r)).write_text(render_rule(r, examples), encoding="utf-8")

    by_cat = group(rules, lambda r: str(r.get("category_code", "UNC")).upper())
    (out / "index.md").write_text(render_index(rules, catalog, registry), encoding="utf-8")

    for cat_code, cat_name in registry_categories(registry, by_cat):
        cat_rules = by_cat.get(cat_code, [])
        cat_dir = out / "categories" / slug(cat_code)
        cat_dir.mkdir(parents=True, exist_ok=True)
        (cat_dir / "index.md").write_text(render_category_index(cat_code, cat_name, cat_rules, registry), encoding="utf-8")
        # compatibility page for older category links
        (out / "categories" / f"{slug(cat_code)}.md").write_text(render_flat_category_index(cat_code, cat_name, cat_rules, registry), encoding="utf-8")

        by_family = group(cat_rules, lambda r: str(r.get("family_code", "GEN")).upper())
        for fam_code, fam_name in registry_families_for_category(registry, cat_code, by_family):
            fam_dir = cat_dir / "families" / slug(fam_code)
            fam_dir.mkdir(parents=True, exist_ok=True)
            (fam_dir / "index.md").write_text(
                render_family_index(cat_code, cat_name, fam_code, fam_name, by_family.get(fam_code, [])),
                encoding="utf-8",
            )

    for layer, rs in group(rules, lambda r: str(r.get("layer", "unknown")).lower()).items():
        (out / "layers" / f"{slug(layer)}.md").write_text(render_layer_index(layer, rs), encoding="utf-8")

    copy_examples(rules, out, examples)
    (out / "examples" / "index.md").write_text(render_examples_index(rules, examples), encoding="utf-8")

    print(f"Generated {len(rules)} rule pages in {out}")
    print(f"Generated {len(by_cat)} category page(s) and family indexes from registry data")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
