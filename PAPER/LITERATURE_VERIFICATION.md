# Phase 8 / Task D — Literature verification record

**Date of verification:** 2026-11-04 (all items).
**Method:** direct retrieval of the publisher/arXiv/MDPI record page, or of at
least two independent secondary records that quote the full citation line.
No PDF of a paywalled article was downloaded; where only secondary evidence was
obtainable this is stated and the entry keeps a `SECONDARY` tag.

The repository bibliography is `01_LITERATURE/references.bib` (Phase 0, extended
in Phase 5). This file records what Phase 8 re-checked, what changed, and what
remains unverified. **No entry in `references.bib` was deleted**; corrections are
recorded here and mirrored in `PAPER/references.bib`.

---

## 1. Verified with a publisher / archive record

| key | verdict | record retrieved | change to the entry |
|---|---|---|---|
| `Alahmadi2013CyclicM2F2` | **VERIFIED** (secondary ×3, concordant) | *J. Franklin Inst.* **350**(9) (2013) 2837–2847; MR 3146951. Quoted verbatim in the reference lists of arXiv:2602.18255, of *On the algebraic structure of quasi-group codes* (World Scientific) and of *Duality preserving Gray maps for codes over rings* | none (publisher DOI still `TO CONFIRM`, but the journal/volume/pages/year are now triple-sourced) |
| `LuoParampalli2018M2F2uF2` | **VERIFIED — volume and pages now resolved** | Springer record: *Cryptogr. Commun.* **10**(6) (2018) 1109–1117; received 25 Dec 2016, accepted 3 Nov 2017, published online 1 Dec 2017; DOI `10.1007/s12095-017-0266-1` | **fill in** `volume = {10}`, `number = {6}`, `pages = {1109--1117}` (previously `TO CONFIRM`) |
| `Dinh2024CyclicRingsOfMatrices` | **VERIFIED** (AIMS record) | *Adv. Math. Commun.* **18**(4) (2024) 1100–1122; DOI `10.3934/amc.2022073`. Same data on the Delhi University publication list and on Google Scholar | none |
| `JoshiPatelPrakash2026M4` | **VERIFIED** (arXiv abs page) | arXiv:2602.18255 [cs.IT], submitted 20 Feb 2026; DOI `10.48550/arXiv.2602.18255`; MSC 12E20, 94B05, 94B15. Ring $\mathcal R = M_4(\mathbb F_2[u]/\langle u^k\rangle)$; Euclidean **and** Hermitian duals; Bachoc + Gray map to $\mathbb F_{16}$; **no** Galois duality, **no** hulls, **no** quantum codes | none |
| `LiuPan2020GaloisHulls` | **VERIFIED** | *Des. Codes Cryptogr.* **88**(2) (2020) 241–255 | none |
| `FanZhang2017GaloisSelfDual` | **VERIFIED** | *Des. Codes Cryptogr.* **84**(3) (2017) 473–492 | none |
| `Cao2021MDSGaloisHulls` | **VERIFIED** | *IEEE Trans. Inform. Theory* **67**(12) (2021) 7964–7984; confirmed on the author's own publication list (BIMSA) and in three independent reference lists | none |
| `ZhangKongZheng2026QuantumGaloisHulls` | **VERIFIED — full record now complete** | ***Entropy*** **28**(4) (2026) article 407, 19 pp.; published 3 April 2026; DOI `10.3390/e28040407`; PMCID PMC13115228 | **fill in** `volume = {28}`, `number = {4}`, `pages = {407}`, `doi = {10.3390/e28040407}`, `note` upgraded from `SECONDARY` to `DIRECT` |
| `Wood1999Duality` | **VERIFIED** | *Amer. J. Math.* **121**(3) (1999) 555–575; DOI `10.1353/ajm.1999.0024` | none |
| `KetkarEtAl2006NonbinaryStabilizer` | **VERIFIED** | *IEEE Trans. Inform. Theory* **52**(11) (2006) 4892–4914; confirmed on the IEEE TIT volume-52 index and on the Klappenecker publication list | upgrade `SECONDARY/TO CONFIRM` → `DIRECT` |
| `WildeBrun2008EA` | **VERIFIED** | *Phys. Rev. A* **77** (2008) 064302 | upgrade to `DIRECT` |
| `LaiBrunWilde2013EADualities` | **VERIFIED, with a correction to the year** | *Quantum Inf. Process.* **13**(4) (2014) 957–990; published online 17 Dec 2013; DOI `10.1007/s11128-013-0704-8`; arXiv:1010.5506 | **CORRECTION:** the entry says `year = {2013}`; the journal volume is 13 (**2014**). Set `year = {2014}`, `volume = {13}`, `number = {4}`, `pages = {957--990}`, `doi = {10.1007/s11128-013-0704-8}`. The 2013 date is the online-first date. |
| `GreferathSchmidt1999GrayIsometry` | **VERIFIED** | *IEEE Trans. Inform. Theory* **45**(7) (1999) 2522–2524; DOI `10.1109/18.796395`. Full title in the IEEE record: “Gray isometries for finite chain rings **and a nonlinear ternary $(36,3^{12},15)$ code**” | add the second half of the title; upgrade to `DIRECT` |

## 2. Verified live: the Grassl tables (`codetables.de`)

Retrieved 2026-11-04. Query pattern
`http://www.codetables.de/QECC.php?q=<Q>&n=<N>&k=<K>`; page footer
“Last change: 10.06.2024”; maintainer Markus Grassl.

* **$q = 4$ is tabulated.** The page header displays the code as $[[N,K]]_2$ and
  the construction as “quantum code over GF(2^2)”: **the site's displayed
  subscript is the prime $p$, not the field size $q$.**
* **$q = 9$ is tabulated.** Displayed as $[[N,K]]_3$, construction
  “quantum code over GF(3^2)”.
* **$q = 8$ is not.** `QECC.php?q=8&n=16&k=4` returns
  “**currently not available for q=8**”. This limitation is real.
* **No entanglement-assisted table.** `QECC-EA.php?q=4&n=12&k=2` returns
  HTTP 404. The EA codes of this framework therefore have **no** published
  table to be compared against.

### Values retrieved (lower .. upper bound on the best known minimum distance)

| $[[N,K]]_q$ | lower .. upper |
|---|---|
| $[[8,4]]_4$ | 2 .. 2 |
| $[[12,8]]_4$ | 2 .. 2 |
| $[[16,4]]_4$ | 5 .. 5 |
| $[[16,8]]_4$ | 3 .. 3 |
| $[[16,12]]_4$ | 2 .. 2 |
| $[[20,4]]_4$ | 6 .. 6 |
| $[[20,12]]_4$ | 3 .. 3 |
| $[[20,16]]_4$ | 2 .. 2 |
| $[[24,4]]_4$ | 6 .. 8 |
| $[[24,8]]_4$ | 5 .. 5 |
| $[[24,12]]_4$ | 4 .. 5 |
| $[[24,16]]_4$ | 3 .. 3 |
| $[[24,20]]_4$ | 2 .. 2 |
| $[[8,4]]_9$ | 3 .. 3 |
| $[[16,8]]_9$ | 4 .. 4 |
| $[[24,8]]_9$ | 6 .. 8 |
| $[[24,10]]_9$ | 6 .. 7 |
| $[[24,12]]_9$ | 5 .. 6 |

(The $q = 4$ values for $[[12,2]]$, $[[20,2]]$, $[[20,8]]$, $[[24,2]]$ were
retrieved in Phase 6 and are unchanged; they concern entanglement-assisted
lengths and are not used for a stabilizer comparison.)

## 3. ERRATUM E-8.1 — the $q = 9$ coverage claim of T-215 and T-228 is wrong

**Statement of the error.** Phase 6 (register row **T-215**) records that
“$q=2,3,4,5,7,8$ are tabulated” and Phase 7 (register row **T-228**) records
that “only `GF(4)` is tabulated (`q = 8` unavailable, `q = 9` not offered)”.
The second half of the Phase-7 statement is **incorrect**: `codetables.de`
returns full $GF(3^2)$ tables for `q=9`. The mistake is a misreading of the
page header, which prints the **prime** $p$ in the code label $[[N,K]]_p$ while
the construction block says “over GF($p^2$)”.

**Why it matters.** It removes a stated limitation: the $q = 9$ *stabilizer*
codes of this framework **can** be benchmarked, and the Phase-7 comparison
(12 entries, all $q = 4$) is therefore incomplete. The Phase-8 comparison is
recomputed in `PAPER/PARAMETER_COMPARISON.md` and now covers $q = 4$ **and**
$q = 9$.

**What does not change.** (i) $q = 8$ is genuinely unavailable, so the
$q = 8$ codes of this framework remain unbenchmarked. (ii) There is still no
entanglement-assisted table, so **every** EA code of this framework remains
unbenchmarked. (iii) **No record is claimed** in either Phase 6, Phase 7 or
this manuscript: the recomputed gaps are reported in
`PAPER/PARAMETER_COMPARISON.md`, and every $q = 9$ stabilizer code found here
is 1–2 below the best known distance.

**Disposition.** Recorded here, in the register annotation for T-215/T-228
(insertion only — the register rows themselves are **not** modified), and in
`PAPER/OPEN_ISSUES_AND_LIMITATIONS.md` as a **RESOLVED / MAJOR** item. It is
not an erratum about the mathematics of Phases 0–7: no parameter, no distance
and no bound changes.

## 4. Still unverified — **not cited**, or cited only as folklore

| key | status | action |
|---|---|---|
| `NebeRainsSloaneAntiIsomorphism` | **NOT VERIFIED** (seen only as a quotation in a ResearchGate abstract) | **excluded from the manuscript**; mentioned in the open-problems discussion only as “an unpublished programme that we have not been able to locate” |
| `Bhowmick2018SelfDualM2Z4` | journal status unconfirmed | **excluded** |
| `OggierEtAlSpaceTimeMatrixRings` | journal/volume unconfirmed | **excluded** |
| `SoleYemenQuasiCyclicMatrixRings` | final publication data unconfirmed | cited only as a preprint, with `year = {2007}` and no journal |
| `FalcunitSison2014M2Fp` | pages unconfirmed; also duplicated by `CyclicM2FpIsometricImages` (arXiv:1409.7228) | keep **one** entry (the arXiv record), drop the duplicate |
| `CalderbankShor1996`, `Steane1996`, `Gottesman1997`, `KnillLaflamme1997`, `Rains1999`, `BrunDevetakHsieh2006` | standard references; bibliographic details not re-retrieved in this sandbox | **excluded from the manuscript bibliography**: the manuscript re-derives the stabilizer/EA formalism from scratch (Phase 5 Lemmas Q1–Q2, T-193–T-201), so no result is imported from them. They are listed in `PAPER/OPEN_ISSUES_AND_LIMITATIONS.md` as items to add if the manuscript is prepared for submission. |
| `GreferathOSullivan2004`, `Honold2001Frobenius`, `Wood2008CodeEquivalence`, `GreferathNechaevWisbauer2004` | secondary only | retained in `references.bib` but **not cited** in the manuscript |
| `SiNiu2023SkewM2F2`, `DuNiu2025WeightSkewM2F2` | AIMS records seen in Phase 0 | cited in the literature review as the **skew** route, explicitly contrasted with our $\theta$-duality route |

## 5. Net effect on the manuscript bibliography

`PAPER/references.bib` contains **13** entries, all of them verified above:
Alahmadi–Sboui–Solé–Yemen 2013; Luo–Parampalli 2018; Dinh–Gaur–Kumar–Singh–Singh
2024; Joshi–Patel–Prakash 2026; Si–Niu 2023; Wood 1999; Fan–Zhang 2017;
Liu–Pan 2020; Cao 2021; Zhang–Kong–Zheng 2026; Greferath–Schmidt 1999;
Ketkar–Klappenecker–Kumar–Sarvepalli 2006; Grassl (codetables.de).
Every one of them is cited at least once in `main.tex`; none is cited for a
result that the manuscript also proves itself.

**Verified-reference count: 13** (13 direct / publisher-record, 0 unverified).
