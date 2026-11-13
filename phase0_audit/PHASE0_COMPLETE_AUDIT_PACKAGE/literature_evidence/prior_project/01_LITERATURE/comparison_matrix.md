# 01 — Literature comparison matrix

**Phase 0 deliverable 2.** One row per closest paper. “Ours (planned)” is the
last row and is a *target*, not an accomplished result.

| Ref | Alphabet (ring) | Code family | Duality used | Hull? | Gray / isometry map | Quantum? | Main result | Limitation w.r.t. our project |
|-----|-----------------|-------------|--------------|-------|--------------------|----------|-------------|-------------------------------|
| **A1** Alahmadi–Sboui–Solé–Yemen 2013 | $M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$ | cyclic = **right ideals** of $A[X]/(X^n-1)$, $n$ odd | **Euclidean** $\sum x_jy_j$ (R-valued) and Hermitian $\sum x_j\bar y_j$ | ✗ | **Bachoc map** $\phi(a+ub)=(a+b,b)$, Hermitian-compatible (their Prop. 2) | ✗ | structure thm $C=(fh)+u(fg)$; Euclidean self-duality criterion; Bachoc image = Plotkin sum of residue & torsion | R-valued dot product; no hulls, no quantum; right-ideal side convention not reconciled with duality |
| **A2** Luo–Parampalli 2018 | $M_2(\mathbb F_2+u\mathbb F_2)$ | cyclic, odd length | Euclidean / Hermitian (R-valued) | ✗ | isometry to $\mathbb F_4$-codes | ✗ | structure theorem; optimal $\mathbb F_4$ codes | same as A1; $t=2$ only |
| **A3** Dinh–Gaur–Kumar–Singh–Singh 2024 | $M_2(\mathbb F_2[u]/\langle u^k\rangle)$ | cyclic, odd length | Euclidean / Hermitian (R-valued) | ✗ | $\theta$ map to length-$2kn$ codes over $\mathbb F_4$ | ✗ | structure theorem via isometry to $\mathbb F_4[u,v]/\langle u^k,v^2,uv-vu\rangle$ | **same ring family as ours**; no Galois duality, no hulls, no quantum |
| **A4** Falcunit–Sison 2014 | $M_2(\mathbb F_p)$, $M_2(\mathbb F_p+u\mathbb F_p)$ | cyclic | Euclidean / Hermitian | ✗ | isometry to $\mathbb F_{p^2}+u\mathbb F_{p^2}(+v\ldots)$ | ✗ | structure + self-dual cyclic codes | conference paper; no duality theory |
| **A5** Bhowmick–Bagchi–Bandi 2018 | $M_2(\mathbb Z_4)$ | cyclic + self-dual | Euclidean (R-valued) | ✗ | – | ✗ | generators of cyclic codes and duals | $\mathbb Z_4$ base (not $A_t$) |
| **A6** Si–Niu 2023 | $M_2(\mathbb F_2)$ | **skew** cyclic | Euclidean / Hermitian | ✗ | – | ✗ | skew codes are free; odd/even ⇒ cyclic / 2-QC | **skew** twist (different mechanism from ours) |
| **A7** Joshi–Patel–Prakash 2026 | $M_4(\mathbb F_2[u]/\langle u^k\rangle)$ | cyclic | Euclidean / Hermitian (R-valued) | ✗ | Bachoc + Gray map to $\mathbb F_{16}$ | ✗ | ideals, sub-module decomposition, cardinalities, good codes | newest & strongest competitor on the *classical* side |
| **A10** Solé–Yemen (preprint) | $M_\ell(\mathbb F_q)$ | quasi-cyclic viewed as cyclic over matrices | – | ✗ | – | ✗ | QC codes ⇄ cyclic codes over matrix rings | methodological precursor of our Morita step |
| **B1** Wood 1999 | any finite **Frobenius** ring (non-commutative allowed) | linear codes over modules | **character duality** | ✗ | – | ✗ | MacWilliams extension + identities; the correct duality for non-commutative rings | framework only, no cyclic/hull/quantum |
| **C1** Fan–Zhang 2017 | $\mathbb F_{p^\ell}$ | constacyclic | **Galois** $\sum a_ib_i^{p^h}$ (Frobenius on 2nd argument) | ✗ (self-dual focus) | – | ✗ | existence of Galois self-dual constacyclic codes | commutative; no anti-automorphism needed there |
| **C2** Liu–Pan 2020 | $\mathbb F_q$ | linear | Galois | ✓ $\mathrm{Hull}_\ell$ | – | ✗ | hull dimension from a generator matrix; $\ell$-Galois LCD | field only |
| **C5** Zhang–Kong–Zheng 2026 | $\mathbb F_{p^m}[u_1,\dots,u_s]/\langle f_j(u_j),\,u_iu_j-u_ju_i\rangle$ (**commutative** non-chain) | constacyclic | $\ell$-Galois | ✓ | new Gray map $\phi$ with $\phi(C)^{\perp_\ell}=\phi(C^{\perp_\ell})$ | ✓ QECC + EAQECC + QMDS | construction X of the Galois inner product | **commutative**; CRT-split; no matrix ring |
| **C6** Debnath–Islam–Martínez-Moro–Prakash 2024/25 | affine algebra / serial rings (commutative) | $\lambda$-constacyclic | $k$-Galois | ✓ | idempotent generators | ✓ EAQECC | hull-dimension formula; $k$-Galois LCD | commutative; no matrix ring; no QECC (EA only) |
| **Ours (planned, Phase 1–8)** | $R=M_m(A_t)$, $A_t=\mathbb F_q[u]/\langle u^t\rangle$, **non-commutative** | cyclic = one-sided ideals of $R[X]/\langle X^n-1\rangle$ | **$\theta_s$-Galois**, $\theta_s=\sigma_s\circ$ transpose (anti-automorphism), R- *and* $\mathbb F_q$-valued versions | ✓ $\mathrm{Hull}_s(C)=C\cap C^{\perp_s}$ | to be constructed (Phase 5); must satisfy a duality-preservation lemma | ✓ CSS / EAQECC (Phase 6) | duality + hull theorems, hull dimension formulas, quantum families | not yet proved — Phase 1 must establish the foundations |

## Reading of the matrix

1. **Nobody has combined a matrix ring with Galois duality.** Cluster A
   (matrix rings) uses only Euclidean/Hermitian duality; cluster C (Galois
   duality/hulls) uses only commutative rings. The intersection is empty in the
   sources found in Phase 0.
2. **Nobody has taken a matrix-ring code to a quantum code.** All of A1–A7 stop
   at good classical codes over a field.
3. **The Galois-hull → quantum vein is being mined heavily right now**
   (C5 is April 2026; C6 is Dec 2024). Novelty must therefore be argued on the
   *non-commutative algebra* (duality, hull structure, classification), not
   merely on “a new ring gives new parameters”.
4. **Wood (B1) is the authority** that makes the whole thing defensible: without
   the Frobenius/character viewpoint the naive dot product silently produces
   wrong duals (Phase-0 computation E4: 31 of 35 cyclic codes over
   $M_2(\mathbb F_2)$, $n=3$, have $|C|\cdot|C^\perp|\ne|R|^n$).
