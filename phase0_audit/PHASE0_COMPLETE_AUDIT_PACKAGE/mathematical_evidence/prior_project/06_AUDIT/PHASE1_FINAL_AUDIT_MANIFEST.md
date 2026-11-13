# PHASE 1 — FINAL AUDIT PACKAGE (manifest)

**Package:** `PHASE1_FINAL_AUDIT_PACKAGE.zip`
**Built:** 2026-11-04 · **Branch:** `arena/59de606f-matrix-ring` · **Repository HEAD at build time:** `2e627b8045ace1e1f98ca4857a34ccecdaeec6f7`
**Contents:** the complete Phase-1 documentary, computational and decision record, the
supplementary left/right module conventions (§5.6 of the Phase-1 foundations document) and
the updated theorem register (rows T-030 … T-043).

> **Provenance note.** Both logs in this package were regenerated immediately before
> packaging and verified **byte-identical** to a second consecutive run of the same script
> from the same directory (deterministic: every probe is fixed or uniformly seeded).
> `ring_structure_log.txt` is additionally byte-identical to the copy committed at
> `2e627b8`.

---

## 1. Purpose

This bundle is the hand-off object for the **independent review** (ChatGPT) and for
**researcher approval**. It contains everything needed to re-run or re-check Phase 1
without access to the working session:

* the Phase-1 foundations document (all definitions, theorems and proofs);
* the Phase-0 pairing proofs on which §6 depends;
* the live theorem register (with the Phase-1 rows) and the original Phase-0 register;
* the two verification scripts and their logs;
* the approved Phase-0 decisions **B1**, **B2**, **B3** and the audit reports behind them;
* the project README, changelog and decision log.

## 2. Verification results contained in this package

| Script | Log | Result |
|---|---|---|
| `03_Computation/ring_structure_checks.py` | `03_Computation/ring_structure_log.txt` | RESULT: all 401 checks PASSED. |
| `03_Computation/module_actions_checks.py` | `03_Computation/module_actions_log.txt` | RESULT: all 276 checks PASSED. |

Both scripts build `F_q`, `A_t` and `M_2(A_t)` from scratch (no external library; nothing
imported from the earlier Phase-0 scripts). `module_actions_checks.py` additionally builds
`B = A_t[X]/⟨X^n−1⟩` and `M_2(B)` from scratch, importing only the arithmetic and the
`F_q`-linear algebra of `ring_structure_checks.py`. Every check is labelled `[EXH]`
(exhaustive over the finite object) or `[SMP]` (uniformly seeded sample, with the sample
size stated in the log).

## 3. What was re-verified in this final pass

1. **Definitions and notation** (§0 of the foundations document) — hypotheses, the four
   regimes R0–R3, and every symbol used later. No inconsistency found.
2. **Every theorem and proof** (§§1–7) — read line by line against the computational
   record. One genuine error was found and is recorded openly: the last clause of
   Remark 5.6 (see §4.4 below; register row T-042).
3. **Left/right module consistency** — the new §5.6 documents all four actions on `R`, the
   two actions on `R_n`, the coordinate formulas on `R^n`, the Morita dictionary in both
   handednesses and the five pairing/action identities (Lemma 5.6a); corroborated by the
   276 checks of `module_actions_checks.py`.
4. **Pairing compatibility** — Lemma 5.6a (five identities), Lemma 6.2 (sesquilinearity),
   Lemma 6.3 (key identity), Corollary 6.4 (the dual of a cyclic code is cyclic),
   Lemma 6.7 (the two orthogonals coincide), Theorem 6.8 (double dual), Lemma 6.11
   (isometry).
5. **Automorphism / anti-automorphism conditions** — `ord σ_s = r/gcd(r,s)`,
   `ord θ_s = 2r/gcd(r,2s)`, `θ_s^{2k} = σ_{2ks}`, `θ_s` involutive ⟺ `r ∣ 2s`.
6. **Morita correspondence** — the column convention is fixed (Convention 5.8); both
   handednesses verified; `dim I_W = 2 dim W`; cyclic-code counts
   `7 / 33 / 343 / 12 / 144 / 11 / 93 / 33` for
   `(q,t,n) = (4,1,1), (4,1,2), (4,1,3), (9,1,1), (9,1,2), (8,1,1), (8,1,2), (4,2,1)`
   (register row T-041).
7. **Consistency with the approved Phase-0 decisions** — **B1** (Alahmadi et al. cited for
   the framework only; their Theorem 1 is neither restated nor challenged; the discrepancy
   is preserved as a documented literature limitation), **B2** (narrowed four-part novelty;
   anti-automorphism duality is *not* claimed new), **B3** (hybrid Galois regime, with the
   warning B3.5 that a non-reflexive code may not enter a quantum construction without the
   hypothesis of Theorem 7.4). All three are respected verbatim in the Phase-1 document
   (§5.5, §7, §8) and in register rows T-029 and T-043.

## 4. Corrections made during Phase 1 (all recorded openly)

1. `b_s` is `σ_s`-**sesquilinear** over `F_q` (hence `F_p`-bilinear; `F_q`-bilinear only
   when `r ∣ s`) — Lemma 6.2(iii) was corrected from "`F_q`-bilinear".
2. Proposition 5.9 was restated: the plain matrix product degenerates on `E_11 R` while the
   entry-wise Frobenius form is perfect at `n = 1` (its failure is an `n ≥ 2` phenomenon,
   register row T-006).
3. A botched side-convention lemma was replaced by Lemma 5.5 plus the honest Remark 5.6.
4. **This pass:** the last clause of Remark 5.6 is **withdrawn**. It asserted that "the
   analogous closure fails in general" for a left module, whereas by the new Lemma 5.6b(2)
   the orthogonal of a left module *is* a left module (register row T-042). The premise —
   that `B_s(a·x,y)` is not in general a left multiple of `B_s(x,y)` — is correct, and a
   witness is printed in `03_Computation/module_actions_log.txt`.
5. **Script bug fixed during Phase 1:** `Field` built its `neg` and `sub` tables in one
   loop, so `sub[a][b]` used `neg[b] = 0` for unvisited `b`; this corrupted row reduction
   over `F_4, F_8, F_9`.

## 5. Unresolved mathematical issues (reported honestly)

* **T-006** — the failure of the entry-wise form is known only as an `n ≥ 2` phenomenon; it
  is **not** characterised (no criterion saying which codes fail).
* **T-027** — the framework is developed only for `τ = σ_s`. For a general
  `τ ∈ Aut(A_t)` one has `θ_τ² = τ²`, `(C^⊥)^⊥ = τ²(C)` and reflexivity ⟺ `τ² = id`, but
  the general case is undeveloped, and by T-030 `Aut(A_t) ⊋ {σ_s}`.
* **T-021** — principality of right ideals of `R_n` is proved only for `t = 1` with
  `X^n−1` squarefree; it is open for `t ≥ 2` or `p ∣ n`. No later phase may assume it.
* No hull-dimension **formula** (only distributions) — Phase 4.
* No Gray map / metric statements — Phase 5.
* No quantum construction — Phase 6; in regime R3 it may use only codes satisfying the
  proved hypothesis of Theorem 7.4 (warning B3.5).
* The cyclic-code enumeration is skipped (with a note in the log) when
  `dim_{F_q} B² > 6` or `|B²| > 20 000`, i.e. for `q = 9, n = 3` and `q = 4, t = 2,
  n = 2`; those two parameter sets are **not** covered by the counts of T-041.
* At `n = 1` the orthogonal of a **left** ideal is two-sided (Remark 5.6c), but for
  `n ≥ 2` no description of the orthogonal of a left submodule is known beyond
  Lemma 5.6b(2) (it is a subbimodule).

## 6. Contents and hashes

Every file below was hashed with SHA-256 at build time. To verify after unzipping:

```
unzip PHASE1_FINAL_AUDIT_PACKAGE.zip && cd PHASE1_FINAL_AUDIT_PACKAGE
awk -F'|' '/^\| `/ {gsub(/[` ]/,"",$2); gsub(/[` ]/,"",$5); print $5"  "$2}' 00_MANIFEST.md | sha256sum -c -
```

(On macOS/BSD replace `sha256sum` by `shasum -a 256`.) `00_MANIFEST.md` is the only file
not hashed — it is generated last, so it cannot contain its own digest.

| File in package | Source file in repository | Bytes | SHA-256 |
|---|---|---:|---|
| `01_Phase1_theorems/RING_AND_GALOIS_FOUNDATIONS.md` | `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` | 55,245 | `5a1a28a935142ebfc609ec2eeb468bd05e10079ef60b6779fbc6c3a409eacb75` |
| `01_Phase1_theorems/PAIRING_COMPLETE_PROOFS.md` | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` | 27,554 | `c276819999f103c7ef849693e4bb2d78a41928ec0ed6f81ef4c008e51f5d3f18` |
| `02_Theorem_register/UPDATED_THEOREM_REGISTER.md` | `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` | 32,017 | `2bac407e55c6275904b29e675da0af9b51d59d0abf353d8f458571d88f793700` |
| `02_Theorem_register/theorem_register.md` | `03_THEOREMS/theorem_register.md` | 6,662 | `6f749455b69a9d9cab9c8c6126e47290e02040b3421c251441c0f6a69257be38` |
| `03_Computation/ring_structure_checks.py` | `04_COMPUTATION/ring_structure_checks.py` | 49,367 | `5f74c8116b169945788e808518dcc4c938937f8d1a5245705f82e94dac500670` |
| `03_Computation/ring_structure_log.txt` | `04_COMPUTATION/ring_structure_log.txt` | 37,626 | `e4c9b9f1ebea1f34b620ab3714ece18d7a9007bb8449eace57c47cbe6d98bb1d` |
| `03_Computation/module_actions_checks.py` | `04_COMPUTATION/module_actions_checks.py` | 45,040 | `203ac53ba6b02c395d1563ddd696757d22d4a8ac2d4ec24f189e739d264fedf5` |
| `03_Computation/module_actions_log.txt` | `04_COMPUTATION/module_actions_log.txt` | 29,305 | `e3c30533be063380a0e3d1f311947adf57ec2e49179851b7f6722b40edcd64e4` |
| `03_Computation/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` | `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` | 8,089 | `f74e801a0fb2b189db9313958f6904c9ba9fbbcf6107bf9d58905ad40a01a421` |
| `03_Computation/README.md` | `04_COMPUTATION/README.md` | 4,649 | `19491d874607b69932a8da8d3cf5d5ac9c76a38b52cbbdb2ddb79bf22842ce51` |
| `04_Phase0_decisions/PHASE0_RESEARCHER_DECISION_SHEET.md` | `06_AUDIT/PHASE0_RESEARCHER_DECISION_SHEET.md` | 16,258 | `4b8f25bffddb47d2e8ed124464b13ae3c4adf54bb70b16db8009019991e55f50` |
| `04_Phase0_decisions/PHASE0_DECISION_FORM.md` | `06_AUDIT/PHASE0_DECISION_FORM.md` | 8,688 | `ad05e8a94ad41f116c894e0e7d0d97d9abaab59288f72c88086ea6046d23af12` |
| `04_Phase0_decisions/PHASE0_FINAL_GO_MODIFY_STOP.md` | `06_AUDIT/PHASE0_FINAL_GO_MODIFY_STOP.md` | 6,796 | `3304e5550fb6887378ae44553ecb7103c8508bea898217354aa3fba986b835ab` |
| `05_Phase0_audit/PHASE0_PROOF_VERIFICATION.md` | `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` | 14,762 | `e4f6f50a6f27a820ba5045909c3fb148f288173d83da3d2dee8af7f7eac65d6e` |
| `05_Phase0_audit/PHASE0_INDEPENDENT_AUDIT_REPORT.md` | `06_AUDIT/PHASE0_INDEPENDENT_AUDIT_REPORT.md` | 17,590 | `8a117426d03dd4c462cd1dc9cfd5ae57b03427b9b8abb575f80b8c38770b1501` |
| `05_Phase0_audit/PHASE0_NOVELTY_REASSESSMENT.md` | `06_AUDIT/PHASE0_NOVELTY_REASSESSMENT.md` | 11,061 | `3cc4e1f04791034e93a658b74e59d6455defeef6cc2eed00dbedcb2cd8ae277d` |
| `05_Phase0_audit/PHASE0_U8_U9_DECISIONS.md` | `06_AUDIT/PHASE0_U8_U9_DECISIONS.md` | 11,839 | `6139f84ca30651498e68872bd10492e210fe9ccaf96b42eb5bf39e1615ae641a` |
| `05_Phase0_audit/PHASE0_COMPUTATIONAL_AUDIT.md` | `06_AUDIT/PHASE0_COMPUTATIONAL_AUDIT.md` | 10,772 | `c678fa6647498e345f48b796dd28a0f4bf1c5dc1b3305ecfa64631d695d86043` |
| `05_Phase0_audit/PHASE0_PARAMETER_SELECTION_RECOMMENDATION.md` | `06_AUDIT/PHASE0_PARAMETER_SELECTION_RECOMMENDATION.md` | 12,030 | `4f120b8c15c39cac578a69e5600da1d03531d3d61dbcd5536665ab1a00fd1d4b` |
| `05_Phase0_audit/PHASE0_FINAL_NOVELTY_STATEMENT.md` | `06_AUDIT/PHASE0_FINAL_NOVELTY_STATEMENT.md` | 13,736 | `a5354a3c2ce440414d1ffbff6a9b0c20e674888d4d7a09b728bed79498b5154b` |
| `06_Supporting/README.md` | `README.md` | 3,086 | `6bb5320dfb5ad403888dafcb69392adec854d0434e5f783affc373c54a51c491` |
| `06_Supporting/CHANGELOG.md` | `CHANGELOG.md` | 10,051 | `ab3487b1f33eeaeaebc2d1d37dad91810493a91d495bd47fe919fef8ca9126c4` |
| `06_Supporting/PROJECT_DECISION_LOG.md` | `PROJECT_DECISION_LOG.md` | 7,178 | `ed0002595951184c2fb5e6ebfb94b06e858a7e5d8d6733c2b40bf60e193e80d4` |

**Total: 23 files, 439,401 bytes (uncompressed).**

## 7. Reproducing the computational record

```
cd 03_Computation
python3 ring_structure_checks.py     # -> ring_structure_log.txt   (401 checks, ~110 s)
python3 module_actions_checks.py     # -> module_actions_log.txt   (276 checks, ~85 s)
```

Python 3, standard library only, single core. `module_actions_checks.py` imports
`ring_structure_checks`, so the two files must sit in the same directory (as they do in
this package and in `04_COMPUTATION/`). Run them **from that directory**: each script
writes its log to the current working directory.

---

## 8. Archive verification (performed at build time)

| Check | Result |
|---|---|
| `zipfile.testzip()` (CRC of every entry) | **OK** |
| Entries in the archive | 24 (23 files + `00_MANIFEST.md`) |
| SHA-256 of every content file, recomputed **from inside the archive** and compared with the table in §6 | **23 / 23 match, 0 mismatch** |
| Archive size | 156,628 bytes |
| SHA-256 of `PHASE1_FINAL_AUDIT_PACKAGE.zip` | `84389a1a5023e40488f07dd0abe6b0787e3c779c1a3a1c30d71a048f53662c9c` |
| Log reproducibility | `ring_structure_log.txt` and `module_actions_checks` logs each byte-identical across two consecutive runs |

This copy of the manifest lives in `06_AUDIT/`; the copy inside the archive is identical
except that it omits this section (the archive digest does not exist until it is sealed).
