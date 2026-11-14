#!/usr/bin/env python3
"""Read-only portable integrity verifier. Does not execute research or fetch URLs."""
from pathlib import Path, PurePosixPath
import collections
import hashlib
import io
import json
import re
import sys
import urllib.parse
import zipfile

PREFIX = 'PHASE0_INDEPENDENT_REVIEW'
ORIGINAL_SHA = '350e5b9e4796d6b7798c17ce8ef047ee032e50cc4e49df0ef6e8d28ea5538c4e'
REPORTS = (
    'INDEPENDENT_PACKAGE_AUDIT.md',
    'MATHEMATICAL_CLAIM_VERIFICATION.md',
    'PAIRING_AND_DUALITY_CRITICAL_AUDIT.md',
    'GRAY_MAP_EVIDENCE_AUDIT.md',
    'LITERATURE_AND_NOVELTY_RECHECK.md',
    'DISCREPANCY_AND_CORRECTION_REGISTER.md',
    'AUTHOR_DECISION_BRIEF.md',
)
H = lambda b: hashlib.sha256(b).hexdigest()


def safe(name):
    p = PurePosixPath(name)
    return bool(p.parts) and not p.is_absolute() and '..' not in p.parts and '\\' not in name


def check(ok, message):
    if not ok:
        raise ValueError(message)


def manifest_entries(text):
    result = {}
    for line in text.splitlines():
        digest, name = line.split('  ', 1)
        check(bool(re.fullmatch(r'[0-9a-f]{64}', digest)), 'Invalid manifest digest')
        check(safe(name) and name not in result, 'Invalid or duplicate manifest path: ' + name)
        result[name] = digest
    return result


def main():
    archive = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1] / (PREFIX + '.zip')
    raw = archive.read_bytes()
    archive_sha = H(raw)
    sidecar = archive.with_name(archive.name + '.sha256')
    sidecar_status = 'NOT_PROVIDED'
    if sidecar.exists():
        expected, filename = sidecar.read_text().strip().split('  ', 1)
        check(filename == archive.name and expected == archive_sha, 'External SHA-256 mismatch')
        sidecar_status = 'PASS'
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos = z.infolist()
        check(all(not i.is_dir() for i in infos), 'Unexpected directory entry')
        fullnames = [i.filename for i in infos]
        check(len(fullnames) == len(set(fullnames)), 'Duplicate review archive members')
        check(all(safe(n) and PurePosixPath(n).parts[0] == PREFIX for n in fullnames), 'Unsafe review paths')
        check(z.testzip() is None, 'Review archive CRC failure')
        files = {PurePosixPath(n).relative_to(PREFIX).as_posix(): z.read(n) for n in fullnames}
        manifest = manifest_entries(files['SHA256SUMS.txt'].decode('utf8'))
        check(set(files) == set(manifest) | {'SHA256SUMS.txt'}, 'Review manifest coverage differs')
        for name, digest in manifest.items():
            check(H(files[name]) == digest, 'Review payload SHA mismatch: ' + name)
        for name in REPORTS:
            check(name in files and files[name].decode('utf8').startswith('#'), 'Missing/unreadable report: ' + name)
        nested_raw = files['evidence/input/PHASE0_COMPLETE_AUDIT_PACKAGE.zip']
        check(H(nested_raw) == ORIGINAL_SHA, 'Nested original archive identity mismatch')
        with zipfile.ZipFile(io.BytesIO(nested_raw)) as original:
            check(original.testzip() is None, 'Nested original archive CRC failure')
            oi = [i for i in original.infolist() if not i.is_dir()]
            original_names = [i.filename for i in oi]
            check(len(oi) == 211 and len(original_names) == len(set(original_names)), 'Original archive file census mismatch')
            original_files = {}
            for info in oi:
                check(safe(info.filename) and PurePosixPath(info.filename).parts[0] == 'PHASE0_COMPLETE_AUDIT_PACKAGE', 'Unsafe nested original name')
                rel = PurePosixPath(info.filename).relative_to('PHASE0_COMPLETE_AUDIT_PACKAGE').as_posix()
                original_files[rel] = original.read(info.filename)
                check(files['work/PHASE0_COMPLETE_AUDIT_PACKAGE/' + rel] == original_files[rel], 'Expanded source differs: ' + rel)
            expanded = {n.removeprefix('work/PHASE0_COMPLETE_AUDIT_PACKAGE/') for n in files if n.startswith('work/PHASE0_COMPLETE_AUDIT_PACKAGE/')}
            check(expanded == set(original_files), 'Extra or absent expanded original source')
            old_manifest = manifest_entries(original_files['SHA256SUMS.txt'].decode('utf8'))
            check(len(old_manifest) == 210 and set(original_files) == set(old_manifest) | {'SHA256SUMS.txt'}, 'Original manifest coverage mismatch')
            check(all(H(original_files[n]) == d for n, d in old_manifest.items()), 'Original internal hash failure')
        links = []
        for name, data in files.items():
            if '/' in name or not name.endswith('.md'):
                continue
            text = data.decode('utf8')
            for mat in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^\n]*?)\)', text):
                target = mat.group(1).strip().strip('<>')
                if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                path, _, fragment = target.partition('#')
                path = urllib.parse.unquote(path)
                dest = path if path else name
                check(safe(dest) and dest in files, 'Unresolved new review link: ' + name + ' -> ' + target)
                # New review links currently use no fragment identifiers.
                check(not fragment, 'Fragment requires explicit validator extension: ' + target)
                links.append((name, target))
        preservation = json.loads(files['evidence/final_original_preservation.json'])
        check(preservation['all_originals_unchanged'] is True, 'Preservation evidence is not PASS')
        check(preservation['baseline_files'] == preservation['unchanged_files'] == 1487, 'Original-file census differs')
        validation = json.loads(files['evidence/final_review_validation.json'])
        check(validation['status'] == 'PASS', 'Review delivery validation is not PASS')
        result = {
            'status': 'PASS',
            'archive': archive.name,
            'archive_sha256': archive_sha,
            'compressed_bytes': len(raw),
            'regular_files': len(files),
            'uncompressed_bytes': sum(len(b) for b in files.values()),
            'manifest_entries': len(manifest),
            'external_sha256_sidecar': sidecar_status,
            'required_reports': len(REPORTS),
            'new_review_local_links_verified': len(links),
            'nested_original_zip_sha256': ORIGINAL_SHA,
            'nested_original_files': len(original_files),
            'nested_original_internal_hashes': len(old_manifest),
            'expanded_original_byte_matches': len(original_files),
            'preservation_evidence': '1487/1487 original files unchanged; recorded evidence, not a fresh remote-filesystem comparison',
            'research_executed_by_this_verifier': False,
            'scientific_decision': 'HOLD',
            'scope': 'Integrity and delivery-reference checks only; not independent proof certification or digital signature of original authorship.',
        }
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('FAIL:', error, file=sys.stderr)
        sys.exit(1)
