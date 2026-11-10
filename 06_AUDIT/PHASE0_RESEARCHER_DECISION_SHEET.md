# Phase 0 — Researcher Decision Sheet

**Purpose.** This sheet puts the three outstanding decisions (B1, B2, B3) in front of the
researcher with the mathematical evidence, the options, and the consequences of each.
**Nothing here is decided on the researcher's behalf**: every recommendation is a
recommendation, and each decision row ends with an empty box for the researcher's answer.

**Status of the repository.** Commit `c092b11`; branch `arena/59de606f-matrix-ring`.
The independent audit is complete. **No Phase 1 work has been started**
(`05_MANUSCRIPT/` is empty) and **no existing approved mathematical result has been
modified** — the theorem register, the proofs file and the experiment scripts are
untouched by this sheet (the only code change in `c092b11` is the one-line bug fix in
`galois_t2_check.py` that the audit mandated).

---

## 0. Decision table (fill in the last column)

| ID | Decision | Options | Evidence | Recommendation (not a decision) | **Your decision** |
|----|----------|---------|----------|---------------------------------|-------------------|
| **B1** | Alahmadi–Sboui–Solé–Yemen (2013), Theorem 1 | (a) re-read and fully reconcile; (b) cite the framework only, never restate the theorem | §1 below | **(b)**, with the convention paragraph of §1.5 | ☐ (a) ☐ (b) ☐ other: ______ |
| **B2** | Novelty claim | (a) keep the broad claim; (b) adopt the narrowed four-part claim | `PHASE0_FINAL_NOVELTY_STATEMENT.md` | **(b)** | ☐ (a) ☐ (b) ☐ other: ______ |
| **B3** | Galois parameter regime | (1) general non-trivial Galois regime; (2) reflexive regime `r ∣ 2s`; (3) hybrid: reflexive primary + per-code Galois-invariant extension | `PHASE0_PARAMETER_SELECTION_RECOMMENDATION.md` | **(3)** | ☐ (1) ☐ (2) ☐ (3) ☐ other: ______ |

**Standing constraints (unchanged, and respected throughout this sheet):**

* no manuscript, no new mathematics outside the audit's remit, until these are answered;
* never assert that a published theorem is wrong;
* every claim must carry a proof, a citation, or a reproducible computation;
* `q = 2` remains enumerator-validation only (`r = 1` ⇒ `σ_s = id` for all `s`).

---

# B1 — Alahmadi, Sboui, Solé, Yemen (2013), Theorem 1

## 1.1 What the record says, and why it cannot be used as it stands

The statement as recorded in the package lists cyclic codes over `M_2(F_2)` "generated
by" the polynomials

1. `x² + x + 1` (case `j = 0`),
2. `(x³ + x + 1)(x³ + x² + 1)` (case `j = 1`),
3. `(x + 1)(x³ + x + 1)(x³ + x² + 1)` (case `j = 2`),

with the remark "the third case enumerates all 8".

A generator of a cyclic code of length `n` must divide `X^n − 1`. Over `F_2`:

* `X² + X + 1 ∣ X³ − 1` and `X² + X + 1 ∤ X⁷ − 1` (its roots have order 3);
* `X³ + X + 1` and `X³ + X² + 1 ∣ X⁷ − 1` and neither divides `X³ − 1`;
* the smallest `n` for which *all three* divide `X^n − 1` is `n = 21`, and there
  `X²¹ − 1` has six irreducible factors, hence **64** divisors, not 8.

⇒ **The recorded statement is internally inconsistent** (F-01). Something in the chain
(transcription, length parameter, or the role of `j`) is wrong. The paper is paywalled
and could not be retrieved from this environment, so the audit cannot resolve which.

## 1.2 What we *do* know, exhaustively, at `n = 3`

Two different families hide behind the words "cyclic code over `M_2(F_2)`":

| | (I) Right ideals of `R_n = A[X]/⟨X^n−1⟩` | (II) Quaternary family (`F_4`-correspondence) |
|---|---|---|
| convention | A1's own Sec. 2 ("RIGHT SIDED IDEALS represent cyclic codes") | A1's bijection with cyclic codes over `F_4 = ⟨I, ω⟩ ⊂ A` |
| count at `n = 3` | **35** | **8** |
| origin of the count | `R_3 ≅ M_2(F_2) × M_2(F_4)` ⇒ `5 × 7` | monic divisors of `X³−1` over `F_4` (`= (X+1)(X+ω)(X+ω²)`) ⇒ `2³` |
| `F_2`-dimensions | 0,2,4,**6**,8,10,12 | 0,4,8,12 |
| self-dual possible? | yes — half-dimension 6 is attained by 15 codes | **no** — `dim = 4(3 − deg g)` never equals 6 |
| verified | 35 by two independent enumerations; dimension distribution `[(0,1),(2,3),(4,6),(6,15),(8,6),(10,3),(12,1)]` **predicted exactly** by CRT+Morita | 8 divisors enumerated; 8 codes of dims 0,4,4,4,8,8,8,12 |

Consequences:

* A1's "8" is a **(II)** number; our 35 is a **(I)** number. **Neither is wrong** — they
  count different families. This alone is worth one explicit paragraph in the manuscript.
* Whatever A1's theorem says, it **cannot** be "the self-dual cyclic codes of length 3
  are …", because family (II) contains no self-dual code and family (I)'s three self-dual
  codes are not of that shape (they are exhibited explicitly in
  `04_COMPUTATION/u8_n3_selfdual_log.txt`).
* The most plausible reading compatible with the recorded polynomials is
  **"self-orthogonal codes at n = 7"** (self-orthogonality needs `deg g ≥ 4`, and the
  divisors of `X⁷ − 1` of degree ≥ 4 are `(X+1)(X³+X+1)`, `(X+1)(X³+X²+1)`,
  `(X³+X+1)(X³+X²+1)`, `X⁷+1` — the record has the last two). **This is a guess and must
  not be asserted.**

## 1.3 A separate, equally important convention divergence (F-07)

A1's "Euclidean" form is `Σ_j x_j y_j` — the **matrix product**, with no transpose. It is
*not* non-degenerate in the `F_q`-bilinear sense. Measured over all 35 codes at
`q = 2, n = 3`:

| form | `dim C + dim C^⊥` | # self-dual |
|---|---|---|
| `Σ_j x_j y_j` (A1) | not constant: `[(6,15),(8,10),(10,6),(12,4)]` | **0** |
| `Σ_j tr(x_j^T y_j)` (our Galois form at `s = 0`) | `= 12` for **35/35** | **3** |

Also: A1's Lemma 4 matched only 3/9 (their form) versus 5/9 (transpose form) on the 9
"genuine" triples. So the two papers use genuinely different dualities, and any
comparison that does not say so is a silent convention clash.

## 1.4 The two options, side by side

| | **(a) Re-read and fully reconcile** | **(b) Cite the framework only** |
|---|---|---|
| What it requires | Access to the paywalled paper (not available here); re-derivation of their parametrization; a correct restatement including length, form, and (I)/(II) convention | Nothing external; we keep only statements we can prove here |
| Upside | A clean reconciliation would be a genuine contribution to the literature; removes a loose end; lets us position our census against theirs | Zero risk of mis-stating a published theorem; zero dependency on an unavailable source; everything asserted is reproducible from this repository |
| Downside | Unknown time; may still be unresolvable (e.g. if the published statement has a typo); every week spent is a week not spent on T-012/T-013 | We forgo a "reconciliation" section; a reader may wonder about the 35-vs-8 gap (we answer it in one paragraph instead) |
| Risk | **High reputational risk** if we "correct" a theorem we have mis-read | Very low |
| Blocks | manuscript §5 (and possibly §1) | nothing |
| Reversible? | No — once published, a wrong correction is permanent | Yes — a reconciliation can always be added later as a remark or a second paper |

## 1.5 Recommendation (mathematically justified)

**Choose (b).** Justification:

1. *Asymmetry of evidence.* We can prove everything (b) needs: 35 codes, the CRT/Morita
   structure, the dimension distribution, the 3 self-dual codes, the 8 quaternary codes,
   the degeneracy of `Σ x_j y_j`. We cannot currently verify a single clause of the
   recorded theorem.
2. *Asymmetry of risk.* (b) is reversible and cheap; (a) is irreversible if the
   reconciliation is wrong. The standing rule "never assert a published theorem is wrong"
   points the same way.
3. *The interesting content survives.* The genuine finding — that A1's "8" and our "35"
   are two conventions, and that A1's form is degenerate while ours is not — is a
   *convention* observation, not a claim of error, and it can be published under (b).

**Exact implications for the manuscript under (b):**

* §1 (introduction): cite A1 for the cyclic-code-over-`M_2(F_2)` framework, the
  `F_4`-correspondence and the residue/torsion description. No statement about their
  duality theorem.
* §3 (duality): one sentence — "Our pairing is `Σ θ_s(x_e) y_e`; at `s = 0` this is
  `Σ tr(x_e^T y_e)`, which should not be confused with the form `Σ x_e y_e` used in
  [A1]; the latter is degenerate on right modules (see §5)."
* §5 (census): our own table (5 codes at `n = 1`; 35 at `n = 3` with the CRT/Morita
  derivation; 3 self-dual codes; hull distributions) + a **convention paragraph**
  explaining (I) vs (II) and stating that A1's "8" is the (II)-count, with no claim about
  their theorem.
* Remove T-019's "adjudication requested" flag; re-word it as a *convention diagnosis*
  (it is a proved computational fact about triples, not a claim about A1).
* If the researcher later obtains the paper and wants (a), §5 can be extended without
  disturbing anything else.

**If (a) is chosen instead**, the required work is: obtain the paper; identify `n`, `j`,
`ℓ`; determine (I) or (II); determine the form; re-run `alahmadi_reconciliation.py`
against the corrected statement; and only then write §5. Budget: unknown, but the
enumeration code is already in place.

---

# B2 — Novelty (summary; full statement in `PHASE0_FINAL_NOVELTY_STATEMENT.md`)

The audit found that the broad claim — *"we introduce a duality for codes over a
non-commutative ring via an anti-automorphism"* — is **published**:

| Prior art | Covers |
|---|---|
| J. A. Wood, *Int. J. Inf. Coding Theory* **1**(4) (2010) 429–444 | exactly the anti-isomorphism approach; explicitly "an elaboration on ideas of Nebe, Rains and Sloane" |
| Szabo & Wood, *J. Algebra Comb. Discrete Struct. Appl.* **4**(2) (2017) 105–113 | module structure of the dual, double-dual, cardinality complementarity, MacWilliams identities for non-degenerate sesquilinear forms over a finite Frobenius ring |
| Nebe–Rains–Sloane, *Self-Dual Codes and Invariant Theory* (Springer 2006) | form rings/types, non-commutative alphabets such as `F_q + F_q u`, `u² = 0` |
| Dougherty & Leroy, *AAECC* **27** (2016) 185–203 | left/right orthogonals over non-commutative Frobenius rings |
| P. Solé, MMS 2011, doi:10.1109/MMS.2011.6068573 | **cyclic self-dual codes over `M_2(F_2)`** — closest predecessor on our alphabet |
| Kushwaha & Prakash, arXiv:2512.12335 / arXiv:2601.06609 | hulls (left/right/two-sided) over a non-commutative, non-unital ring |

What survives, and is defensible: the explicit `θ_s = σ_s ∘ transpose` family; the
double-dual `C^{⊥⊥} = σ_{2s}(C)` with the identity `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)` and
the reflexivity criterion `r ∣ 2s`; the σ_{2s}-isometry lemma; **Galois hulls of cyclic
codes over matrix rings** with exhaustive censuses; and (Phase 5–6, still open) the route
to quantum codes over a non-commutative alphabet.

**Decision requested:** accept the narrowed claim of
`PHASE0_FINAL_NOVELTY_STATEMENT.md` §2 (published / new / computational / still-open
four-way split) and the six new bibliography entries. **Rejecting this leaves the paper
exposed to an immediate priority objection.**

---

# B3 — Reflexive vs general Galois regime (summary; full argument in
`PHASE0_PARAMETER_SELECTION_RECOMMENDATION.md`)

New evidence gathered for this decision (`04_COMPUTATION/decision_support_checks.py`,
log `decision_support_log.txt`; 2 011 (code, s) instances over four parameter sets; the
double-dual assertion `(C^⊥)^⊥ = σ_{2s}(C)` held for **all** of them):

| | q=4, n=3, s=1 | q=9, n=2, s=1 | q=8, n=3, s=1 / s=2 | q=27, n=1, s=1 / s=2 |
|---|---|---|---|---|
| `r ∣ 2s` | **yes** | **yes** | no | no |
| # cyclic codes | 343 | 144 | 737 | 30 |
| form `b_s` is `σ_s`-Hermitian | 300/300 | 300/300 | **30/300, 38/300** | **13/300** |
| `F_p`-form `Tr∘b_s` symmetric (commutation matrix) | 300/300 | 300/300 | **138/300, 158/300** | **100/300, 96/300** |
| reflexive codes | 343/343 | 144/144 | **35/737** | **6/30** |
| codes with `σ_s`-Hermitian Gram | 343/343 | 144/144 | **35/737** | **6/30** |
| the two sets coincide | yes | yes | **yes (35 = 35)** | **yes (6 = 6)** |
| LCD codes | 64 | 64 | 640 | 30 |
| LCD ⇒ dual LCD | 64/64 | 64/64 | 640/640 | 30/30 |
| `dim Hull(C^⊥) = dim Hull(C)` | 343/343 | 144/144 | 737/737 | 30/30 |
| self-orthogonal / self-dual | 64 / **27** | 25 / **16** | 8 / **3** | 1 / **0** |

Two structural confirmations obtained independently of any code (Galois descent):

* `q = 8, n = 3`: `B = F_8 × F_64`; `σ_{2s} = Frob²` has order 3, with fixed field `F_2`
  on `F_8` and `F_4` on `F_64`. Galois descent ⇒ invariant subspaces number
  `1+3+1 = 5` and `1+5+1 = 7`, so `σ_{2s}`-invariant codes `= 5 × 7 = 35` — **exactly the
  35 observed**.
* `q = 27, n = 1`: `Frob²` has fixed field `F_3` on `F_27`; invariant subspaces of `F_3²`
  number `1+4+1 = 6` — **exactly the 6 observed**.

**Implication.** In the non-reflexive regime the loss is not uniform: it is a *per-code*
condition. A cyclic code `C` admits the standard (Hermitian/stabilizer) treatment
**iff `σ_{2s}(C) = C`** — and (proved direction) `σ_s`-Hermitian Gram ⇒ reflexive, with
the converse verified on all 1 254 codes and 2 011 instances.

| Area | Reflexive (`r ∣ 2s`) | General (non-reflexive) |
|---|---|---|
| Galois hull characterization | full: `Hull_s(C) = C ∩ C^⊥`, symmetric/Hermitian form, standard machinery | hull still a right module with `dim Hull(C^⊥) = dim Hull(C)`, but the form is not Hermitian except on `σ_{2s}`-invariant codes |
| duality / double dual | `C^{⊥⊥} = C` | `C^{⊥⊥} = σ_{2s}(C) ≠ C` in general (35/737) |
| LCD | works | works (verified 798/798; follows from `dim Hull(C^⊥) = dim Hull(C)`) |
| CSS | standard derivation applies | derivation uses `C^{⊥⊥} = C`; must be redone, or restricted to `σ_{2s}`-invariant codes |
| EAQECC (`c = dim C − dim Hull_s(C)`) | standard | the *number* is unchanged (isometry), but the commutation-matrix/symplectic argument needs a symmetric `F_p`-form, which fails (138/300) |
| quantum parameter derivations | standard | must be done by direct counting |

**Recommendation: option (3)** — reflexive regime primary (`s ≡ 0` Euclidean baseline, or
`r` even with `s = r/2` for the genuine Galois–Hermitian case), retain all general-`s`
theorems as companions, and allow the non-reflexive regime **only** on `σ_{2s}`-invariant
codes (35/737 at `q = 8`, 6/30 at `q = 27`), where every obstruction disappears.

Note the trade-off the data exposes: at comparable ambient dimension the reflexive regime
is far richer in self-orthogonal and self-dual codes (64/27 at `q = 4` versus 8/3 at
`q = 8`), while the non-reflexive regime is far richer in LCD codes (640/737 versus
64/343). If the intended application is hull/self-orthogonal-based (CSS/EA), the
reflexive regime is the right home; if it is LCD-based, either works.

---

# 4. Dependency map — what each decision unblocks

```
B1 ──► manuscript §5 (M_2(F_2) census, convention paragraph) and the A1 sentence in §1/§3
B2 ──► manuscript §1 (introduction, novelty, prior-art paragraph) and the bibliography
B3 ──► manuscript §3 (which statements carry "assume r | 2s"), §6 (Gray map: which
       duality relation it must respect), §7 (CSS/EA theorems)
                                    │
                                    └──► T-013/T-014 depend on B3; T-012 (Gray map) is
                                         independent of B1–B3 but is the highest-risk item
```

Nothing else is blocked: §2 (preliminaries), §4 (hulls and censuses) and the t = 2
material can be written as soon as B1/B2 are settled, independently of B3.

---

# 5. What happens after you answer

1. The three answers are recorded and applied **verbatim** to the manuscript plan.
2. Mechanical corrections already agreed (M4–M9 of
   `PHASE0_FINAL_GO_MODIFY_STOP.md`) are applied: 32 → 33, squarefree hypothesis,
   `m ≥ 2` in T-017, the new lemmas, the form-distinction sentence, `r ≥ 2` standing
   hypothesis.
3. Only then does Phase 1 (manuscript) begin, and only the sections unblocked above.

**Stopping point.** No further work will be done until these three boxes are ticked.
