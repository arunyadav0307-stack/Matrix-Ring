# Phase 0 — Final decision: GO / MODIFY / STOP

**Decision: MODIFY, then GO to Phase 1. STOP here for researcher approval.**

No Phase 1 work has been started; `05_MANUSCRIPT/` is empty; no research direction has
been changed; all previous files and commit history are preserved; the push is a normal
fast-forward on `arena/59de606f-matrix-ring`.

---

## 1. Why not GO

Three things must change before the manuscript is written:

1. **F-01 / U8** — the recorded A1 theorem statement is inconsistent and cannot be
   restated. Either re-read A1 or adopt the "cite the framework only" position (§3.4 of
   `PHASE0_U8_U9_DECISIONS.md`).
2. **F-02** — the novelty claim is too strong: anti-automorphism duality over finite
   Frobenius rings is published (Wood 2010; Szabo–Wood 2017; NRS 2006). The introduction
   must be reworded and six references added.
3. **F-03 / F-04 / F-06** — concrete corrections: the t = 2 census is 33 not 32; T-018
   needs the squarefree hypothesis (counterexample `q=4,n=2`: 33, not 49); the
   self-orthogonality shortcut `G θ_s(G)^T = 0` is only valid when `r | 2s`.

## 2. Why not STOP

Nothing in the audit invalidates the programme. Specifically:

* the θ_s-duality, the size formula, the double-dual formula
  `(C^{⊥_s})^{⊥_s} = σ_{2s}(C)`, the reflexivity criterion `r | 2s`, the cyclicity of
  duals, and the hull theorems were re-derived from scratch and hold **as stated**
  (`PHASE0_PROOF_VERIFICATION.md`);
* the supplied scripts reproduce their logs byte-for-byte (only timestamps differ);
* an **independent implementation** (no shared code) confirms every prediction, 12.0 s,
  exit 0;
* a **second** verification on the supplied code paths over 6 961 (code, s) instances
  confirms the structural properties 100 %, including the decisive pair
  "double-dual 737/737 at q = 8" versus "reflexive 35/737 at q = 8";
* the enumerator is now confirmed structurally (CRT + Morita predicts the exact dimension
  distribution of the 35 codes at `q=2,n=3`, matched);
* the t = 2 count is now explained by a formula `q² + 3q + 5 = 33` reached independently
  of any code.

The defects found are local and corrected; the foundation is sound.

---

## 3. The MODIFY list (exactly what to change)

| # | Item | Where | Owner |
|---|------|-------|-------|
| M1 | A1 theorem (U8): adopt the recommended position or re-read the source | manuscript §5 (reconciliation section) | **researcher decision** |
| M2 | Novelty paragraph downgraded; add Wood 2010, Szabo–Wood 2017, NRS 2006, Dougherty–Leroy 2016, Solé MMS 2011, Kushwaha–Prakash 2025/26 | manuscript §1 + bibliography | **researcher decision** |
| M3 | Quantum sections to be proved in the **reflexive** regime (`s ≡ 0` or `r` even with `s = r/2`); general-`s` results as companions; no `C^{⊥⊥}` shortcuts elsewhere | manuscript §7 | **researcher decision** |
| M4 | `32 → 33` and the corrected dimension distribution `[(0,1),(2,5),(4,21),(6,5),(8,1)]` in the three Phase-0 revision reports | `02_PHASE_REPORTS/` | agent (Phase 1) |
| M5 | T-018: add `gcd(n,p) = 1` (squarefree) + the `q=4,n=2` counterexample | register (done in this audit) + manuscript §5.2 | agent |
| M6 | T-017: make `m ≥ 2` prominent and note `m = 1` is always reflexive | register (done) | agent |
| M7 | Add the new lemmas (key identity, σ_{2s}-isometry E1–E5, non-squarefree counterexample, t = 2 count `q²+3q+5`) | register (done) + manuscript §3 | agent |
| M8 | Distinguish our form `Σ θ_s(x_e) y_e` from A1's `Σ x_j y_j` wherever A1 is mentioned | manuscript §5, §3 | agent |
| M9 | State `r ≥ 2` as a standing hypothesis (at `r = 1` the Galois action is trivial) | manuscript §1–§2 | agent |

---

## 4. Blockers (must be resolved before the corresponding section is written)

| Blocker | Blocks | Resolution needed |
|---|---|---|
| **B1 — U8 / A1** | manuscript §5 | researcher: (a) re-read A1, or (b) authorise "framework-only citation" |
| **B2 — novelty wording** | manuscript §1 | researcher: accept the §6 wording of `PHASE0_NOVELTY_REASSESSMENT.md` |
| **B3 — reflexive vs general regime** | manuscript §7 | researcher: confirm the §5 recommendation of `PHASE0_U8_U9_DECISIONS.md` |

## 5. Non-blocking open items (carry into Phase 1)

| Item | Note |
|---|---|
| T-021 principality at `t ≥ 2` or `p ∣ n` | still open; nothing may use it |
| T-011 hull-dimension formulas for meaningful families | open (Phase 4); distributions recorded |
| T-012 Gray/Bachoc map with a duality relation | open (Phase 5); **highest technical risk** |
| T-013 / T-014 quantum constructions and bounds | open (Phase 6); depends on B3 |
| Szabo–Wood hypotheses for non-involutive anti-automorphisms (F-13) | needed before claiming MacWilliams in the non-reflexive regime |
| `m = 3`, `t = 3` experiments | cheap, high value; not yet run |
| q = 8 with even `n` | blocked by the enumerator (needs `X^n−1` squarefree ⇒ `n` odd in char 2) |
| `q = 9, n = 4` census | sampled (5 000) — always label `[SMP]` |

---

## 6. Suggested Phase 1 order (for approval, not to be started now)

1. Apply M1–M3 (decisions) and M4–M9 (mechanical).
2. §2 preliminaries (rings, σ_s, θ_s, the key identity, the isometry lemma).
3. §3 duality: size formula, double dual, reflexivity, cyclicity, hulls — with the
   `r | 2s` hypothesis on every symmetry-dependent statement.
4. §4 hulls and the censuses (with the corrected 33 and the squarefree counterexample).
5. §5 the M_2(F_2) census and the (I)/(II) convention remark; A1 cited per B1.
6. §6–§7 quantum: **only** in the reflexive regime (B3), pending T-012.

---

## 7. Audit artefacts delivered

| File | Content |
|---|---|
| `06_AUDIT/PHASE0_INDEPENDENT_AUDIT_REPORT.md` | executive summary, findings F-01…F-13, blockers |
| `06_AUDIT/PHASE0_PROOF_VERIFICATION.md` | item-by-item re-derivation and verdicts |
| `06_AUDIT/PHASE0_COMPUTATIONAL_AUDIT.md` | independent implementation, supplied-script audit, the 32→33 bug, what is still unverified |
| `06_AUDIT/PHASE0_U8_U9_DECISIONS.md` | U8 and U9, with data and recommendations |
| `06_AUDIT/PHASE0_NOVELTY_REASSESSMENT.md` | prior art, defensible claim, bibliography additions |
| `06_AUDIT/PHASE0_FINAL_GO_MODIFY_STOP.md` | this file |
| `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` | re-issued register with the audit outcomes |
| `04_COMPUTATION/independent_audit_checks.py` + log | independent implementation |
| `04_COMPUTATION/audit_pairing_equivalence.py` + log | duality/isometry verification on supplied code paths |
| `04_COMPUTATION/u8_n3_selfdual_check.py` + log | U8 probe at `n = 3`, `A = M_2(F_2)` |
| `04_COMPUTATION/galois_t2_check.py` | patched: zero submodule restored (32 → 33) |

**End of audit. Stopping for researcher approval.**
