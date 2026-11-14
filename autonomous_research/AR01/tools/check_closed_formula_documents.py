#!/usr/bin/env python3
"""Document/range/hash and exact N2 assembly checks; NOT a proof assistant."""
from pathlib import Path
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
RUN = ROOT / "autonomous_research/AR01"
FILES = ["phase3/CORE_A_CLOSED_FORMULA_THEOREM.md", "phase3/CORE_A_CLOSED_FORMULA_FULL_PROOF.md",
         "audits/CORE_A_INDEPENDENT_PROOF_AUDIT.md", "audits/CORE_A_EXCEPTIONAL_CASES_REGISTER.md",
         "audits/CORE_A_THEORY_COMPUTATION_COMPARISON.md", "audits/CORE_A_PROOF_STATUS_REPORT.md"]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


class P:
    def __init__(self, d):
        self.d = {k: v for k, v in d.items() if v}

    @staticmethod
    def cast(a):
        return a if isinstance(a, P) else P({(0,) * 5: a})

    def __add__(self, other):
        d = dict(self.d)
        for key, value in P.cast(other).d.items():
            d[key] = d.get(key, 0) + value
        return P(d)
    __radd__ = __add__

    def __neg__(self):
        return P({k: -v for k, v in self.d.items()})

    def __sub__(self, other):
        return self + (-P.cast(other))

    def __rsub__(self, other):
        return P.cast(other) + (-self)

    def __mul__(self, other):
        d = {}
        for a, x in self.d.items():
            for b, y in P.cast(other).d.items():
                key = tuple(i + j for i, j in zip(a, b))
                d[key] = d.get(key, 0) + x * y
        return P(d)
    __rmul__ = __mul__

    def __pow__(self, n):
        answer = P.cast(1)
        for _ in range(n):
            answer = answer * self
        return answer


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    destination = RUN / "evidence" / (label + ".json")
    assert not destination.exists(), "Refusing to overwrite a check receipt"
    proof = RUN / FILES[1]
    lines = proof.read_text().splitlines()
    starts = [(i + 1, m.group(1)) for i, line in enumerate(lines)
              if (m := re.match(r"### (P\d\d)\.", line))]
    assert [s[1] for s in starts] == [f"P{i:02}" for i in range(1, 31)]
    expected = [(unit, start, starts[i + 1][0] - 1 if i + 1 < len(starts) else len(lines))
                for i, (start, unit) in enumerate(starts)]
    audit = (RUN / FILES[2]).read_text()
    recorded = [("P" + unit, int(start), int(end)) for unit, start, end in re.findall(r"\|P(\d\d),(\d+)–(\d+)\|", audit)]
    assert recorded == expected
    assert digest(proof) in audit and digest(RUN / FILES[0]) in audit
    links = 0
    for name in FILES:
        p = RUN / name
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", p.read_text()):
            if "://" not in target and not target.startswith("#"):
                assert (p.parent / target.split("#")[0]).is_file(), (name, target)
                links += 1
    q, Q, d, U, F = [P({tuple(int(i == j) for i in range(5)): 1}) for j in range(5)]
    a = (q + 1) * (2 * q**2 + q + 1)
    G = q**4 + 3 * q**3 + 4 * q**2 + 3 * q + 5
    L = 2 * q**4 + 8 * q**3 + 10 * q**2 + 7 * q + 9
    n0 = (q + 1 - d) * q**3 + 2
    n1 = 2 * a + d * (q**3 - 2 * q**2 - Q**2 * (q - Q)) + (q + 3) * U - F
    n2 = G + d * (2 * q**2 + Q**2 * (q - Q) - 1) - (q + 3) * U + F
    assert not (n0 + n1 + n2 + d - L).d
    result = {"status": "PASS", "all_six_required_documents_exist": True,
              "documents": {name: {"sha256": digest(RUN / name), "lines": len((RUN / name).read_text().splitlines())} for name in FILES},
              "proof_units_and_exact_audit_line_ranges": expected, "local_document_links_checked": links,
              "exact_five_variable_N2_assembly_identity": True,
              "checker_sha256": digest(Path(__file__).resolve()),
              "scope": "Textual/range/link/hash consistency and exact polynomial identity only, not automated logical proof or human review"}
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must be enabled")
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh check label")
    main(sys.argv[1])
