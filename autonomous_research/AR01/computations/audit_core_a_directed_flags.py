#!/usr/bin/env python3
"""M8 standalone directed-flag stress test, not independent human proof review.

Imports no other repository code. Counts actual right-radical flags over
q=4,8,16 and compares raw, freshly rerun geometry/census data. Field products
use integer-polynomial long multiplication and long division; linear algebra
is implemented here. This adds implementation separation, not an external
reviewer, a formal proof, or a new full B^2-module/global census.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import hashlib
import json
import sys
import traceback

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def add(x, y):
    return tuple(a ^ b for a, b in zip(x, y))


class BinaryField:
    def __init__(self, degree):
        self.m = degree
        self.q = 2**degree
        polynomial = {2: 0b111, 3: 0b1011, 4: 0b10011}[degree]

        def multiply(a, b):
            raw = 0
            for bit in range(degree):
                if (b >> bit) & 1:
                    raw ^= a << bit
            while raw.bit_length() > degree:
                raw ^= polynomial << (raw.bit_length() - degree - 1)
            return raw

        self.times = tuple(tuple(multiply(a, b) for b in range(self.q))
                           for a in range(self.q))
        self.inv = [0] + [next(b for b in range(1, self.q) if self.times[a][b] == 1)
                          for a in range(1, self.q)]
        self.frobs = []
        for s in range(degree):
            row = []
            for a in range(self.q):
                for _ in range(s):
                    a = self.times[a][a]
                row.append(a)
            self.frobs.append(tuple(row))
        for a, b, c in product(range(self.q), repeat=3):
            assert self.times[a][b ^ c] == (self.times[a][b] ^ self.times[a][c])
            assert self.times[self.times[a][b]][c] == self.times[a][self.times[b][c]]
        assert all(self.times[a][b] == self.times[b][a]
                   for a in range(self.q) for b in range(self.q))

    def scale(self, a, v):
        return tuple(self.times[a][b] for b in v)

    def rref(self, rows, width):
        matrix = [tuple(row) for row in rows if any(row)]
        assert all(len(row) == width for row in matrix)
        pivot = 0
        for col in range(width):
            selected = next((i for i in range(pivot, len(matrix)) if matrix[i][col]), None)
            if selected is None:
                continue
            matrix[pivot], matrix[selected] = matrix[selected], matrix[pivot]
            matrix[pivot] = self.scale(self.inv[matrix[pivot][col]], matrix[pivot])
            for i in range(len(matrix)):
                if i != pivot and matrix[i][col]:
                    matrix[i] = add(matrix[i], self.scale(matrix[i][col], matrix[pivot]))
            pivot += 1
        return tuple(matrix[:pivot])

    def kernel(self, rows, width):
        reduced = self.rref(rows, width)
        pivots = [next(i for i, x in enumerate(row) if x) for row in reduced]
        basis = []
        for free in range(width):
            if free in pivots:
                continue
            v = [0] * width
            v[free] = 1
            for pivot, row in zip(pivots, reduced):
                v[pivot] = row[free]
            basis.append(tuple(v))
        return self.rref(basis, width)

    def omega(self, v, y, s):
        sigma = self.frobs[s % self.m]
        result = 0
        for i, j in ((0, 2), (1, 3), (2, 0), (3, 1)):
            result ^= self.times[sigma[v[i]]][y[j]]
        return result

    def right_radical(self, basis, s):
        gram = [tuple(self.omega(x, y, s) for y in basis) for x in basis]
        result = []
        for coeffs in self.kernel(gram, len(basis)):
            v = (0,) * 4
            for c, b in zip(coeffs, basis):
                v = add(v, self.scale(c, b))
            result.append(v)
        return self.rref(result, 4)

    def determinant(self, v):
        return self.times[v[0]][v[3]] ^ self.times[v[1]][v[2]]


def points(field, width):
    for pivot in range(width):
        for tail in product(range(field.q), repeat=width - pivot - 1):
            yield (0,) * pivot + (1,) + tail


def directed_flags(field, s, raw_geometry, census):
    q = field.q
    n_points = n_flags = selfdual_flags = good_flags = 0
    selfdual_planes = set()
    directed_witness = None
    stream = hashlib.sha256()
    for v in points(field, 4):
        if field.determinant(v) == 0 or field.omega(v, v, s):
            continue
        n_points += 1
        line = (v,)
        # omega(x,v)=0, NOT omega(v,x)=0. Apply sigma^{-1} to
        # its value, obtaining one ordinary field-linear equation in x.
        inverse_sigma = field.frobs[(-s) % field.m]
        coefficients = tuple(inverse_sigma[a] for a in v[2:] + v[:2])
        hyperplane = field.kernel([coefficients], 4)
        assert len(hyperplane) == 3
        assert all(field.omega(x, v, s) == 0 for x in hyperplane)
        assert field.right_radical(line, s) == line
        assert field.right_radical(hyperplane, s) == line
        extension = [v]
        for x in hyperplane:
            if len(field.rref(extension + [x], 4)) > len(extension):
                extension.append(x)
        assert len(extension) == 3
        for a, b in [(1, t) for t in range(q)] + [(0, 1)]:
            w = add(field.scale(a, extension[1]), field.scale(b, extension[2]))
            assert field.omega(w, v, s) == 0
            plane = field.rref([v, w], 4)
            radical = field.right_radical(plane, s)
            whole = len(radical) == 2
            assert whole == (field.omega(v, w, s) == 0 and field.omega(w, w, s) == 0)
            if whole:
                assert radical == plane
                selfdual_flags += 1
                selfdual_planes.add(plane)
            else:
                assert radical == line
                good_flags += 1
            if directed_witness is None and field.omega(v, w, s):
                directed_witness = {"v": v, "w": w, "omega_w_v": 0,
                                    "omega_v_w": field.omega(v, w, s)}
            n_flags += 1
            stream.update((json.dumps([v, plane, whole], separators=(",", ":")) + "\n").encode())
    assert n_flags == (q + 1) * n_points == selfdual_flags + good_flags
    observed_k_v = 2 * n_points + good_flags
    assert n_points == raw_geometry["observed_U_rank_two_points"]
    assert selfdual_flags == raw_geometry["observed_B_incidences"]
    assert observed_k_v == raw_geometry["observed_K_V_hull_mu_one"]
    if q == 16:
        assert observed_k_v == census["observed_mu_one_input_strata"]["K_V"]
    if (2 * s) % field.m:
        assert directed_witness is not None
    else:
        assert directed_witness is None
    return {"q": q, "s": s, "scope": "All rank2 isotropic points and their directed flags; not a B^2 module or global census",
            "rank_two_isotropic_points_U": n_points, "dimension_two_candidate_flags": n_flags,
            "selfdual_flags_F": selfdual_flags, "nonselfdual_flags": good_flags,
            "dimension_one_and_three_flags": 2 * n_points,
            "K_V_mu_one_by_actual_right_radicals": observed_k_v,
            "distinct_noncontained_selfdual_planes_met": len(selfdual_planes),
            "wrong_annihilator_direction_witness": directed_witness,
            "complete_flag_stream_sha256_hash_only": stream.hexdigest()}


def hermitian_graphs(field, s):
    if field.m // __import__("math").gcd(field.m, s) % 2:
        return None
    sigma = field.frobs[s]
    sigma2 = field.frobs[(2 * s) % field.m]
    base = [a for a in range(field.q) if sigma2[a] == a]
    fixed = [a for a in base if sigma[a] == a]
    roles = Counter()
    for h, j, x in product(fixed, fixed, base):
        def value(a, b):
            return (field.times[sigma[x]][field.times[a][a]]
                    ^ field.times[h ^ j][field.times[a][b]]
                    ^ field.times[x][field.times[b][b]])
        base_roots = int(value(1, 0) == 0) + sum(value(t, 1) == 0 for t in base)
        extended_roots = int(value(1, 0) == 0) + sum(value(t, 1) == 0 for t in range(field.q))
        contained = x == 0 and h == j
        assert base_roots == len(base) + 1 if contained else base_roots in (1, 2)
        assert extended_roots == (field.q + 1 if contained else base_roots)
        roles["contained" if contained else "tangent" if base_roots == 1 else "secant"] += 1
    return {"q": field.q, "s": s, "E_size": len(base), "Q": len(fixed),
            "graph_matrices": len(base) * len(fixed)**2, "actual_graph_root_types": dict(roles),
            "all_noncontained_graphs_split_over_E": True,
            "scope": "Hermitian graph chart only; ranks0/1 handled in the candidate proof and other geometry driver"}


def main(label):
    assert label and all(c.isalnum() or c in "_-" for c in label)
    destination = HERE / "results" / label
    assert not destination.exists(), "Refusing to overwrite evidence"
    destination.mkdir(parents=True)
    try:
        geometry_path = HERE / "results/finalisation_m8_distribution_audit_v1/geometry_cases.json"
        census_path = HERE / "results/finalisation_m8_distribution_v1/summary.json"
        geometry = {(r["q"], r["s"]): r for r in json.loads(geometry_path.read_text())}
        census = {r["s"]: r for r in json.loads(census_path.read_text())["q16_observations"]}
        flags, graphs = [], []
        for degree in (2, 3, 4):
            field = BinaryField(degree)
            for s in range(degree):
                row = directed_flags(field, s, geometry[(field.q, s)], census.get(s))
                flags.append(row)
                graph = hermitian_graphs(field, s)
                if graph is not None:
                    graphs.append(graph)
                print("PASS standalone directed flags", field.q, s, flush=True)
        (destination / "directed_flag_cases.json").write_text(json.dumps(flags, indent=2) + "\n")
        (destination / "hermitian_graph_cases.json").write_text(json.dumps(graphs, indent=2) + "\n")
        result = {"status": "PASS", "repository_code_imports": [],
                  "field_twist_cases": len(flags),
                  "directed_two_plane_flags_checked": sum(r["dimension_two_candidate_flags"] for r in flags),
                  "nonreflexive_wrong_direction_witnesses": sum(r["wrong_annihilator_direction_witness"] is not None for r in flags),
                  "hermitian_graph_field_twist_cases": len(graphs),
                  "hermitian_graph_matrices_checked": sum(r["graph_matrices"] for r in graphs),
                  "all_fresh_raw_geometry_and_q16_stratum_comparisons_match": True,
                  "source_sha256": sha(Path(__file__)),
                  "input_hashes": {str(p.relative_to(HERE)): sha(p) for p in (geometry_path, census_path)},
                  "output_hashes": {p.name: sha(p) for p in sorted(destination.glob("*.json"))},
                  "human_independent_review_completed": False, "proof_assistant_checked": False,
                  "external_originality_certified": False,
                  "scope": "Additional standalone finite directed-flag/root scrutiny by the same agent; not complete-proof independent acceptance"}
        text = json.dumps(result, indent=2) + "\n"
        (destination / "summary.json").write_text(text)
        (destination / "stdout.txt").write_text(text)
        print(text, end="")
    except Exception:
        (destination / "FAILURE.txt").write_text(traceback.format_exc())
        (destination / "FAILURE_SOURCE.py").write_bytes(Path(__file__).read_bytes())
        raise


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Assertions must remain enabled")
    if len(sys.argv) != 2:
        raise SystemExit("Supply a fresh result label")
    main(sys.argv[1])
