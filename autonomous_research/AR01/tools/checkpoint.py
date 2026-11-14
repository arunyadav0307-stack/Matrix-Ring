#!/usr/bin/env python3
"""Create a bounded, deterministic checkpoint, not a submission release.

Run from any directory: python3 -B .../checkpoint.py M1_INTAKE
A checkpoint never overwrites another checkpoint and never includes backups.
"""
from pathlib import Path
import hashlib
import json
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "autonomous_research" / "AR01"
LOGS = ["GIT_PROGRESS_LOG.md", "RESEARCH_PROGRESS_LOG.md",
        "PHASE_COMPLETION_REGISTER.md", "FINAL_CHANGELOG.md"]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    if len(sys.argv) != 2 or not all(c.isalnum() or c in "_-" for c in sys.argv[1]):
        raise SystemExit("Supply a new alphanumeric checkpoint label")
    destination = RUN / "backups" / ("AR01_" + sys.argv[1] + ".zip")
    if destination.exists():
        raise SystemExit("Refusing to overwrite an existing checkpoint")
    paths = sorted(p for p in RUN.rglob("*") if p.is_file()
                   and "backups" not in p.relative_to(RUN).parts
                   and "__pycache__" not in p.parts)
    paths += [ROOT / n for n in LOGS]
    paths += [ROOT / ".gitignore"]
    payloads = {str(p.relative_to(ROOT)): p.read_bytes() for p in paths}
    manifest = "".join(f"{digest(data)}  {name}\n" for name, data in sorted(payloads.items()))
    payloads["CHECKPOINT_MANIFEST.sha256"] = manifest.encode()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(payloads.items()):
            info = zipfile.ZipInfo(name)  # Explicit reproducibility epoch: 1980-01-01.
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(payloads)
        for name, data in payloads.items():
            assert archive.read(name) == data
    record = {"archive": str(destination.relative_to(ROOT)),
              "bytes": destination.stat().st_size,
              "sha256": digest(destination.read_bytes()),
              "payload_files": len(paths), "zip_entries": len(payloads),
              "all_entries_reopened_byte_identical": True,
              "scope": "AR01 working deliverables plus four root logs and .gitignore; excludes backups and all other original research trees",
              "zip_timestamp": "Fixed technical reproducibility epoch, not claimed execution date",
              "submission_package": False}
    destination.with_suffix(".zip.sha256").write_text(record["sha256"] + "  " + destination.name + "\n")
    destination.with_suffix(".verification.json").write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()
