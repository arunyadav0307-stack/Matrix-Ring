#!/usr/bin/env python3
"""Read-only Phase 0 package verification; standard library only; no research code executes."""
from __future__ import annotations

import ast
import csv
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

ROOT_NAME = "PHASE0_COMPLETE_AUDIT_PACKAGE"
REPORTS = (
    "PHASE0_REPOSITORY_AUDIT.md",
    "PHASE0_LITERATURE_REVIEW.md",
    "PHASE0_RING_FEASIBILITY.md",
    "PHASE0_PAIRING_OPTIONS.md",
    "PHASE0_RESEARCH_GAP.md",
    "PHASE0_DECISION_REPORT.md",
)


def verify(root: Path) -> dict:
    root = root.resolve()
    paths = sorted(p for p in root.rglob("*") if p.is_file())
    errors = []
    if any(p.is_symlink() for p in root.rglob("*")):
        errors.append("Symlinks are not permitted in the package.")
    for name in REPORTS:
        if not (root / "reports" / name).is_file():
            errors.append("Missing report: " + name)
    manifest = root / "SHA256SUMS.txt"
    expected = {}
    if not manifest.is_file():
        errors.append("Missing SHA256SUMS.txt")
    else:
        for line in manifest.read_text(encoding="utf-8").splitlines():
            m = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
            if not m:
                errors.append("Unparseable checksum line: " + line)
                continue
            digest, name = m.groups()
            pure = PurePosixPath(name)
            if pure.is_absolute() or ".." in pure.parts or name in expected:
                errors.append("Unsafe or repeated checksum path: " + name)
                continue
            expected[name] = digest
            target = root / name
            if not target.is_file():
                errors.append("Missing checksummed file: " + name)
            elif hashlib.sha256(target.read_bytes()).hexdigest() != digest:
                errors.append("Checksum mismatch: " + name)
    actual = {p.relative_to(root).as_posix() for p in paths}
    if actual != set(expected) | {"SHA256SUMS.txt"}:
        errors.append("Actual file set does not equal SHA256SUMS.txt plus the manifest itself.")

    provenance_rows = 0
    provenance_file = root / "repository_integrity/source_provenance.csv"
    with provenance_file.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            provenance_rows += 1
            p = root / row["package_path"]
            if not p.is_file():
                errors.append("Missing provenance target: " + row["package_path"])
            elif (len(p.read_bytes()) != int(row["bytes"]) or
                  hashlib.sha256(p.read_bytes()).hexdigest() != row["sha256"]):
                errors.append("Provenance mismatch: " + row["package_path"])

    references_checked = 0
    inherited_exceptions = {}
    with (root / "repository_integrity/reference_resolution.csv").open(
            encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            targets = json.loads(row["package_targets_json"])
            for target in targets:
                references_checked += 1
                if not (root / target).is_file():
                    errors.append("Reference resolution target absent: " + target)
            if row["status"] not in ("PACKAGED", "PACKAGED_ALIAS", "PACKAGED_MULTIPLE"):
                inherited_exceptions[row["status"]] = inherited_exceptions.get(row["status"], 0) + 1

    data_root = root / "computational_evidence/research-data"
    publication_entries = 0
    for line in (data_root / "PUBLICATION_MANIFEST.sha256").read_text().splitlines():
        digest, name = line.split("  ", 1)
        publication_entries += 1
        p = data_root / name
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != digest:
            errors.append("Publication manifest failure: " + name)

    scripts = sorted((data_root / "scripts").glob("*.py"))
    local_names = {p.stem for p in scripts}
    local_import_edges = 0
    for p in scripts:
        try:
            tree = ast.parse(p.read_text(encoding="utf-8"), filename=str(p))
        except SyntaxError as exc:
            errors.append("Script syntax error: " + str(exc))
            continue
        for node in ast.walk(tree):
            names = ([node.module] if isinstance(node, ast.ImportFrom) and node.module
                     else [a.name for a in node.names] if isinstance(node, ast.Import) else [])
            for name in names:
                if name.split(".")[0] in local_names:
                    local_import_edges += 1
                    if not (data_root / "scripts" / (name.split(".")[0] + ".py")).is_file():
                        errors.append("Missing local script dependency: " + name)

    result = {
        "status": "PASS" if not errors else "FAIL",
        "required_reports_present": sum((root / "reports" / n).is_file() for n in REPORTS),
        "regular_file_count_including_SHA256SUMS": len(paths),
        "uncompressed_bytes": sum(p.stat().st_size for p in paths),
        "sha256_manifest_entries": len(expected),
        "source_provenance_rows_checked": provenance_rows,
        "reference_targets_checked": references_checked,
        "inherited_reference_exceptions_by_status": inherited_exceptions,
        "publication_manifest_entries_verified": publication_entries,
        "research_scripts_parsed_not_executed": len(scripts),
        "local_import_edges_present": local_import_edges,
        "errors": errors,
        "scope": "File/structure/checksum verification only; not a mathematical or novelty certification.",
    }
    return result


def main() -> int:
    if len(sys.argv) > 1 and Path(sys.argv[1]).suffix.lower() == ".zip":
        archive = Path(sys.argv[1]).resolve()
        errors = []
        with zipfile.ZipFile(archive) as z:
            infos = z.infolist()
            names = [i.filename for i in infos]
            bad = z.testzip()
            if bad:
                errors.append("CRC failure: " + bad)
            if len(names) != len(set(names)):
                errors.append("Duplicate ZIP entries")
            for name in names:
                parts = PurePosixPath(name).parts
                if not parts or parts[0] != ROOT_NAME or ".." in parts or name.startswith("/"):
                    errors.append("Unsafe/wrong-root ZIP path: " + name)
            prefix = ROOT_NAME + "/"
            checksum_text = z.read(prefix + "SHA256SUMS.txt").decode("utf-8")
            manifest_paths = set()
            for line in checksum_text.splitlines():
                digest, name = line.split("  ", 1)
                manifest_paths.add(prefix + name)
                if hashlib.sha256(z.read(prefix + name)).hexdigest() != digest:
                    errors.append("ZIP SHA-256 mismatch: " + name)
            files = {i.filename for i in infos if not i.is_dir()}
            if files != manifest_paths | {prefix + "SHA256SUMS.txt"}:
                errors.append("ZIP file set does not match SHA-256 manifest")
            for name in REPORTS:
                if prefix + "reports/" + name not in files:
                    errors.append("Missing report in ZIP: " + name)
            result = {
                "status": "PASS" if not errors else "FAIL",
                "zip_regular_file_count": len(files),
                "zip_bytes": archive.stat().st_size,
                "zip_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                "uncompressed_bytes": sum(i.file_size for i in infos if not i.is_dir()),
                "CRC_integrity": "PASS" if bad is None else "FAIL",
                "sha256_manifest_entries": len(manifest_paths),
                "errors": errors,
                "scope": "File integrity only; no research computations execute.",
            }
    else:
        root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2]
        result = verify(root)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
