# -*- coding: ascii -*-
"""CONTROLE (i), SECOND TEMPS -- machine 2, 2026-11-15. Mon propre calcul des sauts d'ordre 3 de l'echelle resonante (T3 : voisin ; W3 : troisieme voisin ; W5 : cinquieme voisin), ecrit a partir
de la formule 3.1 de la note de machine 1 et du moteur (m17_chaine_v17.py, 82a0be882568fe0c) SEULS ; je n'ai pas lu ordre3_bloc_machine1_v1.py avant d'avoir fini et lance ce script. Methode :
enumeration explicite des chemins (jeux de sauts hors echelle, au plus 5 quanta, parite impaire), un chemin = un produit de trois elements de x^5 du moteur et une paire de denominateurs.
La formule est celle du premier temps (formule_ordre3_jouet_machine2_v1.py : exposant 4 contre l'effectif exact d'un jouet). Controles : (1) Hermiticite (H_{m,m+j} = H_{m+j,m}) ; (2) ordre 2 refait par la meme
methode contre le bloc depose (S, U) ; (3) mes tables contre celles de machine 1 (ordre3_par_etat_v1.json : T3/t, partie hors echelle T3_BB/t, partie echelle T3_A/t, W3, maxima de |W3/t| et |W5/t|) ;
(4) option --chaine : ma chaine d'ordre 3 (bloc d'ordre 2 depose + mes T3, W3, W5) contre ses largeurs G_c3 et ses variantes. 1D seulement : AUCUN calcul 2D, aucune largeur 2D lue.
Usage : py -3.11 -P ordre3_machine2_v1.py <moteur_v17.py> <bloc ordre 2> <sonde_ordre2.json> <verdict_ordre2.json> <ordre3_par_etat_v1.json de machine 1> <sortie.json> [--chaine] [--max=N] <id> [<id> ...]"""
import sys
import json
import math
import time
import importlib.machinery
import importlib.util
from fractions import Fraction as F
import numpy as np

MOTEUR, BLOC2, DEP, V98, M1JSON, SORTIE = sys.argv[1:7]
ARGS = sys.argv[7:]
CHAINE = '--chaine' in ARGS
MAXE = [int(a[6:]) for a in ARGS if a.startswith('--max=')]
MAXE = MAXE[0] if MAXE else 10 ** 9
IDS = [a for a in ARGS if not a.startswith('--')]

spec = importlib.util.spec_from_file_location('moteur', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
P = M.P
W1 = float(M.W1)
C0, C1 = M.CANAL
_brut = M.X_saut_reel
_cx = {}


def X(p, k, l, n1, n2, w2):                      # memoire des elements de x^5 : memes valeurs, moins d'appels
    c = (k, l, n1, n2, w2)
    if c not in _cx:
        _cx[c] = _brut(p, k, l, n1, n2, w2)
    return _cx[c]


M.X_saut_reel = X
ld = importlib.machinery.SourceFileLoader('bloc2', BLOC2)
sp2 = importlib.util.spec_from_loader('bloc2', ld)
B2 = importlib.util.module_from_spec(sp2)
B2.M, B2.np, B2.math = M, np, math
ld.exec_module(B2)

# les sauts hors echelle : tous (k, l), 0 < |k| + |l| <= P, parite de P, hors +-CANAL (definition ecrite ici, confrontee a la liste du moteur)
JS = [(k, l) for k in range(-P, P + 1) for l in range(-P, P + 1) if 0 < abs(k) + abs(l) <= P and (k + l) % 2 == P % 2 and (k, l) not in ((C0, C1), (-C0, -C1))]
assert sorted(JS) == M.sauts_hors_chaine_signes(), 'ma liste de sauts hors echelle differe de celle du moteur'
JSET = set(JS)
JALL = JS + [(C0, C1), (-C0, -C1)]
JMAX = (3 * P) // 2 + 1                          # portee maximale en barreaux d'un saut effectif d'ordre 3 : trois sauts de P quanta, (2j, j) -> 3 j <= 3 P


class Chaine:
    """Un etat (n1, n2) a un point (w2, g) : tables d'ordre 2 et 3 par enumeration de chemins."""

    def __init__(self, n1, n2, w2, g, boite=None):
        self.n1, self.n2, self.w2, self.g = n1, n2, w2, g
        self.boite = boite                       # None, ou (N1, N2) : base tronquee, tout element qui sort de la boite est nul (epreuve --boite)
        self.w = float(w2)
        self.d = C1 * self.w - C0 * W1
        self._V = {}
        self._c = {}

    def V(self, a, b, k, l):
        c = (a, b, k, l)
        r = self._V.get(c)
        if r is None:
            hors = a < 0 or b < 0 or a + k < 0 or b + l < 0
            if self.boite is not None:
                hors = hors or a > self.boite[0] or b > self.boite[1] or a + k > self.boite[0] or b + l > self.boite[1]
            r = 0.0 if hors else (self.g / P) * M.X_saut_reel(P, k, l, float(a), float(b), self.w2)
            self._V[c] = r
        return r

    def ej(self, k, l):
        return -W1 * k + self.w * l

    def coord(self, m):
        return self.n1 + C0 * m, self.n2 + C1 * m

    def depuis(self, m):
        """Contributions au saut m -> m + j, j dans +-1, +-3, +-5, par type : A1, A2 (chemins qui repassent par l'echelle), B (chemins hors echelle)."""
        if m in self._c:
            return self._c[m]
        d, V, ej = self.d, self.V, self.ej
        a, b = self.coord(m)
        res = {}

        def ajoute(j, t, x):
            if abs(j) in (1, 3, 5):
                res.setdefault(j, {'A1': 0.0, 'A2': 0.0, 'B': 0.0})[t] += x

        for (k1, l1) in JS:
            v1 = V(a, b, k1, l1)
            if v1 == 0.0:
                continue
            a1, b1, e1 = a + k1, b + l1, ej(k1, l1)
            # terme B : trois sauts, l et l' hors echelle
            for (k2, l2) in JALL:
                v2 = V(a1, b1, k2, l2)
                if v2 == 0.0:
                    continue
                k12, l12 = k1 + k2, l1 + l2
                if k12 * C1 == C0 * l12:                                    # l' sur l'echelle (ou retour en m) : n'appartient pas a B
                    continue
                a2, b2, e2 = a1 + k2, b1 + l2, e1 + ej(k2, l2)
                for j in (-5, -3, -1, 1, 3, 5):
                    k3, l3 = C0 * j - k12, C1 * j - l12
                    if (k3, l3) not in JSET:
                        continue
                    v3 = V(a2, b2, k3, l3)
                    if v3 == 0.0:
                        continue
                    ajoute(j, 'B', 0.5 * v1 * v2 * v3 * (1.0 / (e1 * e2) + 1.0 / ((j * d - e1) * (j * d - e2))))
            # terme A1 : m -> l (hors echelle) -> m'' (echelle) -> m' = m'' +- 1
            for (k2, l2) in JS:
                k12, l12 = k1 + k2, l1 + l2
                if k12 * C1 != C0 * l12:
                    continue
                s = l12 // C1
                if C0 * s != k12:
                    continue
                v2 = V(a1, b1, k2, l2)
                if v2 == 0.0:
                    continue
                a3, b3 = a + k12, b + l12
                for h in (1, -1):
                    v3 = V(a3, b3, C0 * h, C1 * h)
                    if v3 == 0.0:
                        continue
                    j = s + h
                    ajoute(j, 'A1', -0.5 * v1 * v2 * v3 / ((j * d - e1) * (s * d - e1)))
        # terme A2 : m -> m'' = m + h (echelle) -> l (hors echelle) -> m' (echelle)
        for h in (1, -1):
            v1 = V(a, b, C0 * h, C1 * h)
            if v1 == 0.0:
                continue
            a_, b_ = a + C0 * h, b + C1 * h
            for (k2, l2) in JS:
                v2 = V(a_, b_, k2, l2)
                if v2 == 0.0:
                    continue
                a2, b2, e2 = a_ + k2, b_ + l2, self.ej(k2, l2)
                for s in range(-JMAX, JMAX + 1):
                    k3, l3 = C0 * s - k2, C1 * s - l2
                    if (k3, l3) not in JSET:
                        continue
                    v3 = V(a2, b2, k3, l3)
                    if v3 == 0.0:
                        continue
                    ajoute(h + s, 'A2', -0.5 * v1 * v2 * v3 / ((h * d + e2) * e2))
        self._c[m] = res
        return res

    def saut(self, m, j, partie=None):
        r = self.depuis(m).get(j)
        if r is None:
            return 0.0
        return sum(r.values()) if partie is None else (r['A1'] + r['A2'] if partie == 'A' else r[partie])

    def t(self, m):
        a, b = self.coord(m)
        return self.V(a, b, C0, C1)

    def ordre2(self, m, deux):
        """Ordre 2 refait par la meme methode : deplacement S(m) (deux = 0) et saut au second voisin U(m) (deux = 1)."""
        d, V, ej = self.d, self.V, self.ej
        a, b = self.coord(m)
        tot = 0.0
        for (k, l) in JS:
            v = V(a, b, k, l)
            if v == 0.0:
                continue
            e = ej(k, l)
            if deux == 0:
                tot += v * v / (-e)
            else:
                k2, l2 = 2 * C0 - k, 2 * C1 - l
                if (k2, l2) in JSET:
                    tot += 0.5 * v * V(a + k, b + l, k2, l2) * (1.0 / (-e) + 1.0 / (2.0 * d - e))
        return tot


def chaine3(tb, ch, ef, avec_T3=True, avec_W3=True, avec_W5=True, recul=0):
    """Chaine d'ordre 3 : le bloc d'ordre 2 depose (tb) auquel j'ajoute MES sauts T3 (voisin), W3 (3e voisin), W5 (5e voisin)."""
    d, Mh, m_min = tb['d'], tb['Mh'], tb['m_min']
    eta_c = abs(d) * ef
    debut_cap = tb['m2_bord'] + tb['b_M'] // 2 + recul
    n = Mh - m_min + 1
    H = np.zeros((n, n), dtype=complex)
    Wd = np.zeros(n)
    for m in range(m_min, Mh + 1):
        i = m - m_min
        H[i, i] = m * d + (tb['S'][m] - tb['S'][0])
        if m > debut_cap:
            Wd[i] = eta_c * (m - debut_cap) ** 2
            H[i, i] += -1j * Wd[i]
        if m < Mh:
            x = tb['t'][m] + (ch.saut(m, 1) if avec_T3 else 0.0)
            H[i, i + 1] = x
            H[i + 1, i] = x
        if m + 2 <= Mh:
            H[i, i + 2] = tb['U'][m]
            H[i + 2, i] = tb['U'][m]
        if avec_W3 and m + 3 <= Mh:
            x = ch.saut(m, 3)
            H[i, i + 3] = x
            H[i + 3, i] = x
        if avec_W5 and m + 5 <= Mh:
            x = ch.saut(m, 5)
            H[i, i + 5] = x
            H[i + 5, i] = x
    valeurs, vecteurs = np.linalg.eig(H)
    recs = np.abs(vecteurs[-m_min, :]) ** 2
    nu = np.lexsort((valeurs.real, -recs))[0]
    psi2 = np.abs(vecteurs[:, nu]) ** 2
    return {'Gamma_flux': float(2.0 * (Wd @ psi2) / psi2.sum()), 'dE': float(valeurs[nu].real + tb['S'][0]), 'recouvrement': float(recs[nu])}


def epreuve_boite():
    """Epreuve sur le VRAI operateur (elements de x^5 du moteur), dans une base tronquee (boite 0 <= n1 <= 11, 0 <= n2 <= 6), echelle de (3, 1) a w2 = 2.07 (autre echelle, autre w2 que ceux de
    machine 1) : l'echelle y compte 6 sites (m = -1 .. 4), B 72 etats. (a) hermiticite de V ; (b) formule 3.1 ecrite en matrices DENSES contre l'effectif exact de des Cloizeaux (exposants
    de g : 3 sans l'ordre 3, 4 avec) ; (c) mes chemins (classe Chaine, dans la meme boite) contre la formule dense, saut par saut (j = 1, 3, 5, et zero aux j pairs)."""
    N1, N2 = 11, 6
    w2 = F('2.07')
    n1, n2 = 3, 1
    ms = [m for m in range(-5, 12) if n1 + C0 * m >= 0 and n2 + C1 * m >= 0 and n1 + C0 * m <= N1 and n2 + C1 * m <= N2]
    etats = [(a, b) for a in range(N1 + 1) for b in range(N2 + 1)]
    ia = {(n1 + C0 * m, n2 + C1 * m): i for i, m in enumerate(ms)}
    iA = [etats.index(s) for s in ia]
    iB = [i for i in range(len(etats)) if i not in iA]
    w = float(w2)
    Eall = np.array([-W1 * a + w * b for (a, b) in etats])
    ch0 = Chaine(n1, n2, w2, 1.0, boite=(N1, N2))

    def Vmat(g):
        Vm = np.zeros((len(etats), len(etats)))
        for i, (a, b) in enumerate(etats):
            for (k, l) in JALL:
                if 0 <= a + k <= N1 and 0 <= b + l <= N2:
                    Vm[etats.index((a + k, b + l)), i] = g * ch0.V(a, b, k, l)
        return Vm
    V1 = Vmat(1.0)
    herm = np.abs(V1 - V1.T).max() / np.abs(V1).max()
    print('(a) hermiticite de V sur le vrai operateur : ecart relatif max %.3e (|V| max %.3e)' % (herm, np.abs(V1).max()))
    nA, nB = len(iA), len(iB)
    gaps = min(abs(Eall[i] - Eall[j]) for i in iB for j in iA)
    g0 = 0.01 * gaps / np.abs(V1).max()
    print('    echelle de %d sites (m = %d .. %d), B %d etats, plus petit ecart A-B %.3f, g0 = %.3e (|V| max %.3e)' % (nA, ms[0], ms[-1], nB, gaps, g0, g0 * np.abs(V1).max()))
    E = Eall

    def dense(g):
        V = g * V1
        VAA = V[np.ix_(iA, iA)]
        H1 = VAA.copy()
        H2 = np.zeros((nA, nA))
        H3 = np.zeros((nA, nA))
        for p, m in enumerate(iA):
            for q, mp in enumerate(iA):
                vm, vmp = V[iB, m], V[iB, mp]
                H2[p, q] = 0.5 * np.sum(vm * vmp * (1.0 / (E[m] - E[iB]) + 1.0 / (E[mp] - E[iB])))
                s3 = 0.0
                for r, mpp in enumerate(iA):
                    s3 += -0.5 * np.sum(vm * V[iB, mpp] * V[mpp, mp] / ((E[mp] - E[iB]) * (E[mpp] - E[iB])))
                    s3 += -0.5 * np.sum(V[m, mpp] * V[mpp, iB] * vmp / ((E[m] - E[iB]) * (E[mpp] - E[iB])))
                VBB = V[np.ix_(iB, iB)]
                u1, u2 = vm / (E[m] - E[iB]), vmp / (E[m] - E[iB])
                x1, x2 = vm / (E[mp] - E[iB]), vmp / (E[mp] - E[iB])
                s3 += 0.5 * (u1 @ VBB @ u2 + x1 @ VBB @ x2)
                H3[p, q] = s3
        return np.diag(E[iA]), H1, H2, H3

    def exact(g):
        H = np.diag(E) + g * V1
        wv, v = np.linalg.eigh(H)
        poids = (v[iA, :] ** 2).sum(axis=0)
        idx = np.argsort(-poids)[:nA]
        C = v[np.ix_(iA, idx)]
        ws, us = np.linalg.eigh(C.T @ C)
        Ct = C @ (us @ np.diag(ws ** -0.5) @ us.T)
        return Ct @ np.diag(wv[idx]) @ Ct.T
    r2, r3 = [], []
    for lam in (1.0, 2.0, 4.0, 8.0):
        g = g0 * lam
        ex = exact(g)
        H0, H1, H2, H3 = dense(g)
        r2.append(np.abs(ex - (H0 + H1 + H2)).max())
        r3.append(np.abs(ex - (H0 + H1 + H2 + H3)).max())
        print('(b) g = %.3e : reste sans l ordre 3 %.3e ; avec %.3e ; |H3| max %.3e' % (g, r2[-1], r3[-1], np.abs(H3).max()))
    p2 = [math.log2(r2[i + 1] / r2[i]) for i in range(3)]
    p3 = [math.log2(r3[i + 1] / r3[i]) for i in range(3)]
    print('    exposants de g (attendus : 3 sans l ordre 3, 4 avec) : sans %s ; avec %s' % (['%.2f' % x for x in p2], ['%.2f' % x for x in p3]))
    ok_b = all(abs(x - 3) < 0.3 for x in p2[:2]) and all(abs(x - 4) < 0.3 for x in p3[:2])
    g = g0
    H0, H1, H2, H3 = dense(g)
    chb = Chaine(n1, n2, w2, g, boite=(N1, N2))
    pire_c, pire_pair = 0.0, 0.0
    ech = np.abs(H3).max()
    for p, m in enumerate(ms):
        for q, mq in enumerate(ms):
            j = mq - m
            if j == 0:
                mien = 0.0
            else:
                mien = chb.saut(m, j) if abs(j) in (1, 3, 5) else 0.0
            if abs(j) % 2 == 0:
                pire_pair = max(pire_pair, abs(H3[p, q]) / ech)
            else:
                pire_c = max(pire_c, abs(mien - H3[p, q]) / ech)
    print('(c) mes chemins contre la formule dense (|H3| max %.3e) : plus grand ecart %.3e (relatif au plus grand saut) ; sauts d ordre 3 aux j pairs et diagonale (doivent etre nuls) : %.3e' % (ech, pire_c, pire_pair))
    for jj in (1, 3, 5):                        # chaque ordre de saut, a part : grandeur et ecart relatif A LUI-MEME
        paires = [(p, p + jj) for p in range(len(ms) - jj)]
        ec = max(abs(chb.saut(ms[p], jj) - H3[p, q]) / abs(H3[p, q]) for p, q in paires)
        print('    j = %d : %d saut(s), |saut| de %.3e a %.3e (le plus grand |H3| : %.3e), ecart relatif au saut lui-meme %.3e' % (
            jj, len(paires), min(abs(H3[p, q]) for p, q in paires), max(abs(H3[p, q]) for p, q in paires), ech, ec))
    # (d) les sauts lointains, UN A LA FOIS, contre l'exact : aux j = 3 et 5 (impairs), l'exact vaut H3 + O(g^5) (les ordres 1 et 2 n'y atteignent pas, l'ordre 4 est pair) :
    # l'ecart relatif au saut lui-meme doit donc croitre en g^2 (facteur 4 quand g double)
    print('(d) saut lointain contre l effectif exact, ecart relatif au saut lui-meme (attendu : en g^2, facteur 4 par doublement de g)')
    pq = {3: (0, 3), 5: (0, 5)}
    reps = {}
    for jj, (p, q) in pq.items():
        reps[jj] = []
        for lam in (4.0, 8.0, 16.0):
            gg = g0 * lam
            e3 = dense(gg)[3][p, q]
            reps[jj].append(abs(exact(gg)[p, q] - e3) / abs(e3))
        print('    j = %d (m = %d -> %d) : g = %s : ecarts relatifs %s ; rapports %s' % (jj, ms[p], ms[q], ' '.join('%.2e' % (g0 * x) for x in (4.0, 8.0, 16.0)), ' '.join('%.2e' % x for x in reps[jj]),
              ' '.join('%.2f' % (reps[jj][i + 1] / reps[jj][i]) for i in range(2))))
    ok_d = all(3.2 < reps[jj][i + 1] / reps[jj][i] < 5.0 for jj in reps for i in range(2))
    ok_c = pire_c < 1e-10 and pire_pair < 1e-10
    print('EPREUVE SUR LA BASE TRONQUEE : hermiticite %s ; formule contre l exact %s ; chemins contre formule dense %s ; sauts lointains j = 3 et 5 contre l exact %s' % (
        'TIENT' if herm < 1e-12 else 'MORD', 'TIENT' if ok_b else 'MORD', 'TIENT' if ok_c else 'MORD', 'TIENT' if ok_d else 'MORD'))


if '--boite' in ARGS:
    epreuve_boite()
    raise SystemExit(0)

Dp = {p['id']: p for p in json.load(open(DEP))['points']}
Vp = {p['id']: p for p in json.load(open(V98))['points']}
M1 = json.load(open(M1JSON))
EF = M1['reglage']['ef']
out = {'points': {}, 'reglage': {'ef': EF}}
pire = {'herm': 0.0, 'S2': 0.0, 'U2': 0.0, 'T3': 0.0, 'T3_BB': 0.0, 'T3_A': 0.0, 'W3': 0.0, 'W3max': 0.0, 'W5max': 0.0, 'G3': 0.0, 'var': 0.0}
cas = {k: None for k in pire}
cumul = {'etats': 0, 'chaine': 0}


def maj(cle, x, ou):
    if x > pire[cle]:
        pire[cle] = x
        cas[cle] = ou


for pid in IDS:
    t0 = time.time()
    p = Dp[pid]
    w2 = F(p['w2'])
    g = p['g']
    dep = {e['rang']: e for e in p['etats']}
    m1p = {e['rang']: e for e in M1['points'][pid]['etats']}
    liste = []
    nchaine = 0
    for ev in Vp[pid]['etats']:
        if ev['exclu'] is not None:
            continue
        e = dep[ev['rang']]
        n1, n2 = float(e['n1']), float(e['n2'])
        r = ev['rang']
        s1 = m1p[r]
        sites = M.barriere(n1, n2, w2, g, True)
        tb = B2.tables_ordre2(n1, n2, w2, g, sites, M_facteur=4)
        mb = tb['m2_bord']
        assert mb == s1['m_bord'] and tb['m_min'] == s1['m_min'], ('barriere differente', pid, r)
        ch = Chaine(n1, n2, w2, g)
        ou = '%s rang %d (%d,%d)' % (pid, r, e['n1'], e['n2'])
        # (1) hermiticite : H_{m,m+j} = H_{m+j,m}
        for m in range(max(tb['m_min'], 0), mb + 2):
            for j in (1, 3, 5):
                x, y = ch.saut(m, j), ch.saut(m + j, -j)
                maj('herm', abs(x - y) / max(abs(ch.t(m)), 1e-300), ou + ' m=%d j=%d' % (m, j))
        # (2) ordre 2 refait contre le bloc depose
        for m in range(max(tb['m_min'], 0), mb + 3):
            maj('S2', abs(ch.ordre2(m, 0) - tb['S'][m]) / max(abs(tb['S'][m]), 1e-300), ou + ' m=%d' % m)
            maj('U2', abs(ch.ordre2(m, 1) - tb['U'][m]) / max(abs(tb['U'][m]), 1e-300), ou + ' m=%d' % m)
            assert abs(ch.t(m) - tb['t'][m]) <= 1e-15 * abs(tb['t'][m]), ('t differe', ou, m)
        # (3) mes tables contre les siennes
        for b in s1['barriere']:
            m = b['m']
            tm, tm1 = ch.t(m), ch.t(m - 1)
            maj('T3', abs(ch.saut(m - 1, 1) / tm1 - b['T3_sur_t_avant']) / max(abs(b['T3_sur_t_avant']), 1e-300), ou + ' m=%d (avant)' % m)
            maj('T3', abs(ch.saut(m, 1) / tm - b['T3_sur_t']) / max(abs(b['T3_sur_t']), 1e-300), ou + ' m=%d' % m)
            ech = abs(b['T3_BB_sur_t']) + abs(b['T3_A_sur_t'])             # echelle de la compensation : les deux parts
            maj('T3_BB', abs(ch.saut(m, 1, 'B') / tm - b['T3_BB_sur_t']) / max(ech, 1e-300), ou + ' m=%d' % m)
            maj('T3_A', abs(ch.saut(m, 1, 'A') / tm - b['T3_A_sur_t']) / max(ech, 1e-300), ou + ' m=%d' % m)
            if m - 3 >= tb['m_min']:
                maj('W3', abs(ch.saut(m - 3, 3) - b['W3_avant']) / max(abs(b['W3_avant']), 1e-300), ou + ' m=%d (m-3)' % m)
        w3 = max(abs(ch.saut(m, 3) / ch.t(m)) for m in range(0, mb + 1))
        w5 = max(abs(ch.saut(m, 5) / ch.t(m)) for m in range(0, mb + 1))
        maj('W3max', abs(w3 - s1['W3_sur_t_max_barriere']) / s1['W3_sur_t_max_barriere'], ou)
        maj('W5max', abs(w5 - s1['W5_sur_t_max_barriere']) / s1['W5_sur_t_max_barriere'], ou)
        rec = {'rang': r, 'n1': e['n1'], 'n2': e['n2'], 'm_bord': mb, 'W3_max_mien': w3, 'W3_max_sien': s1['W3_sur_t_max_barriere'], 'W5_max_mien': w5, 'W5_max_sien': s1['W5_sur_t_max_barriere']}
        # (4) ma chaine d'ordre 3 contre la sienne
        if CHAINE and nchaine < MAXE:
            nchaine += 1
            c3 = chaine3(tb, ch, EF)
            var = {'T3_seul': chaine3(tb, ch, EF, avec_W3=False, avec_W5=False)['Gamma_flux'], 'W3_seul': chaine3(tb, ch, EF, avec_T3=False, avec_W5=False)['Gamma_flux'],
                   'sans_W5': chaine3(tb, ch, EF, avec_W5=False)['Gamma_flux'], 'ef_double': chaine3(tb, ch, 2 * EF)['Gamma_flux'], 'ef_demi': chaine3(tb, ch, EF / 2)['Gamma_flux'],
                   'recul_4': chaine3(tb, ch, EF, recul=4)['Gamma_flux']}
            maj('G3', abs(c3['Gamma_flux'] / s1['G_c3'] - 1.0), ou)
            for k, v in var.items():
                maj('var', abs(v / s1['variantes'][k] - 1.0), ou + ' ' + k)
            rec.update({'G_c3_mien': c3['Gamma_flux'], 'G_c3_sien': s1['G_c3'], 'rapport_c3_c2_mien': c3['Gamma_flux'] / s1['G_c2'], 'variantes_miennes': var})
            cumul['chaine'] += 1
        liste.append(rec)
        cumul['etats'] += 1
        print('  %s : m_bord %2d, W3max %.3e (sien %.3e), W5max %.3e (sien %.3e)%s' % (ou, mb, w3, s1['W3_sur_t_max_barriere'], w5, s1['W5_sur_t_max_barriere'],
              ('' if 'G_c3_mien' not in rec else ', G_c3 %.5e (sien %.5e)' % (rec['G_c3_mien'], rec['G_c3_sien']))), flush=True)
    out['points'][pid] = {'etats': liste, 'duree_s': round(time.time() - t0, 1)}
print()
print('RESUME : %d etats, dont %d avec chaine' % (cumul['etats'], cumul['chaine']))
for k in ('herm', 'S2', 'U2', 'T3', 'T3_BB', 'T3_A', 'W3', 'W3max', 'W5max', 'G3', 'var'):
    print('  %-6s plus grand ecart relatif %.3e   (%s)' % (k, pire[k], cas[k]))
out['pire'] = pire
out['cas'] = cas
json.dump(out, open(SORTIE, 'w'), indent=1, sort_keys=True)
