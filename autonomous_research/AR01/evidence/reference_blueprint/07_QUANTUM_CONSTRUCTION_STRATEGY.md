# 07 — Optional quantum strategy: physical hypotheses before applications

**Default recommendation: an algebra-first paper. Quantum applications are optional and separately gated. No new quantum code, bridge or parameter is claimed.**

[Theorem roadmap](05_THEOREM_ROADMAP.md) · [Computational design](06_COMPUTATIONAL_METHODOLOGY.md) · [NAD07](09_AUTHOR_DECISION_REGISTER.md)

## 1. Why quantum is not the primary novelty claim

P2-S asks about **minimal module generator number** of the actual Galois hull. Standard EA parameters depend on a specified physical commutator radical or the ordinary Euclidean/Hermitian hull of a field code. These are different invariants. There is no proved μ_B(H_s)→h_E or μ_B(H_s)→c map in this blueprint.

MS03 already has quantum constructions and four supplied q8 EA records; the earlier A8 matrix-ring Gray/CSS construction and field/commutative Galois-hull EA papers are mandatory predecessors. A new table made by the same generic EA formula would not make the new structural result a new quantum construction.

**NAD07 recommendation:** retain a conditional application track, but exclude quantum from the minimum contribution requirement. If no genuinely useful and justified connection survives, remove quantum claims rather than force them into the title.

## 2. Coordinate and physical-alphabet contract

For coefficient expansion of R=M_r(A_t), N=tr²n **field coordinates** over F_q. At r=2, N=4tn. The associated symplectic label space has2N field coordinates; that is not2N physical qudits.

The transported form is σ_s(x)J y^T, J=I_(r²n)⊗H_t in a fixed ordering. It is not automatically ordinary Euclidean. Involutive Hermitian, general sesquilinear, bilinear and absolute-trace forms must be distinguished. A field code over F_(q²) used in a Hermitian construction may correspond to physical q, not physical q²; every record must state both alphabets.

A nonmonomial congruence can change Hamming distance. The characteristic-two/even-t **bilinear** obstruction does not prohibit Hermitian congruences or all individual Euclidean self-orthogonal images. No ambient-form assertion replaces an actual code inclusion or physical isotropy test.

## 3. Standard routes available later — imports, not new results

Let D≤F_q^N be a **specified F_q-linear** field code of dimension k, and H_E=D∩D^(⊥E), h_E=dim_q H_E. The following single-code Euclidean routes are inherited standard constructions under their physical stabilizer hypotheses; no proof is developed here. Distance statements use nonempty logical-error sets, e.g. K>0; zero-dimensional codes require separate conventions.

| Route | Required actual hypothesis / stabilizer input | Parameters | Relative-distance set |
|---|---|---|---|
| SO CSS | D⊆D^(⊥E), with phase-correct scalar-free lift | K=N−2k, c=0 | D^(⊥E) minus D |
| DC CSS | D^(⊥E)⊆D; stabilizer is built from D^(⊥E), **not from the original D as if SO** | K=2k−N, c=0 | D minus D^(⊥E) |
| Euclidean EA | D arbitrary F_q-linear; valid Bob completion of the nonisotropic Alice labels | c=k−h_E, K=N−k−h_E | D^(⊥E) minus H_E |

For EA, c denotes shared maximally entangled **q-dimensional pairs** in this convention; do not silently equate it with a qubit-ebit count. Bob completion and an Alice-only logical-error argument are required; unextended noncommuting Alice labels do not all fix a codespace.

The distance is the minimum **coset-leader** weight of the route-correct relative set, not the Hamming weight of an arbitrary quotient representative. A quotient does not automatically become an ordinary length-N Hamming linear code.

The EA identities K−c=N−2k and K+c=N−2h_E are not universal formulas for R1 or DC with original k. The audit's742 DC metadata failures do not refute their code distances; they refute the blanket bookkeeping scope. No such universal statement will be reused.

## 4. General non-reflexive/trace route — only if explicitly justified

A proposed twisted graph route must identify its exact label space L and linearity field. A map involving coefficient Frobenius can make L **only F_p-linear**, even when its source D is F_q-linear. The commutator is the **absolute trace-symplectic** form. Its trace orthogonal generally differs from the orthogonal defined by an F_q-valued symplectic equation.

For an F_p-linear isotropic label space of dimension a, a scalar-free phase-correct stabilizer lift would have codespace dimension p^(mN−a). Writing that as q^K requires a=m(N−K) with the appropriate integer K; an Fq-linearity assertion cannot be inserted to force this. A graph construction with a=mk is a special case to justify, not an assumption about every label space.

Future proof/verification obligations:

- exact ordered X/Z/Weyl convention and odd-p phase sign;
- trace isotropy on an Fp basis, or genuinely equivalent full-value conditions;
- a scalar-free group/lift with correct p-dependent phases;
- trace centralizer and actual stabilizer subgroup intersection;
- Bob resource accounting if labels are nonisotropic;
- correct physical weight/error model and a nonempty logical-error set.

The existing R1 is prior work, not NT09's novelty. A “semilinear entanglement number” requires a new, valid physical derivation and predecessor comparison, not replacement of h_E by h_s in a formula.

## 5. Gate for connecting the new algebra to quantum information

A quantum application may proceed only if **all** of QG1–QG6 are satisfied in a later approved phase:

| Gate | Evidence required |
|---|---|
| QG1 — algebraic relevance | A proved new structural theorem identifies the actual invariant controlling the selected physical construction, or a clearly limited new consequence |
| QG2 — form bridge | A proved map to the relevant Euclidean/Hermitian/trace form, with fields, sides and domains explicit; or direct physical commutator calculation on each actual field-code matrix |
| QG3 — metric bridge | Monomial/isometric justification where claimed; otherwise recomputed distances in the physical coordinates, no Hamming-preservation assumption |
| QG4 — physical validity | Isotropy/phase/scalar-free lift or Bob completion and route-correct orthogonals, with an independently reviewed proof |
| QG5 — named-object certification | Exact matrices, field encodings, k/h/K/c and inclusions checked; exact d or honest lower bound; no tuple-only certificate reuse |
| QG6 — genuine incremental content | Source-specific comparison with MS03, A8, Cao, C5/C6, NL08 and other relevant works; not a generic EA formula plus another table |

Direct ordinary-Euclidean verification can justify a **particular application** without an ambient Galois→Euclidean theorem. It does not turn a Galois μ-classification into an entanglement-cost theorem. If only such generic applications are available, label them illustrations or omit them.

## 6. Prospective examples and benchmark policy

After QG1–QG6 and author approval, examples could pair an algebraic principal-input classification certificate with a fully specified field image and a correct SO/DC/EA/trace route. No new tuple is predicted now. In particular, neither principal input nor μ3 hull implies distance improvement or low entanglement.

Compare only identical physical alphabet, N,K, distance status, c/resource convention and route/bound hypotheses. Record the returned table header and bound interval, not just a query parameter. Physical-q8 stabilizer tables and qubit/qutrit EA tables exist at audited probes; absence of a guessed endpoint does not establish absence of all tables. Those tables do not automatically benchmark physical q4/q8/q9 EA examples.

No “record”, “optimal”, “first q8”, universal budget ceiling or new Singleton-bound priority is claimed. B047's inherited d≥5 at c=2 already contradicts the old d≤4 low-budget ceiling; it is not a new construction of this proposal. A family sample can contain an exact-distance code, and a full invariant census can still have a capped distance stage.

## 7. Quantum no-go/omit option

If the new structural invariant has no nonroutine physical consequence, if the bridge is already known, or if the metric/trace hypotheses cannot be proved within the authorized scope, end NT09 as **UNRESOLVED/ALREADY KNOWN/OMITTED**. A strong algebraic result can proceed to its own journal-fit assessment without quantum. A weak algebraic result cannot be rescued by adding invalid quantum claims.

**BLUEPRINT DEVELOPMENT ONLY — no quantum construction or implementation authorized.**
