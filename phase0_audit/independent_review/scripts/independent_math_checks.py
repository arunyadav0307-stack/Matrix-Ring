#!/usr/bin/env python3
"""Independent small-case audit and recertification of supplied examples.
No project arithmetic, pairing, hull or distance implementation is imported.
Polynomial bases are explicitly stated; existing examples only, no new code search.
"""
from pathlib import Path
from itertools import product, combinations
import csv
import json
import random
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'work/PHASE0_COMPLETE_AUDIT_PACKAGE/computational_evidence/research-data'

class F:
    def __init__(self,q,encoding='records'):
        self.q=q
        self.p,self.m={2:(2,1),4:(2,2),8:(2,3),9:(3,2)}[q]
        # Records use ring_structure_checks.Field, NOT the identically coded
        # elements in the older matrix_ring_lib.FiniteField at q=8,9.
        self.poly={2:(0,),4:(1,1),8:(1,1,0),9:(1,0)}[q]
        if encoding=='early':self.poly={2:(0,),4:(1,1),8:(1,0,1),9:(2,1)}[q]
        self.add=[[self.enc([(x+y)%self.p for x,y in zip(self.dig(a),self.dig(b))]) for b in range(q)] for a in range(q)]
        self.neg=[self.enc([(-x)%self.p for x in self.dig(a)]) for a in range(q)]
        self.sub=[[self.add[a][self.neg[b]] for b in range(q)] for a in range(q)]
        self.mul=[[self.rawmul(a,b) for b in range(q)] for a in range(q)]
        self.inv=[0]+[next(b for b in range(1,q) if self.mul[a][b]==1) for a in range(1,q)]
    def dig(self,a):return [(a//self.p**i)%self.p for i in range(self.m)]
    def enc(self,x):return sum(a*self.p**i for i,a in enumerate(x))
    def rawmul(self,a,b):
        d=[0]*(2*self.m-1)
        for i,x in enumerate(self.dig(a)):
            for j,y in enumerate(self.dig(b)):d[i+j]=(d[i+j]+x*y)%self.p
        for i in range(2*self.m-2,self.m-1,-1):
            c=d[i]
            for j,v in enumerate(self.poly):d[i-self.m+j]=(d[i-self.m+j]-c*v)%self.p
        return self.enc(d[:self.m])
    def power(self,a,n):
        out=1
        while n:
            if n&1:out=self.mul[out][a]
            a=self.mul[a][a];n//=2
        return out
    def sig(self,a,k):return self.power(a,self.p**(k%self.m))
    def dot(self,a,b):
        out=0
        for x,y in zip(a,b):out=self.add[out][self.mul[x][y]]
        return out

def rr(F,rows,n):
    rows=[list(x) for x in rows if any(x)];piv=[];r=0
    for j in range(n):
        k=next((i for i in range(r,len(rows)) if rows[i][j]),None)
        if k is None:continue
        rows[r],rows[k]=rows[k],rows[r]
        rows[r]=[F.mul[F.inv[rows[r][j]]][x] for x in rows[r]]
        for i in range(len(rows)):
            if i!=r and rows[i][j]:
                a=rows[i][j];rows[i]=[F.sub[x][F.mul[a][y]] for x,y in zip(rows[i],rows[r])]
        piv.append(j);r+=1
        if r==len(rows):break
    return rows[:r],piv

def ker(F,rows,n):
    R,p=rr(F,rows,n);out=[]
    for j in range(n):
        if j not in p:
            x=[0]*n;x[j]=1
            for i,k in enumerate(p):x[k]=F.neg[R[i][j]]
            out.append(x)
    return out

def key(F,rows,n):return tuple(tuple(r) for r in rr(F,rows,n)[0])
def has(F,R,p,v):
    v=list(v)
    for row,j in zip(R,p):
        if v[j]:
            a=v[j];v=[F.sub[x][F.mul[a][y]] for x,y in zip(v,row)]
    return not any(v)

def span_elements(F,rows,n):
    R,_=rr(F,rows,n)
    for cs in product(range(F.q),repeat=len(R)):
        v=[0]*n
        for c,row in zip(cs,R):
            if c:v=[F.add[x][F.mul[c][y]] for x,y in zip(v,row)]
        yield v

def mm(F,A,B):return [[F.dot(row,col) for col in zip(*B)] for row in A]
def trans(A):return list(map(list,zip(*A)))
def ident(n):return [[int(i==j) for j in range(n)] for i in range(n)]
def matmul2(F,a,b):
    return [F.add[F.mul[a[2*i]][b[j]]][F.mul[a[2*i+1]][b[2+j]]] for i in range(2) for j in range(2)]
def theta(F,x,k):return [F.sig(x[j],k) for j in (0,2,1,3)]
def bp(F,x,y,k):return matmul2(F,theta(F,x,k),y)
def field_dual(F,G,n,k=0,J=None):
    if J is None:J=ident(n)
    return ker(F,mm(F,[[F.sig(x,k) for x in r] for r in G],J),n)

def localmul(F,a,b):
    t=len(a);out=[0]*t
    for i in range(t):
        for j in range(t-i):out[i+j]=F.add[out[i+j]][F.mul[a[i]][b[j]]]
    return out

def scalar_pair_from_matrices(F,x,y,t,k):
    # Flattened as four A_t entries, no use of the claimed Gram formula.
    X=[x[i*t:(i+1)*t] for i in range(4)];Y=[y[i*t:(i+1)*t] for i in range(4)]
    T=[[F.sig(v,k) for v in X[i]] for i in (0,2,1,3)]
    Z=[]
    for i in range(2):
        for j in range(2):
            a=localmul(F,T[2*i],Y[j]);b=localmul(F,T[2*i+1],Y[2+j])
            Z.append([F.add[s][v] for s,v in zip(a,b)])
    return F.add[Z[0][-1]][Z[3][-1]]


def core_checks():
    checks=[]
    def record(name,ok,details):
        assert ok,(name,details)
        checks.append({'test':name,'assertion_verified':bool(ok),'details':details})
    for q in (2,4,8,9):
        f=F(q)
        valid=all(f.mul[a][f.inv[a]]==1 for a in range(1,q)) and all(f.sig(f.add[a][b],1)==f.add[f.sig(a,1)][f.sig(b,1)] for a in range(q) for b in range(q))
        record('independent_field_'+str(q),valid,{'p':f.p,'m':f.m,'monic_modulus_low_coefficients':f.poly,'encoding':'base-p little-endian coefficients'})
    f=F(4);e12=[0,1,0,0];e21=[0,0,1,0];I=[1,0,0,1]
    lhs=bp(f,matmul2(f,e12,e21),I,1);rhs=matmul2(f,theta(f,e12,1),bp(f,e21,I,1))
    correct=bp(f,matmul2(f,e21,e12),I,1)
    record('summary_ax_formula_counterexample',lhs!=rhs and correct==rhs,{'a':e12,'x':e21,'y':I,'B(ax,y)':lhs,'theta(a)B(x,y)':rhs,'B(xa,y)':correct})
    record('summary_matrix_unit_nondegeneracy_probe_fails',bp(f,e12,e21,1)==[0]*4 and bp(f,e12,I,1)!=[0]*4,{'x':e12,'report_probe_y':e21,'correct_probe_y':I})
    f2=F(2);mats=list(product(range(2),repeat=4));C=[[a,b,0,0] for a,b in product(range(2),repeat=2)]
    P=[y for y in mats if all(matmul2(f2,x,y)==[0]*4 for x in C)]
    D=[y for y in mats if all(bp(f2,x,y,0)==[0]*4 for x in C)]
    record('plain_pairing_nondegenerate_but_wrong_same_side_size',len(P)==1 and len(D)==4 and all(matmul2(f2,x,I)==list(x) for x in mats),{'C_size':len(C),'plain_dual_size':len(P),'theta_dual_size':len(D),'R_size':16})
    f8=F(8);a=2;G=[[1,0,a,0],[0,1,0,a]]
    D=field_dual(f8,G,4,1);DD=field_dual(f8,D,4,1)
    plus=[[f8.sig(x,2) for x in r] for r in G];minus=[[f8.sig(x,-2) for x in r] for r in G]
    brute=[list(y) for y in product(range(8),repeat=4) if all(bp(f8,g,y,1)==[0]*4 for g in G)]
    record('double_dual_positive_not_negative_direction',key(f8,DD,4)==key(f8,plus,4) and key(f8,DD,4)!=key(f8,minus,4) and key(f8,DD,4)!=key(f8,G,4) and key(f8,brute,4)==key(f8,D,4),{'q':8,'matrix_size':2,'n':1,'k':1,'G':G,'dual_basis':D,'double_dual_basis':DD,'sigma_2_G':plus,'sigma_minus_2_G':minus,'C_size':64,'dual_size':len(brute),'ambient_size':4096})
    X=[1,0,a,0];Y=[f8.neg[f8.sig(a,1)],0,1,0]
    record('nonreflexive_zero_relation_witness',bp(f8,X,Y,1)==[0]*4 and bp(f8,Y,X,1)!=[0]*4,{'X':X,'Y':Y,'B(X,Y)':bp(f8,X,Y,1),'B(Y,X)':bp(f8,Y,X,1)})
    f=F(4);u=[0,1]
    record('coefficient_lift_is_not_full_ring_power',localmul(f,u,u)==[0,0] and [f.sig(x,1) for x in u]==u,{'u':u,'u_to_power_2':localmul(f,u,u),'coefficient_lift_sigma_1_u':u})
    # Enumerate all subspaces of F4^4 in canonical RREF and keep u-stable ones.
    subs=[]
    for dim in range(5):
        for piv in combinations(range(4),dim):
            free=[(i,j) for i,p in enumerate(piv) for j in range(p+1,4) if j not in piv]
            for vals in product(range(4),repeat=len(free)):
                G=[[int(j==p) for j in range(4)] for p in piv]
                for (i,j),v in zip(free,vals):G[i][j]=v
                R,p=rr(f,G,4);UG=[[0,r[0],0,r[2]] for r in R]
                if all(has(f,R,p,v) for v in UG):subs.append({'dimension':len(R),'mu_A':len(R)-len(rr(f,UG,4)[0])})
    record('base_matrix_ring_ideals_are_principal_in_tested_case',len(subs)==33 and max(s['mu_A'] for s in subs)==2,{'A':'F4[u]/u^2','A_submodules_of_A_squared':len(subs),'max_mu_A':max(s['mu_A'] for s in subs),'dimension_counts':{str(i):sum(s['dimension']==i for s in subs) for i in range(5)},'all_33_corresponding_right_ideals_in_M2_A_principal':True})
    # Construct the specific historical nonprincipal hull in B = F4[u,w]/(u^2,w^2).
    gs=[[0,1,0,0,0,1,0,0],[0,0,1,0,0,0,1,1],[0,0,1,1,0,0,1,1]]
    def um(v):return [0,0,v[0],v[1],0,0,v[4],v[5]]
    def wm(v):return [0,v[0],0,v[2],0,v[4],0,v[6]]
    W=gs[:]
    while True:
        R,p=rr(f,W,8);S,_=rr(f,R+[um(v) for v in R]+[wm(v) for v in R],8)
        if len(S)==len(R):W=R;break
        W=S
    radW=rr(f,[um(v) for v in W]+[wm(v) for v in W],8)[0]
    code=[]
    for v in W:
        # Convert w=X+1 coordinates back to (1,X,u,uX) in each B component.
        xs=[]
        for off in (0,4):
            z=v[off:off+4];xs.append([f.add[z[0]][z[1]],z[1],f.add[z[2]][z[3]],z[3]])
        for col in (0,1):
            out=[0]*16
            for row in (0,1):
                for aa in (0,1):
                    for e in (0,1):out[(e*4+2*row+col)*2+aa]=xs[row][aa*2+e]
            code.append(out)
    J=[[int((i//2)==(j//2) and i%2+j%2==1) for j in range(16)] for i in range(16)]
    proofs=[]
    for k in (0,1):
        dual=field_dual(f,code,16,k,J)
        proofs.append({'k':k,'C_dimension':len(rr(f,code,16)[0]),'dual_dimension':len(dual),'self_dual':key(f,code,16)==key(f,dual,16)})
    record('historical_nonprincipal_selfdual_hull_witness',len(W)==4 and len(radW)==1 and all(r['self_dual'] for r in proofs),{'B':'F4[u,w]/(u^2,w^2), w=X+1','B_generators_in_1_w_u_uw_order':gs,'W_basis':W,'radical_W_basis':radW,'dim_W':len(W),'dim_radical_W':len(radW),'mu_B':len(W)-len(radW),'max_columns_of_single_2x2_generator':2,'C_basis_Gray_coordinates':code,'pairings':proofs})
    # Test trace/matrix transport, including the nilpotent top-coefficient functional.
    rng=random.Random(17031);t=2;J8=[[int(i//2==j//2 and i%2+j%2==1) for j in range(8)] for i in range(8)]
    basis=ident(8)
    ok=True
    for k in (0,1):
        for x,y in [(x,y) for x in basis for y in basis]+[([rng.randrange(4) for _ in range(8)],[rng.randrange(4) for _ in range(8)]) for _ in range(500)]:
            lhs=scalar_pair_from_matrices(f,x,y,t,k)
            rhs=f.dot([f.sig(x[i],k) for i in range(8)],[y[j^1] for j in range(8)])
            ok &= lhs==rhs
    record('Gray_Gram_independent_matrix_trace_verification',ok,{'q':4,'t':2,'N':8,'basis_pairs_per_k':64,'seeded_pairs_per_k':500,'J':J8})
    U=[[int(j==i) for j in range(8)] for i in (1,3,5,7)]
    Jh=field_dual(f,U,8,1,J8);E=field_dual(f,U,8,0)
    record('Gray_dual_not_standard_Euclidean',key(f,U,8)==key(f,Jh,8) and key(f,U,8)!=key(f,E,8),{'code':'u M2(F4[u]/u^2), n=1','C_basis':U,'transported_dual':Jh,'Euclidean_dual':E})
    T=[[1,1],[2,3]];H=[[0,1],[1,0]]
    gram=mm(f,mm(f,trans([[f.sig(x,1) for x in row] for row in T]),H),T)
    bil=mm(f,mm(f,trans(T),H),T)
    record('char2_even_t_Hermitian_congruence_counterexample',gram==ident(2) and bil!=ident(2),{'q':4,'t':2,'k':1,'alpha_encoding':2,'T':T,'sigma_T_transpose_H_T':gram,'T_transpose_H_T':bil,'scope':'Refutes an unrestricted sesquilinear obstruction, NOT the bilinear k=0 obstruction. T is not monomial; no Hamming isometry claimed.'})
    for q in (8,9):
        late=F(q);early=F(q,'early');a=2 if q==8 else 3
        power=3 if q==8 else 2
        record('field_encoding_mismatch_'+str(q),late.power(a,power)!=early.power(a,power),{'integer_element':a,'power':power,'records_modulus':late.poly,'early_matrix_ring_lib_modulus':early.poly,'records_result':late.power(a,power),'early_result':early.power(a,power)})
    return checks


def support_distance(F,G,E,n,maxw):
    H=ker(F,G,n);ER,EP=rr(F,E,n);tested=0
    for w in range(1,maxw+1):
        for S in combinations(range(n),w):
            tested+=1
            small=ker(F,[[row[i] for i in S] for row in H],w)
            for x in small:
                v=[0]*n
                for i,a in zip(S,x):v[i]=a
                if any(v) and not has(F,ER,EP,v):return sum(x!=0 for x in v),v,tested
    return None,None,tested


def enumeration_distance(F,G,E,n):
    ER,EP=rr(F,E,n);best=None;witness=None;count=0
    for v in span_elements(F,G,n):
        count+=1
        if not any(v) or has(F,ER,EP,v):continue
        w=sum(x!=0 for x in v)
        if best is None or w<best:best,witness=w,v
    return best,witness,count


def certificate_checks():
    results=[]
    for path in sorted((DATA/'generator_matrices').glob('*.json')):
        if path.name=='INDEX.json':continue
        start=time.monotonic();r=json.loads(path.read_text());f=F(r['q']);n=r['N']
        G,GP=rr(f,r['generator_matrix_A'],n);D=ker(f,G,n);published=r['generator_matrix_Euclidean_dual']
        hull_dim=len(G)+len(D)-len(rr(f,G+D,n)[0]);S=mm(f,G,trans(G));SR,SP=rr(f,S,len(G));c=len(SR)
        dual_ok=key(f,D,n)==key(f,published,n)
        cond=all(not any(row) for row in S) if r['route']=='SO' else all(has(f,G,GP,row) for row in D) if r['route']=='DC' else True
        if r['route']=='SO':K=n-2*len(G);c_used=0
        elif r['route']=='DC':K=2*len(G)-n;c_used=0
        else:K=n-len(G)-hull_dim;c_used=c
        # Numerical Bob completion of the EA CSS commutator: S = U R,
        # X_B=U, Z_B=-R^T, so Alice+Bob X/Z cross-commutators vanish.
        U=[[row[p] for p in SP] for row in S]
        completion_ok=(mm(f,U,SR)==S) if c else all(not any(row) for row in S)
        target,excluded=(G,D) if r['route']=='DC' else (D,G)
        if f.q**len(target)<=100000:
            d,wit,cnt=enumeration_distance(f,target,excluded,n);method='complete independent enumeration';unit='codewords'
        else:
            d,wit,cnt=support_distance(f,target,excluded,n,r['d']);method='complete independent parity-check support search through claimed d';unit='supports'
        all_ok=dual_ok and cond and len(G)==r['k'] and hull_dim==r['h_E'] and K==r['K'] and c_used==r['c'] and d==r['d'] and completion_ok
        result={'file':path.name,'code':r['code'],'q':r['q'],'route':r['route'],'rank':len(G),'N':n,
                'h_E':hull_dim,'K':K,'c':c_used,'dual_matrix_agrees':dual_ok,'CSS_inclusion_valid':cond,
                'EA_commutator_rank':c,'Bob_completion_commutator_cancellation':completion_ok,
                'exact_distance_recomputed':d,'claimed_distance':r['d'],'distance_method':method,
                'tested_'+unit:cnt,'distance_witness':wit,'all_checks_pass':all_ok,'elapsed_seconds':round(time.monotonic()-start,3),
                'field_modulus':f.poly,'scope':'Independent verification of supplied field generator matrices; not reconstruction of their cyclic-ring provenance.'}
        results.append(result)
        print('CERT',path.name,'PASS' if all_ok else 'FAIL','d',d,'time',result['elapsed_seconds'],flush=True)
    assert len(results)==28
    return results

if __name__=='__main__':
    start=time.monotonic()
    core=core_checks()
    for r in core:print('CORE PASS',r['test'],flush=True)
    with (ROOT/'evidence/independent_core_checks.json').open('x') as f:json.dump(core,f,indent=2);f.write('\n')
    certs=certificate_checks()
    with (ROOT/'evidence/independent_28_code_checks.json').open('x') as f:json.dump(certs,f,indent=2);f.write('\n')
    print('SUMMARY',len(core),'core checks;',sum(r['all_checks_pass'] for r in certs),'/28 code records; elapsed',round(time.monotonic()-start,3),flush=True)
    if not all(r['all_checks_pass'] for r in certs):sys.exit(1)
