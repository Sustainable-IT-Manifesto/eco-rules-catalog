#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from collections import defaultdict
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MASTER = ROOT / 'master.json'
DEFAULT_OUT_DIR = ROOT / 'docs' / 'catalog'
DEFAULT_EXAMPLES_DIR = ROOT / 'examples'


def load_json(path: Path) -> Any:
    with path.open('r', encoding='utf-8') as f: return json.load(f)

def get_rules(catalog: dict) -> list[dict]:
    return sorted(catalog.get('rules', []), key=lambda r: r.get('id',''))

def ensure_out(out: Path):
    for sub in ['', 'layers', 'categories', 'examples']:
        (out / sub).mkdir(parents=True, exist_ok=True)

def rule_name(rule): return rule.get('name') or rule.get('title') or rule.get('id','UNKNOWN')
def category_name(rule): return str(rule.get('category') or rule.get('ontology',{}).get('category') or rule.get('category_code',''))
def family_name(rule): return str(rule.get('family') or rule.get('ontology',{}).get('family') or rule.get('family_code',''))
def rule_link(rule): return f"{rule.get('id','UNKNOWN')}.md"

def summary_text(rule):
    for key in ('summary','description','rationale'):
        if rule.get(key):
            text=' '.join(str(rule[key]).split())
            return text[:220] + ('…' if len(text)>220 else '')
    return 'No summary provided.'

def fmt_value(v):
    if isinstance(v, bool): return 'Yes' if v else 'No'
    if isinstance(v, list): return ', '.join(f'`{x}`' for x in v) if v else 'None listed'
    if isinstance(v, dict): return ', '.join(f'**{k}:** {fmt_value(val)}' for k,val in v.items()) if v else 'None listed'
    return str(v)

def add_kv_section(lines, title, data):
    if not data: return
    lines += [f'## {title}', '']
    if isinstance(data, dict):
        for k, v in data.items(): lines.append(f'- **{k}:** {fmt_value(v)}')
    elif isinstance(data, list):
        for item in data: lines.append(f'- {item}')
    else:
        lines.append(str(data))
    lines.append('')

def render_examples_block(items, empty):
    if not items: return [empty, '']
    lines=[]
    for item in items:
        if isinstance(item, dict):
            lines += [f"### {item.get('title','Untitled example')}", '', str(item.get('description','')).strip(), '']
        else: lines += [f'- {item}', '']
    return lines

def render_rule(rule, out_dir: Path, examples_dir: Path) -> str:
    rid=rule.get('id','UNKNOWN'); ontology=rule.get('ontology',{})
    lines=[f'# {rid}','',f'**Name:** {rule_name(rule)}','',f'**Category:** {category_name(rule)}','',f'**Family:** {family_name(rule)}','',f"**Primary layer:** `{rule.get('layer','unknown')}`",'',f"**System layers:** {fmt_value(ontology.get('system_layers', []))}",'','## Description','',rule.get('description') or rule.get('summary') or 'No description provided.','']
    add_kv_section(lines, 'Impact', rule.get('impact'))
    add_kv_section(lines, 'Detection', rule.get('detection'))
    add_kv_section(lines, 'Remediation', rule.get('remediation'))
    add_kv_section(lines, 'Cost Dimensions', rule.get('cost_dimensions'))
    add_kv_section(lines, 'Amplification', rule.get('amplification'))
    add_kv_section(lines, 'Temporal Behavior', rule.get('temporal_behavior'))
    add_kv_section(lines, 'Runtime Evidence', rule.get('runtime_evidence'))
    if rule.get('sustainability_priority') is not None:
        lines += ['## Sustainability Priority','',f"**Priority:** {rule.get('sustainability_priority')} / 5",'']
    examples=rule.get('examples',{})
    if isinstance(examples, dict):
        lines += ['## Pattern examples',''] + render_examples_block(examples.get('pattern',[]), 'No pattern examples provided.')
        lines += ['## Remediation examples',''] + render_examples_block(examples.get('remediation',[]), 'No remediation examples provided.')
    if (examples_dir / f'{rid}.md').exists():
        lines += ['## Detailed example walkthrough','',f'- [Open detailed example](examples/{rid}.md)','']
    add_kv_section(lines, 'Metadata', rule.get('metadata'))
    lines += ['## Navigation','','- [Back to Human Catalog](index.md)','- [Back to Rule Browser](../rule-browser.md)','']
    return '\n'.join(lines).rstrip()+'\n'

def copy_examples(rules, out, examples_dir):
    for r in rules:
        rid=r.get('id','UNKNOWN'); src=examples_dir / f'{rid}.md'
        if src.exists(): (out/'examples'/f'{rid}.md').write_text(src.read_text(encoding='utf-8'), encoding='utf-8')

def render_index(rules, catalog):
    lines=['# Eco Rules Catalog (Human Readable)','',f"**Catalog version:** {catalog.get('catalog_version', catalog.get('version','unknown'))}",'',f'**Total rules:** {len(rules)}','','## Browse','','- [Rule Browser](../rule-browser.md)','- [Examples index](examples/index.md)','- [Layers](#layers)','- [Categories](#categories)','','## Rules','']
    for r in rules: lines.append(f"- [{r.get('id','UNKNOWN')} — {rule_name(r)}]({rule_link(r)})")
    lines.append('')
    return '\n'.join(lines)

def group(rules, keyfn):
    d=defaultdict(list)
    for r in rules: d[keyfn(r)].append(r)
    return {k:sorted(v,key=lambda r:r.get('id','')) for k,v in d.items()}

def render_group(title, code, rules, back='../index.md'):
    lines=[f'# {title} rules','',f'**Code:** `{code}`','',f'**Total rules:** {len(rules)}','',f'- [Back to Human Catalog]({back})','']
    if not rules: return '\n'.join(lines+['No rules are currently listed.',''])
    lines += ['## Rules','']
    for r in rules:
        lines += [f"### [{r.get('id','UNKNOWN')} — {rule_name(r)}](../{rule_link(r)})",'',summary_text(r),'',f"- Category: **{category_name(r)}**",f"- Family: **{family_name(r)}**",f"- Layer: **{r.get('layer','')}**",'']
    return '\n'.join(lines)

def render_examples_index(rules, examples_dir):
    lines=['# Examples index','','Rules with detailed example walkthroughs.','']; found=False
    for r in rules:
        rid=r.get('id','UNKNOWN')
        if (examples_dir/f'{rid}.md').exists():
            found=True; lines.append(f'- [{rid} — {rule_name(r)}]({rid}.md)')
    if not found: lines.append('No detailed examples are currently available.')
    lines.append(''); return '\n'.join(lines)

def main():
    ap=argparse.ArgumentParser(description='Generate human-readable Markdown catalog pages with v0.4.0 metadata sections.')
    ap.add_argument('--in', dest='in_path', default=str(DEFAULT_MASTER))
    ap.add_argument('--out', dest='out_dir', default=str(DEFAULT_OUT_DIR))
    ap.add_argument('--examples-dir', default=str(DEFAULT_EXAMPLES_DIR))
    args=ap.parse_args()
    catalog=load_json(Path(args.in_path)); rules=get_rules(catalog); out=Path(args.out_dir); examples=Path(args.examples_dir)
    ensure_out(out)
    for r in rules: (out/rule_link(r)).write_text(render_rule(r,out,examples), encoding='utf-8')
    (out/'index.md').write_text(render_index(rules,catalog), encoding='utf-8')
    for layer, rs in group(rules, lambda r: str(r.get('layer','unknown')).lower()).items():
        (out/'layers'/f'{layer}.md').write_text(render_group(layer.title(), layer, rs), encoding='utf-8')
    for cat, rs in group(rules, lambda r: str(r.get('category_code','unc')).lower()).items():
        (out/'categories'/f'{cat}.md').write_text(render_group(category_name(rs[0]) if rs else cat.upper(), cat.upper(), rs), encoding='utf-8')
    copy_examples(rules,out,examples)
    (out/'examples'/'index.md').write_text(render_examples_index(rules,examples), encoding='utf-8')
    print(f'Generated {len(rules)} rule pages in {out}')
    return 0
if __name__ == '__main__': raise SystemExit(main())
