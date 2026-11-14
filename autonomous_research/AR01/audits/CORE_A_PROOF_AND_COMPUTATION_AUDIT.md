# Core A — internal proof and computation audit

**Disposition: the stated bounded preservation proof is internally valid; finite checks PASS. External novelty and independent human review remain NOT CERTIFIED.** Session calendar 2026-11-12 UTC. This is the same agent's explicit proof reread plus algorithmically separate arithmetic/representation checks, not a second researcher or a formal proof-assistant certificate.

## 1. Proof obligation ledger

| Claim / obligation | Exact argument reviewed | Disposition / boundary |
|---|---|---|
| Coordinate ring isomorphism | Foundations §2 substitutes X=1+w, gives inverse and both nilpotency relations | Valid for characteristic two, t=n=2; no larger multiplicity copied |
| Sided column dictionary | Foundations §3 uses matrix units, independent columns and right multiplication | Valid right ideals; no row/left convention substitution |
| Global-to-local dual | Foundations §4 checks constant and X coefficients via x and Xx, then each matrix entry | Valid actual first-slot dual, not a conveniently chosen local form |
| Functional and scalar/ring agreement | Foundations §5 ℓ=c_u+c_uw, nonsingular J₄ and multiplier tests on B-modules | Valid; no full-Hom-surjectivity argument or absolute field trace |
| Positive double twist | Inclusion after σ_s and equal dimensions from actual nonsingular scalar form | Valid, not universal DD=W; q8 nonreflexive control distinguishes them |
| Generator calculation | Foundations §6 proves the nilpotent top-quotient/Nakayama step | Valid; μ not socle type, embedded residue dimension or free rank |
| Every scalar ideal has μ≤2 | Result §1 handles unit, socle-only and nonzero linear radical cases | Valid; does not imply every B² submodule has μ≤2 |
| Primitive input branch | Result §2 solves one unit-entry linear equation; hull embeds in a free B-line | Valid for all σ_s; no ambient basis/equivalence change |
| Radical input branch | JW⊂H⊂W, dim JW≤2; h=0,d or the only remaining d=2,h=1 case | Exhaustive; in the last case x in/out of ambient socle supplies the needed bound |
| Universality and zero | Proof uses μ(W)≤2 and exact ring only, never a finite census or σ²=id | Covers all m≥2, all s, zero/nonfree inputs; no arbitrary n/t/r claim |
| Attainability | I₂, diag(u,0), uI₂, with explicit hull arguments | Exactly {0,1,2}, a routine corollary, not multiple new contributions |
| Positive growth | v=(1,1+αuw); restricted norm (α+σ_sα)uw and Ann(uw)=J | Valid when α is nonfixed; μ grows 1→2 without nonprincipality |
| Out-of-class control | W_*=J(1,1)+(uw)B² has μ3 and direct dual equation characterization | Valid known input; not a counterexample to principal-input theorem or new witness |

No step relies on the false old direct-sum family, unqualified freeness, an unproved wider equivalence or a quantum bridge. Old issue records remain unchanged; a new valid argument does not repair a different old printed proof in place.

## 2. Executed primary verification

Script: `../computations/verify_core_a.py`, arithmetic `../computations/core_a.py`. Outputs: `../computations/results/main_v1/` (cases, CSV, summary and stdout). Only Python standard library; seed **20261112**.

- **Auxiliary q=2, m=1:** all **65,536** generating 2×2 matrices over B were examined and deduplicated into **137** principal-input modules. All their hull μ≤2. This is **outside the primary m≥2 contract** and is explicitly labelled auxiliary.
- **Primary q=4,8,16:** **240 stratified sampled generating matrices per q**, tested for every s for those fields: **2,160 field/twist cases**. Not an exhaustive q4/q8/q16 census.
- **72 named field/twist cases**, including the known μ3 input as an out-of-class negative control, cover zero, whole ambient, attainability, radical mixtures, growth and nonreflexive slopes.
- Complete scalar-ideal checks examine **67** ambient subspaces at q2 and **529** at q4, finding **7** and **9** ideals respectively, maximum μ=2.
- Field axioms/inverses/Frobenius pairs, ring basis associativity, scalar Gram rank, module closure, local B/scalar dual equality, size complement, positive double twist, and same-embedded-module presentation changes pass.

These counts refer to actual quantified tasks, not counts of proved theorems or an all-parameter certificate. See source hashes embedded in `main_v1/summary.json`.

## 3. Separately implemented verification

Script: `../computations/audit_core_a_independent.py`; outputs `../computations/results/audit_v1/`. It imports **neither primary arithmetic nor original project code**. It reads the main cases as data only.

1. **Alternative auxiliary q2 exhaustion:** enumerate all **417,199** RREF field subspaces of the 8-dimensional ambient space; filter by u,w action. This finds **159 B-submodules**, exactly **137** with input μ≤2, matching all canonical spaces from the primary generator enumeration. Duals/hulls use brute finite sets and direct B-valued products, not primary kernel/intersection routines.
2. **Original global matrix-valued route:** construct cyclic right ideals through polynomial right multiplication in R², with independent GF4 multiplication and GF8/GF16 primitive-element tables. Intersect successive hyperplanes rather than use the primary nullspace algorithm. On **112 cases** (all 72 named cases plus 40 stratified q4 cases), compare complete global/local **dual and hull spaces**, not dimensions alone; recover μ from projected global hull columns. All agree.
3. Verify the actual global scalar functional against the local ℓ=c_u+c_uw on basis/scalar tests for all three fields/twists. Detect the wrong left-action law and distinguish coefficient Frobenius from whole-ring squaring of u.

Scope: algorithmic/representation separation, not independence of the person/agent writing the mathematics. No named external reviewer or completed external review is invented.

## 4. Negative controls preserved

- The known μ3 self-dual input defeats “all hulls are principal” without the input hypothesis.
- The explicit norm example defeats “positive Δ implies nonprincipal hull”.
- J has μ2 but socle dimension1; uB e₁ has μ1 but zero embedded residue image.
- Ordinary 8-coordinate dot product gives a different dual for a named module.
- The 8-coordinate API rejects a 16-coordinate full-image row.
- At q8,s1, double dual equals the positive double twist and is not the input module.
- The independent original-matrix route detects B(ax,y)=θ(a)B(x,y) as the wrong action rule.

## 5. Claim promotion limit

The proof, not the tests, supports the uniform Core A statement. Its elementary mechanism and positive predecessor coverage prevent promoting it to an externally original, paper-sized or Q1-ready main contribution. Full structural normal form and theorem-level literature differentiation remain separate. No quantum code parameters/distances or CSS/EA construction have been computed or asserted.
