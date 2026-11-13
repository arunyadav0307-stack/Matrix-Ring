# Phase 0 — Independent Self-Audit Report

**Audit object:** `PHASE0_REVISION_AUDIT_PACKAGE.zip` (commit `9a5bf40`), i.e. the revised
Phase 0 (Tasks 1–3) as handed over.
**Audit date:** 2026-11-04.
**Branch:** `arena/59de606f-matrix-ring` (all work committed there, fast-forward only).
**Scope:** mathematical re-derivation, independent computation, Alahmadi (A1) audit,
U8/U9 decisions, novelty re-assessment. **No Phase 1 work, no manuscript, no change of
research direction.** `05_MANUSCRIPT/` is still empty.

---

## 0. Verdict in one paragraph

**MODIFY — then GO.** The mathematical spine of Phase 0 is sound: the θ_s-duality, the
size formula, the double-dual formula `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`, the reflexivity
criterion `r | 2s`, the hull theorems and the cyclicity of duals were re-derived from
scratch (this report) *and* re-verified by an independent implementation
(§2) *and* re-verified once more against the supplied pairing and the supplied
enumerator on 6 961 (code, s) instances (§2.3). Three defects were found and are now
corrected in the working tree: **(a)** a real bug in `04_COMPUTATION/galois_t2_check.py`
that made the t = 2 census report **32** right ideals instead of **33** (the zero
submodule was never enumerated); **(b)** the enumeration formula T-018 is stated in the
register without the **squarefree** hypothesis on `X^n − 1`, which is essential — the
counterexample `q = 4, n = 2` gives 33 codes where the formula predicts 49; **(c)** the
recorded statement of Alahmadi–Sboui–Solé–Yemen Theorem 1 (A1) is **internally
inconsistent** (§4) and must not be restated until the source is re-read. In addition the
**novelty claim must be downgraded** (§5): the general "duality from an anti-automorphism
over a finite Frobenius ring" machinery is due to Wood (2010), Szabo–Wood (2017) and
Nebe–Rains–Sloane (2006); what is new here is the explicit θ_s = σ_s ∘ transpose family,
the `r | 2s` criterion, the Galois-hull treatment of *cyclic* codes over *matrix* rings,
and the censuses. One decision is required from the researcher before Phase 1 (§4, U8).

---

## 1. What was done

| # | Activity | Method | Outcome |
|---|----------|--------|---------|
| 1 | Re-derivation of σ_s, θ_s, non-degeneracy, right-module property, size formula, double dual, cyclicity of the dual, hull, reflexivity | pen-and-paper, from the definitions, **without reading** `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` first; compared afterwards | `PHASE0_PROOF_VERIFICATION.md` |
| 2 | Independent implementation (own finite fields, own RREF/nullspace, own local ring `F_q[u]/⟨u^t⟩`, own `M_m`, own ambient space, own θ_s-pairing, own enumeration) | `04_COMPUTATION/independent_audit_checks.py` (~600 lines, **no** `matrix_ring_lib` import), 12.0 s, exit 0 | `ALL PREDICTIONS CONFIRMED: True` |
| 3 | Re-verification of the double-dual/isometry machinery **on the supplied code paths** (supplied `pair_theta`, supplied `enumerate_ideals_morita`) | `04_COMPUTATION/audit_pairing_equivalence.py`, 86 s | 6 961/6 961 on every structural property |
| 4 | Alahmadi (A1) convention probe at `n = 3`, `A = M_2(F_2)`: both candidate conventions enumerated and their dualities computed | `04_COMPUTATION/u8_n3_selfdual_check.py`, 8 s | see §4 |
| 5 | Re-run of every supplied script for reproducibility | `galois_duality_experiments.py full`, `galois_t2_check.py`, `alahmadi_reconciliation.py` | all exit 0; byte-identical science (only `run:`/`[elapsed]` differ) |
| 6 | Targeted literature search (anti-isomorphism duality, non-commutative hulls, Galois hulls → quantum, matrix-ring alphabets) | web search + primary sources | §5 |

New files created in `04_COMPUTATION/`: `independent_audit_checks.py` (+ log),
`audit_pairing_equivalence.py` (+ log), `u8_n3_selfdual_check.py` (+ log).
Nothing was deleted; `galois_t2_check.py` was patched (one-line seed of the zero
submodule) and is annotated in place.

---

## 2. Computational audit — headline numbers

### 2.1 Independent implementation (§2 of `PHASE0_COMPUTATIONAL_AUDIT.md`)

* q = 4: **σ_1 additive ✓ multiplicative ✓ nontrivial ✓** over all 256² pairs;
  θ_1 anti-multiplicative ✓; θ² = σ_{2s} on all 256 elements ✓; σ_{2s} = id ✓.
* q = 8 (4 000 sampled pairs): σ_1/σ_2, θ_1/θ_2 all ✓; θ² = σ_{2s} ✓; **σ_{2s} = id ✗**
  (r = 3 ∤ 2s). q = 9: all ✓, σ_{2s} = id ✓.
* Gram rank of the pairing: full (4/4 at t = 1, m = 2; 8/8 at t = 2) and full for every
  tested (q, t, n, s) → **non-degenerate everywhere**.
* Independent enumeration of right ideals: q = 2, 4, 8, 9 → 5, 7, 11, 12 = `q + 3`
  (Morita: `1 + (q+1) + 1`), dimension profile `[(0,1), (2,q+1), (4,1)]` ✓.
* t = 2 (`A = F_q[u]/⟨u²⟩`, m = 2): **33** submodules (corrected), see §3.1.
* Cyclic-code censuses: `q=4,n=3 → 343`; `q=9,n=2 → 144`; `q=2,n=3 → 35`
  (direct scan of all 4 096 ambient vectors); `q=4,n=2 → 33` (**not** the 49 predicted
  by the squarefree formula — see §3.2).
* Duality/hull on independently enumerated codes (q = 4, n = 1, s = 1: 7 codes; q = 8,
  n = 1, s = 1, 2: 11 + 11; q = 9, n = 1, s = 1: 12; q = 4, t = 2: 33; q = 2, n = 3: 35):
  right-module ✓ dual-right ✓ size formula ✓ hull-right ✓ **100 %**;
  **double-dual = σ_{2s}(C): 100 % in every case**;
  reflexivity 7/7, 12/12, 33/33, 35/35 when `r | 2s`, and **5/11** at q = 8 for both
  s = 1 and s = 2 — exactly the predicted failure.
  Plain-product control (no θ): size formula succeeds only 2/7, 2/11, 2/12, 3/33, 4/35 →
  the θ_s twist is essential, the plain product is not a substitute.

### 2.2 Corrections made to supplied artefacts

| Artefact | Defect | Correction | Status |
|----------|--------|-----------|--------|
| `04_COMPUTATION/galois_t2_check.py` | `seen` was never seeded with the zero subspace and zero vectors were skipped ⇒ the **zero code was missing** from the census | `seen = {tuple(): []}` + comment; re-run | **32 → 33**; all per-code checks now 33/33 (were 32/32) |
| `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` T-018 | formula stated without the squarefree hypothesis | hypothesis added (`gcd(n,p)=1` / `X^n−1` squarefree) + counterexample | done in `UPDATED_THEOREM_REGISTER.md` (this audit) |
| T-022 / documents quoting "32 right ideals" | inherited from the bug | every such occurrence updated to 33 and to the corrected dimension distribution | done in the register; the revision reports still say 32 and must be corrected (§6 item 4) |

### 2.3 Verification on the supplied code paths (`audit_pairing_equivalence.py`)

For `q = 4, n = 3` (343 codes, s = 1), `q = 8, n = 3` (737 codes, s = 1 and s = 2),
`q = 9, n = 2` (144) and `q = 9, n = 4` (5 000 sampled), using the **supplied**
`pair_theta` and the **supplied** `enumerate_ideals_morita`:

| Property | q = 4, n = 3 | q = 8, n = 3 (s = 1 / s = 2) | q = 9, n = 2 | q = 9, n = 4 |
|---|---|---|---|---|
| trace-valued dual = matrix-valued dual | 343/343 | 737/737 · 737/737 | 144/144 | 5 000/5 000 |
| size formula (both forms) | 343/343 | 737/737 | 144/144 | 5 000/5 000 |
| (E1) `B_s(σ_k x, σ_k y) = σ_k B_s(x,y)` | 300/300 | 300/300 | 300/300 | 300/300 |
| (E2) orthogonality preserved by σ_k | 300/300 | 300/300 | 300/300 | 300/300 |
| (E3) Hamming weight preserved by σ_k | 300/300 | 300/300 | 300/300 | 300/300 |
| (E4) `σ_k(C^⊥) = (σ_k C)^⊥` | 343/343 | 737/737 | 144/144 | 5 000/5 000 |
| (E5) `Hull(σ_k C) = σ_k Hull(C)` | 343/343 | 737/737 | 144/144 | 5 000/5 000 |
| **(E6) `(C^⊥)^⊥ = σ_{2s}(C)`** | **343/343** | **737/737** | **144/144** | **5 000/5 000** |
| **reflexive (`C^{⊥⊥} = C`)** | **343/343** | **35/737 · 35/737** | **144/144** | **5 000/5 000** |

(`k = 2s mod r`.) The last two rows are the decisive ones: the double-dual formula holds
with no hypothesis, while reflexivity holds exactly when `r | 2s`, and fails *massively*
(35/737) when it does not.

---

## 3. Findings register

Severity: **A** = blocks Phase 1 until fixed/resolved; **B** = must be fixed before the
manuscript claims it; **C** = hygiene/documentation.

| ID | Severity | Finding | Evidence |
|----|----------|---------|----------|
| F-01 | **A** | The recorded statement of A1's Theorem 1 is internally inconsistent: the listed generators are divisors of `X^n − 1` for **two different lengths** (`X²+X+1 ∣ X³−1`; `X³+X+1`, `X³+X²+1 ∣ X⁷−1`). No single `n` admits all three. | §4; degree/ divisibility check |
| F-02 | **A** | Novelty over-claim: "duality via an anti-automorphism over a non-commutative ring" is **published** (Wood 2010; Szabo–Wood 2017; NRS 2006). The project's novelty is narrower (§5). | §5, primary sources |
| F-03 | B | `galois_t2_check.py` reported 32 right ideals instead of 33 (zero submodule omitted). | fixed; re-run gives 33, 33/33 |
| F-04 | B | T-018 (enumeration formula) needs `X^n − 1` squarefree; `q = 4, n = 2` gives **33**, the formula predicts **49**. | independent enumeration |
| F-05 | B | T-017's hypothesis `m ≥ 2` is essential: for `m = 1` every ideal of `A_t` is σ-invariant, so the duality is always reflexive. | §2.7 of `PHASE0_PROOF_VERIFICATION.md` |
| F-06 | B | The θ_s-form is **not** symmetric when `σ_{2s} ≠ id`; it satisfies `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)`. Hence "C ⊆ C^⊥" cannot be checked on diagonal/Gram-self-terms only in the non-reflexive case. | §2.8 of the proof-verification file |
| F-07 | B | Alahmadi et al.'s "Euclidean" form is `Σ_j x_j y_j` (matrix product, **no transpose**). It is not non-degenerate in the F_q-bilinear sense: at `q=2, n=3`, `dim C + dim C^⊥` is **not** constant (`[(6,15),(8,10),(10,6),(12,4)]`) and there are **0** self-dual codes. Our form must be explicitly distinguished from theirs in the manuscript. | `alahmadi_reconciliation_log.txt` §5; re-verified |
| F-08 | B | The register states T-010 ("the F_q-valued form defines the same dual") as proved; the *proof* is: inclusion `C^⊥_matrix ⊆ C^⊥_trace` + equal dimension from the size formula. Verified 6 961/6 961. The orientation (θ in the first or second slot) is immaterial — both were tested. | §2.3 |
| F-09 | C | "32 right ideals"/"32/32" appears in the Phase-0 revision reports; must become 33. | grep needed (§6 item 4) |
| F-10 | C | `q = 8` censuses: the Morita enumerator requires `X^n − 1` squarefree, which in characteristic 2 forces `n` **odd**; any future q = 8 run must not use `n = 2`. | `audit_pairing_equivalence.py` run aborted at `q=8,n=2` with `X^n-1 is not squarefree` |
| F-11 | C | Reflexivity at q = 8 is not "no code is reflexive": 35 of 737 codes are (those with `σ_{2s}(C) = C`). T-017 says "reflexive **for all** C ⟺ r|2s", which is correct; the looser reading must not be used. | §2.3 |
| F-12 | C | The q = 2 runs (`r = 1`) are **not** Galois evidence: σ_s = id for all s there. They are enumerator-validation only. (Already stated in the package; re-affirmed.) | — |
| F-13 | B | Szabo–Wood (2017) work with **hermitian** sesquilinear forms; whether their MacWilliams/double-dual statements cover the non-involutive case is **not yet checked**. If they require an involutive anti-automorphism, our non-reflexive regime has no MacWilliams theorem yet. | §5; action item |

---

## 4. U8 and U9 (summary; full argument in `PHASE0_U8_U9_DECISIONS.md`)

**U8 — Alahmadi convention.** Two conventions for "cyclic A-code of length n" exist and
they are different:

* **(I) right-ideal convention** (ours, and the one A1 states in its Sec. 2): at
  `q = 2, n = 3` there are **35** cyclic codes. This is now *structurally* confirmed: by
  CRT + Morita, `R_3 ≅ M_2(F_2) × M_2(F_4)`, so the count is `5 × 7 = 35` with
  F_2-dimensions `2v_1 + 4v_2` (`v_1 ∈{0,1,2}` with multiplicities 1,3,1; `v_2 ∈{0,1,2}`
  with 1,5,1). The predicted distribution
  `[(0,1),(2,3),(4,6),(6,15),(8,6),(10,3),(12,1)]` **matches the enumeration exactly**.
* **(II) quaternary convention** (A1's bijection with cyclic codes over `F_4` via
  `F_4 = ⟨I, ω⟩ ⊂ A`): at `n = 3` there are **8** codes (monic divisors of `X³−1` over
  `F_4`) — this is A1's "8". Computed: dims `0, 4, 4, 4, 8, 8, 8, 12`; **no** nonzero
  self-orthogonal code and **no** self-dual code under either form
  (half-dimension = 6 is unreachable, since `dim = 4(3 − deg g)`).

Consequences: A1's "8" is a **(II)**-statement; our 35 is a **(I)**-statement; neither
supports the recorded "self-dual … generator" list. Under (I) at `n = 3` there are exactly
**3** self-dual codes (against the form `Σ_j tr(x_j^T y_j)`, i.e. our Galois form at
s = 0), and they are exhibited explicitly in `u8_n3_selfdual_log.txt`.
**Decision required:** re-read A1 (paywalled; not reachable from this sandbox) **or** drop
the A1 theorem from the manuscript and cite A1 only for the cyclic-code framework
(recommended — see `PHASE0_U8_U9_DECISIONS.md` §3).

**U9 — is reflexivity necessary?** Verified: `σ_{2s}` is a **semilinear isometry** of the
pairing (E1), it preserves Hamming weight (E3), it intertwines the dual (E4) and the hull
(E5), and `(C^⊥)^⊥ = σ_{2s}(C)` (E6). Therefore `C^{⊥⊥}` has the **same size, the same
weight enumerator, the same minimum distance and the same hull dimension** as `C`.
⇒ Reflexivity is **not** needed for any statement that only uses `C ⊆ C^⊥`,
`|C|·|C^⊥| = |R|^n`, `dim Hull_s(C)` and distance/weight data.
It **is** needed wherever the *set* `C^{⊥⊥}` must literally be `C`: the classical CSS/EA
parameter derivations, LCD (`C ⊕ C^⊥`), and any MacWilliams statement proved via double
duality. **Recommendation:** prove the quantum theorems in the **reflexive** regime
(`s ≡ 0` Euclidean, or `r` even with `s = r/2`, the "Galois–Hermitian" case), and state
the general `s` results with the σ_{2s} twist as companion theorems. Do **not** claim
quantum constructions in the non-reflexive regime until the parameter formula is derived
directly (no double-duality shortcut).

---

## 5. Novelty (summary; full write-up in `PHASE0_NOVELTY_REASSESSMENT.md`)

**Downgrade.** The following are **prior art** and must be cited as such:

* *duality over a finite Frobenius ring defined by a non-degenerate form attached to an
  anti-automorphism* — J. A. Wood, *Anti-isomorphisms, character modules and self-dual
  codes over non-commutative rings*, Int. J. Inf. Coding Theory **1**(4) (2010) 429–444
  (explicitly "an elaboration on ideas of Nebe, Rains and Sloane");
* *module structure of the dual, double-dual, cardinality complementarity, MacWilliams
  identities for sesquilinear/bilinear forms* — Szabo & Wood, J. Algebra Comb. Discrete
  Struct. Appl. **4**(2) (2017) 105–113 (MR3601342);
* *form rings/types, non-commutative alphabets such as* `F_q + F_q u, u² = 0` —
  Nebe–Rains–Sloane, *Self-Dual Codes and Invariant Theory*, Springer 2006;
* *left/right orthogonals over non-commutative Frobenius rings* — Dougherty & Leroy,
  AAECC **27** (2016) 185–203;
* *cyclic self-dual codes over* `M_2(F_2)` — P. Solé, MMS 2011, doi:10.1109/MMS.2011.6068573;
* *hulls over non-commutative rings* — Kushwaha & Prakash, arXiv:2512.12335 (2025) and
  arXiv:2601.06609 (2026) — but over a tiny **non-unital** ring, no Galois action;
* *Galois hulls → quantum codes* — Zhang, Kong & Zheng, Entropy **28**(4) 407 (2026)
  (commutative non-chain ring).

**What remains defensible as new** (and is all we should claim): the explicit family
`θ_s = σ_s ∘ transpose` on `M_m(F_q[u]/⟨u^t⟩)`; the double-dual formula
`C^{⊥⊥} = σ_{2s}(C)` with the reflexivity criterion `r | 2s` and its counterexamples;
**Galois (σ_s-) hulls of cyclic codes over matrix rings**; the exhaustive censuses and
hull-dimension distributions; and the (still open, Phase 5–6) route to quantum codes over
a non-commutative alphabet.

---

## 6. Remaining blockers and required researcher decisions

| # | Blocker | Decision / action required | Blocking? |
|---|---------|----------------------------|-----------|
| 1 | A1 (U8) statement inconsistent; source not reachable here | **(a)** re-read A1 and re-record the theorem, **or** **(b)** authorise "cite A1 for the framework only, do not restate its theorem" | **Yes** — blocks §5 of the manuscript only |
| 2 | Novelty wording (U3/F-02) | Accept the downgraded claim in §5 and the six new references | **Yes** — blocks the introduction |
| 3 | Reflexive vs general regime (U9) | Confirm: main quantum theorems in the reflexive regime (`s ≡ 0` or `r` even, `s = r/2`), general-`s` results as companions | **Yes** — blocks §7 |
| 4 | "32" leftovers in `02_PHASE_REPORTS/` revision docs (F-09) | Authorise the 32 → 33 correction in the three revision reports | No (hygiene, do it in Phase 1) |
| 5 | Szabo–Wood hypotheses (F-13) | Obtain the PDF and check whether their MacWilliams/double-dual statements cover a **non-involutive** anti-automorphism | No (but needed before claiming MacWilliams in the non-reflexive regime) |
| 6 | T-021 principality at `t ≥ 2` or `p ∣ n` | still **open**; nothing may use it | No (already flagged) |
| 7 | T-012 (Gray/Bachoc map), T-013, T-014 | out of Phase 0 scope; unchanged | No |

---

## 7. Recommendation

**MODIFY** (items 1–4 above; items 1–3 require a researcher decision), then **GO** to
Phase 1 with the corrected register, the corrected t = 2 census, the downgraded novelty
claim and the reflexive-regime plan for the quantum sections. **Stop and wait for
approval** — no Phase 1 work has been started and none will be started in this turn.
