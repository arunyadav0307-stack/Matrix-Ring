# 06 — Computational methodology, example design and certificate plan

**DESIGN ONLY. No scientific implementation, import, experiment, enumeration or new code construction is performed in this task.**

[Framework](04_MATHEMATICAL_FRAMEWORK.md) · [Theorem targets](05_THEOREM_ROADMAP.md) · [Future phase gates](08_PHASE_WISE_EXECUTION_PLAN.md)

The scripts in this delivery copy/hash/check/package planning files only. They are **not** prototypes of the following research programme.

## 1. Purpose and separation of evidence

Future computation, if expressly authorized, should falsify overly broad structural claims, verify explicit objects and support proofs. It must not substitute a finite scan for a parameter-uniform theorem, establish priority by no-match searches or claim optimal quantum parameters by sample maxima.

Separate labels for:

1. original-source execution and its side effects;
2. equality of the **actual** input object after coordinate/field translation;
3. independent arithmetic on that object;
4. completeness of an input-family enumeration;
5. exactness or lower-bound status of a distance;
6. universal proof status and external novelty, both separate from1–5.

No old campaign is to be rerun merely to fill the new paper's tables. The completed28/51-code audits and1,221-module census are reusable **reference evidence**, not newly generated results.

## 2. Future arithmetic and representation contract

| Layer | Required contract before implementation |
|---|---|
| Finite field | p,m, explicit irreducible polynomial, ordered polynomial basis, integer encoding, arithmetic version and field-isomorphism maps where needed |
| A_t and B | u/X coefficient order, truncation, reduction modulo X^n−1, cyclic shift; all units/zero tests unambiguous |
| Local T_j | Explicit global-to-local isomorphism and inverse, K_j embedding, u/w ordering, induced σ_s/rev/form operators |
| Matrix ideal | Right ideals and **column** Morita modules; r=2 fixed unless separately approved |
| Morita basis | Canonical F_q-basis in F_q^(2tn) for W and H_s(W), not merely a B-generating list |
| Image-code basis | Separate F_q-basis in F_q^(4tn), with explicit maps to/from Morita representation; dimensions checked |
| Equivalence | Exact subspace identity keys distinguished from generator changes, ambient GL or physical isometries |
| Duals/hulls | Actual first-slot Galois form, ring/scalar comparison where valid, induced local form; Euclidean/trace outputs named separately |

For reuse of old matrices, the actual encodings are GF8: **x³+x+1**, GF9: **x²+1**, GF4: x²+x+1. Earlier alternative library polynomials do not define identical integer labels. New work may use another encoding only with an explicit checked isomorphism and provenance; it must not rewrite inherited bytes.

## 3. Independent calculation paths — future design

- **Path A (definition):** compute the dual using the specified scalar/ring pairing and field linear algebra; intersect with the input code, then convert to its Morita module under a validated representation map.
- **Path B (module structure):** use the source-reviewed column image/kernel/reversal description and the proposed structural invariants/normal form; construct the hull module directly.
- **Path C (small exact control):** on explicitly tiny cases only, enumerate module elements or candidate generators to validate closure, equality and minimal-generation certificates.

A and B must compare **subspaces**, not only dimensions. If both use the same flawed field routine or the same hull helper, agreement is not independent arithmetic. A later verifier should use separately implemented arithmetic/linear algebra or a justified external system with frozen versions. Shared standard mathematics is acceptable; shared unexamined implementation is disclosed.

Minimality is certified by the residue-space dimension H/mH over the correct K and a generator lift whose module closure equals H. Not finding a small generating set in a random search is not a minimality proof. Generic Nakayama arithmetic is a **check of an object**, not by itself a new structural theorem.

## 4. Planned input families and example roles

No row below reports a new outcome.

| Planned family | Purpose | Proposed mode / limit | Expected evidence, not expected answer |
|---|---|---|---|
| Existing (4,2,2), s=0,1, r=2 | Regression/old finite anchor; principal-input filter | **Reuse sealed existing census**, not rerun the campaign in this planning task | Known1+3 nonprincipal hulls belong to nonprincipal inputs; old data only |
| q=2, t=2,n=2 | Tiny arithmetic/negative controls if approved | Exhaust only if the chosen object count is proved small | No nontrivial Galois evidence at a prime field |
| q=8, t=2,n=2, s=0,1,2 | Non-reflexive comparison in proposed Core A | Normal-form-directed finite class or capped sample, never a claimed full ambient census | Explicit profile/counterexample or no finding **within the actual range** |
| Symbolic q=2^m Core A | Test structural theorem hypotheses and parameter dependence | Future symbolic reasoning separately authorized; not replaced by many numerical q | Parameter-uniform theorem only with proof |
| t=2,e=3,p=3 local factor, e.g. q9,n3 | Odd-characteristic/repeated-root contrast, only after Core A gate | Small chosen principal-input classes/capped examples | Exact induced form and named profiles, not a prefilled μ3 growth claim |
| Several CRT factors | Validate coupling and any genuine NT07 extension | Only after approved local result and explicit transport | A nontrivial coupled example if one exists; naive independent-hull control |
| r=3 or larger t/e | Optional later extension | **Not part of the initial pilot** | Requires new structural justification, budgets and approval |

Expected worked examples: zero and ambient codes; principal LCD and principal self-orthogonal inputs; an example distinguishing embedding/form data if it exists; preservation/growth boundary examples dictated by a proved theorem; a nonprincipal-input old witness clearly labelled **prior work**. No example category is guaranteed nonempty.

## 5. Planned table schemas — no fabricated parameter rows

### Table A — algebraic generator profiles

`object_id; origin (old/new); q/p/m; field modulus; r/t/n; local factors; s; input generators and hash; dim_q W; μ_B(W); input principal certificate; dim_q H; μ_B(H); local radical/Loewy profile; relevant embedding/form data; P_s; proof/theorem locator; verification mode; exactness/completeness; limitations`.

### Table B — principal-input spectrum/classification

`class_id; exact class definition; number expected/proved if available; number visited; completeness argument; twists; attained hull μ values; bound; attainment witness IDs; unvisited/timeout count; theorem versus finite status`.

### Table C — algorithm/certificate costs

`input model; D; coefficient field; arithmetic operation count if proved; wall time/hardware; memory; candidate count; rejected/accepted/duplicate counts; verifier time; version/seed/budget; timeout or incomplete status`.

### Table D — optional quantum parameters

Only after the separate quantum gate: `actual field-code matrix/hash; physical q; classical construction alphabet; N; k; h_E or exact trace-radical dimension; route; K; c and resource convention; d exact or ≥L; certificate method/range; Bob/phase check; source of external comparator and returned physical header; novelty qualification`.

An algebraic μ column is never substituted for an h_E column. Repeated parameter tuples, route-labelled rows, equal matrices and equivalent codes are counted separately and named explicitly.

## 6. Certificate bundle per named new object — future requirement

At minimum retain:

1. exact field/ring/coordinate metadata and generator bytes;
2. input and hull canonical field bases with separate module/image dimensions;
3. B-action closure witnesses and right-sided generator reconstruction;
4. dual/hull bases from both paths, or an explicit unresolved disagreement;
5. local H/mH bases, radical products and generator lifts;
6. rank/nullity checks, input μ≤2 certificate and hull μ value;
7. theorem-hypothesis flags, including t/e and reflexivity distinctions;
8. independent verifier output, source/program hashes and execution environment;
9. enumeration scope or sample seed/selection rule, rejected/duplicate/timeout counts;
10. if quantum retained, all physical checks and distance evidence separately.

An object with matching parameters but different matrices does not inherit another certificate. Any coordinate transformation or field migration invalidates byte-level reuse until its map and any weight change are checked.

## 7. Verification and falsification tests to specify before running

Future tests must include: wrong left/right action; rows-versus-columns; omission of rev at **n≥3** (n≤2 is vacuous); wrong twist orientation; local factor permutation omitted; illegal freeness assertion; coarse-dimension-only classification; full image rows passed as Morita vectors; bilinear/Hermitian form confusion; ordinary-Euclidean versus transported hull substitution; incorrect GF8/GF9 labels; duplicate generator presentations counted as distinct codes.

If quantum is approved: include odd-characteristic phase sign, trace tests on a full Fp basis, Fq/trace orthogonal mismatch, missing Bob completion and SO/DC logical-set mismatch. Do not report a negative control as passed when the chosen test case makes it tautological.

## 8. Complexity and proposed resource envelope

Let D=2tn be the Morita field dimension at r=2; full image dimension is2D. A local T_j² has K_j-dimension2te. Dense linear algebra has ordinary polynomial-size costs in the expanded dimension, but **enumerating subspaces or generator tuples is exponential**; a precise algorithm bound is NT08, not asserted here.

Naively scanning every pair of generator columns already involves q^(2D) presentations before deduplication. Enumerating all submodules in F_q^D can be vastly larger than listing the few relevant normal forms. Full-ring or rank-three exhaustive search is not the fallback.

**Proposed initial pilot cap, NOT AUTHORIZED:** at most3 explicitly listed parameter families; at most2,000 distinct candidate inputs per new family unless a proved complete smaller class is chosen; total2 CPU-hours,4GiB RAM,250MiB new artifact budget. The author may choose smaller/larger limits or no computation (NAD10). Preflight must count/upper-bound candidates and estimate memory; stop at budget rather than silently switch to sampling and keep an EXH label. Large later data stay outside Git according to an author-approved storage/manifest policy.

These are safeguards, not performance promises. No timer, sample or resource usage from a new scientific run is reported now.

## 9. Completeness and distance vocabulary

Use **EXACT_OBJECT_LINEAR_ALGEBRA**, **EXHAUSTIVE_STATED_FAMILY**, **EXHAUSTIVE_PAIRS**, **SAMPLED**, **PARTIAL/TIMEOUT**, **DISTANCE_EXACT**, **DISTANCE_LOWER_BOUND**, and **NOT_COMPUTED** as separate fields. Enumerating all ambient words does not imply testing all word pairs. Exhaustive invariant enumeration does not imply all distances were evaluated.

For any later distance: complete enumeration or a complete increasing-support search through an attained minimum may certify exactness; excluding weights≤L without finding a witness gives d≥L+1. An ambient search lower bound is not an exact independent distance. The historical M1=24/M2 fallback=4/M3 exact11+LB17 counts are not a template for declaring “all three methods” on new records.

## 10. Safe future execution boundary

Scientific work, if later approved, uses a fresh disposable successor workspace, `python3 -B`/`PYTHONDONTWRITEBYTECODE=1`, immutable inputs and side-effect paths outside sealed evidence. A relocated historical extractor needs its recorded `MATRIX_RING_COMP`; do not run it again gratuitously. New implementations should not write beside old research data. No existing scientific script is executed or modified by this blueprint.

**Exit for computation:** every retained new object has a typed certificate and honest completeness label; disagreements/timeouts remain visible. **A computational PASS is not a theorem, novelty, quantum-validity or Q1 PASS.**

**BLUEPRINT DEVELOPMENT ONLY — wait for explicit author approval before Phase1.**
