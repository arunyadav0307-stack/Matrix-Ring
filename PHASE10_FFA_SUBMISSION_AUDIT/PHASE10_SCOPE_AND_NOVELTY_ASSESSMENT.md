# Phase 10 — Scope and novelty positioning for FFA

**Journal:** *Finite Fields and Their Applications*
**Audit date:** 2026-11-10 (guidelines and scope accessed 2026-11-10)
**Stance:** no inflated novelty. No record parameters are claimed anywhere in
this document, because none are claimed anywhere in the manuscript.

---

## 1. The specific test FFA applies

FFA's aims and scope name the application areas — algebraic coding theory,
cryptology, combinatorial design theory, pseudorandom number generation, linear
recurring sequences — but closes with the operative sentence:

> "There are other areas of application to be included, but **the important
> point is that finite fields play a nontrivial role in the theory,
> application, or algorithm**."

and:

> "… maintains **very strict refereeing standards, accepting only those papers
> which receive excellent referee reports**."

So the positioning question is not "is this coding theory?" — it plainly is.
The question is: **do finite fields carry nontrivial weight, or are they
incidental scenery?** The table below answers that for each of the seven
contribution areas named in the brief.

## 2. The seven contributions, assessed

### 2.1 Noncommutative matrix-ring cyclic codes — **IN SCOPE, with a framing caveat**

**What it is.** Cyclic codes as right ideals of `R_n = R[X]/⟨X^n−1⟩` with
`R = M_2(A_t)`, `A_t = F_q[u]/⟨u^t⟩`; the right-module convention is proved
forced, not chosen (`lem:failure`).

**Why finite fields are nontrivial here.** `F_q` is the residue field of the
chain ring `A_t`; `R_n ≅ M_2(B_q)` with `B_q = A_t[X]/⟨X^n−1⟩`; and `B_q`
decomposes by CRT into `F_{q^{d_j}}[w]/⟨w^{e_j}⟩`, where the `d_j` come from
the factorisation of `X^n − 1` over `F_q` — i.e. from cyclotomic cosets. The
framework's behaviour is governed by the arithmetic of `F_q`.

**The caveat, stated because a referee will find it in ten minutes.** The
manuscript itself observes (`03_preliminaries.tex` l.26–38) that `B_q` is
commutative, that `R_n ≅ M_2(B_q)`, and that under Morita, right ideals
correspond to `B_q`-submodules of `B_q^2` — "we do not reprove it". So the
structure theory is, after one standard equivalence, a theory of submodules of
the square of a **commutative** finite ring. The noncommutativity is genuine
and load-bearing in the *pairing* (the transpose in `θ_s = σ_s ∘ (·)^T` is
exactly what makes the dual of a right module a right module of the right
size), but it is not load-bearing in the *hull structure theory*.

**Positioning consequence.** Lead with the finite-field/chain-ring content and
with what the anti-automorphism buys. Do **not** sell the paper as
noncommutative ring theory — FFA is not the venue that rewards that framing,
and the Morita equivalence means a referee can deflate it in one line.

### 2.2 Galois duality and hull structure — **STRONGEST FIT**

**What it is.** `σ_s(a) = a^{p^s}` — the coefficient Frobenius — extended to
`A_t`, `R` and `R_n`; `θ_s = σ_s ∘ (·)^T`; the pairing
`b_s(x,y) = Λ(Σ θ_s(x_i) y_i)` with `Λ = λ ∘ tr` a Frobenius functional;
`C^{⊥_s} = rev(ann_r(θ_s(C)))` for arbitrary right ideals; hull theory with no
principality hypothesis; self-orthogonality with no reflexivity hypothesis.

**Why this is the most FFA-native part of the paper.** `σ_s` **is** the
Frobenius automorphism of `F_q`. The reflexive / general Galois regimes are
stated in terms of `r | 2s` where `q = p^r`. The CRT decomposition of `B_q`
and the `r`-dependence of the Frobenius order are finite-field theory in the
sense FFA uses the term. This is the part of the manuscript where finite fields
are not scenery but the engine.

**Assessment.** Verified in scope, and the natural centre of gravity for an
FFA submission.

### 2.3 Non-principal hull examples — **IN SCOPE, and unusually well suited**

**What it is.** The refutation: Galois hulls need not be principal. Hulls with
minimal generator number `MU_B = 3` exist, and `MU_B ≥ 3` forces **`t ≥ 2` and
`p | n`** (`thm:nonprincipal`). Plus `thm:noclosed`: no universal gcd-type
closed formula for the hull over this ring.

**Why FFA-shaped.** `p | n` is the repeated-root / wild case, and the
`p | n` versus `p ∤ n` dichotomy is a finite-field characteristic phenomenon.
The witnesses are explicit and small: `q = 4, t = 2, n = 2`; `q = 9, t = 2,
n = 3`; `q = 4, t = 2, n = 4`. The companion negative result (`thm:noclosed`)
is the kind of nonexistence statement FFA demonstrably publishes — Vol 112
(June 2026) carries "Counterexamples, constructions, and nonexistence results
for optimal ternary cyclic codes".

**Honest limit, stated by the manuscript.** Only the stronger reading
(O-3.1a — hulls of *arbitrary* codes) is refuted. The sharper question
(O-3.1b — can a *principal* code have a non-principal hull?) is **open** and
the manuscript claims nothing about it.

### 2.4 Gray-map compatibility — **WEAKEST FIT — do not lead with this**

**What it is.** The coefficient-expansion map `φ_n : R^n → F_q^{4tn}`, with
`thm:grayduality` (`φ_n(C^{⊥_s}) = φ_n(C)^{⊥̂_s}`) and `thm:grayhull`
(`φ_n(Hull_s(C)) = φ_n(C) ∩ φ_n(C)^{⊥̂_s}`, including the non-principal
hulls). Also `prop:qc`: the image is quasi-cyclic of index `4t` and co-index
`n`.

**Why it is weak for FFA.** `rem:noisometry` states that the homogeneous
weight on `M_2(F_q)` takes the values `0`, `1 + 1/(q²−1)` and
`1 − 1/((q−1)²(q+1))`, which are not integers, and concludes that **no** map
into any Hamming space is an isometry. So `φ_n` transports **duality and hulls
only**; it carries no metric content. FFA's interest in Gray-type maps (where
it has one) is metric — the cited ancestor is Greferath–Schmidt, *Gray
isometries for finite chain rings*. This paper's map is deliberately not an
isometry, and distances are computed directly on the image code.

**Assessment.** In scope as algebra — the transported form
`u^{[s]}(I_{4n} ⊗ H_t)v^T` is exact and interesting — but **"Gray map" is a
misleading headline for FFA** and belongs in the middle of the paper, not the
cover letter. The paper is honest about this; the framing should be too.

### 2.5 Quantum stabilizer and EAQECC constructions — **IN SCOPE as an application, weak as a headline**

**What it is.** Three routes of length `N = 4tn`: a Galois-native twisted
stabilizer route (R1), a Euclidean/CSS route (R2) and an entanglement-assisted
route (R3), plus `thm:obstruction` (`p = 2`, `t` even ⇒ no congruence ⇒ the
CSS route is unavailable for **every** code at those parameters).

**Scope.** FFA's aims and scope include applications in **information
theory**, and Vol 111 (March 2026) carries "Quantum MDS codes induced by the
projective linear transformation". Quantum code construction is therefore
**not** out of scope.

**Assessment.** In scope, and the paper's stated motivation — but it is
downstream of the algebra, and its parameter yield is weak (§2.7). Present it
as the application that justifies the machinery, not as the result.

### 2.6 Exact distance certifications — **IN SCOPE, and underestimated**

**What it is.** 28 codes certified by three independent methods (M1 complete
enumeration, M2 support search, M3 ambient quantum search); 5 055 codes with a
computed distance; 368 distinct `(N,K,d,c)` tuples, 88 non-dominated; all 5 055
verified against the EA Singleton bound and against the paper's own coset
Singleton bound. Appendix B gives the reproducibility path; `supplementary/`
carries 28 generator matrices, 8 CSVs, 24 scripts, 24 logs and a manifest.

**Why this matters for FFA specifically.** The scope statement explicitly
includes "**computational** aspects of finite fields as well as **algorithms**
and complexity of finite field-related methods". This is the one part of the
paper that speaks to that clause directly, and it is the part where the paper
is hardest to argue with: the numbers are reproducible from shipped artefacts
with a fixed seed (`SEED = 20261210`).

**Honest limits, all stated by the manuscript.** 15 of 42 families are
unreachable; 4 further families are counted but not enumerated; M3 is a
**lower bound** for most codes; two rows carry `d = 5` as a lower bound; the
Pareto frontier is a frontier **of the scanned families**, not of the
framework.

### 2.7 "Improved quantum parameter constructions" — **NOT AVAILABLE. Do not claim it.**

This is the one item in the brief that the manuscript cannot support, and the
audit says so plainly rather than finding a way to phrase it.

Verified from §9.2 (`sections/09_comparison.tex`) against Grassl's tables
(retrieved 2026-11-04; page last changed 10.06.2024):

| code produced | best known | position |
|---|---|---|
| `[[16,12,2]]_4`, `[[20,16,2]]_4`, `[[24,20,2]]_4` | 2 | **equal** — equality at `d = 2` is uninformative |
| `[[20,12,2]]_4`, `[[24,16,2]]_4` | 3 | 1 below |
| `[[16,4,3]]_4` | 5 | **2 below** |
| `[[20,4,4]]_4` | 6 | **2 below** |
| `[[16,8,3]]_9` | 4 | 1 below |
| `[[24,8,4]]_9` | 6 (bounds 6..8) | **2 below** |
| `[[24,12,3]]_9` | 5 (bounds 5..6) | **2 below** |

The manuscript's own words: "Every stabilizer code constructed here is at best
*equal* to the best known distance, and then only with `d = 2`, where equality
is uninformative. Every code with `d ≥ 3` is one or two below the best known
value. **No record parameter is claimed**, and none is implied."

The paper's largest distances are in the entanglement-assisted class
(`d = 10` at `[[20,2,10;18]]_4` and `[[24,2,10;18]]_9`) — and **those cannot be
benchmarked at all**, because codetables.de has no EA table (HTTP 404). The
`q = 8` codes are likewise unbenchmarked. Of 28 certified codes, 10 can be
compared and 18 cannot.

**Recommendation.** Item 7 must **not** appear in any future cover letter. If
the construction's parameters are mentioned at all, they should be mentioned
exactly as the manuscript mentions them: codes presented for their algebraic
origin, with the gap to best known stated. Any other framing is not supported
by §9.2 and would be contradicted by the first referee who opens the
comparison table.

## 3. The three strongest contributions for a future cover letter

Ranked for **FFA specifically** — i.e. by how much finite-field content they
carry and how well they survive FFA's "very strict refereeing standards", not
by how impressive they sound.

### 1. The Galois duality over `M_2(F_q[u]/⟨u^t⟩)`, and the refutation of principality

`θ_s = σ_s ∘ (·)^T` is an anti-automorphism, not an automorphism, and that is
what makes the dual of a right module a right module of the correct size;
hull theory is then developed for arbitrary right ideals; and the natural
conjecture that hulls are principal is **false**, with the phenomenon confined
by `MU_B ≥ 3 ⇒ t ≥ 2` **and** `p | n`.

*Why first.* `σ_s` is the Frobenius; `p | n` is a characteristic phenomenon;
the result is structural and includes a refutation. FFA publishes
nonexistence results. It is also the claim a referee cannot check by opening a
code table.

### 2. The exact transported form, and the two bounds

`φ_n` carries the Galois pairing to `u^{[s]}(I_{4n} ⊗ H_t)v^T` — a
`σ̂_s`-Hermitian form with **Hankel** Gram, not Euclidean unless `t = 1` —
and preserves duality and hulls, **including the non-principal ones**
(`thm:gram`, `thm:grayduality`, `thm:grayhull`). From the coset-distance
theorem (`d = min wt` of `D^{⊥_E}/Hull_E(D)`) follows the coset Singleton
bound `K + d ≤ N + 1`, proved **not** to be implied by the EA Singleton bound
(`prop:newsbound`).

*Why second.* It is exact and checkable, the Hankel structure is chain-ring
duality over `F_q`, and the bound comes with a stated independence proof — the
kind of claim that produces "excellent referee reports" rather than
"incremental".

### 3. The certification: 28 codes, three independent methods, reproducible

28 codes certified by M1/M2/M3; 5 055 codes with a computed distance; 368
distinct tuples; 88 non-dominated; every one checked against both the EA
Singleton bound and the new coset bound; 28 generator matrices, 8 CSVs, 24
scripts and 24 logs shipped with a fixed seed and a manifest.

*Why third.* FFA's scope names computation and algorithms explicitly, and this
is where the paper is verifiable rather than arguable. It also gives the
referee something concrete to check, which is the fastest route to a good
report.

**A credible fourth, if the letter has room.** `thm:obstruction`: for `p = 2`
and `t` even there is **no** matrix `T` with `T^T H_t T = I_t`, so the
Euclidean/CSS route is unavailable for every code at those parameters. A clean
nonexistence result in characteristic two — squarely finite-field content. The
manuscript itself warns that it must not be extended beyond `p = 2`, `t` even,
and any letter should respect that boundary.

## 4. What must not be claimed

| must not be said | why |
|---|---|
| "record parameters" / "best known" / "improved parameters" | §9.2: every `d ≥ 3` code is 1–2 **below** best known; the manuscript states this itself |
| "first quantum codes from Galois hulls over a non-chain ring" | the closest prior work (Zhang–Kong–Zheng, *Entropy* **28**(4) 407, 3 April 2026) does exactly this over a commutative non-chain ring |
| "a Gray isometry" | `rem:noisometry` proves no such map exists for this alphabet |
| "the principality conjecture is refuted" without qualification | only reading O-3.1a is refuted; O-3.1b (principal codes) is **open** |
| "the framework achieves distance `d`" generally | M3 is a lower bound for most codes; two rows carry `d ≥ 5` |
| "the Pareto frontier" as a property of the framework | it is a frontier of the **scanned families** only |
| "the characteristic-two obstruction is general" | it is proved for `p = 2`, `t` even only; congruences exist at `t = 1, 3, 5` |

## 5. One-sentence positioning, if it is wanted later

> The paper develops a Galois/Frobenius duality and hull theory for cyclic
> codes over `M_2(F_q[u]/⟨u^t⟩)` — which, by the Morita equivalence
> `R_n ≅ M_2(B_q)` with `B_q = F_q[u,X]/⟨u^t, X^n−1⟩` commutative, is a
> repeated-root problem governed by the factorisation of `X^n − 1` over
> `F_q` — refutes the principality conjecture for hulls with the exact
> obstruction `t ≥ 2` and `p | n`, identifies the transported form exactly as
> a Hankel-Gram `σ̂_s`-Hermitian form, and certifies the resulting quantum
> constructions by three independent computational methods.

That sentence is supported by the manuscript. Nothing in it is inflated, and
every clause maps to a numbered theorem.
