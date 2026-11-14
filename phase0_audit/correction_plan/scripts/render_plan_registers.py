#!/usr/bin/env python3
"""Render planning documents from inventories and hand-authored correction actions.
This generates plans only, never manuscript text, replacement theorems or proofs.
"""
from pathlib import Path
import collections, csv, hashlib, json
B=Path(__file__).resolve().parents[1];E=B/'evidence';REPO=B.parents[1]
STATUS='HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.'
MS='phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/'
CAN='phase0_audit/extracted/prior_project/PAPER/'
HIST='phase0_audit/extracted/prior_project/'
actions=json.loads((E/'correction_actions.json').read_text())
versions=list(csv.DictReader((E/'manuscript_versions.csv').open()))
latest=next(v for v in versions if v['version_id']=='MS03')
canonical=next(v for v in versions if v['version_id']=='MS01')
byid={a['id']:a for a in actions}
assert len(byid)==43 and set(byid)=={'CP%02d'%i for i in range(1,44)}
assert collections.Counter(a['severity'] for a in actions)=={'CRITICAL':8,'MAJOR':29,'MINOR':6}
# A verified dependency DAG, not an authorization/execution schedule.
order=[];pending=set(byid)
while pending:
    ready=sorted(i for i in pending if set(byid[i]['depends_on'])<=set(order))
    assert ready,('Dependency cycle',pending)
    order.extend(ready);pending.difference_update(ready)

def expand(target):
    if target.startswith('CAN/'):return CAN+target.removeprefix('CAN/')
    if target.startswith('HIST/'):return HIST+target.removeprefix('HIST/')
    return MS+target

def out(name,text):
    with (B/name).open('x',encoding='utf8') as f:f.write(text.rstrip()+'\n')

def table(header,rows):
    def cell(x):return str(x).replace('|','\\|').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(header)+' |','|'+'|'.join('---' for _ in header)+'|']+['| '+' | '.join(cell(x) for x in r)+' |' for r in rows])

head=f'''# Authoritative manuscript identification

**Recorded planning execution:** 2026-11-13 UTC (workspace clock).  
**{STATUS}**

## 1. Exact finding: authoritative **staging** source is documented

The historical Phase23 data-availability record explicitly says:

> Applied to: `PAPER/FFA_FINAL_SUBMISSION_V2/` (the new authoritative staging copy) only. The canonical manuscript, the V2 and V3 reviewer packages and the Phase 19 FFA copy are untouched.

See the [verbatim Phase23 designation](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md), opening and §§B5–B8. This is stronger evidence than folder names or filesystem mtimes. It identifies a staging authority, **not** an actually submitted or accepted version.

**Documented correction-planning baseline: MS03**

- Title: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings*.
- Complete recovered source root: `{latest['root']}/`.
- Entry file: `{latest['main_file']}`.
- Entry file size: **{int(latest['main_bytes']):,} bytes**.
- Observed entry-file mtime UTC: **{latest['observed_main_mtime_utc']}**.
- Entry-file SHA-256: `{latest['main_sha256']}`.
- **14-file core-source-set SHA-256:** `{latest['source_payload_sha256']}`.
- Core set: `main.tex`, **12** `sections/*.tex` files and `references.bib`. All literal section inputs exist in this full recovered root.

The core-set digest is SHA-256 of UTF-8 lines `file_sha256 + two spaces + relative_filename + newline`, sorted by relative filename. It is not the SHA of a hypothetical ZIP or compiled PDF. The exact [MS03 source manifest](evidence/MS03_source_manifest.sha256) and [all-file inventory](evidence/manuscript_files.csv) identify each source's bytes and observed mtime. Generated `.bbl` snapshots are inventoried separately and are not part of that 14-file digest.

**Author gate:** confirm that MS03 is still the intended baseline and identify any later/private/submitted revision before implementation. Until then no working manuscript copy is created and no source selection is silently adopted for correction.

## 2. Inventory scope and timestamp interpretation

Read-only local inventory found **19 recovered campaign source roots**, containing **9 distinct 14-file core payloads**, plus **4 curated audit mirrors**. These are snapshots/build copies of **one prior campaign**, not 19 different papers. Every available source filename, size, observed mtime and SHA-256 appears in [manuscript_files.csv](evidence/manuscript_files.csv); root identities are in [manuscript_versions.csv](evidence/manuscript_versions.csv).

The mtimes below are **recovery/extraction filesystem observations**, not verified creation dates, author approval dates or submission timestamps. The primary recovered files cluster around 2026-11-13T06:47:04Z; sorting those timestamps would give a misleading chronology. Original documents contain historical Nov9/Nov10 labels and decisions; these remain attributed historical records. No missing timestamp or hash is invented.

`PRIOR/` in the following table means exactly `phase0_audit/extracted/prior_project/`. Each entry file is `PRIOR/<root>/main.tex`.

'''
roots=[v for v in versions if v['kind'].startswith('RECOVERED')]
head+=table(['ID','Root relative to PRIOR','Observed main mtime UTC','main.tex SHA-256','14-file core SHA-256'],[[v['version_id'],v['root'].removeprefix(HIST),v['observed_main_mtime_utc'],'`'+v['main_sha256']+'`','`'+v['source_payload_sha256']+'`'] for v in roots])
head+='''

### Curated audit mirrors — not four extra author versions

The inventory mirror identifiers `CP01`/`CP02` below are **not** the correction-action identifiers of the same spelling in the master register; their namespace is the version inventory.

The full canonical mirrors CP01/IP01 reproduce MS01. CP02/IP02 contain only the curated MS03 delta (**5 core files**, not the full14); eight section inputs plus the bibliography are mapped to shared canonical sources by the original package's input-resolution table. Their entry-file hash matches MS03, but their partial directory digest does not identify a self-contained manuscript. **Use the complete MS03 recovered source set for any later approved build, not a delta directory alone.**

'''
head+=table(['ID','Exact root','Observed main mtime UTC','main.tex SHA-256','Core files'],[[v['version_id'],v['root'],v['observed_main_mtime_utc'],'`'+v['main_sha256']+'`',v['core_files']] for v in versions if not v['kind'].startswith('RECOVERED')])
head+=f'''

## 3. Which version corresponds to the completed prior research campaign?

**MS01**, `{canonical['root']}/`, is the preserved Phase8 canonical manuscript with the full completed-campaign theorem/computation sections. Its entry SHA-256 is `{canonical['main_sha256']}` and its 14-file core digest is `{canonical['source_payload_sha256']}`. Its [README](evidence/documentary_sources/PAPER/README.md) is an earlier Phase8 record and is not an up-to-date submission-status attestation.

**MS03 is the later documented authoritative staging derivative of that same campaign**, incorporating author/abstract/certification/formatting/data-availability updates through Phase23. The included 28 supplied generator records, q4/q8/q9 routes and historical wider search are the campaign described by these sources; MS03 is not a new P1/P2/P3 manuscript. The existence of a completed campaign does not certify every theorem or mean it is submission-ready.

## 4. Conflicting arguments and why switching folders will not remove HOLD

The [per-version comparison table](evidence/version_comparisons.csv) and [MS03-versus-canonical diff](evidence/version_diffs/MS03_vs_canonical.diff) show exactly which files differ. Across all 19 recovered roots, the core files **§§2–6, §9, §10, Appendix Reproducibility and references.bib are byte-identical** to their canonical counterparts. Thus the nonprincipal-hull family, scalar/module/slot proof obligations, broad alternatingness/congruence consequences and benchmark mistakes are not cured by selecting a later directory.

Between MS01 and MS03:

- `main.tex`: author metadata, abstract and declaration/data-availability blocks differ; the MS03 abstract gives the11/17 quantum-search split instead of the historical three-method overclaim.
- `sections/01_introduction.tex`: updated contribution/certification description.
- `sections/07_quantum.tex`: exponential typesetting only; **the substantive stabilizer, EA and all-route parameter proof defects persist**.
- `sections/08_certification.tex`: historical “all three methods”/worked-example statements are corrected in MS03; route/quotient/bookkeeping defects persist.
- `sections/appendix_tables.tex`: later certification-method explanation/table presentation; it does not recertify all wild/headline claims.

MS04/MS05 are the Phase19 formatting copies; MS09/MS16/MS17 carry the later approved abstract; MS18/MS19 stage private-request data wording; MS03 stages the later public commit-pinned data wording. These sources contain **incompatible data-access declarations** if treated as simultaneously current. The Phase23 record supersedes the earlier statement only for MS03 and keeps its own wording **PROPOSED**. This plan does not select author declarations or conflate formatting/certification updates with repaired mathematics.

The [supplemental source-reading observations](evidence/source_reading_observations.md) refine existing audit action scopes (CP01/03/04/05/08/12/31/40). They flag exact printed proof/type/quantifier obligations, **not** newly supplied proofs or a claim that all manuscript arguments have now been re-audited.

## 5. Compiled PDFs and archival versions

- `{CAN}main.pdf` is the previously audited lossy patch-text recovery, **not a valid authoritative compiled manuscript**. Observed size617,752 bytes; observed SHA-256 `709fdd7bc52cd66187e39839ad9a5a9eb0c3818b73501270b57aa548ef11faf1`. Its `%PDF` prefix does not repair the binary corruption.
- The Phase23 record claims a42-page/580,019-byte staged PDF with SHA-256 `d125cc096f0c7344f5435193bb410813c3bcc1175cb828b5c9980b00446b5ee1`. Its actual bytes were **not** recovered/verified here. Treat this as a historical documentary digest, not the hash of an available submitted PDF.
- The patch inventories **11 manuscript-related binary-only paths**:7PDFs and4ZIPs. See [unavailable artifacts](evidence/unavailable_manuscript_artifacts.csv). Other PDFs mentioned in review-package manifests are also not established as recovered valid binaries merely by their names/digests in text.
- Four manuscript archive `.sha256` sidecars survive. Their exact filenames, observed timestamps, sidecar hashes and **unverified inherited target digests** are in [historical archive claims](evidence/historical_archive_digest_claims.csv). None of those four target ZIPs is present. Neither `Matrix Ring.zip` (an empty unrelated archive) nor the literature `Matrix Ring 1.zip` is a manuscript release.
- `PHASE0_COMPLETE_AUDIT_PACKAGE.zip` and `PHASE0_INDEPENDENT_REVIEW.zip` are audit containers with selected sources/evidence, not original author submission archives.

No PDF reconstruction, TeX build or manuscript ZIP reconstruction is authorized or performed in this planning task.

## 6. Submission status — **AUTHOR CONFIRMATION REQUIRED**

The local documentary search covered **209 recovered Markdown records**, plus the source/version inventories and submission-like filenames. See [search rows](evidence/submission_documentary_search.csv) and [scope summary](evidence/manuscript_inventory_summary.json). Findings:

1. The [earlier final-submission package README](evidence/documentary_sources/PAPER/FFA_FINAL_SUBMISSION_PACKAGE/README.md) explicitly calls itself preparation and says no submission was made/authorized.
2. [Phase21](evidence/documentary_sources/PHASE21_PRIVATE_DATA_ACCESS/PHASE21_FINAL_DECISION_REPORT.md), §6, says nothing was submitted and no Editorial Manager account existed **at that historical stage**.
3. The later [Phase23 data statement](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_DATA_AVAILABILITY_STATEMENT.md), §B6, says “Submitted anything — No”; §B8 still awaits researcher/editorial confirmation.
4. [Phase23 Option-C record](evidence/documentary_sources/PHASE23_FFA_FINALIZATION/PHASE23_FFA_OPTION_C_COMPLIANCE.md), Appendix E, marks its email **DRAFT — NOT SENT**. No editorial acceptance/exception follows from the manuscript phrase “referred for editorial confirmation.”
5. No verified journal receipt, manuscript/submission identifier, dated editorial decision or acceptance letter was located. No journal account, email service, current submission portal or private author records were accessed. Historical data publication on GitHub is not manuscript submission.

Therefore the documents support **historical non-submission/preparation**, not an unconditional claim about today's private author actions. Current submission status, any later version and exact submitted PDF/source identity remain **AUTHOR CONFIRMATION REQUIRED**. A missing local receipt does not prove no external submission occurred.

## 7. Consequence for this plan

Use **MS03** for exact line/label locators and planned successor work **subject to fresh author confirmation**. Preserve MS01 and every other snapshot as immutable history. Confirm existing authorship/declaration approvals rather than inventing new ones. Do not compile, change claims, send an editorial message, submit, create a release, commit or push without separate explicit authorization.

**{STATUS}**
'''
out('AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md',head)
# Source-set manifest, not replacement manuscript bytes.
rows=list(csv.DictReader((E/'manuscript_files.csv').open()))
core=[r for r in rows if r['version_id']=='MS03' and (r['relative_file']=='main.tex' or r['relative_file']=='references.bib' or r['relative_file'].startswith('sections/'))]
with (E/'MS03_source_manifest.sha256').open('x') as f:
    for r in sorted(core,key=lambda x:x['relative_file']):f.write(r['sha256']+'  '+r['relative_file']+'\n')

master=f'''# Master correction register

**Recorded planning execution:** 2026-11-13 UTC.  
**{STATUS}**

## 1. Counts, severity and provenance

This register expands **all 43 CR01–CR43 issue families** from the independent review into **CP01–CP43**, one to one. It does not silently modify that review. There are **8 CRITICAL HOLD blockers**, **29 MAJOR** actions and **6 MINOR** actions. CR03 is escalated from the audit's MEDIUM to MAJOR because direct source reading finds inconsistent ring/example/proof typing in the current failure lemma. Other source-reading refinements stay inside their existing issue families and do not create a misleading extra count.

**Blocking-count definition:** the 8 inherited BLOCKING findings are the 8 CRITICAL actions below. Six are mathematical theorem/proof/route failures, one is physical-alphabet benchmarking, and one is author/provenance/submission control. MAJOR prerequisites still must be satisfactorily closed, restricted or withdrawn before their dependent blocker can close; “not CRITICAL” does **not** mean optional. 43 is not a count of 43 false current manuscript theorems: several rows are ancillary errors, boundary controls or already-corrected historical overclaims.

Severity is separate from the independent audit's six mathematical classifications, which remain unchanged. All requested repairs/tests are **future obligations conditional on explicit implementation approval**. No proof, theorem, code, dataset or manuscript has been repaired by this plan.

'''
critical=[a for a in actions if a['severity']=='CRITICAL']
master+=table(['Critical ID','Audit ID','Blocker'],[[a['id'],a['audit_id'],a['title']] for a in critical])
master+='''

### Exact-path conventions and evidence

Every target below is expanded to the exact recovered manuscript path. `CAN/` targets explicitly mean the historical canonical source, not MS03. An ancillary-only issue lists the related manuscript consistency check and says no direct MS03 error was located; that is not a fabricated theorem defect.

- Primary baseline and complete version/time/hash inventory: [AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md](AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md).
- Independent [correction register](evidence/audit_reports/DISCREPANCY_AND_CORRECTION_REGISTER.md), [claim ledger](evidence/audit_reports/MATHEMATICAL_CLAIM_VERIFICATION.md), [pairing audit](evidence/audit_reports/PAIRING_AND_DUALITY_CRITICAL_AUDIT.md), [Gray audit](evidence/audit_reports/GRAY_MAP_EVIDENCE_AUDIT.md), [literature audit](evidence/audit_reports/LITERATURE_AND_NOVELTY_RECHECK.md).
- References to `independent_core_checks.json`, `critical_followup_checks.json`, `remaining_scope_checks.json` and `independent_28_code_checks.json` are the **existing** copied audit evidence under `evidence/audit_reports/evidence/`, not new execution results.
- Fresh source locators/refinements: [source-reading observations](evidence/source_reading_observations.md) and [statement locators](evidence/manuscript_statement_locators.csv).
- Machine-readable [action index](evidence/master_correction_register.csv) and [authored action definitions](evidence/correction_actions.json).
- Planned B00–B08 tests are specified in [COMPUTATIONAL_REPAIR_PLAN.md](COMPUTATIONAL_REPAIR_PLAN.md). All are **NOT RUN / NOT AUTHORIZED** in this task.

## 2. Action index

'''
master+=table(['ID ↔ audit','Group','Severity','Current disposition / scope','Dependencies'],[[a['id']+' ↔ '+a['audit_id'],a['group'],a['severity'],a['baseline_disposition'],', '.join(a['depends_on']) or 'Author gate; no predecessor'] for a in actions])
master+='\n\n## 3. Detailed action cards — eleven explicitly numbered fields\n'
for a in actions:
    master+=f"\n### {a['id']} — {a['title']}\n\n"
    master+=f"**Group:** {a['group']}. **Disposition:** {a['baseline_disposition']}\n\n"
    master+=f"**1. Issue ID:** {a['id']} (audit {a['audit_id']}).\n\n"
    master+='**2. Exact manuscript filename / section:**\n\n'+'\n'.join('- `'+expand(t)+'`' for t in a['manuscript_targets'])+'\n\n'
    for label,key in [('3. Relevant theorem / equation / proof','related_claim'),('4. Defect explanation','source_issue'),('5. Independent-audit evidence / source-reading refinement','audit_evidence'),('6. Required mathematical / editorial correction — future only','required_correction'),('7. New proof required?','new_proof_required'),('8. Computational verification required — NOT RUN','computational_verification'),('9. Impact on quantum-code parameters','quantum_parameter_impact')]:
        master+='**'+label+':** '+a[key]+'\n\n'
    master+='**10. Severity:** '+a['severity']+'.\n\n'
    master+='**11. Dependencies:** '+(', '.join(a['depends_on']) or 'None; first author/provenance gate.')+'\n\n'
master+=f'''## 4. Closure evidence and what must not be changed

A future action may close only with a frozen input identity, an authorized successor diff or an explicit restriction/withdrawal, proof/citation review where required, the specified test records where applicable, and an independent reviewer sign-off. A plan, passing old log, or source hash alone never closes a proof defect.

The positive double dual, conditional size/reflexivity results, exact transported Gram form, valid earlier nonprincipal witness, reproduced 463 assertions and 28 recertified field records are **retained at their audited scope**. Do not alter valid tuples merely to fit an erroneous all-route identity. Do not claim that CP28 refutes the restricted Singleton inequality.

Audit self-disclosures **A01–A04** are not four more research defects or blockers. They concern the preserved snapshot date field, a corrected parser artifact, an extraneous first checker assertion and the resolved PDF-parser dependency. Keep the authoritative-v2 evidence and the historical artifacts together; no independent-review file is edited. They are addressed by CP43's lineage control, not by rewriting research proofs.

No issue card authorizes P1/P2/P3, a new code search, manuscript drafting now, old-report edits, publication, Git commit or push. All implementation decisions remain in [AUTHOR_APPROVAL_CHECKLIST.md](AUTHOR_APPROVAL_CHECKLIST.md).

**{STATUS}**
'''
out('MASTER_CORRECTION_REGISTER.md',master)
with (E/'master_correction_register.csv').open('x',encoding='utf8',newline='') as f:
    keys=['id','audit_id','title','group','severity','exact_manuscript_targets','related_theorem_equation_proof','defect','audit_evidence','required_correction','new_proof_required','computational_verification','quantum_parameter_impact','dependencies','baseline_disposition']
    w=csv.DictWriter(f,fieldnames=keys);w.writeheader()
    for a in actions:w.writerow({'id':a['id'],'audit_id':a['audit_id'],'title':a['title'],'group':a['group'],'severity':a['severity'],
        'exact_manuscript_targets':' ; '.join(expand(t) for t in a['manuscript_targets']),'related_theorem_equation_proof':a['related_claim'],'defect':a['source_issue'],'audit_evidence':a['audit_evidence'],
        'required_correction':a['required_correction'],'new_proof_required':a['new_proof_required'],'computational_verification':a['computational_verification'],
        'quantum_parameter_impact':a['quantum_parameter_impact'],'dependencies':'; '.join(a['depends_on']),'baseline_disposition':a['baseline_disposition']})

mapping=f'''# Correction dependency map

**Recorded planning execution:** 2026-11-13 UTC.  
**{STATUS}**

## 1. Gate logic — a dependency is not permission

```text
Current task: READ + PLAN + FILE-INTEGRITY CHECKS ONLY
             |
             v
CP40: author confirms MS03/source hash + actual submission status
      and separately authorizes a bounded implementation scope
             |
             v
B00/B01: preservation + exact field/coordinate contract
             |
             v
Group A foundations -> hull proof/representation -> Gray form scope
             |
             v
Weyl/stabilizer -> EA + route contracts -> quotient/bound/bookkeeping
             |
             v
Group B targeted recertification of explicitly retained claims/rows
             |
             v
Group D matching benchmarks + source/theorem-level novelty comparison
             |
             v
Group C final notation/summary/declarations/source-build reconciliation
             |
             v
Independent re-audit; separate author publication decision
```

Metadata/source reading may be parallelized after authorization, but no final novelty summary or benchmark interpretation can precede the corrected retained claim/parameter set. No date/duration estimate here promises proof success. If a proof cannot be repaired from existing material without new results, choose restriction/withdrawal or stop for a new authorization—not an unapproved research phase.

## 2. Safest group order

| Group | Safest internal execution order, only after approval | Exit requirement |
|---|---|---|
| **A Mathematical proof corrections** | Fix conventions/functional/codomain and cyclic/annihilator hypotheses; confirm +DD/reflexivity; replace/withdraw the invalid hull family; delimit Gray forms; Weyl phases → scoped stabilizer → Bob completion → route groups → quotient/metric/bookkeeping | Each retained theorem has a reviewed proof/citation with exact hypotheses; no formula is accepted from a log count |
| **B Computational/reproducibility** | B00 preserve → B01 field encoding → algebra/hull/Gray controls → quantum/route checks → exact28 regression → expressly selected extra rows → table/census provenance → final build | Explicit certificates with form/field/route/basis identities, exact/lower-bound flags and no unapproved search expansion |
| **C Manuscript structure/notation** | CP40 baseline/author gates first; fixed glossary/claim map early; later reconcile labels, method wording, counts, origin/summary claims and declarations; source build only after mathematical/content freeze | One named successor source/PDF, no stale simultaneous declarations or false universal route summaries; old versions unchanged |
| **D Literature/novelty** | Repair citation identities/metadata and scope flags early; verify actual comparator endpoints; after corrected retained parameter set rebuild same-alphabet comparisons; then nearest-theorem claim matrix; exclude P1/P2/P3 promises | No unsupported record, firstness, Q1 guarantee or automatic novelty claim; attributed predecessor hypotheses checked |

## 3. Exact issue dependency DAG

CP IDs refer to [MASTER_CORRECTION_REGISTER.md](MASTER_CORRECTION_REGISTER.md). Table entries are **all** immediate predecessors. Empty means the author/provenance gate. No cycle is permitted.

'''
mapping+=table(['Action','Group / severity','Immediate predecessors'],[[a['id'],a['group']+' / '+a['severity'],', '.join(a['depends_on']) or 'None (first author gate)'] for a in actions])
mapping+='\n\n### One valid topological ordering\n\n'+ ' → '.join(order)+'\n\n'
mapping+='''This is a serialization satisfying the DAG, not a recommendation to treat CP03 and CP35 as equally urgent merely because they occur in one linear list. The proof work packages prioritize the mathematical critical path. Parallel planning/metadata work must not bypass its gates.

## 4. Critical-blocker acceptance dependencies

'''
mapping+=table(['Blocker','Cannot be signed off before','Decisive acceptance record'],[
 ['CP10 hull proof','CP08/09/11/12 and selected CP31 evidence','Reviewed existing witness/proof or explicit narrowed/withdrawn claim; mu and hull certificate'],
 ['CP23 stabilizer','CP22 phase convention','Valid scoped stabilizer lift/isotropy/scalar conditions and quantum review'],
 ['CP24 EA proof','CP23 and CP05','Bob-completed construction and Alice-only error/radical argument, independent commutator tests'],
 ['CP25 route theorem','CP12/16/23/24','R1/SO/DC/EA contract with correct field, label group, orthogonal and distance exclusion'],
 ['CP27 DC quotient','CP25','DC counterexample reconciled without changing a valid K4 tuple to K0'],
 ['CP29 bookkeeping','CP25/27','Per-route symbolic derivations and row-level K/c/budget checks'],
 ['CP32 benchmark','CP20/25/27/29/31/33','Same physical alphabet/resources and retained tuple identity; old invalid gaps withdrawn'],
 ['CP40 author gate','Author-supplied facts, not guessed policy/status','Baseline and actual submission-status confirmation; explicit bounded implementation permission']])
mapping+=f'''

## 5. Conflict/stop conditions

- A later submitted/private source differs from MS03: freeze it, inventory it and revise the plan before editing anything; do not mix theorem bodies between versions.
- A retained tuple differs under the **documented actual encoding**: stop, preserve both results, determine matrix identity and provenance before changing a value.
- A proposed proof needs a genuinely new structural family, twist bridge, size-three classification or Ore compatibility theory: **out of scope**; withdraw/restrict or request separate research approval.
- A benchmark differs only because q or c conventions do not match: do not call it a record or a numerical correction to the construction.
- An author declaration or journal status cannot be verified: leave it **AUTHOR CONFIRMATION REQUIRED**. No editorial message is sent by this plan.
- A final build passes: that does not close mathematical, novelty or submission-policy gates. Require an independent re-audit.

The machine-readable [dependency map](evidence/correction_dependency_map.json) is checked for43unique IDs and acyclicity. Approval state for every action remains **IMPLEMENTATION NOT AUTHORIZED**.

**{STATUS}**
'''
out('CORRECTION_DEPENDENCY_MAP.md',mapping)
with (E/'correction_dependency_map.json').open('x',encoding='utf8') as f:
    json.dump({'status':STATUS,'nodes':[{k:a[k] for k in ['id','audit_id','group','severity','depends_on']} for a in actions],
               'topological_order':order,'critical_blockers':[a['id'] for a in critical],'severity_counts':dict(collections.Counter(a['severity'] for a in actions)),
               'implementation_authorized':False},f,indent=2);f.write('\n')
print('Rendered 3 planning documents; 43 action cards; 8 CRITICAL / 29 MAJOR / 6 MINOR; dependency DAG acyclic.')
