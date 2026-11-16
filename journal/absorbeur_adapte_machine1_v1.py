# -*- coding: ascii -*-
"""ABSORBEUR DE CHAINE ADAPTE AU SAUT -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. Aucun calcul 2D.
La chaine deposee absorbe avec W_m = ef |delta| (m - debut)^2 : sa force suit le desaccord, pas le saut. Ici :
    W_m = a |t_m| ((m - debut) / L)^2  pour debut < m <= debut + L,  debut = m_bord + c,  chaine coupee a debut + L,
de sorte que l'absorption cumulee, somme de W_m / (2 |t_m|), vaut a L / 6 quel que soit l'etat.
Variantes jouees : a dans (1, 2, 4), c dans (6, 8, 10), L dans (16, 24) : 18 ; centrale a = 2, c = 8, L = 24.
"Plateau" d'une largeur : mediane des 18 logarithmes ; "etendue" : max - min des 18.
Parties :
  A. Diagnostic sur la regle deposee : largeur du vide (ordres 1 et 3) quand ef varie de 2^-6 a 2^8 fois 0.0625.
  B. Le vide, barrieres de 2 a 6 barreaux, |delta| = 0.005, 0.01, 0.02 : plateau et etendue aux ordres 1, 2, 3 ;
     Phi* (limite delta -> 0, absorbeur adapte) contre Phi (regle deposee) ; forme fermee contre Phi*.
  C. Phi* contre Phi pour quelques etats excites.
Usage : python3 -I absorbeur_adapte_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <phi_echelle.py> <carte.py>
        <forme_phi.json> <sortie.json>"""
import sys, math, json, importlib.util, statistics
from fractions import Fraction as F
import numpy as np

VARIANTES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]
CENTRALE = (2.0, 8, 24)
C = PH = M = None


def charger(moteur, bloc2, bloc3, phi, carte):
    """Charge carte_machine1_v1.py (qui charge le moteur, les blocs deposes et phi_echelle)."""
    global C, PH, M
    sauv = list(sys.argv)
    sys.argv = [carte, moteur, bloc2, bloc3, phi, "/dev/null"]
    spec = importlib.util.spec_from_file_location("carte", carte); C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C)
    sys.argv = sauv
    PH, M = C.PH, C.M
    return C


def tables(n1, n2, w2, g, m_facteur=4):
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    if not sites:
        return None, None
    tb = C.tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=m_facteur)
    return tb, C.tables_ordre3(float(n1), float(n2), w2, g, tb)


def matrice_adaptee(tb, t3, ordre, a, c, L):
    """Ordre 1 : sauts du premier ordre seuls (sites bas compris) ; 2 et 3 : les matrices des blocs deposes.
    Seul l'absorbeur change, et la longueur."""
    d, m_min = tb["d"], tb["m_min"]; cap = tb["m2_bord"] + c; Mh = cap + L
    if Mh > tb["Mh"]:
        raise RuntimeError("tables trop courtes : %d > %d" % (Mh, tb["Mh"]))
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + ((tb["S"][m] - tb["S"][0]) if ordre >= 2 else 0.0)
        if m > cap:
            Wd[i] = a * abs(tb["t"][m]) * ((m - cap) / float(L)) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0)
            H[i, i + 1] = x; H[i + 1, i] = x
        if ordre >= 2 and m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, Wd, -m_min


def plateau(tb, t3, ordre, ln_estime):
    """ln(Gamma / |delta|) aux 18 variantes : mediane, etendue, valeur centrale."""
    d = abs(tb["d"]); v = []
    for (a, c, L) in VARIANTES:
        H, Wd, i0 = matrice_adaptee(tb, t3, ordre, a, c, L)
        v.append(math.log(C.largeur(H, Wd, i0, d, ln_estime)[0] / d))
    return {"mediane": statistics.median(v), "etendue": max(v) - min(v), "centrale": v[VARIANTES.index(CENTRALE)], "valeurs": v}


def phi_adaptee(kappa, n1, n2, a, c, L, s=1):
    """Chaine de la limite (unites de |delta|, w2 = 2) sous l'absorbeur adapte."""
    rg = PH.reglage(kappa, n1, n2)
    if rg is None:
        return None
    m_min = rg["m_min"]; cap = rg["m_bord"] + c; Mh = cap + L
    t0 = PH.tau(n1, n2, 0)
    T = {m: kappa * PH.tau(n1, n2, m) / t0 for m in range(m_min, Mh + 1)}
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = s * m
        if m > cap:
            Wd[i] = a * T[m] * ((m - cap) / float(L)) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            H[i, i + 1] = T[m]; H[i + 1, i] = T[m]
    est = PH.phi_fc(kappa, n1, n2)["ln_Phi"]
    return math.log(C.largeur(H, Wd, -m_min, 1.0, est)[0])


def plateau_phi(kappa, n1, n2):
    v = [phi_adaptee(kappa, n1, n2, a, c, L) for (a, c, L) in VARIANTES]
    return {"mediane": statistics.median(v), "etendue": max(v) - min(v), "centrale": v[VARIANTES.index(CENTRALE)]}


def cellule_du_vide(m_cible, delta):
    k = C.kappa_pour_m_bord(0, 0, m_cible)[0]
    w2 = F(2) + F(delta).limit_denominator(10 ** 7); df = float(w2) - 2.0
    g = k * abs(df) / (M.X_saut_reel(M.P, M.CANAL[0], M.CANAL[1], 0.0, 0.0, w2) / M.P)
    return k, w2, df, g


if __name__ == "__main__":
    MOTEUR, BLOC2, BLOC3, PHI, CARTE, FORME, SORTIE = sys.argv[1:8]
    charger(MOTEUR, BLOC2, BLOC3, PHI, CARTE)
    FP = json.load(open(FORME)); B = 2.0 * FP["I"]
    ref = [x for x in FP["B"] if (x["n1"], x["n2"], x["M0"]) == (0, 0, 4096)][0]; C0, D0 = ref["c_L"], -ref["reste3"]
    XC = M.coeff_homogene_X_s(F(2))
    out = {"variantes": VARIANTES, "centrale": CENTRALE, "A": [], "B": [], "C": []}

    print("A. REGLE DEPOSEE : ln(Gamma / |delta|) - ln Phi du vide quand la force ef de l'absorbeur varie (debut inchange)")
    print("   cas                     ordre   " + "".join("ef=%-9.5f" % (0.0625 * 2.0 ** j) for j in range(-6, 9, 2)))
    for (mc, d) in ((3, -0.02), (4, 0.01), (5, 0.02)):
        k, w2, df, g = cellule_du_vide(mc, d); tb, t3 = tables(0, 0, w2, g); lp = PH.phi_fc(k, 0, 0)["ln_Phi"]
        for ordre in (1, 3):
            row = []
            for j in range(-6, 9, 2):
                ef = 0.0625 * 2.0 ** j
                if ordre == 1:
                    G = C.gamma_chaine_ordre3(tb, t3, ef, avec_T3=False, avec_W3=False, avec_S=False, avec_U=False, avec_W5=False)["Gamma_flux"]
                else:
                    H, Wd, i0 = C.matrice(tb, t3, ef, 3); G = C.largeur(H, Wd, i0, abs(df), lp)[0]
                row.append(math.log(G / abs(df)) - lp)
            out["A"].append({"m_cible": mc, "delta": df, "g": g, "ordre": ordre, "ef": [0.0625 * 2.0 ** j for j in range(-6, 9, 2)], "r": row})
            print("   vide, %d barreaux, %+.3f   %d     " % (mc, df, ordre) + "".join("%+-12.4f" % x for x in row))

    print()
    print("B. LE VIDE SOUS L'ABSORBEUR ADAPTE (18 variantes) : plateau = mediane, etendue = max - min ; r = ln(Gamma / |delta|) - ln Phi*")
    print("   barreaux  kappa     ln Phi (deposee)  ln Phi*    etendue  Phi*-Phi  ferme-Phi* | delta     g          r1 (et.)          r2 (et.)          r3 (et.)        r3 depose-r3*  ln(G3*/|d|)")
    for mc in (2, 3, 4, 5, 6):
        k = C.kappa_pour_m_bord(0, 0, mc)[0]
        lam = k * XC / (M.P * PH.tau(0, 0, 0)); M0 = (2.0 * lam) ** (-2.0 / 3.0)
        lpd = PH.phi_fc(k, 0, 0)["ln_Phi"]; ps = plateau_phi(k, 0, 0); ferme = -B * M0 + C0 * math.log(M0) + D0
        for d in (-0.02, -0.01, -0.005, 0.005, 0.01, 0.02):
            k, w2, df, g = cellule_du_vide(mc, d); tb, t3 = tables(0, 0, w2, g)
            p = [plateau(tb, t3, o, lpd) for o in (1, 2, 3)]
            H, Wd, i0 = C.matrice(tb, t3, 0.0625, 3); dep = math.log(C.largeur(H, Wd, i0, abs(df), lpd)[0] / abs(df))
            rec = {"m_cible": mc, "kappa": k, "M0": M0, "delta": df, "g": g, "m_bord": tb["m2_bord"], "ln_Phi_deposee": lpd, "ln_Phi_etoile": ps["mediane"], "etendue_Phi_etoile": ps["etendue"],
                   "forme_fermee": ferme, "ordres": {str(o): {"plateau": p[o - 1]["mediane"], "etendue": p[o - 1]["etendue"], "centrale": p[o - 1]["centrale"]} for o in (1, 2, 3)},
                   "ln_G3_depose": dep, "Gamma3_etoile": abs(df) * math.exp(p[2]["mediane"])}
            out["B"].append(rec)
            print("   %d        %.5f   %+.4f          %+.4f   %.4f   %+.4f   %+.4f    | %+.3f   %.3e   %+.4f (%.4f)  %+.4f (%.4f)  %+.4f (%.4f)   %+.4f       %+.4f" % (
                mc, k, lpd, ps["mediane"], ps["etendue"], ps["mediane"] - lpd, ferme - ps["mediane"], df, g,
                p[0]["mediane"] - ps["mediane"], p[0]["etendue"], p[1]["mediane"] - ps["mediane"], p[1]["etendue"], p[2]["mediane"] - ps["mediane"], p[2]["etendue"],
                dep - p[2]["mediane"], p[2]["mediane"]))

    print()
    print("C. Phi* (absorbeur adapte) contre Phi (regle deposee), etats excites")
    print("   etiquette  kappa    m_bord  ln Phi      ln Phi*     etendue   Phi* - Phi")
    for (n1, n2, ks) in ((6, 2, (0.30, 0.22, 0.15, 0.10)), (10, 3, (0.40, 0.30, 0.22)), (9, 3, (0.2986,)), (2, 1, (0.10, 0.05))):
        for k in ks:
            f = PH.phi_fc(k, n1, n2)
            if f is None:
                continue
            ps = plateau_phi(k, n1, n2)
            out["C"].append({"n1": n1, "n2": n2, "kappa": k, "m_bord": f["m_bord"], "ln_Phi": f["ln_Phi"], "ln_Phi_etoile": ps["mediane"], "etendue": ps["etendue"]})
            print("   (%2d,%2d)   %.4f   %3d    %+.4f   %+.4f   %.4f   %+.4f" % (n1, n2, k, f["m_bord"], f["ln_Phi"], ps["mediane"], ps["etendue"], ps["mediane"] - f["ln_Phi"]))
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
