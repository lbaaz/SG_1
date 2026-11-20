# -*- coding: ascii -*-
"""LE PONT ENTRE LA LARGEUR SOUS ABSORBEUR ET LE SYSTEME FERME -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3 : une chaine
a une dimension, aucune 2D, aucun run, aucune cellule jugee.
QUESTION. La chaine fermee (coupee au site N, SANS absorbeur) est reelle symetrique : son spectre est discret, l'etat porte
par le site 0 n'y a pas de largeur. Que devient la largeur Gamma lue sous absorbeur ?
ATTENDU, ECRIT AVANT LE CALCUL (golden rule a spectre discret, Bixon-Jortner) : l'etat du site 0, d'energie E_a, est couple
aux niveaux de la region d'apres la barriere, d'espacement local D, par un element V ; alors
        Gamma = 2 pi V^2 / D .
Dans la chaine fermee, V se lit comme la demi-largeur du croisement evite entre l'etat du site 0 et un niveau du dehors,
quand on fait defiler les niveaux du dehors par un parametre de bord u (energie ajoutee au dernier site : u parcourt la
famille des conditions de bord reflechissantes). D se lit comme la demi-distance entre les deux niveaux voisins de la paire.
Le rapport R = 2 pi V^2 / (D Gamma_absorbeur) doit valoir 1 a chaque croisement, quels que soient N, la cellule et l'ordre.
MESURE. Par cellule (table gelee du gel "largeur du vide", cellules lisibles), par ordre (1 : diagonale m delta et sauts t_m ;
3 : la chaine des blocs deposes), par coupure N = m_bord + c + L : le croisement est localise par dichotomie sur theta
(u = |t_N| tan theta) jusqu'a la precision de la machine ; V, D, R.
Usage : python3 -I -B pont_ferme_absorbeur_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <table gelee.json>
        <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, TABLE, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
T = json.load(open(TABLE)); CELLULES = [c for c in T["cellules"] if c["ligne"] == "lisible"]
COUPURES = [(c, L) for c in (6, 8, 10) for L in (16, 20, 24)]

def fermee(tb, t3, N, ordre):
    """Chaine fermee, sites m_min..N, reelle symetrique."""
    d, m_min = tb["d"], tb["m_min"]; n = N - m_min + 1; H = np.zeros((n, n))
    for m in range(m_min, N + 1):
        i = m - m_min; H[i, i] = m * d + ((tb["S"][m] - tb["S"][0]) if ordre == 3 else 0.0)
        if m < N:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); H[i, i + 1] = x; H[i + 1, i] = x
        if ordre == 3:
            for pas, tab in ((2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
                if m + pas <= N:
                    H[i, i + pas] = tab[m]; H[i + pas, i] = tab[m]
    return H, -m_min

def absorbeur_ordre1(tb):
    """Plateau du premier ordre sous l'absorbeur adapte : mediane des dix-huit ln Gamma (flux)."""
    d, m_min = tb["d"], tb["m_min"]; v = []
    for (a, c, L) in VARIANTES_ADAPTEES:
        debut = tb["m2_bord"] + c; Mh = debut + L; n = Mh - m_min + 1
        H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
        for m in range(m_min, Mh + 1):
            i = m - m_min; H[i, i] = m * d
            if m > debut:
                Wd[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2; H[i, i] += -1j * Wd[i]
            if m < Mh:
                H[i, i + 1] = tb["t"][m]; H[i + 1, i] = tb["t"][m]
        val, vec = np.linalg.eig(H); poids = np.abs(vec[-m_min, :]) ** 2; nu = np.lexsort((val.real, -poids))[0]
        psi2 = np.abs(vec[:, nu]) ** 2; v.append(math.log(float(2.0 * (Wd @ psi2) / psi2.sum())))
    s = sorted(v); return 0.5 * (s[len(s) // 2 - 1] + s[len(s) // 2]), s[-1] - s[0]

def croisement(H0, i0, echelle):
    """Fait defiler u = echelle tan(theta) ; rend le croisement evite de l'etat du site 0 avec un niveau du dehors."""
    def lire(theta):
        H = H0.copy(); H[-1, -1] += echelle * math.tan(theta); val, vec = np.linalg.eigh(H); p = vec[i0, :] ** 2
        return val, p
    def rang(theta):
        val, p = lire(theta); return int(np.argmax(p))
    grille = np.linspace(-1.5, 1.5, 241); rangs = [rang(th) for th in grille]
    sauts = [k for k in range(len(grille) - 1) if rangs[k] != rangs[k + 1]]
    res = []
    for k in sauts:
        lo, hi = float(grille[k]), float(grille[k + 1]); rlo = rangs[k]
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if mi == lo or mi == hi:
                break
            if rang(mi) == rlo:
                lo = mi
            else:
                hi = mi
        val, p = lire(0.5 * (lo + hi)); o = np.argsort(-p)[:2]; i, j = sorted(int(x) for x in o)
        if j != i + 1 or i - 1 < 0 or j + 1 >= len(val):
            continue
        V = 0.5 * (val[j] - val[i]); D = 0.5 * (val[j + 1] - val[i - 1])
        res.append({"theta": 0.5 * (lo + hi), "V": float(V), "D": float(D), "poids": [float(p[i]), float(p[j])], "E": float(0.5 * (val[i] + val[j])),
                    "voisins": [float(val[i - 1]), float(val[j + 1])]})
    # loin du croisement : le plus grand poids du site 0, et le plus petit, sur la grille
    pm = [float(np.max(lire(th)[1])) for th in grille]
    return res, max(pm), min(pm)

out = {"piece": "pont_ferme_absorbeur_machine1_v1", "cellules": []}
print("cellule  ordre  N   Gamma absorbeur  V           D         D/|delta|  2 pi V^2 / D   ln R      poids au croisement")
for c in CELLULES:
    w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb)
    p3 = plateau_adapte(tb, t3); lnG = {3: p3["ln_G"], 1: absorbeur_ordre1(tb)[0]}
    rec = {"id": c["id"], "w2": c["w2"], "g": c["g"], "delta": c["delta"], "m_bord": tb["m2_bord"], "ln_G_absorbeur": {str(k): v for k, v in lnG.items()}, "croisements": []}
    for ordre in (1, 3):
        for (cc, L) in COUPURES:
            N = tb["m2_bord"] + cc + L; H0, i0 = fermee(tb, t3, N, ordre); ech = abs(tb["t"][N - 1])
            res, pmax, pmin = croisement(H0, i0, ech)
            for r in res:
                Gp = 2 * math.pi * r["V"] ** 2 / r["D"]; lnR = math.log(Gp) - lnG[ordre]
                rec["croisements"].append(dict(r, ordre=ordre, N=N, c=cc, L=L, Gamma_pont=Gp, ln_R=lnR, poids_max_hors=pmax))
                print("%-7s  %d      %-3d %.4e       %.4e  %.5f   %.3f      %.4e     %+.4f   %.3f %.3f" % (
                    c["id"], ordre, N, math.exp(lnG[ordre]), r["V"], r["D"], r["D"] / abs(c["delta"]), Gp, lnR, r["poids"][0], r["poids"][1]), flush=True)
    out["cellules"].append(rec)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
