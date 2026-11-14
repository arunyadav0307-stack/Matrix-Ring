# Core A embedded-structure theorem — internal audit

Session calendar **2026-11-12 UTC**. **Proof reread: internally valid in the exact Core A contract. Executed finite checks: PASS. External originality/depth, independent human review and submission readiness: NOT CERTIFIED.** This is not a claim of a second reviewer.

## Proof obligations actually checked

| Obligation | Check and outcome |
|---|---|
| Exhaustive scalar ideal list and annihilators | Unit/proper ideal split; nonzero linear radical image forces z; line/full image covers all cases. Ann(I_L)=I_L uses characteristic two explicitly. |
| Radical descriptor extraction | K is the complete socle intersection; T is the first-layer projection. Both u,w actions force both projections of T inside K. f is defined as a quotient coset, not an unproved splitting. |
| Reconstruction and uniqueness | The inverse (R1) is closed under k,u,w; extracting K,T,f returns the same triple. Coordinate order fixed. This is an embedded descriptor, not isomorphism classification/minimality. |
| Actual induced form | Multiply β_s in B: only u×w and w×u survive. Thus Ω_s is exactly the displayed first-slot σ form. No alternating assumption for s≠0. |
| Exact hull layers | zK is orthogonal to all of W, and testing the first layer gives exactly T_s. f restricts, K does not change; radical images are zP(T_s). |
| Primitive input exhaustiveness | Residue rank two forces full ambient by nilpotent Nakayama; residue rank one admits the deterministic unit projection. I is allowed to equal J, eliminating a strict-subset notation ambiguity. |
| Primitive graph/colon rule | Solve the first generator equation then all kernel-ideal tests. Membership in W gives the colon condition. Representative change t→t+j was checked using bσ(j)=0. |
| Full profile table | Scalar annihilator/ideal intersections give all four nonzero/zero I cases. Unit n, zero n, pure nonzero socle n and mixed radical n are disjoint and exhaustive. |
| Nonprincipal classification | Primitive case gives ≤2. In radical case dim K≤1 gives ≤2. K=V implies f=0; nonsingularity bounds dim T_s≤min(t,4−t). The only >2 option is t=dim T_s=2, projection rank1, forcing T=L⊕L and precisely the isotropic line condition. No finite test is used in this argument. |
| Self-duality, not only self-orthogonality | The exceptional W has dimension4; size complement gives dim D=4, hence W=D=H. Every proper hull therefore principal. |
| Isotropic counts/support | Normalize to (1,a), a≠0; roots of a^(2^s+1)=1 in cyclic k× count d_s. Fixed field of σ² gives the gcd cases; minimal-degree Frobenius orbit gives the same-input support criterion. |
| Input enumeration | Disjoint residue ranks and canonical (K,T,f)/(I,t+I) data. Count quotient maps, Grassmannian subspaces and quotient representatives; no full-GL quotient. |
| Hull-zero count | Nonzero radical input has surviving socle. Primitive nonzero I has nonzero hull. Free lines contribute exactly anisotropic residue lines times q³; add zero and full ambient. |

The strongest new internal conclusion is **μ(H)>2 iff W=J L+uwV for a σ-isotropic line L**, and then H=W=D, μ=3. This is not an extension to n=4 or general factor coupling. The legacy proper μ3 hull examples at n=4 belong to another ring and remain attributed there.

## Executed structural verifier

`../computations/verify_core_a_structure.py`, output `../computations/results/structure_v1/`:

| Field | Embedded modules (complete) | All twists / field-twist cases | Hull-μ histogram by twist |
|---|---:|---:|---|
| q2, auxiliary outside m≥2 | 159 | 1 /159 | s0: {0:18,1:78,2:62,3:1} |
| q4, core | 1,221 | 2 /2,442 | s0: {0:258,1:522,2:440,3:1}; s1: {0:130,1:538,2:550,3:3} |
| q8, core | 12,993 | 3 /38,979 | s0: {0:4098,1:3858,2:5036,3:1}; s1,s2: {0:4098,1:3534,2:5360,3:1} |

The constructor uses the proved descriptors, then deduplicates all canonical spaces and checks module closure, input μ, complete generic-vs-structural hull bases, all exceptional inputs and the proved total/LCD counts. At auxiliary q2 its **entire 159-space set** matches the separately implemented 417,199-ambient-subspace enumeration from `audit_v1`, not merely the count. q4 matches the earlier documented counts while being a new run, not reuse of old outputs.

Storage: all 2,442 q4 case records are saved in compact JSONL. All q8 cases were computed and checked, but only summary and deterministic complete-stream SHA-256 are retained to avoid a large generated dataset; regeneration is deterministic. **No q16 exhaustive census was run.** The value 166,521 there is the proved counting formula, not an observed q16 enumeration.

## Executed separate original-global-pairing audit

`../computations/audit_core_a_structure_global.py`, output `../computations/results/structure_global_v1/`:

- Imports the unchanged alternative arithmetic/global checker, **not** primary or structural code.
- **All 1,221 q4 modules, both twists: 2,442 cases.** Reconstructs right ideals by original polynomial matrix multiplication in R²; tests the original matrix-valued first-slot dual; obtains full global dual/hull spaces by independent field tables and successive hyperplane restriction.
- Compares the complete independently derived local hull basis with the saved generic/structural basis, as well as full global/local spaces within the alternative route. All agree.
- Builds **87** named line-family field/twist cases, exhausting a∈k× at q4,q8,q16; checks the norm-root counts and same-input minimal-degree twist support. q16 covers this named family only.
- Does not repeat the complete q8 census through the global implementation. Original `main_v1`/`audit_v1` evidence remains unchanged.

Source and input hashes are embedded in both summaries. No source file hashed by an old run was silently edited to make a test pass.

## Evidence and publication limits

Finite algorithmic checks are not the universal proof. Separate algorithms by the same agent are not external human review. The new formulas are a rigorous bounded structural development, but parts are elementary and parts use standard field intersection linear algebra. Closest-source theorem comparison remains incomplete, especially scalar repeated-root hulls and the same nonchain-ring QC lead. No firstness, paper-sized novelty, journal/quartile or quantum bridge is certified. Historical correction-family/RF/claim/decision registers remain unclosed by this audit.
