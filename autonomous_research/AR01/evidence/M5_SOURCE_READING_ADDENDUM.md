# M5 source-lead inspection and actual reading scope

This supplements, without rewriting, `M5_ALLOWED_HOST_SOURCE_SEARCH.json` and `M5_SOURCE_LEAD_INSPECTION.json`. Those receipts preserve the actual GitHub API queries/results, exact fetched Git blobs, byte counts and SHA-256 values. Search result titles and repository paths are leads, not publication/version authentication. External text was treated as data, not executed. Raw caches are outside Git in `/home/user/AR01_M5_SOURCE_CACHE/`; no complete external article is republished in this checkpoint.

## S11 — FinInG project draft: complete file read, not a final paper

Pinned source: https://github.com/gap-packages/FinInG/blob/9aef2a28b6ba500c9fedf2ddad79343895096a16/paper/fining.tex . Git blob `f3316459a685c4f07a84ca9136ebeb86b7bca863`. The complete231-line,13,907-byte retrieved TeX file was read.

Header: John Bamberg, Anton Betten, Philippe Cara, Jan De Beule, Max Neunhöffer and Michel Lavrauw, *FinInG: a package for finite incidence geometry*. The file describes projective spaces, classical polar spaces, user-specified sesquilinear/quadratic forms, semilinear collineations, Klein correspondences and related computational infrastructure. **It visibly contains unfinished sections, editorial placeholders and a duplicated section.** No journal/version/DOI or complete final article identity is inferred. The section titled “Enumerators of polar spaces” is a placeholder, not a verified enumeration theorem or an executed external checker.

Consequence: finite geometry and form/quadric enumeration are established tooling, not new ingredients. This draft neither supplies nor rules out the exact arbitrary-Frobenius incidence formula in A13. GAP/FinInG was not installed or executed here. Coordinate transformations in a classical-geometry program are not a licence for full-GL equivalence of the retained embedded code/pairing.

## S12 — polar-space article mirror: partial background reading only

Pinned mirror: https://github.com/AlexenderSokolov/cross-theory-formal-database/blob/92817451c2cf25194bff33da46a1d43e24045fd5/editable-corpus/sources/154191/source0.tex . Git blob `51b15f63de261990fd27cb99e49066769a0ea040`.

The header gives Sam Adriaensen and Maarten De Boeck, *Association schemes and orthogonality graphs on anisotropic points of polar spaces*. **Only lines80–299 were read technically**: header, abstract/introduction and early polar-space/quadric definitions. Primary author/publisher provenance, arXiv/final version equality, date and full theorem coverage are unestablished from this mirror. It is not a load-bearing reference for theorem truth or a new verified bibliography entry.

The inspected definitions explicitly concern a polarity/involution and reflexive sesquilinear forms with a second-slot twist, identity or Hermitian involution. They describe classical quadric/point infrastructure and cite further standard geometry sources. Those exact hypotheses do **not** justify treating the arbitrary non-involutive Ω_s on all of k⁴ as a classical polar space. A13 therefore counts its isotropic points directly and invokes alternating/Hermitian geometry only after the explicitly proved σ² fixed-field descent. No whole-paper noncoverage or originality conclusion is inferred from this partial reading.

## Other inspected leads — rejected or not technically used

- Blob `50195b9fc394512f35f489ee2da5334394b1eff5` (initial cache tag `Coding_1810_09951`) is headed *GhostVLAD for set-based face recognition*, not the scalar hull article. Rejected as a mismatched search lead; no coding-theory citation or technical claim relies on it.
- Blob `1586a36b75fceb6aaf12cd6a57fbb044da05b5ee` is headed *Geometric Classification of Biased Quantum Capacity via Harmonic Translation*, not S09. Header inspection only; provenance/correctness not validated; not used.
- Blob `bbd428cc759c3fbdcae2f9986492f711420f28b5` is headed *On the Levi map of nondegenerate CR submanifolds*. Header/keyword triage only; not a closest coding source and not technically used.
- Blob `691331ac1999870304c279c41342bb8a1b14a252` is headed *Hermitian-Singer Functional and Differential Codes*. Lines20–99 (header, abstract/introduction and beginning of preliminaries) were read. It concerns Hermitian-curve AG-code constructions, not an established full-text match to either missing closest source. Mirror provenance/version and the rest of its proofs are not validated; no theorem/parameter is imported.

The coding/geometry keyword search was noisy and only a bounded returned subset was inspected. **None of these actions completes the missing S01/NL10 or S09 technical comparison.** A source-access limitation, mirror mismatch or uninspected result is not evidence of a gap or of new research priority.
