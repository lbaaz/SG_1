# -*- coding: utf-8 -*-
"""Deux controles de plus pour la certification P-4 (machine 2) :
 (1) A-1, le perimetre de l'instrument, re-derive a l'AST -- l'acte affirme 5 lignes de diff en
     3 endroits, 5 noeuds Name(eta), UN SEUL usage arithmetique, et AST identique au patron apres
     neutralisation. C'est la l'affirmation qui fait que "le jumeau est le patron a un signe pres" ;
 (2) A-3, les plafonds s_CAP du degre pair, re-derives de la forme fermee (D-P4-2 : le terme
     g s^p/(p delta) doit y etre)."""
import ast, difflib, math, os, sys

INST = r"C:\Users\bazil\AppData\Local\Temp\claude\d--devs-bocal\c05caab7-d368-4b5e-a48a-79643f7042ff\scratchpad\P4inst"
A = open(os.path.join(INST, "integrer_indice.py"), encoding="utf-8").read()
B = open(os.path.join(INST, "integrer_jumeau_machine1_v1.py"), encoding="utf-8").read()


def sans_docstring(src):
    t = ast.parse(src)
    if t.body and isinstance(t.body[0], ast.Expr) and isinstance(t.body[0].value, ast.Constant) \
       and isinstance(t.body[0].value.value, str):
        t.body = t.body[1:]
    return t


print("=== (1) A-1 : LE PERIMETRE DE L'INSTRUMENT, A L'AST ===")
la = [l for l in A.split("\n")]
lb = [l for l in B.split("\n")]
# diff hors docstring : on compare le code sans les docstrings de module
ca = ast.unparse(sans_docstring(A)).split("\n")
cb = ast.unparse(sans_docstring(B)).split("\n")
d = list(difflib.unified_diff(ca, cb, n=0, lineterm=""))
ret = [x for x in d if x.startswith("-") and not x.startswith("---")]
add = [x for x in d if x.startswith("+") and not x.startswith("+++")]
hunks = [x for x in d if x.startswith("@@")]
print("  diff du code deparse (docstrings retirees) : %d retirees, %d ajoutees, %d endroits"
      % (len(ret), len(add), len(hunks)))
print("  acte : 5 lignes (2 retirees, 3 ajoutees) en trois endroits -> %s"
      % ("CONFORME" if (len(ret), len(add), len(hunks)) == (2, 3, 3) else "a lire ci-dessous"))
for x in ret + add:
    print("      %s" % x[:96])

tb = ast.parse(B)
noms = [n for n in ast.walk(tb) if isinstance(n, ast.Name) and n.id == "eta"]
mult = [n for n in ast.walk(tb) if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult)
        and isinstance(n.left, ast.Name) and n.left.id == "eta"
        and isinstance(n.right, ast.Name) and n.right.id == "d1"]
print("  noeuds Name(eta) a l'AST : %d   (acte : 5) -> %s" % (len(noms), "CONFORME" if len(noms) == 5 else "ECART <<<"))
print("  usages arithmetiques BinOp(Mult, Name(eta), Name(d1)) : %d   (acte : UN SEUL) -> %s"
      % (len(mult), "CONFORME" if len(mult) == 1 else "ECART <<<"))


class Neutralise(ast.NodeTransformer):
    """eta * d1 -> d1 ; retire la signature kw-only eta et l'assert sur eta."""
    def visit_BinOp(self, n):
        self.generic_visit(n)
        if (isinstance(n.op, ast.Mult) and isinstance(n.left, ast.Name) and n.left.id == "eta"
                and isinstance(n.right, ast.Name) and n.right.id == "d1"):
            return n.right
        return n

    def visit_FunctionDef(self, n):
        self.generic_visit(n)
        if n.name != "integrer_jumeau":      # ne pas toucher aux fonctions imbriquees (acc)
            return n
        n.args.kwonlyargs = [a for a in n.args.kwonlyargs if a.arg != "eta"]
        n.args.kw_defaults = n.args.kw_defaults[:len(n.args.kwonlyargs)]
        n.name = "integrer_indice"
        n.body = [s for s in n.body
                  if not (isinstance(s, ast.Assert) and "eta" in ast.dump(s))
                  and not (isinstance(s, ast.Assign) and "eta" in ast.dump(s.targets[0]))]
        return n


nb = Neutralise().visit(sans_docstring(B))
ast.fix_missing_locations(nb)
na = sans_docstring(A)
ident = ast.dump(na) == ast.dump(nb)
print("  AST identique au patron apres neutralisation : %s   (acte : IDENTIQUE) -> %s"
      % (ident, "CONFORME" if ident else "ECART <<<"))
if not ident:
    for x in list(difflib.unified_diff(ast.unparse(na).split("\n"), ast.unparse(nb).split("\n"), n=0, lineterm=""))[:14]:
        print("      %s" % x[:96])

print("")
print("=== (2) A-3 : LES PLAFONDS s_CAP DU DEGRE PAIR, RE-DERIVES ===")
G, CAP = 0.05, 1.0e4
ATT = {(4, 2.22): 353.66, (4, 2.00): 330.56, (4, 3.00): 422.55}
NAIF = {(4, 2.22): 5304, (4, 2.00): 4685, (4, 3.00): 6860}
n_ok = 0
for (p, w2), att in sorted(ATT.items()):
    delta = w2 * w2 - 1.0
    Q = ((1.0 + w2 * w2) ** 2 + 4.0 * w2 * w2) / (2.0 * delta * delta)
    # |x1| <= sqrt(2 E0) ; le plafond est atteint quand sqrt(2 E0) = CAP
    def E0(s):
        return Q * s * s + (G / (p * delta)) * s ** p
    lo, hi = 0.0, 1e6
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if 2 * E0(mid) < CAP * CAP:
            lo = mid
        else:
            hi = mid
    s_cap = 0.5 * (lo + hi)
    # la forme fautive D-P4-2 : sans le terme g s^p
    s_naif = math.sqrt(CAP * CAP / (2 * Q))
    ok = abs(s_cap - att) < 0.01
    n_ok += ok
    print("  %d|%.2f : s_CAP = %.2f  (acte : %.2f) %s   ; sans le terme g s^p : %.0f (acte : %d, faute D-P4-2)"
          % (p, w2, s_cap, att, "CONFORME" if ok else "ECART <<<", s_naif, NAIF[(p, w2)]))
print("  s_CAP : %d sur %d conformes" % (n_ok, len(ATT)))
print("  rapport au haut de la grille de P-1 (1.15 s_ref) : l'acte annonce 106.7, 110.5, 38.9")
