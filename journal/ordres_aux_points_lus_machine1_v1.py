# -*- coding: ascii -*-
"""APRES COUP, SANS VALEUR D'EPREUVE : LES ORDRES DE MA CHAINE AUX SIX POINTS LUS OU delta N'EST PAS NUL -- machine 1, v1,
2026-11-22. UNE DIMENSION. Aucun calcul 2D ; les plateaux du lecteur sont relus dans mes deux journaux de notation.
Question posee par la section 3 de la note de machine 2 (lot 295b2b1549b076c2) : aux deux points de barriere, le lecteur
est a 5e-05 de SA chaine du premier ordre et a 2 a 4e-04 de MA G3*. Est-ce l'absorbeur de ma chaine, ou ses ordres ?
Par point : plateau (mediane des dix-huit variantes) aux ordres 1, 2, 3 ; puis, VARIANTE PAR VARIANTE (meme absorbeur des
deux cotes), ln(G3 / G1) et ln(G2 / G1) : moyenne, plus petit, plus grand. Si l'ecart est le meme a toutes les variantes,
il vient des ordres, pas de l'absorbeur.
Usage : python3 -I -B ordres_aux_points_lus_machine1_v1.py <moteur> <bloc 2> <bloc 3> <bloc adapte> <journal note Q> <journal note Q2>"""
import sys, math, re, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
import mpmath as mp
MOTEUR, BLOC2, BLOC3, BLOC_A, JQ, JQ2 = sys.argv[1:7]
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
def plateaux_lus(journal):
    out = {}; pid = None
    for l in open(journal):
        m = re.match(r"=== (Q2?[a-f])\s", l)
        if m: pid = m.group(1)
        m = re.match(r"\s+A : PLATEAU .*Gamma_pl = ([0-9.e+-]+)", l)
        if m and pid: out[pid] = float(m.group(1))
    return out
LUS = dict(plateaux_lus(JQ)); LUS.update(plateaux_lus(JQ2))
# le premier ordre de machine 2 : recopie de sa note (lot 295b2b1549b076c2, section 3, colonne "mon 1er ordre")
SON_1ER = {"Qe": 1.20928e-05, "Qf": 2.91456e-06, "Q2a": 4.94741e-08, "Q2b": 2.05525e-09, "Q2c": 1.21069e-05, "Q2d": 2.92055e-06}
POINTS = (("Qe", "20001/10000", "3e-4"), ("Qf", "20001/10000", "1.5e-4"), ("Q2a", "20001/10000", "6e-5"), ("Q2b", "20001/10000", "4e-5"),
          ("Q2c", "19999/10000", "3e-4"), ("Q2d", "19999/10000", "1.5e-4"))
def ordre1_par_variante(tb):
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
    return v
med = lambda v: 0.5 * (sorted(v)[8] + sorted(v)[9])
print("point  m  kappa    lecteur      G1* (moi)    G2* (moi)    G3* (moi)    ln(L/G1*)  ln(L/G2*)  ln(L/G3*)  ln(L/son 1er)  ln(G1*/son 1er)")
lignes = []
for (pid, w2t, gt) in POINTS:
    _cache.clear(); w2 = F(w2t); g = float(gt); d = abs(float(w2) - 2.0)
    sites = M.barriere(0.0, 0.0, w2, g, True)
    if not sites:
        sites = [(0, 0.0, abs(M.t_site(0, 0.0, 0.0, w2, g)))]
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=5); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    v3 = plateau_adapte(tb, t3, 3)["valeurs"]; v2 = plateau_adapte(tb, t3, 2)["valeurs"]; v1 = ordre1_par_variante(tb)
    L = math.log(LUS[pid]); kappa = g * _brut(M.P, 2, 1, 0.0, 0.0, w2) / (M.P * d)
    d31 = [a - b for a, b in zip(v3, v1)]; d21 = [a - b for a, b in zip(v2, v1)]
    lignes.append((pid, d31, d21, max(v3) - min(v3), max(v1) - min(v1)))
    print("%-5s  %d  %.4f   %.5e  %.5e  %.5e  %.5e  %+.5f   %+.5f   %+.5f   %+.5f       %+.5f" % (pid, sites[-1][0], kappa, LUS[pid], math.exp(med(v1)), math.exp(med(v2)),
          math.exp(med(v3)), L - med(v1), L - med(v2), L - med(v3), L - math.log(SON_1ER[pid]), med(v1) - math.log(SON_1ER[pid])))
print()
print("VARIANTE PAR VARIANTE (dix-huit absorbeurs, le meme des deux cotes de chaque difference)")
print("point  ln(G3 / G1) : moyenne  de ... a ...           ln(G2 / G1) : moyenne  de ... a ...           etendue ordre 3  etendue ordre 1")
for (pid, d31, d21, e3, e1) in lignes:
    print("%-5s                %+.5f   %+.5f a %+.5f                  %+.5f   %+.5f a %+.5f     %.4f           %.4f" % (pid, sum(d31) / 18, min(d31), max(d31), sum(d21) / 18, min(d21), max(d21), e3, e1))
