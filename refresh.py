#!/usr/bin/env python3
"""Refresh evidence without automatic payments or overwriting failed results."""
import argparse,json,shutil,urllib.request,urllib.error
from pathlib import Path
from build_table import build,validate,DOMAINS
ROOT=Path(__file__).parent
def store(row):
 validate(row);p=ROOT/'data'/f"{row['domain']}.json";p.parent.mkdir(exist_ok=True);tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(row,indent=2,ensure_ascii=False)+'\n',encoding='utf-8');tmp.replace(p)
def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('domains',nargs='*');parser.add_argument('--render-only',action='store_true');parser.add_argument('--import-dir',type=Path);args=parser.parse_args()
 if set(args.domains)-set(DOMAINS):parser.error('Unknown company domain; see DOMAINS in build_table.py')
 if args.import_dir:
  for p in sorted(args.import_dir.glob('*.json')):
   try:store(json.loads(p.read_text(encoding='utf-8')));print('Imported',p.name)
   except (ValueError,KeyError) as e:print('Preserved existing snapshot:',p.name,str(e))
 elif not args.render_only:
  for domain in args.domains or DOMAINS:
   req=urllib.request.Request('https://gethirepulse.xyz/v1/company-profile',data=json.dumps({'domain':domain}).encode(),headers={'Content-Type':'application/json','User-Agent':'HirePulse-Radar/1.0'})
   try:
    with urllib.request.urlopen(req,timeout=35) as r:row=json.load(r)
    if row.get('domain')!=domain:raise ValueError('Response domain mismatch')
    store(row);print('Updated',domain)
   except (urllib.error.URLError,ValueError,KeyError) as e:print('Preserved existing snapshot:',domain,type(e).__name__)
 print('Rendered',build(ROOT),'companies from saved evidence.')
if __name__=='__main__':main()
