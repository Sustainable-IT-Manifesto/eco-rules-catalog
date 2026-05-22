#!/usr/bin/env python3
import argparse, json, os, subprocess, sys
from datetime import datetime, timezone


def run(cmd, label):
    print('\n==> {}'.format(label)); print('    {}'.format(' '.join(cmd)))
    result = subprocess.run(cmd, timeout=120)
    if result.returncode != 0: print('\nERROR: step failed: {}'.format(label))
    return result.returncode

def ensure_parent_dir(path):
    if path:
        parent=os.path.dirname(os.path.abspath(path))
        if parent and not os.path.isdir(parent): os.makedirs(parent)

def write_report(path, report):
    ensure_parent_dir(path)
    with open(path,'w',encoding='utf-8') as f: json.dump(report,f,ensure_ascii=False,indent=2,sort_keys=True)

def main():
    ap=argparse.ArgumentParser(description='Publish/validate Eco Rules catalog using the v0.4.0 toolchain.')
    ap.add_argument('--root', default='.')
    ap.add_argument('--catalog', default='master.json')
    ap.add_argument('--registry', default='registry.json')
    ap.add_argument('--schema', default='schema/schema-rule.json')
    ap.add_argument('--human-out', default='docs/catalog')
    ap.add_argument('--examples-dir', default='examples')
    ap.add_argument('--build', action='store_true', help='Build master catalog from rules first')
    ap.add_argument('--skip-normalize', action='store_true')
    ap.add_argument('--skip-validate', action='store_true')
    ap.add_argument('--validate-ontology', action='store_true', help='Also run the noisier ontology completeness validator')
    ap.add_argument('--skip-human', action='store_true')
    ap.add_argument('--report-out', default=None)
    ap.add_argument('--python', default=sys.executable)
    args=ap.parse_args()
    py=args.python; root=args.root
    def p(path): return os.path.join(root,path) if not os.path.isabs(path) else path
    report={'generated_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'catalog':args.catalog,'registry':args.registry,'schema':args.schema,'steps':[],'success':False}
    if args.build:
        rc=run([py,p('tools/build_catalog.py'),'--root',root,'--out',args.catalog], 'Build master catalog')
        report['steps'].append({'name':'build_catalog','returncode':rc})
        if rc: write_report(args.report_out,report) if args.report_out else None; return rc
    if not args.skip_normalize:
        rc=run([py,p('tools/normalize_ontology.py'),'--in',p(args.catalog),'--check'], 'Check ontology normalization')
        report['steps'].append({'name':'normalize_ontology_check','returncode':rc})
        if rc: write_report(args.report_out,report) if args.report_out else None; return rc
    if not args.skip_validate:
        for name, cmd in [
            ('validate_registry',[py,p('tools/validate_registry.py'),'--registry',p(args.registry),'--schema',p('schema/schema-registry.json')]),
            ('validate_rules_v2',[py,p('tools/validate_rules_v2.py'),p(args.catalog),'--registry',p(args.registry),'--schema',p(args.schema)])
        ]:
            rc=run(cmd, name.replace('_',' ').title()); report['steps'].append({'name':name,'returncode':rc})
            if rc: write_report(args.report_out,report) if args.report_out else None; return rc
        if args.validate_ontology:
            name='validate_ontology'; cmd=[py,p('tools/validate_ontology.py'),'--in',p(args.catalog),'--registry',p(args.registry),'--require-ontology']
            rc=run(cmd, name.replace('_',' ').title()); report['steps'].append({'name':name,'returncode':rc})
            if rc: write_report(args.report_out,report) if args.report_out else None; return rc
    if not args.skip_human:
        rc=run([py,p('tools/generate_human_catalog_v2.py'),'--in',p(args.catalog),'--out',p(args.human_out),'--examples-dir',p(args.examples_dir)], 'Generate human-readable catalog')
        report['steps'].append({'name':'generate_human_catalog_v2','returncode':rc})
        if rc: write_report(args.report_out,report) if args.report_out else None; return rc
    report['success']=True; print('\nPublish pipeline completed successfully.')
    if args.report_out: write_report(args.report_out, report)
    return 0
if __name__ == '__main__': raise SystemExit(main())
