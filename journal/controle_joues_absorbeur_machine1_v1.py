# -*- coding: ascii -*-
"""L'ABSORBEUR ADAPTE AUX ETATS DEJA JOUES -- machine 1, v1, 2026-11-16. Hors chaine, classe 3, APRES COUP. Aucun 2D.
Pour chaque etat juge, qualifie et dans le domaine des deltas 98 et 100 (liste et largeurs LUES dans
superposition_v1.json) : la chaine d'ordre 3 des blocs deposes sous l'absorbeur adapte au saut (18 variantes),
contre la largeur d'ordre 3 deposee (meme chaine, absorbeur depose) et contre la largeur de plateau 2D.
Ce n'est PAS un rejeu du gel du delta 100 : les tolerances de E1 ne sont rappelees que pour situer les ecarts.
Usage : python3 -I controle_joues_absorbeur_machine1_v1.py <moteur> <bloc 2> <bloc 3> <phi_echelle.py> <carte.py>
        <absorbeur_adapte.py> <superposition.json> <sortie.json>"""
import sys, math, json, importlib.util, statistics
from fractions import Fraction as F
MOTEUR, BLOC2, BLOC3, PHI, CARTE, ADAPTE, SUPER, SORTIE = sys.argv[1:9]
spec = importlib.util.spec_from_file_location("adapte", ADAPTE); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
C = A.charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE)
E = [e for e in json.load(open(SUPER))["etats"] if e["domaine"]]
med = statistics.median
out = []
for i, e in enumerate(E):
    C._cache.clear()
    w2 = F(e["w2"]); tb, t3 = A.tables(e["n1"], e["n2"], w2, e["g"])
    p = A.plateau(tb, t3, 3, e["ln_Phi"])
    d = abs(e["delta"])
    rec = {"source": e["source"], "id": e["id"], "rang": e["rang"], "n1": e["n1"], "n2": e["n2"], "delta": e["delta"], "e_bord": e["e_bord"], "m_bord": e["m_bord"],
           "ln_G3_depose": math.log(e["G3"] / d), "ln_G3_etoile": p["mediane"], "etendue": p["etendue"], "ln_Gpl": math.log(e["Gamma_pl"] / d)}
    rec["etoile_moins_depose"] = rec["ln_G3_etoile"] - rec["ln_G3_depose"]
    rec["ln_q3_depose"] = rec["ln_G3_depose"] - rec["ln_Gpl"]; rec["ln_q3_etoile"] = rec["ln_G3_etoile"] - rec["ln_Gpl"]
    rec["tolerance_E1"] = 0.05 if e["e_bord"] < 0.3 else 0.10
    out.append(rec)
print("etats du domaine : %d (delta 100 : %d, delta 98 : %d)" % (len(out), sum(1 for r in out if r["source"] == "delta100"), sum(1 for r in out if r["source"] == "delta98")))
et = sorted(r["etendue"] for r in out)
print("etendue de l'ordre 3 sous les 18 variantes : mediane %.4f, neuvieme decile %.4f, plus grande %.4f" % (med(et), et[int(0.9 * len(et))], et[-1]))
dd = [r["etoile_moins_depose"] for r in out]
print("ln(G3 adapte / G3 depose) : mediane %+.4f, de %+.4f a %+.4f ; |.| mediane %.4f ; signe positif a %d etats sur %d" % (med(dd), min(dd), max(dd), med([abs(x) for x in dd]), sum(1 for x in dd if x > 0), len(dd)))
for nom, cle in (("depose", "ln_q3_depose"), ("adapte", "ln_q3_etoile")):
    q = [abs(r[cle]) for r in out]
    hors = [r for r in out if abs(r[cle]) > r["tolerance_E1"]]
    h100 = [r for r in hors if r["source"] == "delta100"]
    print("|ln q3| (%s) : mediane %.4f, plus grand %.4f ; hors de la tolerance rappelee de E1 : %d etats (dont delta 100 : %d : %s)" % (
        nom, med(q), max(q), len(hors), len(h100), ", ".join("%s rang %d %.4f/%.2f" % (r["id"], r["rang"], abs(r[cle]), r["tolerance_E1"]) for r in h100) or "aucun"))
mieux = sum(1 for r in out if abs(r["ln_q3_etoile"]) < abs(r["ln_q3_depose"]))
print("l'absorbeur adapte est plus pres du plateau 2D a %d etats sur %d" % (mieux, len(out)))
print()
print("par cellule ou point :  delta    etats  etendue max   adapte - depose : min ; mediane ; max     |ln q3| depose max   |ln q3| adapte max")
par = {}
for r in out:
    par.setdefault((r["source"], r["id"]), []).append(r)
resume = []
for cle in sorted(par, key=lambda c: (par[c][0]["delta"], c)):
    L = par[cle]; x = sorted(r["etoile_moins_depose"] for r in L)
    row = {"source": cle[0], "id": cle[1], "delta": L[0]["delta"], "etats": len(L), "etendue_max": max(r["etendue"] for r in L), "diff": [x[0], med(x), x[-1]],
           "q3_depose_max": max(abs(r["ln_q3_depose"]) for r in L), "q3_etoile_max": max(abs(r["ln_q3_etoile"]) for r in L)}
    resume.append(row)
    print("  %-8s %-3s   %+.3f   %3d    %.4f        %+.4f ; %+.4f ; %+.4f           %.4f               %.4f" % (cle[0], cle[1], row["delta"], row["etats"], row["etendue_max"], x[0], med(x), x[-1], row["q3_depose_max"], row["q3_etoile_max"]))
json.dump({"etats": out, "resume": resume}, open(SORTIE, "w"), indent=1, sort_keys=True)
