#!/usr/bin/env python3
"""Read-only text/PDF readability and original PDF-member identity checks."""
from pathlib import Path
import ast,csv,hashlib,json,subprocess,zipfile,datetime,sys
BASE=Path(__file__).resolve().parents[1];ROOT=BASE/'work/PHASE0_COMPLETE_AUDIT_PACKAGE';REPO=BASE.parents[1]
sys.path.insert(0,str(BASE/'work/python-dependencies'))
import pypdf
OUT=BASE/'evidence/supporting_checks_v2';OUT.mkdir(exist_ok=False)
rows=[];errors=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file() or p.suffix.lower()=='.pdf':continue
    try:
        s=p.read_text(encoding='utf8');extra='UTF-8 decoded'
        if p.suffix=='.json':json.loads(s);extra+='; JSON parsed'
        elif p.suffix=='.csv':list(csv.DictReader(s.splitlines()));extra+='; CSV parsed'
        elif p.suffix=='.py':ast.parse(s);extra+='; Python AST parsed'
        rows.append({'file':p.relative_to(ROOT).as_posix(),'readable':True,'details':extra})
    except Exception as e:
        errors.append({'file':p.relative_to(ROOT).as_posix(),'error':str(e)})
with (OUT/'supporting_text_readability.csv').open('x',newline='') as f:
    w=csv.DictWriter(f,fieldnames=['file','readable','details']);w.writeheader();w.writerows(rows)
comparisons=list(csv.DictReader((ROOT/'repository_integrity/supplied_pdf_source_comparison.csv').open()))
pdfs=[]
for row in comparisons:
    p=ROOT/row['package_path'];b=p.read_bytes()
    reader=pypdf.PdfReader(p)
    extracted='\n'.join(page.extract_text() or '' for page in reader.pages)
    source_zip=REPO/'Matrix Ring 1.zip';source_ok=None
    if source_zip.is_file():
        archive,member=row['archive_member'].split('::',1)
        with zipfile.ZipFile(source_zip) as z:source_ok=z.read(member)==b
    d={'file':row['package_path'],'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest(),'matches_recorded_authentic_member':hashlib.sha256(b).hexdigest()==row['original_member_sha256'],'matches_actual_original_zip_member':source_ok,'pdf_magic':b.startswith(b'%PDF-'),'parser':'pypdf '+pypdf.__version__,'text_bytes':len(extracted.encode()),'pages':len(reader.pages),'scope':'Readable PDF text and source identity, not mathematical validation of competitor paper.'}
    pdfs.append(d)
    if not d['matches_recorded_authentic_member'] or source_ok is False or not extracted:errors.append(d)
result={'text_files_checked':len(rows),'text_errors':errors,'pdfs':pdfs,'all_checks_pass':not errors,'original_zip_comparison_available':(REPO/'Matrix Ring 1.zip').is_file(),'scope':'Independent readability/identity checks; no files overwritten.'}
with (OUT/'supporting_file_checks.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
if errors:sys.exit(1)
