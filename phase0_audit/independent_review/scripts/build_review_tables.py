#!/usr/bin/env python3
"""Build reviewer navigation tables from already captured audit evidence."""
from pathlib import Path
import csv,json,collections,difflib
B=Path(__file__).resolve().parents[1];E=B/'evidence';P=B/'work/PHASE0_COMPLETE_AUDIT_PACKAGE'

def outcsv(name,rows):
    with (E/name).open('x',newline='',encoding='utf8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

inventory=list(csv.DictReader((E/'package_checks_v2/independent_bibliography_inventory.csv').open()))
source_map={
'Alahmadi2013CyclicM2F2':('L14a,L14b,L09','PRIMARY_METADATA','10.1016/j.jfranklin.2013.06.023','Manuscript .008 DOI is unrelated; repository uses arXiv DOI.'),
'LuoParampalli2018M2F2uF2':('L09','PRIMARY_METADATA','10.1007/s12095-017-0266-1','10, 1109-1117 (2018); pending large-bibliography pages now supported.'),
'Dinh2024CyclicRingsOfMatrices':('L08','PRIMARY_METADATA','10.3934/amc.2022073','18(4),1100-1122(2024); online 2022.'),
'SiNiu2023SkewM2F2':('L21a','PRIMARY_METADATA','10.3934/math.20231246','Metadata/abstract checked, not full proof.'),
'DuNiu2025WeightSkewM2F2':('L21b','PUBLISHER_SEARCH_ONLY','10.3934/math.2025520','Title/volume/pages/DOI corroborated by publisher search result; not full page.'),
'JoshiPatelPrakash2026M4':('L11','PRIMARY_METADATA','10.48550/arXiv.2602.18255','Preprint; no journal DOI verified.'),
'OggierEtAlSpaceTimeMatrixRings':('L19','PRIMARY_METADATA','10.1109/TIT.2011.2173732','Same-title record is Oggier-Sole-Belfiore, 2012,58(2),734-746; original 2010 author list defective.'),
'Wood1999Duality':('L20','PRIMARY_METADATA','10.1353/ajm.1999.0024','Frobenius-ring foundation, not priority for specialization.'),
'FanZhang2017GaloisSelfDual':('L06','PRIMARY_METADATA','10.1007/s10623-016-0282-8','Volume84; original six-report matrix says85, BibTeX says84.'),
'LiuPan2020GaloisHulls':('L07','PRIMARY_METADATA','10.1007/s10623-019-00681-2','Missing DOI in originals.'),
'Cao2021MDSGaloisHulls':('L15','PRIMARY_METADATA','10.1109/TIT.2021.3117562','Missing DOI in originals.'),
'ZhangKongZheng2026QuantumGaloisHulls':('L02','PRIMARY_METADATA','10.3390/e28040407','Commutative-ring nearest neighbour.'),
'DebnathEtAl2024AffineAlgebraGaloisHulls':('L13','PRIMARY_METADATA','10.1016/j.disc.2025.114750','Journal349(2),114750(2026); preprint2024 retained as provenance.'),
'PereiraMancini2023EAQECCyclic':('L16','PRIMARY_METADATA','10.3390/e25010037','2023 issue, online2022.'),
'KetkarEtAl2006NonbinaryStabilizer':('L17','PRIMARY_METADATA_WITH_UNIVERSITY_CORROBORATION','10.1109/TIT.2006.883612','First author Avanti, not Andreas. Registry has initials; university record corroborates identity.'),
'GrasslCodeTables':('B01-B07','PRIMARY_ENDPOINT_CHECK','not applicable','Duplicate-theme key; metadata and physical-alphabet semantics need explicit retrieval dates.'),
'GrasslCodetables':('B01-B07','PRIMARY_ENDPOINT_CHECK','not applicable','Legacy q is construction alphabet, not physical dimension; EA tables exist.'),
'GreferathSchmidt1999GrayIsometry':('L18','PRIMARY_METADATA','10.1109/18.796395','Use S.E.Schmidt; manuscript Sergio R. not supported.'),
'NebeRainsSloaneAntiIsomorphism':('L03,L04','PLACEHOLDER_NOT_A_VERIFIED_CITATION','','Related real sources located: NRS2006 book; Wood2010 article; Szabo-Wood2017. Do not invent identity for the placeholder title.')}
rows=[]
for r in inventory:
    info=source_map.get(r['key'],('','NOT_FRESHLY_REVERIFIED','','Historical provenance only. No independently verified label inferred.'))
    rows.append({'file':r['file'],'key':r['key'],'original_doi':r['doi_field'],'fresh_evidence_ids':info[0],'fresh_scope':info[1],'supported_doi':info[2],'correction_or_limit':info[3]})
outcsv('bibliography_recheck_by_entry.csv',rows)

records=json.loads((E/'independent_28_code_checks.json').read_text())
ct=[]
for i,r in enumerate(records,1):
    ct.append({'row':i,'file':r['file'],'code':r['code'],'q':r['q'],'route':r['route'],'N':r['N'],'rank_k':r['rank'],'h_E':r['h_E'],'K':r['K'],'c':r['c'],'exact_d':r['exact_distance_recomputed'],'independent_method':r['distance_method'],'matrix_dual_agrees':r['dual_matrix_agrees'],'CSS_route_condition':r['CSS_inclusion_valid'],'all_checks_pass':r['all_checks_pass']})
outcsv('independent_28_code_summary.csv',ct)
refs=list(csv.DictReader((P/'repository_integrity/reference_resolution.csv').open()))
outcsv('reference_exceptions_for_review.csv',[r for r in refs if r['status'] not in ('PACKAGED','PACKAGED_ALIAS','PACKAGED_MULTIPLE')])
a=(P/'computational_evidence/research-data/logs/phase0_results.txt').read_text().splitlines()
b=(E/'phase0_rerun__phase0_results.txt').read_text().splitlines()
with (E/'phase0_rerun_vs_archived.diff').open('x') as f:f.write('\n'.join(difflib.unified_diff(a,b,fromfile='archived phase0 log',tofile='independent-review historical-source rerun',n=2))+'\n')
dc=next(r for r in records if r['route']=='DC')
scope={'DC_counterexample_to_unqualified_EA_bookkeeping_and_coset_theorem':{'record':dc['file'],'N':dc['N'],'k_original_D':dc['rank'],'h_E':dc['h_E'],'actual_CSS_K':dc['K'],'actual_CSS_c':0,'EA_N_minus_k_minus_h':dc['N']-dc['rank']-dc['h_E'],'dimension_Ddual_mod_H':dc['N']-dc['rank']-dc['h_E'],'proper_DC_distance':'min wt(D minus Ddual), not min wt(Ddual minus Hull_E(D))','actual_exact_d':dc['exact_distance_recomputed'],'K_minus_c':dc['K'],'N_minus_2k_original_D':dc['N']-2*dc['rank'],'scope':'Arithmetic/scope diagnosis of a supplied record, not a new construction.'},'bibliography_scope_counts':dict(collections.Counter(r['fresh_scope'] for r in rows))}
with (E/'route_and_bibliography_scope.json').open('x') as f:json.dump(scope,f,indent=2);f.write('\n')
print('50 bibliography occurrences, 28 code summary rows, reference exception table, Phase0 diff, and DC-scope evidence written.')
