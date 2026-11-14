#!/usr/bin/env python3
"""Read-only comparison to the original intake file manifest."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "autonomous_research" / "AR01"


def main():
    initial = json.loads((RUN / "evidence" / "INITIAL_PRESERVATION.json").read_text())
    changed, missing = [], []
    for record in initial["files"]:
        path = ROOT / record["path"]
        if not path.is_file():
            missing.append(record["path"])
        elif path.stat().st_size != record["bytes"] or hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
            changed.append(record["path"])
    result = {"protected_files": len(initial["files"]),
              "protected_bytes": sum(x["bytes"] for x in initial["files"]),
              "changed_originals": changed, "missing_originals": missing,
              "scope": "Intake-byte preservation only; not historical seal/source/mathematical certification"}
    print(json.dumps(result, indent=2))
    if missing or changed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
