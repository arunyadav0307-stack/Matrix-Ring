#!/usr/bin/env python3
"""Scope/representation checks, not new research or a code search."""
from pathlib import Path
import json,sys,shutil
import independent_math_checks as M
BASE=Path(__file__).resolve().parents[1]
checks=[]
def rec(name,ok,detail):
    assert ok,(name,detail)
    checks.append({'test':name,'assertion_verified':bool(ok),'details':detail})
f=M.F(4)
E=M.ident(4);C=[E[0]]
ring_dual=[E[2],E[3]]
scalar_dual=M.field_dual(f,C,4)
rec('scalar_orthogonal_requires_module_hypothesis',len(ring_dual)==2 and len(scalar_dual)==3,{'C':'F4 E11 in M2(F4), an F4-subspace but NOT a right R-submodule','ring_valued_dual_dimension':2,'Lambda_trace_dual_dimension':3})
N=8;basis=M.ident(N);D=[basis[i] for i in (1,3,5,7)]
J=[[int(i//2==j//2 and i%2!=j%2) for j in range(N)] for i in range(N)]
def Ts(u):return M.mm(f,[[f.sig(x,1) for x in u]],J)[0]
a=basis[0];b=basis[1]
values=[f.sub[f.dot(a,Ts(u))][f.dot(u,b)] for u in M.span_elements(f,D,N)]
rec('R1_trace_and_Fq_orthogonals_are_different',all(f.add[v][f.sig(v,1)]==0 for v in values) and any(values),{'source_code':'C=u M2(F4[u]/u^2), n=1','D_basis_indices':[1,3,5,7],'R1_graph':'(u | sigma1(u) J)','test_label_a_index':0,'test_label_b_index':1,'all_symplectic_values':sorted(set(values)),'all_absolute_traces_zero':True,'in_Fq_symplectic_orthogonal':False,'scope':'Refutes identifying the two orthogonal sets for R1; this example alone does not show different minimum distances.'})
rec('R1_not_covered_by_EA_bookkeeping_identities',N-4!=N-2*4,{'N':N,'k':4,'R1_c':0,'R1_K':N-4,'claimed_all_routes_N_minus_2k':N-2*4,'source':'PAPER/sections/08_certification.tex thm:bookkeeping'})
f2=M.F(2);H=[[1,1,0]];coset=[[0,0,1],[1,1,1]]
rec('quotient_is_not_ordinary_coordinate_Hamming_code',sorted(sum(bool(x) for x in v) for v in coset)==[1,3],{'D':'span_F2(110)','D_Euclidean_dual':'span_F2(110,001)','Hull_E':'span_F2(110)','same_nonzero_coset_representatives':coset,'representative_weights':[1,3],'coset_minimum_weight':1,'scope':'Coset-leader metric is well-defined; it is not an ordinary length-N coordinate code with representative-independent Hamming weights.'})
# Explicit reproduction of the already documented Phase-5 coordinate bug.
# Imports are disposable copies only, with bytecode disabled.
SOURCE=M.DATA/'scripts';COPY=BASE/'work/focused_source_check/scripts'
shutil.copytree(SOURCE,COPY)
sys.path.insert(0,str(COPY))
import phase3_stage3b_hull_enumeration as S
E=S.Ring3B(4,2,2);C=E.C
G=[((1,1,0,0),(1,1,0,0)),((0,0,1,0),(0,0,0,1)),((0,0,0,1),(0,0,0,1))]
W=S.mod_of(C,G)
dimH,inter,Wp,hrows=S.hull_by_morita(E,W,1)
proper=S.mod_of(C,[S.unpair(C,tuple(v)) for v in inter])
wrong=S.mod_of(C,[S.unpair(C,tuple(v)) for v in hrows])
rec('Phase5_hull_mu_coordinate_error_reproduced',dimH==8 and E.mu(proper)==3 and E.mu(wrong)==4,{'method':'Focused use of unchanged source helpers in disposable copy, NOT independent arithmetic','known_Stage3B_witness':G,'dimH':dimH,'inter_row_length':len(inter[0]),'hrows_row_length':len(hrows[0]),'proper_Morita_module_mu':E.mu(proper),'Phase5_wrong_hrows_conversion_mu':E.mu(wrong),'corrected_source_exists':'phase6_quantum_parameter_enhancement.py:hull_mu explicitly warns against using the fourth return value.'})
with (BASE/'evidence/remaining_scope_checks.json').open('x') as out:json.dump(checks,out,indent=2);out.write('\n')
for row in checks:print('PASS',row['test'])
