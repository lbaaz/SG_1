# -*- coding: ascii -*-
"""ELIGIBILITE DES CELLULES CANDIDATES DE LA REGLE DE TIRAGE -- machine 1, v1, 2026-11-15. AUCUN CALCUL 2D.
Derive de carte_chaine_machine1_v1.py (f0f6581d87176752, lot 1e8413aed149429f, non edite) par quatre retouches : cet en-tete (en deux
endroits), la liste des cellules (les quatre creneaux de la regle au lieu de la grille) et les modes. Les fonctions etat et cellule sont celles de
la carte, au caractere pres.
--- texte de l'en-tete d'origine :
CARTE PAR LA CHAINE SEULE -- machine 1, v1, 2026-11-15. Hors chaine. AUCUN CALCUL 2D, aucune largeur 2D lue ni jouee.
Pour une cellule (w2, facteur) : le point que la sonde deposee du delta 98 y jouerait (g = facteur x g_du_point(w2),
s = 0.70 s_ff, graine, barriere a la graine, r_c, boite N = r_c + 20, faisable si N <= N_MAX_EB), par les fonctions du
moteur et la regle ecrite au gel du delta 98 (section 3) ; puis, pour les etiquettes (n1, n2) de plus grand poids de la
graine coherente (poids de Poisson), la chaine du moteur, la chaine d'ordre 2 du bloc depose et la chaine d'ordre 3 du
bloc de la note du 15/11 : largeurs, stabilites, desaccord au bout de la barriere.
Ce que la sonde 2D lirait (ses 14 etats, leurs largeurs) n'est PAS calcule : les etiquettes sont PREDITES par le poids
de la graine ; le mode "depot" confronte cette prediction aux seize points deja joues, lus dans le depot.
--- usage de ce script :
Usage : python3 -I eligibilite_creneaux_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <sonde_ordre2.json>
        <sortie.json> <creneaux>      creneaux : noms separes par des virgules, parmi N, P, BN, BP"""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, DEP, SORTIE, MODE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                      # memoire des elements de x^5 : memes valeurs, moins d'appels
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))
FRACTION = 0.70; L_BOITE = 20; EF = 0.0625; ETAS = (0.25, 0.125, 0.0625, 0.03125); K_PREDITS = 16
CINQ = [F(3, 4), F(5, 6), F(1), F(6, 5), F(4, 3)]
CRENEAUX = {"N": ([F(k, 1000) for k in range(1931, 1940)], CINQ),                               # delta dans ]-0.070, -0.060[
            "P": ([F(k, 1000) for k in list(range(2031, 2040)) + list(range(2041, 2050))], CINQ),  # delta dans ]+0.030, +0.050[
            "BN": ([F(k, 1000) for k in list(range(1916, 1920)) + list(range(1921, 1925))], [F(1)]),  # delta dans ]-0.085, -0.075[
            "BP": ([F(k, 1000) for k in range(2061, 2070)], [F(1)])}                             # delta dans ]+0.060, +0.070[

def stable(v):
    return bool(all(x > 0.0 for x in v) and max(v) / min(v) <= 2.0)

def etat(w2, g, a, b):
    d = float(w2) - 2.0
    sites = M.barriere(float(a), float(b), w2, g, True)
    if not sites:
        return {"n1": a, "n2": b, "vide": True}
    g1 = [float(M.gamma_chaine(float(a), float(b), w2, g, sites, eta_facteur=x, M_facteur=4)["Gamma_c"]) for x in ETAS]
    tb = tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4)
    r2 = [gamma_chaine_ordre2(tb, x) for x in ETAS]; g2 = [r["Gamma_flux"] for r in r2]
    t3 = tables_ordre3(float(a), float(b), w2, g, tb)
    r3 = gamma_chaine_ordre3(tb, t3, EF); G3 = r3["Gamma_flux"]
    var = [gamma_chaine_ordre3(tb, t3, 2 * EF)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF / 2)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF, recul=4)["Gamma_flux"]]
    mb = tb["m2_bord"]
    return {"n1": a, "n2": b, "vide": False, "card": len(sites), "m_bord": mb, "e_bord": abs(mb * d + tb["S"][mb] - tb["S"][0]), "t_bord": abs(tb["t"][mb]),
            "kappa": abs(tb["t"][0]) / abs(d), "G1": g1, "stable1": stable(g1), "G2": g2, "stable2": stable(g2), "dE2": r2[2]["dE"],
            "G3": G3, "dE3": r3["dE"], "stab3": (max(abs(math.log(x / G3)) for x in var) if G3 > 0.0 and all(x > 0.0 for x in var) else None),
            "E_libre": float(M.energie_libre(a, b, w2))}

def cellule(w2, fac, en_plus=()):
    _cache.clear(); t0 = time.time()
    g_regle = float(M.g_du_point(w2)); g = g_regle * float(fac); s = FRACTION * M.s_ff(w2, g)
    n1m, n2m = M.appariement(s, w2); sites0 = M.barriere(n1m, n2m, w2, g, True)
    m2b = sites0[-1][0] if sites0 else 0; b_M = max(8, m2b)
    r_c = int(math.ceil(n1m)) + 2 * (m2b + b_M) + 2; N = r_c + L_BOITE
    cand = []
    for a in range(0, int(n1m + 8 * math.sqrt(n1m) + 12)):
        for b in range(0, int(n2m + 8 * math.sqrt(n2m) + 12)):
            cand.append((-n1m + a * math.log(n1m) - math.lgamma(a + 1) - n2m + b * math.log(n2m) - math.lgamma(b + 1), a, b))
    cand.sort(key=lambda c: (-c[0], c[1], c[2])); lw = {(a, b): x for x, a, b in cand}
    labels = [(a, b) for _, a, b in cand[:K_PREDITS]] + [l for l in en_plus if l not in [(a, b) for _, a, b in cand[:K_PREDITS]]]
    etats = []
    for r, (a, b) in enumerate(labels):
        e = etat(w2, g, a, b); e["rang_predit"] = r if r < K_PREDITS else None; e["poids_graine"] = math.exp(lw[(a, b)]) if (a, b) in lw else 0.0
        etats.append(e)
    return {"w2": str(w2), "delta": float(w2) - 2.0, "facteur": str(fac), "g_regle": g_regle, "g": g, "s": s, "graine": [n1m, n2m], "card_barriere_graine": len(sites0),
            "m_bord_graine": m2b, "r_c": r_c, "N": N, "faisable": bool(N <= M.N_MAX_EB), "etats": etats, "duree_s": round(time.time() - t0, 1)}

out = {"reglage": {"fraction": FRACTION, "L_boite": L_BOITE, "ef": EF, "etas": list(ETAS), "K_predits": K_PREDITS, "M_facteur": 4}, "mode": MODE, "cellules": []}
travail = [(w2, f, nom, ()) for nom in MODE.split(",") for w2 in CRENEAUX[nom][0] for f in CRENEAUX[nom][1]]
for (w2, fac, pid, plus) in travail:
    c = cellule(w2, fac, plus); c["id"] = pid; out["cellules"].append(c)
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
    print("%s w2 = %s x %s : g = %.4e, graine (%.2f, %.2f), N = %d, %d etiquettes, %.0f s" % (pid or "-", w2, fac, c["g"], c["graine"][0], c["graine"][1], c["N"], len(c["etats"]), c["duree_s"]), flush=True)
print("FIN %s : %d cellules" % (MODE, len(out["cellules"])))
