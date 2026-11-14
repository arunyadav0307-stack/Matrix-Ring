"""Integer formulas from A13; not a field or hull implementation.

Counts EMBEDDED Core A inputs by the B-column hull generator number.
They are marginal counts for one twist, not a joint same-input profile.
The verification drivers must compare these predictions with actual spaces.
"""
from math import gcd


def distribution(m, s):
    assert m >= 1 and 0 <= s < m  # m=1 is an auxiliary comparison only.
    q = 1 << m
    g = gcd(s, m)
    Q = 1 << g
    order = m // g
    if order % 2:
        d = 1
        c = Q**2
        incidences = q * (Q**3 + Q**2 - 1) - Q**2
        plane_types = {"contained": Q + 2, "tangent": Q**2 - 1,
                       "secant": Q**2 * (Q + 1) // 2, "external": Q**2 * (Q - 1) // 2}
    else:
        d = Q + 1
        c = Q * (Q**2 - Q + 1)
        incidences = (Q**2 - 1) * (q * (Q**2 + Q + 1) - Q**2)
        plane_types = {"contained": 2 * (Q + 1), "tangent": (Q + 1) * (Q**2 - 1),
                       "secant": Q**2 * (Q**2 - 1), "external": 0}
    assert d == gcd((1 << s) + 1, q - 1)
    isotropic_points = q**2 + q + 1 + q * c
    isotropic_rank_one = (q + 1) * (Q + 1) + d * (q - Q)
    isotropic_rank_two = isotropic_points - isotropic_rank_one
    layer_mu_one = (q + 3) * isotropic_rank_two - incidences
    a = (q + 1) * (2 * q**2 + q + 1)
    primitive_mu_one = a + d * (q**3 - q**2 - Q**2 * (q - Q))
    K_line_mu_one = a - d * q**2
    n0 = (q + 1 - d) * q**3 + 2
    n1 = primitive_mu_one + K_line_mu_one + layer_mu_one
    n3 = d
    total = 2 * q**4 + 8 * q**3 + 10 * q**2 + 7 * q + 9
    n2 = total - n0 - n1 - n3
    assert min(n0, n1, n2, n3, isotropic_rank_two, incidences, layer_mu_one) >= 0
    assert incidences == plane_types["tangent"] * q + plane_types["secant"] * (q - 1) + plane_types["external"] * (q + 1)
    return {"m": m, "q": q, "s": s, "gcd_s_m": g, "fixed_field_size_Q": Q,
            "Frobenius_order": order, "isotropic_residue_lines_d": d,
            "all_embedded_input_modules": total,
            "hull_mu_counts": {0: n0, 1: n1, 2: n2, 3: n3},
            "layer_isotropic_projective_points": isotropic_points,
            "isotropic_projection_rank_one_points": isotropic_rank_one,
            "isotropic_projection_rank_two_points_U": isotropic_rank_two,
            "selfdual_two_plane_quadric_intersection_types": plane_types,
            "selfdual_two_plane_rank_two_point_incidences_B": incidences,
            "mu_one_K_equals_V_inputs": layer_mu_one,
            "mu_one_primitive_inputs": primitive_mu_one,
            "mu_one_radical_K_line_inputs": K_line_mu_one}
