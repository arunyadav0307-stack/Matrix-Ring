# Counterexamples and failed approaches: source index

This is an index of existing artifacts, not a new proof or implementation. Consult the complete derivations and their stated left/right conventions; source-level labels are not independently certified by packaging.

| Issue reported in Phase 0 | Included source evidence |
|---|---|
| Plain product and one-sided-module size-law failure | `prior_project/03_THEOREMS/PAIRING_COMPLETE_PROOFS.md`, section 5; `../computational_evidence/research-data/scripts/phase0_feasibility.py`; its recorded log and the existing current-Phase-0 rerun in `../computational_evidence/current_phase0/` (E4) |
| Non-reflexive Galois regime / double-dual orientation | Complete pairing proofs, sections 3.6–3.9; `prior_project/06_AUDIT/PHASE0_PROOF_VERIFICATION.md`; `galois_duality_experiments.py`, `independent_audit_checks.py`, and their historical logs in the research-data tree |
| Squarefree-factorization and generator/principality assumptions | `prior_project/02_PHASE_REPORTS/Phase_0/ALAHMADI_THEOREM_RECONCILIATION.md`; Stage 2A/2B/2C sources; reconciliation and CRT scripts/logs |
| Non-principal hull examples | Stage 3B hull-enumeration proof source and log; `../computational_evidence/research-data/quantum_code_records/nonprincipal_witnesses.csv` |
| Gray expansion is not automatically Euclidean-compatible or a ring-Hamming isometry | `prior_project/03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md`, sections 0.3, 2 and 3; `../computational_evidence/research-data/logs/phase4_gray_map_log.txt` |
| Candidate approaches rejected only for scope/novelty, versus mathematical failure | Mandatory `../reports/PHASE0_PAIRING_OPTIONS.md` and `PHASE0_RESEARCH_GAP.md`; inherited novelty audit. Do not conflate a scope rejection with an invalid mathematical construction. |

The summary in `../reports/PHASE0_PAIRING_OPTIONS.md` uses `ax` in one semilinearity formula, whereas the complete source proof Proposition 2.1(3) uses the right action `x a`. Both are preserved without modification so the independent reviewer can check the side convention. This package does not repair or certify the reports' shorthand, candidate equivalences, or theorems.
