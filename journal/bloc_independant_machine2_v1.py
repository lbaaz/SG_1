# -*- coding: ascii -*-
"""BLOC DE LA CHAINE D'ORDRE 2, RECALCULE A PART PAR MACHINE 2 (gel 41153158190cf7f1, bloc 7cd5977bc27bebc1). Ecrit du TEXTE du gel (section 3) et de la note
de machine 1 ; aucune ligne du bloc n'est reprise. Le bloc de machine 1 n'est charge que pour etre COMPARE. Sans aucune diagonalisation 2D du lot (le H_2D
du moteur n'est construit qu'a petite boite et a eta = 0, pour B et C).
  A. TABLES, par une somme GENERIQUE sur tous les sauts de x^5 depuis chaque site de l'echelle (36 sauts, canal compris, sans argument de parite, sans
     liste de 34, sans exclusion autre que 'q sur l'echelle'), avec les elements de matrice ENTIERS du moteur (X_saut), contre les tables du bloc de machine 1
     (t, Sigma2, u) : a l'etat des deux ancres, aux etats voisins des graines des seize points. La somme generique rend aussi les termes entre voisins,
     a trois sites et a quatre sites : ils doivent etre nuls (parite, portee).
  B. LOWDIN SUR LE H_2D EXACT DU MOTEUR : la matrice du moteur (x5, eta = 0), les sites de l'echelle comme espace P, le reste comme Q ; le terme du second
     ordre est calcule SUR LA MATRICE (aucun saut enumere), contre les tables du bloc.
  C. ENERGIE ET SIGNE : l'energie exacte de l'etat de plus grand recouvrement avec le site 0, du H_2D du moteur (hermitien, boite moyenne), contre celle de la
     chaine d'ordre 2 (mes tables), a g, g/2, g/4 : l'erreur relative doit decroitre ; et les variantes 'ordre 1', 'Sigma2 seul', 'u seul'.
  D. LA CHAINE : mon solveur contre gamma_chaine_ordre2 du bloc, aux quatre eta de chaine, aux memes etats (Gamma_flux, -2 Im E, dE).
  E. LA NOTE : les 262 etats des deux runs deja joues (JSON du registre, lus a leur chemin), juges par les criteres (1) a (8) et l'etiquette unique ; q1, q2
     et le decalage d'energie recalcules par moi, contre les chiffres de la section 2 du gel (i), (ii), (iv) et contre le tableau de la note.
  F. LES REFERENCES DE G-8 : ma chaine aux deux etats d'ancre, contre les quatre constantes du gel (section 10, G-8), lues dans son texte.
Usage (depuis BOCAL4) : python -P ordre2/bloc_independant_machine2_v1.py <moteur> <bloc> <clone du registre> <gel.md>"""
import importlib.util
import json
import math
import os
import re
import sys
from fractions import Fraction as F

import numpy as np

MOTEUR, BLOC, REG, GELP = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
spec = importlib.util.spec_from_file_location("moteur", MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
spb = importlib.util.spec_from_file_location("bloc_m1", BLOC)
BL = importlib.util.module_from_spec(spb)
BL.M, BL.np, BL.math = M, np, math                 # le bloc 'depend de M, np et math, deja charges par la sonde'
spb.loader.exec_module(BL)
assert M.P == 5 and tuple(M.CANAL) == (2, 1) and float(M.W1) == 1.0
W1 = 1.0
bad = []
NCTRL = [0]


def dire(s=''):
    print(s, flush=True)


def verdict(nom, ok, detail=''):
    NCTRL[0] += 1
    if not ok:
        bad.append(nom)
    dire('  %-6s %s  %s' % (nom, 'TIENT' if ok else 'MORD ', detail))


JUMPS = [(k, l) for k in range(-5, 6) for l in range(-5, 6) if 0 < abs(k) + abs(l) <= 5 and (k + l) % 2 == 1]
assert len(JUMPS) == 36
_CACHE = {}


def Vint(g, k, l, a, b, w2):
    """<a+k, b+l | (g/5) x^5 | a, b>, occupations entieres, routine ENTIERE du moteur (X_saut)."""
    if a + k < 0 or b + l < 0:
        return 0.0
    cle = (w2, k, l, a, b)
    if cle not in _CACHE:
        _CACHE[cle] = M.X_saut(5, k, l, a, b, w2)
    return (g / 5.0) * _CACHE[cle]


def tables_miennes(n1, n2, w2, g, m_hi):
    """t[m], H2[(m, m + dm)] pour dm = 0..4, par somme generique sur les 36 sauts ; sites de m_lo a m_hi (les sites m + dm au-dela de m_hi ne sont pas comptes)."""
    w = float(w2)
    m_lo = -min(n1 // 2, n2)
    E = lambda a, b: -W1 * a + w * b
    t, H2 = {}, {}
    for m in range(m_lo, m_hi + 1):
        a, b = n1 + 2 * m, n2 + m
        t[m] = Vint(g, 2, 1, a, b, w2)
        for dm in range(0, 5):
            H2[(m, m + dm)] = 0.0
        Ea = E(a, b)
        for (k, l) in JUMPS:
            qa, qb = a + k, b + l
            if qa < 0 or qb < 0:
                continue
            if qa - n1 == 2 * (qb - n2):                       # q sur l'echelle : exclu de la somme sur Q
                continue
            v1 = Vint(g, k, l, a, b, w2)
            if v1 == 0.0:
                continue
            Eq = E(qa, qb)
            for dm in range(0, 5):
                m2 = m + dm
                if m2 > m_hi:
                    continue
                ba, bb = n1 + 2 * m2, n2 + m2
                jk, jl = ba - qa, bb - qb
                if abs(jk) + abs(jl) > 5 or (jk + jl) % 2 != 1:
                    continue
                v2 = Vint(g, jk, jl, qa, qb, w2)
                if v2 == 0.0:
                    continue
                Eb = E(ba, bb)
                H2[(m, m2)] += 0.5 * v1 * v2 * (1.0 / (Ea - Eq) + 1.0 / (Eb - Eq))
    return m_lo, t, H2


def chaine_miens(n1, n2, w2, g, sites, ef):
    """Chaine d'ordre 2 : diagonale m*delta + Sigma2(m) - Sigma2(0), saut t_m, saut u_m au second voisin, absorbeur de gamma_chaine du moteur (lu dans le
    moteur : sites[-1][0], b_M = max(8, .), M = 4 (m2 + b_M), eta = |delta| ef, debut m2 + b_M // 2, W = eta (m - debut)^2)."""
    d = float(w2) - 2.0 * W1
    m2b = sites[-1][0]
    bM = max(8, m2b)
    Mh = (m2b + bM) * 4
    m_lo, t, H2 = tables_miennes(n1, n2, w2, g, Mh)
    eta = abs(d) * ef
    debut = m2b + bM // 2
    n = Mh - m_lo + 1
    H = np.zeros((n, n), dtype=complex)
    Wd = np.zeros(n)
    for m in range(m_lo, Mh + 1):
        i = m - m_lo
        H[i, i] = m * d + (H2[(m, m)] - H2[(0, 0)])
        if m > debut:
            Wd[i] = eta * (m - debut) ** 2
            H[i, i] += -1j * Wd[i]
        if m + 1 <= Mh:
            H[i, i + 1] = H[i + 1, i] = t[m]
        if m + 2 <= Mh:
            H[i, i + 2] = H[i + 2, i] = H2[(m, m + 2)]
    val, vec = np.linalg.eig(H)
    rec = np.abs(vec[-m_lo, :]) ** 2
    nu = np.lexsort((val.real, -rec))[0]
    p2 = np.abs(vec[:, nu]) ** 2
    return {'flux': float(2.0 * (Wd @ p2) / p2.sum()), 'im': float(-2.0 * val[nu].imag), 'dE': float(val[nu].real + H2[(0, 0)]), 'rec': float(rec[nu])}


def rel(a, b):
    return abs(a - b) / abs(b) if b else abs(a - b)


# ------------------------------------------------------------------------------------------------------------------ A. tables
dire('A. TABLES : somme generique (36 sauts, elements entiers) contre le bloc de machine 1')
ETATS_A = []
POINTS_GEL = [("C1", "197/100", "2/3"), ("C2", "97/50", "3/4"), ("C3", "203/100", "3/2"), ("C4", "103/50", "4/3"), ("M1", "193/100", "1"), ("M2", "48/25", "4/3"),
              ("M3", "207/100", "2/3"), ("M4", "21/10", "3/4"), ("L1", "189/100", "4/3"), ("L2", "47/25", "1"), ("L3", "211/100", "3/2"), ("L4", "53/25", "2/3"),
              ("A1", "39/20", "1"), ("A2", "41/20", "1"), ("W1", "107/50", "1"), ("W2", "209/100", "1/2")]
for pid, w, f in POINTS_GEL:
    w2 = F(w)
    g = float(M.g_du_point(w2)) * float(F(f))
    s = 0.70 * M.s_ff(w2, g)
    n1g, n2g = M.appariement(s, w2)
    if pid in ('A1', 'A2'):
        voisins = [(7, 2) if pid == 'A1' else (8, 2)]
    else:
        voisins = [(round(n1g) + dj, round(n2g) + dk) for dj in (-1, 0, 1) for dk in (-1, 0, 1)]
    for (n1, n2) in voisins:
        if n1 >= 0 and n2 >= 0:
            ETATS_A.append((pid, w2, g, n1, n2))
pire = {'t': 0.0, 'S': 0.0, 'U': 0.0, 'nul13': 0.0, 'nul4': 0.0, 'S0_moteur': 0.0}
nb_ech = 0
for (pid, w2, g, n1, n2) in ETATS_A:
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    if not sites:
        continue
    tb = BL.tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4)
    m_lo, t, H2 = tables_miennes(n1, n2, w2, g, tb['Mh'])
    assert m_lo == tb['m_min']
    ech = max(abs(x) for x in list(tb['t'].values()) + list(tb['S'].values()) + list(tb['U'].values()))
    s0_moteur = M.Sigma2_site(float(n1), float(n2), w2, g)[0]                  # Sigma2(0) du moteur lui-meme (la note, section 5 : a 5e-15 pres)
    pire['S0_moteur'] = max(pire['S0_moteur'], abs(H2[(0, 0)] - s0_moteur) / max(abs(s0_moteur), 1e-300), abs(tb['S'][0] - s0_moteur) / max(abs(s0_moteur), 1e-300))
    for m in range(m_lo, tb['Mh'] + 1):
        if m + 1 <= tb['Mh']:
            pire['t'] = max(pire['t'], abs(t[m] - tb['t'][m]) / max(abs(tb['t'][m]), 1e-300))
        pire['S'] = max(pire['S'], abs(H2[(m, m)] - tb['S'][m]) / max(abs(tb['S'][m]), 1e-300))
        if m + 2 <= tb['Mh']:
            pire['U'] = max(pire['U'], abs(H2[(m, m + 2)] - tb['U'][m]) / abs(tb['U'][m]) if tb['U'][m] != 0.0 else abs(H2[(m, m + 2)]))
        for dm in (1, 3):
            if m + dm <= tb['Mh']:
                pire['nul13'] = max(pire['nul13'], abs(H2[(m, m + dm)]) / ech)
        if m + 4 <= tb['Mh']:
            pire['nul4'] = max(pire['nul4'], abs(H2[(m, m + 4)]) / ech)
    nb_ech += 1
dire('  %d etats (ancres A1 (7,2) et A2 (8,2), 3 x 3 etiquettes voisines de la graine aux 14 autres points) ; tous les sites de m_min a la fin de la chaine' % nb_ech)
dire('  plus grand ecart relatif : t %.2e ; Sigma2 %.2e ; u %.2e' % (pire['t'], pire['S'], pire['U']))
dire('  termes nuls (relatifs a la plus grande valeur de la table) : entre voisins et a trois sites %.2e ; a quatre sites %.2e' % (pire['nul13'], pire['nul4']))
verdict('A1', max(pire['t'], pire['S'], pire['U']) < 1e-9, 't, Sigma2 et u du bloc == ma somme generique, a 1e-9 relatif')
verdict('A2', pire['nul13'] < 1e-12 and pire['nul4'] < 1e-12, 'la parite et la portee annulent bien les termes entre voisins, a trois et a quatre sites')
dire("  Sigma2(0) du bloc et de ma somme contre Sigma2_site du moteur (celui de la barriere, que la note dit retrouve 'a 5e-15 pres') : ecart relatif maximal %.2e" % pire['S0_moteur'])
verdict('A3', pire['S0_moteur'] < 1e-12, "Sigma2(0) du bloc == Sigma2_site du moteur, a 1e-12 relatif")

# ------------------------------------------------------------------------------------------------------------------ B. Lowdin sur H_2D
dire()
dire('B. LOWDIN SUR LE H_2D EXACT DU MOTEUR (x5, eta = 0) : le second ordre est lu SUR LA MATRICE, contre les tables du bloc')
pireB = {'t': 0.0, 'S': 0.0, 'U': 0.0, 'nul': 0.0}
for (pid, n1, n2) in (('A1', 7, 2), ('A2', 8, 2), ('A1', 6, 1), ('A2', 9, 3), ('A1', 5, 2)):
    w2 = F(39, 20) if pid == 'A1' else F(41, 20)
    g = float(M.g_du_point(w2))
    m_hi = 8
    N = n1 + 2 * m_hi + 8
    H, idx = M.H_2D(N, w2, g, -1, 'x5', 0.0, None)
    Hr = H.real
    assert np.abs(H.imag).max() == 0.0 and np.abs(Hr - Hr.T).max() == 0.0
    E = np.diag(Hr).copy()
    dim = N * N
    sur_echelle = np.zeros(dim, dtype=bool)
    for (a, b), i in idx.items():
        if a - n1 == 2 * (b - n2):
            sur_echelle[i] = True
    Q = ~sur_echelle
    m_lo = -min(n1 // 2, n2)
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    tb = BL.tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4)
    ia = {m: idx[(n1 + 2 * m, n2 + m)] for m in range(m_lo, m_hi + 1)}
    ech = max(abs(tb['S'][m]) for m in range(m_lo, m_hi + 1))
    for m in range(m_lo, m_hi + 1):
        ra = Hr[ia[m], :] * Q
        for dm in range(0, 5):
            if m + dm > m_hi:
                continue
            rb = Hr[ia[m + dm], :] * Q
            sel = (ra != 0.0) & (rb != 0.0)
            val = 0.5 * float(np.sum(ra[sel] * rb[sel] * (1.0 / (E[ia[m]] - E[sel]) + 1.0 / (E[ia[m + dm]] - E[sel])))) if sel.any() else 0.0
            if dm == 0:
                pireB['S'] = max(pireB['S'], rel(val, tb['S'][m]))
            elif dm == 2:
                pireB['U'] = max(pireB['U'], rel(val, tb['U'][m]) if tb['U'][m] != 0.0 else abs(val))
            else:
                pireB['nul'] = max(pireB['nul'], abs(val) / ech)
        if m + 1 <= m_hi:
            pireB['t'] = max(pireB['t'], rel(Hr[ia[m + 1], ia[m]], tb['t'][m]))
dire('  5 etats, boite N = n1 + 24, sites de m_min a 8 ; ecart relatif : t %.2e ; Sigma2 %.2e ; u %.2e ; termes nuls (dm = 1, 3, 4) %.2e' % (
    pireB['t'], pireB['S'], pireB['U'], pireB['nul']))
verdict('B1', max(pireB['t'], pireB['S'], pireB['U']) < 1e-9 and pireB['nul'] < 1e-12,
        'le bloc == le second ordre lu sur la matrice du moteur, sans aucune enumeration de saut de ma part')

# ------------------------------------------------------------------------------------------------------------------ C. energie et signe
dire()
dire("C. ENERGIE ET SIGNE : l'energie exacte de l'etat de plus grand recouvrement avec le site 0 (H_2D du moteur, hermitien) contre la chaine, a g, g/2, g/4")
pireC = []
for (pid, n1, n2, w2) in (('A1', 7, 2, F(39, 20)), ('A2', 8, 2, F(41, 20)), ('C1', 7, 2, F(197, 100)), ('L3', 8, 2, F(211, 100))):
    g0 = float(M.g_du_point(w2)) * 0.5
    errs = {}
    for fac in (1.0, 0.5, 0.25):
        g = g0 * fac
        m_hi = 9
        N = n1 + 2 * m_hi + 8
        H, idx = M.H_2D(N, w2, g, -1, 'x5', 0.0, None)
        val, vec = np.linalg.eigh(H.real)
        i0 = idx[(n1, n2)]
        nu = int(np.argmax(vec[i0, :] ** 2))
        dE_ex = float(val[nu]) - M.energie_libre(float(n1), float(n2), w2)
        m_lo, t, H2 = tables_miennes(n1, n2, w2, g, m_hi)
        d = float(w2) - 2.0

        def energie(avec_S, avec_U):
            n = m_hi - m_lo + 1
            Hc = np.zeros((n, n))
            for m in range(m_lo, m_hi + 1):
                i = m - m_lo
                Hc[i, i] = m * d + ((H2[(m, m)] - H2[(0, 0)]) if avec_S else 0.0)
                if m + 1 <= m_hi:
                    Hc[i, i + 1] = Hc[i + 1, i] = t[m]
                if avec_U and m + 2 <= m_hi:
                    Hc[i, i + 2] = Hc[i + 2, i] = H2[(m, m + 2)]
            v, w = np.linalg.eigh(Hc)
            k = int(np.argmax(w[-m_lo, :] ** 2))
            return float(v[k]) + (H2[(0, 0)] if avec_S else 0.0)
        e2, e1, eS, eU = energie(True, True), energie(False, False), energie(True, False), energie(False, True)
        errs[fac] = (abs(e2 - dE_ex), abs(e1 - dE_ex), abs(eS - dE_ex), abs(eU - dE_ex), dE_ex, e2)
    r = errs
    ratio = (r[1.0][0] / r[0.5][0], r[0.5][0] / r[0.25][0])
    dire("  %s (%d,%d) w2=%s : dE exact %.4e (g), %.4e (g/2) ; erreur / |dE| de la chaine d'ordre 2 : %.2e, %.2e, %.2e ; ordre 1 : %.2e ; Sigma2 seul : %.2e ; u seul : %.2e ; rapports d'erreur par moitie de g : %.1f, %.1f" % (
        pid, n1, n2, w2, r[1.0][4], r[0.5][4], r[1.0][0] / abs(r[1.0][4]), r[0.5][0] / abs(r[0.5][4]), r[0.25][0] / abs(r[0.25][4]),
        r[1.0][1] / abs(r[1.0][4]), r[1.0][2] / abs(r[1.0][4]), r[1.0][3] / abs(r[1.0][4]), ratio[0], ratio[1]))
    pireC.append((r[1.0][0] / abs(r[1.0][4]), r[0.25][0] / abs(r[0.25][4]), ratio, r[0.25][1] / abs(r[0.25][4]), r[0.25][2] / abs(r[0.25][4]), r[0.25][3] / abs(r[0.25][4])))
verdict('C1', all(x[0] < 0.05 and x[1] < 0.005 for x in pireC), "l'erreur de la chaine d'ordre 2 sur dE est sous 5 pour cent de dE a g et sous 0.5 pour cent a g/4")
verdict('C2', all(x[2][0] > 3.5 and x[2][1] > 3.5 for x in pireC), "l'erreur relative decroit au moins comme g^2 (rapport > 3.5 a chaque moitie de g ; cubique : 8)")
dire("  a g/4 (la ou le developpement tient) : erreur / |dE|, ordre 2 complet %s ; ordre 1 %s ; Sigma2 seul %s ; u seul %s" % (
    ['%.1e' % x[1] for x in pireC], ['%.1e' % x[3] for x in pireC], ['%.1e' % x[4] for x in pireC], ['%.1e' % x[5] for x in pireC]))
verdict('C3', all(x[3] > 3 * x[1] and x[5] > 3 * x[1] and x[4] < 3 * x[1] + 1e-4 for x in pireC),
        "a g/4, l'ordre 1 et 'u seul' sont au moins trois fois plus loin de l'energie exacte que l'ordre 2 complet ; 'Sigma2 seul' est aussi bon que lui "
        "(le decalage d'energie de l'etat central est le terme Sigma2 : u n'agit pas a cet ordre sur l'energie, il agit sur la saut entre sites, donc sur la largeur)")

# ------------------------------------------------------------------------------------------------------------------ D. solveur
dire()
dire('D. LE SOLVEUR : ma chaine (mes tables) contre gamma_chaine_ordre2 du bloc (ses tables), aux quatre eta, aux etats de A')
pireD = {'flux': 0.0, 'im': 0.0, 'dE': 0.0, 'rec': 0.0, 'n': 0, 'im_tout': 0.0, 'n_bas': 0}
EFS = (0.25, 0.125, 0.0625, 0.03125)
for (pid, w2, g, n1, n2) in ETATS_A[::3] + [x for x in ETATS_A if x[0] in ('A1', 'A2')]:
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    if not sites:
        continue
    tb = BL.tables_ordre2(float(n1), float(n2), w2, g, sites, M_facteur=4)
    for ef in EFS:
        r1 = BL.gamma_chaine_ordre2(tb, ef)
        r2 = chaine_miens(n1, n2, w2, g, sites, ef)
        pireD['flux'] = max(pireD['flux'], rel(r2['flux'], r1['Gamma_flux']))
        if r1['Gamma_flux'] >= 1e-12:
            pireD['im'] = max(pireD['im'], rel(r2['im'], r1['Gamma_c2']))
        else:
            pireD['n_bas'] += 1
        pireD['im_tout'] = max(pireD['im_tout'], rel(r2['im'], r1['Gamma_c2']))
        pireD['dE'] = max(pireD['dE'], rel(r2['dE'], r1['dE']))
        pireD['rec'] = max(pireD['rec'], rel(r2['rec'], r1['recouvrement']))
        pireD['n'] += 1
dire('  %d (etat, eta) : ecart relatif max : Gamma_flux %.2e ; dE %.2e ; recouvrement %.2e ; -2 Im E %.2e aux largeurs de la fenetre de lecture (Gamma_flux >= 1e-12) ; '
     'sur les %d (etat, eta) a Gamma_flux sous 1e-12 le -2 Im E des deux solveurs differe jusqu a %.2e (arrondi de la diagonalisation non hermitienne, gel section 2 (iv))' % (
         pireD['n'], pireD['flux'], pireD['dE'], pireD['rec'], pireD['im'], pireD['n_bas'], pireD['im_tout']))
verdict('D1', max(pireD['flux'], pireD['dE'], pireD['rec']) < 1e-6,
        'le bloc == mon solveur sur mes tables, a 1e-6 relatif, pour les trois valeurs que la feuille lit : Gamma_flux, dE, recouvrement')
verdict('D2', pireD['im'] < 0.17,
        "-2 Im E (valeur NON lue, consignee) : les deux solveurs different de moins de 17 pour cent aux largeurs de la fenetre de lecture, le plus grand arrondi que le gel (iv) declare")

# ------------------------------------------------------------------------------------------------------------------ E. la note
dire()
dire("E. LA NOTE : les 262 etats des deux runs deja joues (JSON du registre), juges par (1) a (8) et l'etiquette unique ; q1, q2, decalage d'energie recalcules")
J1 = json.load(open(os.path.join(REG, 'journal', 'sonde_chaine_par_etat.json'), encoding='ascii'))
J2 = json.load(open(os.path.join(REG, 'journal', 'sonde_domaine_G1.json'), encoding='ascii'))
note = json.load(open(os.path.join(os.path.dirname(BLOC), 'ordre2_par_etat_v3.json'), encoding='utf-8'))
NOTE = {(p['id'], e['n1'], e['n2']): e for p in note['points'] for e in p['etats']}
vus_pt = {}
for p in J1['points'] + J2['points']:
    vus_pt.setdefault(p['id'], p)


def motif8(e):
    if not e['J_ecart_type'] < 0.2:
        return 1
    if e['n1'] < 0 or e['n2'] < 0:
        return 2
    if not e['poids_site'] >= 0.5:
        return 3
    if not e['Gamma_2D']['3'] > 1.33e-12:
        return 4
    if e['suivi']['2'] < 0.9 or e['suivi']['4'] < 0.9:
        return 5
    gs = [e['Gamma_2D'][k] for k in ('2', '3', '4')]
    if not (min(gs) > 0 and max(gs) / min(gs) <= 2.0):
        return 6
    c = e['chaine']
    if c['erreur'] is not None or c['vide'] or not c['definie']:
        return 7
    if not (min(c['gammas']) > 0 and max(c['gammas']) / min(c['gammas']) <= 2.0):
        return 8
    return None


LIGNES = []
for pid, p in sorted(vus_pt.items()):
    w2 = F(p['w2'])
    fac = F(p['facteur'])
    g = float(M.g_du_point(w2)) * float(fac)
    assert abs(g - p['g']) <= 1e-12 * g
    cnt = {}
    for e in p['etats']:
        cnt[(e['n1'], e['n2'])] = cnt.get((e['n1'], e['n2']), 0) + 1
    for e in p['etats']:
        if motif8(e) is None and cnt[(e['n1'], e['n2'])] == 1:
            LIGNES.append((pid, w2, fac, g, e))
dire('  %d etats juges sur %d points distincts (la note : 262 etats sur 24 points)' % (len(LIGNES), len(vus_pt)))
res = []
pire_note = {'q2_bas': 0.0, 'q1': 0.0, 'dE2_bas': 0.0}
pire_bas = {'q2_bas': 0.0, 'q1': 0.0}
for (pid, w2, fac, g, e) in LIGNES:
    n1, n2 = e['n1'], e['n2']
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    r = chaine_miens(n1, n2, w2, g, sites, 0.0625)
    g3 = e['Gamma_2D']['3']
    q2f, q2i = r['flux'] / g3, r['im'] / g3
    q1 = e['chaine']['gammas'][2] / g3
    de2d = e['E_re'] - M.energie_libre(float(n1), float(n2), w2)
    ecart_e = abs(r['dE'] - de2d) / abs(de2d)
    nt = NOTE.get((pid, n1, n2))
    if nt is not None:
        cible = pire_note if g3 >= 1e-11 else pire_bas
        cible['q2_bas'] = max(cible['q2_bas'], rel(q2i, nt['q2_bas']))
        cible['q1'] = max(cible['q1'], rel(q1, nt['q1']))
        pire_note['dE2_bas'] = max(pire_note['dE2_bas'], rel(r['dE'], nt['dE_2_bas']))
    res.append({'id': pid, 'w2': float(w2), 'delta': float(w2) - 2.0, 'fac': str(fac), 'n1': n1, 'n2': n2, 'q2f': q2f, 'q2i': q2i, 'q1': q1,
                'ecart_e': ecart_e, 'fluxim': abs(r['im'] / r['flux'] - 1.0)})
dire('  mes valeurs contre celles du tableau de la note, par etat, Gamma_2D >= 1e-11 : q2 (lu a -2 Im E) %.2e ; q1 %.2e ; dE %.2e (ecarts relatifs maximaux)' % (
    pire_note['q2_bas'], pire_note['q1'], pire_note['dE2_bas']))
dire("  les memes aux etats de Gamma_2D sous 1e-11, ou -2 Im E s'arrondit (13 pour cent aux deux plus petits, a T3) : q2 %.2e ; q1 %.2e" % (
    pire_bas['q2_bas'], pire_bas['q1']))
verdict('E1', len(LIGNES) == 262 and len(vus_pt) == 24 and len(NOTE) >= 262, "262 etats sur 24 points, comme la note")
verdict('E2', max(pire_note.values()) < 5e-3 and max(pire_bas.values()) < 0.15,
        "mes q2, q1 et dE == le tableau de la note a 5e-3 relatif des que Gamma_2D >= 1e-11 (arrondi de -2 Im E) ; a 15 pour cent au plus en dessous")
ex = [r for r in res if r['id'] not in ('T3', 'T4')]
q2s = [r['q2i'] for r in ex]
q2f = [r['q2f'] for r in ex]
q1s = [r['q1'] for r in ex]
dire("  %d etats hors 1.85 et 2.15 : q2 (-2 Im E) de %.3f a %.3f ; (Gamma_flux) de %.3f a %.3f ; la chaine du moteur q1 de %.3f a %.3f" % (
    len(ex), min(q2s), max(q2s), min(q2f), max(q2f), min(q1s), max(q1s)))
verdict('E3', len(ex) == 243 and round(min(q2s), 3) == 0.998 and round(max(q2s), 3) == 1.512 and round(min(q1s), 3) == 0.375 and abs(max(q1s) - 7.00) < 0.02,
        'le gel (i) : q2 dans [0.998 ; 1.512] (exact) contre [0.375 ; 7.00] pour la chaine du moteur (mon maximum : H3 (7,1), Gamma_2D 2.2e-12, a 0.2 pour cent du 7.00)')
bandes = [('|delta| <= 0.05', lambda x: abs(x) < 0.0501), ('0.08 a 0.10', lambda x: 0.0799 < abs(x) < 0.1001), ('0.11 a 0.12', lambda x: 0.1099 < abs(x) < 0.1201)]
tab = []
for nom, f in bandes:
    xs = [r['q2i'] for r in ex if f(r['delta'])]
    tab.append((nom, len(xs), max(xs) if xs else 0.0))
    dire('    %-16s %3d etats, plus grand q2 %.3f' % (nom, len(xs), max(xs) if xs else 0.0))
verdict('E4', [t[1] for t in tab] == [88, 118, 37] and [round(t[2], 3) for t in tab] == [1.101, 1.512, 1.474], 'le gel (ii) : 88 etats, plus grand q2 1.101 ; 118, 1.512 ; 37, 1.474')
n15 = sum(1 for r in ex if 1 / 1.5 <= r['q2i'] <= 1.5)
n15_1 = sum(1 for r in ex if 1 / 2 <= r['q1'] <= 2)
dire("  dans un facteur 1.5 a l'ordre 2 : %d sur 243 (la note : 241) ; dans un facteur 2 a l'ordre 1 : %d sur 243 (la note : 143)" % (n15, n15_1))
lim = sorted((round(r['q2i'], 4), r['id'], r['n1'], r['n2']) for r in ex if 1.49 < r['q2i'] < 1.52)
dire('  etats a q2 entre 1.49 et 1.52 : %s' % lim)
verdict('E5', abs(n15 - 241) <= 1 and n15_1 == 143,
        "la note, verdict 2 : 241 etats sur 243 dans un facteur 1.5 (moi : %d, a un etat de la limite 1.5 : H2 (10,3) a 1.4948) ; 143 dans un facteur 2 au premier ordre (exact)" % n15)
ee = sorted(r['ecart_e'] for r in ex)
med = 0.5 * (ee[len(ee) // 2 - 1] + ee[len(ee) // 2]) if len(ee) % 2 == 0 else ee[len(ee) // 2]
dire("  decalage d'energie, ecart relatif de la chaine d'ordre 2 a l'etat 2D : mediane %.4f, pire %.4f (le gel : 0.11 pour cent, 0.50 pour cent ; plus grand ecart 0.0050)" % (med, ee[-1]))
verdict('E6', abs(med - 0.0011) < 0.00006 and abs(ee[-1] - 0.0050) < 0.0006, "le gel (i), section 9 : energie a 0.11 pour cent en mediane, 0.50 au pire, sur les 243 etats")
fi = sorted(r['fluxim'] for r in ex)
fmed = 0.5 * (fi[len(fi) // 2 - 1] + fi[len(fi) // 2]) if len(fi) % 2 == 0 else fi[len(fi) // 2]
dire("  Gamma_flux contre -2 Im E, au reglage de la sonde : ecart relatif median %.2e, pire %.2e (le gel (iv) : 1.5e-06 et 1.6e-02)" % (fmed, fi[-1]))
verdict('E7', 1e-6 < fmed < 2e-6 and 1.2e-2 < fi[-1] < 2.0e-2,
        "le gel (iv) : Gamma_flux et -2 Im E different de 1.5e-06 en mediane et de 1.6e-02 au pire (moi : meme ordre, a l'arrondi pres de -2 Im E)")
dire('  hors fenetre : T3 (1.85) q2 de %.3f a %.3f ; T4 (2.15) q2 de %.3f a %.3f' % (
    min(r['q2i'] for r in res if r['id'] == 'T3'), max(r['q2i'] for r in res if r['id'] == 'T3'),
    min(r['q2i'] for r in res if r['id'] == 'T4'), max(r['q2i'] for r in res if r['id'] == 'T4')))
dire()
dire("F. LES REFERENCES DE G-8 : ma chaine d'ordre 2 aux deux etats d'ancre, sans decomposition 2D, contre les constantes du gel (section 10)")
GEL = open(GELP, encoding='ascii').read()
GN = re.sub(r'\s+', ' ', GEL)
REFG = {'A1': (2.3236497766513317e-10, 0.002118984943055927), 'A2': (2.794344791699548e-09, -0.0028201377357584354)}
dans_gel = all(repr(x) in GN for pair in REFG.values() for x in pair)
dire('  les quatre constantes sont dans le texte du gel, au caractere pres : %s' % dans_gel)
pireF = []
for pid, (n1, n2) in (('A1', (7, 2)), ('A2', (8, 2))):
    w2 = F(39, 20) if pid == 'A1' else F(41, 20)
    g = float(M.g_du_point(w2))
    sites = M.barriere(float(n1), float(n2), w2, g, True)
    r = chaine_miens(n1, n2, w2, g, sites, 0.0625)
    fl, de = REFG[pid]
    pireF.append((rel(r['flux'], fl), rel(r['dE'], de)))
    dire('  %s (%d,%d) : Gamma_flux %.16e (gel %.16e, ecart %.2e) ; dE %.16e (gel %.16e, ecart %.2e)' % (pid, n1, n2, r['flux'], fl, pireF[-1][0], r['dE'], de, pireF[-1][1]))
verdict('F1', dans_gel and all(a < 1e-3 and b < 1e-6 for a, b in pireF),
        "G-8 : mes references (chaine d'ordre 2 aux etats (7,2) et (8,2), tables et solveur a moi) == les quatre constantes du gel, a 1e-3 (Gamma) et 1e-6 (dE) relatif")
dire()
dire('BILAN : %d controles, %d mordent %s' % (NCTRL[0], len(bad), bad))
sys.exit(1 if bad else 0)
