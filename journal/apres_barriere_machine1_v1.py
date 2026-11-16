# -*- coding: ascii -*-
"""CE QUI RESTE INSTABLE SOUS L'ABSORBEUR ADAPTE -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.
Partie A. A huit points de la carte ou l'ordre 3 reste instable sous l'absorbeur adapte : plateau et etendue (18 variantes)
  aux ordres 1, 2 et 3 ; premier site ou le saut depasse 1 ; premier site ou le saut corrige t + T3 change de signe.
Partie B. Essai (NEGATIF, consigne) : couper net les termes d'ordre 3 au-dela d'un site m_s (premier site ou le saut
  depasse t_s, t_s = 0.15, 0.3, 0.5), ordre 2 au-dela ; aux memes points, a deux points stables et a quatre etats joues.
  Pour les etats joues, la largeur de plateau 2D et la largeur d'ordre 3 deposee sont LUES dans superposition_v1.json.
Usage : python3 -I apres_barriere_machine1_v1.py <moteur> <bloc 2> <bloc 3> <phi_echelle.py> <carte.py> <absorbeur_adapte.py>
        <carte_v1.json> <superposition_v1.json> <sortie.json>"""
import sys, math, json, importlib.util, statistics
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, PHI, CARTE, ADAPTE, ENTREE, SUPER, SORTIE = sys.argv[1:10]
spec = importlib.util.spec_from_file_location("adapte", ADAPTE); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
C = A.charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE)
J = json.load(open(ENTREE))["points"]; S = json.load(open(SUPER))["etats"]

def point_carte(n1, mc, e, sg):
    return [q for q in J if q["n1"] == n1 and q["m_cible"] == mc and abs(q["e_cible"] - e) < 1e-9 and ((q["delta"] < 0) == (sg < 0))][0]

def matrice_tronquee(tb, t3, a, c, L, m_s):
    d, m_min = tb["d"], tb["m_min"]; cap = tb["m2_bord"] + c; Mh = cap + L
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > cap:
            Wd[i] = a * abs(tb["t"][m]) * ((m - cap) / float(L)) ** 2; H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb["t"][m] + (t3["T3"][m] if m + 1 <= m_s else 0.0); H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if m + 3 <= Mh and m + 3 <= m_s:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if m + 5 <= Mh and m + 5 <= m_s:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, Wd, -m_min

INSTABLES = ((0, 4, 0.15, -1), (0, 4, 0.3, -1), (0, 6, 0.3, -1), (0, 8, 0.5, -1), (6, 4, 0.3, 1), (6, 6, 0.5, 1), (6, 8, 0.7, -1), (0, 12, 1.0, -1))
out = {"A": [], "B": []}
print("A. sous l'absorbeur adapte : r = ln(Gamma / |delta|) - ln Phi (regle deposee), plateau (etendue)")
print("   point                              g         ordre 1            ordre 2            ordre 3            saut > 1 au site   t + T3 change de signe au site   dernier site de la plus longue variante")
for (n1, mc, e, sg) in INSTABLES:
    p = point_carte(n1, mc, e, sg); w2 = F(2) + F(p["delta"]).limit_denominator(10 ** 7)
    tb, t3 = A.tables(p["n1"], p["n2"], w2, p["g"]); mb = tb["m2_bord"]
    pl = [A.plateau(tb, t3, o, p["ln_Phi"]) for o in (1, 2, 3)]
    s1 = next((m for m in range(1, tb["Mh"]) if abs(tb["t"][m]) > 1.0), None)
    sz = next((m for m in range(0, tb["Mh"]) if (tb["t"][m] + t3["T3"][m]) * tb["t"][m] <= 0), None)
    out["A"].append({"n1": p["n1"], "n2": p["n2"], "m_cible": mc, "delta": p["delta"], "g": p["g"], "m_bord": mb, "site_saut_1": s1, "site_signe": sz, "dernier_site": mb + 34,
                     "ordres": {str(o): {"r": pl[o - 1]["mediane"] - p["ln_Phi"], "etendue": pl[o - 1]["etendue"]} for o in (1, 2, 3)}})
    print("   (%d,%d) %2d barreaux, delta %+.4f   %.2e   %+.3f (%.3f)   %+.3f (%.3f)   %+.3f (%.3f)   %-18s %-32s %d" % (
        p["n1"], p["n2"], mc, p["delta"], p["g"], pl[0]["mediane"] - p["ln_Phi"], pl[0]["etendue"], pl[1]["mediane"] - p["ln_Phi"], pl[1]["etendue"],
        pl[2]["mediane"] - p["ln_Phi"], pl[2]["etendue"], s1, sz, mb + 34))

print()
print("B. ESSAI : termes d'ordre 3 coupes net au-dela du premier site ou le saut depasse t_s ; r median des 18 variantes (etendue)")
print("   cas                                      m_bord   t_s = 0.15            t_s = 0.30            t_s = 0.50            ecart entre les trois   sans coupure          2D lu     depose")
cas = [("carte (%d,%d) %d barreaux %+.4f" % (0 if n1 == 0 else 6, 0 if n1 == 0 else 2, mc, point_carte(n1, mc, e, sg)["delta"]), point_carte(n1, mc, e, sg), None) for (n1, mc, e, sg) in INSTABLES + ((0, 4, 0.075, -1), (6, 8, 0.3, -1))]
for (idc, rang) in (("N1", 0), ("BP", 3), ("P1", 0), ("C1", 0)):
    e = [x for x in S if x["id"] == idc and x["rang"] == rang][0]
    cas.append(("joue %s rang %d (%d,%d) %+.3f" % (idc, rang, e["n1"], e["n2"], e["delta"]), e, (math.log(e["Gamma_pl"] / abs(e["delta"])), math.log(e["G3"] / abs(e["delta"])))))
for (nom, p, ref) in cas:
    w2 = F(p["w2"]) if "w2" in p else F(2) + F(p["delta"]).limit_denominator(10 ** 7)
    tb, t3 = A.tables(p["n1"], p["n2"], w2, p["g"]); d = abs(tb["d"]); mb = tb["m2_bord"]; lp = p["ln_Phi"]
    res = []
    for ts in (0.15, 0.3, 0.5):
        ms = max(next((m for m in range(1, tb["Mh"]) if abs(tb["t"][m]) > ts), tb["Mh"]), mb)
        v = []
        for (a, c, L) in A.VARIANTES:
            H, Wd, i0 = matrice_tronquee(tb, t3, a, c, L, ms); v.append(math.log(C.largeur(H, Wd, i0, d, lp)[0] / d) - lp)
        res.append((ms, statistics.median(v), max(v) - min(v)))
    plein = A.plateau(tb, t3, 3, lp)
    ecart = max(r[1] for r in res) - min(r[1] for r in res)
    out["B"].append({"cas": nom, "m_bord": mb, "coupures": [{"t_s": ts, "m_s": r[0], "r": r[1], "etendue": r[2]} for ts, r in zip((0.15, 0.3, 0.5), res)], "ecart": ecart,
                     "sans_coupure": {"r": plein["mediane"] - lp, "etendue": plein["etendue"]}, "r_2D": (ref[0] - lp) if ref else None, "r_depose": (ref[1] - lp) if ref else None})
    print("   %-40s %2d    %s   %.3f                   %+.3f (%.3f)      %s" % (nom, mb, "   ".join("m_s=%2d %+.3f (%.3f)" % r for r in res), ecart, plein["mediane"] - lp, plein["etendue"],
          ("%+.3f    %+.3f" % (ref[0] - lp, ref[1] - lp)) if ref else ""))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
