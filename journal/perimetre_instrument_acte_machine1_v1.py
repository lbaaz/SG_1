# Re-derivation du perimetre de l'instrument (gel 6.1, precision 1 de m2) : diff textuel hors docstring,
# usages de eta, AST apres neutralisation, egalite exacte sur le champ (eta=+1 == moteur ; eta=-1 == -d1/delta).
import ast, difflib, hashlib, sys, copy
import numpy as np
BASE = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/P4'
P4 = BASE + '/lot_machine1_2026-09-02_P4_instrument_v1/'
pat=open(P4+'integrer_indice.py').read(); jum=open(P4+'integrer_jumeau_machine1_v1.py').read()
print("patron", hashlib.sha256(pat.encode()).hexdigest()[:16], "instrument", hashlib.sha256(jum.encode()).hexdigest()[:16])
def sans_docstring(src):
    t=ast.parse(src); body=[n for n in t.body if not (isinstance(n,ast.Expr) and isinstance(getattr(n,'value',None),ast.Constant) and isinstance(n.value.value,str))]
    # texte : retirer les lignes de la docstring de module
    lines=src.split('\n'); 
    if lines[0].startswith('"""'):
        j=next(i for i in range(1,len(lines)) if lines[i].rstrip().endswith('"""')); lines=lines[j+1:]
    return '\n'.join(lines), body
pt, pb = sans_docstring(pat); jt, jb = sans_docstring(jum)
d=[l for l in difflib.unified_diff(pt.split('\n'), jt.split('\n'), lineterm='', n=0) if l.startswith(('+','-')) and not l.startswith(('+++','---'))]
ret=[l for l in d if l.startswith('-')]; ajo=[l for l in d if l.startswith('+')]
print(f"diff hors docstring : {len(ret)} retirees + {len(ajo)} ajoutees = {len(d)} lignes")
for l in d: print("   ", l)
hunks=sum(1 for l in difflib.unified_diff(pt.split('\n'), jt.split('\n'), lineterm='', n=0) if l.startswith('@@')); print("sites (hunks) :", hunks)
# usages de eta
tj=ast.parse(jum); names=[n for n in ast.walk(tj) if isinstance(n,ast.Name) and n.id=='eta']
arith=[n for n in ast.walk(tj) if isinstance(n,ast.BinOp) and any(isinstance(x,ast.Name) and x.id=='eta' for x in (n.left,n.right))]
print(f"noeuds Name(eta) : {len(names)} ; usages arithmetiques : {len(arith)} -> {[ast.dump(a) for a in arith]}")
# neutralisation : eta * d1 -> d1 ; retrait de la signature (kwonly eta) et de l'assert
class Neut(ast.NodeTransformer):
    def visit_BinOp(self, n):
        self.generic_visit(n)
        if isinstance(n.op,ast.Mult) and isinstance(n.left,ast.Name) and n.left.id=='eta': return n.right
        return n
    def visit_FunctionDef(self, n):
        self.generic_visit(n)
        if n.name=='integrer_jumeau':
            n.name='integrer_indice'; n.args.kwonlyargs=[a for a in n.args.kwonlyargs if a.arg!='eta']; n.args.kw_defaults=[]
            n.body=[s for s in n.body if not (isinstance(s,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='eta' for t in s.targets)) and not (isinstance(s,ast.Assert))]
        return n
tj2=Neut().visit(copy.deepcopy(tj)); ast.fix_missing_locations(tj2)
tp=ast.parse(pat)
def corps(t): return [n for n in t.body if not (isinstance(n,ast.Expr) and isinstance(n.value,ast.Constant))]
jd=ast.dump(ast.Module(body=corps(tj2),type_ignores=[])); pd=ast.dump(ast.Module(body=corps(tp),type_ignores=[]))
print("AST identique apres neutralisation (hors docstrings) :", jd==pd)
if jd!=pd:
    import itertools
    for a,b in zip(jd.split('),'), pd.split('),')):
        if a!=b: print("  premier ecart :", a[:120], "|", b[:120]); break
# champ : eta=+1 == moteur depose ; eta=-1 == -d1/delta ecrit en dur, exactement
sys.path.insert(0,P4); from charge_moteur import charger; m=charger()
rng=np.random.default_rng(0); nok=0; ntot=0
for p in (4,5,7):
    m.P=p
    for w2 in (1.5,2.0,2.42,3.0):
        delta=w2*w2-1; a1=rng.uniform(-3,3,200000); a2=rng.uniform(-3,3,200000); g=m.G_REF
        d1,d2=m.grad_rapide(a1,a2,g)
        acc_m=(-m.W1*m.W1*a1 + d1/delta, -w2*w2*a2 - d2/delta)   # forme du moteur depose (fantome)
        acc_p=(-m.W1*m.W1*a1 + 1.0*d1/delta, -w2*w2*a2 - d2/delta) # instrument eta=+1
        acc_dur=(-m.W1*m.W1*a1 - d1/delta, -w2*w2*a2 - d2/delta)   # -d1/delta ecrit en dur
        acc_m1=(-m.W1*m.W1*a1 + (-1.0)*d1/delta, -w2*w2*a2 - d2/delta) # instrument eta=-1
        e1=np.array_equal(acc_m[0],acc_p[0]) and np.array_equal(acc_m[1],acc_p[1]); e2=np.array_equal(acc_dur[0],acc_m1[0]) and np.array_equal(acc_dur[1],acc_m1[1])
        ntot+=2; nok+=int(e1)+int(e2)
print(f"champ : egalites exactes {nok}/{ntot} sur 12 cellules x 200000 points (eta=+1 == moteur ; eta=-1 == -d1/delta en dur)")
