# Literature and novelty recheck

**Audit execution:** 2026-11-13 UTC (workspace clock). **Verdict: bounded comparison completed; novelty/Q1 readiness not certified.** The unchanged blueprint overlaps the author's own completed campaign. The earlier recommendation to submit immediately is not supported until the mathematical and benchmarking defects in this review are resolved.

## 1. Evidence standard and actual coverage

The full source register, retrieval scope, selected excerpts and endpoint results are preserved as **reviewer notes**, not invented raw web captures, in [LITERATURE_WEB_RECHECK_NOTES.md](evidence/LITERATURE_WEB_RECHECK_NOTES.md). Source IDs L01–L22 and B01–B07 below refer to that register. The [entry-by-entry table](evidence/bibliography_recheck_by_entry.csv) records all **50 occurrences** across the **37-entry repository bibliography** and **13-entry manuscript bibliography**.

- All 37 repository entries were inventoried. **17** have a fresh primary/registry/endpoint check, **1** has publisher-search-level corroboration, **1** remains an unverified placeholder with genuine related sources located, and **18** were **not freshly reverified**. This is not a complete current 37-entry sweep.
- All 13 manuscript entries received a fresh metadata/endpoint check; this does not validate all cited theorems. Several entries need correction.
- The large bibliography has **12 DOI fields / 25 absent**; the manuscript has **9 / 4**. A present DOI may be wrong, a missing DOI does not imply a nonexistent paper, and an arXiv DOI is not a journal DOI.
- The repository's `DIRECT` (13), `SECONDARY` (23) and pending/qualification (24) flags **overlap**. “37-entry verified bibliography” is not an independent finding.
- All **7 supplied PDFs** parse, contain extractable text, and match the **actual original ZIP members** byte-for-byte. See [supporting-file checks](evidence/supporting_checks_v2/supporting_file_checks.json). This validates identity/readability, not the correctness of their mathematics.
- Primary abstracts/records, previews, supplied full texts, registry metadata, historical tags and search-only leads are kept separate. No exhaustive database search, priority certificate, journal-quartile check, acceptance-status check, or complete proof audit of competing papers was performed.

## 2. Updated bounded comparison matrix

| Reference / evidence | Ring and family | Duality / hull scope actually supported | Gray / quantum scope | Consequence for the proposed gap |
|---|---|---|---|---|
| Alahmadi–Sboui–Solé–Yemen 2013, JFI 350(9),2837–2847; **L14/L09** | M2(F2), cyclic right ideals | Classical Euclidean/Hermitian conventions; do not assume their R-valued product yields this audit's same-sided size law | Classical matrix-ring images | Existing matrix-cyclic framework; correct journal DOI `.023`, not manuscript `.008` |
| Luo–Parampalli 2018; **L09** | M2(F2+uF2), odd length | Classical structure | Bachoc/Lee-type isometric images; classical codes | Nilpotent matrix alphabet and images are not new |
| Dinh et al. 2024, AMC18(4),1100–1122; **L08** | **M2(F2[u]/(u^k))**, odd length | Classical cyclic structure/duals | Classical image constructions | Same r=2 coefficient family is already occupied; distinguish field extension/Galois-hull content rather than claiming a new ring |
| Islam–Prakash–Bhunia 2024, JDMSC27(1),189–201; **L10** | M3(Fp), certain primes; publisher abstract specifies p divides N | Classical cyclic structure | Classical isometry/images to extension-field alphabet | Resolves A9b venue/DOI. Not the separate PJM M3(F3) title and not A11 |
| Pal–Bhowmick–Bagchi 2019, M4(F2); Patel–Prakash–Islam 2022, M4(F2+uF2); supplied PDFs | Matrix sizes 4, t=1/2 | Classical cyclic/self-dual setting | Classical images | Larger matrix size is not itself a gap. Metadata here partly inherited/PDF-supported, not a new full publisher sweep |
| Joshi–Patel–Prakash, arXiv2602.18255v1; **L11 + supplied PDF** | M4(F2[u]/(u^k)) | Euclidean/Hermitian classical constructions reported | Gray/Bachoc images to F16 reported | Recent classical overlap; no journal DOI verified; do not endorse asserted ring isomorphisms merely because PDF is authentic |
| **Joshi–Patel–Prakash, QIP25:207(2026), DOI10.1007/s11128-026-05230-0; L01 + supplied PDF** | M3 truncated-ring cyclic codes | Euclidean/Hermitian quantum-facing duality reported; no general Galois-hull framework located in the bounded reading | **Gray + CSS quantum output** reported | Broad “first quantum codes from cyclic codes over matrix rings” cannot be claimed. Cite/discuss, while independently checking mathematical comparability |
| Wood1999/2010; Szabo–Wood2017; Dougherty–Leroy2016; **L03–L05/L20** | Finite noncommutative Frobenius rings/modules | Anti-isomorphism/sesquilinear forms, same-/opposite-sided annihilators, cardinality and mixed double duals | Foundational framework | The anti-automorphism duality mechanism is published. This does not automatically prove the positive same-twist formula without convention checking |
| Fan–Zhang2017, DCC84,473–492; **L06** | Finite-field constacyclic | Galois inner products/self-duality | No matrix-ring hull stack asserted | Foundational field convention differs by which argument is twisted |
| Liu–Pan2020, DCC88,241–255; **L07** | Finite-field linear/matrix-product codes | Galois hull dimension, generator calculation, Galois LCD | Field-level hull theory | Hull dimension from a Gram/generator matrix is not new in itself |
| Liu–Yu–Hu2019; Cao2021; **L22/L15** | Finite-field codes / GRS-type families | k-/ell-Galois hull or dual constructions | **EAQECC** | Hull-to-EA mechanics already occupied; field/matrix bridge must be justified, not asserted |
| Zhang–Kong–Zheng2026, Entropy28(4):407; **L02** | **Commutative** finite non-chain ring, constacyclic | Galois hulls | Gray transfer + QECC/EAQECC/Construction X | Very close ingredient overlap; noncommutativity alone is not a proven new theorem |
| Debnath–Islam–Martínez-Moro–Prakash, Discrete Math349(2):114750(2026); **L13** | Commutative squarefree affine algebra | Galois hull generators/dimensions/LCD | EA examples | Frozen 2024/25 citation must distinguish preprint and journal record |
| Kushwaha–Prakash, arXiv2512.12335 and2601.06609; **L12** | **Noncommutative non-unital** ring E, free codes | Hulls and left/right/two-sided symplectic hulls | No matrix-ring Galois/quantum conclusion inferred | Broad “first hulls over noncommutative rings” unavailable; unital matrix specialization still needs exact comparison |
| Si–Niu2023; Du–Niu2025; **L21** | Skew cyclic over M2(F2) | Skew structure and duals / weight distributions | No full two-twist hull/quantum result located here | P3 is a candidate extension question, not an unoccupied-intersection proof |
| **Author's included FFA-prepared manuscript and data** | M2(Fq[u]/(u^t)), right cyclic ideals | Theta-Galois duality, hulls, nonreflexive regimes, structural computations | Coefficient Gray map, SO/DC/EA, q4/8/9, **28 supplied records** | **Direct internal overlap with the unchanged blueprint.** A campaign exists; this review does not certify every result or publication readiness |

This matrix describes **reported scope**, not an endorsement of every competitor theorem. “No located treatment” cannot be promoted to “unpublished everywhere.”

## 3. Specific bibliographic corrections

| Original issue | Independently supported correction | Evidence / remaining limit |
|---|---|---|
| Manuscript Alahmadi DOI `10.1016/j.jfranklin.2013.06.008` | **10.1016/j.jfranklin.2013.06.023** | L14a correct authors/pages; L09 full title. L14b shows `.008` is an unrelated control-systems article |
| Six-report Fan–Zhang comparison volume85 | **84** | L06; both original BibTeX entries already say84 |
| Liu–Pan DOI absent | **10.1007/s10623-019-00681-2** | L07 publisher record; preserve2020 issue versus2019 online date |
| Cao DOI absent | **10.1109/TIT.2021.3117562** | L15 registry/title/pages |
| Ketkar first author expanded as “Andreas” | **Avanti Ketkar** | Registry initial A.; university record corroboration. [2](https://vivo.library.tamu.edu/vivo/display/n62208SE) |
| Greferath–Schmidt second author expanded as “Sergio R.” | Use verified **S. E. Schmidt** pending full-name authority | L18 registry. Do not fabricate a full name |
| Large-bib Oggier same-title record has Viterbo,2010 | **Oggier–Solé–Belfiore,2012**, IEEE TIT58(2),734–746; DOI **10.1109/TIT.2011.2173732** | L19 registry |
| NRS-themed anti-isomorphism placeholder | Distinguish **NRS2006 book** from **Wood2010 article**, DOI **10.1504/IJICOT.2010.032867**, and **Szabo–Wood2017**, DOI **10.13069/jacodesmath.284934** | L03/L04; do not turn the placeholder into an invented citation |
| A9b venue unknown | JDMSC27(1),189–201(2024); DOI **10.47974/JDMSC-1730** | L10. This DOI does **not** belong to the distinct five-page A11/t=3 paper |
| Affine-algebra work labelled2024/25 only | Discrete Math349(2),114750(2026); DOI **10.1016/j.disc.2025.114750** | L13; preprint remains arXiv2412.08512 |
| QIP2026 absent from manuscript citations | Add/discuss the authentic L01 work in any **authorized future revision** | It is already identified by the six reports, but remains absent from the included 13-entry manuscript bibliography |

The publisher-search-level Du–Niu record supports DOI10.3934/math.2025520, not a full technical check. [1](http://www.aimspress.com/article/doi/10.3934/math.2025520) The Liu–Yu–Hu publisher search record supports DOI10.1016/j.ffa.2018.09.001 and metadata, not an independent proof audit. [1](https://www.sciencedirect.com/science/article/pii/S1071579718301084)

## 4. Benchmarking requires the **physical** alphabet

**INCORRECT:** the manuscript/prior table treats the legacy backend `q=4` result as a physical-q=4 code and `q=9` as physical-q=9. The returned headers actually give **physical q=2 and q=3**, respectively. “Construction over GF(p²)” is the additive construction alphabet, not a reason to relabel qubits/qutrits as physical p²-level systems.

| Fresh probe | Returned physical header and bounds | Permitted interpretation |
|---|---|---|
| B01: legacy q=4,n20,k4 | `[[20,4]]_2`,6..6 | Binary, not a comparator for supplied `[[20,4,4]]_4` |
| B02: legacy q=9,n24,k8 | `[[24,8]]_3`,6..8 | Qutrit, not a comparator for supplied `[[24,8,4]]_9` |
| B03: legacy **q=16**,n20,k4 | **`[[20,4]]_4`,7..8** | Correct same-physical-alphabet query. The supplied d4 code is below a known d7 construction; no record claim |
| B04: legacy **q=64**,n12,k4 | **`[[12,4]]_8`,5..5** | Physical-q8 stabilizer bounds do exist at least for this tuple |
| B05: legacyq81,n24,k8 | Not available | No physical-q9 bound obtained here; no global nonexistence claim |
| B06: new front end | Local dimensions2,3,4,5,7,8 | Refutes blanket “q8 untabulated” wording |
| B07: actual `/EAQECC/index.html` | Qubit/qutrit **EA** tables, non-catalytic c | Refutes “no EA tables exist”; does not by itself give a q4/8/9 EA comparison |

Exact URLs and selected returned text are in the preserved notes. An old 404 at `QECC-EA.php` proves only that the guessed endpoint failed. It cannot establish absence of all EA tables.

**Required consequence:** retire/review the old “record”, “gap-to-best” and “q8 unavailable” labels until a same-physical-q, same N,K, same EA/stabilizer and same entanglement convention comparison is rebuilt in a separately authorized correction pass. The two physical-q4 SO/DC records are arithmetically valid but **not** best-known-distance records at N20,K4 on the fresh evidence. No silent replacement benchmark table has been made. No q4/8/9 EA optimality is established.

## 5. Blueprint versus prior FFA campaign

The blueprint asks for ring/module foundations, a justified Galois pairing, cyclic dual/hull structure, Gray transfer, CSS/EA output and a manuscript. The included campaign already contains those same layers at matrix-size2, with uniformly stated duality results and finite examples. Therefore **re-executing the unchanged blueprint is duplicative**, even though this review exposes errors requiring correction in the previous presentation.

There is no repository evidence establishing that the FFA manuscript was actually submitted, accepted, or received an editorial decision. The Phase-23 Option-C compliance record is preparation/history, **not editorial authorization**. Only the author can resolve the true submission status. The source also has canonical and staged variants; the later staged §08 correctly fixes the “all three certification methods” overclaim, whereas the deeper route/quotient/proof defects remain.

## 6. P1/P2/P3: differentiation must be proved, not promised

The labels in this section mean **research proposals**, not the pairing-options P1/P2/P3.

### Proposed P1 — odd-extension / nonreflexive quantum applications

**Classification: INCOMPLETE as a new problem; INCORRECT in the asserted “first q8 EA” subclaim.** Positive double dual, nonreflexivity, hull theory and q8 computations already exist. Four of the supplied, independently recertified EA records are over **physical q8**. An application layer cannot be called wholly absent. A genuinely twist-dependent new theorem or family might still be possible, but must differ from those records and from field Galois-EA literature. The ordinary EA formula uses **h_E**, not an arbitrary Galois hull dimension h_k; a valid bridge is required. No such new bridge has been implemented in this audit.

### Proposed P2 — matrix-size3 structural hulls

**Classification: INCOMPLETE; no novelty guarantee.** General-r pairing/Gray algebra already transfers, and classical/Euclidean-Hermitian quantum M3 neighbours exist. For M3(B), **principality is μ_B≤3**, so a nonprincipal hull needs **μ_B>3**, not merely μ_B=3. The coefficient Gray index is **9t**, not3. Complexity is |R|=p^(m t r²); the proposal's example m=t=2,r=3 gives **p^36**, not p^18. A viable study would need genuinely new structural/enumerative hull theorems and verified witnesses, not a larger matrix parameter table. None is claimed here.

### Proposed P3 — skew × Galois × matrix × hull × quantum

**Classification: INCOMPLETE; priority UNVERIFIABLE on this search.** Existing skew-matrix duality work prevents claiming the skew/matrix combination as new. The exact proposed two-twist structural question was not found in the bounded search, but this is not a LOW-risk or firstness certificate. Before treating R[X;α]/(X^n−1) as a ring, its quotient ideal must be two-sided; **α^n=id** is a standard sufficient condition for the advertised central polynomial. Compatibility of α with θ_k, duals, cyclic shifts, hulls and the quantum target is an unproved task, not a present theorem. Matrix-parameter changes, unspecified Ore quotients and a hoped-for compatibility theorem are not completed contributions.

## 7. Recommendation and author gate

1. **HOLD** submission-readiness and new-phase recommendations pending correction/independent re-audit of the blocking findings.
2. Confirm actual submission status and choose the authoritative manuscript baseline.
3. If the author wants further work, authorize a **correction-only** scope first, separately from any new research program.
4. Only after that gate, choose whether a narrowly differentiated P1, a structural P2, or an exploratory P3 merits a new proposal and literature search. This report selects none automatically.

No claim of Q1 viability, a guaranteed unoccupied intersection, acceptance, novelty, or journal ranking is supported by this review. No Phase1/P1/P2/P3 implementation, original-file revision, commit, push or submission has occurred.
