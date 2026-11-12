# Final audit decision

## Decision

# **REJECT AS SUBMITTED — DO NOT PROCEED WITH THIS BLUEPRINT IN ITS CURRENT FORM**

This is the audit's no-go decision for the submitted blueprint, not a conclusion that all research on constacyclic codes or quantum codes over matrix rings is impossible. A substantially revised proposal may be considered only after explicit researcher approval.

## Direct answers

### Is the blueprint reliable?

**No.** Its key ring claim is wrong: \(M_4(\mathbb F_2[u]/(u^k))\) is noncommutative and not local, with radical quotient \(M_4(\mathbb F_2)\), not residue field \(\mathbb F_{16}\). The proposed unit test, order-5 “central” multipliers, local CRT factors, and downstream ideal/cardinality framework therefore do not describe the named matrix ring. Duality and Gray-map transfer are also left as goals rather than proved properties.

### Is it novel?

**Not established.** The \(k=2\) cyclic-code case has a 2022 journal article and correction; the \(k=3\) case has an ISIT 2025 paper; and a 2026 preprint treats cyclic codes for general \(k\). A 2026 QIP paper studies quantum construction from cyclic codes over \(M_3\)-matrix rings, alongside a substantial existing constacyclic/non-chain-ring quantum literature. These do not prove that a valid \(M_4\) constacyclic/quantum theorem cannot be novel, but the blueprint has not demonstrated a distinct, valid contribution.

### Is it ready for research execution or a Q1 submission?

**No.** The algebra, multiplier convention, polynomial/module model, involution and inner product, dual theorem, Gray-map properties, novelty position, and exact-distance methodology must be resolved first. Q1 quartile status is also database/category/year-dependent and does not remedy missing mathematical foundations.

## Basis for the no-go decision

1. A foundational matrix-ring/local-ring contradiction affects every later section.
2. The chosen order-5 multipliers are not central units of the stated ring, so the proposed ordinary polynomial-ideal framework is not justified.
3. The structural, cardinality, dual-containment, and Gray-map theorems are mostly targets contingent on that invalid framework.
4. The quantum construction is standard only after a valid \(\mathbb F_{16}\)-linear Hermitian dual-containing image exists; the blueprint does not establish one.
5. Prior art is material and incompletely represented; novelty remains unverified.

## Scope and stop point

The requested audit files and consolidated PDF/ZIP are the final deliverables. No paper was written, no construction or theorem was developed, no computation or code-parameter search was run, and no correction was applied to the uploaded blueprint. The original uploaded PDF remains unchanged. **Stop here and wait for explicit researcher approval** before any literature expansion, blueprint modification, proof work, implementation, or parameter search.

## Primary references

- Joshi, Patel & Prakash, [arXiv:2602.18255v1](https://arxiv.org/abs/2602.18255), cyclic codes over a class of matrix rings, submitted 20 February 2026.
- Patel, Prakash & Islam, [“Cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2)\)”](https://doi.org/10.1007/s12095-022-00572-9), 2022, with [published correction](https://doi.org/10.1007/s12095-022-00584-5).
- Joshi, Patel & Prakash, [“Quantum codes construction from cyclic codes over matrix rings”](https://doi.org/10.1007/s11128-026-05230-0), *Quantum Information Processing* 25, 207 (2026).
- Joshi, Patel & Prakash, “Construction of new codes over \(\mathbb F_{16}\) from cyclic codes over \(M_4(\mathbb F_2+u\mathbb F_2+u^2\mathbb F_2)\),” IEEE ISIT 2025; cited in the 2026 QIP paper, Ref. 19.
