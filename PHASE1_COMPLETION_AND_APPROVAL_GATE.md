# PHASE 1 — COMPLETION AND APPROVAL GATE

**Status: PHASE 1 COMPLETE — AWAITING THE RESEARCHER'S EXPLICIT APPROVAL.**
No Phase-2 work has been started, and no Phase-1 file has been modified after the
final commit. This document is the handover record only; it introduces no new
mathematical claim.

---

## 1. Identity of the branch and the final commit

| Item | Value |
|---|---|
| Repository | `arunyadav0307-stack/Matrix-Ring` (`https://github.com/arunyadav0307-stack/Matrix-Ring.git`) |
| Branch (exact name) | `arena/59de606f-matrix-ring` |
| Final Phase-1 commit (short) | `238a174` |
| Final Phase-1 commit (full) | `238a174594a36b49d9e1d47dcbb69d0ca47af309` |
| Parent commit | `2e627b8045ace1e1f98ca4857a34ccecdaeec6f7` (push was a normal fast-forward — no force, no rewrite) |
| Commit date | 2026-11-04 |
| Files in the commit | 7 |
| Local `HEAD` vs remote tip | identical (`238a174…`); working tree clean |
| Commit subject | `Phase 1 final verification: left/right action conventions, register rows T-030..T-043, audit package` |

The branch head reported by the GitHub API is the same hash, so the remote and local
states agree.

---

## 2. Audit package — direct download

| Item | Value |
|---|---|
| File | `PHASE1_FINAL_AUDIT_PACKAGE.zip` (repository root) |
| **Direct download (pinned to the commit)** | `https://raw.githubusercontent.com/arunyadav0307-stack/Matrix-Ring/238a174594a36b49d9e1d47dcbb69d0ca47af309/PHASE1_FINAL_AUDIT_PACKAGE.zip` |
| **Direct download (branch head)** | `https://raw.githubusercontent.com/arunyadav0307-stack/Matrix-Ring/arena/59de606f-matrix-ring/PHASE1_FINAL_AUDIT_PACKAGE.zip` |
| Blob page (browser preview) | `https://github.com/arunyadav0307-stack/Matrix-Ring/blob/arena/59de606f-matrix-ring/PHASE1_FINAL_AUDIT_PACKAGE.zip` |
| Whole-repo archive at the commit | `https://github.com/arunyadav0307-stack/Matrix-Ring/archive/238a174594a36b49d9e1d47dcbb69d0ca47af309.zip` |

---

## 3. Size and SHA-256 of the ZIP

| Item | Value |
|---|---|
| Size | **156,628 bytes** (152.9 KiB) — confirmed both locally and by the GitHub API (`size: 156628`) |
| **SHA-256** | `84389a1a5023e40488f07dd0abe6b0787e3c779c1a3a1c30d71a048f53662c9c` |
| Git blob SHA-1 (GitHub) | `b59906de37f859ab08f02cde61c8693418cefafe` |
| Contents | 24 entries (23 files + `00_MANIFEST.md`) |
| Integrity checks performed | `zipfile.testzip()` CRC test **OK**; SHA-256 of every content file recomputed **from inside the archive** and compared with the manifest: **23 / 23 match, 0 mismatch** |

Verify locally after download:

```
sha256sum PHASE1_FINAL_AUDIT_PACKAGE.zip
# expect 84389a1a5023e40488f07dd0abe6b0787e3c779c1a3a1c30d71a048f53662c9c

unzip PHASE1_FINAL_AUDIT_PACKAGE.zip && cd PHASE1_FINAL_AUDIT_PACKAGE
awk -F'|' '/^\| `/ {gsub(/[` ]/,"",$2); gsub(/[` ]/,"",$5); print $5"  "$2}' 00_MANIFEST.md | sha256sum -c -
# expect 23 lines, all OK
```

The manifest is mirrored (with the archive-verification table appended) at
`06_AUDIT/PHASE1_FINAL_AUDIT_MANIFEST.md`.

---

## 4. Exact paths of the deliverables

| Deliverable | Path | Notes |
|---|---|---|
| **Main theorem document** | `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md` | 985 lines; §0 hypotheses/notation, §1 `A_t`, §2 `R = M_2(A_t)` + Morita, §3 `R_n ≅ M_2(B)`, §4 `σ_s`/`θ_s`, §5 module conventions, §6 the pairing, §7 regime-dependent statements, §8 non-claims, §9 computational corroboration |
| **Supplementary §5.6 (left/right actions)** | `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`, **lines 564–716** | §5.6.1 (l. 572) actions on `R` + Morita both handednesses; §5.6.2 (l. 597) actions on `R_n` and code coordinates; §5.6.3 (l. 617) Lemma 5.6a (five identities) and **Lemma 5.6b** (l. 617 ff.); §5.6.4 (l. 654) correction to Remark 5.6; §5.6.5 (l. 683) corroboration |
| **Theorem register (live)** | `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` | Phase-1 rows **T-030 … T-043** added in this pass (section "Rows added by Phase 1", from line 72) |
| Theorem register (original, audit trail) | `03_THEOREMS/theorem_register.md` | Phase-0-only version, kept unchanged |
| **Verification script 1** | `04_COMPUTATION/ring_structure_checks.py` | from-scratch `F_q`, `A_t`, `M_2(A_t)`; **401 / 401 checks PASS** |
| **Log 1** | `04_COMPUTATION/ring_structure_log.txt` | byte-identical to the copy committed at `2e627b8`; reproducible byte-for-byte |
| **Verification script 2 (new)** | `04_COMPUTATION/module_actions_checks.py` | `B = A_t[X]/⟨X^n−1⟩` and `M_2(B)` built from scratch; **276 / 276 checks PASS**; deterministic (two runs byte-identical) |
| **Log 2 (new)** | `04_COMPUTATION/module_actions_log.txt` | covers §5.6, incl. a brute-force cross-check of the orthogonal encoding |
| Package manifest | `06_AUDIT/PHASE1_FINAL_AUDIT_MANIFEST.md` | §8 records the archive-verification results |
| Earlier Phase-0 pairing proofs | `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` | dependency of §6; included in the package |

Run the scripts **from their own directory** (each writes its log to the current working
directory); `module_actions_checks.py` imports `ring_structure_checks`.

---

## 5. Unresolved issues and remaining limitations (recorded honestly)

| ID | Issue | Status |
|---|---|---|
| **T-006** | The **entry-wise (Frobenius) form** fails on right modules, but only as an `n ≥ 2` phenomenon; there is **no criterion** characterising which codes fail. The entry-wise form is used nowhere in the paper. | open, uncharacterised |
| **T-027** | The framework is developed **only for `τ = σ_s`**. For a general `τ ∈ Aut(A_t)`: `θ_τ = τ ∘ (·)^T`, `θ_τ² = τ²`, `(C^⊥)^⊥ = τ²(C)`, reflexivity ⟺ `τ² = id`. By T-030, `Aut(A_t) ⊋ {σ_s}` (`|Aut(A_t)| = r` at `t = 1`, `r(q−1)q^{t−2}` at `t ≥ 2`), so this is a genuine restriction. | open, undeveloped |
| **T-021** | **Principality** of right ideals of `R_n` is proved only for `t = 1` with `X^n−1` squarefree; open for `t ≥ 2` or `p ∣ n`. No later phase may assume "every cyclic code is principal". | open (conditional) |
| **T-011** | No hull-**dimension formula** — only the distributions recorded in Phase 0. | deferred to Phase 4 |
| **T-012** | No Gray map / no metric or distance statements. | deferred to Phase 5 |
| **T-013 / T-014** | No quantum construction, no parameter or defect analysis. | deferred to Phase 6 |
| **B3.5** | In regime R3 (`r ∤ 2s`) a quantum construction may use **only** codes satisfying the proved hypothesis of Theorem 7.4 (`σ_{2s}(C) = C`), or a derivation that avoids `C^{⊥⊥} = C` and the symmetry of the commutation form. | standing warning |
| Coverage gap | The `B`-submodule enumeration is skipped (noted in the log) when `dim_{F_q} B² > 6` or `|B²| > 20 000`: the parameter sets **`q = 9, n = 3`** and **`q = 4, t = 2, n = 2`** are **not** covered by the counts of T-041. | not covered |
| Structural gap | For `n ≥ 2` there is no description of the orthogonal of a left submodule beyond Lemma 5.6b(2) (it is a subbimodule). At `n = 1` it is two-sided (Remark 5.6c). | open |
| **B1** | Alahmadi–Sboui–Solé–Yemen (2013) is cited **for its framework only**; its Theorem 1 is **neither restated nor challenged**, and the discrepancy (35 vs 8 codes at `q = 2, n = 3`) is preserved as a documented literature limitation. | recorded, not resolved |
| **B2** | The novelty claim is narrowed (four parts); **anti-automorphism duality is not claimed new** (Wood 2010; Szabo–Wood 2017; NRS 2006). | recorded |

---

## 6. T-042 — WITHDRAWN CLAIM (not a theorem)

> **T-042 is recorded in the register as a WITHDRAWN claim (`needs correction`), not as a
> valid theorem. It must never be cited as a result.**

* **What was claimed** (last clause of Remark 5.6, `03_THEOREMS/RING_AND_GALOIS_FOUNDATIONS.md`):
  for a **left** module `C`, "replacing `x` by `a·x` gives `B_s(a·x,y) = Σ_e θ_s(x_e)θ_s(a)y_e`,
  which is not a left multiple of `B_s(x,y)`; the analogous closure therefore fails in general."
* **What is correct:** the **premise** — `B_s(a·x,y)` is not, in general, a left multiple of
  `B_s(x,y)`. A witness is printed in `04_COMPUTATION/module_actions_log.txt`
  (at `q = 4, t = 1, n = 1, s = 0`: `B_s(a·x,y) = [[3,0],[2,1]]` while
  `a·B_s(x,y) = [[2,3],[1,0]]`).
* **What is wrong:** the **conclusion**. The criterion used (factoring the multiplier out of
  `B_s`) is not the one that governs closure of an orthogonal. By **Lemma 5.6a(3)–(4)**,
  `B_s(a·x, y) = B_s(x, θ_s(a)·y)` and `B_s(x, a·y) = B_s(θ_s^{-1}(a)·x, y)`: the multiplier
  is *transferred to the other slot*, not extracted. Hence by **Lemma 5.6b(2)** the orthogonal
  of a left `R`-submodule **is** a left `R`-submodule (indeed a subbimodule), always.
* **Disposition:** the clause is **withdrawn** in §5.6.4, with a correction note inserted
  directly after Remark 5.6 pointing to §5.6.4. It is register row **T-042**, status
  `needs correction` (withdrawn, and **not** replaced by any left-module duality theory).
* **Blast radius:** none. Every statement in §§6–8 concerns right modules and rests on
  Lemma 6.2 / Corollary 6.4, which are untouched. The right-module convention itself
  (Definition 5.1, Convention 5.2) is unchanged, because only for right modules is the dual
  of a cyclic code again a cyclic code (Corollary 6.4).

---

## 7. What Phase 1 does and does not deliver

**Delivered (all with complete proofs in the repository, all corroborated computationally):**
the ring specification `A_t`, `R = M_2(A_t)` and `R_n ≅ M_2(B)`; the Morita dictionary
(column convention, both handednesses); the Galois datum `σ_s`, `θ_s` with orders and the
involution criterion `r ∣ 2s`; the module conventions (§5.6, Task-C clarification); the
validated pairing package (sesquilinearity, key identity, cyclicity of the dual,
non-degeneracy and the size formula, equality of the two orthogonals, the double-dual
formula `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`, reflexivity criterion, hull and isometry); the
regime-dependent statements (Theorems 7.1–7.4) and the exit gate (§6.8, satisfied under the
recorded regime restriction).

**Not delivered (by design):** hull-dimension formulas, Gray map / metric results, quantum
constructions, any novelty claim for anti-automorphism duality, any restatement of
Alahmadi et al.'s Theorem 1.

---

## 8. Approval gate

**Phase 1 is complete and frozen. The researcher's explicit approval is required before any
further phase begins.**

Requested sign-off (please reply explicitly with APPROVED or with the changes required):

1. Confirm the supplementary §5.6 (left/right module conventions) satisfies the Task-C
   clarification.
2. Confirm the withdrawal of the Remark 5.6 clause (T-042) and its replacement by
   Lemma 5.6b.
3. Confirm the unresolved issues in §5 above are correctly and completely recorded.
4. Authorise (or refuse) the hand-over to the independent review with the package at the
   URLs in §2.

| Role | Name | Decision | Date |
|---|---|---|---|
| Researcher | | ☐ Approved ☐ Approved with changes ☐ Not approved | |
| Independent reviewer (ChatGPT) | | ☐ Findings recorded | |

**On approval, the next step is the independent review; Phase 2 and the manuscript remain
un-started and must not begin without a further explicit instruction.**
