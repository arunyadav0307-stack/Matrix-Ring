# Phase 0 — Final Researcher Decision Form

**State pinned at commit `ce856e0`.** No existing file is modified by this form; no Phase 1
work has started (`05_MANUSCRIPT/` is empty). **B1, B2 and B3 remain open** — this sheet
states only the mathematical consequences of each option, so that the choice can be made
on the mathematics.

Evidence pointers (already on the branch): `06_AUDIT/PHASE0_U8_U9_DECISIONS.md`,
`PHASE0_FINAL_NOVELTY_STATEMENT.md`, `PHASE0_PARAMETER_SELECTION_RECOMMENDATION.md`,
`04_COMPUTATION/decision_support_log.txt`.

**What changes if you answer nothing:** nothing. Every proved result below holds as stated
regardless of these three choices; B1–B3 affect only *framing*, *which hypotheses the
quantum theorems carry*, and *what we say about one cited paper*.

---

## B1 — Alahmadi, Sboui, Solé, Yemen (2013), Theorem 1

*Facts (not in dispute):* the recorded statement lists generators that divide `X^n − 1`
for **two different lengths** (`X²+X+1 ∣ X³−1`; `X³+X+1`, `X³+X²+1 ∣ X⁷−1`) — internally
inconsistent. A1's "8" is the **quaternary**-convention count at `n = 3`; our 35 is the
**right-ideal** count. A1's Euclidean form `Σ x_j y_j` is degenerate (`dim C + dim C^⊥`
not constant: `[(6,15),(8,10),(10,6),(12,4)]`; **0** self-dual codes), whereas our form
`Σ tr(x_j^T y_j)` satisfies `dim C + dim C^⊥ = 12` for **35/35** and admits **3**
self-dual codes.

| | **(a) Re-read and fully reconcile** | **(b) Cite the framework only** |
|---|---|---|
| Immediate consequence | §5 blocks until the source is obtained and the statement (length `n`, role of `j`/`ℓ`, convention (I) or (II), form) is recovered | §5 is written now from our own census |
| If the source confirms a *different* statement | We present both conventions; their theorem stands; our census is unaffected (it counts a different family) | — not applicable |
| If the source is mis-transcribed in *our* record only | We may restate it correctly; no claim of error against the paper | — |
| If the published statement itself is defective | We may say so **only** with an exact quotation and a full re-derivation | We never raise it |
| Effect on our mathematics | **None** (T-001…T-018, T-020, T-022…T-028 stand) | **None** |
| Effect on T-019 | stays "adjudication requested" | re-labelled "convention diagnosis" (it is a proved computational fact about triples) |
| Reversible | **No** (a published correction is permanent) | **Yes** — (a) can be added later as a remark or a second paper |
| Risk | High: mis-stating a published theorem | Very low |
| Delays | §5, and the A1 sentences in §1/§3; T-012/T-013 slip | nothing |

**Audit recommendation: (b).** Asymmetric evidence (we can prove everything (b) needs;
we can verify no clause of the recorded theorem) and asymmetric risk ((b) reversible,
(a) not). The genuine finding — the (I)/(II) convention split and the degeneracy of
`Σ x_j y_j` — is publishable under (b) without any claim about their theorem.

☐ (a) ☐ (b) ☐ other: ______________________

---

## B2 — Novelty claim

*Facts:* Wood 2010 is precisely "anti-isomorphism + duality over non-commutative rings";
Szabo–Wood 2017 prove module structure, double-dual, cardinality complementarity and
MacWilliams for non-degenerate sesquilinear forms over finite Frobenius rings; Solé
(MMS 2011) studies cyclic self-dual codes over `M_2(F_2)`.

| | **(a) Keep the broad claim** ("we introduce duality via an anti-automorphism") | **(b) Narrowed four-part claim** |
|---|---|---|
| Exposure | Priority objection at the first reading: three directly overlapping references | Claim is scoped to what the references do not contain |
| What must be rewritten | §1 after referee report (and possibly the framing of §3) | §1 once, now |
| Bibliography | unchanged (+0) | +6 (Wood 2010; Szabo–Wood 2017; NRS 2006; Dougherty–Leroy 2016; Solé 2011; Kushwaha–Prakash ×2) |
| Our mathematics | **unchanged** | **unchanged** |
| Claim level | Q1 asserted, Q2 delivered | Q2 now; Q1 only if T-012/T-013 land |
| Excluded claims | none | five listed in `PHASE0_FINAL_NOVELTY_STATEMENT.md` §3 |

What **(b)** retains as ours: the explicit family `θ_s = σ_s ∘ transpose`; the identity
`θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)`; the twisted double dual `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`;
the criterion `r ∣ 2s` (with `m ≥ 2` essential); the σ_{2s}-isometry and parameter
invariance; **Galois hulls of cyclic codes over matrix rings**; the censuses; the
squarefree counterexample.

**Audit recommendation: (b).** ☐ (a) ☐ (b) ☐ other: ______________________

---

## B3 — Galois parameter regime

*Facts* (2 011 (code, *s*) instances, four parameter sets; `(C^⊥)^⊥ = σ_{2s}(C)` held for
every one):

| | reflexive (`r ∣ 2s`) | non-reflexive |
|---|---|---|
| `b_s` is `σ_s`-Hermitian | 300/300 | **30/300, 13/300** |
| commutation form `Tr∘b_s` symmetric | 300/300 | **138/300, 100/300** |
| reflexive codes | all | **35/737** (q=8), **6/30** (q=27) |
| self-orthogonal / self-dual | 64 / **27** (q=4), 25 / **16** (q=9) | 8 / **3** (q=8), 1 / **0** (q=27) |
| LCD | 64/343, 64/144 | **640/737**, 30/30 |

| | **(1) General regime primary** | **(2) Reflexive primary** | **(3) Hybrid** |
|---|---|---|---|
| Galois hull characterization | hull fine; only the *twisted* symmetry `b_s(y,x) = σ_s(b_s(σ_{−2s}x,y))` | σ_s-Hermitian; standard | both, split by hypothesis |
| Duality / double dual | `C^{⊥⊥} = σ_{2s}(C) ≠ C` (35/737) | `C^{⊥⊥} = C` | both statements proved |
| LCD | works (798/798 verified) | works | works — regime-independent |
| CSS | needs a bespoke counting proof; commutation form **not symmetric** (138/300) | standard derivation | standard under `r ∣ 2s`; else restricted to `σ_{2s}`-invariant codes |
| EAQECC (`c = dim C − dim Hull`) | `c` unchanged (isometry), but the rank/symplectic argument unavailable | standard | standard under `r ∣ 2s` |
| Parameter derivations | must avoid every `C^{⊥⊥}` step | standard | standard under `r ∣ 2s` |
| Families available | any `r ≥ 2` (q=8 `s=1,2`; q=27 `s=1,2`) | `s ≡ 0`, or `r` even with `s = r/2` (q=4, 9, 16, 25) | both, with `q=8`/`q=27` as the failure case |
| New work created | a counting-based CSS/EA derivation (unwritten) | none | two small proofs (see below), or state as computational |
| Richness | LCD-rich (87 %) | self-orthogonal/self-dual-rich (64/27) | both exploited |
| Risk | high | low | low |

Extra facts specific to **(3)**: the `{Hermitian Gram}` and `{σ_{2s}-invariant}` families
coincide **as sets** in every parameter set (35 = 35; 6 = 6); the counts 35 and 6 are
predicted exactly by Galois descent (`5×7` and `6`); `dim Hull(C^⊥) = dim Hull(C)` for
1 254/1 254 codes. Two items would need proofs (or explicit `[EXH]` labels): the converse
"reflexive ⇒ Hermitian Gram", and `dim Hull(C^⊥) = dim Hull(C)`.

Note for **(2)**: for `r` odd, a non-trivial Galois action and reflexivity are mutually
exclusive, so `q = 8` and `q = 27` leave the quantum sections entirely.

**Audit recommendation: (3)** — §7 theorems carry `r ∣ 2s`; all general-*s* theorems
(double dual, size formula, cyclicity, hull closure, isometry, parameter invariance) are
retained as companions; the non-reflexive regime is used only on `σ_{2s}`-invariant codes.

☐ (1) ☐ (2) ☐ (3) ☐ other: ______________________

---

## Unaffected by all three decisions

The proved core: T-001…T-011, T-015…T-018, T-020…T-028; the corrected `t = 2` census
(**33**, not 32, with the structural formula `q²+3q+5`); the squarefree-hypothesis
counterexample (`q=4, n=2`: 33, not 49); the `m ≥ 2` requirement in T-017; the standing
hypothesis `r ≥ 2`; and the rule that `q = 2` is enumerator validation only.

## After you answer

1. Your three choices are applied **verbatim**; nothing else changes.
2. Mechanical corrections already agreed (32 → 33; squarefree hypothesis; `m ≥ 2`; new
   lemmas; the form-distinction sentence; `r ≥ 2`) are applied to the register and the
   three revision reports.
3. Only then does Phase 1 (manuscript) begin, and only for the sections your answers
   unblock (B1 → §5 and two sentences in §1/§3; B2 → §1; B3 → §3, §6, §7).

---

**Researcher's answer**

B1: ☐ (a) ☐ (b) ☐ other ____________________  B2: ☐ (a) ☐ (b) ☐ other ____________________
B3: ☐ (1) ☐ (2) ☐ (3) ☐ other ____________________

Approved by: ____________________  Date: ____________
Additional instructions: ______________________________________________

*Waiting for explicit approval. No further work will be carried out until then.*
