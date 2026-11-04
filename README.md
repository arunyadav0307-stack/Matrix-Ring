# Quantum Error-Correcting Codes from Galois Hulls of Cyclic Codes over Noncommutative Matrix Rings

Working title. Research project executed under the controlling document
`00_BLUEPRINT/Research_Blueprint.pdf`.

**Current status: Phase 0 REVISED (Tasks 1-3 of the revision complete), pending
the independent audit. Phase 1 has NOT been started** (the blueprint forbids
starting a later phase before the current one is accepted).

Revision headline: the Galois pairing `<x,y>_s = sum_i theta_s(x_i) y_i`,
`theta_s = sigma_s o transpose`, is now **proved** (not merely proposed) to give a
perfect duality on right-ideal (cyclic) codes, for every `m`, `n`, `t`; and the
duality is **reflexive iff `r | 2s`**, so the recommended family is `q = p^{2e}`
with `s = r/2` (at `q = 8` there is no nontrivial reflexive choice: 35/737).

## Repository layout
```
00_BLUEPRINT/            controlling document (PDF) + text extract
01_LITERATURE/           annotated bibliography, BibTeX, comparison matrix
02_PHASE_REPORTS/        one folder per phase  -> Phase_0/ (report + 3 revision docs)
03_THEOREMS/             PAIRING_COMPLETE_PROOFS.md, UPDATED_THEOREM_REGISTER.md
                         (theorem_register.md retained as the original version)
04_COMPUTATION/          exact-arithmetic library, feasibility + Galois + A1
                         reconciliation experiments, logs
05_MANUSCRIPT/           (empty until Phase 8)
06_AUDIT/                audit requests for the independent referee (ChatGPT)
PROJECT_DECISION_LOG.md  dated decisions and their rationale
CHANGELOG.md             scope / notation / assumption changes + file tree
```

## Reading order for a newcomer (or for the auditor)
1. `02_PHASE_REPORTS/Phase_0/PHASE0_REVISION_REPORT.md` — master report for the
   revision (Tasks 1-3).
2. `02_PHASE_REPORTS/Phase_0/UPDATED_PHASE0_FINAL_RECOMMENDATION.md` — the
   current GO/MODIFY/STOP verdict (supersedes `Phase_0_Report.md` Sec. 8).
3. `02_PHASE_REPORTS/Phase_0/NONTRIVIAL_GALOIS_EXPERIMENTS.md` — Task 1 record.
4. `02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md` — Task 3 record.
5. `03_THEOREMS/PAIRING_COMPLETE_PROOFS.md` — Task 2: the complete proofs.
6. `03_THEOREMS/UPDATED_THEOREM_REGISTER.md` — what is claimed, and how strongly.
7. `04_COMPUTATION/UPDATED_COMPUTATION_SCRIPTS_AND_LOGS.md` — how to reproduce,
   and what the experiments do and do *not* prove.
8. `06_AUDIT/Phase0_audit_request.md` — the prompt to hand to ChatGPT.

## Standing rules (blueprint)
* One phase at a time; no phase is complete until the independent audit says so.
* Nothing is invented: no fabricated references, DOIs, theorems or numbers.
* Every claim is tagged established / proved / proved-conditional /
  conjectural / computational-only / open.
* `q = 2` data is enumerator validation only; it is never Galois evidence.
* `theta_s` is never called an involution without checking `r | 2s`.
* No claim is made that any published theorem (in particular
  Alahmadi-Sboui-Sole-Yemen 2013) is incorrect; discrepancies are reported as
  discrepancies.
