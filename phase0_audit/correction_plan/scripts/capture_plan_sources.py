#!/usr/bin/env python3
"""Copy existing planning evidence verbatim and record source-reading locators.
No manuscript, audit or research code is modified or executed.
"""
from pathlib import Path
import hashlib, json, re, urllib.parse
BASE=Path(__file__).resolve().parents[1];REPO=BASE.parents[1]
IR=REPO/'phase0_audit/independent_review';E=BASE/'evidence';OUT=E/'audit_reports'
records=[]
def record_copy(src,dst):
    b=src.read_bytes();dst.parent.mkdir(parents=True,exist_ok=True)
    if dst.exists():
        assert dst.read_bytes()==b,('Existing planning copy differs',dst)
    else:
        with dst.open('xb') as f:f.write(b)
    records.append({'source':src.relative_to(REPO).as_posix(),'copy':dst.relative_to(BASE).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()})
# Maintain relative-link closure of the seven immutable report copies.
queue=[p.name for p in OUT.glob('*.md')];seen=set()
while queue:
    rel=queue.pop(0)
    if rel in seen:continue
    seen.add(rel);src=IR/rel;dst=OUT/rel
    assert src.is_file(),rel
    record_copy(src,dst)
    if src.suffix!='.md':continue
    for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]*?)\)',src.read_text()):
        target=m.group(1).strip().strip('<>')
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
        path=urllib.parse.unquote(target.partition('#')[0])
        p=(src.parent/path).resolve() if path else src
        assert p.is_relative_to(IR),target
        queue.append(p.relative_to(IR).as_posix())
# Additional audit evidence read to plan bounded test obligations, not rerun.
for rel in ['evidence/critical_followup_checks.json','evidence/remaining_scope_checks.json','evidence/route_and_bibliography_scope.json','evidence/bibliography_recheck_by_entry.csv','evidence/included_source_run_summary.json']:
    if rel not in seen:record_copy(IR/rel,OUT/rel)
# Historic records establishing which staging source was intended, not actual present submission.
prior=REPO/'phase0_audit/extracted/prior_project'
for rel in ['PAPER/README.md','PAPER/FFA_FINAL_SUBMISSION_PACKAGE/README.md',
            'PHASE18_ABSTRACT_OPTION_B_IMPLEMENTATION.md',
            'PHASE21_PRIVATE_DATA_ACCESS/PHASE21_FINAL_DECISION_REPORT.md',
            'PHASE21_PRIVATE_DATA_ACCESS/PHASE21_MANUSCRIPT_STAGING_NOTE.md',
            'PHASE22_GITHUB_DATA_PUBLICATION/PHASE22_GITHUB_PUBLICATION_REPORT.md',
            'PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md',
            'PHASE23_FFA_FINALIZATION/PHASE23_FFA_OPTION_C_COMPLIANCE.md']:
    record_copy(prior/rel,E/'documentary_sources'/rel)
# Supplemental source inspection is explicitly not a new proof audit or a repair.
ms=prior/'PAPER/FFA_FINAL_SUBMISSION_V2'
observations=[
 ('CP01','sections/04_cyclic_galois.tex',63,93,'The printed polynomial closure proof uses an equality not established by the coefficient-level right action; require a side/index-complete proof review. Do not transplant the valid source theorem without its proof.'),
 ('CP03','sections/03_preliminaries.tex',99,121,'The failure lemma mixes M2(F2), t=2, a nilpotent u, ring versus trace orthogonals, and a generic finite Frobenius ring with an Fq-specific proof. Require a consistent example and typed proof; no new counterexample was computed here.'),
 ('CP04','sections/04_cyclic_galois.tex',43,48,'The slot-immaterial sentence calls theta an involution without the reflexivity condition and transfers slots without convention translation. The independent audit already warns about positive/negative twists.'),
 ('CP05','sections/04_cyclic_galois.tex',209,228,'The printed proof asserts surjectivity to full Hom_Fq(C,R) from nondegeneracy. The audited module/functional argument must replace this unsupported reasoning; the equality result itself is conditionally retained.'),
 ('CP08','sections/04_cyclic_galois.tex',52,60,'The text equates cyclic with principal although its own standing definition allows all right ideals. A principality assertion needs a separate theorem and hypotheses.'),
 ('CP08','sections/04_cyclic_galois.tex',131,145,'Generator/annihilator sidedness must be reconciled explicitly. A right generating set cannot be passed through ann_r using the printed intuition alone.'),
 ('CP08','sections/04_cyclic_galois.tex',189,207,'The principal reduction and universal dropping-reversal corollary need side/quantifier review, not an inference from the fact that an annihilator is a right ideal.'),
 ('CP12','sections/03_preliminaries.tex',177,183,'The unused arbitrary-A-automorphism remark must not be read as a blanket extension of every Gray/metric/quantum assertion; the audit verifies the duality generalization, not all such extensions.'),
 ('CP31','sections/05_hulls.tex',355,379,'The witness-B prose says a proper superobject despite defining a hull as an intersection. Include this wording and every extra witness in the scoped verification/notation pass.'),
 ('CP40','main.tex',237,290,'Data availability remains PROPOSED, the text says referred for editorial confirmation while the documentary email is unsent, and the AI declaration awaits author confirmation. These are author gates, not facts to invent.')]
lines=['# Supplemental source-reading observations for the correction plan','',
       'These observations refine existing CP/CR action scopes. They are not repaired proofs, new theorems, new computations, or alterations of the independent audit. Exact line numbers refer to the frozen MS03 bytes in the inventory.','']
for issue,rel,start,end,remark in observations:
    p=ms/rel;s=p.read_text().splitlines()
    lines+=['## '+issue+' — '+rel+':'+str(start)+'–'+str(end),'',
            '**Source:** `'+p.relative_to(REPO).as_posix()+'`','',remark,'','```text']
    lines += [str(n)+': '+s[n-1] for n in range(start,min(end,len(s))+1)]
    lines+=['```','']
with (E/'source_reading_observations.md').open('x',encoding='utf8') as f:f.write('\n'.join(lines)+'\n')
with (E/'copied_evidence_provenance.json').open('x',encoding='utf8') as f:json.dump(records,f,indent=2);f.write('\n')
print('Verbatim source evidence copies:',len(records),'Supplemental source locators:',len(observations))
