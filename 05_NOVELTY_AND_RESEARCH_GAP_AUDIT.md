# Novelty and research-gap audit

## Executive assessment

**The blueprint's novelty claim is not established.** The exact proposed conjunction—an appropriately defined constacyclic family over the stated \(M_4\)-matrix ring, a valid field image, and quantum codes—was not identified as an exact duplicate in the targeted search. That is not proof of novelty. The claimed gap omits direct prior work on the same matrix-ring family and has a foundational mismatch: the order-5 multipliers are not central scalars of the stated ring, while the proposed local-ring quotient model is not the matrix ring.

## Claim-by-claim novelty audit

### “The matrix-ring paper studies only cyclic codes and stops at classical \(\mathbb F_{16}\) codes.”

This is a fair description of the 2026 arXiv v1 preprint's stated scope: cyclic codes, dual formulas, and Gray/Bachoc images over \(\mathbb F_{16}\). It does not mean the cyclic/dual/Gray foundations are new. The 2022 \(k=2\) article and 2025 \(k=3\) ISIT paper cover direct specializations; the 2026 preprint covers general \(k\) as a preprint.

### “The quantum paper does CSS only for \(M_3\).”

The 2026 *Quantum Information Processing* article's matrix-ring setting is \(M_3\), not \(M_4\), and it uses a CSS route with a new inner product/map. That is adjacent, not a direct duplicate. It is nevertheless close prior art for quantum construction from cyclic matrix-ring codes and demonstrates that dual transfer through a Gray map is not automatic.

### “\(M_4\) + constacyclic + quantum is not covered in either introduction.”

This phrase is not enough to establish a research gap. A novelty review must check full texts, references, current publications/preprints, and adjacent formulations, not only introductions. The 2025 ISIT \(k=3\) paper and 2022 corrected \(k=2\) article are not mentioned in the blueprint's stated gap. The 2021–2026 constacyclic/non-chain-ring quantum literature also covers the general methods and expected claims.

### “Replacing cyclic by constacyclic opens new lengths and codes cyclic codes cannot reach.”

No theorem or example supports this. The claimed image length \(N=4kn\) is independent of \(\lambda\); the same \(k,n\) gives the same block length. A different shift might yield a different code family in a valid setup, but “new lengths” and superiority to every cyclic family require a precise comparison and evidence. Moreover, the proposed fifth-root multipliers are noncentral in \(M_4(A_k)\); the blueprint's polynomial-ideal route does not accommodate them as written.

## Prior-art map

- **Same ring, cyclic codes, duals and \(\mathbb F_{16}\)-linear Gray images:** Patel–Prakash–Islam (2022), exact \(k=2\), with a published correction.
- **Same ring family, cyclic codes:** Joshi–Patel–Prakash (ISIT 2025), exact \(k=3\) case.
- **Same ring family, general \(k\), cyclic codes and dual formulas:** Joshi–Patel–Prakash (arXiv:2602.18255v1, 2026 preprint).
- **Matrix-ring quantum construction:** Joshi–Patel–Prakash (QIP 2026), \(M_3\) rather than \(M_4\), with CSS and a map designed to transfer a nonstandard dual.
- **Constacyclic/Hermitian/quantum methods on finite non-chain rings:** papers from 2021, 2022, 2024, and September 2026 listed in the literature audit. These are adjacent families, not the same matrix ring.

## What might remain as a research gap

A carefully defined \(M_4\) constacyclic theory using an admissible multiplier class and a proved map/inner-product bridge might contain new results. This audit does **not** certify that gap. The blueprint's current candidate family does not yet provide a valid object on which to assess novelty: it conflates a matrix ring with a commutative local ring, and it does not specify the right/left action for noncentral multipliers. Novelty must be reassessed only after those choices are approved and the claimed theorem statements are made precise.

## Minimum standard for a later novelty claim

1. State the exact ring presentation with all cross-relations and identify central versus noncentral elements.
2. Define the code module side, multiplier class, shift, and polynomial/endomorphism model.
3. State a theorem that is genuinely new relative to the cyclic results at \(k=2,3\) and general \(k\), and separate structural novelty from new parameter tuples.
4. Compare the exact duality, Gray map, and quantum construction against the 2026 \(M_3\) CSS method and established constacyclic quantum work.
5. For each claimed “new” quantum code, compare exact \((N,K_q,D_q)\) parameters against current sources, using exact distances or clearly labelled certified bounds.
6. Record database/search terms, dates, citations, and excluded near-matches. Do not treat a novelty search as a theorem proof.

## Decision

**Novelty: unverified, not presently defensible as claimed.** This is not a finding that no novel contribution can exist; it is a finding that the supplied blueprint has not demonstrated one. See `04_LITERATURE_AND_PRIOR_ART_AUDIT.md` for source details and limitations.
