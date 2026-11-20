# -*- coding: ascii -*-
"""LE PONT EN 2D : LE DEHORS CONTINUE-T-IL DE SE PEUPLER ? -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3, point SACRIFIE.
Jusqu'au cote 64 (diagonalisation complete), le nombre de niveaux du dehors dans la fenetre de 0.05 a 8 |delta| croit avec le
cote (droite ajustee : pente +0.084 par quantum, 4.6 niveaux par boite aux cotes 57 a 64) et la somme reponderee reste a 1.
La conjecture de la note (le grand bocal 2D tend vers une vraie desintegration) repose sur la poursuite de cette croissance.
Ici : boites plus grandes, par decalage-inversion creuse autour de la fenetre (pas de diagonalisation complete).
Chaque boite est resolue DEUX fois, a deux decalages (2 et 5 |delta| sous le vide) ; un niveau n'est compte fiable que si ses
deux lectures de y s'accordent a 2 pour cent pres. Controle : le cote 64 doit rendre ce que rend la diagonalisation complete.
ATTENDU ECRIT AVANT DE LANCER (droite des cotes 21 a 64 prolongee : 7.8 niveaux au cote 100, 12.0 au cote 150) :
  E1  aux cotes 150 et 151, entre 9 et 15 niveaux dans la fenetre (moyenne des deux boites). Six ou moins : la croissance sature,
      et la conjecture tombe.
  E2  somme des y / 7.95, moyennee sur les boites de cote >= 72 : entre 0.85 et 1.15.
  E3  participation moyenne aux cotes >= 128 superieure a celle des cotes 57 a 64 (3.15).
Usage : python3 -I -B pont_2d_grand_machine1_v1.py <moteur> <sonde deposee du lecteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>
        <w2> <g> <sortie.json> <cote> [<cote> ...]"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
import mpmath as mp
MOTEUR, S_LECT, BLOC2, BLOC3, BLOC_A, W2S, GS, SORTIE = sys.argv[1:9]; COTES = [int(x) for x in sys.argv[9:]]; NMAX = max(COTES)
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):
    cle = (p, k, l, n1, n2, w2)
    if cle not in _cache:
        _cache[cle] = _brut(p, k, l, n1, n2, w2)
    return _cache[cle]
M.X_saut_reel = _X
src = open(S_LECT, encoding="utf-8").read(); exec(compile(src[src.index("# --- LECTEUR CREUX"):src.index("# --- fin du bloc ---")], "bloc_lecteur", "exec"))
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
w2 = F(W2S); g = float(GS); delta = float(w2) - 2.0; ad = abs(delta); sg = 1.0 if delta > 0 else -1.0
sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb); p3 = plateau_adapte(tb, t3); G = math.exp(p3["ln_G"])
BORNES = [0.05, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0, 8.0]          # en |delta|, du cote oppose a delta

def chaine(N, ordre, absorbe=None):
    H = np.zeros((N + 1, N + 1), dtype=complex if absorbe else float)
    for m in range(N + 1):
        H[m, m] = m * tb["d"] + ((tb["S"][m] - tb["S"][0]) if ordre == 3 else 0.0)
        if absorbe and m > absorbe[0]:
            H[m, m] += -1j * absorbe[1] * abs(tb["t"][m]) * ((m - absorbe[0]) / float(absorbe[2])) ** 2
        if m < N:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); H[m, m + 1] = x; H[m + 1, m] = x
        if ordre == 3:
            for pas, tab in ((2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
                if m + pas <= N:
                    H[m, m + pas] = tab[m]; H[m + pas, m] = tab[m]
    return H

# --- le lisse : chaine d'ordre 3 sous absorbeur adapte (a = 2, c = 8, L = 24), densite locale de (0, 0)
debut = tb["m2_bord"] + 8; Ha = chaine(debut + 24, 3, absorbe=(debut, 2.0, 24)); va, ve = np.linalg.eig(Ha); ia = int(np.argmax(np.abs(ve[0, :]) ** 2)); Ea = float(va[ia].real)
def rho(E):
    x = np.linalg.solve(E * np.eye(Ha.shape[0]) - Ha, np.eye(Ha.shape[0])[:, 0]); return -x[0].imag / math.pi    # -(1/pi) Im <0|(E - H)^-1|0>
def lisse(x1, x2, n=400):
    """Integrale de (E - Ea)^2 rho(E) entre Ea - sg x2 |delta| et Ea - sg x1 |delta| (trapezes en ln de l'ecart)."""
    xs = np.exp(np.linspace(math.log(x1), math.log(x2), n)); f = [((x * ad) ** 2) * rho(Ea - sg * x * ad) for x in xs]
    return float(np.trapezoid(np.array(f) * xs * ad, np.log(xs)))
L = [lisse(BORNES[i], BORNES[i + 1]) for i in range(len(BORNES) - 1)]
print("point w2 = %s, g = %s ; Gamma (chaine d'ordre 3, plateau) = %.4e ; (E - Ea)^2 rho juste sous le vide, fois 2 pi : %.4e" % (W2S, GS, G, 2 * math.pi * (0.05 * ad) ** 2 * rho(Ea - sg * 0.05 * ad)))

def forces(val, c2):
    """Couplages V_k^2 = c_k^2 (E_k - E_vide)^2 / poids du vide, ranges par fenetre du cote oppose a delta."""
    iv = int(np.argmax(c2)); Ev = val[iv]; w0 = c2[iv]; S = [0.0] * (len(BORNES) - 1); n = [0] * (len(BORNES) - 1); proche = None
    for k in range(len(val)):
        if k == iv:
            continue
        x = -sg * (val[k] - Ev) / ad
        if proche is None or abs(val[k] - Ev) < abs(proche[0]):
            proche = (float(val[k] - Ev), float(c2[k] * (val[k] - Ev) ** 2 / w0))
        for i in range(len(BORNES) - 1):
            if BORNES[i] <= x < BORNES[i + 1]:
                S[i] += c2[k] * (val[k] - Ev) ** 2 / w0; n[i] += 1
    return S, n, float(w0), proche

def par_niveau(val, c2, Tc):
    """Par niveau du cote oppose a delta : ecart au vide, V_k^2, et sa part de la force d'un canal : V_k^2 T / Gamma(E_k)."""
    iv = int(np.argmax(c2)); Ev = val[iv]; w0 = c2[iv]; res = []
    for k in range(len(val)):
        x = -sg * (val[k] - Ev) / ad
        if k != iv and BORNES[0] <= x < BORNES[-1]:
            V2 = c2[k] * (val[k] - Ev) ** 2 / w0; r = rho(Ea + (val[k] - Ev)); res.append((float(x), float(V2), float(c2[k] / (w0 * r * ad))))
    return res

import time
t0 = time.time(); H0m, dm = assembler(w2, g, NMAX, signe=-1); print("assemblage au cote %d : %.0f s" % (NMAX, time.time() - t0), flush=True)
LARG = BORNES[-1] - BORNES[0]; out = {"piece": "pont_2d_grand_machine1_v1", "w2": W2S, "g": GS, "bornes": BORNES, "boites": []}

def lire(H, sigma, k):
    """Niveaux proches de sigma, avec leur poids sur l'etat (0, 0)."""
    val, vec = sl.eigsh(H, k=k, sigma=sigma, which="LM", tol=0); o = np.argsort(val); return val[o], vec[0, o] ** 2

for N in COTES:
    t0 = time.time(); H0, d = restreindre(H0m, dm, NMAX, N); H = (H0 + sp.diags(d)).tocsc()
    v0, c0 = lire(H, 0.0, 8); iv = int(np.argmax(c0)); Ev = float(v0[iv]); w0 = float(c0[iv])
    lect = []
    kk = max(60, int(0.6 * N))                         # nombre de niveaux demandes autour de chaque decalage
    for dec, k in ((2.0, kk), (5.0, kk)):
        val, c2 = lire(H, Ev - sg * dec * ad, k); x = -sg * (val - Ev) / ad
        couvre = (x.min() < BORNES[0]) and (x.max() > BORNES[-1])
        lect.append({"couvre": bool(couvre), "niv": [(float(x[i]), float(c2[i] / (w0 * rho(Ea + (val[i] - Ev)) * ad))) for i in range(len(val)) if BORNES[0] <= x[i] < BORNES[-1]]})
    a, b = lect[0]["niv"], lect[1]["niv"]; fi = []; nf = 0
    if len(a) == len(b):
        for (xa, ya), (xb, yb) in zip(sorted(a), sorted(b)):
            ok = abs(xa - xb) < 1e-6 and abs(ya - yb) <= 0.02 * max(ya, yb, 1e-300); fi.append((xa, 0.5 * (ya + yb), bool(ok))); nf += 0 if ok else 1
    else:
        fi = [(xa, ya, False) for xa, ya in sorted(a)]; nf = len(fi)
    ys = [y for _, y, _ in fi]; tot = sum(ys) / LARG; part = (sum(ys) ** 2 / sum(y * y for y in ys)) if ys else 0.0
    rec = {"N": N, "E_vide": Ev, "poids_vide": w0, "niveaux": fi, "n": len(fi), "non_fiables": nf, "y_non_fiable_max": max([y for _, y, ok in fi if not ok] or [0.0]), "somme_sur_largeur": tot, "participation": part,
           "couvre": [lect[0]["couvre"], lect[1]["couvre"]], "memes_comptes": len(a) == len(b), "duree_s": time.time() - t0}
    out["boites"].append(rec)
    print("cote %-3d (%5d etats, %4.0f s)  poids du vide %.6f  niveaux %2d  non fiables %d (y max %.2g)  somme / %.2f = %.3f  participation %.2f  plus petit y %.2g  couvre %s  memes comptes %s" % (
        N, H.shape[0], rec["duree_s"], w0, len(fi), nf, rec["y_non_fiable_max"], LARG, tot, part, min(ys) if ys else 0.0, rec["couvre"], rec["memes_comptes"]), flush=True)
    json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
