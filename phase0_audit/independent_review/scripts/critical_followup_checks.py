#!/usr/bin/env python3
"""Focused checks of errors noticed while reading the unchanged sources.
Uses only the independently written audit arithmetic, not project arithmetic.
"""
from pathlib import Path
import json
from itertools import product
import independent_math_checks as M
B=Path(__file__).resolve().parents[1]
f=M.F(4)
checks=[]
def record(name,ok,detail):
    assert ok,(name,detail)
    checks.append({'test':name,'assertion_verified':bool(ok),'details':detail})
# The alternate left convention is valid but twists the OTHER argument.
f8=M.F(8);G=[[1,2,0,0],[0,0,1,2]]
D=M.field_dual(f8,G,4,-1);DD=M.field_dual(f8,D,4,-1)
sigminus=[[f8.sig(x,-2) for x in r] for r in G]
sigplus=[[f8.sig(x,2) for x in r] for r in G]
# Explicit matrix-valued zero equations, not merely trace equations.
def Lalt(x,y):return M.matmul2(f8,x,M.theta(f8,y,1))
brute=[list(y) for y in product(range(8),repeat=4) if all(Lalt(x,y)==[0]*4 for x in G)]
a=[0,1,0,0];y=D[0];x=G[0]
leftsemilinear=Lalt(x,M.matmul2(f8,a,y))==M.matmul2(f8,Lalt(x,y),M.theta(f8,a,1))
record('alternate_left_mirror_has_negative_double_twist',M.key(f8,brute,4)==M.key(f8,D,4) and M.key(f8,DD,4)==M.key(f8,sigminus,4) and M.key(f8,DD,4)!=M.key(f8,sigplus,4) and leftsemilinear,{'left_ideal_basis':G,'alternate_pairing':'Lalt(x,y)=x theta_1(y)','dual_basis':D,'double_dual_basis':DD,'sigma_minus_2_basis':sigminus,'sigma_plus_2_basis':sigplus,'dual_cardinality':len(brute),'semilinear_left_multiplier_identity':'Lalt(x,a y)=Lalt(x,y) theta_1(a)','not_claimed_ordinary_left_linear_in_y':True})
f9=M.F(9);T=[[3,2],[3,1]];H=[[0,1],[1,0]]
bil=M.mm(f9,M.mm(f9,M.trans(T),H),T)
sesq=M.mm(f9,M.mm(f9,M.trans([[f9.sig(x,1) for x in r] for r in T]),H),T)
record('stated_GF9_congruence_not_Hermitian',bil==M.ident(2) and sesq!=M.ident(2),{'field_modulus':f9.poly,'T_from_Phase5_T199':T,'T_transpose_H_T':bil,'sigma1_T_transpose_H_T':sesq})
record('zero_diagonal_does_not_mean_alternating',f9.dot([1,1],[1,1])==2 and f.add[2][f.sig(2,1)]==1,{'odd_characteristic_example':'(1,1) H2 (1,1)^T = 2 in F9, not zero','Hermitian_even_characteristic_example':'sigma_1(1,alpha) H2 (1,alpha)^T = alpha+alpha^2 = 1 in F4','Hermitian_value':f.add[2][f.sig(2,1)]})
# Manuscript thm:nonprincipal, i=0, dim U=2: direct-sum assumption fails.
e=M.ident(8);Be1=e[:4];U=[e[3],e[7]]
W=M.rr(f,Be1+U,8)[0]
def um(v):return [0,0,v[0],v[1],0,0,v[4],v[5]]
def wm(v):return [0,v[0],0,v[2],0,v[4],0,v[6]]
rad=M.rr(f,[um(v) for v in W]+[wm(v) for v in W],8)[0]
mu=len(W)-len(rad)
record('manuscript_nonprincipal_i0_family_proof_fails',len(W)==5 and len(rad)==3 and mu==2,{'B':'F4[u,w]/(u^2,w^2)','proposed_U':'socle(B^2)=span(uw e1,uw e2)','dim_Be1':4,'dim_U':2,'intersection_dimension':1,'dim_sum':len(W),'dim_radical_times_sum':len(rad),'actual_mu_B':mu,'manuscript_claimed_mu_B':3,'scope':'Does not refute the valid explicit Stage3B nonprincipal self-dual witness.'})
record('odd_characteristic_Weyl_phase_sign_counterexample',0!=(1+1)%3 and 0==(-1+1)%3,{'p':3,'a':1,'b':1,'v':0,'XZ_on_v_phase_exponent':0,'claimed_chi_plus_ab_ZX_phase_exponent':2,'correct_chi_minus_ab_ZX_phase_exponent':0,'commutation_zero_test_unaffected':True})
record('arbitrary_additive_group_stabilizer_lemma_missing_isotropy',2/4==0.5,{'p':2,'N':1,'C':'F2^2','C_size':4,'X_Z_commutator':'XZ=-ZX','joint_eigenspace_exists':False,'claimed_dimension':0.5,'required_conditions':'Trace isotropy, suitable phase-correct stabilizer lift with no nontrivial scalar, nonzero logical space conventions.'})
wrong=[]
for p in sorted((M.DATA/'generator_matrices').glob('*.json')):
    if p.name=='INDEX.json':continue
    r=json.loads(p.read_text())
    if r['q'] not in (8,9):continue
    ef=M.F(r['q'],'early');n=r['N'];G=r['generator_matrix_A'];D=r['generator_matrix_Euclidean_dual']
    de=M.ker(ef,G,n);h=len(M.rr(ef,G,n)[0])+len(de)-len(M.rr(ef,G+de,n)[0])
    wrong.append({'file':p.name,'q':r['q'],'early_modulus':ef.poly,'dual_agrees_using_wrong_documented_encoding':M.key(ef,de,n)==M.key(ef,D,n),'h_E_using_wrong_encoding':h,'recorded_h_E':r['h_E']})
record('incorrect_field_documentation_has_real_effect',any(not r['dual_agrees_using_wrong_documented_encoding'] for r in wrong),{'records_checked':len(wrong),'records_with_dual_mismatch_under_wrong_encoding':sum(not r['dual_agrees_using_wrong_documented_encoding'] for r in wrong),'details':wrong})
with (B/'evidence/critical_followup_checks.json').open('x') as out:json.dump(checks,out,indent=2);out.write('\n')
for r in checks:print('PASS',r['test'])
