# Computational and reproducibility repair plan

**Recorded planning execution:** 2026-11-13 UTC (workspace clock).  
**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**

## 1. Group B scope: proposed verification, not new executions

**No scientific script was run in this correction-planning task.** The current operations are source reading, version/hash inventory, evidence copying, action/dependency validation and delivery-integrity checks. No field-code record, script, log, certificate, manuscript or original archive was edited; no TeX compilation or new code search was performed.

The B00–B08 gates below are proposed for a separately authorized, bounded correction pass. **Every scientific gate is NOT RUN / NOT AUTHORIZED in this task.** Existing independent-review results remain historical evidence, not newly executed tests. B00's preservation inventory and this delivery's integrity checks are planning safeguards, not scientific repair results.

Baseline: **MS03**, the full recovered `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/` root, pending author confirmation; source-set SHA-256 `b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24`. Input identity must be rechecked after the author identifies any later/private/submitted revision. See [source identification](AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md).

## 2. Existing evidence — preserve without overstating it

| Existing execution/validation | Actual scope and outcome | What it does not establish |
|---|---|---|
| Original-source feasibility rerun | Exit 0; historical finite feasibility results; 32.460 s in the independent review | All later theorem/proof correctness |
| Original Gray script rerun | Exit 0; **463 assertions =311 EXH+152 SMP**; archived log reproduced byte-identically, SHA-256 `55656a9da040df99e0d577ecb4f22c079bf9abd7b377c98eace31bca107c9a92` | 463 codes, universal proof, all ambient pairs, all CSS routes |
| Original generator reconstruction | Exit 0; **28 records + INDEX.json** byte-identical; 616.785 s in the independent review | An independent implementation or the entire historical search census |
| Separate independent arithmetic | 17 core assertions, 7 follow-ups, 5 scope checks; last scope check explicitly reproduces a source bug on disposable copies | 29 new universal theorems or repaired proofs |
| Independent 28-record recertification | **25 EA+2 SO+1 DC**; exact distance by 24 complete enumerations+4 complete support searches; correct actual field encoding | Optimality, priority, all headline/wild/R1 rows, all 120,721 scans or 5,055 distance results |

See the copied [run summary](evidence/audit_reports/evidence/included_source_run_summary.json), [28-code JSON](evidence/audit_reports/evidence/independent_28_code_checks.json), [28-code CSV](evidence/audit_reports/evidence/independent_28_code_summary.csv), [focused controls](evidence/audit_reports/evidence/critical_followup_checks.json), [remaining scope checks](evidence/audit_reports/evidence/remaining_scope_checks.json) and [Gray audit](evidence/audit_reports/GRAY_MAP_EVIDENCE_AUDIT.md). Historical times are observations, not promised runtimes for a future pass.

## 3. Safety contract for a later authorized pass

1. Freeze source/data hashes and preserve every original. Use a **new approved successor/test directory**. Do not run historical scientific scripts in place: several write adjacent logs or caches.
2. Use disposable input copies, `python3 -B` and `PYTHONDONTWRITEBYTECODE=1`. A copied generator reconstruction needs `MATRIX_RING_COMP` set to the **absolute copied script directory**. Do not point it at frozen originals.
3. Keep original arithmetic, independent arithmetic and a corrected successor implementation separate. A rerun of the same algorithm is not independent recertification.
4. Preserve failed attempts/negative controls with clear authoritative-v2 or later-successor status. Never overwrite an old result to make an aggregate PASS.
5. Set explicit case lists, budgets and stop conditions before launching. Default scope is the existing 28 records, existing focused controls and only the additional manuscript rows explicitly retained by the author. **No new family search, exhaustive historical rerun, Phase1 or P1/P2/P3.**
6. Record exact versus lower-bound results. Exhausting a partial support budget does not prove the distance; a skipped algorithm is not a completed check.
7. Scientific equality and byte identity are different. Date/timing changes may alter bytes without changing computed values; record both comparisons.
8. A test can diagnose a false claim or check a finite certificate. It cannot repair a universal proof, establish novelty, resolve author declarations or prove actual submission status.

## 4. Proposed bounded gates

### B00 — Input identity, preservation and execution envelope

**Actions:** CP40, CP42, CP43; prerequisite for every other future gate.

- Author confirms MS03 or supplies the exact later source/PDF and status facts. Re-inventory instead of merging variants by intuition.
- Record entry/core hashes, data-tree hash list, branch/HEAD, environment/dependency versions, planned commands and exclusive output destinations.
- Current planning preservation baseline: **1,959 pre-existing files / 106,136,867 bytes**, captured at `2026-11-13T08:19:29.687083+00:00` in [pre_plan_snapshot.json](evidence/pre_plan_snapshot.json). A future implementation pass must capture its own baseline, not modify this one.
- Require all retained literal inputs to resolve in the **complete** source root. Audit delta directories are not standalone build roots.

**Acceptance later:** approved input/scope record, pre/post original-file comparison, exclusive new outputs, no out-of-scope writes. Current final preservation results will be reported separately in this plan's delivery evidence. **Stop** on any unexplained original-file change, branch mismatch or later-source conflict.

### B01 — Actual finite-field encoding and generator identity

**Actions:** CP20, prerequisites for CP11/15/22/31/32.

| Field | Actual producer/decoder | Modulus for integer polynomial labels |
|---|---|---|
| GF4 | `ring_structure_checks.Field` | `x²+x+1` |
| GF8 | `ring_structure_checks.Field` | `x³+x+1` |
| GF9 | `ring_structure_checks.Field` | `x²+1` |

- Freeze all **28 existing matrix records plus INDEX** without relabelling integers. Document the little-endian coefficient basis and arithmetic implementation actually used.
- Compare project arithmetic with an independent implementation on these fixed fields; include additive/multiplicative identities and inverses.
- Retain the existing wrong-documentation negative control: decoding the 15 q8/q9 records using the older library labels caused **5 dual-matrix mismatches**. Do not mistake an abstract field isomorphism for identity of integers.
- Safest correction is documentation/decoder provenance, **not** a matrix migration. A basis migration would require extra approval and complete explicit conversion verification.

**Acceptance later:** unchanged matrix identities, exact basis/modulus contract, independent arithmetic agreement and correctly interpreted negative control. **Stop** on a mismatch under the actual encoding before changing any parameter or certificate.

### B02 — Pairing, cyclic closure, duals and convention controls

**Actions:** CP01–CP06, CP08, CP12, CP17; supports WP-A1/A2.

**Fixed starting controls from existing audit evidence:**

- Wrong `ax` action versus the correct right action; invalid matrix-unit probe versus valid nonzero-coordinate/identity probes.
- Plain-product elementwise nondegeneracy versus the correctly specified same-sided size failure.
- Nonmodule scalar/ring orthogonal mismatch (dimensions 2 and 3), alongside actual right-module equality.
- F8 positive double twist versus negative twist and versus `C`; a separately typed alternate-left convention if it is retained at all.
- Per-code invariant and noninvariant cases in a globally nonreflexive regime.

**Additional bounded review checks, only for retained manuscript claims:** constant right multiplication and cyclic shifts on selected small explicit modules; scalar/ring orthogonals; correctly sided annihilator/reversal formulas at named `n≥3` examples and zero/full cases. Check actual subspace equality, not only dimensions or cardinalities. Do not attempt a new global search for a principal-dual classification.

**Acceptance later:** exact rings, module bases, slot/side, coefficient Frobenius, dual bases and memberships in each certificate; separate proof review for universal claims. A finite PASS does not validate the printed convolution or full-Hom-surjectivity argument.

### B03 — Morita rows, torsion, mu and retained hull witnesses

**Actions:** CP07–CP11, CP31; supports WP-A3.

- Keep the existing 33-submodule base-ring regression separate from a general principality proof.
- Retain a torsion/nonfree control; never equate field rank or “submodule of free” with freeness/generator number.
- Assert row widths and coordinate contracts at every conversion: full image rows, two-column Morita rows, intersection basis and radical generators.
- Reproduce the known Phase5 Task-D3 wrong-representation control (**wrong mu4 versus correct mu3**) using copied sources. Compare with the already documented Phase6 `hull_mu` route; never patch the historical script/log in place.
- Recheck the earlier explicit `(4,2,2)` self-dual witness: actual module/hull, radical, generator count and both recorded twists. Separately retain the failed direct-sum family as a **negative** control (intersection1, sum-dimension5, radical-dimension3, mu2).
- Any extra `(9,2,3)`, `(4,2,4)` or other wild witness is **not** automatically included. Author selects it under CP31; require an explicit basis and a bounded full certificate or remove/qualify the claim.

**Acceptance later:** basis identity, right closure, computed dual/hull/intersection, radical containment and independent generator number; no randomized-generator-failure proxy. New generic families or new classification are out of scope.

### B04 — Gray ordering, form type, congruence and evidence quantifiers

**Actions:** CP13–CP19, CP26; supports WP-A4.

- Verify the actual coordinate order and `J=I⊗H_t` against direct matrix/top-coefficient evaluation on the existing small cases; compare transported and actual Euclidean duals separately.
- Retain the ordinary-Euclidean counterexample and explicit F4 Hermitian-congruence control. Check `TᵀHT` and `sigma(T)ᵀHT` **separately**; neither identity alone implies a Hamming isometry.
- Retain the odd-characteristic bilinear and characteristic-two Hermitian self-value controls for the overbroad alternatingness clause.
- Check the displayed GF9 transformation in its actual encoding, orientation and form type. If a transformation is used for a retained example, certify the transformed physical-coordinate distance rather than assuming it is preserved.
- Reconcile the reflexivity diagnostic: historical line982 header is tautological; actual line1026 C5 condition is correct. Do not relabel all C5 tests as tautologies.
- Audit/log actual EXH/SMP quantifiers: **311/152 labels**, pair caps **120²/50²**, seeds and negative-control meanings. Complete ambient enumeration is not complete pairwise enumeration.
- Default correction testing is targeted. A full rerun of the 463-assertion source suite is an **optional explicitly approved regression**, on disposable copies, not a new search and not already run now.

**Acceptance later:** exact map/form/metric contract, independent basis/control calculations and truthful assertion-scope labels. No automatic Gray-to-Euclidean/CSS or Galois-hull-to-EA substitution.

### B05 — Quantum phases, route contracts, Bob checks and relative distances

**Actions:** CP22–CP29, CP31; supports WP-A5–A8.

**Bounded tests:**

1. Direct small operator-action tests at `p=3`, with GF9 absolute-trace cases and characteristic-two controls; verify the adopted sign convention consistently.
2. Existing nonisotropic stabilizer negative control; phase/lift/scalar checks on selected small `p=2` and `p=3` examples. No large Hilbert-space simulation is proposed.
3. For retained EA records, Gram rank, actual `h_E`, Bob cross-commutator cancellation, dimensions and Alice-only relative target/exclusion. Distinguish finite arithmetic from the universal construction proof.
4. Actual ordinary-Euclidean SO/DC inclusions; R1 `Fp` trace-orthogonal versus `Fq`-value orthogonal controls. Do not infer equality from equal dimensions.
5. Mandatory DC record `03_20_4_4_4_(4,1,5)_DC.json`: reconcile valid `N20,k12,h8,K4,c0,d4` with the manuscript's zero-dimensional wrong quotient. Check the correct route object without changing the valid tuple to K0.
6. Mandatory R1 bookkeeping counterexample `N8,k4,K4,c0`, and DC `K−c=4` versus `N−2k=−4` under the original-input convention.
7. Existing F2 coset representative-weight control (weights1 and3 in the same coset); actual quotient dimensions and relative distance for retained routes. Finite controls do not refute the audit's conditionally valid restricted Singleton inequality or prove it universally.

**Acceptance later:** a written route contract, independent proof/citation review, explicit form/field/label-space/orthogonal/excluded-space certificates and correct exact/lower-bound distance semantics. Stop if a route must be changed beyond the approved correction scope.

### B06 — Existing 28-record regression, extra-row gate and table lineage

**Actions:** CP19, CP21, CP30, CP31, CP37, CP43.

- Reconcile the **existing 28 records only** using independent arithmetic under B01 and the B05 route contract: rank, Euclidean dual, `h_E`, SO/DC inclusion, EA `K,c`, exact relative distance. Use complete enumeration or complete increasing-support exclusion through the attained distance, as appropriate; record the actual method.
- Preserve the historical certification split: **M1 exact24; M2 fallback exact4; M3 exact11/lower17; 0/28 all-three**. A lower-bound M3 is not a second exact distance algorithm. MS03 already states this more accurately and must not regress.
- Build a provenance ledger from retained manuscript rows to generator basis, field encoding, ring-origin evidence, route, historical log, exact/lower certificate and independent-check scope. A row may have a valid field tuple but unverified ring-origin narrative.
- Extra wild/headline/R1 rows require an **author-supplied named retain list** and explicit computational budgets before work. Without that decision, qualify/remove rather than infer certification from the 28-record pass.
- Reconcile inherited aggregate counts such as 120,721/5,055/4,418/637 using existing source/log/census semantics, not an unapproved rerun. Distinguish scanned, exact, sampled, blocked and counted-only families.
- Inventory the four already supplied q8 EA records; no “first q8 EA” search or P1 implementation.

**Acceptance later:** one unambiguous row-to-evidence ledger; no unsupported optima/frontier claim; all retained extra rows either certified within scope, explicitly lower-bound-only, or withdrawn. Independent full historical-census recertification is **not** the default plan.

### B07 — Same-physical-alphabet benchmark verification

**Actions:** CP32–CP33; coordinated with Group D.

For only the retained tuples, capture query URL, retrieval time, returned physical alphabet/header, `N,K`, stabilizer/EA type, entanglement convention, lower/upper bounds, source citation and comparability decision. Save actual primary returned content when access permits; reviewer notes must not be relabelled as raw captures.

**Starting historical audit controls, not fresh queries in this task:** legacy query q4 returned physicalq2; q9 returned physicalq3; q16/N20/K4 returned **physicalq4,7..8**; q64/N12/K4 returned **physicalq8,5..5**. The actual EA front end exposes qubit/qutrit non-catalytic-c tables; it does not automatically compare q4/8/9 EA records. A failed q81 query establishes only that no comparable bound was obtained there.

**Acceptance later:** matching physical resources and correctly interpreted lower/upper information; retire incompatible old record/gap/ratio labels. Construction tuples are not changed solely because an old comparator was wrong. If primary access is unavailable in the authorized environment, obtain author-provided source captures or leave the comparator unverified—do not fabricate a replacement table.

### B08 — Citation/build/manifest checks and independent closure audit

**Actions:** CP17, CP30, CP34–CP36, CP38–CP43; final Group C consistency gate.

- Static citation and identity check for the retained bibliography; no guessed names/DOIs or placeholder-to-publication invention.
- Resolve literal inputs, labels, citations, cross-references, theorem dependencies, table-to-row provenance and exact source-set manifest in the approved successor.
- State the file-count basis: current tree88, nonmanifest86, publication entries87, historical footprint86 are different bases. Verify the exact future referenced tree, not a mixed total.
- Keep author-proposed data statements, pending editorial confirmation, licence and declarations distinct. Do not remove author-only pending markers by automation.
- **Only after separate implementation/build approval and content freeze**, compile and visually check the successor. Record engine/tool versions, warnings, PDF/source digests and rendered formula/table/declaration checks. A new PDF is not a recovered old or submitted PDF.
- Obtain a fresh independent mathematical/parameter/literature review, with explicit closed/restricted/withdrawn/unresolved states for all43 actions. No automatic GO from a successful build.

**Acceptance later:** approved-source artifact, qualified dependency closure, unchanged historical material, reviewed retained claims and author decisions. Publication, deposit/release, journal contact, submission, Git commit or push need their own authorization.

## 5. Minimal future certificate schema

A later result should record: CP/B identifiers; command and implementation type (original/independent/successor); input paths/hashes; field polynomial/basis; coordinate order and row shape; module side; form/Frobenius/trace; route and actual target/exclusion; seed/case list/budget; exact/lower-bound/skipped state; numerical result and certificate; comparison to inherited evidence; environment/date; stdout/error paths; preservation result; reviewer acceptance. These are required metadata, **not new certificates produced now**.

## 6. Cost and authorization controls

Proof review precedes dependent numerical interpretation. Start with existing small controls, then the 28-record regression, then only explicitly retained extra rows; source-pipeline reruns are optional independent decisions. A budget exhaustion, inaccessible source or need for new structure triggers **STOP / QUALIFY / REQUEST APPROVAL**, not silent scope expansion. No timing in the historical table is a commitment to a future runtime.

See [AUTHOR_APPROVAL_CHECKLIST.md](AUTHOR_APPROVAL_CHECKLIST.md) for the decisions needed before any of B01–B08's scientific work. Plan-package integrity checks do not execute these gates.

**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**
