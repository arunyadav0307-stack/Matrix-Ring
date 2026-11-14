# Computational evidence and reproducibility status

- `current_phase0/`: the already-existing 2026-11-12 run of **the same** prior Phase 0 feasibility script and its recorded diff. `RERUN_COMPARISON.json` verifies the 3 differing metadata/timing/path lines; it does not claim a mathematically independent implementation.
- `research-data/`: the complete original reproducibility unit (88 regular files including its two manifests). It contains 22 scripts, 23 logs, 29 JSON files, 8 CSV tables, 4 Markdown files, and 2 `.sha256` files. No file in it is newly authored or executed by this packaging task.
- `prior_project/`: distinct historical documentation and certification-method notes. Duplicate historical scripts/logs are stored only once in `research-data/`; their aliases are in `../repository_integrity/source_provenance.csv`.
- `SCRIPT_DEPENDENCIES.csv`: static syntax and local-import checks only, no execution.

## Gray-map results
The historical `research-data/logs/phase4_gray_map_log.txt` ends with 463 checks / 463 PASS / 0 FAIL, distinguishes EXH from SMP, and records the transported Hankel/reversal Gram matrix. Its script and complete mathematical source are included. It was **not re-run** during this packaging task; preservation and checksum verification are not fresh computational or mathematical certification. The report's broad wording about hundreds of checks being rerun should be read alongside this narrower actual-run evidence.

## Safe reproduction by an independent reviewer
Some historical scripts write log files next to their own source, and some have expensive/exhaustive modes. Do not run them directly in the sealed package or the original repository. First copy `research-data/` to a separate disposable working directory, inspect each script's entry point and the included environment/certification procedures, then run the desired historical check there with `PYTHONDONTWRITEBYTECODE=1`. Full extended searches are not implied by package verification.

Directly checking the active source-data manifest is read-only:

```sh
cd research-data
sha256sum -c PUBLICATION_MANIFEST.sha256
```

`documentation/MANIFEST.sha256` describes an older flat layout. Its entries were checked through an explicit relocation map in `../repository_integrity/inherited_manifest_verification.csv`; do not interpret its old paths as newly missing research data.
