# -*- coding: ascii -*-
"""MANDATAIRE A UNE DIMENSION DE L'ABSORBEUR DU LECTEUR 2D, POUR LE VIDE -- machine 1, v1, 2026-11-16.
Hors chaine, classe 3. AUCUN CALCUL 2D : c'est la chaine du premier ordre du vide (sites (2 m, m), sauts du moteur au
w2 du point) a laquelle on donne l'absorbeur DU LECTEUR, lu le long de l'echelle : r = max(a, b) = 2 m,
  F1 : W = eta (r - bord)^2 ;  F2 : W = eta (r - bord)^4 / L^2 ;  boite coupee a r = bord + L - 1 ;
  bord = r_c + decalage, r_c = 2 (m_bord + max(8, m_bord)) + 2 ; eta_k = eta0 2^(-k), k = -3 a 8.
Deux regles pour eta0 : celle du depot (eta0 = |delta|) et une regle adaptee au saut (eta0 = saut au site r_c / 2).
A chaque serie on applique la REGLE DE PLATEAU de la feuille deposee (cinq barreaux consecutifs, max <= 1.05 min).
Ce mandataire ne dit rien de la largeur 2D ; il dit si la force de l'absorbeur est du bon ordre pour le vide.
Usage : python3 -I mandataire_absorbeur_2D_machine1_v1.py <moteur> <bloc 2> <bloc 3> <phi_echelle.py> <carte.py>
        <absorbeur_adapte.py> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
MOTEUR, BLOC2, BLOC3, PHI, CARTE, ADAPTE, SORTIE = sys.argv[1:8]
spec = importlib.util.spec_from_file_location("adapte", ADAPTE); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
C = A.charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE); M = C.M; PH = C.PH
KS = list(range(-3, 9))
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]

def chaine(w2, g, m_max):
    d = float(w2) - 2.0
    t = [(g / M.P) * M.X_saut_reel(M.P, 2, 1, float(2 * m), float(m), w2) for m in range(m_max + 1)]
    return d, t

def largeur(d, t, forme, bord, L, eta, ln_estime):
    m_max = (bord + L - 1) // 2
    n = m_max + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(n):
        H[m, m] = m * d
        x = 2 * m - bord
        if x > 0:
            Wd[m] = eta * (float(x * x) if forme == "F1" else float(x ** 4) / float(L * L)); H[m, m] += -1j * Wd[m]
        if m < m_max:
            H[m, m + 1] = t[m]; H[m + 1, m] = t[m]
    return C.largeur(H, Wd, 0, abs(d), ln_estime)[0]

def plateau(ser):
    """Regle de la feuille deposee : fenetre de cinq k consecutifs, max <= (1 + 1/20) min ; plus petit rapport, puis plus petit k."""
    best = None
    for k0 in range(-3, 5):
        v = [ser[k] for k in range(k0, k0 + 5)]
        r = max(v) / min(v)
        if best is None or r < best[0] - 1e-15:
            best = (r, k0)
    return {"rapport": best[0], "k0": best[1], "plateau": bool(best[0] <= 1.05)}

out = {"cas": []}
print(" cas                          regle eta0        absorbeur  r = ln(Gamma_k / |delta|) - plateau adapte (ordre 1), k = -3 ... 8                                    fenetre   rapport  plateau")
for (mc, dlt) in ((3, 0.02), (3, -0.005), (4, -0.01), (4, 0.02), (5, 0.02), (5, -0.01)):
    k, w2, df, g = A.cellule_du_vide(mc, dlt)
    tb, t3 = A.tables(0, 0, w2, g)
    lp = PH.phi_fc(k, 0, 0)["ln_Phi"]; ref = A.plateau(tb, t3, 1, lp)["mediane"]
    r_c = 2 * (mc + max(8, mc)) + 2
    d, t = chaine(w2, g, (r_c + 10 + 100) // 2 + 1)
    for regle, eta0 in (("depot : |delta|", abs(df)), ("saut au site r_c/2", abs(t[r_c // 2]))):
        for nom, forme, dr, L in ABSORBEURS:
            bord = r_c + dr
            ser = {kk: largeur(d, t, forme, bord, L, eta0 * 2.0 ** (-kk), lp) for kk in KS}
            p = plateau(ser)
            rr = [math.log(ser[kk] / abs(df)) - ref for kk in KS]
            out["cas"].append({"m_cible": mc, "delta": df, "g": g, "r_c": r_c, "regle": regle, "eta0": eta0, "absorbeur": nom, "r": rr, "fenetre_k0": p["k0"], "rapport": p["rapport"], "plateau": p["plateau"],
                               "r_fenetre": [rr[p["k0"] + 3 + j] for j in range(5)]})
            print(" vide %d barreaux, %+.3f, r_c %d  %-18s %s   %s   k = %+d a %+d  %.4f  %s" % (mc, df, r_c, regle, nom, " ".join("%+.3f" % x for x in rr), p["k0"], p["k0"] + 4, p["rapport"], "OUI" if p["plateau"] else "non"))
n_dep = [c for c in out["cas"] if c["regle"].startswith("depot")]; n_sau = [c for c in out["cas"] if not c["regle"].startswith("depot")]
for nom, L in (("eta0 = |delta| (depot)", n_dep), ("eta0 = saut au site r_c / 2", n_sau)):
    ok = [c for c in L if c["plateau"]]
    print("%s : plateau a %d series sur %d ; dans les fenetres retenues, plus grand |r| : %.4f" % (nom, len(ok), len(L), max(abs(x) for c in ok for x in c["r_fenetre"]) if ok else float("nan")))
out["resume"] = {"depot": {"plateaux": sum(1 for c in n_dep if c["plateau"]), "series": len(n_dep)}, "saut": {"plateaux": sum(1 for c in n_sau if c["plateau"]), "series": len(n_sau)}}
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
