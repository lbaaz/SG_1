# -*- coding: ascii -*-
"""LE PONT, SECONDE PASSE : QUEL ESPACEMENT ? -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3, chaine du premier ordre seule.
La premiere passe (pont_ferme_absorbeur_machine1_v1.py) a FAUSSE l'attendu ecrit avant elle : avec l'espacement D lu sur les deux
niveaux voisins, 2 pi V^2 / D depasse Gamma de 12 a 25 pour cent, d'autant plus que la barriere est profonde, et de la meme facon
aux quatre desaccords. Lecture APRES COUP, eprouvee ici sans parametre : l'espacement qui entre dans la regle d'or n'est pas la
distance aux voisins mais dE/dk, la derivee de l'energie par rapport au numero du niveau a condition de bord fixee, c'est-a-dire
2 pi / T, T etant le temps classique d'aller et retour entre la sortie de la barriere et le bout de la chaine :
        T(E) = 2 Integrale dm / racine( 4 t(m)^2 - (E - m d)^2 ) ,   Gamma = V^2 T .
Trois lectures de l'espacement, par croisement : (a) voisins ; (b) dE/dk par differences centrees a 5 et 7 points sur les niveaux
de la chaine fermee ; (c) 2 pi / T, T calcule sur les sauts t_m du moteur, sans rien lire du spectre.
Usage : python3 -I -B pont_semiclassique_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte> <table gelee.json>
        <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
from scipy.interpolate import CubicSpline
from scipy.integrate import quad
from scipy.optimize import brentq
MOTEUR, BLOC2, BLOC3, BLOC_A, TABLE, SORTIE = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in (BLOC2, BLOC3, BLOC_A):
    exec(compile(open(bloc, encoding="ascii").read(), bloc, "exec"))
T = json.load(open(TABLE)); CELLULES = [c for c in T["cellules"] if c["ligne"] == "lisible"]
COUPURES = [(c, L) for c in (6, 8, 10) for L in (16, 20, 24)]

def absorbeur_ordre1(tb):
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
    s = sorted(v); return 0.5 * (s[len(s) // 2 - 1] + s[len(s) // 2])

def croisement(H0, echelle):
    def lire(theta):
        H = H0.copy(); H[-1, -1] += echelle * math.tan(theta); val, vec = np.linalg.eigh(H); return val, vec[0, :] ** 2
    rang = lambda th: int(np.argmax(lire(th)[1]))
    grille = np.linspace(-1.5, 1.5, 241); rangs = [rang(th) for th in grille]
    for k in range(len(grille) - 1):
        if rangs[k] == rangs[k + 1]:
            continue
        lo, hi, rlo = float(grille[k]), float(grille[k + 1]), rangs[k]
        for _ in range(200):
            mi = 0.5 * (lo + hi)
            if mi == lo or mi == hi:
                break
            lo, hi = (mi, hi) if rang(mi) == rlo else (lo, mi)
        val, p = lire(0.5 * (lo + hi)); i, j = sorted(int(x) for x in np.argsort(-p)[:2])
        if j != i + 1 or i - 3 < 0 or j + 3 >= len(val):
            continue
        E = lambda q: (0.5 * (val[i] + val[j]) if q == 0 else (val[j + q] if q > 0 else val[i + q]))   # niveau du dehors numero k + q
        return {"V": float(0.5 * (val[j] - val[i])), "E": float(E(0)), "D_voisins": float(0.5 * (E(1) - E(-1))),
                "D_5": float((-E(2) + 8 * E(1) - 8 * E(-1) + E(-2)) / 12.0), "D_7": float((E(3) - 9 * E(2) + 45 * E(1) - 45 * E(-1) + 9 * E(-2) - E(-3)) / 60.0),
                "niveaux": [float(E(q)) for q in range(-3, 4)]}
    return None

def temps_classique(tb, E, N):
    """T(E) = 2 Int dm / racine(4 t(m)^2 - (E - m d)^2), de la sortie de la barriere au bout de la chaine (m = N). Le saut entre
    les sites m et m + 1 est place en m + 1/2 ; ln t est interpole en ln(m + 1/2) par une spline cubique."""
    d = tb["d"]; ms = sorted(m for m in tb["t"] if m >= 0); x = np.log(np.array(ms) + 0.5); y = np.log(np.abs([tb["t"][m] for m in ms]))
    sp = CubicSpline(x, y); t = lambda m: math.exp(float(sp(math.log(m))))
    f = lambda m: 4.0 * t(m) ** 2 - (E - m * d) ** 2
    # sortie de la barriere : le dernier changement de signe de f en montant
    grille = np.linspace(0.6, float(N), 4000); s = [f(m) for m in grille]; k = max(i for i in range(len(grille) - 1) if s[i] < 0 <= s[i + 1])
    m0 = brentq(f, grille[k], grille[k + 1], xtol=1e-14)
    g = lambda u: 2.0 * u / math.sqrt(max(f(m0 + u * u), 1e-300))            # m = m0 + u^2 : la singularite en racine est levee
    I, err = quad(g, 0.0, math.sqrt(N - m0), limit=400, epsabs=0, epsrel=1e-10)
    return 2.0 * I, m0

out = {"piece": "pont_semiclassique_machine1_v1", "cellules": []}
print("cellule  m  N   Gamma abs     V           E du croisement  espacement / |delta| : voisins  5 pts   7 pts   2 pi / T    ln R : voisins  5 pts    7 pts    2 pi/T     sortie")
for c in CELLULES:
    w2 = F(c["w2"]); g = float(c["g"]); sites = M.barriere(0, 0, w2, g, True); tb = tables_ordre2(0, 0, w2, g, sites)
    lnG = absorbeur_ordre1(tb); G = math.exp(lnG); ad = abs(c["delta"]); rec = {"id": c["id"], "m_bord": tb["m2_bord"], "delta": c["delta"], "ln_G_absorbeur_ordre1": lnG, "croisements": []}
    for (cc, L) in COUPURES:
        N = tb["m2_bord"] + cc + L; n = N + 1; H0 = np.zeros((n, n))
        for m in range(N + 1):
            H0[m, m] = m * tb["d"]
            if m < N:
                H0[m, m + 1] = tb["t"][m]; H0[m + 1, m] = tb["t"][m]
        r = croisement(H0, abs(tb["t"][N - 1]))
        if r is None:
            continue
        Tc, m0 = temps_classique(tb, r["E"], N); r["D_T"] = 2 * math.pi / Tc; r["sortie_de_barriere"] = m0; r["N"] = N
        for cle in ("D_voisins", "D_5", "D_7", "D_T"):
            r["ln_R_" + cle[2:]] = math.log(2 * math.pi * r["V"] ** 2 / r[cle]) - lnG
        r["Gamma_T_sur_V2"] = G * Tc / r["V"] ** 2
        rec["croisements"].append(r)
        print("%-7s  %d  %-3d %.4e    %.4e  %+.3e                              %.3f    %.3f   %.3f   %.3f              %+.4f   %+.4f  %+.4f  %+.4f    %.2f" % (
            c["id"], tb["m2_bord"], N, G, r["V"], r["E"], r["D_voisins"] / ad, r["D_5"] / ad, r["D_7"] / ad, r["D_T"] / ad, r["ln_R_voisins"], r["ln_R_5"], r["ln_R_7"], r["ln_R_T"], m0), flush=True)
    out["cellules"].append(rec)
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
