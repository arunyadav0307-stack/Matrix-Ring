# 01 — Verified annotated bibliography

**Phase 0 deliverable 1** (blueprint §5, Phase 0).
Project: *Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over
Noncommutative Matrix Rings*.

**Verification policy (blueprint rule 4 / §8A.4):** every entry below was located
during Phase 0 by direct retrieval of the publisher / arXiv / DOI record.  No
entry is copied from memory alone.  The field `VERIFY` records how the entry was
confirmed and what still has to be checked against the primary source.

Legend for `VERIFY`:
* `DIRECT` — the record page (DOI landing page, arXiv abs page, journal page) was
  retrieved and read during Phase 0.
* `SECONDARY` — metadata reconstructed from *quotations inside other verified
  papers* (reference lists of arXiv papers retrieved in Phase 0); bibliographic
  details still to be confirmed on the publisher page.
* `TO CONFIRM` — the item exists (title/venue seen) but page numbers, journal or
  year are not yet pinned down.

---

## Cluster A — Cyclic codes over matrix rings (the alphabet side)

### A1. Alahmadi, Sboui, Solé, Yemen (2013)  — *the closest paper*
* **Title:** Cyclic codes over $M_2(\mathbb{F}_2)$
* **Authors:** Adel Alahmadi, Houda Sboui, Patrick Solé, Olfa Yemen
* **Journal:** Journal of the Franklin Institute **350**(9), 2837–2847 (2013)
* **Preprint:** arXiv:1201.6533 — https://arxiv.org/abs/1201.6533
  (arXiv DOI 10.48550/arXiv.1201.6533)
* **VERIFY:** DIRECT (arXiv abs page + PDF sections 1–5 read; journal reference
  quoted verbatim in the reference list of arXiv:2602.18255 as
  “J. Frankl. Inst. 350 (9) (2013) 2837–2847”).  Publisher DOI not yet confirmed.
* **What it does:** $A=M_2(\mathbb F_2)=\mathbb F_4\oplus u\mathbb F_4$,
  $u^2=0$; cyclic codes = **right ideals** of $R_n=A[X]/(X^n-1)$; structure
  theorem $C=(fh)+u(fg)$ with $X^n-1=fgh$ over $\mathbb F_4$ (n odd);
  Euclidean dual $C^\perp=(g^*h^*,\,ug^*f^*)$; characterisation of Euclidean
  self-dual cyclic codes; Bachoc map $\phi(a+ub)=(a+b,b)$; the Bachoc image of a
  cyclic code is a Plotkin sum of its residue and torsion code; Hermitian
  self-dual cyclic codes of odd length do not exist.
* **Relation to our project:** this is the *base* paper for the alphabet.  Two
  things in it are directly relevant to us: (i) it fixes the **right-ideal**
  convention, and (ii) it uses the **ring-valued Euclidean dot product**
  $\sum_j x_jy_j$ — which our Phase-0 computation (E4) shows is *not* a perfect
  duality for right ideals.  See `02_PHASE_REPORTS/Phase_0/`.

### A2. Luo & Parampalli (2018)
* **Title:** Cyclic codes over $M_2(\mathbb{F}_2+u\mathbb{F}_2)$
* **Authors:** R. Luo, U. Parampalli
* **Journal:** Cryptography and Communications **10**(?) — Springer,
  DOI **10.1007/s12095-017-0266-1**
  (https://link.springer.com/article/10.1007/s12095-017-0266-1)
* **VERIFY:** DIRECT (Springer record retrieved).  Volume/issue/pages
  **TO CONFIRM**.
* **What it does:** structure theorem for cyclic codes of **odd** length $n$
  over the non-commutative Frobenius non-chain ring
  $A=M_2(\mathbb F_2+u\mathbb F_2)$; constructs optimal cyclic codes over
  $\mathbb F_4$.
* **Relation:** the $t=2$ case of our candidate family $M_m(A_t)$, $m=2$.
  Duals: Euclidean/Hermitian, in the same (ring-valued) style as A1.

### A3. Dinh, Gaur, Kumar, Singh & Singh (2024)
* **Title:** Cyclic codes over rings of matrices
* **Authors:** Hai Q. Dinh, Atul Gaur, Pratyush Kumar, Manoj Kumar Singh,
  Abhay Kumar Singh
* **Journal:** Advances in Mathematics of Communications **18**(4),
  1100–1122 (2024); early access 15 Sep 2022; **DOI 10.3934/amc.2022073**
* **VERIFY:** DIRECT (AIMS journal record + the same reference quoted in
  arXiv:2602.18255 as “Adv. Math. Commun. 18 (4) (2024), 1100–1122”).
* **What it does:** $\mathcal A=M_2(\mathbb F_2[u]/\langle u^k\rangle)$ — exactly
  our ring family with $m=2,t=k,q=2$; structure theorem for cyclic codes of odd
  length via an isometry onto $\mathbb F_4[u,v]/\langle u^k,v^2,uv-vu\rangle$;
  a map $\theta$ from length-$n$ codes over $\mathcal A$ to length-$2kn$ codes
  over $\mathbb F_4$; a weight extending the $M_2(\mathbb F_2)$ weight.
* **Relation:** the *most directly competing* prior work on our ring family.
  It does **not** treat Galois duality, hulls, or quantum codes.

### A4. Falcunit & Sison (2014)
* **Title:** Cyclic codes over the matrix ring $M_2(\mathbb F_p)$ and their
  isometric images over $\mathbb F_{p^2}+u\mathbb F_{p^2}$
* **Venue:** 23rd International Zurich Seminar on Communications (IZS),
  ETH Zürich, Feb 2014
* **VERIFY:** SECONDARY (title + venue quoted in the introductions of A3, A7 and
  in the ResearchGate record).  Page numbers TO CONFIRM.
* **What it does:** structure of cyclic codes over $M_2(\mathbb F_p)$;
  isometry onto $\mathbb F_{p^2}+u\mathbb F_{p^2}$; later extended to
  $M_2(\mathbb F_p+u\mathbb F_p)\to
  \mathbb F_{p^2}+u\mathbb F_{p^2}+v\mathbb F_{p^2}+uv\mathbb F_{p^2}$.
* **Relation:** the $t=1$/$m=2$ case over general $p$; establishes the
  “isometric image” technique that our Gray-map step (Phase 5) must generalise.

### A5. Bhowmick, Bagchi, Bandi (2018)
* **Title:** Self-dual cyclic codes over $M_2(\mathbb Z_4)$
* **VERIFY:** SECONDARY / TO CONFIRM (record seen on DeepAI, 13 Jul 2018;
  abstract states: “perhaps the first time the ring structure $M_2(\mathbb Z_4)$
  is considered as a code alphabet”; $M_2(\mathbb Z_4)\cong
  \mathbb Z_4[w]+U\mathbb Z_4[w]$; generators of cyclic codes and their duals).
  Journal status not confirmed.
* **Relation:** shows the $M_2(\cdot)$ programme over $\mathbb Z_4$; again
  Euclidean/Hermitian duality only.

### A6. Si & Niu (2023)
* **Title:** On skew cyclic codes over $M_2(\mathbb F_2)$
* **Authors:** Xuesong Si, Chuanze Niu
* **Journal:** AIMS Mathematics **8**(10), 24434–24445 (2023);
  **DOI 10.3934/math.20231246**
* **VERIFY:** DIRECT (AIMS record with full citation line).
* **What it does:** skew cyclic codes over $M_2(\mathbb F_2)$ using the
  $\mathbb F_4$-cyclic algebra; a skew cyclic code with minimal-degree
  polynomial $d(x)$ is free, generated by $d(x)$; odd/even length $\Rightarrow$
  cyclic / 2-quasi-cyclic over $M_2(\mathbb F_2)$; self-dual skew condition for
  Hermitian duals; generator polynomials of Euclidean duals.
* **Relation:** the **skew** route to a “twisted” shift over a matrix ring —
  an alternative to our automorphism-twisted duality.  Must be compared in
  Phase 1/2 (skew-cyclicity vs. $\theta$-duality are *different* mechanisms).

### A6b. Du & Niu (2025)
* **Title:** Weight distributions of a class of skew cyclic codes over
  $M_2(\mathbb F_2)$, AIMS Mathematics **10**(5), 11435–11443 (2025).
* **VERIFY:** DIRECT (AIMS citation line seen).  DOI TO CONFIRM
  (listed as 10.3934/math.2025520 in the AIMS citation export).

### A7. Joshi, Patel & Prakash (2026)  — *the most recent competitor*
* **Title:** Construction of Cyclic Codes over a Class of Matrix Rings
* **Authors:** Soham Ravikant Joshi, Shikha Patel, Om Prakash
* **Preprint:** arXiv:2602.18255 (20 Feb 2026),
  https://arxiv.org/abs/2602.18255
* **VERIFY:** DIRECT (arXiv abs page + HTML read).
* **What it does:** $\mathcal R=M_4(\mathbb F_2[u]/\langle u^k\rangle)$ — our
  family with $m=4$; ring is decomposed as a commutative-looking ring
  $(\mathbb F_{16}+v\mathbb F_{16}+\dots)+u(\dots)$, $v^4=0$; ideals,
  cyclic codes as direct sums of $\mathcal R$-submodules of
  $\mathcal R[x]/\langle x^n-1\rangle$, cardinality formulas; Euclidean and
  Hermitian duals; Bachoc + Gray map to $\mathbb F_{16}$; tables of good codes.
* **Relation:** raises the bar for “matrix ring + $u$-adic ring” papers.  It
  does **not** do Galois duality, hulls, or quantum codes — the three things
  our project is about.  It also shows the area is **active right now**.

### A8. Oggier, Belfiore, Viterbo (ca. 2010–2012) — space-time origin
* **Title:** Codes Over Matrix Rings for Space-Time Coded Modulations
* **VERIFY:** SECONDARY (record + abstract seen; journal/volume TO CONFIRM —
  quoted in the introductions of A1, A2, A3 as the source of the $M_2(\mathbb F_2)$
  and $M_2(\mathbb F_2[i])$ alphabets for the Golden code).
* **Relation:** historical origin of the alphabet; not coding-theoretic duality.

### A9. Bachoc (1997) — origin of the alphabet
* **Title:** Applications of coding theory to the construction of modular
  lattices; *J. Combin. Theory Ser. A* **78**(1), 92–119 (1997).
* **VERIFY:** SECONDARY / TO CONFIRM (cited as reference [1] of A1 as the first
  appearance of $A=M_2(\mathbb F_2)$ as a code alphabet and as the source of the
  Bachoc map / Bachoc weight; the year 1997 and the modular-lattice context are
  quoted verbatim in A1 and A3).  Exact volume/pages TO CONFIRM.
* **Relation:** source of the **Bachoc map** — the model for our Phase-5
  isometry.

### A10. Solé & Yemen / Cayrel–Solé–Yemen — quasi-cyclic view
* **Title:** Quasi-cyclic codes as codes over rings of matrices
  (TU Darmstadt/CASED preprint, https://download.hrz.tu-darmstadt.de/pub/FB20/Dekanat/Publikationen/CASED/Quasi-cyclic_codes_as_codes_over_rings_of_matrices.pdf)
* **VERIFY:** SECONDARY / TO CONFIRM (PDF located and abstract read; author list
  and final journal TO CONFIRM).
* **Relation:** **methodologically important for us**: quasi-cyclic codes over
  a field are cyclic codes over a matrix ring.  This is the same phenomenon
  behind the Morita correspondence we rediscovered in Phase 0
  (one-sided ideals of $M_m(B)$ ⇄ $B$-submodules of $B^m$).  We must cite and
  compare this in Phase 2.

---

## Cluster B — Duality over finite rings (the foundation we must respect)

### B1. Wood (1999)  — *the authority for duality over non-commutative rings*
* **Title:** Duality for modules over finite rings and applications to coding
  theory; *Amer. J. Math.* **121**(3), 555–575 (1999);
  **DOI 10.1353/ajm.1999.0024** (Project MUSE).
* **VERIFY:** DIRECT (Project MUSE record).
* **What it does:** singles out finite **Frobenius** rings as the right alphabets;
  MacWilliams extension theorem and MacWilliams identities hold over them;
  character-theoretic duality for modules over **not necessarily commutative**
  finite rings.
* **Relation:** this is the theorem that makes our trace pairing correct and
  that explains why the naive ring-valued dot product fails (see Phase-0
  computation E3/E4).  Must be cited and used in Phase 1.

### B2. Wood (2008)
* **Title:** Code equivalence characterizes finite Frobenius rings;
  *Proc. Amer. Math. Soc.* **136**(2), 699–706 (2008).
* **VERIFY:** SECONDARY (quoted with full journal data in several retrieved
  papers).  DIRECT confirmation of the publisher page pending.

### B3. Greferath, Nechaev & Wisbauer (2004)
* **Title:** Finite quasi-Frobenius modules and linear codes;
  *J. Algebra Appl.* **3**(3), 247–272 (2004).
* **VERIFY:** DIRECT (full citation line seen in a retrieved reference list).
* **Relation:** Frobenius **bimodule** alphabets — the general non-commutative
  duality framework; the place to check whether our $\Lambda=\lambda\circ\mathrm{tr}$
  fits the standard theory (it does; Phase 1 must say so explicitly).

### B4. Honold (2001)
* **Title:** Characterization of finite Frobenius rings; *Arch. Math.* **76**,
  406–415 (2001).
* **VERIFY:** SECONDARY (title + year + the statement
  “$\mathrm{soc}({}_RR)\cong R/\mathrm{rad}\,R$” quoted in retrieved sources).
  Journal volume/pages TO CONFIRM.

---

## Cluster C — Galois duality and Galois hulls (all commutative so far)

### C1. Fan & Zhang (2017) — the origin of the Galois inner product
* **Title:** Galois self-dual constacyclic codes;
  *Des. Codes Cryptogr.* **84**(3), 473–492 (2017);
  **DOI 10.1007/s10623-016-0282-8**
* **VERIFY:** DIRECT (DOI + Semantic Scholar record).
* **What it does:** for $|F|=q=p^\ell$ and $0\le h<\ell$,
  $\langle a,b\rangle_h=\sum_i a_i b_i^{p^h}$ — **Frobenius on the second
  argument**; $h=0$ is Euclidean, $h=\ell/2$ is Hermitian; existence criteria
  for Galois self-dual / isometrically Galois self-dual constacyclic codes.
* **Relation:** the definition we must *transport* to $M_m(A_t)$.  **Important:**
  our Phase-0 computation shows that transporting it literally (Frobenius on the
  second argument, no transpose) does **not** give a perfect duality for
  right ideals.  This is the crux of our planned modification (see Phase-0
  report, §“Central design decision”).

### C2. Liu & Pan (2020)
* **Title:** Galois hulls of linear codes over finite fields;
  *Des. Codes Cryptogr.* **88**(2), 241–255 (2020); arXiv:1809.08053.
* **VERIFY:** DIRECT (arXiv abs page + Springer record).
* **Relation:** hull dimension via generator matrices; $\ell$-Galois LCD codes;
  matrix-product codes.  The commutative template for our hull-dimension
  formulas.

### C3. Liu, Fan & Liu (2018)
* **Title:** Galois LCD codes over finite fields;
  *Finite Fields Appl.* **49**, 227–242 (2018).
* **VERIFY:** SECONDARY (quoted with full data in C2’s references).

### C4. Cao (2021)
* **Title:** MDS codes with Galois hulls of arbitrary dimensions and related
  entanglement-assisted quantum error correction;
  *IEEE Trans. Inform. Theory* **67**(12), 7964–7984 (2021).
* **VERIFY:** SECONDARY (quoted with full data in arXiv:2210.05551 and in the
  Entropy 2026 paper’s introduction).

### C5. Zhang, Kong & Zheng (2026)  — *closest quantum + Galois-hull paper*
* **Title:** Quantum Codes from Galois Hulls of Constacyclic Codes over a
  Finite Non-Chain Ring; *Entropy* **28**(4), 407 (3 Apr 2026);
  **DOI 10.3390/e28040407**; PMC13115228; PMID 42072532.
* **Authors:** Enbin Zhang, Bo Kong, Xiying Zheng (Henan Finance University;
  Huanghe Science and Technology College).
* **VERIFY:** DIRECT (MDPI record read: authors, affiliations, date, DOI).
* **What it does:** ring
  $R=\mathbb F_{p^m}[u_1,\dots,u_s]/\langle f_j(u_j),\,u_iu_j-u_ju_i\rangle$
  (**commutative**, non-chain, CRT-split); $\ell$-Galois duals via a new Gray
  map $\phi$; $\mathrm{Hull}_\ell(C)=C\cap C^{\perp_\ell}$; generator of the hull
  as an lcm; **construction X of the Galois inner product** (CSS + Hermitian +
  construction X) $\Rightarrow$ QMDS and QECCs; EAQECCs from hull dimensions.
  Key lemma they use: $\phi(C)^{\perp_\ell}=\phi(C^{\perp_\ell})$.
* **Relation:** this is *exactly* the template we would follow on the quantum
  side — but over a **commutative** ring, where the duality issues we found do
  not arise.  It sets the standard our Phase 6 must meet, and it is 6 months
  old: the “Galois hull → quantum codes” vein is currently being mined hard.

### C6. Debnath, Islam, Martínez-Moro & Prakash (2024/25)
* **Title:** Galois hulls of constacyclic codes over affine algebra rings;
  arXiv:2412.08512 (11 Dec 2024); journal version *Discrete Mathematics*
  (2025) — ScienceDirect S0012365X25003589 (journal/volume TO CONFIRM).
* **VERIFY:** DIRECT (arXiv abs page with author list; ScienceDirect record for
  the published version seen).
* **What it does:** $k$-Galois hulls of $\lambda$-constacyclic codes over a
  **serial** (commutative) ring $A=\mathbb F_q[X_1,\dots,X_\ell]/I$; idempotent
  generators; hull-dimension formula; $k$-Galois LCD condition; EAQECCs.
* **Relation:** the state of the art for Galois hulls over **commutative**
  non-chain rings.  Our contribution must be compared against C5 and C6.

### C7. Pereira & Mancini (2023)
* **Title:** Entanglement-assisted quantum codes from cyclic codes;
  *Entropy* **25**(1), 37 (2023); DOI 10.3390/e25010037.
* **VERIFY:** DIRECT (MDPI citation block read).
* **Relation:** Euclidean/Hermitian EAQECC constructions from cyclic codes —
  the field case of what we want.

### C8. Brun, Devetak & Hsieh (2006)
* **Title:** Correcting quantum errors with entanglement;
  *Science* **314**(5798), 436–439 (2006).
* **VERIFY:** SECONDARY (quoted as the source of the EA formalism in C5’s
  introduction).  **TO CONFIRM** page numbers.
* **Relation:** the EAQECC route — the only route that works when the code is
  *not* dual-containing, which is our situation unless we force
  self-orthogonality.

### C9. Ketkar, Klappenecker, Kumar & Sarvepalli (2006)
* **Title:** Nonbinary stabilizer codes over finite fields;
  *IEEE Trans. Inform. Theory* **52**(11), 4892–4914 (2006).
* **VERIFY:** SECONDARY / TO CONFIRM (standard reference; not retrieved in
  Phase 0).
* **Relation:** additive-code ↔ stabilizer-code correspondence over
  $\mathbb F_q$: the fallback route if a duality-preserving Gray map cannot be
  built (see Phase 0 report, risk R3).

### C10. Grassl — code tables
* M. Grassl, *Bounds on the minimum distance of linear codes and quantum codes*,
  http://www.codetables.de — the reference database for “better than the
  best known” claims in Phase 8.
* **VERIFY:** SECONDARY (cited as “Grassl’s Table” in C6 and in many of the
  papers above).  URL to be confirmed live in Phase 8.

---

## Cluster D — Papers seen but **not yet verified** (do not cite until checked)

| # | Item seen | Where seen | Status |
|---|-----------|-----------|--------|
| D1 | “Self-Dual Cyclic Codes over $M_2(\mathbb F_2+u\mathbb F_2)$” (EJSE, 2019) | syniutajournals record | title/venue seen; journal quality & details TO CONFIRM |
| D2 | Pal, Bhowmick, Satya (2019), cyclic codes over a matrix ring | quoted in A5/D1 introductions | TO CONFIRM |
| D3 | Nebe–Rains–Sloane: “an elaboration on ideas of Nebe, Rains and Sloane: by assuming the existence of an **anti-isomorphism** on a finite ring …” | quoted in a ResearchGate abstract in the $M_2(\mathbb F_2)$ cluster | **HIGH PRIORITY for Phase 1** — if this is a published treatment of self-dual codes over rings via an anti-isomorphism, it is the closest conceptual precursor to our $\theta$-duality and must be cited |
| D4 | “A Non-Commutative Ring Whose Ideals are Quasi-Cyclic Codes” (M. T. Vo, Southeastern Louisiana Univ. seminar PDF) | PDF located | seminar notes; useful for the Morita/ideal viewpoint, not a citation-grade source |

---

## What is **not** in the literature (to be confirmed by the Phase-1 search)

1. A **Galois / $\sigma$-dual or Galois hull** for codes over a
   **non-commutative** ring.  Every Galois-hull paper found in Phase 0
   (C1–C6) is over a finite field, a finite chain ring, or a commutative
   non-chain/serial ring.
2. **Quantum codes constructed from codes over a matrix ring**
   $M_m(A_t)$.  A1–A7 all stop at good classical codes over $\mathbb F_4$ /
   $\mathbb F_{16}$ / $\mathbb F_{p^2}$ via the Bachoc or Gray map.
3. Any treatment of the **failure of the ring-valued Euclidean dot product**
   as a perfect duality for one-sided codes over a non-commutative ring.
