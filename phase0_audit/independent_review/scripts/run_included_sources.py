#!/usr/bin/env python3
"""Re-execute existing included checks in disposable copies, never in original data."""
from pathlib import Path
import concurrent.futures as futures
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parents[1]
INPUT = BASE / 'work/PHASE0_COMPLETE_AUDIT_PACKAGE/computational_evidence/research-data'
EVIDENCE = BASE / 'evidence'
RUNS = BASE / 'work/source_runs'
RUNS.mkdir(exist_ok=False)

def run_one(name, script, args, limit):
    root = RUNS / name
    root.mkdir()
    scripts = root / 'scripts'
    shutil.copytree(INPUT / 'scripts', scripts)
    command = [sys.executable, '-B', str(scripts / script)] + [str(x).replace('{ROOT}',str(root)) for x in args]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', MATRIX_RING_COMP=str(scripts))
    log = EVIDENCE / (name + '_stdout.txt')
    start = time.monotonic()
    print('START',name,'limit',limit,'seconds',flush=True)
    with log.open('x',encoding='utf8') as out:
        try:
            p = subprocess.run(command, cwd=root, env=env, stdout=out, stderr=subprocess.STDOUT, timeout=limit)
            state,code = 'COMPLETED',p.returncode
        except subprocess.TimeoutExpired:
            state,code = 'TIME_LIMIT_REACHED',None
    generated = []
    # Logs are generated either in CWD or next to copied source, depending on historical script.
    for p in sorted(list(root.glob('*.txt')) + list(scripts.glob('*.txt'))):
        dest = EVIDENCE / (name + '__' + p.name)
        with dest.open('xb') as out:out.write(p.read_bytes())
        generated.append({'file':dest.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    comparisons=[]
    if name == 'generator_reconstruction' and (root/'generated/INDEX.json').exists():
        for p in sorted((root/'generated').glob('*.json')):
            original=INPUT/'generator_matrices'/p.name
            comparisons.append({'file':p.name,'exists_in_original':original.exists(),
                'byte_equal': original.is_file() and p.read_bytes()==original.read_bytes(),
                'json_equal':original.is_file() and json.loads(p.read_text())==json.loads(original.read_text())})
    result={'name':name,'command':command,'cwd':str(root),'timeout_seconds':limit,'state':state,
            'exit_code':code,'elapsed_seconds':round(time.monotonic()-start,3),'stdout':log.name,
            'generated_logs':generated,'generator_comparisons':comparisons,
            'scope':'Re-execution of included historical scripts, not an independent implementation.'}
    with (EVIDENCE/(name+'_run.json')).open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    print('END',name,state,code,result['elapsed_seconds'],flush=True)
    return result

jobs=[('phase0_rerun','phase0_feasibility.py',[],90),
      ('gray_full_rerun','phase4_gray_map_compatibility.py',[],480),
      ('generator_reconstruction','extract_certified_generators.py',['{ROOT}/generated'],720)]
with futures.ThreadPoolExecutor(max_workers=3) as pool:
    results=list(pool.map(lambda x:run_one(*x), jobs))
with (EVIDENCE/'included_source_run_summary.json').open('x') as f:json.dump(results,f,indent=2);f.write('\n')
print('SOURCE RUNS FINISHED',flush=True)
