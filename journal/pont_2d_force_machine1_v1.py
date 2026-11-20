# -*- coding: ascii -*-
"""LE PONT EN 2D : OU EST PASSEE LA FORCE ? -- machine 1, v1, 2026-11-16. HORS CHAINE, classe 3, au point SACRIFIE w2 = 101/50.
Le premier regard 2D (pont_2d_sacrifie_machine1_v1.py) a FAUSSE l'attendu dans 4 boites sur 7 : au croisement trouve, la
demi-largeur V est bien plus petite que racine(Gamma / T) des que la boite depasse une trentaine de quanta. Deux lectures :
la force du couplage est PERDUE (la largeur sous absorbeur ne dirait alors rien du systeme ferme), ou elle est PARTAGEE entre
plusieurs niveaux du dehors (le dehors 2D n'est plus une echelle). Ce script les departage sans balayage :
  dans la boite fermee nue, chaque niveau k du dehors porte un poids c_k^2 sur (0, 0) ; V_k = |c_k| |E_k - E_a| est son couplage
  au vide (premier ordre, valable loin du croisement). Sous absorbeur, la meme grandeur est lisse : Gamma(E) / (2 pi) =
  (E - E_a)^2 rho(E), rho etant la densite locale de (0, 0) dans la chaine d'ordre 3 sous absorbeur adapte.
  REGLE DE SOMME ATTENDUE SI LA FORCE EST PARTAGEE : par fenetre d'energie, la moyenne sur les tailles de boite de la somme des
  V_k^2 vaut l'integrale de Gamma(E) / (2 pi). Les chaines fermees (ordre 1, ordre 3), coupees au meme site, servent de controle.
Fenetres : du cote des energies opposees a delta (aucun etat localise sous la barriere n'y tombe), de 0.05 a 8 |delta| du vide.
Usage : python3 -I -B pont_2d_force_machine1_v1.py <moteur> <sonde deposee du lecteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>
        <w2> <g> <N min> <N max> <sortie.json>"""
import sys, math, json, importlib.util
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sl
import mpmath as mp
MOTEUR, S_LECT, BLOC2, BLOC3, BLOC_A, W2S, GS, NMIN, NMAX, SORTIE = sys.argv[1:11]; NMIN, NMAX = int(NMIN), int(NMAX)
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
            V2 = c2[k] * (val[k] - Ev) ** 2 / w0; Gk = 2 * math.pi * (val[k] - Ev) ** 2 * rho(val[k]); res.append((float(x), float(V2), float(V2 * Tc / Gk)))
    return res

H0m, dm = assembler(w2, g, NMAX, signe=-1)
out = {"piece": "pont_2d_force_machine1_v1", "w2": W2S, "g": GS, "Gamma": G, "bornes": BORNES, "lisse": L, "boites": []}
som = {"2d": np.zeros(len(L)), "ch1": np.zeros(len(L)), "ch3": np.zeros(len(L))}; cnt = {"2d": np.zeros(len(L)), "ch1": np.zeros(len(L)), "ch3": np.zeros(len(L))}; nb = 0
print("N    M   poids du vide  niveau le plus proche (en |delta|) et son 2 pi V^2 T / Gamma-equivalent   niveaux 2D par fenetre")
for N in range(NMIN, NMAX + 1):
    Mb = (N - 1) // 2; H0, d = restreindre(H0m, dm, NMAX, N); Hd = H0.toarray() + np.diag(d); val, vec = np.linalg.eigh(Hd)
    S2, n2, w0, pr = forces(val, vec[0, :] ** 2); rec = {"N": N, "M": Mb, "poids_vide": w0, "proche": pr, "S_2d": S2, "n_2d": n2}
    Tc = 2 * math.pi / (2.9 * ad); rec["niveaux_2d"] = par_niveau(val, vec[0, :] ** 2, Tc)
    v3, e3 = np.linalg.eigh(chaine(Mb, 3)); rec["niveaux_ch3"] = par_niveau(v3, e3[0, :] ** 2, Tc); v1, e1 = np.linalg.eigh(chaine(Mb, 1)); rec["niveaux_ch1"] = par_niveau(v1, e1[0, :] ** 2, Tc)
    for nom, ordre in (("ch1", 1), ("ch3", 3)):
        v, e = np.linalg.eigh(chaine(Mb, ordre)); Sc, nc, _, _ = forces(v, e[0, :] ** 2); som[nom] += Sc; cnt[nom] += nc; rec["S_" + nom] = Sc
    som["2d"] += S2; cnt["2d"] += n2; nb += 1; out["boites"].append(rec)
    print("%-3d  %-2d  %.6f       %+7.2f   V^2 = %.3e                                              %s" % (N, Mb, w0, pr[0] / ad, pr[1], n2), flush=True)
print("%d boites. Par fenetre (ecart au vide en |delta|, cote oppose a delta) : lisse = integrale de Gamma(E)/(2 pi) ; moyenne sur les boites de la somme des V_k^2" % nb)
print("fenetre        lisse        boite 2D : moyenne  rapport  niveaux    chaine ordre 3 : moyenne  rapport  niveaux    chaine ordre 1 : rapport")
tot = {"lisse": 0.0, "2d": 0.0, "ch1": 0.0, "ch3": 0.0}
for i in range(len(L)):
    m2, m3, m1 = som["2d"][i] / nb, som["ch3"][i] / nb, som["ch1"][i] / nb; tot["lisse"] += L[i]; tot["2d"] += m2; tot["ch3"] += m3; tot["ch1"] += m1
    print("%4.2f a %4.2f   %.3e    %.3e           %6.3f   %-3d        %.3e                 %6.3f   %-3d        %6.3f" % (BORNES[i], BORNES[i + 1], L[i], m2, m2 / L[i], int(cnt["2d"][i]), m3, m3 / L[i], int(cnt["ch3"][i]), m1 / L[i]))
print("ENSEMBLE       %.3e    %.3e           %6.3f              %.3e                 %6.3f              %6.3f" % (tot["lisse"], tot["2d"], tot["2d"] / tot["lisse"], tot["ch3"], tot["ch3"] / tot["lisse"], tot["ch1"] / tot["lisse"]))
import statistics
for nom, cle in (("BOITE 2D", "niveaux_2d"), ("chaine ordre 3", "niveaux_ch3"), ("chaine ordre 1", "niveaux_ch1")):
    r = sorted(x[2] for b in out["boites"] for x in b[cle])
    print("part de la force d'un canal portee par un niveau, V_k^2 T / Gamma(E_k), %s : %d niveaux ; min %.3g ; quartiles %.3g / %.3g / %.3g ; max %.3g ; moyenne %.3g" % (
        nom, len(r), r[0], r[len(r) // 4], statistics.median(r), r[(3 * len(r)) // 4], r[-1], sum(r) / len(r)))
out["moyennes"] = {k: (v / nb).tolist() for k, v in som.items()}; out["comptes"] = {k: v.tolist() for k, v in cnt.items()}; out["boites_n"] = nb
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
