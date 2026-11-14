#!/usr/bin/env python3
"""Repository-specific read-only original comparison and new-review-only sealer.
No Git writes, original modifications, research execution or network activity.
All output paths are under this already authorized independent-review directory.
"""
from pathlib import Path, PurePosixPath
import ast
import collections
import csv
import datetime
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import urllib.parse
import zipfile

BASE = Path(__file__).resolve().parents[1]
REPO = BASE.parents[1]
E = BASE / 'evidence'
ORIGINAL = REPO / 'phase0_audit/PHASE0_COMPLETE_AUDIT_PACKAGE.zip'
EXPANDED = BASE / 'work/PHASE0_COMPLETE_AUDIT_PACKAGE'
EXPECTED_ORIGINAL = '350e5b9e4796d6b7798c17ce8ef047ee032e50cc4e49df0ef6e8d28ea5538c4e'
PREFIX = 'PHASE0_INDEPENDENT_REVIEW'
REPORTS = (
    'INDEPENDENT_PACKAGE_AUDIT.md',
    'MATHEMATICAL_CLAIM_VERIFICATION.md',
    'PAIRING_AND_DUALITY_CRITICAL_AUDIT.md',
    'GRAY_MAP_EVIDENCE_AUDIT.md',
    'LITERATURE_AND_NOVELTY_RECHECK.md',
    'DISCREPANCY_AND_CORRECTION_REGISTER.md',
    'AUTHOR_DECISION_BRIEF.md',
)
ALLOWED = {
    'VERIFIED', 'VERIFIED UNDER CONDITIONS', 'COMPUTATIONALLY SUPPORTED ONLY',
    'INCOMPLETE', 'INCORRECT', 'UNVERIFIABLE',
}
H = lambda b: hashlib.sha256(b).hexdigest()


def check(ok, message):
    if not ok:
        raise ValueError(message)


def git(*args):
    return subprocess.check_output(['git', '--no-optional-locks', *args], cwd=REPO, text=True).strip()


def write_json(path, value):
    with path.open('x', encoding='utf8') as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write('\n')


def write_csv(path, rows):
    with path.open('x', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    outputs = [E / 'final_original_preservation.json', E / 'final_original_file_comparison.csv',
               E / 'final_review_validation.json', E / 'final_review_links.csv',
               E / 'claim_classification_index.csv', E / 'manuscript_variant_comparison.diff',
               E / 'manuscript_variant_comparison.json', E / 'input/PHASE0_COMPLETE_AUDIT_PACKAGE.zip',
               BASE / 'SHA256SUMS.txt', BASE / (PREFIX + '.zip'), BASE / (PREFIX + '.zip.sha256')]
    check(all(not p.exists() for p in outputs), 'Sealed output already exists; do not overwrite the delivery')
    check(BASE == REPO / 'phase0_audit/independent_review', 'Unexpected repository/review layout')
    snapshot_file = E / 'pre_review_snapshot.json'
    snapshot = json.loads(snapshot_file.read_text())
    original_rows = snapshot['files']
    check(len(original_rows) == 1487 and sum(r['bytes'] for r in original_rows) == 71459327, 'Baseline census differs')
    check(git('branch', '--show-current') == snapshot['branch'] == 'arena/7d88376d-matrix-ring', 'Branch changed')
    check(git('rev-parse', 'HEAD') == snapshot['head'] == '168ec3e0b860cbe086ccb7a92a1a1aac5f8a277b', 'HEAD changed')
    subprocess.run(['git', '--no-optional-locks', 'diff', '--quiet', 'HEAD', '--'], cwd=REPO, check=True)
    comparisons = []
    for row in original_rows:
        path = REPO / row['path']
        exists = path.is_file()
        raw = path.read_bytes() if exists else b''
        same = exists and len(raw) == row['bytes'] and H(raw) == row['sha256']
        comparisons.append({'path': row['path'], 'baseline_bytes': row['bytes'], 'current_bytes': len(raw) if exists else '',
                            'baseline_sha256': row['sha256'], 'current_sha256': H(raw) if exists else '', 'status': 'UNCHANGED' if same else 'CHANGED_OR_MISSING'})
    check(all(r['status'] == 'UNCHANGED' for r in comparisons), 'An original file changed or is missing')
    baseline_names = {r['path'] for r in original_rows}
    current_outside = set()
    for root, dirs, names in os.walk(REPO):
        path = Path(root)
        dirs[:] = [n for n in dirs if n != '.git' and path / n != BASE]
        for name in names:
            p = path / name
            if p.is_file():
                current_outside.add(p.relative_to(REPO).as_posix())
    unexpected = sorted(current_outside - baseline_names)
    check(not unexpected and not (baseline_names - current_outside), 'Addition/deletion outside authorized review directory')
    original_raw = ORIGINAL.read_bytes()
    check(H(original_raw) == EXPECTED_ORIGINAL, 'Original input ZIP differs')
    with zipfile.ZipFile(io.BytesIO(original_raw)) as z:
        check(z.testzip() is None, 'Original ZIP CRC failed at sealing')
        members = [i for i in z.infolist() if not i.is_dir()]
        check(len(members) == 211, 'Original member census differs')
        for info in members:
            rel = PurePosixPath(info.filename).relative_to('PHASE0_COMPLETE_AUDIT_PACKAGE').as_posix()
            check((EXPANDED / rel).read_bytes() == z.read(info.filename), 'Expanded source changed: ' + rel)
    source_paths = [
        'mathematical_evidence/prior_project/03_THEOREMS/PAIRING_COMPLETE_PROOFS.md',
        'mathematical_evidence/prior_project/03_THEOREMS/PHASE2_STAGE2A_MORITA_GENERATORS.md',
        'mathematical_evidence/prior_project/03_THEOREMS/PHASE2_STAGE2B_CRT_PRINCIPALITY.md',
        'mathematical_evidence/prior_project/03_THEOREMS/PHASE3_STAGE3B_GALOIS_HULL_ENUMERATION.md',
        'mathematical_evidence/prior_project/03_THEOREMS/PHASE4_GRAY_MAP_COMPATIBILITY.md',
        'mathematical_evidence/prior_project/06_AUDIT/PHASE0_FINAL_NOVELTY_STATEMENT.md',
        'mathematical_evidence/prior_project/06_AUDIT/PHASE0_PROOF_VERIFICATION.md',
        'mathematical_evidence/prior_project/06_AUDIT/PHASE0_U8_U9_DECISIONS.md',
        'computational_evidence/prior_project/PHASE16_CERTIFICATION_DOCUMENTATION/PHASE16_CERTIFICATION_METHOD_AUDIT.md',
        'computational_evidence/prior_project/PHASE17_RESEARCHER_DECISION/PHASE17_CERTIFICATION_LOGIC.md',
        'repository_integrity/prior_work/PAPER/SUPPLEMENTARY_V2/SUPPLEMENTARY_CORRECTION_NOTE.md',
        'repository_integrity/prior_work/PAPER/references.bib',
        'computational_evidence/research-data/scripts/phase5_quantum_constructions.py',
        'computational_evidence/research-data/scripts/phase6_quantum_parameter_enhancement.py',
        'computational_evidence/research-data/scripts/phase7_extended_search.py',
    ]
    for p in source_paths:
        check((EXPANDED / p).is_file(), 'Wrong source locator in review: ' + p)
    # Report names, readable syntax and exact classification vocabulary.
    texts = {}
    for name in REPORTS + ('REPRODUCTION_NOTES.md',):
        text = (BASE / name).read_text(encoding='utf8')
        check(text.startswith('#') and '\ufffd' not in text, 'Unreadable report: ' + name)
        check('2026-11-13' in text or name == 'REPRODUCTION_NOTES.md', 'Audit date missing: ' + name)
        # Each contiguous table must retain consistent unescaped column counts.
        columns = None
        for line in text.splitlines():
            if line.startswith('|'):
                count = len(re.findall(r'(?<!\\)\|', line))
                if columns is None:
                    columns = count
                check(count == columns, 'Malformed Markdown table in ' + name + ': ' + line)
            else:
                columns = None
        texts[name] = text
    claim_rows = []
    for line in texts['MATHEMATICAL_CLAIM_VERIFICATION.md'].splitlines():
        if not re.match(r'^\|\s*(?:[FDGQ]\d{2}|N\d{1,2})\s*\|', line):
            continue
        cells = [s.strip() for s in line.strip('|').split('|')]
        match = re.findall(r'\*\*([^*]+)\*\*', line)
        categories = [s for s in match if s in ALLOWED]
        check(len(categories) == 1, 'Missing/ambiguous classification: ' + line)
        claim_rows.append({'claim_id': cells[0], 'statement_and_scope': cells[1], 'classification': categories[0], 'evidence_and_conditions': cells[1] if cells[0].startswith('N') else cells[3]})
    expected_ids = {'F%02d' % n for n in range(1, 12)} | {'D%02d' % n for n in range(1, 22)} | {'G%02d' % n for n in range(1, 18)} | {'Q%02d' % n for n in range(1, 24)} | {'N%d' % n for n in range(1, 13)}
    check(len(claim_rows) == 84 and {r['claim_id'] for r in claim_rows} == expected_ids, 'Claim ledger ID closure failed')
    corrections = re.findall(r'^\| (CR\d{2})\b', texts['DISCREPANCY_AND_CORRECTION_REGISTER.md'], re.M)
    check(corrections == ['CR%02d' % n for n in range(1, 44)], 'Correction register ID closure failed')
    for script in (BASE / 'scripts').glob('*.py'):
        ast.parse(script.read_text(), filename=str(script))
    for name, length in [('independent_core_checks.json', 17), ('critical_followup_checks.json', 7), ('remaining_scope_checks.json', 5)]:
        checks = json.loads((E / name).read_text())
        check(len(checks) == length and all(r['assertion_verified'] for r in checks), 'Failed/missing focused evidence: ' + name)
    records = json.loads((E / 'independent_28_code_checks.json').read_text())
    check(len(records) == 28 and all(r['all_checks_pass'] for r in records), '28-code evidence differs')
    check(collections.Counter(r['route'] for r in records) == {'EA': 25, 'SO': 2, 'DC': 1}, 'Route counts differ')
    runs = json.loads((E / 'included_source_run_summary.json').read_text())
    check(len(runs) == 3 and all(r['state'] == 'COMPLETED' and r['exit_code'] == 0 for r in runs), 'Source rerun evidence differs')
    generated = next(r for r in runs if r['name'] == 'generator_reconstruction')['generator_comparisons']
    check(len(generated) == 29 and all(r['byte_equal'] for r in generated), 'Generator byte comparison failed')
    check(H((E / 'gray_full_rerun__phase4_gray_map_log.txt').read_bytes()) == '55656a9da040df99e0d577ecb4f22c079bf9abd7b377c98eace31bca107c9a92', 'Gray log identity differs')
    check(json.loads((E / 'package_checks_v2/independent_package_checks.json').read_text())['errors'] == [], 'Authoritative package check has errors')
    check(json.loads((E / 'supporting_checks_v2/supporting_file_checks.json').read_text())['all_checks_pass'], 'Authoritative readability check failed')
    # Link destinations may include the sealing evidence about to be written.
    planned = {p.relative_to(BASE).as_posix() for p in outputs}
    links = []
    for name, text in texts.items():
        for mat in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]*?)\)', text):
            target = mat.group(1).strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                links.append({'file': name, 'line': text[:mat.start()].count('\n') + 1, 'target': target, 'status': 'EXTERNAL_SOURCE_ATTRIBUTION_NOT_REFETCHED'})
                continue
            path, _, fragment = target.partition('#')
            path = urllib.parse.unquote(path) or name
            check(not fragment and not PurePosixPath(path).is_absolute() and '..' not in PurePosixPath(path).parts, 'Unsafe/unchecked review link: ' + target)
            check((BASE / path).is_file() or path in planned, 'Broken review link: ' + name + ' -> ' + target)
            links.append({'file': name, 'line': text[:mat.start()].count('\n') + 1, 'target': target, 'status': 'LOCAL_DESTINATION_VERIFIED'})
    preservation = {
        'checked_clock_utc': timestamp,
        'baseline_snapshot_sha256': H(snapshot_file.read_bytes()),
        'baseline_capture_clock_utc': snapshot['capture_clock_utc'],
        'baseline_review_date_field': snapshot['review_date'],
        'date_field_discrepancy': 'Copied review_date is one day before recorded capture; preserved and disclosed, not corrected in source evidence.',
        'baseline_files': len(comparisons), 'baseline_bytes': sum(r['bytes'] for r in original_rows),
        'unchanged_files': len(comparisons), 'all_originals_unchanged': True,
        'changed_or_missing': [], 'unexpected_additions_outside_review': unexpected,
        'branch': snapshot['branch'], 'head': snapshot['head'], 'tracked_diff_from_HEAD': False,
        'git_writes_commits_pushes_performed_by_sealer': False,
        'scope': 'Every baseline regular file rehashed; .git excluded from content census but branch/HEAD and tracked diff checked. New files limited to phase0_audit/independent_review/.',
    }
    variants = []
    diffs = []
    paper = EXPANDED / 'repository_integrity/prior_work/PAPER'
    for section in ['07_quantum.tex', '08_certification.tex']:
        canonical = paper / 'sections' / section
        staged = paper / 'FFA_FINAL_SUBMISSION_V2/sections' / section
        a, b = canonical.read_bytes(), staged.read_bytes()
        variants.append({'section': section, 'canonical_sha256': H(a), 'staged_sha256': H(b), 'same_bytes': a == b})
        diffs.extend(difflib.unified_diff(a.decode().splitlines(), b.decode().splitlines(), fromfile='canonical/sections/' + section, tofile='FFA_FINAL_SUBMISSION_V2/sections/' + section, n=3))
    validation = {
        'checked_clock_utc': timestamp, 'status': 'PASS', 'required_reports': list(REPORTS),
        'report_readability_and_table_syntax': 'PASS',
        'report_sha256': {name: H((BASE / name).read_bytes()) for name in REPORTS},
        'classified_claim_entries_including_historical_N_map': len(claim_rows),
        'classification_counts': dict(collections.Counter(r['classification'] for r in claim_rows)),
        'correction_register_main_entries': len(corrections), 'auditor_self_disclosures': ['A01', 'A02', 'A03', 'A04'],
        'new_review_local_links': sum(r['status'] == 'LOCAL_DESTINATION_VERIFIED' for r in links),
        'new_review_external_attribution_links': sum(r['status'] != 'LOCAL_DESTINATION_VERIFIED' for r in links),
        'source_locator_paths_verified': source_paths,
        'independent_focused_assertions': 29, 'independent_code_records': 28,
        'source_reruns_exit0': 3, 'generator_records_plus_index_byte_identical': 29,
        'expanded_original_files_byte_matched': 211,
        'all_baseline_original_files_preserved': True, 'scientific_decision': 'HOLD',
        'limits': ['No TeX compilation', 'Qualified historical reference closure', 'Bounded external literature/metadata review', 'Not independent recertification of all historical search outputs', 'No implementation of manuscript corrections or new research'],
    }
    # All validations above precede output creation. Outputs below are exclusive.
    (E / 'input').mkdir(exist_ok=False)
    with (E / 'input/PHASE0_COMPLETE_AUDIT_PACKAGE.zip').open('xb') as f:
        f.write(original_raw)
    write_csv(E / 'final_original_file_comparison.csv', comparisons)
    write_json(E / 'final_original_preservation.json', preservation)
    write_csv(E / 'claim_classification_index.csv', claim_rows)
    write_csv(E / 'final_review_links.csv', links)
    with (E / 'manuscript_variant_comparison.diff').open('x', encoding='utf8') as f:
        f.write('\n'.join(diffs) + '\n')
    write_json(E / 'manuscript_variant_comparison.json', variants)
    write_json(E / 'final_review_validation.json', validation)
    payload = [p for p in BASE.iterdir() if p.is_file() and p.suffix == '.md']
    payload += [p for p in (BASE / 'scripts').rglob('*') if p.is_file()]
    payload += [p for p in E.rglob('*') if p.is_file()]
    payload += [p for p in EXPANDED.rglob('*') if p.is_file()]
    payload = sorted(payload, key=lambda p: p.relative_to(BASE).as_posix())
    check(len(payload) == len(set(payload)), 'Duplicate payload selection')
    with (BASE / 'SHA256SUMS.txt').open('x', encoding='utf8') as f:
        for p in payload:
            f.write(H(p.read_bytes()) + '  ' + p.relative_to(BASE).as_posix() + '\n')
    payload.append(BASE / 'SHA256SUMS.txt')
    archive = BASE / (PREFIX + '.zip')
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in payload:
            z.write(p, PREFIX + '/' + p.relative_to(BASE).as_posix())
    digest = H(archive.read_bytes())
    with (BASE / (PREFIX + '.zip.sha256')).open('x', encoding='ascii') as f:
        f.write(digest + '  ' + archive.name + '\n')
    print(json.dumps({'status': 'PASS', 'originals_unchanged': len(comparisons), 'original_bytes': sum(r['bytes'] for r in original_rows),
                      'classified_claim_entries': len(claim_rows), 'local_review_links': validation['new_review_local_links'],
                      'archive': str(archive), 'regular_files': len(payload), 'manifest_entries': len(payload) - 1,
                      'archive_bytes': archive.stat().st_size, 'archive_sha256': digest, 'scientific_decision': 'HOLD'}, indent=2))


if __name__ == '__main__':
    main()
