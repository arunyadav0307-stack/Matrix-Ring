# Literature and prior-art audit

**Purpose:** assess the blueprint's cited gap, not certify an exhaustive literature search. Search and source review were current to 12 November 2026. No quantum-code parameter search was run.

## 1. Direct matrix-ring prior art

### \(M_4(\mathbb F_2+u\mathbb F_2)\): the \(k=2\) case

Patel, Prakash and Islam, “Cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2)\),” *Cryptography and Communications* 14 (2022), 1021–1034, [DOI 10.1007/s12095-022-00572-9](https://doi.org/10.1007/s12095-022-00572-9). The publisher abstract states that this exact ring is studied, with cyclic-code structure, Euclidean and Hermitian duals, and a Gray image whose codes are \(\mathbb F_{16}\)-linear. This is the \(k=2\) member of the blueprint's matrix-ring family and is material prior art for its claimed ring/cyclic/duality/Gray-map foundation.

A published correction appeared 24 May 2022: [DOI 10.1007/s12095-022-00584-5](https://doi.org/10.1007/s12095-022-00584-5). The correction lists twelve equation/display corrections, including generator expressions and the displayed Gray-map matrix. Any reuse or comparison must consult the corrected version. The correction notice describes presentation/formula-display errors; this audit does not infer from that notice that every underlying theorem has been independently revalidated.

**Access limitation:** the full 2022 article body was not available in the workspace for line-by-line theorem verification. Its publisher metadata/abstract and the complete correction notice were reviewed. The existence and stated scope of the prior work are nevertheless clear.

### \(M_4(\mathbb F_2+u\mathbb F_2+u^2\mathbb F_2)\): the \(k=3\) case

Joshi, Patel and Prakash, “Construction of new codes over \(\mathbb F_{16}\) from cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2+u^2\mathbb F_2)\),” IEEE International Symposium on Information Theory (ISIT 2025). This conference paper is cited as reference 19 in the 2026 *Quantum Information Processing* article. It directly covers the \(k=3\) cyclic-code specialization. The ISIT 2025 proceedings table of contents lists the paper; see [proceedings listing](https://www.proceedings.com/content/082/082545webtoc.pdf).

### General \(k\), cyclic codes over \(M_4\)

Joshi, Patel and Prakash, “Construction of Cyclic Codes over a Class of Matrix Rings,” [arXiv:2602.18255v1](https://arxiv.org/abs/2602.18255), submitted 20 February 2026. The preprint treats \(M_4(\mathbb F_2[u]/\langle u^k\rangle)\), cyclic codes (odd-length structural results), Euclidean/Hermitian dual formulas, and Bachoc/Gray maps to \(\mathbb F_{16}\). It is direct overlap for the blueprint's cyclic baseline across general \(k\), though it does not by itself settle the proposed constacyclic extension or its quantum application. No journal version was confirmed in the sources checked; cite it as a preprint unless that status is rechecked.

The attached arXiv preprint's Theorem 4.1 is specifically an **odd-length cyclic Euclidean-dual** statement. Its proof presents a candidate dual submodule, establishes an inclusion by generator orthogonality, then compares cardinalities. It is not a theorem for nontrivial constacyclic multipliers and does not prove the blueprint's new component/Gray/quantum claims.

## 2. Matrix-ring quantum precedent

Joshi, Patel and Prakash, “Quantum codes construction from cyclic codes over matrix rings,” *Quantum Information Processing* 25, article 207 (2026), [DOI 10.1007/s11128-026-05230-0](https://doi.org/10.1007/s11128-026-05230-0), published 9 June 2026. It studies cyclic codes over \(M_3(\mathbb F_p[u]/\langle u^k\rangle)\), and for a matrix ring over \(\mathbb F_3\) gives a CSS route using a new non-degenerate inner product and a suitable Gray map. This is not the same alphabet or constacyclic family as the blueprint, but it is close matrix-ring/quantum prior art. Its full text expressly notes that an earlier Gray map did not transfer the required dual-containment property and introduces a different map/product pair. That makes the blueprint's Gray-map orthogonality claim a substantive proof obligation.

The 2026 article also cites both the 2022 \(M_4\) cyclic-code paper and the 2025 \(k=3\) ISIT paper. Those works must appear in any current account of the gap.

## 3. Constacyclic/quantum adjacent work

These works show that “constacyclic codes over finite non-chain rings,” Hermitian dual containment, Gray maps, and quantum constructions are established research themes. They are not direct duplicates of \(M_4(\mathbb F_2[u]/(u^k))\), but they make a novelty claim based only on combining the words “constacyclic” and “quantum” untenable.

- Alahmadi et al., “New quantum codes from constacyclic codes over a non-chain ring,” *Quantum Information Processing* 20, article 60 (2021), [DOI 10.1007/s11128-020-02977-y](https://doi.org/10.1007/s11128-020-02977-y).
- Islam, Patel and Prakash, “A family of constacyclic codes over a class of non-chain rings \(A_{q,r}\) and new quantum codes,” *Journal of Applied Mathematics and Computing* 68 (2022), 2493–2514, [DOI 10.1007/s12190-021-01623-9](https://doi.org/10.1007/s12190-021-01623-9). The article studies constacyclic and skew constacyclic codes and Hermitian-dual-containing conditions over a commutative non-chain family.
- Yadav et al., “Hermitian hull of constacyclic codes over a class of non-chain rings and new quantum codes,” *Computational and Applied Mathematics* 43, article 269 (2024), [DOI 10.1007/s40314-024-02789-1](https://doi.org/10.1007/s40314-024-02789-1).
- Tian, Gao and Gao, “Hulls of constacyclic codes over finite non-chain rings and their applications in quantum codes construction,” *Quantum Information Processing* 23, article 9 (2024), [DOI 10.1007/s11128-023-04230-8](https://doi.org/10.1007/s11128-023-04230-8).
- Tang et al., “Quantum codes from constacyclic codes over finite non-chain rings,” *Quantum Information Processing* 25, article 305 (2026), published 3 September 2026, [DOI 10.1007/s11128-026-05334-7](https://doi.org/10.1007/s11128-026-05334-7). Its ring is a commutative finite non-chain family, not the blueprint's matrix ring; it is current adjacent literature.

## 4. Earlier matrix cyclic-code context

The 2026 preprint cites earlier work including Pal, Bhowmick and Bagchi, “Cyclic codes over \(M_4(\mathbb F_2)\),” *Journal of Applied Mathematics and Computing* 60 (2019), 749–756, [DOI 10.1007/s12190-018-01235-w](https://doi.org/10.1007/s12190-018-01235-w), as well as work on \(M_2\) matrix rings. This is relevant background for the matrix-ring/\(\mathbb F_{16}\) coordinate viewpoint, not evidence that the proposed quantum extension is either novel or non-novel.

## 5. Audit of the blueprint's literature statement

The blueprint says the matrix-ring paper covers only cyclic codes and the QIP paper covers \(M_3\) quantum codes. Those scope descriptions are broadly accurate for the cited papers, but the gap argument is incomplete because it omits the exact \(k=2\) published article's correction, the \(k=3\) ISIT 2025 paper, several general constacyclic/quantum precedents, and current 2026 work. “The combination was not found in either introduction” is not a novelty test.

A targeted search did **not** establish a prior article exactly matching “\(M_4\), noncentral order-5 constamultiplier, Hermitian Gray image, and \(\mathbb F_4\) quantum codes.” It also did not establish that no such work exists. The search was not exhaustive, and the blueprint's multiplier/algebra framework is not yet coherent enough to define a stable novelty query.

## 6. Literature-review limits and required standard

- Search date: 12 November 2026; web metadata/abstracts and the supplied PDFs were reviewed.
- The 2026 arXiv preprint and QIP article were read in the supplied/extracted versions for relevant sections; the 2022 full article body was not available for complete theorem-by-theorem review.
- No citation chaining, database-by-database systematic review, or code-table search was performed.
- Before claiming novelty, a researcher must compare exact ring, module side, multiplier class, length hypotheses, dual form, map, and quantum parameters against the direct and adjacent works above, and document the search protocol. Novelty cannot be certified from this audit.
