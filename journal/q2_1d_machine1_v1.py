# -*- coding: ascii -*-
"""LES QUATRE POINTS "Q2" DEMANDES PAR MACHINE 2, A UNE DIMENSION, AVANT TOUTE LECTURE -- machine 1, v1, 2026-11-22.
Hors chaine, classe 3. AUCUN CALCUL 2D. Charge, au canon controle et sans les editer, le moteur et les trois blocs deposes
(clone du registre public, tete 055be58). Par point : la barriere du moteur, r_c et eta0 par la regle de l'esquisse
(r_c = 2 (m + max(8, m)) + 2 ; eta0 = max(|w2 - 2|, g X(w2) / (P kappa_3)), kappa_3 = 0.0262, six chiffres) ; la colonne G3*
(chaine d'ordre 3 sous l'absorbeur adapte, plateau_adapte du bloc depose, dix-huit variantes), les ordres 2 et 1 ; puis le
mandataire a une dimension du lecteur (premier ordre, quatre absorbeurs du lecteur le long de l'echelle, douze barreaux).
Les points Q-e et Q-f, deja lus, sont recalcules pour les rapports de signe : ce que la CHAINE dit du passage de delta > 0 a
delta < 0 au meme couplage.
Usage : python3 -I -B q2_1d_machine1_v1.py <moteur> <bloc ordre 2> <bloc ordre 3> <bloc adapte>"""
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
print("canons controles : moteur %s ; bloc 2 %s ; bloc 3 %s ; bloc adapte %s" % tuple(CANONS[k] for k in ("moteur", "bloc2", "bloc3", "bloc_adapte")))
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
POINTS = [("Q2-a", "20001/10000", 6e-05), ("Q2-b", "20001/10000", 4e-05), ("Q2-c", "19999/10000", 3e-04), ("Q2-d", "19999/10000", 1.5e-04),
          ("Q-e", "20001/10000", 3e-04), ("Q-f", "20001/10000", 1.5e-04)]

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

KS = list(range(-3, 9))
ABSORBEURS = [("A", "F2", 0, 80), ("B", "F2", 0, 100), ("C", "F1", 0, 100), ("D", "F2", 10, 80)]
def lecteur_1d(d, t, forme, bord, L, eta):
    m_max = (bord + L - 1) // 2; n = m_max + 1
    H = np.zeros((n, n), dtype=complex); Wd = np.zeros(n)
    for m in range(n):
        H[m, m] = m * d
        x = 2 * m - bord
        if x > 0:
            Wd[m] = eta * (float(x * x) if forme == "F1" else float(x ** 4) / float(L * L)); H[m, m] += -1j * Wd[m]
        if m < m_max:
            H[m, m + 1] = t[m]; H[m + 1, m] = t[m]
    val, vec = np.linalg.eig(H)
    nrm = (np.abs(vec) ** 2).sum(axis=0); poids = np.abs(vec[0, :]) ** 2 / nrm
    j0 = int(np.argmin(np.abs(val)))
    return float(2.0 * (Wd @ (np.abs(vec[:, j0]) ** 2)) / nrm[j0]), float(poids[j0])
def plateau(ser):
    best = None
    for k0 in range(-3, 5):
        v = [ser[k] for k in range(k0, k0 + 5)]
        r = max(v) / min(v)
        if best is None or r < best[0] - 1e-15:
            best = (r, k0)
    return best

R = {}
print()
print("=== 1. LA COLONNE G3* ET LA GEOMETRIE (une dimension)")
print("point  w2            g        |d| / g  kappa    m_bord  r_c  eta0         eta0 / g  G3*          G3* / g      etendue  ln(G3/G2)  ln(G3/G1)")
for (nom, w2s, g) in POINTS:
    _cache.clear()
    w2 = F(w2s); d = float(w2) - 2.0
    sites = M.barriere(0.0, 0.0, w2, g, True); vide = not sites
    if vide:
        sites = [(0, 0.0, abs(M.t_site(0, 0.0, 0.0, w2, g)))]
    m_bord = sites[-1][0]
    tb = tables_ordre2(0.0, 0.0, w2, g, sites, M_facteur=(5 if m_bord < 3 else 4)); t3 = tables_ordre3(0.0, 0.0, w2, g, tb)
    p3 = plateau_adapte(tb, t3, 3); p2 = plateau_adapte(tb, t3, 2); l1 = plateau_ordre1(tb)
    X = _brut(M.P, 2, 1, 0.0, 0.0, w2)
    kappa = g * X / (M.P * abs(d)); r_c = 2 * (m_bord + max(8, m_bord)) + 2
    eta0 = float("%.5e" % max(abs(d), g * X / (M.P * KAPPA3)))
    R[nom] = {"w2": w2, "g": g, "d": d, "m_bord": m_bord, "r_c": r_c, "eta0": eta0, "ln_G3": p3["ln_G"], "et3": p3["etendue"], "ln_G1": l1, "regle": "absolu" if g * X / (M.P * KAPPA3) >= abs(d) else "depot"}
    print("%-5s  %-12s  %.1e  %.3f    %.4f   %d%s      %d   %.5e  %.4f    %.5e  %.5e  %.4f   %+.5f   %+.5f" % (
        nom, w2s, g, abs(d) / g, kappa, m_bord, "*" if vide else " ", r_c, eta0, eta0 / g, math.exp(p3["ln_G"]), math.exp(p3["ln_G"]) / g, p3["etendue"],
        p3["ln_G"] - p2["ln_G"], p3["ln_G"] - l1), flush=True)
print("(* = barriere du moteur vide, m_bord = 0 pose ; eta0 : regle %s aux six points)" % sorted(set(r["regle"] for r in R.values())))
print()
print("=== 2. CE QUE LA CHAINE DIT DU SIGNE DE DELTA, au meme couplage")
for (neg, pos) in (("Q2-c", "Q-e"), ("Q2-d", "Q-f")):
    print("ln[G3*(%s) / G3*(%s)] = %+.5f   (G3* = %.5e a delta < 0, %.5e a delta > 0)" % (neg, pos, R[neg]["ln_G3"] - R[pos]["ln_G3"], math.exp(R[neg]["ln_G3"]), math.exp(R[pos]["ln_G3"])))
print()
print("=== 3. LE MANDATAIRE A UNE DIMENSION DU LECTEUR, aux quatre points Q2 (premier ordre ; regle de plateau de la feuille)")
for nom in ("Q2-a", "Q2-b", "Q2-c", "Q2-d"):
    r = R[nom]; w2, g, d, r_c, eta0 = r["w2"], r["g"], r["d"], r["r_c"], r["eta0"]
    t = [(g / M.P) * _brut(M.P, 2, 1, float(2 * m), float(m), w2) for m in range((r_c + 10 + 100) // 2 + 2)]
    res = {}
    for (an, forme, dr, L) in ABSORBEURS:
        ser, pds = {}, {}
        for k in KS:
            ser[k], pds[k] = lecteur_1d(d, t, forme, r_c + dr, L, eta0 * 2.0 ** (-k))
        rr, k0 = plateau(ser)
        res[an] = (k0, rr, ser[k0], min(pds[k] for k in range(k0, k0 + 5)), [k for k in KS if abs(ser[k] / ser[k0] - 1.0) <= 0.005])
    qual = all(res[a][1] <= 1.05 for a in "ABCD") and all(abs(math.log(res[a][2] / res["A"][2])) <= 0.05 for a in "BCD") and all(res[a][3] >= 0.5 for a in "ABCD")
    print("%-5s r_c = %d  %s  fenetres k0 : A %+d B %+d C %+d D %+d  plus grand |ln(X / A)| %.4f  ln(plateau A / G1*) = %+.5f  poids >= %.3f  plat a 0.005 sous A : k = %d a %d" % (
        nom, r_c, "QUALIFIE (mandataire)" if qual else "NON QUALIFIE (mandataire)", res["A"][0], res["B"][0], res["C"][0], res["D"][0],
        max(abs(math.log(res[a][2] / res["A"][2])) for a in "BCD"), math.log(res["A"][2]) - r["ln_G1"], min(res[a][3] for a in "ABCD"), min(res["A"][4]), max(res["A"][4])))
