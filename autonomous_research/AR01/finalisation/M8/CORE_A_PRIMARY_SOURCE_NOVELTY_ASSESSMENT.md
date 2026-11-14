# Core A — separate primary-source overlap and novelty assessment, M8

## Decision

**Novelty and sufficient paper depth: NOT CLEARED.** This is separate from whether the candidate derivation is mathematically correct. No firstness, Q1/journal suitability, submission-readiness or external-review claim is made. A search failure, a locally written proof, different notation, a passing census and a verified Git hash do not establish novelty.

The task continues from `c4f170d`. Existing source notes, PDFs, reading scopes and M5/M6 assessments remain unchanged. This successor corrects any reading of their “proved research output” wording as satisfying the user's renewed independent-scrutiny requirement; it does not erase historical observations.

## 1. What is actually primary evidence here

### S10 — supplied published-article PDF, locally verified exact artifact

Representative: `phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/literature_evidence/supplied_pdfs/s13226-021-00014-x (2).pdf` from the repository root. SHA-256 **`0679c4a6077b8477e8d325737b8efc8d3d96b9f8f356be6b8edaa06d6a26f989`**;9 pages. The first-page header identifies Habibul Islam, Om Prakash and Dipak Kumar Bhunia, *On the structure of cyclic codes over M₂(F_p+uF_p)*, and its DOI/title identity is recorded in the inherited primary reading notes. The corrected supplied extraction is `phase0_audit/pdfs_text/s13226-021-00014-x_2.txt`.

**Fresh bounded technical inspection:** extraction lines1–27,140–170,244–295, plus exact first-page PDF header. The inherited complete378-line reading remains an earlier, separately described scope; it is not relabelled as a new complete M8 reading. The locally available preserved pypdf6.1.1 extractor was found and used read-only; lack of a globally installed extractor did not make the supplied PDF inaccessible. Text has visible encoding artifacts; no new formula-level certification of the whole paper is inferred.

What that primary text actually supports:

- Its standing field parameter is a prime p with p≡2 or3 (mod5).
- From §3 onward it explicitly assumes gcd(N,p)=1; Theorem2 states this condition.
- Its §4 prints the untransposed product Σc_i c′_i as its Euclidean form; this is not automatically the present first-slot coefficient-Frobenius transpose convention.
- Matrix-ring cyclic-code structure and transport are occupied territory. They are not new merely because the present notation uses B or column μ.

For Core A, characteristic2 and central length2 give p|N. Therefore that literal coprime-length theorem cannot simply be specialized to certify the present all-input repeated-root histogram. **This is a hypothesis mismatch, not proof that its methods or later work do not imply the result.** The unread erratum `10.1007/s13226-021-00142-4` and exact final/corrected-version relation remain open; they are not silently filled in. The article is treated as a supplied primary technical artifact of exact known bytes, not as a freshly downloaded publisher-certified final version.

### Other locally supplied primary artifacts

[M8_LOCAL_PDF_SCOPE_V1.json](../../evidence/M8_LOCAL_PDF_SCOPE_V1.json) inventories **10 distinct PDF hashes**:9 returned page-count/metadata records (8 also returned nonempty first-page header text); one archived draft `PAPER/main.pdf` extraction failed with `list index out of range` and has **no technical reading** claimed. The inventory includes a blueprint and alternate copies, not10 newly reviewed literature articles. Successful first-page/metadata inspection is distinguished from technical reading. S06's supplied QIP PDF has hash `beb31f56d58a88d9674d86700390a5e0bc4faddc0eadf787f06c6a1ccd32bb8b`; only its header was freshly inspected in this inventory. Its prior selected-page reading and font caveats are not upgraded to a full-paper theorem comparison. PDF extraction warnings are not evidence that an article is false.

### Previously inspected primary technical versions, not newly reauthenticated

The exact earlier preprint/publisher scopes for S01–S10 are preserved in [PRIMARY_SOURCE_READING_NOTES.md](../../phase1/PRIMARY_SOURCE_READING_NOTES.md). In particular:

|Lane|Positive earlier primary evidence|Still missing|
|---|---|---|
|S01 / NL10, Cao–Cao–Fu, scalar repeated-root cyclic hulls over F_(2^m)+uF_(2^m)|Indexed preprint §5 locators and metadata for arXiv:1910.02237 / DOI10.1007/s00200-019-00408-9|Complete authenticated technical tables/proofs/dependencies and final-version comparison|
|S09, same nonchain-ring one-generator QC theory, DOI10.1007/s11128-024-04514-7|Publisher preview/abstract scope only|Full theorem/form/module-generator/specialization comparison|
|S02, Galois hull generator polynomial matrices|Specified preprint statement/proof portions of arXiv:2305.15237v1; occupied generic generator infrastructure|Full final technical-version equality and relevant enumerative consequences|
|S03, intersections of linear/multi-twisted codes|Specified primary preprint intersection/hull matrix theorem portions|Any final-version/enumerative comparison; inverse twist for translating its second-slot convention|
|S04, Ore/matrix selfdual transport; S05, Artinian invariants|Specified primary preprint portions; transport, μ/type/top dimension and ordinary duality are existing infrastructure|Exact assumptions/version issues and any directly relevant all-input counting specialization|

No missing complete S01/S09 article or missing primary geometry table is asserted to have been obtained in M8. The previous primary observations are not automatically evidence that every theorem in the final publications was read or excludes Core A.

## 2. Fresh allowed-host searches and what they did not establish

[M8_PRIMARY_SOURCE_SEARCH_V1.json](../../evidence/M8_PRIMARY_SOURCE_SEARCH_V1.json) and [M8_PRIMARY_GEOMETRY_REFINEMENT_V1.json](../../evidence/M8_PRIMARY_GEOMETRY_REFINEMENT_V1.json) record **9 actual bounded GitHub code queries**, first5 results per query. Exact identity/refinement searches were used for S01, S09 and the Hermitian/quadric intersection lead. All accesses stayed on allowed GitHub hosts; no author/editor contact, payment, login workaround, Drive access or submission occurred.

Two actual acquisitions are pinned in [M8_SOURCE_ACQUISITION_V1.json](../../evidence/M8_SOURCE_ACQUISITION_V1.json):

1. Third-party mirrored TeX `editable-corpus/sources/201507/source0.tex`, Git blob `3d9f458f7c77552abf498b1d6f280fd441460b51`. Its header/abstract, lines108–148, name Jitman/Boonsuriyatham and *Good Integers: (T,k)-Subclasses and Applications to Galois Duality in Coding Theory*. A section/keyword inventory identifies finite-field cyclic-code/Galois-duality applications, including repeated roots. No complete coding-theorem/proof reading or primary/final authenticity was established; it cannot clear or defeat the exact nonchain QC histogram claim merely by its title.
2. Third-party BibTeX file `crypto_DCC14.bib`, Git blob `3752c218a2646591c0ea87f249ee1fa4e7749ded`. The complete entry at lines1863–1876 reports Bartoli–De Boeck–Fanali–Storme, *On the functional codes defined by quadrics and Hermitian varieties*, DCC71(2014),21–46, DOI10.1007/s10623-012-9712-4. This is **secondary bibliographic metadata**, not authenticated primary technical text or proof/table verification. Exact DOI refinement found bibliographic copies, not the required full article.

Git blob SHA-1 was recomputed from each retrieved byte sequence and SHA-256 recorded. That authenticates content identity at the recorded GitHub revision, **not** an author's approval, publication identity/version equality or scientific truth. Caches are disposable/excluded from Git; receipts retain immutable retrieval locators. No new primary closest-result body was acquired. The unrelated Hodge/black-hole search results are not coding or finite-field-geometry evidence.

## 3. Exact mathematical translation that a novelty comparison must respect

The unchanged [scalar-QC crosswalk](../../phase1/A13_SCALAR_QC_REDUCTION_AND_CLOSEST_RESULT_COMPARISON.md) gives

W≤B² ↔ A-linear length4/index2 QC codes Q,
A=k[u]/u², B=A[X]/(X²−1),
C=I_W ↔ Q×Q,
C∩C^(⊥s) ↔ (Q∩Q^(⊥h_s))²,
h_s(a,b)=Σσ(a_i)b_i valued in A,
μ_B(H)=dim_k H_Q/[uH_Q+(τ+1)H_Q].

This is exact original-global hull transport for every σ, not a Gray/field/physical isometry. Both constant and shift tests are essential. Matrix generators are only ceil(μ_B/2). One-generator QC (μ_B≤1), matrix-principal (μ_B≤2), A-linear generator number and free rank are not the same predicate. The full family includes μ_B4 inputs. A direct sum of scalar B ideals does not exhaust it: B(1,1) already couples the coordinates. Conversely that distinction is **not** evidence that existing QC/module theory does not already imply the aggregation.

The finite geometry to compare is also precise:

- Ω_s((a,b),(c,d))=σ(a)·d+σ(b)·c may be nonreflexive on k.
- Its self-dual two-planes descend to E=Fix(σ²), where the form becomes alternating or Hermitian.
- U subtracts rank1 points of the fixed Segre quadric Δ=a₁b₂+a₂b₁ from the actual Ω_s-isotropic point count.
- F is the **rank2 point / self-dual-plane incidence count**, not merely a surface point count.
- At E=F_(Q²), the base rank1 point count is (Q+1)(2Q²−Q+1)=2Q³+Q²+1, literally a Hermitian-surface/Segre-quadric intersection. Functional-code intersection tables are therefore substantive comparison targets, not irrelevant geometry.

The earlier M6G1/M6G2 mirror portions show positive classical plane/point overlap, but remain unauthenticated primary versions. The symplectic/Hermitian plane products, trace/norm linear algebra, Morita dictionary, Nakayama invariant and generic intersection algorithm are **not claimed new**. No Hermitian polarity is applied on all k in a non-involutive regime.

## 4. Claim-by-claim current disposition

|Candidate component|What can responsibly be said now|
|---|---|
|Original matrix/column/QC packaging and ordinary generator invariant|Conventional infrastructure and existing territory; not a standalone contribution.|
|Principal-input preservation at central length2|Short elementary argument retained; not selected as sufficient paper novelty. The impossible counterexample search stays rejected.|
|A12 moving split-factor witness|Exact scalar reduction already supplied; useful boundary, rejected alone as a sufficient original result.|
|Arbitrary-Frobenius point count and fixed-field incidence lemmas|Candidate derivations internally replayed with different routes. Classical ingredients/possible prior relative-incidence coverage remain to be checked against authenticated primary results.|
|Complete all-input marginal μ histogram|Strongest developed candidate, but exact prior all-generator scalar-QC coverage and sufficient research depth are UNKNOWN. No claim that it is either new or already known.|
|Independent proof acceptance|NOT ESTABLISHED; source overlap assessment is not an independent proof certificate.|
|Paper, journal/Q1, quantum application or submission|NOT selected/certified. No-paper remains legitimate if authenticated comparison shows the result known, routine or insufficiently deep.|

## 5. Precise remaining source obligations

**NL01:** obtain/verify S01's complete scalar repeated-root technical tables/proofs and any all-generator module/QC consequences, then translate the exact A-valued form and radical-quotient generator statistic.

**NL02:** obtain/verify S09's full text, permitted block-length specialization, generator threshold and actual pairing/Frobenius convention; do not substitute an abstract for this comparison.

**NL03:** authenticate/read the specific Hermitian/quadric intersection and line-type results (Bartoli–De Boeck–Fanali–Storme; the identified Edoukou/Bose–Chakravarti leads), then compare U, F and arbitrary-order descent precisely. A bibliography entry or total point intersection alone does not settle the line-incidence formula.

**NL04:** reconcile load-bearing preprint/final technical versions where equality is not established. Do not invent theorem numbers, final-text coverage, DOIs not evidenced, firstness or publication status.

The available tools/sources have not discharged these obligations. Access limits block **novelty clearance**, not the logical validity of a self-contained mathematical argument. More finite fields or cosmetic scope expansion cannot replace primary evidence. [Current status](CORE_A_PROOF_STATUS_REPORT.md) separately records the incomplete independent-scrutiny gate and the work that actually passed.
