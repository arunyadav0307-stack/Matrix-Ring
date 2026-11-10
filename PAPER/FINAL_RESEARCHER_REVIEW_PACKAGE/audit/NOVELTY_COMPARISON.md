# Phase 8 / Task D — Novelty comparison table

**What is *not* claimed.** Matrix rings as code alphabets, Galois hulls, Gray
maps, quasi-cyclic images, the stabilizer/CSS formalism, entanglement-assisted
codes and the quantum Singleton/Hamming bounds are all prior art and are
attributed below. The novelty claim concerns **one specific proved combination**
and the constructions it produces.

**The novelty claim, stated once and precisely.**

> Over the **non-commutative** alphabet $R=M_2(A_t)$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$,
> with the **anti-automorphism** $\theta_s=\sigma_s\circ(\cdot)^{\mathsf T}$ (which
> is not available, and has no analogue, over a commutative ring), we prove a
> Galois duality for **right** $R_n$-modules together with a hull theory that
> carries **no principality hypothesis** — and the hypothesis is genuinely
> needed to be absent, because we exhibit Galois hulls that are **not**
> principal ($\mu_B=3$, O-3.1 refuted). We then transport the whole structure
> through the coefficient-expansion Gray map to $\mathbb F_q^{4tn}$, identifying
> the induced form **exactly** (a $\widehat\sigma_s$-Hermitian form with Hankel
> Gram matrix $I_{4n}\otimes H_t$), prove that every Galois hull is
> self-orthogonal **without** any reflexivity hypothesis, and construct
> stabilizer and entanglement-assisted $q$-ary quantum codes of length $N=4tn$
> from them — including from non-principal hulls.

---

## 1. Comparison table

| existing work | code family | ring / field | duality & hull method | quantum parameters | difference from the present work |
|---|---|---|---|---|---|
| Alahmadi–Sboui–Solé–Yemen 2013 [*J. Franklin Inst.* 350(9):2837–2847] | cyclic codes, $n$ odd | $M_2(\mathbb F_2)$ | Euclidean dot product, ring-valued; right-ideal convention fixed | **none** | Same alphabet family and the same (right) convention, but $t=1$, $q=2$, **no $\theta_s$-duality, no hulls, no Gray map, no quantum step** |
| Luo–Parampalli 2018 [*Cryptogr. Commun.* 10(6):1109–1117] | cyclic codes, $n$ odd | $M_2(\mathbb F_2+u\mathbb F_2)$ | structure theorem; Euclidean duals | **none** | First $t=2$ case of our family, but Euclidean only; **no Galois parameter, no hulls, no quantum** |
| Dinh–Gaur–Kumar–Singh–Singh 2024 [*Adv. Math. Commun.* 18(4):1100–1122] | cyclic codes, $n$ odd | $M_2(\mathbb F_2[u]/\langle u^k\rangle)$ — **the same ring family** | isometry to $\mathbb F_4[u,v]/\langle u^k,v^2\rangle$; map $\theta$ to codes of length $2kn$ over $\mathbb F_4$ | **none** | Same ring $R$, same $u$-adic parameter; but the image length is $2kn$ (their isometry), **no $\sigma_s$-Galois duality, no hulls, no quantum** |
| Falcunit–Sison 2014 / arXiv:1409.7228 | cyclic codes | $M_2(\mathbb F_p)$ | homogeneous weight via the generating character; left-$\mathbb F_p$ isometry onto $\mathbb F_{p^2}+u\mathbb F_{p^2}$; Euclidean **and** Hermitian duals | **none** | Closest prior work on the **weight** side; but $t=1$, $p$ prime, **no $\sigma_s$-Galois duality, no hulls, no quantum** |
| Joshi–Patel–Prakash 2026 [arXiv:2602.18255] | cyclic codes | $M_4(\mathbb F_2[u]/\langle u^k\rangle)$ | Euclidean + Hermitian duals; Bachoc **and** Gray map to $\mathbb F_{16}$ | **none** | Most recent competitor, non-commutative non-chain, $4\times4$ matrices; **still no Galois duality, no hulls, no quantum codes** |
| Si–Niu 2023 [*AIMS Math.* 8(10):24434–24445]; Du–Niu 2025 [*AIMS Math.* 10(5):11435–11443] | **skew** cyclic codes | $M_2(\mathbb F_2)$ | cyclic-algebra / skew-polynomial route | **none** | A genuinely different mechanism (a skew derivation, not a coefficient-Frobenius anti-automorphism); no hulls, no quantum |
| Wood 1999 [*Amer. J. Math.* 121(3):555–575] | linear codes | arbitrary finite rings | duality for modules over finite (Frobenius) rings | — | The authority we **import**; we do not reprove it. It does not treat a Galois parameter, hulls, or quantum codes |
| Greferath–Schmidt 1999 [*IEEE TIT* 45(7):2522–2524] | Gray isometries | finite **chain** rings | isometry into Hamming space | — | Explicitly **not** applicable to $R=M_2(A_t)$ (not a chain ring); we use it to state the limitation of our own map, not as a tool |
| Fan–Zhang 2017 [*DCC* 84(3):473–492] | constacyclic codes | finite **fields** | the $\ell$-Galois inner product $\langle a,b\rangle_h=\sum a_ib_i^{p^h}$ (Frobenius on the second argument) | — | Origin of the Galois idea, over a **field**: no anti-automorphism is needed there because the ring is commutative |
| Liu–Pan 2020 [*DCC* 88(2):241–255] | linear codes | finite **fields** | $\ell$-Galois hulls, dimension formulas | — | Same hull notion, commutative base; no matrix ring, no Gray map, no quantum |
| Cao 2021 [*IEEE TIT* 67(12):7964–7984] | (extended) GRS codes | finite **fields** | MDS codes with Galois hulls of arbitrary dimensions | EAQECC from Galois hulls | Galois-hull $\to$ EAQECC **over a finite field**; no ring, no non-commutativity, no Gray map |
| **Zhang–Kong–Zheng 2026** [*Entropy* 28(4):407, DOI 10.3390/e28040407] | constacyclic codes | a finite **non-chain** ring, **commutative**, with a CRT decomposition $C=e_1C_1\oplus\cdots\oplus e_tC_t$ | $\ell$-Galois duals and hull **dimensions** via a new Gray map $\phi$; CSS + Hermitian + Construction X | EAQECC and QECC, some QMDS, some better than the best known | **The closest prior work.** It is Galois-hull $\to$ Gray map $\to$ quantum over a non-chain ring. Differences: (i) their ring is **commutative**, so no anti-automorphism and no left/right issue arise; (ii) consequently **no analogue of O-3.1 exists** for them and no principality question is asked; (iii) their image length is $tn$ (from the CRT product), ours is $4tn$ (from $\dim_{\mathbb F_q}M_2(A_t)=4t$); (iv) they determine hull **dimensions**, we construct codes from **non-principal** hulls and classify when $\mu_B\ge3$ can occur; (v) we prove a coset-distance characterisation and a coset Singleton bound, which they do not |
| Ketkar–Klappenecker–Kumar–Sarvepalli 2006 [*IEEE TIT* 52(11):4892–4914] | stabilizer codes | $\mathbb F_q$ | symplectic stabilizer formalism | $[[n,k,d]]_q$ | The formalism we **re-derive from scratch** (Phase 5, Lemmas Q1–Q2) rather than import; no ring, no hull |

---

## 2. The precise novelty, decomposed

| ingredient | new here? | comment |
|---|---|---|
| matrix ring $M_2(A_t)$ as a code alphabet | **no** | Alahmadi et al. 2013; Luo–Parampalli 2018; Dinh et al. 2024; Joshi et al. 2026 |
| right-ideal (right-module) convention | **no** | fixed by Alahmadi et al. 2013; we add the **proved failure lemma** for the plain product on right modules (T-006) |
| Galois ($\ell$-Galois) duality | **no** | Fan–Zhang 2017 over finite fields |
| Galois hulls | **no** | Liu–Pan 2020 over finite fields |
| Gray map to a finite field | **no** | the whole rings literature |
| quantum codes from hulls | **no** | Cao 2021; Zhang–Kong–Zheng 2026 |
| $\theta_s=\sigma_s\circ(\cdot)^{\mathsf T}$ as an **anti**-automorphism of $R_n$ driving a duality on right modules | **YES** | requires non-commutativity to be meaningful; over a commutative ring $\theta_s$ degenerates to $\sigma_s$ |
| hull theory with **no principality hypothesis**, and the **refutation** of the natural conjecture that hulls are principal (O-3.1), with the classification $\mu_B\ge3 \Rightarrow t\ge2$ and $p\mid n$ | **YES** | the counterexample families are $(4,2,2)$, $(9,2,3)$, $(4,2,4)$; $(8,2,2)$ is a negative |
| the **exact** induced form of the coefficient expansion: $\langle u,v\rangle^{\widehat{}}_s=u^{[s]}(I_{4n}\otimes H_t)v^{\mathsf T}$, with duality **and** hull preservation valid on the non-principal witnesses | **YES** | prior commutative work transports to the Euclidean or plain Hermitian form; the Hankel factor is forced by $u$-adic duality and is what obstructs the CSS route for $p=2$, $t$ even |
| hull self-orthogonality **without** reflexivity (one-sided argument) | **YES** | this is the hinge that makes the quantum step possible in the general Galois regime |
| $N_{\rm phys}=4tn$ **derived**, with the char-2 obstruction for $t$ even stated under its exact hypotheses | **YES** | the obstruction is a *theorem* about the form, not about a code |
| **coset-distance characterisation** $d=\min\mathrm{wt}(D^{\perp_E}\setminus\mathrm{Hull}_E(D))$ as the minimum weight of the quotient code, and the **coset Singleton bound** $K+d\le N+1$ | **YES (new, proved)** | neither bound appears in the EA literature we surveyed; the coset Singleton bound is not the EA Singleton bound and is not implied by it |
| quantum codes (stabilizer and EA) constructed from **non-principal** hulls over a non-commutative ring | **YES** | $[[24,6,2;2]]_9$ and $[[32,8,2;4]]_4$: the parameters are weak, the point is structural |

---

## 3. What the manuscript must *not* claim

* Not that matrix rings, Galois hulls, Gray maps, stabilizer codes or EAQECC are
  new. Each is attributed.
* Not a record parameter. Every stabilizer code we construct is at best equal to
  the best known distance, and then only with $d=2$; every $d\ge3$ code is 1–2
  below (`PARAMETER_COMPARISON.md` §4).
* Not that the $q=8$ codes or any EA code are benchmarked: no table exists for
  them (§2 of `LITERATURE_VERIFICATION.md`).
* Not that the classification of $\mu_B\ge3$ witnesses is complete: it is
  complete for the **enumerable** families and for the deterministic constructed
  family $W=m^ie_1\oplus U$, $U\le\operatorname{ann}_{B^2}(m)$, and the families
  that remain out of reach are listed (Phase 7 §1.2).
* Not a Q1-journal suitability assessment: no documented comparison of scope,
  standards and novelty against a specific venue has been performed.
