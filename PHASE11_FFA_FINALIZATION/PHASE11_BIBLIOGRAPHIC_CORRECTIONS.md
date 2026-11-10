# Phase 11 / Task E — Bibliographic corrections

Date: 2026-11-10. Method: append-only, as required. Nothing in any prior
document was deleted or rewritten; corrections were appended as correction
records, and no content was silently altered.

## 1. Headline finding

**The manuscript's bibliography, `PAPER/references.bib`, is correct. Four
venue attributions in the Phase 9 journal-selection documents were wrong.**

This distinction matters: the error never reached the manuscript, so nothing
in the paper needs correcting. What needed correcting were the *arguments*
built on those attributions — in particular the claim that the manuscript
already cites FFA papers, which was used as evidence of topical fit and which
would have repeated a falsehood in a cover letter.

## 2. The four errors

| # | key | Phase 9 attribution (WRONG) | Correct venue | Verification |
|---|---|---|---|---|
| 1 | `FanZhang2017GaloisSelfDual` | *Finite Fields Appl.* | **Designs, Codes and Cryptography** 84(3), 473–492, doi 10.1007/s10623-016-0282-8 | Springer article page: "Designs, Codes and Cryptography, Volume 84, pages 473–492 (2017)", published 29 Sep 2016 |
| 2 | `LiuPan2020GaloisHulls` | *Finite Fields Appl.* | **Designs, Codes and Cryptography** 88(2), 241–255 | Springer record for the article |
| 3 | `Cao2021MDSGaloisHulls` | *Discrete Math.* | **IEEE Transactions on Information Theory** 67(12), 7964–7984 | Author's publication list and three independent reference lists |
| 4 | `Dinh2024CyclicRingsOfMatrices` | *J. Algebra Appl.* | **Advances in Mathematics of Communications** 18(4), 1100–1122, doi 10.3934/amc.2022073 | AIMS article page; corroborated by Google Scholar, Delhi Mathematics Dept. publications list, and a 2026 arXiv paper's reference list |

**`references.bib` was checked and carries the correct venue in all four
cases.** No change to `references.bib` was made, and none is warranted: the
standing instruction is not to modify it unless a genuine error is found
there, and none was.

## 3. Corrected census of the 13 cited works

| venue | count | works |
|---|---:|---|
| IEEE Trans. Inform. Theory | 3 | Greferath–Schmidt 1999; Cao 2021; Ketkar et al. 2006 |
| Designs, Codes and Cryptography | 2 | Fan–Zhang 2017; Liu–Pan 2020 |
| Cryptography and Communications | 1 | Luo–Parampalli 2018 |
| Advances in Mathematics of Communications | 1 | Dinh et al. 2024 |
| Entropy | 1 | Zhang–Kong–Zheng 2026 |
| J. Franklin Inst. | 1 | Alahmadi et al. 2013 |
| J. Pure Appl. Algebra | 1 | Wood 1999 |
| J. Appl. Math. Comput. | 1 | Si–Niu 2023 |
| arXiv e-print | 1 | Joshi–Patel–Prakash 2026 |
| online tables (misc) | 1 | Grassl, codetables.de |
| **Finite Fields and their Applications** | **0** | — |

**Total: 13.** The Phase 9 statement that two of the 13 cited works are FFA
papers is **withdrawn**.

## 4. Documents corrected (append-only)

| document | action taken |
|---|---|
| `PHASE9_JOURNAL_SELECTION/PHASE9_SOURCE_VERIFICATION.md` | Correction record appended: the four-row correction table and the corrected census. The original table above it is retained unaltered. |
| `PHASE9_JOURNAL_SELECTION/PHASE9_FINAL_RECOMMENDATION.md` | Correction record appended: point 2 and the Discrete Mathematics claim withdrawn as stated; points 1, 3, 4 preserved. |
| `PHASE9_JOURNAL_SELECTION/PHASE9_JOURNAL_COMPARISON.md` | Correction record appended: three wrong attributions corrected; the J. Algebra Appl. fit score noted as reduced. |
| `PHASE9_JOURNAL_SELECTION/PHASE9_MANUSCRIPT_PROFILE.md` | **No correction required.** Its reference to "the Fan–Zhang, Liu–Pan, Cao, Zhang–Kong–Zheng line" names authors only and asserts no venue. |
| `PHASE9_JOURNAL_SELECTION/PHASE9_EVIDENCE_REGISTER.md` | **No correction required** — no venue attributions for these four works found in it. |

## 5. Does this change the FFA recommendation?

**No. The recommendation stands, but one of its supporting arguments is
withdrawn.**

| argument | status after correction |
|---|---|
| (1) FFA's aims and scope name algebraic coding theory, cryptology and combinatorial design theory | **UNCHANGED — verified directly from the FFA guide** |
| (2) The manuscript's citation lineage already runs through FFA | **WITHDRAWN — false; zero FFA papers are cited** |
| (3) FFA is currently publishing in this area (Vols 109, 110, 111, 112 verified) | **UNCHANGED — verified directly from FFA TOCs** |
| (4) FFA tolerates structural negative results; "very strict refereeing standards" | **UNCHANGED — verified from the FFA guide** |
| (5) FFA is Q1 (SJR 2025 = 0.906) | **UNCHANGED** |

Three of the five arguments are unaffected and each was verified directly
against the official FFA pages, not inferred from the bibliography. The
recommendation therefore does not depend on the withdrawn argument.

**Practical consequence:** the withdrawn argument must **not** appear in any
cover letter or submission communication. Doing so would repeat a factual
error to an editor.

## 6. Status

**CORRECTED.** All four errors recorded and corrected append-only. No
protected file was modified; `references.bib` and `PAPER/main.tex` are
byte-identical to their pre-Phase-11 state (hashes in
`PHASE11_FINAL_COMPLIANCE_MATRIX.md`).
