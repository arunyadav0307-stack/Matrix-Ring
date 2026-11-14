#!/usr/bin/env python3
"""Repository-specific seal of a planning-only delivery.
Read/hash pre-existing files; write exclusively beneath correction_plan.
No scientific imports/execution, original-file edits, TeX, network or Git writes.
"""
from pathlib import Path
from datetime import datetime,timezone
import ast,collections,csv,hashlib,importlib.util,io,json,re,subprocess,sys,zipfile

B=Path(__file__).resolve().parents[1]; E=B/'evidence'; REPO=B.parents[1]
PREFIX='PHASE0_CORRECTION_PLAN';STATUS='HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.'
Z=B/(PREFIX+'.zip');SIDE=B/(PREFIX+'.zip.sha256');VERIFICATION=B/(PREFIX+'_VERIFICATION.txt')
PRES='evidence/final_original_preservation.json';COMP='evidence/final_original_file_comparison.csv';VALID='evidence/final_plan_validation.json'
reserved=[B/PRES,B/COMP,B/VALID,B/'SHA256SUMS.txt',Z,SIDE,VERIFICATION]
assert B==REPO/'phase0_audit/correction_plan'
assert all(not p.exists() for p in reserved),'Final seal outputs already exist; do not rerun into a sealed delivery.'
clock=datetime.now(timezone.utc);iso=clock.isoformat()
def sha(b):return hashlib.sha256(b).hexdigest()
def jbytes(v):return (json.dumps(v,indent=2,ensure_ascii=False)+'\n').encode('utf8')
def git(*args):return subprocess.check_output(['git',*args],cwd=REPO,text=True).strip()

snap=json.loads((E/'pre_plan_snapshot.json').read_text())
assert len(snap['files'])==1959 and sum(x['bytes'] for x in snap['files'])==106136867
branch=git('branch','--show-current');head=git('rev-parse','HEAD')
assert branch==snap['branch']=='arena/7d88376d-matrix-ring'
assert head==snap['head']=='168ec3e0b860cbe086ccb7a92a1a1aac5f8a277b'
assert subprocess.run(['git','diff','--quiet'],cwd=REPO).returncode==0,'Tracked working tree changed'
assert subprocess.run(['git','diff','--cached','--quiet'],cwd=REPO).returncode==0,'Index changed'
base={x['path']:x for x in snap['files']};comparisons=[];bad=[]
for rel,x in sorted(base.items()):
 p=REPO/rel
 if not p.is_file():
  actual=b'';h='MISSING';n=0;ok=False
 else:
  actual=p.read_bytes();h=sha(actual);n=len(actual);ok=(h==x['sha256'] and n==x['bytes'])
 if not ok:bad.append(rel)
 comparisons.append({'path':rel,'expected_bytes':x['bytes'],'actual_bytes':n,'expected_sha256':x['sha256'],'actual_sha256':h,'status':'UNCHANGED' if ok else 'CHANGED_OR_MISSING'})
assert not bad,('Original files changed/missing',bad)
current={p.relative_to(REPO).as_posix() for p in REPO.rglob('*') if p.is_file() and not p.is_relative_to(REPO/'.git') and not p.is_relative_to(B)}
extra=sorted(current-set(base));assert not extra,('New files outside correction_plan',extra)
assert set(base)<=current
# The completed independent-review ZIP must remain the delivered original.
review=REPO/'phase0_audit/independent_review/PHASE0_INDEPENDENT_REVIEW.zip'
assert review.stat().st_size==10731792 and sha(review.read_bytes())=='72e0edd006499ad77f37bcb0f905844ca96a46aa3a6f84daed81c123ed2aaa88'
prov=json.loads((E/'copied_evidence_provenance.json').read_text())
assert len(prov)==42
for x in prov:
 src=REPO/x['source'];dst=B/x['copy'];b=src.read_bytes()
 assert len(b)==x['bytes'] and sha(b)==x['sha256'] and dst.read_bytes()==b,('Source copy differs',x)
# Verify every available version-file identity against frozen source bytes.
versionfiles=list(csv.DictReader((E/'manuscript_files.csv').open()))
assert len(versionfiles)==320
for x in versionfiles:
 b=(REPO/x['file']).read_bytes();assert len(b)==int(x['bytes']) and sha(b)==x['sha256'],x['file']
versions=list(csv.DictReader((E/'manuscript_versions.csv').open()))
for v in versions:
 rows=[x for x in versionfiles if x['version_id']==v['version_id'] and (x['relative_file'] in ['main.tex','references.bib'] or (x['relative_file'].startswith('sections/') and x['relative_file'].endswith('.tex')))]
 manifest=''.join(x['sha256']+'  '+x['relative_file']+'\n' for x in sorted(rows,key=lambda y:y['relative_file'])).encode('utf8')
 assert len(rows)==int(v['core_files']) and sha(manifest)==v['source_payload_sha256'],v['version_id']
# Target checks are path/line checks only, not proof evaluation.
actions=json.loads((E/'correction_actions.json').read_text());target_checks=0;range_checks=0
for a in actions:
 for target in a['manuscript_targets']:
  if target.startswith('CAN/'):root=REPO/'phase0_audit/extracted/prior_project/PAPER';rel=target[4:]
  elif target.startswith('HIST/'):root=REPO/'phase0_audit/extracted/prior_project';rel=target[5:]
  else:root=REPO/'phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2';rel=target
  files=list(re.finditer(r'[A-Za-z0-9_./-]+\.(?:tex|bib|md|py)',rel));assert files,rel
  for i,m in enumerate(files):
   source=root/m.group(0);assert source.is_file(),str(source)
   lines=source.read_text().splitlines()
   scope=rel[m.end():files[i+1].start() if i+1<len(files) else len(rel)]
   for lm in re.finditer(r'[:;]\s*(\d+)(?:-(\d+|end))?',scope):
    start=int(lm.group(1));end=len(lines) if lm.group(2) in [None,'end'] else int(lm.group(2))
    assert 1<=start<=end<=len(lines),(target,len(lines))
    range_checks+=1
   target_checks+=1
for p in (B/'scripts').glob('*.py'):ast.parse(p.read_text(),filename=str(p))
# Import only the nonresearch archive validator, with -B used for this process.
spec=importlib.util.spec_from_file_location('plan_integrity_verifier',B/'scripts/verify_correction_plan_archive.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
# Stage the final records in memory before any final seal files are written.
payload={p.relative_to(B).as_posix():p.read_bytes() for p in B.rglob('*') if p.is_file()}
assert all(not p.is_symlink() for p in B.rglob('*'))
preservation={'recorded_clock_utc':iso,'baseline_capture_clock_utc':snap['capture_clock_utc'],'scope':snap['scope'],
 'protected_original_count':len(base),'protected_original_bytes':sum(x['bytes'] for x in base.values()),
 'all_original_files_unchanged':True,'changed_or_missing':bad,'new_files_outside_correction_plan':extra,
 'branch_before':snap['branch'],'branch_after':branch,'head_before':snap['head'],'head_after':head,
 'git_tracked_worktree_and_index_diff_empty':True,'git_status_after':git('status','--short'),
 'independent_review_zip_unchanged':True,'independent_review_zip_sha256':'72e0edd006499ad77f37bcb0f905844ca96a46aa3a6f84daed81c123ed2aaa88',
 'status':STATUS,'note':'Byte/size preservation and source identity, not mathematical readiness. No pre-existing file was changed.'}
payload[PRES]=jbytes(preservation)
s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=['path','expected_bytes','actual_bytes','expected_sha256','actual_sha256','status']);w.writeheader();w.writerows(comparisons);payload[COMP]=s.getvalue().encode('utf8')
validation={'recorded_clock_utc':iso,'status':STATUS,'implementation_authorized':False,
 'scientific_executions_in_this_task':0,'fresh_external_queries_in_this_task':0,'manuscript_edits_in_this_task':0,
 'replacement_theorems_or_proofs_generated':False,'tex_compilation_performed':False,'commits_or_pushes_performed':False,
 'all_new_outputs_within_correction_plan':True,'verbatim_source_copies_verified_against_originals':42,
 'available_version_file_hashes_verified':len(versionfiles),'manuscript_target_paths_checked':target_checks,'manuscript_target_line_ranges_checked':range_checks,
 'protected_original_count':len(base),'protected_original_bytes':sum(x['bytes'] for x in base.values()),
 'blocking_count_convention':'8 inherited BLOCKING finding families -> 8 CRITICAL actions; 29 MAJOR and 6 MINOR actions remain; A01–A04 excluded from research-blocker count.',
 'submission_status':'AUTHOR CONFIRMATION REQUIRED','authoritative_staging_version':'MS03; subject to current author baseline confirmation',
 'not_claimed':['proof repair','new result','new code search','full historical census recertification','exhaustive literature/priority check','actual submission/acceptance verification','journal-policy clearance','mathematical GO']}
payload[VALID]=jbytes(validation)
checks=v.validate_payload(payload.__getitem__,set(payload))
validation['content_validation']=checks;payload[VALID]=jbytes(validation)
assert v.validate_payload(payload.__getitem__,set(payload))==checks
# Preflight succeeded; write final records and seal, all under the allowed root.
for rel in [PRES,COMP,VALID]:
 with (B/rel).open('xb') as f:f.write(payload[rel])
manifest=''.join(sha(b)+'  '+rel+'\n' for rel,b in sorted(payload.items())).encode('utf8')
with (B/'SHA256SUMS.txt').open('xb') as f:f.write(manifest)
payload['SHA256SUMS.txt']=manifest
assert {p.relative_to(B).as_posix() for p in B.rglob('*') if p.is_file()}==set(payload)
with zipfile.ZipFile(Z,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for rel,b in sorted(payload.items()):
  i=zipfile.ZipInfo(PREFIX+'/'+rel,date_time=clock.timetuple()[:6]);i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o100644<<16
  z.writestr(i,b,compress_type=zipfile.ZIP_DEFLATED,compresslevel=9)
zh=sha(Z.read_bytes())
with SIDE.open('x') as f:f.write(zh+'  '+Z.name+'\n')
# Portable verifier is read-only and invokes no scientific code.
run=subprocess.run([sys.executable,'-B',str(B/'scripts/verify_correction_plan_archive.py'),str(Z)],cwd=REPO,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
with VERIFICATION.open('x',encoding='utf8') as f:f.write(run.stdout);f.write(run.stderr)
assert run.returncode==0,run.stderr
assert git('branch','--show-current')==branch and git('rev-parse','HEAD')==head
print('PASS: planning delivery sealed at',iso)
print('Protected originals:',len(base),'files /',sum(x['bytes'] for x in base.values()),'bytes; all unchanged.')
print('Versions:',len(versions),'inventory roots;',len(versionfiles),'available-file hashes; copies:',len(prov))
print('Register: 43 actions x 11 explicit fields; 8 CRITICAL / 29 MAJOR / 6 MINOR; dependency DAG acyclic.')
print('ZIP:',Z.relative_to(REPO),'bytes:',Z.stat().st_size,'SHA256:',zh)
print('ZIP entries:',len(payload),'internal hashes:',len(payload)-1,'local planning/report links:',checks['local_planning_and_report_links_checked'])
print('Portable verification: PASS. No scientific scripts executed.')
print(STATUS)
