# -*- coding: ascii -*-
"""L'ESQUISSE DU GEL "SOMMET" : ses cellules candidates passees au predicteur, A UNE DIMENSION -- machine 1, v1,
2026-11-22. Hors chaine, classe 3. AUCUN CALCUL 2D, aucune piece de gel : une esquisse a demolir.
Cellule candidate = (w2, kappa) ; couplage ecrit g = kappa |w2 - 2| P / X(w2) a six chiffres (regle du gel du vide).
  kappa : 0.0363 (2 barreaux), 0.0530 (1 barreau), 0.0800, 0.1300, 0.2000, 0.4000, 1.0000 (fenetre sans barriere)
  |w2 - 2| : 0.5, 1.0, 1.5, 2.0 dix-milliemes (creneaux MP, PP) ; 2.5 a 5.0 par pas de 0.5 (creneaux MG, PG) ;
             w2 = 2.0001 retire (point de qualification, sacrifie).
Par cellule : barriere du moteur (m_bord, 0 si elle est vide), chaine d'ordre 3 sous l'absorbeur adapte du bloc depose
(plateau et etendue des dix-huit variantes), ordres 2 et 1, premier site ou le saut depasse 1 (m*), debut des absorbeurs
du lecteur sur l'echelle (r_c / 2), eta0 de la regle en absolu.
Usage : python3 -I -B esquisse_gel_sommet_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>"""
import sys, math, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A = sys.argv[1:5]
CANONS = {"moteur": "82a0be882568fe0c", "bloc2": "7cd5977bc27bebc1", "bloc3": "534ba246aa3b8973", "bloc_adapte": "49a40d9098b55361"}
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
for nom, chemin in (("moteur", MOTEUR), ("bloc2", BLOC2), ("bloc3", BLOC3), ("bloc_adapte", BLOC_A)):
    if canon_B(chemin) != CANONS[nom]:
        raise SystemExit("REFUS : %s n'est pas au canon %s" % (nom, CANONS[nom]))
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
KAPPA3 = 0.0262
KAPPAS = ((0.0363, 2), (0.0530, 1), (0.0800, 0), (0.1300, 0), (0.2000, 0), (0.4000, 0), (1.0000, 0))
CRENEAUX = (("MP", -1, ("0.00005", "0.00010", "0.00015", "0.00020")), ("PP", +1, ("0.00005", "0.00015", "0.00020")),
            ("MG", -1, ("0.00025", "0.00030", "0.00035", "0.00040", "0.00045", "0.00050")),
            ("PG", +1, ("0.00025", "0.00030", "0.00035", "0.00040", "0.00045", "0.00050")))

def plateau_ordre1(tb):
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
    s = sorted(v); return 0.5 * (s[8] + s[9])

cellules = []
print("creneau  w2         kappa   cible  m_bord  g            |d|/g   G3* / g      G3*          etendue  ln(G3/G1)  ln(G3/G2)  m*   r_c  eta0 absolu  eligible")
for (nom, signe, ds) in CRENEAUX:
    for dtxt in ds:
        w2 = F(2) + signe * F(dtxt); d = float(w2) - 2.0
        for (kappa, cible) in KAPPAS:
            _cache.clear()
            g = float("%.5e" % (kappa * abs(d) * M.P / _brut(M.P, 2, 1, 0.0, 0.0, w2)))
            sites = M.barriere(0.0, 0.0, w2, g, True)
            if not sites:
                sites = [(0, 0.0, abs(M.t_site(0, 0.0, 0.0, w2, g)))]
            m_bord = sites[-1][0]
            tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=(5 if m_bord < 3 else 4)); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
            p3 = plateau_adapte(tb, t3, 3); p2 = plateau_adapte(tb, t3, 2); l1 = plateau_ordre1(tb)
            m_et = next(m for m in range(1, 400) if abs(M.t_site(m, 0.0, 0.0, w2, g)) > 1.0)
            r_c = 2 * (m_bord + max(8, m_bord)) + 2
            eta0 = max(abs(d), g * _brut(M.P, 2, 1, 0.0, 0.0, w2) / (M.P * KAPPA3))
            ok = (m_bord == cible) and (p3["etendue"] is not None) and (p3["etendue"] <= 0.02)
            c = {"creneau": nom, "w2": float(w2), "kappa": kappa, "cible": cible, "m_bord": m_bord, "g": g, "x": abs(d) / g, "G3": math.exp(p3["ln_G"]),
                 "et3": p3["etendue"], "d31": p3["ln_G"] - l1, "d32": p3["ln_G"] - p2["ln_G"], "m_etoile": m_et, "r_c": r_c, "eta0": eta0, "eligible": ok}
            cellules.append(c)
            print("%-7s  %.5f   %.4f  %d      %d       %.5e  %6.3f  %.5e  %.5e  %.4f   %+.4f    %+.4f    %-3d  %d   %.5e  %s" % (
                nom, float(w2), kappa, cible, m_bord, g, c["x"], c["G3"] / g, c["G3"], c["et3"], c["d31"], c["d32"], m_et, r_c, eta0, "oui" if ok else "NON"), flush=True)
n = len(cellules)
print()
print("cellules candidates : %d (19 w2 x 7 kappa) ; eligibles (m_bord = cible et etendue <= 0.02) : %d" % (n, sum(c["eligible"] for c in cellules)))
print("m_bord different de la cible : %d" % sum(c["m_bord"] != c["cible"] for c in cellules))
print("couplages : de %.5e a %.5e ; largeurs predites G3* : de %.5e a %.5e" % (min(c["g"] for c in cellules), max(c["g"] for c in cellules), min(c["G3"] for c in cellules), max(c["G3"] for c in cellules)))
print("etendue d'ordre 3 : plus grande %.4f ; |ln(G3/G1)| : plus grand %.4f ; |ln(G3/G2)| : plus grand %.4f" % (max(c["et3"] for c in cellules), max(abs(c["d31"]) for c in cellules), max(abs(c["d32"]) for c in cellules)))
print("m* (premier site ou le saut depasse 1) : de %d a %d ; cellules ou m* <= r_c / 2 (l'absorbeur du lecteur commence au-dela de m*) : %d" % (
    min(c["m_etoile"] for c in cellules), max(c["m_etoile"] for c in cellules), sum(c["m_etoile"] <= c["r_c"] // 2 for c in cellules)))
print("cellules ou G3* depasse 1.785e-05 (le plus grand plateau qualifie a ce jour) : %d ; plus grand rapport : %.1f" % (sum(c["G3"] > 1.785e-05 for c in cellules), max(c["G3"] for c in cellules) / 1.785e-05))
for (kappa, cible) in KAPPAS:
    L = [c for c in cellules if c["kappa"] == kappa]
    v = [math.log(c["G3"] / abs(c["w2"] - 2.0)) for c in L]
    print("kappa = %.4f : %d cellules ; G3* / |d| de %.4e a %.4e (etalement %.4f en logarithme) ; G3* / g de %.4e a %.4e" % (
        kappa, len(L), math.exp(min(v)), math.exp(max(v)), max(v) - min(v), min(c["G3"] / c["g"] for c in L), max(c["G3"] / c["g"] for c in L)))
