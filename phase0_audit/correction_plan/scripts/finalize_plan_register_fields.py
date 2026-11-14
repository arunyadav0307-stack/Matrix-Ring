#!/usr/bin/env python3
"""Finalize eleven explicitly numbered fields in the new, unsealed plan only.
No original, scientific source or manuscript is written or executed.
"""
from pathlib import Path
import csv,json
B=Path(__file__).resolve().parents[1]; E=B/'evidence'
a=json.loads((E/'correction_actions.json').read_text())
assert all('related_claim' not in x for x in a),'One-time plan refinement already applied'
claims={
'CP01':'def:code; eq:morita; def:pairing; lem:sesqui; thm:duality(a), especially its polynomial-closure proof.',
'CP02':'eq:Lambda / lem:lambda; thm:duality(b); ancillary P1 nondegeneracy probe versus the existing supporting Proposition 2.2.',
'CP03':'lem:failure and its printed example/proof; rem:convention; duality-origin wording in section 9.',
'CP04':'Unnumbered slot-immaterial paragraph, section 4 lines 43–48; thm:duality(c); alternate-left mirror in the frozen pairing-options summary.',
'CP05':'eq:Lambda; lem:lambda; prop:twoorth, especially full-Hom-surjectivity proof; thm:grayduality and thm:grayhull dependencies.',
'CP06':'def:pairing / fixed slot convention: manuscript consistency guard only. The disputed P3 candidate is ancillary, not an existing MS03 theorem to replace.',
'CP07':'eq:rings; eq:morita; lem:basic; prop:moritahull and base-chain-ring versus cyclic-B discussion. Ancillary base-ideal assertion is the direct false claim.',
'CP08':'eq:crt; lem:components; thm:duality(d); lem:ann; thm:dualformula; cor:rev; prop:moritahull. Existing S2B Theorems 4.1/4.3/Corollary 4.4 resolve the old open-status claim.',
'CP09':'False freeness premise opening the section 5 non-principal-hull subsection; generation argument used by lem:components.',
'CP10':'thm:nonprincipal; eq:witnessfamily; tab:witnesses; rem:o31b; thm:noclosed; ex:witnessA/B; dependent abstract and novelty claims.',
'CP11':'Phase5 Task D3 lines 1364–1368 and the existing Phase6 hull_mu helper; manuscript rem:mub and witness-mu table interpretation. This is a representation bug, not a new theorem.',
'CP12':'def:sigma; lem:theta and arbitrary-automorphism remark; thm:duality(b,c); def:regimes / prop:regimes; thm:hullstruct; supporting S Theorems 3.6/3.9.',
'CP13':'cor:noteuclid; def:congruence; thm:obstruction; rem:obstructionexact; related thm:parameters scope. Retain the valid restricted bilinear theorem.',
'CP14':'thm:gram alternatingness clause and final proof paragraph; ex:gray.',
'CP15':'prop:congruence; rem:obstructionexact; ex:obstruction; thm:R2; actual Phase5 GF9 congruence matrix/form contract.',
'CP16':'thm:obstruction universal code-level consequence; thm:R2; thm:parameters and route recommendation.',
'CP17':'Lambda codomain / lem:sesqui; eq:weyl / eq:omega / lem:Q1 trace levels. The direct type error is in the ancillary Gray source, not the correctly typed MS03 central-scalar law.',
'CP18':'Historical Gray script reflexivity header at line 982 versus actual C5 condition at line 1026; manuscript regime/reproduction description, not a refuted reflexivity theorem.',
'CP19':'Finite-suite EXH/SMP quantifiers, appendix reproduction scope and section 8 methodology. No universal theorem is established by the count 463.',
'CP20':'Generator JSON/README environment and integer encoding contract; tab:cert / appendix environment description. No theorem identity needs replacement solely for metadata.',
'CP21':'Frontier/headline/budget/census statements and abstract numerical scope; not an independent proof of every historical scanned code or distance row.',
'CP22':'eq:weyl; eq:omega; lem:Q1; downstream lem:Q2 / thm:fpbasis phase convention.',
'CP23':'lem:Q2 statement/proof; thm:fpbasis; R1/R2 uses of the stabilizer result.',
'CP24':'thm:R3 proof and field-discipline remark; EA distance uses in thm:cosetdistance / thm:feasibility. Standard conditional formulas are not refuted.',
'CP25':'eq:V; thm:R1; thm:R1cap; thm:R2; thm:parameters; standing dimension-field convention.',
'CP26':'thm:grayduality / thm:grayhull versus ordinary-Euclidean h_E in thm:R3. No unproved transported-Galois-hull-to-EA bridge is an existing result.',
'CP27':'thm:cosetdistance; eq:criterion; thm:R2(b); abstract universal distance interpretation.',
'CP28':'thm:cosetdistance metric interpretation; thm:cosetsingleton projection proof; prop:newsbound and separate nonimplication/priority claims.',
'CP29':'thm:feasibility; thm:bookkeeping and erratum; thm:parameters; downstream frontier/budget statements.',
'CP30':'Section 8 methodology; ex:certify; tab:cert and staged abstract 11/17 split. Historical all-three claim is already corrected in MS03.',
'CP31':'ex:witnessA/B; tab:witnesses; tab:headline; additional nonprincipal-origin quantum claims. Extra rows are not included in the 28-record certificate verdict.',
'CP32':'tab:comparison; tab:grassl; all same-alphabet gap/record/ratio interpretations and related abstract/introduction claims.',
'CP33':'Table-availability prose and GrasslCodetables entry; no mathematical construction theorem is directly changed by an endpoint correction.',
'CP34':'Bibliographic key Alahmadi2013CyclicM2F2 and its section 2 citation; direct citation-identity defect, not a theorem counterexample.',
'CP35':'GreferathSchmidt1999GrayIsometry / Fan / LiuPan / Cao / Ketkar records and attributed comparisons; ancillary Oggier/affine/placeholder identities. No automatic proof validation from metadata.',
'CP36':'Specific-and-proved novelty list; prop:newsbound / new-bound independence claim; contribution summaries in abstract/introduction/conclusion and related-work comparison.',
'CP37':'Ancillary first-q8-EA proposal; manuscript/future-work boundary only. No existing MS03 theorem is being replaced by new P1 research.',
'CP38':'Standing matrix-size-two scope and prop:qc consistency; ancillary P2 threshold/index/complexity assertions, not a defect in the current size-two formula.',
'CP39':'Central-X / R_n definition and future-work boundary; ancillary unproved P3 Ore-quotient/compatibility claim, not a current skew theorem.',
'CP40':'Author/data/AI/declaration blocks and exact manuscript provenance; author-only status decisions, not a mathematical theorem.',
'CP41':'Data-availability / appendix package-count and manifest statements; provenance counting bases, no mathematical theorem.',
'CP42':'All literal manuscript inputs, source/build and historical-reference closure; missing-container/partial-mirror qualifications, not universal proof closure.',
'CP43':'Reproduction appendix and section 8 methodology execution attribution; audit self-disclosures A01–A04 remain historical checker/date issues, not manuscript counterexamples.'}
assert set(claims)=={x['id'] for x in a}
for x in a:x['related_claim']=claims[x['id']]
MS='phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/';CAN='phase0_audit/extracted/prior_project/PAPER/';HIST='phase0_audit/extracted/prior_project/'
def expand(t):
 if t.startswith('CAN/'):return CAN+t[4:]
 if t.startswith('HIST/'):return HIST+t[5:]
 return MS+t
cards=[]
for x in a:
 s=f"### {x['id']} — {x['title']}\n\n**Group:** {x['group']}. **Disposition:** {x['baseline_disposition']}\n\n"
 s+=f"**1. Issue ID:** {x['id']} (audit {x['audit_id']}).\n\n"
 s+='**2. Exact manuscript filename / section:**\n\n'+'\n'.join('- `'+expand(t)+'`' for t in x['manuscript_targets'])+'\n\n'
 for label,key in [('3. Relevant theorem / equation / proof','related_claim'),('4. Defect explanation','source_issue'),('5. Independent-audit evidence / source-reading refinement','audit_evidence'),('6. Required mathematical / editorial correction — future only','required_correction'),('7. New proof required?','new_proof_required'),('8. Computational verification required — NOT RUN','computational_verification'),('9. Impact on quantum-code parameters','quantum_parameter_impact')]:s+='**'+label+':** '+x[key]+'\n\n'
 s+='**10. Severity:** '+x['severity']+'.\n\n'
 s+='**11. Dependencies:** '+(', '.join(x['depends_on']) or 'None; first author/provenance gate.')+'\n\n'
 cards.append(s)
p=B/'MASTER_CORRECTION_REGISTER.md';old=p.read_text();start=old.index('## 3. Detailed action cards');end=old.index('## 4. Closure evidence')
new=old[:start]+'## 3. Detailed action cards — eleven explicitly numbered fields\n\n'+''.join(cards)+old[end:]
p.write_text(new)
with (E/'correction_actions.json').open('w',encoding='utf8') as f:json.dump(a,f,indent=2,ensure_ascii=False);f.write('\n')
keys=['id','audit_id','title','group','severity','exact_manuscript_targets','related_theorem_equation_proof','defect','audit_evidence','required_correction','new_proof_required','computational_verification','quantum_parameter_impact','dependencies','baseline_disposition']
with (E/'master_correction_register.csv').open('w',encoding='utf8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
 for x in a:w.writerow({'id':x['id'],'audit_id':x['audit_id'],'title':x['title'],'group':x['group'],'severity':x['severity'],'exact_manuscript_targets':' ; '.join(expand(t) for t in x['manuscript_targets']),'related_theorem_equation_proof':x['related_claim'],'defect':x['source_issue'],'audit_evidence':x['audit_evidence'],'required_correction':x['required_correction'],'new_proof_required':x['new_proof_required'],'computational_verification':x['computational_verification'],'quantum_parameter_impact':x['quantum_parameter_impact'],'dependencies':'; '.join(x['depends_on']),'baseline_disposition':x['baseline_disposition']})
print('New unsealed register finalized: 43 cards × 11 numbered fields; separate claim/proof field in JSON/CSV. No original file touched.')
