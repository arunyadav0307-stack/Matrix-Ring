# Phase 0 — Novelty Re-assessment (literature audit)

**Purpose.** Re-check the closest papers, quantify the overlap with our theorems, and
state a novelty claim we can actually defend. No Q1 claim is made; the claim below is
deliberately narrower than the one carried into the Phase-0 revision.

---

## 1. Verdict

**The novelty claim must be downgraded (F-02).** The statement

> "we introduce a duality for codes over a non-commutative ring via an anti-automorphism"

is **prior art**, and has been since 2010. What survives as new is narrower but still
substantial: the **explicit** family `θ_s = σ_s ∘ transpose` on `M_m(F_q[u]/⟨u^t⟩)`, the
**double-dual formula `C^{⊥⊥} = σ_{2s}(C)` with the reflexivity criterion `r | 2s`**, the
**Galois (σ_s-) hulls of *cyclic* codes over *matrix* rings**, and the censuses.

---

## 2. Prior art that directly overlaps (must be cited as the foundation)

| Ref | What it proves | Overlap with us |
|---|---|---|
| **J. A. Wood**, *Anti-isomorphisms, character modules and self-dual codes over non-commutative rings*, Int. J. Inf. Coding Theory **1**(4) (2010) 429–444, doi:10.1504/IJICOT.2010.032867 | "It is an elaboration on ideas of Nebe, Rains and Sloane: by assuming the existence of an **anti-isomorphism** on a finite ring and by assuming a module alphabet has a well-behaved duality, one is able to study self-dual codes defined over alphabets that are modules over a non-commutative ring." | **This is our θ_s.** The idea "use an anti-isomorphism to dualise over a non-commutative ring" is his (building on NRS). We must not claim it. |
| **S. Szabo, J. A. Wood**, *Properties of dual codes defined by nondegenerate forms*, J. Algebra Comb. Discrete Struct. Appl. **4**(2) (2017) 105–113, doi:10.13069/jacodesmath.284934 (MR3601342, Zbl 1423.94156) | Over a **finite Frobenius ring**, duals w.r.t. non-degenerate **sesquilinear** forms (relative to an anti-automorphism) and bilinear forms: module structure of the dual, **double-dual property**, cardinality complementarity, **MacWilliams identities**; a referee remark that the sesquilinear case is a special case of the bilinear one. They work with `A` Frobenius, `ρ` a generating character, `σ` an anti-automorphism, and a non-degenerate σ-sesquilinear form, and assume **hermitian** in places. | Our T-007/T-010/T-016 sit inside this framework. **Open check (F-13):** whether their double-dual and MacWilliams statements cover a *non-involutive* anti-automorphism. If they do, our T-016 is a special case of a published theorem (still fine, but must be presented as such); if they require an involution, our σ_{2s}-twisted version is new. |
| **G. Nebe, E. M. Rains, N. J. A. Sloane**, *Self-Dual Codes and Invariant Theory*, Alg. Comput. Math. **17**, Springer 2006 | Form rings / types over finite rings, including **non-commutative** examples such as `F_q + F_q u` with `u² = 0` (and `ua = a^q u`); Clifford–Weil groups and genus-`m` weight enumerators. | The general theory of self-dual codes over non-commutative Frobenius rings; the "type" formalism is the right language for our forms. |
| **S. T. Dougherty, A. Leroy**, *Euclidean self-dual codes over non-commutative Frobenius rings*, AAECC **27** (2016) 185–203, doi:10.1007/s00200-015-0277-0 | Left and right orthogonals over a non-commutative Frobenius ring; a code equals its left orthogonal **iff** its right orthogonal; constructions from self-dual codes over the centre. | Directly relevant to the left/right convention question (U8) and to the "two-sided" option. |
| **J. A. Wood**, *Duality for modules over finite rings and applications to coding theory*, Amer. J. Math. **121** (1999) 555–575 | Frobenius rings are exactly the alphabets with a perfect duality / extension theorem. | Already cited by us as E-001. |

## 3. Prior art on **our alphabet family** (matrix rings)

| Ref | What it does | Gap we fill |
|---|---|---|
| **P. Solé**, *Cyclic codes and self-dual codes over `M_2(F_2)` and `M_2(F_2[i])`*, 11th Mediterranean Microwave Symposium (MMS) 2011, doi:10.1109/MMS.2011.6068573 | Cyclic **self-dual** codes over `M_2(F_2)` "by analogy with the `Z_4` case"; factorisation of `X⁷+1` over `M_2(F_2)` and a factorisation of `X^m+1` over `M_2(F_2[i])`. | **Closest predecessor on the same alphabet**: cyclic + a duality over `M_2(F_2)`. But: no Galois twist, no θ_s-family, no `r|2s` phenomenon (their field is `F_2`/`F_2[i]`), no hulls, no quantum. Cite and differentiate. |
| **F. Oggier, P. Solé, J.-C. Belfiore** et al., codes over matrix rings for space-time coding (`M_2(F_2)`, `M_2(F_2[i])`, cyclic algebras) | Matrix rings as code alphabets; division-algebra/cyclic-algebra codes for MIMO. | Establishes the alphabet as legitimate; no duality/hull/Galois theory. |
| Alahmadi–Sboui–Solé–Yemen (2013) — A1 | Cyclic codes over `M_2(F_2)`; quaternary correspondence; residue/torsion; a duality theorem (see U8, F-01). | Framework yes; theorem: see U8. |

## 4. Prior art on **hulls over non-commutative rings**

| Ref | What it does | Gap we fill |
|---|---|---|
| **Kushwaha & Prakash**, *Hulls of free linear codes over a non-unital ring*, arXiv:2512.12335 (Dec 2025); *Symplectic hulls over a non-unital ring*, arXiv:2601.06609 (Jan 2026) | Left / right / **two-sided** hulls over the 4-element non-commutative **non-unital** ring `E = ⟨κ,τ⟩`; residue and torsion codes, generator matrix of the hull, build-up constructions, hull variation, classification up to length 8 (Euclidean and symplectic). | Confirms "hulls over non-commutative alphabets" is an active niche — but with **no** Galois action, **no** matrix ring, **no** cyclic/constacyclic structure, and a ring that is not even unital. Our setting is disjoint; cite as evidence of timeliness. |

## 5. Prior art on **Galois hulls → quantum codes**

| Ref | What it does | Gap we fill |
|---|---|---|
| **Zhang, Kong & Zheng**, *Quantum Codes from Galois Hulls of Constacyclic Codes over a Finite Non-Chain Ring*, Entropy **28**(4) 407 (2026), doi:10.3390/e28040407 | ℓ-Galois hulls of constacyclic codes over a **commutative** non-chain ring; CSS + Hermitian + Construction X; QMDS/EAQEC. | The **template** for our Phase 6 — but commutative, Gray-mapped, no anti-automorphism. Cite as the "closest competitor" and as the benchmark for the parameter tables. |
| **Li & Liu**, *Cyclic codes over a semi-local ring and their applications to QEC and EAQEC codes*, Quantum Inf. Process. **24**:49 (2025) | Euclidean sums and hulls over a commutative ring → QEC/EAQEC. | Same remark. |
| **Debnath & Prakash**, *Hulls of Cyclic Codes Over a Local Ring*, ICTIS 2025 (Springer, 2026) | Hull dimensions / LCD over a commutative local ring. | Same remark. |
| **Yadav, Debnath, Prakash**, *Some constructions of ℓ-Galois LCD codes*, Adv. Math. Commun. **19**(1) (2025) 227–244 | ℓ-Galois LCD over finite fields. | Field case of the Galois-dual idea. |
| *W-δ-μ dual codes and LCD codes*, arXiv:2606.13467 (2026) | σ-inner products and σ-duals for **classical and quantum** codes, σ a semilinear automorphism of `F_q^n` (cites [3],[4] for σ-duals in quantum coding). | Shows σ-duals for quantum codes are established over **fields**; ours is the matrix-ring/non-commutative analogue. Useful for positioning §7. |

## 6. What we may claim (defensible wording)

> **Not new (cite as foundation).** Duality for codes over a finite Frobenius ring defined
> by a non-degenerate form attached to an anti-automorphism (Wood 2010; Szabo–Wood 2017;
> Nebe–Rains–Sloane 2006); left/right orthogonal theory over non-commutative Frobenius
> rings (Dougherty–Leroy 2016); self-dual cyclic codes over `M_2(F_2)` (Solé 2011);
> hulls over non-commutative rings (Kushwaha–Prakash 2025/26); Galois hulls of
> constacyclic codes over commutative rings and their quantum applications
> (Zhang–Kong–Zheng 2026 and predecessors).
>
> **New, as far as we can establish.** (i) The explicit anti-automorphism family
> `θ_s = σ_s ∘ transpose` on `M_m(F_q[u]/⟨u^t⟩)` and the associated pairing
> `B_s(x,y) = Σ θ_s(x_e) y_e`; (ii) the **double-dual formula**
> `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)` together with the identity
> `θ_s(B_s(x,y)) = B_s(y, σ_{2s}x)` and the **reflexivity criterion `r | 2s`**, including
> the structural consequence that for odd `r` a non-trivial Galois action and reflexivity
> are mutually exclusive; (iii) the σ_{2s}-**isometry** lemma: even in the non-reflexive
> regime, size, weight enumerator, minimum distance and hull dimension are unchanged;
> (iv) **Galois (σ_s-) hulls of cyclic codes over matrix rings** — the object itself — with
> exhaustive censuses (`35` codes at `q=2,n=3` with the CRT/Morita structure; `343`,
> `737`, `144`; `33` at `t=2`; hull-dimension distributions) and the squarefree-hypothesis
> counterexample `q=4,n=2` (33, not 49); (v) the (Phase 5–6, still open) route to quantum
> codes over a **non-commutative** alphabet.

**Claim level.** With (i)–(iv) the work is a solid **Q2/Q1-borderline** paper in a
specialist journal (e.g. *Finite Fields and Their Applications*, *Designs, Codes and
Cryptography*, *AAECC*, *Quantum Information Processing*) — **provided** Phase 5–6 deliver
a Gray/Bachoc map with a duality relation (T-012) and at least one genuinely new quantum
family (T-013/T-014). Without T-012/T-013 it is a **Q2** algebra-of-codes paper.
No Q1 claim should be made at Phase 0.

## 7. Required bibliography additions (new references, all verified this session)

1. Wood 2010 (Int. J. Inf. Coding Theory 1(4):429–444).
2. Szabo & Wood 2017 (J. Algebra Comb. Discrete Struct. Appl. 4(2):105–113).
3. Nebe, Rains & Sloane 2006 (Springer, Alg. Comput. Math. 17).
4. Dougherty & Leroy 2016 (AAECC 27:185–203).
5. Solé, MMS 2011 (doi:10.1109/MMS.2011.6068573).
6. Kushwaha & Prakash, arXiv:2512.12335 and arXiv:2601.06609.
7. arXiv:2606.13467 (W-δ-μ / σ-duals for quantum codes) — optional but useful for §7.

(Already in the bibliography: Zhang–Kong–Zheng 2026, Li–Liu 2025, Debnath–Prakash 2025,
Yadav–Debnath–Prakash 2025, Wood 1999, Bachoc 1997, Fan–Zhang 2017, Alahmadi et al. 2013.)

## 8. Actions

* **A1 (blocking).** Reword the introduction's novelty paragraph to the wording of §6 and
  add references 1–6. Do not write "we introduce a duality via an anti-automorphism"
  without "following Wood (2010) / Szabo–Wood (2017)".
* **A2 (before claiming MacWilliams).** Obtain the Szabo–Wood PDF and check the hypotheses
  of their double-dual and MacWilliams statements for a non-involutive anti-automorphism
  (F-13). Core.ac.uk timed out; the journal page confirms the metadata
  (https://jacodesmath.com/index.php/jacodesmath/article/view/60).
* **A3.** Add a "relation to prior work" paragraph naming Solé (MMS 2011) as the closest
  predecessor on the same alphabet and Kushwaha–Prakash as the closest on non-commutative
  hulls.
* **A4.** Keep the claim level at Q2 for now; revisit only after T-012/T-013 exist.
