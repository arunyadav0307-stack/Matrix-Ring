#!/usr/bin/env python3
"""Verify this fixed branch and every Git blob/mode; optionally save a fresh receipt.

Usage: python3 -B .../verify_remote_checkpoint.py RECEIPT_LABEL BASE_COMMIT
       python3 -B .../verify_remote_checkpoint.py --print-only BASE_COMMIT
The BASE_COMMIT identifies the reviewed expected changed files; it never moves HEAD.
Raw clock observations are not normalized session or publication dates.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "autonomous_research/AR01"
BRANCH = "arena/7d88376d-matrix-ring"
REPOSITORY = "arunyadav0307-stack/Matrix-Ring"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main(label, base):
    assert git("branch", "--show-current").decode().strip() == BRANCH
    head = git("rev-parse", "HEAD").decode().strip()
    base = git("rev-parse", "--verify", base + "^{commit}").decode().strip()
    subprocess.run(["git", "merge-base", "--is-ancestor", base, head], cwd=ROOT, check=True)
    if label != "--print-only":
        assert label and all(c.isalnum() or c in "_-" for c in label)
        destination = RUN / "evidence" / (label + ".json")
        assert not destination.exists(), "Refusing to overwrite a prior receipt"
    ref = "refs/heads/" + BRANCH
    before = git("ls-remote", "origin", ref).decode().strip().split()
    assert before == [head, ref], ("Remote ref mismatch", before, head)
    local = {}
    for record in git("ls-tree", "-r", "--full-tree", "-z", head).split(b"\0"):
        if not record:
            continue
        meta, name = record.split(b"\t", 1)
        mode, kind, oid = meta.decode().split()
        assert kind == "blob", ("Non-blob needs a separately specified comparison", name)
        local[name.decode()] = (oid, mode)
    raw = subprocess.check_output(["gh", "api", "repos/" + REPOSITORY + "/git/trees/" + head + "?recursive=1"], cwd=ROOT)
    response = json.loads(raw)
    assert response.get("truncated") is False, "Truncated GitHub tree"
    remote = {entry["path"]: (entry["sha"], entry["mode"])
              for entry in response["tree"] if entry["type"] == "blob"}
    assert local == remote, "Remote blob/path/mode tree mismatch"
    expected = [p.decode() for p in git("diff", "--name-only", "--diff-filter=ACMRT", "-z", base, head).split(b"\0") if p]
    assert expected and all(path in remote for path in expected)
    deleted = [p.decode() for p in git("diff", "--name-only", "--diff-filter=D", "-z", base, head).split(b"\0") if p]
    assert not deleted, "This preservation milestone must not delete prior tracked files"
    assert git("rev-parse", "HEAD").decode().strip() == head
    after = git("ls-remote", "origin", ref).decode().strip().split()
    assert after == [head, ref], ("Remote moved during verification", after)
    result = {
        "status": "PASS", "raw_environment_observed_at_utc": datetime.now(timezone.utc).isoformat(),
        "timestamp_kind": "Raw sandbox clock observation, not normalized session calendar or publication date",
        "repository": REPOSITORY, "branch": BRANCH, "verified_commit": head,
        "expected_paths_base_commit": base, "verified_blob_count": len(local),
        "all_remote_local_blob_paths_oids_and_modes_equal": True,
        "remote_ref_matched_before_and_after_tree_check": True,
        "github_tree_response_sha256": hashlib.sha256(raw).hexdigest(),
        "expected_changed_paths_verified": {p: {"git_blob_sha": local[p][0], "mode": local[p][1]} for p in sorted(expected)},
        "expected_changed_path_count": len(expected), "deleted_tracked_paths": deleted,
        "working_tree_status_before_receipt": git("status", "--porcelain=v1").decode().splitlines(),
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Git synchronization and expected file identity only; not scientific truth, novelty or external review"
    }
    if label != "--print-only":
        destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must be enabled")
    if len(sys.argv) != 3:
        raise SystemExit("Supply a fresh receipt label (or --print-only) and a reviewed base commit")
    main(sys.argv[1], sys.argv[2])
