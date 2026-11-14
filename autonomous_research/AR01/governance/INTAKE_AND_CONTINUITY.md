# Intake, continuity and remote reconciliation

## Actual starting state

Branch `arena/7d88376d-matrix-ring`, local HEAD `12db091726835cc6f264fb0f679afc759610c89a`; 94 tracked files and **2,059 total repository files / 110,323,589 bytes**, excluding `.git`. The initial index and tracked diff were empty; `phase0_audit/` was an existing untracked user research tree. All its intake bytes are protected by `../evidence/INITIAL_PRESERVATION.json`. Tracking authorized originals is not modifying their scientific contents.

The previous external author guide is available and copied byte-exact into `history/PHASE1_AUTHOR_DECISION_GUIDE_prior.md`. The six standalone Phase-1 reports, three final HOLD source documents, exact mathematical supplement, later consolidated master and detailed RF follow-up files are **not physically available** at intake. Earlier conversation findings/hashes are historical context, not freshly verified files. No substitutes are presented as their originals.

## Remote history — do not force-push or overwrite an original

Read-only inspection and fetch of the **same designated branch** found existing remote HEAD `d2e7c70c5a2d2605f976d5c0e08a30510294e4f3`, descending from `168ec3e0b860cbe086ccb7a92a1a1aac5f8a277b` and the local base. Relative to the local base there are **1,394 additions**: 1,392 already present with identical bytes, one different existing PDF, and one absent blueprint PDF. The full per-file comparison is in `../evidence/REMOTE_INTAKE.json`.

An initial fast-forward preflight **stopped before staging/merge** when it found different bytes for:

`phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/literature_evidence/supplied_pdfs/s12190-018-01235-w (1).pdf`

- Intake local: 547,790 bytes, SHA-256 `410b6df35669b8d9f21fa0c5a2a3ae9e721306f2d1bf22474e1a983a4e43b52b`.
- Existing remote version: 414,858 bytes, SHA-256 `cf1af5654ff639a3195b18d1dab1c2d5dad0497994779a77aa24f63804f1f810`, blob `7227e2abc2b1956b04be9cf8ff6b814ea6ad8cfb`.

The intake original remains at its original path. The remote variant is copied into `../evidence/history/remote_s12190-018-01235-w.pdf` and also remains in immutable remote history. No inference is made about which variant is valid or why they differ; an old archive/seal cannot be certified from current intake preservation alone.

**Reconciliation procedure:** explicitly commit the intake research files plus the new work and the one recovered remote-only blueprint PDF. Then make an ancestry merge of the inspected remote commit using the preserved local snapshot tree (`git merge -s ours`), rather than check out different original bytes. This narrowly justified merge accounts for every remote path; it is not a general instruction to discard future incoming work. Both histories and both differing payloads survive. Push only the designated branch, without force, and verify its remote hash. Execution/receipt is recorded in `GIT_PROGRESS_LOG.md`.

## Blueprint recovery actually verified

The remote-only `NEW_RESEARCH_BLUEPRINT_REVIEW.pdf` was recovered from its Git blob, **382,351 bytes / 64 pages / SHA-256 f432b4cf10f939b1a82aa2b1782a36460dc65a76a54eb2c02e1431789787b16c**. Its 14 native embedded files comprise 13 sources plus a digest manifest. All 13 source hashes match; a parser-exposed identical crosswalk alias was stored once. See `../evidence/BLUEPRINT_RECOVERY.json` and `../evidence/reference_blueprint/`.

These exact blueprint attachments preserve the pending original decisions and 43-family/16-RF edge crosswalk, but not the missing detailed RF findings or standalone later reports. New delegated authority is recorded separately. No theorem/source gap is administratively closed by recovery.
