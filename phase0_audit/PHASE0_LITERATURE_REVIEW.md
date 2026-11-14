# PHASE 0 — LITERATURE REVIEW

**Scope:** cyclic codes over matrix rings · noncommutative matrix-ring codes · (k)-Galois inner products and duality · Galois hulls of (consta)cyclic codes · Gray maps over finite/matrix rings · quantum codes from matrix-ring codes · CSS constructions from hulls.
**Date:** 2026-11-12. No reference is invented; every entry carries a verification tag.

## 1. Verification policy and environment limits

| Tag | Meaning |
|---|---|
| **PDF-DIRECT** | full text physically read in this audit (the 7 zip PDFs); bibliographic data quoted from the paper itself |
| **WEB-VERIFIED** | record verified 2026-11-12 via the platform web-search tool against the publisher/arXiv record |
| **INHERITED-DIRECT** | record marked `DIRECT` by the prior campaign's bibliography (publisher/arXiv page retrieved 2026-11-04…10), `01_LITERATURE/annotated_bibliography.md` |
| **SECONDARY** | metadata quoted inside verified papers' reference lists; publisher page not yet seen |
| **UNVERIFIED** | existence plausible; details not pinned down |

**Environment limitation (recorded):** scholarly database access from the sandbox is restricted; three decisively important items were verified by the search tool (A8, C2, C7). A full online re-verification sweep of all 37 inherited bibliography entries remains a **mandatory pre-submission task** for whichever project direction continues.

## 2. The seven physically-present sources (PDF-DIRECT)

| ID | Reference (exact, from the PDF) | Content core |
|---|---|---|
| **A8** | S. R. Joshi, S. Patel, O. Prakash, *Quantum codes construction from cyclic codes over matrix rings*, **Quantum Information Processing 25:207 (2026)**, DOI 10.1007/s11128-026-05230-0 (received 2025-12-31, published online 2026-06-09) — **also WEB-VERIFIED 2026-11-12** | R = M₃(F_p[u]/⟨uᵏ⟩); cyclic codes as direct sums of submodules; Euclidean and Hermitian duals over S = M₃(F₃+uF₃+⋯); **new non-degenerate inner product** for dual-containing pairs; **CSS quantum codes over F₂₇** via a Gray map; AMDS/best-known classical codes over F₁₂₅, F₂₇, F₈. **No general Galois twist (only the Hermitian Frobenius on F_{p³}), no hull theory, no entanglement-assisted codes.** |
| **A7** | S. R. Joshi, S. Patel, O. Prakash, *Construction of cyclic codes over a class of matrix rings*, arXiv:2602.18255v1 (Feb 2026), 30 pp | M₄(F₂[u]/⟨uᵏ⟩), cyclic codes → F₁₆ codes via Gray-type map; classical only (word "quantum" appears 3×, as motivation). |
| **A10** | S. Patel, O. Prakash, H. Islam, *Cyclic codes over M₄(F₂+uF₂)*, Cryptogr. Commun. (2022), DOI 10.1007/s12095-022-00572-9, 14 pp | M₄ over the t = 2 ring; classical structure. |
| **A5b** | J. Pal, S. Bhowmick, S. Bagchi, *Cyclic codes over M₄(F₂)*, J. Appl. Math. Comput. 60:749–756 (2019), DOI 10.1007/s12190-018-01235-w | classical M₄(F₂). |
| **A9** | H. Islam, O. Prakash, D. K. Bhunia, *On the structure of cyclic codes over M₂(F_p+uF_p)*, INSA journal (2021, corr.), DOI 10.1007/s13226-021-00014-x | cyclic codes as right R-submodules, primes p ≢ ±2,3 (mod 5). |
| **A9b** | H. Islam, O. Prakash, D. K. Bhunia, *Algebraic structure of cyclic codes over M₃(F_p)* (venue unconfirmed — UNVERIFIED venue) | classical M₃(F_p), isometric image. |
| **A11** | S. Patel, S. R. Joshi, O. Prakash, *Construction of codes over F_{p³} from cyclic codes over M₃(F_p+uF_p+u²F_p)* (venue unconfirmed — UNVERIFIED venue) | classical M₃ at t = 3 → F_{p³}. |

## 3. Comparison matrix (blueprint-mandated format)

| Reference | Ring/Structure | Code family | Duality / Hull | Gray map | Quantum | Remaining gap |
|---|---|---|---|---|---|---|
| A1 Alahmadi–Sboui–Solé–Yemen 2013, J. Franklin Inst. 350(9):2837–2847; arXiv:1201.6533 **[INHERITED-DIRECT]** | M₂(F₂) = F₄⊕uF₄ | cyclic = right ideals, n odd | R-valued Euclidean & Hermitian; hulls ✗ | Bachoc map φ(a+ub)=(a+b,b) | ✗ | no Galois, no hulls, no quantum; R-valued dot product is **not a perfect duality for right ideals** (in-repo computation E4: 31/35 codes at q=2,n=3 fail the size formula) |
| A2 Luo–Parampalli 2018, Cryptogr. Commun., DOI 10.1007/s12095-017-0266-1 **[INHERITED-DIRECT]** | M₂(F₂+uF₂) | cyclic, odd n | Euclidean/Hermitian (R-valued) | isometry to F₄-codes | ✗ | t = 2 only; no hulls/quantum |
| A3 Dinh–Gaur–Kumar–Singh–Singh 2024, Adv. Math. Commun. 18(4):1100–1122, DOI 10.3934/amc.2022073 **[INHERITED-DIRECT]** | M₂(F₂[u]/⟨uᵏ⟩) — **exactly the r = 2 candidate family** | cyclic, odd n | Euclidean/Hermitian | θ-map to F₄ codes of length 2kn | ✗ | no Galois duality, no hulls, no quantum |
| A4 Falcunit–Sison 2014, IZS Zürich **[SECONDARY]** | M₂(F_p), M₂(F_p+uF_p) | cyclic | Euclidean/Hermitian | isometric images F_{p²}(+u,v) | ✗ | conference; no quantum |
| A5a Bhowmick–Bagchi–Bandi 2018, self-dual cyclic over M₂(Z₄) **[SECONDARY]** | M₂(Z₄) | cyclic/self-dual | Euclidean | – | ✗ | Z₄ base |
| A5b Pal–Bhowmick–Bagchi 2019 **[PDF-DIRECT]** | M₄(F₂) | cyclic/self-dual | Euclidean | – | ✗ | classical M₄ |
| A6 Si–Niu 2023 **[INHERITED]**; Du–Niu 2025 **[INHERITED]** | M₂(F₂) | **skew** cyclic | Euclidean/Hermitian | – | ✗ | skew twist only; no hulls, no quantum, no Galois |
| A7 Joshi–Patel–Prakash 2026 **[PDF-DIRECT]** | M₄(F₂[u]/⟨uᵏ⟩) | cyclic | Euclidean/Hermitian | → F₁₆ | ✗ | classical; recent strong competitor |
| **A8 Joshi–Patel–Prakash 2026** **[PDF-DIRECT + WEB-VERIFIED]** | M₃(F_p[u]/⟨uᵏ⟩) | cyclic (submodule direct sums) | Euclidean+Hermitian; "new" non-degenerate product for dual-containment | Gray → F₂₇ | **✓ CSS, small Singleton defects** | **occupies "quantum codes from cyclic codes over matrix rings" (Euclidean/Hermitian, M₃)** — no Galois hulls, no EA |
| A9, A9b Islam–Prakash–Bhunia 2021 + n.d. **[PDF-DIRECT]** | M₂(F_p+uF_p); M₃(F_p) | cyclic | – | isometries | ✗ | classical M₂/M₃ structure |
| A10 Patel–Prakash–Islam 2022 **[PDF-DIRECT]** | M₄(F₂+uF₂) | cyclic | – | – | ✗ | classical M₄, t = 2 |
| A11 Patel–Joshi–Prakash **[PDF-DIRECT, venue UNVERIFIED]** | M₃(F_p+uF_p+u²F_p) | cyclic | – | → F_{p³} | ✗ | classical M₃, t = 3 |
| B1 Wood 1999, Amer. J. Math. 121:555–575 **[INHERITED-DIRECT]** | any finite **Frobenius** ring (noncommutative allowed) | linear | character duality (MacWilliams) | – | – | the framework authority that legitimizes whole program |
| B2–B5 Wood 2010 IJICOT 1(4):429–444; Szabo–Wood 2017 JACODSA 4(2):105–113; Nebe–Rains–Sloane 2006 (Springer ACM 17); Dougherty–Leroy 2016 AAECC 27:185–203 **[INHERITED-DIRECT]** | noncommutative Frobenius rings | linear | **sesquilinear duality w.r.t. anti-automorphisms**: double-dual, cardinality, MacWilliams | – | – | **PUB-warning: the anti-automorphism duality *mechanism itself* is published** — novelty must lie in the cyclic/Galois/hull/quantum specialization, not in the duality framework |
| C1 Fan–Zhang 2017, Des. Codes Cryptogr. 85:473–492 **[INHERITED-DIRECT]** | F_{p^m} (field) | constacyclic | Galois σ_s-sesquilinear; self-dual existence | – | ✗ | field only |
| C2 Liu–Pan 2020, Des. Codes Cryptogr. 88:241–255, DOI 10.1007/s10623-019-00681-2 **[WEB-VERIFIED]** | F_q | linear | **ℓ-Galois hulls**; hull dimension from generator matrix; ℓ-Galois LCD | – | ✗ | field only |
| C2′ Liu–Yu–Hu 2019, Finite Fields Appl. 55:21–32 (cited inside C2's publisher page) **[WEB-VERIFIED as citation]** | F_q | linear | **(k)-Galois dual** | – | **✓ EAQECC** | field only |
| C3 Liu–Fan–Liu 2018 Galois LCD **[INHERITED]**; C4 Cao 2021 MDS Galois hulls **[INHERITED]** | F_q | constacyclic/MDS | Galois hulls/LCD | – | EA/MDS | field only |
| C5 Zhang–Kong–Zheng 2026 (prior audit P7: *Entropy* 28(4):407) **[INHERITED-DIRECT]** | **commutative** non-chain F_{p^m}[u₁,…]/⟨…⟩ | constacyclic | ℓ-Galois hulls | new Gray with φ(C)^{⊥_ℓ} = φ(C^{⊥_ℓ}) | **✓ QECC + EAQECC + QMDS** | commutative; CRT-split; no matrix ring |
| C6 Debnath–Islam–Martínez-Moro–Prakash 2024/25 **[INHERITED-DIRECT]** | affine-algebra serial rings (commutative) | λ-constacyclic | k-Galois hulls, dimension formula, LCD | – | EA (no plain QECC) | commutative |
| C7 Kushwaha–Prakash 2025/26, arXiv:2512.12335 & arXiv:2601.06609 **[WEB-VERIFIED]** | **non-commutative non-unital** 4-element ring E | free linear | Euclidean + symplectic hulls (residue/torsion) | – | ✗ | hulls over a noncommutative alphabet now exist — but non-unital, non-matrix, no Galois twist, no quantum |
| Q-cluster: Calderbank–Shor 1996; Steane 1996; Gottesman 1997; Knill–Laflamme 1997; Rains 1999; Ketkar et al. 2006; Brun–Devetak–Hsieh 2006; Wilde–Brun 2008; Lai–Brun–Wilde 2013 **[INHERITED]** | — | — | — | — | stabilizer/CSS/EA foundations | — |
| **IN-REPO prior manuscript** (this repository; FFA-prepared, submission-prep stage) **[REPO — physically inspected]** | R = M₂(F_q[u]/⟨uᵗ⟩), q = p^{r_old} | cyclic = **right ideals** of R[X]/⟨Xⁿ−1⟩ | **θ_s-Galois duality + hulls, all s; reflexive mainline s = r_old/2** | **φ_n with proved transported pairing (463/463 checks)** | **✓ CSS self-orthogonal & dual-containing + EAQECC; 28 certified codes (q = 4, 8, 9; t ≤ 4; n ≤ 6)** | **covers the blueprint's exact intersection at matrix size 2** |

## 4. Reading of the landscape

1. **The naive intersection is empty no longer — internally.** The "(k)-Galois hulls over matrix rings → Gray → CSS/EA quantum" chain exists **in this very repository**, with proofs and certified codes. Any new paper must cite it and differentiate, or be the same paper.
2. **The nearest external compression is A8 (QIP 2026)**: after it, "first quantum codes from cyclic codes over matrix rings" is **not** an available claim for anyone, including this repository's manuscript. A8 does *not* contain Galois twists or hulls — that specific intersection remains externally unpublished (as of 2026-11-12, within reach of the checks above). **A8 is absent from the prior campaign's bibliography (grep-confirmed) — a literature gap that must be closed in any submission version.**
3. **The Galois-hull→quantum vein over commutative alphabets is occupied and active** (C5 *Entropy* 2026; C6; C2, C2′). Novelty cannot rest on hull→quantum mechanics itself.
4. **Hulls over a noncommutative alphabet now exist** (C7, non-unital E, Euclidean/symplectic). This weakens any broad "first hulls over noncommutative rings" phrasing; the matrix-ring + Galois + cyclic + quantum combination is the defensible remnant.
5. **The classical matrix-ring-cyclic literature is crowded and converging (A1–A11, same IIT-Patna-linked school at M₂, M₃, M₄)**, with 2026 items at M₄ (A7) and quantum M₃ (A8). A parameter-push paper (bigger r, bigger t) without a new structural theorem would duplicate their style and is a high rejection risk.

## 5. Unverified residuals (recorded, not hidden)

- Venues of A9b and A11 (PDFs present; no journal line printed) — TO CONFIRM.
- Full publisher-page re-verification of inherited entries B2–B5, C3, C4, C5's exact venue/pages, A5a's journal status.
- Grassl codetables values inside `research-data/` were external data retrieved 2026-11-04 by the prior campaign; not re-checkable from this sandbox.
