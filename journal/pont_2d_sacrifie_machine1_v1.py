# -*- coding: ascii -*-
"""LE PONT EN DEUX DIMENSIONS, A UN POINT SACRIFIE -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3. EXPLORATION, PAS UN RUN.
Premiere lecture 2D du systeme a fantome FERME (boite coupee, AUCUN absorbeur). Point : w2 = 101/50, la cellule de pre-vol PV3
du gel "largeur du vide" (un centieme, exclu de tout tirage ; seul son jumeau sans fantome y avait ete lu). Ce point est
declare SACRIFIE : il ne pourra servir a aucun gel sur le systeme ferme.
ON REGARDE : dans la boite N x N fermee, on ajoute une energie u au dernier site de l'echelle, (2 M, M), M = (N - 1) // 2, et on
la fait defiler (u = |t_(M-1)| tan theta). A chaque theta le spectre ENTIER est calcule (matrice dense reelle symetrique) ;
l'etat du vide est celui de plus grand poids sur (0, 0). Chaque changement de rang de cet etat est un croisement : il est
localise par dichotomie, et sa demi-largeur V est lue.
ATTENDU, ECRIT AVANT LE CALCUL : il y a un croisement dominant, ou les deux etats portent chacun la moitie du poids de (0, 0), et
        -0.05 <= ln( V^2 T / Gamma ) <= +0.03 ,
Gamma etant le plateau de la chaine d'ordre 3 sous absorbeur a ce point (aucune largeur 2D n'y a ete lue) et T le temps
classique du premier ordre jusqu'au site M. S'il y a d'autres croisements (autres canaux), ils sont listes.
Usage : python3 -I -B pont_2d_sacrifie_machine1_v1.py <moteur> <sonde deposee du lecteur> <bloc ordre 2> <bloc ordre 3>
        <bloc adapte> <w2> <g> <sortie.json> <N>..."""
import sys, math, json, time, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
import mpmath as mp
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.optimize import brentq
MOTEUR, S_LECT, BLOC2, BLOC3, BLOC_A, W2S, GS, SORTIE = sys.argv[1:9]; BOITES = [int(x) for x in sys.argv[9:]]
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
w2 = F(W2S); g = float(GS); delta = float(w2) - 2.0; ad = abs(delta)
sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb); p3 = plateau_adapte(tb, t3); G = math.exp(p3["ln_G"])
print("point w2 = %s, g = %s : barriere de %d barreaux ; chaine d'ordre 3 sous absorbeur : Gamma = %.4e (etendue %.4f)" % (W2S, GS, tb["m2_bord"], G, p3["etendue"]), flush=True)

def temps_classique(E, N):
    d = tb["d"]; ms = sorted(m for m in tb["t"] if m >= 0); spl = CubicSpline(np.log(np.array(ms) + 0.5), np.log(np.abs([tb["t"][m] for m in ms])))
    t = lambda m: math.exp(float(spl(math.log(m)))); f = lambda m: 4.0 * t(m) ** 2 - (E - m * d) ** 2
    gr = np.linspace(0.6, float(N), 4000); s = [f(m) for m in gr]; k = max(i for i in range(len(gr) - 1) if s[i] < 0 <= s[i + 1])
    m0 = brentq(f, gr[k], gr[k + 1], xtol=1e-14)
    I, err = quad(lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300)), 0.0, math.sqrt(N - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I, m0

def balayer(Hd, i_bord, ech, i_vide, n_grille=241):  # 241 pour la chaine, 61 pour la boite 2D (un croisement attendu par balayage)
    """Tous les changements de rang de l'etat de plus grand poids sur le site du vide, quand u defile au site de bord."""
    def lire(theta):
        H = Hd.copy(); H[i_bord, i_bord] += ech * math.tan(theta); val, vec = np.linalg.eigh(H); return val, vec[i_vide, :] ** 2, vec
    rang = lambda th: int(np.argmax(lire(th)[1]))
    grille = np.linspace(-1.5, 1.5, n_grille); rangs = [rang(th) for th in grille]; res = []
    for k in range(len(grille) - 1):
        if rangs[k] == rangs[k + 1]:
            continue
        lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rangs[k]
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if mi == lo or mi == hi:
                break
            lo, hi = (mi, hi) if rang(mi) == rlo else (lo, mi)
        val, p, vec = lire(0.5 * (lo + hi)); o = np.argsort(-p)[:2]; i, j = sorted(int(x) for x in o)
        res.append({"theta": 0.5 * (lo + hi), "u": ech * math.tan(0.5 * (lo + hi)), "saut_de_rang": rangs[k + 1] - rangs[k], "adjacents": bool(j == i + 1), "V": float(0.5 * (val[j] - val[i])),
                    "E": float(0.5 * (val[i] + val[j])), "poids": [float(p[i]), float(p[j])], "norme": float(max(abs(val[0]), abs(val[-1])))})
    val, p, vec = lire(0.0); iv = int(np.argmax(p))
    return res, {"E_vide": float(val[iv]), "poids_site": float(p[iv]), "vecteur": vec[:, iv], "voisins": [float(val[iv - 1]), float(val[iv + 1])]}

out = {"piece": "pont_2d_sacrifie_machine1_v1", "w2": W2S, "g": GS, "m_bord": tb["m2_bord"], "Gamma_chaine_ordre3": G, "etendue": p3["etendue"], "boites": []}
for N in BOITES:
    t0 = time.time(); Mb = (N - 1) // 2; ech = abs(tb["t"][Mb - 1]); Tc, m0 = temps_classique(0.0, Mb); Vp = math.sqrt(G / Tc)
    # la chaine fermee du premier ordre et de l'ordre 3, coupee au meme site
    ch = {}
    for ordre in (1, 3):
        Hc = np.zeros((Mb + 1, Mb + 1))
        for m in range(Mb + 1):
            Hc[m, m] = m * tb["d"] + ((tb["S"][m] - tb["S"][0]) if ordre == 3 else 0.0)
            if m < Mb:
                x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); Hc[m, m + 1] = x; Hc[m + 1, m] = x
            if ordre == 3:
                for pas, tab in ((2, tb["U"]), (3, t3["W3"]), (5, t3["W5"])):
                    if m + pas <= Mb:
                        Hc[m, m + pas] = tab[m]; Hc[m + pas, m] = tab[m]
        rc, _ = balayer(Hc, Mb, ech, 0); ch[ordre] = [{k: v for k, v in r.items()} for r in rc]
    # la boite 2D fermee
    H0, diag = assembler(w2, g, N, signe=-1); Hd = H0.toarray() + np.diag(diag); i_bord = (2 * Mb) * N + Mb
    res, nu = balayer(Hd, i_bord, ech, 0, n_grille=61)
    psi2 = nu["vecteur"] ** 2; dedans = sum(psi2[a * N + b] for a in range(N) for b in range(N) if b <= tb["m2_bord"] + 1); dt = time.time() - t0
    print("boite %d x %d (%d etats), dernier site de l'echelle (%d, %d), %.0f s : T = %.2f, sortie de barriere %.2f, V attendu = racine(Gamma / T) = %.4e" % (N, N, N * N, 2 * Mb, Mb, dt, Tc, m0, Vp))
    print("   boite nue (u = 0) : energie du vide %+.3e ; poids sur (0, 0) %.6f ; poids hors des %d premiers barreaux : %.2e ; niveaux voisins a %+.4f et %+.4f (en |delta| : %+.2f, %+.2f)" % (
        nu["E_vide"], nu["poids_site"], tb["m2_bord"] + 1, 1.0 - dedans, nu["voisins"][0] - nu["E_vide"], nu["voisins"][1] - nu["E_vide"], (nu["voisins"][0] - nu["E_vide"]) / ad, (nu["voisins"][1] - nu["E_vide"]) / ad))
    for nom, liste in (("chaine fermee, ordre 1", ch[1]), ("chaine fermee, ordre 3", ch[3]), ("BOITE 2D FERMEE      ", res)):
        for r in liste:
            print("   %s : croisement a u = %+.4e ; V = %.4e ; poids %.3f / %.3f ; adjacents %s ; ln(V^2 T / Gamma) = %+.4f ; ecart/bruit %.1e" % (
                nom, r["u"], r["V"], r["poids"][0], r["poids"][1], r["adjacents"], math.log(r["V"] ** 2 * Tc / G), 2 * r["V"] / (2.2e-16 * r["norme"])), flush=True)
        if not liste:
            print("   %s : aucun croisement" % nom)
    out["boites"].append({"N": N, "M": Mb, "T": Tc, "sortie": m0, "V_attendu": Vp, "boite_nue": {k: v for k, v in nu.items() if k != "vecteur"}, "poids_hors_barriere": 1.0 - dedans,
                          "chaine_ordre1": ch[1], "chaine_ordre3": ch[3], "boite_2d": res, "duree_s": dt})
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
