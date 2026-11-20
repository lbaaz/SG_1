# -*- coding: ascii -*-
"""ELIGIBILITE DU GEL "PONT", PREMIERE PARTIE -- ma chaine, ECRITE DEPUIS LE TEXTE DU GEL SEUL (sections 2 et 4 de gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md, canon 735ce41be200c5cd).
Machine 2, 2026-11-17. Je n'ai PAS lu eligibilite_pont_machine1_v1.py avant d'avoir rendu ma table. Seules les definitions du gel et les blocs deposes du registre (moteur 82a0be882568fe0c,
tables_ordre2, tables_ordre3) sont utilises ; la matrice sous absorbeur, les valeurs propres, les densites, les lisses et l'eligibilite sont MON code.
Chaine a une dimension seule : AUCUNE 2D.
Usage : py -3.11 -P eligibilite_pont_machine2_v1.py <registre clone> <table.json> <details.json> [--mutation NOM]
Sortie : une ligne par cellule (stdout) ; table.json au format de la section 5 ; details.json avec tous les nombres."""
import importlib.util
import json
import math
import sys
from fractions import Fraction as F
import numpy as np
import mpmath as mp

executer = exec
REG, TABLE, DETAILS = sys.argv[1].rstrip('/\\'), sys.argv[2], sys.argv[3]
MUT = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == '--mutation' else None
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))   # seules tables_ordre2 / tables_ordre3 sont utilisees

P = 5
KAPPA = {3: 0.0262, 4: 0.0200, 5: 0.0159}                                            # section 2
CRENEAUX = {'MG': [F(k, 1000) for k in (1981, 1983, 1984, 1985, 1986, 1987, 1988, 1989)],
            'PG': [F(k, 1000) for k in (2011, 2012, 2013, 2014, 2015, 2016, 2018, 2019)]}
VARIANTES = [(a, c, L) for a in (1.0, 2.0, 4.0) for c in (6, 8, 10) for L in (16, 24)]   # 4.3
ECARTS = [0.05, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]              # 4.5
SEUIL_E_BORD, SEUIL_VIDE, SEUIL_LISSE, SEUIL_PAS = 0.7, 0.02, 0.03, 0.10             # 4.6
if MUT == 'seuil_lisse_04':
    SEUIL_LISSE = 0.04
if MUT == 'seuil_pas_15':
    SEUIL_PAS = 0.15
if MUT == 'seuil_vide_03':
    SEUIL_VIDE = 0.03
if MUT == 'seuil_ebord_08':
    SEUIL_E_BORD = 0.8
if MUT == 'ecarts_sans_8':
    ECARTS = ECARTS[:-1]
if MUT == 'ecarts_sans_005':
    ECARTS = ECARTS[1:]


def coupling(w2, m):
    X = M.X_saut_reel(P, 2, 1, 0, 0, w2)
    v = KAPPA[m] * abs(float(w2) - 2.0) * P / X
    if MUT == 'g_cinq_chiffres':
        return '%.4e' % v
    if MUT == 'kappa_permutes':
        v = KAPPA[{3: 5, 4: 4, 5: 3}[m]] * abs(float(w2) - 2.0) * P / X
    return '%.5e' % v


def matrice(tb, t3, a, c, L, ordre):
    """Section 4.3 : diag m delta + S_m - S_0 - i W_m ; t_m + T3_m (m, m+1) ; U_m (m, m+2) ; W3_m (m, m+3) ; W5_m (m, m+5) ; W_m = a |t_m| ((m - debut)/L)^2, debut < m <= debut + L."""
    d, m_min, m_bord = tb["d"], tb["m_min"], tb["m2_bord"]; debut = m_bord + c; Mh = debut + L; n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex); W = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb["S"][m] - tb["S"][0])
        if m > debut:
            W[i] = a * abs(tb["t"][m]) * ((m - debut) / float(L)) ** 2; H[i, i] += -1j * W[i]
        if m + 1 <= Mh:
            x = tb["t"][m] + (t3["T3"][m] if ordre == 3 else 0.0); H[i, i + 1] = x; H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb["U"][m]; H[i + 2, i] = tb["U"][m]
        if ordre == 3 and m + 3 <= Mh:
            H[i, i + 3] = t3["W3"][m]; H[i + 3, i] = t3["W3"][m]
        if ordre == 3 and m + 5 <= Mh:
            H[i, i + 5] = t3["W5"][m]; H[i + 5, i] = t3["W5"][m]
    return H, W, -m_min


def etat_vide(H, i0):
    """4.4 : valeur propre dont le vecteur propre norme porte le plus grand poids sur le site 0 ; a poids egal, la plus petite partie reelle."""
    val, vec = np.linalg.eig(H); poids = np.abs(vec[i0, :]) ** 2 / np.sum(np.abs(vec) ** 2, axis=0)
    k = int(np.lexsort((val.real, -poids))[0])
    if MUT == 'plus_grande_partie_reelle':
        k = int(np.lexsort((-val.real, -poids))[0])
    return val[k], vec[:, k]


def valeur_propre_hp(H, vec, E0, dps=40, iterations=4):
    """Valeur propre de H (complexe symetrique, entrees = doubles exacts) proche de E0, en precision etendue : iteration inverse a decalage E0 depuis le vecteur de double precision,
    puis quotient de Rayleigh BILINEAIRE x^T H x / x^T x. Sert a Gamma = -2 Im(E), qui vaut ~1e-12 a 5 barreaux : -2 Im(E) lu sur la valeur propre en double precision y est faux de ~1e-3 en relatif."""
    mp.mp.dps = dps
    n = len(H); A = mp.matrix(n, n)
    for i in range(n):
        for j in range(n):
            if H[i, j] != 0:
                A[i, j] = mp.mpc(float(H[i, j].real), float(H[i, j].imag))
    x = mp.matrix([mp.mpc(float(v.real), float(v.imag)) for v in vec])
    B = A - mp.mpc(float(E0.real), float(E0.imag)) * mp.eye(n)
    for _ in range(iterations):
        y = mp.lu_solve(B, x); k = max(range(n), key=lambda i: abs(y[i])); x = y / y[k]
    num = sum(x[i] * sum(A[i, j] * x[j] for j in range(n) if A[i, j] != 0) for i in range(n)); den = sum(x[i] * x[i] for i in range(n))
    return num / den


def mediane(v):
    s = sorted(v); n = len(s)
    return 0.5 * (s[n // 2 - 1] + s[n // 2]) if n % 2 == 0 else s[n // 2]


def cellule(w2, m):
    gs = coupling(w2, m); g = float(gs); delta = float(w2) - 2.0
    sites = M.barriere(0, 0, w2, g, True)
    out = {"w2": str(w2), "m": m, "g": gs}
    if not sites:
        out.update(eligible=False, raison="aucun site de barriere"); return out
    m_bord = sites[-1][0]
    S2 = lambda mm: M.Sigma2_site(M.CANAL[0] * mm, M.CANAL[1] * mm, w2, g)[0]
    e_bord = abs(m_bord * delta + S2(m_bord) - S2(0))
    if MUT == 'e_bord_sans_sigma':
        e_bord = abs(m_bord * delta)
    tb = tables_ordre2(0, 0, w2, g, sites); t3 = tables_ordre3(0, 0, w2, g, tb)
    lnG, ordre_val = [], {2: [], 3: []}
    mats = {}; ecart_gamma = 0.0
    for (a, c, L) in VARIANTES:
        for o in (2, 3):
            H, W, i0 = matrice(tb, t3, a, c, L, o); E, vec = etat_vide(H, i0); mats[(a, c, L, o)] = (H, i0, E.real)
            if o == 3:
                Gd = -2.0 * E.imag
                cle = '%s|%d|%g|%d|%d' % (w2, m, a, c, L)
                if cle in CACHE and MUT not in (None, 'gamma_double_recalcul'):
                    Gh = CACHE[cle]                                   # mutation : les matrices ne changent pas, on reutilise le Gamma en precision etendue du passage de reference
                else:
                    Ehp = valeur_propre_hp(H, vec, E); Gh = float(-2 * Ehp.imag); NOUVEAU[cle] = Gh
                if Gh > 0 and Gd > 0:
                    ecart_gamma = max(ecart_gamma, abs(Gd / Gh - 1.0))
                G = Gd if MUT == 'gamma_double' else Gh
                lnG.append(math.log(G) if G > 0 else float('nan')); ordre_val[3].append(G)
    positives = all(G > 0 for G in ordre_val[3]); etendue_vide = (max(lnG) - min(lnG)) if positives else float('nan')
    plateau = math.exp(mediane(lnG)) if positives else float('nan')
    ecarts = []
    pos_rho = True
    for x in ECARTS:
        ln = {2: [], 3: []}
        for (a, c, L) in VARIANTES:
            for o in (2, 3):
                H, i0, Ev = mats[(a, c, L, o)]
                sgn = -1.0 if MUT == 'cote_oppose_inverse' else 1.0
                E = Ev - sgn * x * delta
                if MUT == 'ordre_2_pour_3' and o == 3:
                    H, i0, Ev = mats[(a, c, L, 2)]; E = Ev - x * delta
                y = np.linalg.solve(E * np.eye(len(H)) - H, np.eye(len(H))[:, i0])
                rho = -(1.0 / math.pi) * y[i0].imag
                if o == 3 and not rho > 0:
                    pos_rho = False
                ln[o].append(math.log(rho) if rho > 0 else float('nan'))
        if any(np.isnan(ln[3])):
            ecarts.append(dict(x=x, etendue=float('nan'), pas=float('nan'), ln3=float('nan'), ln2=float('nan'))); continue
        med3 = mediane(ln[3]); med2 = mediane(ln[2]) if not any(np.isnan(ln[2])) else float('nan')
        if MUT == 'lisse_moyenne':
            med3 = sum(ln[3]) / 18.0; med2 = sum(ln[2]) / 18.0
        ecarts.append(dict(x=x, etendue=max(ln[3]) - min(ln[3]), pas=med2 - med3, ln3=med3, ln2=med2))
    cond_i = (m_bord == m)
    cond_ii = e_bord < SEUIL_E_BORD
    cond_iii = positives and etendue_vide <= SEUIL_VIDE
    cond_iv = pos_rho and all(e['etendue'] <= SEUIL_LISSE for e in ecarts)
    cond_v = all(abs(e['pas']) <= SEUIL_PAS for e in ecarts)
    if MUT == 'sans_condition_v':
        cond_v = True
    if MUT == 'sans_condition_iv':
        cond_iv = True
    if MUT == 'sans_condition_i':
        cond_i = True
    if MUT == 'ebord_inclus':
        cond_ii = e_bord <= SEUIL_E_BORD
    out.update(m_bord=m_bord, e_bord=e_bord, etendue_vide=etendue_vide, plateau=plateau, gamma_double_vs_hp_rel=ecart_gamma,
               etendue_lisse_max=max(e['etendue'] for e in ecarts), pas_max=max(abs(e['pas']) for e in ecarts), rho3_8=math.exp(ecarts[-1]['ln3']) if ECARTS[-1] == 8.0 else float('nan'),
               conditions=dict(i=bool(cond_i), ii=bool(cond_ii), iii=bool(cond_iii), iv=bool(cond_iv), v=bool(cond_v)), eligible=bool(cond_i and cond_ii and cond_iii and cond_iv and cond_v),
               ecarts=ecarts)
    return out


import os
CHEMIN_CACHE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cache_gamma_hp_pont_machine2_v1.json')      # a cote du script, pas du fichier de sortie
CACHE = json.load(open(CHEMIN_CACHE)) if (MUT is not None and os.path.isfile(CHEMIN_CACHE)) else {}
NOUVEAU = {}
tab = {"creneaux": {}}; det = []
print('# creneau w2     m  g            m_bord e_bord   etendue_vide  etendue_lisse_max  pas_max   conditions(i ii iii iv v)  eligible')
for s, liste in CRENEAUX.items():
    cand = []
    for w2 in liste:
        cells = [cellule(w2, m) for m in (3, 4, 5)]
        for c in cells:
            det.append(c)
            cd = c.get('conditions', {})
            print('%-4s %-9s %d  %s  %-5s %.4f  %.4f        %.4f             %.4f   %s   %s' % (s, ('%.3f' % float(w2)), c['m'], c['g'], c.get('m_bord', '-'), c.get('e_bord', float('nan')), c.get('etendue_vide', float('nan')),
                                                               c.get('etendue_lisse_max', float('nan')), c.get('pas_max', float('nan')), ' '.join('1' if cd.get(k) else '0' for k in ('i', 'ii', 'iii', 'iv', 'v')), 'OUI' if c['eligible'] else 'non'), flush=True)
        cand.append({"w2": "%d/%d" % (w2.numerator, w2.denominator), "eligible": all(c['eligible'] for c in cells),
                     "cellules": [{"m": c['m'], "g": c['g'], "eligible": c['eligible']} for c in cells]})
    tab["creneaux"][s] = {"candidats": cand}
    print('# creneau %s : %d w2 eligibles sur %d' % (s, sum(1 for c in cand if c['eligible']), len(cand)))
if MUT is None and NOUVEAU:
    json.dump(NOUVEAU, open(CHEMIN_CACHE, 'w'), indent=0, sort_keys=True)          # le passage de reference ecrit le cache ; une mutation ne l'ecrit jamais
json.dump(tab, open(TABLE, 'w', encoding='ascii'), indent=1, sort_keys=True)
json.dump(det, open(DETAILS, 'w', encoding='ascii'), indent=1, sort_keys=True)
