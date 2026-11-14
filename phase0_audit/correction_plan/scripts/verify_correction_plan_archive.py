#!/usr/bin/env python3
"""Read-only, standard-library verification of a correction-PLAN archive.
Never imports/executes scientific code, edits files, compiles TeX or uses the network.
"""
from pathlib import Path, PurePosixPath
import collections,csv,hashlib,io,json,posixpath,re,stat,sys,urllib.parse,zipfile

PREFIX='PHASE0_CORRECTION_PLAN'
STATUS='HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.'
REPORTS=[
 'AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md','MASTER_CORRECTION_REGISTER.md',
 'MATHEMATICAL_PROOF_REPAIR_PLAN.md','COMPUTATIONAL_REPAIR_PLAN.md',
 'LITERATURE_NOVELTY_REPAIR_PLAN.md','CORRECTION_DEPENDENCY_MAP.md','AUTHOR_APPROVAL_CHECKLIST.md']
AUDIT_REPORTS={
 'AUTHOR_DECISION_BRIEF.md','INDEPENDENT_PACKAGE_AUDIT.md','MATHEMATICAL_CLAIM_VERIFICATION.md',
 'PAIRING_AND_DUALITY_CRITICAL_AUDIT.md','GRAY_MAP_EVIDENCE_AUDIT.md',
 'LITERATURE_AND_NOVELTY_RECHECK.md','DISCREPANCY_AND_CORRECTION_REGISTER.md'}
CRITICAL={'CP10','CP23','CP24','CP25','CP27','CP29','CP32','CP40'}
CORE_SHA='b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24'
MAIN_SHA='8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0'

def require(ok,message):
 if not ok:raise ValueError(message)

def digest(b):return hashlib.sha256(b).hexdigest()

def local_links(name,text):
 # Literal code is provenance, not a clickable Markdown dependency.
 text=re.sub(r'^```.*?^```[^\n]*$', '',text,flags=re.M|re.S)
 for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]*?)\)',text):
  target=m.group(1).strip().strip('<>')
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
  p=urllib.parse.unquote(target.partition('#')[0])
  if not p:yield name;continue
  require(not p.startswith('/') and '\\' not in p,'Absolute/backslash Markdown target: '+target)
  dest=posixpath.normpath(posixpath.join(posixpath.dirname(name),p))
  require(dest!='..' and not dest.startswith('../'),'Escaping Markdown link: '+target)
  yield dest

def validate_payload(read,names):
 """Content checks shared by the repository sealer and portable verifier.
 read(relative_name)->bytes; names lists payload files (manifest may be present).
 """
 names=set(names)
 for n in REPORTS:
  require(n in names,'Missing requested document: '+n)
  require(STATUS in read(n).decode('utf8'),'Missing HOLD/nonauthorization status: '+n)
 require('README.md' in names,'Missing safe-verification navigation')
 a=json.loads(read('evidence/correction_actions.json'))
 ids={f'CP{i:02}' for i in range(1,44)};by={x['id']:x for x in a}
 require(len(a)==43 and set(by)==ids,'Action IDs are not exactly CP01–CP43')
 for x in a:
  require(x['audit_id']=='CR'+x['id'][2:],'Audit mapping mismatch: '+x['id'])
  require(x['group'] in 'ABCD' and len(x['group'])==1,'Invalid group: '+x['id'])
  require(x['severity'] in {'CRITICAL','MAJOR','MINOR'},'Invalid severity: '+x['id'])
  require(isinstance(x['depends_on'],list) and len(x['depends_on'])==len(set(x['depends_on'])),'Dependency list: '+x['id'])
  require(set(x['depends_on'])<=ids and x['id'] not in x['depends_on'],'Unknown/self dependency: '+x['id'])
  for k in ['title','manuscript_targets','related_claim','source_issue','audit_evidence','required_correction','new_proof_required','computational_verification','quantum_parameter_impact','baseline_disposition']:
   require(bool(x.get(k)),'Empty required register field '+k+' in '+x['id'])
 sev=dict(collections.Counter(x['severity'] for x in a))
 require(sev=={'CRITICAL':8,'MAJOR':29,'MINOR':6},'Severity count mismatch')
 require({x['id'] for x in a if x['severity']=='CRITICAL'}==CRITICAL,'Critical blocker set mismatch')
 order=[]
 while len(order)<43:
  ready=sorted(i for i in ids-set(order) if set(by[i]['depends_on'])<=set(order))
  require(bool(ready),'Dependency cycle');order.extend(ready)
 dep=json.loads(read('evidence/correction_dependency_map.json'))
 require(dep['status']==STATUS and dep['implementation_authorized'] is False,'Dependency authorization state')
 require(set(dep['critical_blockers'])==CRITICAL and dep['severity_counts']==sev,'Dependency count mismatch')
 require(len(dep['nodes'])==43 and {x['id'] for x in dep['nodes']}==ids,'Dependency node coverage')
 for x in dep['nodes']:
  require(all(x[k]==by[x['id']][k] for k in ['audit_id','group','severity','depends_on']),'Dependency node mismatch: '+x['id'])
 topo=dep['topological_order'];require(len(topo)==43 and set(topo)==ids,'Topological-order coverage')
 positions={v:i for i,v in enumerate(topo)}
 require(all(positions[d]<positions[x['id']] for x in a for d in x['depends_on']),'Invalid topological order')
 master=read('MASTER_CORRECTION_REGISTER.md').decode('utf8')
 heads=list(re.finditer(r'^### (CP\d{2}) — .+$',master,re.M))
 require(len(heads)==43 and {m.group(1) for m in heads}==ids,'Markdown action-card coverage')
 for i,m in enumerate(heads):
  text=master[m.end():heads[i+1].start() if i+1<len(heads) else len(master)]
  fields=re.findall(r'^\*\*(\d+)\. [^\n]+?\*\*',text,re.M)
  require(fields==[str(j) for j in range(1,12)],'Eleven explicit fields not found: '+m.group(1))
  require('**10. Severity:** '+by[m.group(1)]['severity']+'.' in text,'Card severity mismatch')
 rows=list(csv.DictReader(io.StringIO(read('evidence/master_correction_register.csv').decode('utf8'))))
 require(len(rows)==43 and {x['id'] for x in rows}==ids,'CSV action coverage')
 for x in rows:
  y=by[x['id']]
  for csvkey,key in [('audit_id','audit_id'),('title','title'),('group','group'),('severity','severity'),('related_theorem_equation_proof','related_claim'),('defect','source_issue'),('audit_evidence','audit_evidence'),('required_correction','required_correction'),('new_proof_required','new_proof_required'),('computational_verification','computational_verification'),('quantum_parameter_impact','quantum_parameter_impact'),('baseline_disposition','baseline_disposition')]:
   require(x[csvkey]==y[key],'CSV/JSON mismatch: '+x['id']+' / '+csvkey)
  require(x['dependencies']=='; '.join(y['depends_on']),'CSV dependency mismatch')
 audit=read('evidence/audit_reports/DISCREPANCY_AND_CORRECTION_REGISTER.md').decode('utf8')
 inherited=set(re.findall(r'^\| (CR\d+) BLOCKING \|',audit,re.M))
 require(inherited=={'CR'+x[2:] for x in CRITICAL},'Inherited blocking count mismatch')
 require(set(re.findall(r'^\| (CR\d+) (?:BLOCKING|HIGH|MEDIUM) \|',audit,re.M))=={'CR'+x[2:] for x in ids},'Inherited CR coverage mismatch')
 require(set(re.findall(r'^\| (A0[1-4]) \|',audit,re.M))=={'A01','A02','A03','A04'},'Audit self-disclosure coverage')
 prov=json.loads(read('evidence/copied_evidence_provenance.json'))
 require(len(prov)==42 and len({x['copy'] for x in prov})==42,'Source-copy provenance coverage')
 for x in prov:
  b=read(x['copy']);require(len(b)==x['bytes'] and digest(b)==x['sha256'],'Copied evidence differs: '+x['copy'])
 inputs=json.loads(read('evidence/audit_report_inputs.json'))
 require(len(inputs)==7 and {PurePosixPath(x['file']).name for x in inputs}==AUDIT_REPORTS,'Seven input-report coverage')
 for x in inputs:
  b=read('evidence/'+x['copied_verbatim_to']);require(len(b)==x['bytes'] and digest(b)==x['sha256'],'Input-report copy mismatch')
 core=read('evidence/MS03_source_manifest.sha256')
 require(digest(core)==CORE_SHA and len(core.splitlines())==14,'MS03 source manifest fingerprint')
 versions=list(csv.DictReader(io.StringIO(read('evidence/manuscript_versions.csv').decode('utf8'))))
 recovered=[x for x in versions if x['kind'].startswith('RECOVERED')]
 require(len(recovered)==19 and len(versions)==23,'Version inventory counts')
 require(len({x['source_payload_sha256'] for x in recovered})==9,'Distinct source payload count')
 ms=next(x for x in recovered if x['version_id']=='MS03')
 require(ms['main_sha256']==MAIN_SHA and ms['source_payload_sha256']==CORE_SHA and ms['core_files']=='14','MS03 inventory identity')
 historical=read('evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md').decode('utf8')
 require('new authoritative staging copy' in ' '.join(historical.split()),'Missing documentary staging authority')
 require('AUTHOR CONFIRMATION REQUIRED' in read('AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md').decode('utf8'),'Missing actual-submission qualification')
 snap=json.loads(read('evidence/pre_plan_snapshot.json'))
 require(len(snap['files'])==1959 and sum(x['bytes'] for x in snap['files'])==106136867,'Planning baseline count/bytes')
 preserved=json.loads(read('evidence/final_original_preservation.json'))
 require(preserved['all_original_files_unchanged'] is True and not preserved['changed_or_missing'] and not preserved['new_files_outside_correction_plan'],'Original preservation failure recorded')
 require(preserved['protected_original_count']==1959 and preserved['protected_original_bytes']==106136867,'Preservation counts')
 require(preserved['branch_before']==preserved['branch_after']==snap['branch'] and preserved['head_before']==preserved['head_after']==snap['head'],'Branch/HEAD preservation mismatch')
 comparisons=list(csv.DictReader(io.StringIO(read('evidence/final_original_file_comparison.csv').decode('utf8'))))
 require(len(comparisons)==1959 and {x['path'] for x in comparisons}=={x['path'] for x in snap['files']},'Original comparison coverage')
 baseline={x['path']:x for x in snap['files']}
 for x in comparisons:
  y=baseline[x['path']]
  require(x['status']=='UNCHANGED' and x['expected_sha256']==x['actual_sha256']==y['sha256'] and int(x['expected_bytes'])==int(x['actual_bytes'])==y['bytes'],'Original comparison mismatch: '+x['path'])
 validation=json.loads(read('evidence/final_plan_validation.json'))
 require(validation['status']==STATUS and validation['implementation_authorized'] is False and validation['scientific_executions_in_this_task']==0,'Final plan authorization/execution state')
 link_names=set(REPORTS+['README.md'])|{n for n in names if n.startswith('evidence/audit_reports/') and n.endswith('.md')}
 count=0
 for n in sorted(link_names):
  for target in local_links(n,read(n).decode('utf8')):
   require(target in names,'Missing local planning/report link: '+n+' -> '+target);count+=1
 return {'requested_documents':7,'actions':43,'explicit_fields_per_action':11,'severity_counts':sev,'critical_blockers':sorted(CRITICAL),'dependency_dag_acyclic':True,'verbatim_source_copies':42,'recovered_source_roots':19,'distinct_complete_core_payloads':9,'curated_mirror_roots':4,'ms03_source_manifest_sha256':CORE_SHA,'protected_original_count':1959,'protected_original_bytes':106136867,'local_planning_and_report_links_checked':count,'implementation_authorized':False,'scientific_scripts_executed':False}

def verify_archive(path):
 path=Path(path)
 with zipfile.ZipFile(path) as z:
  info=z.infolist();names=[x.filename for x in info]
  require(len(names)==len(set(names)),'Duplicate archive paths')
  require(len(names)<=10000 and sum(x.file_size for x in info)<=128*1024*1024,'Unexpectedly large plan archive')
  for x in info:
   p=PurePosixPath(x.filename)
   require(not x.is_dir() and not p.is_absolute() and '\\' not in x.filename and '..' not in p.parts and p.parts[0]==PREFIX and len(p.parts)>1,'Unsafe archive path: '+x.filename)
   require(not stat.S_ISLNK(x.external_attr>>16),'Archive symlink: '+x.filename)
   require(not(x.flag_bits&1),'Encrypted entry')
  require(z.testzip() is None,'ZIP CRC failure')
  relative={n.removeprefix(PREFIX+'/'):n for n in names}
  require('SHA256SUMS.txt' in relative,'Missing internal manifest')
  read=lambda n:z.read(relative[n])
  entries={}
  for line in read('SHA256SUMS.txt').decode('utf8').splitlines():
   m=re.fullmatch(r'([0-9a-f]{64})  (.+)',line);require(m is not None,'Malformed manifest line')
   h,n=m.groups();require(n not in entries,'Duplicate manifest item');entries[n]=h
  require(set(entries)==set(relative)-{'SHA256SUMS.txt'},'Manifest coverage mismatch')
  for n,h in entries.items():require(digest(read(n))==h,'Payload checksum failure: '+n)
  checked=validate_payload(read,set(relative))
 sidecar=Path(str(path)+'.sha256');sidecar_state='not supplied'
 if sidecar.is_file():
  m=re.fullmatch(r'([0-9a-f]{64})  (.+)\n?',sidecar.read_text())
  require(m is not None and m.group(2)==path.name and m.group(1)==digest(path.read_bytes()),'External sidecar mismatch')
  sidecar_state='PASS'
 checked.update({'zip_crc':'PASS','archive_entries':len(names),'manifest_hashes':len(entries),'external_sidecar':sidecar_state,'status':STATUS})
 return checked

def main():
 if len(sys.argv)!=2:raise SystemExit('Usage: python3 -B verify_correction_plan_archive.py /path/to/PHASE0_CORRECTION_PLAN.zip')
 try:checked=verify_archive(sys.argv[1])
 except (ValueError,KeyError,AssertionError,StopIteration,OSError,zipfile.BadZipFile,json.JSONDecodeError) as e:
  print('FAIL:',e,file=sys.stderr);raise SystemExit(1)
 print('PASS — correction-plan archive integrity and planning-structure checks; no research executed.')
 print(json.dumps(checked,indent=2,ensure_ascii=False))
 print('Integrity PASS is not mathematical GO. '+STATUS)

if __name__=='__main__':main()
