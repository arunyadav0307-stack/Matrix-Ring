#!/usr/bin/env python3
"""Read-only independent package inventory and explicit cross-reference audit.
See the reports for human semantic checks; this script does not prove mathematics.
"""
from pathlib import Path,PurePosixPath
import ast
import collections
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
import urllib.parse
import zipfile

BASE=Path(__file__).resolve().parents[1]
REPO=BASE.parents[1]
ZIP=REPO/'phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE.zip'
if not ZIP.exists():ZIP=BASE/'evidence/input/PHASE0_COMPLETE_AUDIT_PACKAGE.zip'
ROOT=BASE/'work/PHASE0_COMPLETE_AUDIT_PACKAGE'
OUT=BASE/'evidence/package_checks_v2'
OUT.mkdir(exist_ok=False)
errors=[]
H=lambda b:hashlib.sha256(b).hexdigest()
EXPECTED='350e5b9e4796d6b7798c17ce8ef047ee032e50cc4e49df0ef6e8d28ea5538c4e'
REPORTS=['PHASE0_REPOSITORY_AUDIT.md','PHASE0_LITERATURE_REVIEW.md','PHASE0_RING_FEASIBILITY.md','PHASE0_PAIRING_OPTIONS.md','PHASE0_RESEARCH_GAP.md','PHASE0_DECISION_REPORT.md']

def csvout(name,rows):
    if not rows:return
    with (OUT/name).open('x',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def check(ok,reason):
    if not ok:errors.append(reason)

inventory=[]
with zipfile.ZipFile(ZIP) as z:
    infos=[x for x in z.infolist() if not x.is_dir()];names=[x.filename for x in infos]
    check(z.testzip() is None,'ZIP CRC failure')
    check(len(names)==len(set(names)),'Duplicate members')
    check(all(not PurePosixPath(n).is_absolute() and '..' not in PurePosixPath(n).parts and PurePosixPath(n).parts[0]=='PHASE0_COMPLETE_AUDIT_PACKAGE' for n in names),'Unsafe member paths')
    check(H(ZIP.read_bytes())==EXPECTED,'ZIP identity differs from sealed input')
    for i in infos:
        rel=PurePosixPath(i.filename).relative_to('PHASE0_COMPLETE_AUDIT_PACKAGE').as_posix()
        b=z.read(i.filename);p=ROOT/rel
        check(p.is_file() and p.read_bytes()==b,'Fresh extraction mismatch: '+rel)
        inventory.append({'path':rel,'bytes':len(b),'sha256':H(b),'text_utf8':rel[-4:]!='.pdf'})
    internal_manifest={}
    for line in z.read('PHASE0_COMPLETE_AUDIT_PACKAGE/SHA256SUMS.txt').decode().splitlines():
        digest,name=line.split('  ',1)
        check(name not in internal_manifest,'Duplicate manifest name: '+name)
        internal_manifest[name]=digest
        check(H(z.read('PHASE0_COMPLETE_AUDIT_PACKAGE/'+name))==digest,'Internal manifest mismatch: '+name)
    check(set(x['path'] for x in inventory)==set(internal_manifest)|{'SHA256SUMS.txt'},'Internal manifest coverage')
csvout('independent_original_archive_inventory.csv',inventory)

readability=[]
for name in REPORTS:
    b=(ROOT/'reports'/name).read_bytes();text=b.decode('utf8',errors='strict')
    original=REPO/'phase0_audit'/name
    same=(original.read_bytes()==b) if original.exists() else None
    check('\ufffd' not in text and text.startswith('#'),'Unreadable mandatory report: '+name)
    check(same is not False,'Frozen report copy mismatch: '+name)
    readability.append({'report':name,'bytes':len(b),'lines':len(text.splitlines()),'UTF8_readable':True,'sha256':H(b),'same_as_original':same})
csvout('six_report_readability.csv',readability)

provenance=list(csv.DictReader((ROOT/'repository_integrity/source_provenance.csv').open()))
for row in provenance:
    p=ROOT/row['package_path']
    check(p.is_file() and p.stat().st_size==int(row['bytes']) and H(p.read_bytes())==row['sha256'],'Provenance mismatch: '+row['package_path'])

# Both inherited manifests are independently resolved from their documented mappings.
mappings=list(csv.DictReader((ROOT/'repository_integrity/inherited_manifest_verification.csv').open()))
for row in mappings:
    p=ROOT/row['package_path']
    check(p.is_file() and H(p.read_bytes())==row['expected_sha256'],'Inherited manifest mapping failure: '+row['original_manifest_path'])
data=ROOT/'computational_evidence/research-data'
all_data=[p for p in data.rglob('*') if p.is_file()]
publines=(data/'PUBLICATION_MANIFEST.sha256').read_text().splitlines()
public=[]
for line in publines:
    digest,name=line.split('  ',1);public.append(name)
    check((data/name).is_file() and H((data/name).read_bytes())==digest,'Publication manifest failure: '+name)
check(set(public)=={p.relative_to(data).as_posix() for p in all_data if p.name!='PUBLICATION_MANIFEST.sha256'},'Publication manifest coverage')

# Check every declared resolution, and also whether its referring line still carries the literal.
refs=list(csv.DictReader((ROOT/'repository_integrity/reference_resolution.csv').open()))
ref_results=[];line_exceptions=[]
for row in refs:
    p=ROOT/row['referring_package_file'];lines=p.read_text().splitlines();n=int(row['line'])
    exists=p.is_file() and 0<n<=len(lines)
    check(exists,'Bad reference source/line: '+str(row))
    literal=row['literal_reference'];line=lines[n-1] if exists else ''
    literal_visible=literal in line
    # A shorthand expanded by the historical builder can legitimately differ.
    if not literal_visible:line_exceptions.append({'file':row['referring_package_file'],'line':n,'literal':literal,'source_line':line})
    targets=json.loads(row['package_targets_json'])
    all_exist=all((ROOT/t).is_file() for t in targets)
    check(all_exist,'Absent reference target: '+str(row))
    ref_results.append({'file':row['referring_package_file'],'line':n,'literal':literal,'recorded_status':row['status'],'targets':json.dumps(targets),'all_targets_exist':all_exist,'literal_at_recorded_line':literal_visible,'scope':'Existence; not approval of omitted/unavailable targets or scientific content'})
csvout('independent_reference_resolution_check.csv',ref_results)
csvout('reference_literal_line_exceptions.csv',line_exceptions)

# Scan actual Markdown link destinations in EVERY packaged Markdown source.
links=[]
for p in sorted(ROOT.rglob('*.md')):
    s=p.read_text()
    for mat in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]*?)\)',s):
        target=mat.group(1).strip().strip('<>');line=s[:mat.start()].count('\n')+1
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):state='EXTERNAL_NOT_FETCHED'
        else:
            path,_,frag=target.partition('#');path=urllib.parse.unquote(path)
            dest=p.parent/path if path else p
            if dest.exists():state='EXISTS_ANCHOR_REQUIRES_SEMANTIC_CHECK' if frag else 'EXISTS'
            else:state='NOT_DIRECTLY_RESOLVED_IN_RELOCATED_PACKAGE'
        links.append({'file':p.relative_to(ROOT).as_posix(),'line':line,'target':target,'status':state})
csvout('all_markdown_links.csv',links)

# Local Python imports for all 22 research programs; stdlib / third-party names distinguished.
scripts=sorted((data/'scripts').glob('*.py'));local={p.stem for p in scripts};imports=[]
for p in scripts:
    tree=ast.parse(p.read_text(),filename=str(p))
    for n in ast.walk(tree):
        modules=[n.module] if isinstance(n,ast.ImportFrom) and n.module else [a.name for a in n.names] if isinstance(n,ast.Import) else []
        for module in modules:
            short=module.split('.')[0]
            status='LOCAL_PRESENT' if short in local else 'STANDARD_LIBRARY' if short in sys.stdlib_module_names else 'EXTERNAL_OR_DYNAMIC_REQUIRES_REVIEW'
            imports.append({'file':p.name,'line':n.lineno,'import':module,'status':status})
            if status=='LOCAL_PRESENT':check((data/'scripts'/(short+'.py')).is_file(),'Local import absent: '+short)
csvout('independent_python_imports.csv',imports)

# Full manuscript include, label, ref and citation pass for both source variants.
inputs=list(csv.DictReader((ROOT/'repository_integrity/manuscript_input_resolution.csv').open()))
latex=[];latex_summary=[]
for main in sorted({r['main_source'] for r in inputs}):
    variant='FFA_FINAL_SUBMISSION_V2' if 'FFA_FINAL_SUBMISSION_V2' in main else 'canonical'
    relevant=[r for r in inputs if r['main_source']==main]
    mainpath=ROOT/'repository_integrity/prior_work/PAPER'/('FFA_FINAL_SUBMISSION_V2/main.tex' if variant!='canonical' else 'main.tex')
    texpaths=[mainpath]+[ROOT/r['package_path'] for r in relevant if r['package_path'].endswith('.tex')]
    bibpaths=[ROOT/r['package_path'] for r in relevant if r['package_path'].endswith('.bib')]
    labels=collections.Counter();references=[];cites=[]
    for r in relevant:
        dest=ROOT/r['package_path'];check(dest.is_file(),'Manuscript input absent '+r['package_path'])
        # This distinguishes source-reuse mappings from out-of-the-box build paths.
        natural=mainpath.parent/r['input']
        direct=natural.exists() or natural.with_suffix('.tex').exists() or natural.with_suffix('.bib').exists()
        latex.append({'variant':variant,'kind':'input','file':mainpath.relative_to(ROOT).as_posix(),'line':'','key':r['input'],'status':'DIRECT_PATH_PRESENT' if direct else 'RESOLVED_BY_DOCUMENTED_SOURCE_REUSE','target':r['package_path']})
    for p in texpaths:
        s=re.sub(r'(?<!\\)%[^\n]*','',p.read_text())
        labels.update(re.findall(r'\\label\{([^}]+)\}',s))
        for mat in re.finditer(r'\\(?:[cC]ref|[eE]qref|[rR]ef|pageref|autoref)\*?\{([^}]+)\}',s):
            for k in mat.group(1).split(','):references.append((p,s[:mat.start()].count('\n')+1,k.strip()))
        for mat in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^}]+)\}',s):
            for k in mat.group(1).split(','):cites.append((p,s[:mat.start()].count('\n')+1,k.strip()))
    bibkeys=set()
    for p in bibpaths:bibkeys.update(re.findall(r'@\w+\s*\{\s*([^,\s]+)',p.read_text()))
    for kind,items,universe in [('label_ref',references,labels),('citation',cites,bibkeys)]:
        for p,n,k in items:
            state='RESOLVED' if k in universe else 'UNRESOLVED'
            latex.append({'variant':variant,'kind':kind,'file':p.relative_to(ROOT).as_posix(),'line':n,'key':k,'status':state,'target':''})
    latex_summary.append({'variant':variant,'input_rows':len(relevant),'labels':len(labels),'duplicate_labels':[k for k,v in labels.items() if v>1],'reference_occurrences':len(references),'undefined_references':sorted(set(k for _,_,k in references if k not in labels)),'citation_occurrences':len(cites),'undefined_citations':sorted(set(k for _,_,k in cites if k not in bibkeys)),'bibliography_entries':len(bibkeys),'nonliteral_relocated_inputs':sum(r['variant']==variant and r['kind']=='input' and r['status']=='RESOLVED_BY_DOCUMENTED_SOURCE_REUSE' for r in latex)})
csvout('independent_latex_cross_references.csv',latex)

# Every explicit T-ID and range cited in the six reports is traced to packaged mathematical text.
proofs=list((ROOT/'mathematical_evidence/prior_project/03_THEOREMS').glob('*.md'))
idrefs=[]
for name in REPORTS:
    text=(ROOT/'reports'/name).read_text()
    ids=set(re.findall(r'\bT-\d{3}\b',text))
    for a,b in re.findall(r'T-(\d{3})\s*(?:…|–|\.\.\.)\s*(?:T-)?(\d{3})',text):ids.update('T-%03d'%i for i in range(int(a),int(b)+1))
    for k in sorted(ids):
        targets=[p.relative_to(ROOT).as_posix() for p in proofs if k in p.read_text()]
        idrefs.append({'report':name,'theorem_id':k,'present_in_packaged_mathematics':bool(targets),'targets':json.dumps(targets),'scope':'Identifier existence only; proof applicability/staleness audited in reports'})
        check(bool(targets),'Missing cited theorem ID: '+k)
csvout('six_report_theorem_id_resolution.csv',idrefs)

# BibTeX entries: presence and historical qualifiers, not fabricated publisher validation.
bibs=[]
for p in sorted(ROOT.rglob('*.bib')):
    s=p.read_text();starts=list(re.finditer(r'@\w+\s*\{\s*([^,\s]+)',s))
    for i,mat in enumerate(starts):
        block=s[mat.start(): starts[i+1].start() if i+1<len(starts) else len(s)]
        dois=re.findall(r'\bdoi\s*=\s*\{([^}]+)\}',block,re.I)
        bibs.append({'file':p.relative_to(ROOT).as_posix(),'key':mat.group(1),'doi_field':'; '.join(dois),'has_TO_CONFIRM':bool(re.search(r'TO CONFIRM|NOT VERIFIED|not confirmed|not retrieved',block,re.I)),'has_SECONDARY': 'SECONDARY' in block,'has_DIRECT':bool(re.search(r'\bDIRECT\b',block)),'fresh_external_reverification':'NOT_INFERRED_FROM_HISTORICAL_TAG'})
csvout('independent_bibliography_inventory.csv',bibs)

result={'zip_file':str(ZIP),'zip_sha256':H(ZIP.read_bytes()),'zip_bytes':ZIP.stat().st_size,'regular_files':len(inventory),'uncompressed_bytes':sum(r['bytes'] for r in inventory),'internal_manifest_entries':len(internal_manifest),'six_reports':readability,'research_data_files':len(all_data),'research_data_bytes':sum(p.stat().st_size for p in all_data),'non_manifest_data_files':sum(p.suffix!='.sha256' for p in all_data),'data_extension_counts':dict(collections.Counter(p.suffix for p in all_data)),'publication_manifest_entries':len(public),'legacy_manifest_rows_verified':sum(r['source_manifest']!='PUBLICATION_MANIFEST.sha256' for r in mappings),'provenance_rows':len(list(csv.DictReader((ROOT/'repository_integrity/source_provenance.csv').open()))),'reference_occurrences':len(refs),'reference_targets':sum(len(json.loads(r['package_targets_json'])) for r in refs),'reference_statuses':dict(collections.Counter(r['status'] for r in refs)),'mandatory_report_reference_statuses':dict(collections.Counter(r['status'] for r in refs if r['referring_package_file'].startswith('reports/'))),'literal_line_exceptions':len(line_exceptions),'markdown_link_occurrences':len(links),'markdown_link_statuses':dict(collections.Counter(r['status'] for r in links)),'research_scripts_parsed':len(scripts),'local_python_import_edges':sum(r['status']=='LOCAL_PRESENT' for r in imports),'nonstdlib_nonlocal_imports':[r for r in imports if r['status']=='EXTERNAL_OR_DYNAMIC_REQUIRES_REVIEW'],'latex':latex_summary,'theorem_id_report_pairs':len(idrefs),'errors':errors,'integrity_status':'PASS' if not errors else 'FAIL','reference_closure_status':'QUALIFIED_NOT_UNIVERSALLY_COMPLETE','scope':'Existence/integrity/syntactic reference checks only. Missing historical documents and semantic cross-reference errors remain explicitly qualified.'}
with (OUT/'independent_package_checks.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
if errors:sys.exit(1)
