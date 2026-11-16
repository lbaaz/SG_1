# -*- coding: ascii -*-
"""LA CARTE REJOUEE SOUS L'ABSORBEUR ADAPTE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.
Les points de carte_v1.json de 16 barreaux au plus (ceux ou la regle deposee rendait la chaine d'ordre 3 instable) :
meme chaine d'ordre 3 (blocs deposes), absorbeur adapte au saut. r3* = ln(Gamma_3* / |delta|) - ln Phi*.
Variantes : les 18 jusqu'a 8 barreaux ; au-dela, six (a = 1, 2, 4 ; c = 8 ; L = 16, 24), declarees.
"Instable" garde le sens de la carte : etendue des variantes au-dessus de 0.05.
Usage : python3 -I carte_adaptee_machine1_v1.py <moteur> <bloc 2> <bloc 3> <phi_echelle.py> <carte.py>
        <absorbeur_adapte.py> <carte_v1.json> <sortie.json>"""
import sys, math, json, importlib.util, statistics
from fractions import Fraction as F
MOTEUR, BLOC2, BLOC3, PHI, CARTE, ADAPTE, ENTREE, SORTIE = sys.argv[1:9]
spec = importlib.util.spec_from_file_location("adapte", ADAPTE); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
C = A.charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE); PH = C.PH
SIX = [v for v in A.VARIANTES if v[1] == 8]
P = [p for p in json.load(open(ENTREE))["points"] if p["m_cible"] <= 16]
STAB_MAX = 0.05
phi_et = {}
out = []
for p in P:
    if p["vide"]:
        out.append({"n1": p["n1"], "n2": p["n2"], "m_cible": p["m_cible"], "e_cible": p["e_cible"], "delta": p["delta"], "vide": True}); continue
    C._cache.clear()
    var = A.VARIANTES if p["m_cible"] <= 8 else SIX
    cle = (p["n1"], p["n2"], p["m_cible"])
    if cle not in phi_et:
        v = [A.phi_adaptee(p["kappa"], p["n1"], p["n2"], a, c, L) for (a, c, L) in var]
        phi_et[cle] = (statistics.median(v), max(v) - min(v))
    w2 = F(2) + F(p["delta"]).limit_denominator(10 ** 7)
    assert abs((float(w2) - 2.0) - p["delta"]) < 1e-15
    tb, t3 = A.tables(p["n1"], p["n2"], w2, p["g"])
    d = abs(tb["d"]); v = []
    for (a, c, L) in var:
        H, Wd, i0 = A.matrice_adaptee(tb, t3, 3, a, c, L)
        G = C.largeur(H, Wd, i0, d, p["ln_Phi"])[0]
        v.append(math.log(G / d) if G > 0 else float("nan"))
    ok = all(x == x for x in v)
    rec = {"n1": p["n1"], "n2": p["n2"], "m_cible": p["m_cible"], "e_cible": p["e_cible"], "delta": p["delta"], "g": p["g"], "vide": False, "m_bord": p["m_bord"], "e_bord": p["e_bord"],
           "variantes": len(var), "ln_Phi_etoile": phi_et[cle][0], "etendue_Phi_etoile": phi_et[cle][1],
           "r3_etoile": (statistics.median(v) - phi_et[cle][0]) if ok else None, "etendue": (max(v) - min(v)) if ok else None,
           "r3_depose": p["r3"], "stab3_depose": p["stab3"], "instable_depose": bool(p["stab3"] is None or p["stab3"] > STAB_MAX)}
    rec["instable_adapte"] = bool((not ok) or rec["etendue"] > STAB_MAX)
    out.append(rec)
    print("  (%d,%d) %2d barreaux e = %.3f delta %+.5f : r3* = %s (etendue %s) ; depose : r3 = %+.4f (stabilite %s)" % (
        p["n1"], p["n2"], p["m_cible"], p["e_cible"], p["delta"], ("%+.4f" % rec["r3_etoile"]) if ok else "  -  ", ("%.4f" % rec["etendue"]) if ok else "-",
        p["r3"], ("%.4f" % p["stab3"]) if p["stab3"] is not None else "-"), flush=True)
calc = [r for r in out if not r["vide"]]
inst_d = [r for r in calc if r["instable_depose"]]; inst_a = [r for r in calc if r["instable_adapte"]]
print()
print("points de 16 barreaux au plus : %d calcules ; instables sous la regle deposee : %d ; sous l'absorbeur adapte : %d (dont deja instables : %d)" % (
    len(calc), len(inst_d), len(inst_a), sum(1 for r in inst_a if r["instable_depose"])))
for (n1, n2) in ((0, 0), (6, 2)):
    L = [r for r in inst_a if (r["n1"], r["n2"]) == (n1, n2)]
    print("  (%d,%d) : instables sous l'absorbeur adapte : %d ; leur plus petit |delta| : %s ; leur plus petit e_bord : %s" % (
        n1, n2, len(L), ("%.4f" % min(abs(r["delta"]) for r in L)) if L else "-", ("%.3f" % min(r["e_bord"] for r in L)) if L else "-"))
    S = [r for r in calc if (r["n1"], r["n2"]) == (n1, n2) and not r["instable_adapte"]]
    print("          stables : %d ; leur plus grand |delta| : %.4f ; leur plus grand e_bord : %.3f ; leur plus grand |r3*| : %.4f" % (
        len(S), max(abs(r["delta"]) for r in S), max(r["e_bord"] for r in S), max(abs(r["r3_etoile"]) for r in S)))
json.dump({"points": out, "comptes": {"calcules": len(calc), "instables_depose": len(inst_d), "instables_adapte": len(inst_a)}}, open(SORTIE, "w"), indent=1, sort_keys=True)
