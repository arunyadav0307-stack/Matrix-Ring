# Core A closed-formula finalisation — current status, M8

## Current decision

**Candidate all-parameter derivation supplied and internally scrutinized; fresh regressions PASS. Genuinely independent scrutiny of the complete proof is NOT ESTABLISHED. Under the user's explicit gate, the theorem is NOT marked unqualifiedly “proved”. Novelty is separately NOT CLEARED.**

No mathematical counterexample, failed regression or unresolved mathematical implication was identified in the new internal replay. That is not a guarantee that the argument has no error. It would be misleading either to turn a same-agent reread into independent acceptance or to invent a missing lemma merely to label the stop as a mathematical failure.

This is a **verified internal-scrutiny/reproducibility milestone**, not completion of the requested independent-proof gate or a publication/submission release. The earlier six M5 files and stronger status language remain immutable historical records. The present six versioned successors supersede that acceptance wording for current use without changing the candidate formulas or hypotheses.

## 1. Six requested documents, now versioned together

All paths in this table are in `autonomous_research/AR01/finalisation/M8/`.

|Document|Role|
|---|---|
|[CORE_A_CLOSED_FORMULA_THEOREM.md](CORE_A_CLOSED_FORMULA_THEOREM.md)|Exact candidate T1–T5; all embedded central-length2 right codes, all Frobenius orders, original matrix-valued form; column/matrix counts separated.|
|[CORE_A_CLOSED_FORMULA_FULL_PROOF.md](CORE_A_CLOSED_FORMULA_FULL_PROOF.md)|Self-contained candidate derivation P01–P30, including original-global transport, complete descriptors, trace/fixed-field counts and even-extension graph splitting.|
|[CORE_A_INDEPENDENT_PROOF_AUDIT.md](CORE_A_INDEPENDENT_PROOF_AUDIT.md)|Every proof unit line-indexed; alternative point/plane derivations, adversarial tests and exact independence limitation. **Not** an independent-person certificate.|
|[CORE_A_EXCEPTIONAL_CASES_REGISTER.md](CORE_A_EXCEPTIONAL_CASES_REGISTER.md)|38 endpoint/degeneracy/scope/acceptance records, stable original EX01–EX30 plus explicit M8 additions.|
|[CORE_A_THEORY_COMPUTATION_COMPARISON.md](CORE_A_THEORY_COMPUTATION_COMPARISON.md)|Fresh q16 census and μ1 strata; exact scopes/hashes for all11 runs; q32/q64 geometry-only.|
|CORE_A_PROOF_STATUS_REPORT.md|This controlling current-status report.|

Supporting records: [input inventory](CORE_A_INPUT_INVENTORY.md), [machine proof obligations](CORE_A_PROOF_OBLIGATIONS.json), [separate primary-source assessment](CORE_A_PRIMARY_SOURCE_NOVELTY_ASSESSMENT.md) and [machine gate status](CORE_A_GATE_STATUS.json). Hash/range/link validation is a document-integrity check, not a theorem prover.

## 2. Substantive mathematical work completed internally

The formula and family are unchanged from the verified starting checkpoint `c4f170dffbb6c6a99b7ae2339851ea3d29039022`. The new full derivation explicitly supplies or expands:

- Localness of B and the nilpotent Nakayama premise, not just J³=0.
- Both original cyclic-shift coefficient tests and the actual right-column matrix pairing; no convenient substitute form.
- The distinction between the auxiliary [uw] Frobenius functional used for dimensions and the actual global [u]trace scalar companion c_u+c_uw. Equal submodule orthogonals do not mean equal scalar forms.
- Unique embedded radical extension data (K,T,f) and primitive ideal/coset descriptors, including the vertical chart and I=J.
- The **positive** law D_s²=σ_(2s), not assumed reflexivity for arbitrary σ.
- The correct **left-annihilator hyperplane for a right radical**, Ω(x,ℓ)=0; explicit nonreflexive counterexamples prevent exchanging it with Ω(ℓ,x)=0.
- Arbitrary-order isotropic point counting via scaled trace hyperplanes, with a separate character-sum derivation.
- Exact σ²-fixed-field descent and ordinary involutive geometry **only after descent**.
- Even-order incidence correction through a graph splitting lemma that works when [k:E] is even; non-graph charts, zero coefficients, infinity and the Artin–Schreier trace normalization are explicit. A second semilinear-descent/plane-type derivation gives the same incidence count.
- Every generator-number alternative, disjoint μ1 stratum and expanded N2 assembly, including s0/order2/non-involutive odd/even orders.

All30 units were internally replayed against hypotheses/directions and dependencies. The [audit](CORE_A_INDEPENDENT_PROOF_AUDIT.md) records the exact statement/proof hashes and line ranges. No quantum/Gray/physical, larger-rank/nilpotency/length, joint same-input histogram, freeness or ambient-GL equivalence is inferred.

## 3. Fresh executed evidence

|Evidence|Actual result|Limit|
|---|---|---|
|Full q16 generic/structural census|**PASS:166,521 inputs ×4 twists =666,084 complete hull-space comparisons**. Every marginal and μ1 input stratum agrees.|Descriptor-based exhaustive census, not every ambient subspace and not a full original-global census.|
|Full small-field structural census|PASS:41,580 q2/q4/q8 input/twist cases.|Includes159 auxiliary q2 cases outside m≥2.|
|Separate all-T geometry|PASS:334,413 cases at q4/q8/q16.|Width4 layer geometry, not another full B² enumeration.|
|Original-global route|PASS:all2,442 q4 cases;176 selected q16 cases;4,608 product/shift basis tests;other explicitly named foundational/family controls.|Same q4/q16 sets recur in several drivers; do not add them as distinct codes.|
|q32/q64|PASS for selected projective-point/trace/descended-plane geometry only.|q32 s1–4; q64 s1,2,4,5. No full module census or untested twist coverage.|
|Scalar A-valued QC route|PASS:same2,442 q4/176 q16 complete-space sets;176 exported duals;1,152 basis/shift tests.|Shares alternative field/row/global helper; not a field/Gray isometry.|
|New standalone directed scrutiny|PASS:101,316 actual two-plane flags;304 Hermitian graph matrices;four explicit wrong-direction witnesses.|No repository-code imports, but still same-agent finite verification, not independent complete-proof acceptance.|
|Foundational negatives / larger-length boundary|PASS:q2 arbitrary-subspace filter,actual functional/side controls and41 named split original-global boundary cases.|Outside-family cases guard scope; do not extend the theorem.|
|Exact identities / integer regressions|PASS:5 exact identities;2,080 integer pairs m1…64;expanded N2 assembly checked separately.|Not field/module censuses or a formalization of all geometry.|

Ten unchanged-driver reruns generate39 files byte-identical to their deterministic predecessors. One new standalone run generates four more files. All have fresh refused-overwrite labels. Sources and old outputs are preserved. Exact hashes and dependencies are in [M8_REGRESSION_COMPARISON_V1.json](../../evidence/M8_REGRESSION_COMPARISON_V1.json), each result summary and the theory/computation comparison.

## 4. Explicit independent-scrutiny blocker

**RB01 — complete-proof independent mathematical acceptance: OPEN.**

The exact candidate statement/proof hashes are in the audit and machine obligation ledger. An independently attributable reviewer, or an appropriately complete formal derivation, must validate **the entire implication chain P01–P29**, not just the numerical formulas. Critical review targets are:

1. Original-global/module correspondence and semilinear dimension/double-dual laws, P03–P05.
2. Exhaustive embedded descriptors and every generator-number/counting alternative, P06–P18.
3. Arbitrary-order trace point count, right-radical flag subtraction, fixed-field descent and odd/even relative-incidence counts, P18–P26.
4. Exact assembly, endpoint coverage and interpretation, P27–P29.

Any objection must be resolved against the versioned argument and the independently reviewed exact version identified. No second independent researcher/referee or complete proof-assistant certificate exists in the available evidence. Separate derivations, no-import software, integrity checks and commits cannot self-issue that acceptance. No external review/contact/acceptance is invented.

**Nature of this blocker:** verification evidence, not an established mathematical counterexample or an unproved lemma identified inside the current candidate. The requested independent-proof terminal condition is therefore **not claimed reached**. The available work is preserved and made reviewable rather than reported as a completed theorem-proof gate.

## 5. Novelty is an independent open gate

The separate [primary-source assessment](CORE_A_PRIMARY_SOURCE_NOVELTY_ASSESSMENT.md) freshly verifies the identity and bounded hypotheses/form scope of the supplied S10 primary article. Its coprime-length condition excludes a direct specialization to characteristic2,length2, but does not establish a literature gap. Prior primary/preprint readings retain their exact version limits.

Nine new bounded allowed-host queries and two hashed acquisitions yielded only secondary/mirrored leads, not the missing authenticated closest-source bodies. Full S01 scalar repeated-root tables, S09 same-nonchain-ring QC statements and the specific primary Hermitian/quadric relative-incidence results remain unverified. Required obligations NL01–NL04 are explicit; no search/access failure counts as novelty.

Matrix packaging is not the candidate contribution: the whole problem is exactly scalar A-valued length4/index2 QC with the module-generator invariant dim H/[uH+(τ+1)H]. The potential residual contribution is the all-input closed marginal aggregation if authenticated comparison leaves a sufficiently deep distinct result. It may be known or routine; no-paper remains a valid outcome. No Q1/journal, application, final manuscript, declaration or submission gate is closed.

## 6. Request-by-request disposition

|Requested requirement|Current disposition|
|---|---|
|Locate/inspect candidate formulas, drafts, census and original-global audits|Complete bounded inventory:166 frozen AR01 inputs,12 precursor content groups/93 paths; technical versus locator reading scopes explicit.|
|Rigorous all-parameter derivation including non-involutive twists/fixed-field incidence|Candidate derivation supplied and internally replayed, with expanded assumptions and two central routes.|
|Independent line-by-line proof scrutiny|**NOT ESTABLISHED**. Complete same-agent line audit supplied; it is not falsely relabelled independent acceptance.|
|Resolve logical gaps/exceptions/unstated assumptions|All identified internal obligations resolved/explained; no counterexample or unresolved implication identified internally. Independent objections remain possible.|
|Compare exhaustive q16; keep q32/q64 geometry-only|PASS with a fresh full q16 rerun; exact higher-field limit retained.|
|Six required documents|Versioned successors supplied above; original six untouched.|
|Separate verified-primary novelty assessment|Separate, precisely scoped comparison supplied; **clearance OPEN**, with missing primary technical obligations recorded.|
|Relevant regressions preserving old results|PASS:10 fresh reruns plus1 new standalone run; no old results/sources overwritten.|
|Commit/push/remote files/logs and research ZIP|Integrity and synchronization receipts record actual completion separately; pre-commit pending wording is not a push-success claim.|
|Do not claim proved/novel prematurely|Enforced:both acceptance gates remain open. No mathematical blocker or external acceptance is fabricated to force a positive/terminal result.|

## 7. Preservation and synchronization provenance

The task began on verified c4f170d, already containing M7 payload `bab5774` and its completion receipt. All historical checkpoints—including original `a74f33f`—remain unchanged ancestors. No branch change, force-push, deletion or history rewrite is used.

The166-file M8 baseline and2,059-file original-intake manifests are checked. Only append-only progress/readme additions are allowed among old paths; all old six documents, computation sources/results, primary evidence and seven old checkpoint ZIPs remain byte-identical. A fresh deterministic bounded research ZIP is reopened, its manifest and each payload verified, and recorded separately. It is a research backup, not a submission package.

At this report's pre-commit creation, the payload commit/push is **not yet asserted complete**. A later append-only synchronization addendum and remote receipt supply actual commit/ref/tree/file checks without a circular self-hash. New wall-clock timestamps are labelled raw sandbox observations rather than normalized session or publication dates; earlier discrepant date fields are not rewritten.
