#!/usr/bin/env python3
"""Read-only manuscript/version/document inventory. No research code is executed.
All new output is exclusive and restricted to correction_plan/evidence.
"""
from pathlib import Path
import csv
import datetime
import difflib
import hashlib
import json
import re

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
PRIOR = REPO / 'phase0_audit/extracted/prior_project'
E = BASE / 'evidence'
H = lambda b: hashlib.sha256(b).hexdigest()

def stamp(p):
    return datetime.datetime.fromtimestamp(p.stat().st_mtime, datetime.timezone.utc).isoformat()

def csvout(name, rows):
    with (E / name).open('x', newline='', encoding='utf8') as out:
        w = csv.DictWriter(out, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)

def jsonout(name, obj):
    with (E / name).open('x', encoding='utf8') as out:
        json.dump(obj, out, indent=2, ensure_ascii=False); out.write('\n')

roots = sorted(p.parent for p in PRIOR.rglob('main.tex'))
latest = PRIOR / 'PAPER/FFA_FINAL_SUBMISSION_V2'
canonical = PRIOR / 'PAPER'
versions = []
files = []
comparisons = []
(E / 'version_diffs').mkdir(exist_ok=False)

def core_paths(root):
    return [root / 'main.tex', *sorted((root / 'sections').glob('*.tex')), *([root / 'references.bib'] if (root / 'references.bib').is_file() else [])]

def inventory(root, vid, kind):
    core = [p for p in core_paths(root) if p.is_file()]
    rows = []
    for p in core:
        b = p.read_bytes(); rows.append((p.relative_to(root).as_posix(), H(b)))
    identity = ''.join(d + '  ' + n + '\n' for n, d in sorted(rows))
    main = root / 'main.tex'
    all_inputs = re.findall(r'\\input\{([^}]+)\}', main.read_text())
    missing = [n for n in all_inputs if not (root / n).is_file() and not (root / (n + '.tex')).is_file()]
    value = {'version_id': vid, 'kind': kind, 'root': root.relative_to(REPO).as_posix(),
             'main_file': main.relative_to(REPO).as_posix(), 'main_bytes': main.stat().st_size,
             'observed_main_mtime_utc': stamp(main), 'main_sha256': H(main.read_bytes()),
             'core_files': len(core), 'section_files': len(list((root / 'sections').glob('*.tex'))),
             'source_payload_sha256': H(identity.encode()), 'literal_input_paths_missing': '; '.join(missing),
             'timestamp_caveat': 'Observed recovery/extraction filesystem mtime, not authorship/submission time'}
    versions.append(value)
    # Includes bibliography generation snapshots where present, and the invalid canonical PDF.
    extra = [p for p in [root / 'main.bbl', root / 'main.pdf', root / 'manuscript.pdf'] if p.is_file()]
    for p in core + extra:
        b = p.read_bytes()
        files.append({'version_id': vid, 'file': p.relative_to(REPO).as_posix(), 'relative_file': p.relative_to(root).as_posix(),
                      'bytes': len(b), 'observed_mtime_utc': stamp(p), 'sha256': H(b),
                      'pdf_magic_if_pdf': b.startswith(b'%PDF-') if p.suffix == '.pdf' else '',
                      'scope': 'Observed bytes only; PDF header alone is not parser validation'})
    return value

for i, root in enumerate(roots, 1):
    vid = 'MS%02d' % i
    inventory(root, vid, 'RECOVERED_CAMPAIGN_SOURCE_SNAPSHOT')
    changes = []
    dtext = []
    names = sorted({p.relative_to(root).as_posix() for p in core_paths(root)} | {p.relative_to(canonical).as_posix() for p in core_paths(canonical)})
    for name in names:
        a, b = canonical / name, root / name
        equal = a.is_file() and b.is_file() and a.read_bytes() == b.read_bytes()
        if not equal:
            changes.append(name)
            dtext.extend(difflib.unified_diff(a.read_text().splitlines() if a.is_file() else [], b.read_text().splitlines() if b.is_file() else [], fromfile='canonical/' + name, tofile=vid + '/' + name, n=2))
    comparisons.append({'version_id': vid, 'root': root.relative_to(REPO).as_posix(), 'changed_core_files_vs_canonical': '; '.join(changes),
                        'diff_file': 'version_diffs/' + vid + '_vs_canonical.diff',
                        'scope': 'Text differences; mathematical conflict interpreted in plan, not inferred from hash alone'})
    with (E / 'version_diffs' / (vid + '_vs_canonical.diff')).open('x', encoding='utf8') as out:
        out.write('\n'.join(dtext) + ('\n' if dtext else ''))

mirrors = [
    ('CP01', REPO / 'phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER'),
    ('CP02', REPO / 'phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER/FFA_FINAL_SUBMISSION_V2'),
    ('IP01', REPO / 'phase0_audit/independent_review/work/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER'),
    ('IP02', REPO / 'phase0_audit/independent_review/work/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/prior_work/PAPER/FFA_FINAL_SUBMISSION_V2'),
]
for vid, root in mirrors:
    inventory(root, vid, 'CURATED_AUDIT_MIRROR_NOT_NEW_AUTHOR_VERSION')
csvout('manuscript_versions.csv', versions)
csvout('manuscript_files.csv', files)
csvout('version_comparisons.csv', comparisons)

# Enumerate manuscript-related binary-only paths without pretending their bytes exist.
patch = list(csv.DictReader((REPO / 'phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE/repository_integrity/patch_diff_inventory.csv').open()))
missing = []
for row in patch:
    name = row['prior_path']
    if row['diff_kind'] == 'BINARY_ONLY' and (name.startswith('PAPER/') or name.startswith('PHASE21_PRIVATE_DATA_ACCESS/')) and (name.endswith(('.zip', '.pdf', '.doc', '.docx', '.eml', '.msg'))):
        missing.append({'declared_prior_path': name, 'available_regular_file': (PRIOR / name).is_file(),
                        'byte_sha256': 'UNAVAILABLE_FROM_BINARY_PLACEHOLDER', 'source': 'repository_integrity/patch_diff_inventory.csv',
                        'scope': 'Declared path is not a recovered valid binary; historical manifests may supply unverified inherited digests'})
csvout('unavailable_manuscript_artifacts.csv', missing)
claims = []
for p in sorted((PRIOR / 'PAPER').glob('*.zip.sha256')):
    for line in p.read_text().splitlines():
        mat = re.fullmatch(r'([a-f0-9]{64})  (.+)', line)
        if mat:
            claims.append({'sidecar_file': p.relative_to(REPO).as_posix(), 'sidecar_observed_mtime_utc': stamp(p),
                           'sidecar_sha256': H(p.read_bytes()), 'claimed_archive': mat.group(2),
                           'claimed_archive_sha256': mat.group(1), 'actual_archive_available': (p.parent / mat.group(2)).is_file(),
                           'digest_status': 'HISTORICAL_TEXT_CLAIM_NOT_FRESH_BYTE_VERIFICATION'})
csvout('historical_archive_digest_claims.csv', claims)

# Line-level label/environment locators in the two principal author-source variants.
locators = []
for role, root in [('canonical', canonical), ('latest_staged', latest)]:
    for p in core_paths(root):
        if p.suffix != '.tex': continue
        lines = p.read_text().splitlines()
        for n, line in enumerate(lines, 1):
            if re.search(r'\\(?:label|section|subsection)\*?\{', line):
                locators.append({'variant': role, 'file': p.relative_to(REPO).as_posix(), 'line': n, 'text': line})
csvout('manuscript_statement_locators.csv', locators)

# Local-only documentary search: historical records are evidence, not current status attestations.
patterns = re.compile(r'not submitted|no submission|nothing.*submitted|not.*sent|DRAFT.*NOT SENT|manuscript (?:ID|number)|submission (?:ID|number)|Editorial Manager|final submission|canonical manuscript|FFA_FINAL_SUBMISSION_V2', re.I)
corpus = sorted(PRIOR.rglob('*.md'))
hits = []
for p in corpus:
    for n, line in enumerate(p.read_text().splitlines(), 1):
        if patterns.search(line):
            hits.append({'file': p.relative_to(REPO).as_posix(), 'line': n, 'text': line,
                         'interpretation_limit': 'Historical local documentary statement; no inference of present journal status'})
csvout('submission_documentary_search.csv', hits)

report_names = [
    'INDEPENDENT_PACKAGE_AUDIT.md', 'MATHEMATICAL_CLAIM_VERIFICATION.md',
    'PAIRING_AND_DUALITY_CRITICAL_AUDIT.md', 'GRAY_MAP_EVIDENCE_AUDIT.md',
    'LITERATURE_AND_NOVELTY_RECHECK.md', 'DISCREPANCY_AND_CORRECTION_REGISTER.md', 'AUTHOR_DECISION_BRIEF.md']
audit_rows = []
(E / 'audit_reports').mkdir(exist_ok=False)
for name in report_names:
    p = REPO / 'phase0_audit/independent_review' / name
    raw = p.read_bytes()
    with (E / 'audit_reports' / name).open('xb') as out: out.write(raw)
    audit_rows.append({'file': p.relative_to(REPO).as_posix(), 'bytes': len(raw), 'sha256': H(raw), 'copied_verbatim_to': 'audit_reports/' + name})
jsonout('audit_report_inputs.json', audit_rows)
jsonout('manuscript_inventory_summary.json', {
    'recorded_clock_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'recovered_source_roots': len(roots), 'curated_mirror_roots': len(mirrors),
    'distinct_complete_core_payloads_in_recovered_roots': len({v['source_payload_sha256'] for v in versions if v['kind'].startswith('RECOVERED')}),
    'unique_main_hashes_in_recovered_roots': len({v['main_sha256'] for v in versions if v['kind'].startswith('RECOVERED')}),
    'file_inventory_rows': len(files), 'declared_binary_only_manuscript_artifacts': len(missing),
    'historical_archive_sidecar_claims': len(claims), 'documentary_markdown_files_searched': len(corpus),
    'documentary_hit_rows': len(hits), 'submission_status': 'AUTHOR CONFIRMATION REQUIRED',
    'no_editorial_receipt_verified': True,
    'latest_staged_version': next(v for v in versions if v['root'] == latest.relative_to(REPO).as_posix()),
    'canonical_version': next(v for v in versions if v['root'] == canonical.relative_to(REPO).as_posix()),
    'scope': 'Read-only local inventory and text comparison. No research runs, proof repairs, TeX compilation, external status query or manuscript edits.',
})
print(json.dumps({'recovered_source_roots': len(roots), 'audit_mirror_roots': len(mirrors),
                  'distinct_core_payloads': len({v['source_payload_sha256'] for v in versions if v['kind'].startswith('RECOVERED')}),
                  'latest_main_sha256': H((latest / 'main.tex').read_bytes()),
                  'canonical_main_sha256': H((canonical / 'main.tex').read_bytes()),
                  'binary_only_manuscript_paths': len(missing), 'doc_files_searched': len(corpus)}, indent=2))
