# Mathematical proof repair plan

**Recorded planning execution:** 2026-11-13 UTC (workspace clock).  
**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**

## 1. Purpose, baseline and limits

This is **Group A**, coordinated with Groups B–D in the [dependency map](CORRECTION_DEPENDENCY_MAP.md). It specifies proof obligations and safe restrict/withdraw alternatives; it supplies **no replacement theorem, proof or manuscript section**. Every package below is **NOT STARTED / NOT AUTHORIZED**.

The exact target is the complete recovered **MS03** source root, `phase0_audit/extracted/prior_project/PAPER/FFA_FINAL_SUBMISSION_V2/`, **subject to author confirmation**. Its `main.tex` SHA-256 is `8c4f53380f8677e425a639a87fc3294fefc21bdac33fa4df2f8d8db4b9f156c0`; its 14-file source-set digest is `b52028fac20c3d4603cfd8e2c44d6d885003ae444098437223a9c71875ac3e24`. See [source identification](AUTHORITATIVE_MANUSCRIPT_IDENTIFICATION.md) for all versions, hashes and timestamps. Neither the historical canonical manuscript nor an audit delta directory is an authorized editable baseline.

The evidence is the existing independent [claim ledger](evidence/audit_reports/MATHEMATICAL_CLAIM_VERIFICATION.md), [pairing audit](evidence/audit_reports/PAIRING_AND_DUALITY_CRITICAL_AUDIT.md), [Gray audit](evidence/audit_reports/GRAY_MAP_EVIDENCE_AUDIT.md) and [source-reading observations](evidence/source_reading_observations.md). Their conclusions are not silently upgraded. A theorem may survive while its printed proof fails; a correct finite tuple does not repair a universal argument; truth and novelty require different evidence.

## 2. Fixed mathematical contract to confirm before any proof edit

The following records the **existing audited framework**, not a proposed generalization.

| Object | Contract / invariant to retain | Review failure to prevent |
|---|---|---|
| Coefficient ring and ambient ring | `q=p^e`, `A=Fq[u]/(u^t)`, `R=M_r(A)`, matrix size `r=2` for this campaign; central `X`; cyclic ambient `R[X]/(X^n−1)` | Whole-ring powering instead of coefficient Frobenius; an unapproved Ore quotient or matrix-size change |
| Notation | This plan uses `e` for field-extension degree, `r` for matrix size and `s` for Frobenius exponent. The manuscript instead uses `r` for extension degree and `m=2` for matrix size | A silent interchange of field and matrix dimensions; divisibility tests using the wrong symbol |
| Codes and Morita model | Right modules/right ideals; code-cyclic means shift-invariant, not automatically principal; column/Morita ordering fixed | Right/left side switches; base-ring ideals confused with wild cyclic-ambient submodules |
| Anti-automorphism | Coefficient `sigma_s` fixes `u` and `X`; `theta_s=sigma_s` followed by transpose | Calling every `theta_s` an involution; extending every metric/quantum claim to arbitrary automorphisms |
| Pairing and codomain | First-slot `B_s(x,y)=Σ theta_s(x_i)y_i`, valued in `R`; top-coefficient matrix-trace scalar form `b_s=Lambda∘B_s`, valued in `Fq` | Arbitrary matrix multiplication on a scalar output; conflating matrix trace/top coefficient with the absolute field trace |
| Right action | The retained ring-valued action is `B_s(xa,y)=theta_s(a)B_s(x,y)` and `B_s(x,yb)=B_s(x,y)b` for constant `a,b` | Reusing the frozen summary's `ax` formula; assuming the same formula proves polynomial convolution closure |
| Double dual | Retain the **positive** same-convention double twist; universal reflexivity needs `e | 2s` and matrix size at least 2; single-code reflexivity is a separate invariance condition | Replacing the positive twist because a different left-slot convention has a negative twist; using a changing vector as proof that its generated module changes |
| Gray coordinates | Specific coefficient expansion, fixed ordering, `N=t r² n`, target Gram form `J=I_(r²n)⊗H_t` | Treating an arbitrary Gray map or ordinary Euclidean pairing as the transported target |
| Physical quantum coordinates | Named actual image `D` or transformed image `D′`; ordinary Euclidean hull `h_E` used where required; exact field encoding retained | Substituting a transported Galois hull into an EA formula; transporting distance through an unproved Hamming isometry |

A future correction record must attach this contract to each retained claim and example. It must not silently replace the manuscript's notation in old files.

## 3. Proof work packages and acceptance gates

### WP-A1 — Right-module closure, functionals and orthogonal equality

**Actions:** CP01–CP06 and CP17. **Targets:** MS03 §§3–4, especially `lem:failure`, `lem:sesqui`, `thm:duality(a,b)`, `prop:twoorth`; downstream `thm:grayduality`. Exact line ranges are in the [master register](MASTER_CORRECTION_REGISTER.md).

**Required work after authorization:**

- Reconcile the valid constant right-action law with the printed cyclic/polynomial closure proof. Check the convolution indices and Frobenius/trace manipulations separately. The equality asserted in §4 lines 69–93 is not established by the existing displayed calculation.
- Separate elementwise nondegeneracy, a correctly sided generating functional and the module-perfect/cardinality argument. Retain a valid identity/nonzero-coordinate probe; do not reuse the erroneous matrix-unit probe.
- Replace the inconsistent failure-lemma example with a single correctly specified **existing** finite example, or remove it. It currently mixes `M2(F2)`, `t=2`, `uR` and two different notions of orthogonal. A generic finite-Frobenius-ring statement cannot be justified using undefined `Fq`-linear data.
- Integrate the audited module/functional justification for scalar/ring orthogonal equality. The assertion that a map to the full `Hom_Fq(C,R)` is surjective by nondegeneracy does not establish the required dimension count; its semilinear typing also needs review.
- Keep the right-module hypothesis explicit wherever equality of scalar and ring orthogonals is used. Distinguish nonmodule subspaces, correctly sided plain-product duals and the chosen same-sided anti-automorphism framework.
- Safest treatment of unused left-slot/A-valued alternatives: omit claimed equivalences. Developing them is not required for the correction-only scope.

**Acceptance:** a side/codomain-complete proof chain and applicable foundational citations; author/reviewer sign-off; B02 controls on actual subspaces. A valid supporting theorem must be imported with its hypotheses and proof trail, not merely its conclusion. **No direct numerical change to the 28 correctly decoded field records is inferred.**

### WP-A2 — Double dual, cyclic annihilators, reversal and reflexivity

**Actions:** CP04, CP07, CP08, CP12. **Targets:** MS03 `lem:theta`, the slot paragraph, `thm:duality(c,d)`, `lem:ann`, `thm:dualformula`, `cor:rev`, `prop:regimes`.

**Required work after authorization:**

- Preserve the audited positive double twist and sound slope-module necessity argument. Distinguish a universally reflexive regime from an individual Frobenius-invariant code.
- Remove or justify the claim that moving the twist to the other slot gives the same dual; specify sides, parameters and orientation for any retained alternative. Do not call a noninvolutive map an involution.
- Separate “cyclic right ideal” from “principal right ideal.” Import the already proved matrix-size-two principality criterion with its exact hypotheses; do not present it as still open.
- Review every annihilator generator reduction by its actual side. A displayed left-generated sum does not automatically justify the stated reduction for a right-generated ideal. Reconcile the principal-dual consequence with what has actually been proved about the ambient ring.
- Review the universal wording of “dropping reversal changes the dual for n≥3.” The nonidentity of the reversal operator is not, by itself, a per-code change assertion. Check exceptional/invariant/zero/full cases explicitly.
- Do not extend every Gray/metric/quantum result “verbatim” to arbitrary coefficient-ring automorphisms merely because the existing duality generalization is audited.

**Acceptance:** exact hypotheses and quantifiers for each retained statement; B02 annihilator/reversal and twist controls, including `n≥3` and zero/full examples. If a stronger principal-dual/reversal claim has no valid existing proof, restrict or withdraw it; do not start a new classification problem.

### WP-A3 — Nonprincipal hulls, torsion and witness provenance

**Actions:** CP07–CP11, CP12, CP31. **Critical:** CP10. **Targets:** MS03 §5 `thm:nonprincipal`, `eq:witnessfamily`, witness census, `thm:noclosed`, examples A/B, abstract and contribution summaries.

**Decisive distinction:** the audit's earlier explicit `(q,t,n)=(4,2,2)` self-dual hull has `dim W=4`, `dim rad W=1`, **mu=3>2**. The manuscript's different claimed direct-sum family has intersection dimension 1, sum dimension 5, radical dimension 3 and **mu=2**, not 3. These cannot be interchanged by renaming the construction.

**Author must choose a path; no choice is presumed:**

1. **Safest bounded path:** withdraw the invalid generic family and base any retained existence claim only on an already verified explicit witness, with its complete existing proof/certificate independently reviewed.
2. **Restrict further:** withdraw unsupported nonprincipal-origin/census/headline claims pending later review.
3. **Request a proof replacement:** identify an existing valid replacement argument and approve its bounded review. If a genuinely new family/theorem is needed, stop for separate research authorization; it is not an automatic correction task.

**Proof obligations:**

- Use generation bounds, not the false assertion that every submodule of a free chain-ring module is free.
- Distinguish the base `A`-module, cyclic ambient `B`-module, full image rows and Morita-intersection rows. A field rank is not a module generator number.
- Give an explicit immutable basis, module closure, actual dual/hull, radical and generator-number evidence for each retained finite witness. Preserve the distinction between code mu and hull mu.
- Check all dependent statements: nonexistence of one-generator formulas, the “principal codes have principal hulls” question, enumerated family sizes, abstract/newness claims and wild/R1 headline rows. The existence of one nonprincipal hull does not settle every finer principal-code question.
- Treat the Phase5 wrong-row helper as a provenance defect, not a proof of mu=4. Phase6 already provides the corrected route. Original scripts/logs remain unchanged.
- Clarify the example-B “proper superobject” wording only after identifying its actual starting code; a hull defined as an intersection cannot be a strict superobject of that same code.

**Acceptance:** reviewed retained proof or explicit withdrawal; B03 controls; a named CP31 list of any additional witnesses to recertify. Randomly failing to find a generator is not proof of nonprincipality. **The 28 field records do not inherit or supply missing ring-origin certificates.**

### WP-A4 — Gray transport, form classification, metrics and CSS applicability

**Actions:** CP13–CP19 and CP26. **Targets:** MS03 §6 and R2/R3 uses in §7.

**Required work after authorization:**

- Preserve the specific coefficient-map/Gram calculation and module-dependent transport theorem at their audited scope. Preserve quasi-cyclic index `4t` for matrix size 2 and distinguish coefficient weight from ring-symbol and normalized homogeneous weights.
- Qualify “J is alternating iff t is even” by characteristic and form type. Zero diagonal alone is not alternating in an odd-characteristic bilinear or general Hermitian form.
- Keep ordinary bilinear congruence, involutive Hermitian congruence and general Galois sesquilinearity separate. The characteristic-two/even-t **bilinear** obstruction is retained; it does not prohibit all Hermitian congruences.
- Use the displayed GF9 transformation only in its checked bilinear scope unless a separately reviewed argument establishes more. Verify orientation and Frobenius exponent before any use.
- Remove the implication “no ambient Euclidean congruence, therefore no CSS code for every individual image.” Each retained code needs its actual ordinary-Euclidean SO/DC inclusion checked.
- A nonmonomial congruence is not automatically a Hamming isometry. Distances must be certified in the actual physical coordinates.
- Keep `h_E` distinct from a transported Galois hull. An unproved twist-dependent bridge would be new P1 research and is excluded.

**Acceptance:** restricted form/metric statements and actual coordinate conventions, B04 tests, explicit image/inclusion records. The 463 assertion count is a reproducibility fact, not the proof of a universal Gray/CSS theorem.

### WP-A5 — Weyl phases and the stabilizer foundation

**Actions:** CP22–CP23. **Critical:** CP23. **Targets:** MS03 §7 `lem:Q1`, `lem:Q2`, `thm:fpbasis` and their uses.

**Required work after authorization:**

- Select one consistent convention matching the displayed `X` and `Z` operators. Reconcile the odd-characteristic product/commutator signs throughout; a characteristic-two test cannot validate the odd-p sign.
- State and check isotropy, the phase-correct stabilizer lift, closure, absence of nonidentity scalar operators and the nontrivial code-space/distance domain. Arbitrary additive label groups are not sufficient.
- Replace general “±S”/“anti-commutes” language by the correct nonbinary phase/error formulation where applicable.
- Distinguish an `Fp` commutation basis from an `Fq` basis. Trace-zero tests on only an `Fq` basis are not generally a substitute for checking all required scalars; exact `Fq`-valued symplectic zero tests have a different justification.
- Prefer a precise applicable standard theorem with its hypotheses over an unsupported claim that all stabilizer machinery has been newly derived without imports.

**Acceptance:** quantum-specialist proof/citation review and B05 operator/isotropy/scalar controls. A sign error does not by itself refute every q9 tuple; correcting a sign alone does not close CP23.

### WP-A6 — EA completion and Alice-only logical errors

**Actions:** CP24, CP26. **Critical:** CP24. **Targets:** MS03 §7 `thm:R3`; §8 use of EA distance.

**Required work after authorization:**

- Replace the defective nonisotropic/hyperbolic-decomposition argument by a correct standard Bob-completed, phase-correct construction, with all dimensions and fields specified.
- Check the Alice-only commuting and stabilizer/radical sets. The unextended operators labelled by every `v` do not all fix the code when the Alice label space is nonisotropic.
- Derive the conditional parameter/distance interpretation from that construction or cite a fully applicable theorem. Keep ordinary Euclidean `h_E` and the role of Bob's noiseless systems explicit.
- Preserve the audit's distinction: the standard conditional EA formulas survive; the printed proof does not. No new Galois-hull-to-EA theorem is supplied here.

**Acceptance:** reviewed complete construction/derivation and B05 Gram-rank/Bob-commutator/distance checks for retained records. Arithmetic cancellation alone is not a universal Hilbert-space proof.

### WP-A7 — Route contracts, relative quotients and metric/bound scope

**Actions:** CP25, CP27, CP28. **Critical:** CP25 and CP27. **Targets:** MS03 §§7–8, parameter summary, `thm:cosetdistance`, `thm:cosetsingleton`, `prop:newsbound`.

The table below records **audited distinctions to preserve**, not a replacement theorem to paste into a manuscript. Every use still needs its explicit hypotheses and proof chain.

| Route | Required source/field distinction | Distance object / principal risk |
|---|---|---|
| R1 graph | A transported-self-orthogonal code yields a graph that is generally only `Fp`-linear; retain trace-symplectic orthogonality | Do not replace its trace orthogonal by the smaller `Fq`-value orthogonal; no asserted distance difference follows from a set difference alone |
| SO | Actual `D ⊆ Ddual_E`; the original `D` is the stabilizer input | Classical target/exclusion is `Ddual_E` outside `D` |
| DC | Actual `Ddual_E ⊆ D`; either keep the original `D` throughout or explicitly rename the stabilizer input everywhere | Classical target/exclusion is **D outside Ddual_E**; the universal EA quotient in the manuscript gives a contradiction here |
| EA | Actual Euclidean hull; correctly completed standard construction | Classical target/exclusion is `Ddual_E` outside `Hull_E(D)`; a transported hull is not an automatic substitute |

**Required work after authorization:**

- Attach a route contract to every theorem, table and certificate: original/transformed input, linearity field, label space, orthogonal, excluded subspace, parameter convention and metric.
- Reconcile the supplied DC example `03_20_4_4_4_(4,1,5)_DC.json`: `N=20,k=12,h_E=8,K=4,c=0,d=4`. The manuscript's unqualified EA quotient has dimension zero. **Do not “fix” this valid tuple to K=0.**
- Describe relative quotients using coset-leader minimum weight, not arbitrary representative weight or an automatic ordinary coordinate-Hamming code. Require a positive-dimensional/nonempty distance domain or separately justified zero-dimensional convention.
- Review the printed projection/codomain argument. The audit identifies an existing valid route-restricted justification for `K+d≤N+1`; this plan does not reproduce that proof. The coset counterexample does **not** refute the restricted inequality.
- Review `prop:newsbound` and nonimplication separately: validity of an elementary inequality, independence from other bounds and priority are different questions. A proof check is not a novelty certificate.

**Acceptance:** route-correct proof/restriction/withdrawal and B05 set/dimension/relative-distance controls; CP36 literature work for any retained newness claim.

### WP-A8 — Parameter identities, frontier consequences and summary alignment

**Actions:** CP29–CP31, with CP21. **Critical:** CP29. **Targets:** MS03 §8 `thm:feasibility`, `thm:bookkeeping`, frontier/budget/headline tables; §7 summary and abstract.

**Required work after authorization:**

- Derive each identity and parity/budget/feasibility consequence using its own route and the same meaning of `k`. Do not apply EA/SO identities to original-input DC or R1 by changing notation halfway through.
- Preserve valid tuples even where they contradict the false all-route summary. The audited R1 and DC counterexamples are mandatory negative controls.
- Reconcile only the explicitly retained table rows and frontier/optimality claims. The 28 records do not independently certify all 5,055 historical distance rows or every additional wild/R1 example.
- Preserve MS03's already-corrected certification-method wording. Historical M1/M2/M3 completion/lower-bound states are not three exact methods for every row.
- Only after proof/parameter closure may final Group C prose, Group D comparisons and any abstract/conclusion claims be aligned in an authorized successor. No new manuscript drafting is done now.

**Acceptance:** explicit route-to-row formulas, exact/lower-bound/census labels, B05/B06 results, and independent review of all dependent consequences. If the scope cannot be supported from existing approved evidence, qualify/remove it rather than launching an unapproved search.

## 4. Retain, restrict or withdraw — decision discipline

- **Retain at audited scope:** first-slot right pairing; conditional size law; positive double dual/reflexivity criterion; specified Gray transport; earlier explicit nonprincipal witness; exact 28 finite record verdicts.
- **Restrict:** ambient congruence obstruction, alternatingness, automorphism remarks, route/quotient/budget assertions and finite-search completeness claims.
- **Withdraw unless adequately supported in an authorized successor:** failed generic hull family, unproved principal-dual/general reversal consequences, unsupported extra-row ring provenance, blanket no-CSS or firstness/record claims.
- **Do not solve under this task:** principal-code hull classification, new twist-dependent EA bridge, size-three hull classification, skew/Ore compatibility, new parameter-family searches.

A future inability to close a proof is an acceptable stop/restriction outcome, not permission to fabricate a replacement. The independent reviewer must check actual retained statements and proofs, not this proposed work list alone.

## 5. Proof-closure record required later

For each CP action: frozen baseline/line locator → chosen retain/restrict/withdraw option → exact authorized successor diff → complete hypotheses/citation/proof obligations → applicable B-test certificates → dependent parameter/summary checks → independent reviewer decision. Record theorem truth, proof validity, finite verification and novelty in separate fields.

Nothing in this document changes a source file, certifies a repaired proof, sends an editorial message or authorizes implementation. The [author checklist](AUTHOR_APPROVAL_CHECKLIST.md) must be resolved first.

**HOLD — CORRECTION PLAN ONLY — IMPLEMENTATION NOT AUTHORIZED.**
