# M4 — split double-root proof and computation audit

**Disposition:** A12 is internally proved in its exact fully split contract and its named certificates pass a separately implemented original-global check. External originality/depth, independent human review, manuscript readiness and submission readiness remain **NOT CERTIFIED**. This audit is by the same agent.

## Provenance before mathematics

The continuation checkout was at the base commit, not the previously recorded working state. Recovery, the unsuccessful first fast-forward, reviewed adoption of 1,965 identical untracked files and the successful retry are documented in the M4 resumption records. All 2,059 original files remained unchanged. M3 was freshly reverified at `d278f163c6cdcc4010fb1c19d30fddee801b63ee`, with all 2,135 tracked blobs/modes and its 26 changed paths matching GitHub. This supersedes the M3 root-log pending entries, not the historical evidence bytes.

The previous local-only split artifacts were missing. Both reconstructed script sources exactly match the SHA-256 values recorded in the preceding tool transcript. New outputs have **fresh labels** `split_resumed_v1` and `split_global_resumed_v1`; no claim is made to have recovered old output files. Chronology metadata is explicitly distinguished in `../evidence/M4_CHRONOLOGY_AND_CONTINUATION.md`.

## Proof obligations checked

| Obligation | Internal check |
|---|---|
| Fully split hypotheses | n=2N, N odd and N|(q−1); local factor B and coefficient field unchanged. N=1 explicitly recovers Core A. No non-split factor claim. |
| Global/local nilpotent coordinate | X=λ(1+w) gives X^N−1=w because λ^N=1 and N is odd. Thus no hidden root-dependent rescaling of u or w. |
| Explicit CRT inverse | e_λ evaluated at all roots is the Kronecker delta, including nilpotent parts since only even X powers occur. The displayed inverse is well-defined. |
| Actual global orthogonality | Testing every cyclic shift extracts every coefficient of x^†s y. Matrix multiplication and the original first-slot form, not an arbitrary scalar image, are retained. |
| Factor direction | Evaluation of X⁻¹ gives reversal; pulling Frobenius outside gives δ_s(λ)=σ_(−s)(λ⁻¹). No involution assumption. |
| Dual and hull transport | All input column vectors in the source factor are tested against the output factor, yielding exactly D_s(W_δ) and the displayed intersection. |
| Generator number | Product maximum and two-column packing proved in both directions. μ4 column space means two matrix generators. Zero ideals require zero generators. |
| Ambient bound and equality | Primitive module μ≤3; radical descriptor t≤2r gives μ≤4, with equality only at JB². |
| Preservation iff criterion | Fixed-factor condition equivalent to N|(2^s+1). Sufficiency uses the established same-input theorem. Necessity uses the explicit single scalar-matrix generator, not a finite search. |
| μ4 witness | D_s(zV)=JB², so the moving target has hull JB². Input remains principal in all factors. |
| μ3 witness | Directly solve dual equations for Q; check P∩P′ through ua∈kz; bound every other nonzero component via its primitive-line embedding. No unproved disjoint-sum assertion. |
| Values 0,1,2 | Constant I₂, diag(u,0), uI₂, independent of factor permutation. These are proof-derived controls; the new numerical run explicitly tests μ2 and μ3/4 witnesses, not every control at every length. |
| Same-code q4n6 example | Inverse CRT coefficients checked, same generator and same canonical input basis across both twists; complete dual/hull spaces and explicit minimal hull-generating lists verified. |
| Scalar reduction | Central scalar generator h yields the entrywise ideal (h)∩Ann(h^†s). Its matrix generator number equals the scalar ideal generator number. The μ4 mechanism is not intrinsically noncommutative. |

No proof contradiction was found in these obligations. This is not a formal proof-assistant or external referee certificate.

## Fresh executed checks

`verify_split_coupling.py split_resumed_v1`: **PASS, 41 named cases.** This is the reference component route using the unchanged `core_a.py` arithmetic. It is not by itself separate arithmetic verification or a direct test of the global form.

`audit_split_global.py split_resumed_v1 split_global_resumed_v1`: **PASS, all 41 cases** through alternative field tables, right polynomial matrix products and successive hyperplane restriction. It does not import the primary/reference computation code; primary records are read as data. It tests all eight field coordinates of Σθ_s(x_i)y_i. Complete global input/dual/hull spaces match the reference after direct CRT evaluation; dimensions alone are not the comparison. The CRT map is tested for full rank at all eight field/length pairs: (4,2),(4,6),(8,2),(8,14),(16,2),(16,6),(16,10),(16,30).

| Same q4n6 input | Input dimension | Dual dimension | Hull dimension | Max column μ | Minimum matrix generators |
|---|---:|---:|---:|---:|---:|
| s=0 |20|28|12|4|2|
| s=1 |20|28|4|2|1|

Saved certificates include the input polynomial generator, original-coordinate global hull bases, explicit minimal matrix-generator lists and full-basis hashes. Their right-generated spans are exactly the computed global hulls. Negative controls at (q4,N3,s0) and (q8,N7,s1) reject omission of reversal and forward rather than inverse Frobenius respectively: both wrong rules predict μ2 instead of the actual μ4.

### Immutable evidence identifiers

- Reference script: `ac5317018c0f5232884fd22308dce23952b8904ceec8e6b409787c0d03f9778f`.
- Global script: `703e1e07ad866dcddf09f108d5a8c473d953ca4ee10b46bc7b943f7acd1ec2aa`.
- Reference case stream: `c9295448655cdeaac3cf6281e01c652cb458f86bdb7fa8fb40f066521f268809`.
- Global case stream: `da18d2e28d30d77a912b38d3ea37de24d35123abdc48302de5d8feb6bc2fec77`.
- Same-input certificates: `947a9821edae66e145e3edf3cc5c5f0a3590a4385d422bac250ec3f79e8ca44a`.

The regenerated stream/certificate hashes also match the corresponding prior transcript results; that is reproducibility evidence, not recovered old file provenance. Neither run is an exhaustive code census at larger lengths. M2/M3 evidence is not overwritten or retroactively extended.

## Literature and publication decision

A12 is **not selected as a sole original paper contribution**. The scalar reduction positively demonstrates its routine ingredient mechanism; different ring wording or a passing example does not supply novelty. Prior S01/NL10 indexed/preview evidence reports scalar repeated-root hull determination in the matching oddly-even family; its complete technical text and version equality are still missing. S09's same nonchain-ring QC technical overlap is likewise unresolved. Previous failed retrieval/search is not a noncoverage result. New local filename inventory found no files named for these missing sources; it does not prove that every unidentified PDF has been exhaustively inspected.

A defensible next same-ring question is a closed all-q/all-twist **distribution** of Core A hull generator numbers, beyond the existing reconstruction/rank prescription and μ0/μ3 counts. It must have a complete counting proof and checks of its incidence/descent cases; it too may be known or insufficiently deep. Do not manufacture a main manuscript, quantum application, journal/quartile verdict or paper-sized novelty from these checkpoints.
