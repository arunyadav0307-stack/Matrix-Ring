# Phase 9A — Independent audit of the FFA recommendation

**Date:** 2026-11-10
**Auditor stance:** adversarial to the Phase 9 conclusion. Where the audit
confirms Phase 9 it says so; where it contradicts Phase 9 it says so and shows
the evidence.
**Baseline:** `PAPER/MatrixRingManuscript_20261110_Phase8B.zip` (read-only,
verified `6d39f643…86fec0`).
**Safeguards held:** no manuscript file modified; no Phase 9 file modified;
nothing recompiled; no cover letter; no submission; no journal-specific
formatting; no acceptance probability estimated.

---

## 1. Independent re-inspection of the manuscript

Phase 9 profiled the manuscript largely from its abstract, its own §9.4 novelty
list and its own self-audit. This audit re-read the source directly:
`main.tex`, all twelve section files, all 83 theorem-like environments, the
proofs, the 13 examples, and `references.bib`.

### 1.1 What the machinery actually is

The single most important structural fact, stated by the manuscript itself at
`03_preliminaries.tex` l.26–38:

> "The ring `B_q` is commutative, being a quotient of the commutative ring
> `A_t[X]`, and there is a canonical isomorphism `R_n ≅ M_2(B_q)` because `X`
> is central … Under this, right ideals of `R_n` correspond to `B_q`-submodules
> of `B_q^2`; this is the Morita correspondence we use repeatedly and **we do
> not reprove it**."

with `B_q = A_t[X]/⟨X^n − 1⟩ = F_q[u,X]/⟨u^t, X^n − 1⟩`.

Everything downstream is expressed through this dictionary:

| object | under Morita |
|---|---|
| cyclic code `C` (right ideal of `R_n`) | `B_q`-submodule `W ≤ B_q^2` |
| Galois dual `C^{⊥_s}` | `W' = W(C^{⊥_s})` |
| Galois hull `Hull_s(C)` | `I_{W ∩ W'}` (`prop:moritahull`) |
| principality of the hull | `MU_{B_q}(W ∩ W') ≤ 2` |
| `thm:noclosed` (no gcd-type closed formula) | a statement about `B_q`-modules |

**Audit finding A-1 (substantive).** The noncommutativity of `R = M_2(A_t)` is
genuinely present in the *set-up* and largely absent from the *structure
theory*. It is present where the manuscript says it is: `lem:failure` shows the
plain product fails on right modules and that the transpose in
`θ_s = σ_s ∘ (·)^T` is what makes the dual of a right module a right module of
the correct size; `prop:twoorth` records that a second orthogonality coincides.
But once the pairing is fixed, hull theory is the theory of intersections of
submodules of `B_q^2` over the **commutative** ring `B_q`, and the paper says
so. This is not a defect — the manuscript is candid — but it is the fact that
any competent referee will seize on, and Phase 9 did not record it.

**Audit finding A-2 (consequence).** The correct description of the paper's
mathematical content, for venue-matching purposes, is:

> a Galois/Frobenius duality and hull theory for submodules of `B_q^2`, where
> `B_q = F_q[u,X]/⟨u^t, X^n − 1⟩` is a commutative finite ring, with the
> `p | n` (repeated-root / wild) regime carrying the interesting structure,
> plus a coefficient expansion to `F_q^{4tn}` and an application to quantum
> code construction.

That is a *repeated-root cyclic code over a chain ring* paper with a Galois
twist and a quantum application. It is **not** a noncommutative-ring-theory
paper in the sense a reader of the title might expect. Venue matching should be
done against the former description, not the latter.

### 1.2 What the results actually are

Verified theorem inventory (83 environments; 21 theorems, 11 lemmas, 9
propositions, 2 corollaries, 8 definitions, 19 remarks, 13 examples):

**Structural core (§4–§6).** `thm:duality` (dual of a right module is a right
module; dimension formula); `thm:dualformula` (`C^{⊥_s} = rev(ann_r(θ_s(C)))`);
`thm:hullstruct`; `thm:nonprincipal` (**refutation**: `MU_{B_q} ≥ 3` requires
`t ≥ 2` **and** `p | n`); `thm:noclosed` (no universal gcd-type closed formula);
`prop:moritahull`; `prop:lcdso`; `thm:gram` (transported form
`u^{[s]}(I_{4n} ⊗ H_t)v^T`); `thm:grayduality`; `thm:grayhull`; `thm:hullso`
(self-orthogonality without reflexivity); `thm:obstruction` (`p = 2`, `t` even
⇒ no congruence ⇒ CSS route unavailable); `cor:noteuclid`.

**Quantum (§7).** `thm:fpbasis`; `thm:R1`/`thm:R1cap` (twisted route — distance
only **upper**-bounded); `thm:R2` (Euclidean/CSS); `thm:R3` (EA route);
`thm:parameters`; `thm:cosetdistance` (distance = min weight of
`D^{⊥_E} / Hull_E(D)`); `thm:cosetsingleton` (`K + d ≤ N + 1`);
`thm:feasibility`; `thm:bookkeeping`.

**Certification (§8).** 5 055 codes with a computed distance; 368 distinct
`(N,K,d,c)` tuples; 88 non-dominated; all satisfy the EA Singleton bound and
the new coset bound (`prop:bounds`, `prop:frontier`).

### 1.3 Three things the independent read found that Phase 9 did not record

**(a) The Gray map is not an isometry, and the manuscript says so.**
`rem:noisometry`: the homogeneous weight on `M_2(F_q)` takes values
`0`, `1 + 1/(q²−1)` and `1 − 1/((q−1)²(q+1))`, which are not integers, so "**no**
map into any Hamming space is an isometry". The coefficient expansion `φ_n`
therefore transports **duality and hulls only** (`thm:grayduality`,
`thm:grayhull`); distances are computed directly on the image code.
Consequence: the paper has no weight-theoretic machinery, which is why §8 is a
brute-force scan and why 15 of 42 families are unreachable (minor issue m-4).
Referees at a venue that values isometry/Gray-map technique (the
Greferath–Schmidt line, which the paper cites) will notice this.

**(b) The comparison table is uniformly unfavourable.** §9.2, verified line by
line: every stabilizer code produced is at best **equal** to the best known,
and only with `d = 2` where equality is uninformative. Every code with `d ≥ 3`
is **one or two below** the best known value:

| code | best known | gap |
|---|---|---|
| `[[16,4,3]]_4` | 5 | 2 below |
| `[[20,4,4]]_4` | 6 | 2 below |
| `[[16,8,3]]_9` | 4 | 1 below |
| `[[24,8,4]]_9` | 6 (bounds 6..8) | 2 below |
| `[[24,12,3]]_9` | 5 (bounds 5..6) | 2 below |

Phase 9 described `[[24,8,4]]_9` and `[[20,4,4]]_4` as "the first stabilizer
distance 4 in this framework". That is accurate as an **internal** milestone and
the manuscript does not overstate it — but the external position is 2 below
best known, and Phase 9 did not say so.

**(c) The entanglement-assisted codes are unbenchmarkable, by the paper's own
admission.** §9.1: Grassl's tables cover stabilizer codes only; there is no EA
table (HTTP 404); only `q = 4` and `q = 9` are tabulated. The paper's **largest**
distances (`d = 10` at `[[20,2,10;18]]_4`, `[[24,2,10;18]]_9`) are in the EA
class and therefore cannot be compared to anything. The manuscript argues this
is a gap in the literature. A referee may instead read it as: the best numbers
in the paper are unverifiable.

### 1.4 Integrity signals (positive)

* The manuscript records its own prior error: an earlier phase misread Grassl's
  prime-vs-field labelling and wrongly concluded `q = 9` was not covered; this
  is logged as an erratum (§9.1).
* It records a second error: an earlier version stated `c + K = N − k`, which is
  false and contradicted by 23 of 25 rows (§7 remark).
* It separates two readings of the refuted conjecture — O-3.1a (all codes)
  refuted, O-3.1b (principal codes) explicitly **open** (`rem:o31b`).
* `rem:obstructionexact` warns that `thm:obstruction` is `p = 2` **and** `t`
  even and "must not be extended".
* `prop:frontier` states the frontier is of the **scanned** families only.

This is an unusually self-critical manuscript. It is an asset with careful
referees and irrelevant to a screener.

---

## 2. Verification of the cited "FFA papers" — **Phase 9 claim falsified**

Phase 9 asserted, in three separate deliverables, that the manuscript's
bibliography demonstrates lineage into FFA:

> "Two of the 13 cited works are FFA papers: Fan–Zhang 2017 (Galois self-dual
> constacyclic codes) and Liu–Pan 2020 (Galois hulls of constacyclic codes)."
> — `PHASE9_FINAL_RECOMMENDATION.md` §2.1

**This is false.** Direct read of `sources/references.bib`, then independent
verification:

| Phase 9 claim | actual venue (from `references.bib`) | independent verification | verdict |
|---|---|---|---|
| Fan–Zhang 2017 is an FFA paper | **Designs, Codes and Cryptography** 84(3), 473–492, doi 10.1007/s10623-016-0282-8 | Springer article page confirms: "Designs, Codes and Cryptography", Volume 84, pages 473–492 (2017), published 29 Sep 2016 | **Phase 9 wrong** |
| Liu–Pan 2020 is an FFA paper | **Designs, Codes and Cryptography** 88(2), 241–255, doi 10.1007/s10623-019-00681-2 | Confirmed by four independent reference lists (arXiv 2405.02285, 2505.08506, 2210.05551, AMC 10.3934/amc.2025010) | **Phase 9 wrong** |
| Cao 2021 (MDS Galois hulls) is a Discrete Mathematics paper | **IEEE Trans. Inform. Theory** 67(12), 7964–7984 | Confirmed by five independent sources incl. the author's own BIMSA publication list | **Phase 9 wrong** |
| Dinh 2024 (cyclic codes over rings of matrices) is a JAA paper | **Advances in Mathematics of Communications** 18(4), 1100–1122, doi 10.3934/amc.2022073 | Official AIMS article page: "Advances in Mathematics of Communications, 2024, Volume 18, Issue 4: 1100-1122" | **Phase 9 wrong** |

**Corrected venue distribution of the 13 cited works:**

| venue | count | which |
|---|---|---|
| **IEEE Trans. Inform. Theory** | **3** | Greferath–Schmidt 1999; Cao 2021; Ketkar et al. 2006 |
| **Designs, Codes and Cryptography** | **2** | Fan–Zhang 2017; Liu–Pan 2020 |
| **Entropy** | **1** | Zhang–Kong–Zheng 2026 |
| **Adv. Math. Commun.** | **1** | Dinh 2024 |
| **Cryptography and Communications** | **1** | Luo–Parampalli 2018 |
| J. Franklin Inst. | 1 | Alahmadi et al. 2013 |
| AIMS Mathematics | 1 | Si–Niu 2023 |
| Amer. J. Math. | 1 | Wood 1999 |
| arXiv preprint | 1 | Joshi–Patel–Prakash 2026 |
| online tables | 1 | Grassl |
| **Finite Fields and their Applications** | **0** | — |
| **Discrete Mathematics** | **0** | — |
| **J. Algebra Appl.** | **0** | — |

**Audit finding A-3 (critical).** The manuscript cites **zero** FFA papers. The
"lineage runs through FFA" argument in `PHASE9_FINAL_RECOMMENDATION.md` §2.1
point 2 is unsupported and must be withdrawn. Its converse is true and was
missed: **the two papers that founded the Galois-duality / Galois-hulls
subfield that this manuscript works in — Fan–Zhang 2017 and Liu–Pan 2020 — are
both DCC papers**, and the manuscript cites both. The strongest bibliographic
lineage in the paper points at **DCC**, not FFA.

**Audit finding A-4.** Dinh et al. 2024 — cyclic codes over the *same* matrix
ring family `M_2(F_2[u]/⟨u^k⟩)` — is an **AMC** paper, not JAA. Phase 9's
"we cite Dinh 2024 here [JAA]" is wrong, and the error understated AMC's claim.

---

## 3. Verification of FFA's recent related publications

Phase 9 claimed: "Volumes 109 (Jan 2026), 110 (Feb 2026) and 111 (Mar 2026)
all carry constacyclic/cyclic-code papers, including Graner's closed-form
generators and a cyclotomic-coset construction." This audit read the actual
tables of contents.

### 3.1 FFA Vol 111 (March 2026) — verified contents

1. Editorial board
2. A provably quasi-polynomial algorithm for the **discrete logarithm problem** in finite fields of small characteristic (Lido) — OA
3. On the Hermitian Veronesean (Bamberg, Van de Voorde)
4. Maps preserving a fixed rank-distance on matrices over finite fields
5. On the `PGL_2(q)`-orbits of lines of `PG(3,q)` and binary quartic forms in characteristic three
6. **Explicit representatives and sizes of cyclotomic cosets and their application to cyclic codes over finite fields** (Zhu, Liu, Wu)
7. Permutation polynomials and involutions over `F_{2^{2m}}` (Qian, Shi, Cao)
8. **Quantum MDS codes induced by the projective linear transformation** (Li, Liu, Jiang)
9. On two conjectures of the duals of AMDS BCH codes (Yan)
10. Linear codes arising from the point-hyperplane geometry — Part I: Segre embedding
11. Multiplicative character sums over two classes of subsets of quadratic extensions
12. Criteria of maximality and minimality of van der Geer–van der Vlugt curves
13. A family of optimal dual-containing and reversible linear codes over `F_4`
14. Cycles and cuts in supersingular `L`-isogeny graphs
15. Two classes of NMDS codes from Roth–Lempel codes

### 3.2 FFA Vol 110 (February 2026) — verified contents (extract)

* Finite fields whose members are the sum of a potent and a 4-potent
* Mean value theorems for short rational exponential sums
* Large cyclic subspace codes over finite fields
* The dual codes of two families of BCH codes
* Weierstrass semigroups and automorphism group of a maximal function field
* **Trace duality and additive complementary pairs of additive cyclic codes over finite chain rings** (Bhowmick, Deka, Fotue Tabue, Martínez-Moro) — OA
* Brocard–Ramanujan problem for polynomials over finite fields
* Estimates on the number of rational solutions of Markoff–Hurwitz equations
* Automorphism groups of the fields of definition of torsion points of elliptic curves
* Superspeciality of genus-two curves; supersingular curves of genus five

### 3.3 FFA Vol 112 (June 2026) — verified contents (extract)

* Hermitian–Singer functional and differential codes
* **Construction of several infinite families of linear codes with new parameters: Hamming weight enumerators and hull dimensions** (Lavanya G, Sharma)
* **Counterexamples, constructions, and nonexistence results for optimal ternary cyclic codes** (Bao, Zou)
* Function-correcting codes with homogeneous distance
* Twisted group algebra of dihedral groups over finite fields
* Permutation polynomials (×2); De Bruijn tori; quasi-optimum distance flag codes
* Binary linear codes with at most three weights from cyclotomic mappings
* Easy repair via codes with simplex locality

### 3.4 Audit reading

**Audit finding A-5.** Phase 9's characterisation is *literally* true and
*substantively* misleading. Across three sampled 2026 volumes of FFA:

* **Directly relevant:** one paper — "additive cyclic codes over finite chain
  rings" (Vol 110).
* **Topically adjacent:** "hull dimensions" (Vol 112, but over finite fields),
  "cyclic codes over finite fields" via cyclotomic cosets (Vol 111), "quantum
  MDS codes" (Vol 111, over finite fields).
* **Not relevant:** the modal FFA paper — discrete logarithms, exponential
  sums, permutation polynomials, curves and function fields, finite geometry,
  isogeny graphs — roughly 12–15 of ~20 articles per volume.
* **Zero** papers on Galois hulls over rings, on matrix rings, or on quantum
  codes from hulls over rings, in any of the three volumes sampled.

The "Graner closed-form generators, Vol 109" claim was never verified against
an official page in Phase 9 (it came from a search snippet) and remains
**UNVERIFIED**; this audit did not confirm it.

**Audit finding A-6 (the decisive one for FFA).** FFA does publish
negative/nonexistence results (Vol 112: "Counterexamples, constructions, and
nonexistence results") and does publish codes over chain rings (Vol 110). So
the *genre* is not excluded. But FFA's coding-theory papers are
**parameter-forward**: "new parameters", "optimal", "NMDS", "quantum MDS",
"large cyclic subspace codes". A manuscript whose every `d ≥ 3` code is 1–2
below the best known (§1.3(b)) and whose best numbers are unbenchmarkable
(§1.3(c)) runs against that grain. The manuscript's real strengths — the
refutation, the exact Hankel Gram, the two bounds — are structural, and FFA
has no recent precedent for valuing *that* combination in a coding paper.

---

## 4. Is FFA an appropriate venue? — the audit's assessment

### 4.1 The case for FFA that survives the audit

1. **Stated scope genuinely covers it.** FFA's aims and scope name algebraic
   coding theory, cryptology and combinatorial design theory — verified on the
   official journal page.
2. **After Morita, the object is FFA-shaped.** `B_q = F_q[u,X]/⟨u^t, X^n−1⟩`
   and its CRT decomposition into `F_{q^{d_j}}[w]/⟨w^{e_j}⟩` are finite-field
   and chain-ring objects, and the `p | n` regime is exactly the repeated-root
   case that FFA publishes (Vol 110). The Frobenius `σ_s` is finite-field
   arithmetic.
3. **FFA demonstrably publishes adjacent work:** cyclic codes over finite
   chain rings (Vol 110), hull dimensions (Vol 112), negative results
   (Vol 112).
4. **FFA publishes 8 volumes a year** (Vols 109–116 in 2026), roughly 15–25
   articles each — there is room.
5. **The subscription route is free**; gold OA USD 3 240 is optional.
6. **Q1 / SJR 0.906 / h-index 60** — reported, not used as a reason.

### 4.2 The case against, as developed by this audit

1. **The lineage argument collapses.** Zero FFA papers cited (§2). The
   subfield's founding papers are DCC's.
2. **The "recent related work" evidence was overstated.** One directly
   relevant paper in three sampled volumes, none in-genre (§3.4).
3. **The advertised novelty is the part FFA is least placed to value.** The
   noncommutative framing is largely removed by the Morita equivalence the
   paper itself invokes (§1.1). FFA's finite-field expertise does not extend
   naturally to "what survives after Morita", and the residue is commutative
   ring/module theory — respectable, but not FFA's distinctive strength.
4. **Parameter position is unfavourable, in a parameter-forward venue**
   (§1.3(b), §3.4).
5. **No isometry** (§1.3(a)) in a lineage where the Gray-isometry paper
   (Greferath–Schmidt, IEEE TIT) is a cited ancestor.
6. **Two scoring inputs in Phase 9 were wrong in FFA's favour**: B was scored
   5 and C was scored 5. On the evidence assembled here, B = 4 and C = 3 is
   the defensible reading (see `PHASE9A_SCORING_SENSITIVITY.md` §2).

### 4.3 Conclusion on suitability

**FFA is a defensible venue. It is not the best-supported venue.**

It is defensible because the corrected description of the paper's content
(§1.1) lands on repeated-root cyclic codes over a chain ring with a Galois
twist, which FFA does publish, and because FFA tolerates negative results.

It is not the best-supported venue because the specific argument Phase 9 used
to place it first — bibliographic lineage plus three consecutive volumes of
related work — does not survive verification, and because the genre in which
the manuscript actually sits (quantum codes from hulls of codes over rings) has
verifiable recent homes elsewhere, not in FFA.

The detailed comparison, including the corrected scores and the sensitivity
analysis, is in `PHASE9A_SCORING_SENSITIVITY.md` and
`PHASE9A_ALTERNATIVE_JOURNAL_REASSESSMENT.md`.
