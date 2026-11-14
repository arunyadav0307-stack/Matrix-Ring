# Core A — continuation from preserved GitHub checkpoint a74f33f

## Requirement and disposition

**Requirement:** continue the existing Core A work from GitHub checkpoint `a74f33f`, preserving that checkpoint and keeping the existing scope.

**Disposition:** the exact checkpoint is preserved, its committed successors are restored on the same branch, and fresh in-scope proof/global/scalar-QC regressions pass. No theorem hypothesis, ring, length, side, pairing, source claim or publication status is expanded by this continuation.

## 1. Immutable checkpoint and retained history

- Branch: `arena/7d88376d-matrix-ring` throughout; no branch switch, rename or additional branch.
- Requested checkpoint: **`a74f33f6c6fed1fd8315309815d9e98749c58026`**.
- Checkpoint root tree: **`e01bab242916b84b80caa6de390d47f6e41e7348`**.
- All **2,156** checkpoint blob paths, object IDs and modes match the GitHub tree.
- Saved successor chain: `a74f33f → eef4ab6 → 48fb990`; the requested checkpoint is an ancestor, not replaced by a reconstruction or reset.
- Restored committed successor: `48fb99064996c53bd3a60711ff666bf41559d64e`, all **2,213** blobs/modes matched GitHub before restoration.
- No checkpoint path was deleted. Changes to its pre-existing logs/AR01 READMEs/source-direction notes are append-only. Its proof sources, result bytes and historical backups are untouched.

Evidence: [remote trees](../evidence/A74F33F_REMOTE_BASELINE_VERIFICATION_V1.json), [successful recovery](../evidence/A74F33F_CONTINUATION_RECOVERY_V1.json). Commit/tree reachability preserves the whole checkpoint without introducing a new branch or a large duplicate Git bundle.

## 2. Unexpected local checkout state and safe restoration

At the start of this continuation, the current branch's local HEAD was the original base `12db091726835cc6f264fb0f679afc759610c89a`, with94 tracked and1,965 untracked phase0 files. The AR01 successors were absent locally. This differed from the preceding verified push; **the cause is unknown**. No platform/reset/clock explanation is inferred.

Before fetching or adopting paths, all **2,059 existing files /110,323,589 bytes** were hashed into the new [baseline receipt](../evidence/A74F33F_CONTINUATION_BASELINE_V1.json). The same remote branch still pointed at48fb990. Its fetched objects included the original a74f33f checkpoint and all later committed Core A work.

Only the1,965 existing phase0 paths were adopted in the index, after every raw byte hash, Git blob ID and file mode was verified identical to the fetched target. This avoids the untracked-collision abort documented in the earlier M4 recovery. The [narrow adoption receipt](../evidence/A74F33F_CONTINUATION_ADOPTION_V1.json) is not permission to stage unrelated files.

`git merge --ff-only --no-stat FETCH_HEAD` then completed with exit0. No new commit was created by restoration. All2,059 pre-existing files remained byte-identical, and the restored tracked tree/index were clean. Later provenance files and regression outputs are separately new, not purportedly recovered old local-only outputs.

Raw receipt times are labelled as sandbox clock observations, not normalized session/publication dates. Historical date fields and earlier recovery records are not rewritten.

## 3. Existing Core A scientific scope retained

The six [proof-finalisation records](CORE_A_PROOF_STATUS_REPORT.md) remain byte-identical to the verified M5 milestone. The statement is still the closed **marginal** hull-generator distribution for all central-length2 cyclic right codes over M₂(F_(2^m)[u]/u²),m≥2, under the original first-slot coefficient-Frobenius matrix pairing. Non-involutive twists remain covered; no joint same-input distribution or longer-length theorem is added.

The existing [scalar QC reduction/source crosswalk](../phase1/A13_SCALAR_QC_REDUCTION_AND_CLOSEST_RESULT_COMPARISON.md) and [novelty/depth assessment](A13_NOVELTY_AND_DEPTH_M6.md) also remain unchanged. Matrix-ring packaging is not promoted as novelty. Complete primary-source/version comparison, sufficient paper depth, independent human review and Q1/submission readiness remain open/not certified.

This continuation does not pretend to repeat the entire mathematical line audit or obtain new literature. It restores its committed proof/audit records, verifies document identity and runs fresh finite regressions with the already recorded scope.

## 4. Fresh executions — not overwritten or relabelled old evidence

|Fresh result label|Actual executed checks|Outcome|
|---|---|---|
|`checkpoint_continuation_proof_v1`|All2,442 q4 original-global cases;176 selected q16 cases;4,608 pairing/coefficient/shift basis checks;17 trace/graph geometry cases; non-involutive double-dual control;5 exact polynomial identities;2,080 integer-only formula pairs|PASS|
|`checkpoint_continuation_scalar_qc_v1`|All2,442 q4 and176 selected q16 scalar-QC/original-global cases; complete hull spaces and176 exported q16 duals; closure/top generator counts;1,152 scalar coefficient/shift basis checks|PASS|
|`A74F33F_CONTINUATION_DOCUMENT_CHECKS_V1`|Six-file hashes, exact proof-unit/line ranges, local links and formal N2 assembly identity|PASS|

The two numerical drivers use different routes on **the same saved q4/q16 object sets**. Their counts must not be added to claim more distinct codes. Both are same-agent computational checks, not independent human review or a proof assistant.

The fresh proof result exactly reproduces the earlier stream hashes:

- Original-global basis stream(hash only): `007b4e2ca7166f7ecda7c29e19b172f5b02874a51ed3c361c5ce716b3412c6c9`.
- Trace/graph records: `d5039892c5b218034227875237494d9e345456725de39a792121da489390dc6a`.
- Scalar-QC/global basis stream(hash only): `c64cfd97e5aeb0c14a78e7d56d61a3255974b679f89e4f0d52053baaba4d0f39`.

These are fresh successful executions in refused-overwrite result directories. The original `closed_formula_proof_v1` and `scalar_qc_v1` outputs remain unchanged.

**Coverage limits unchanged:** the666,084-case full q16 module census is read as existing executed evidence, **not rerun** here. q16 original-global/scalar-QC checking remains a176-case subset. q32/q64 checks are selected-twist geometry only, not module censuses. Integer regressions through m64 are not computations in all those fields.

## 5. Integrity, backup and synchronization

All intake bytes, the19 frozen pre-finalisation inputs, original six-document hashes, historical computation sources/results and prior ZIP hashes are checked again. Root progress records and the two AR01 READMEs receive append-only continuation entries; the intake-protected repository-root README is not edited.

`AR01_M7_CHECKPOINT_CONTINUATION.zip` is a bounded research backup of AR01 plus the four progress logs and ignore file, reopened and checked against its internal SHA-256 manifest. It is not a manuscript/submission archive. Its sidecar verification records the actual final archive hash and coverage.

The continuation payload is committed/pushed only on the existing fixed branch, without force-push, after reviewed staging. The containing commit cannot embed its own hash. Post-push remote-ref/all-blob/mode/expected-file verification and the final response identify that successor; this pre-commit report does not invent a self-referential hash or prematurely claim its push.

## 6. Actual completion, appended after push

The scientific/provenance continuation payload was committed and pushed as **`bab577437a94dc3324b589699c0ce4bf8008a0e3`**. The [post-push receipt](../evidence/A74F33F_CONTINUATION_REMOTE_RECEIPT_V1.json) verifies the fixed branch ref before/after comparison, all **2,230** local/remote blob paths/OIDs/modes and all **23** expected continuation paths. There are no deleted tracked paths. Original a74f33f remains unchanged and ancestral.

This actual-success entry supersedes the pre-commit synchronization wording above. The receipt and this addendum were written **after** the immutable research ZIP; they are archived in a small documentary follow-up rather than silently modifying that ZIP. Its verified SHA-256 remains `d97052012c462b4c072c8b56fd17f5a5aa7a599196f8c2699bf44ee8884ffc63`. No new mathematical scope, external review or novelty claim follows. The final receipt-only commit is identified/verified through Git history, not a fabricated self-hash inside this document.
