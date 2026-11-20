# -*- coding: ascii -*-
"""GRANDES BOITES au point sacrifie w2 = 101/50, 3 barreaux (machine 2, hors chaine, classe 3) -- calcul demande par machine 1 (lot 4e15e302d97e26b8), ATTENDUS ECRITS PAR ELLE AVANT.
Derive de boite2d_nue_machine2_v1.py (meme boite, meme fenetre, meme rho lisse, meme y_k) avec DEUX LECTURES independantes de chaque niveau : decalage-inversion a 2 |delta| puis a 5 |delta|
sous le niveau-vide ; chaque lecture exige que la fenetre soit strictement contenue dans les niveaux trouves (k double tant que non) ; un niveau est FIABLE si ses deux y s'accordent a 2 pour cent.
Sortie : une ligne lisible par boite et, dans le fichier JSONL passe en dernier argument, une ligne JSON par boite : cote, w0, niveaux (ecart au vide en |delta|, y lecture 1, y lecture 2, fiable), somme / largeur, participation.
Usage : py -3.11 -P grandes_boites_machine2_v1.py <registre> <barreaux> <fichier.jsonl> <cote> [cote ...]"""
import importlib.util
import json
import math
import sys
import time
from fractions import Fraction as F
import numpy as np
import mpmath as mp
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

executer = exec
REG = sys.argv[1].rstrip('/\\'); NB = int(sys.argv[2]); JSONL = sys.argv[3]; COTES = [int(x) for x in sys.argv[4:]]
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
for bloc in ("chaine_ordre2_bloc_machine1_v1.py", "ordre3_bloc_machine1_v1.py", "chaine_adaptee_bloc_machine1_v1.py"):
    p = REG + "/scripts/" + bloc; executer(compile(open(p, encoding="ascii").read(), p, "exec"))
W2 = F(101, 50); W2F = float(W2); AD = abs(W2F - 2.0); P5 = 5
G_DE = {3: 5.53067e-03, 4: 4.22189e-03, 5: 3.35640e-03}
g = G_DE[NB]
SAUTS = sorted((k, l) for k in range(-P5, P5 + 1) for l in range(-P5, P5 + 1) if abs(k) + abs(l) <= P5 and (k + l) % 2 == P5 % 2 and (k, l) > (0, 0))
sites = M.barriere(0, 0, W2, g, True); tb = tables_ordre2(0, 0, W2, g, sites); t3 = tables_ordre3(0, 0, W2, g, tb)
OFFS = np.sort(-np.logspace(math.log10(0.04 * AD), math.log10(9.0 * AD), 3000))
LOGRHO = []
for (a, c, L) in VARIANTES_ADAPTEES:
    H, Wd, i0 = matrice_adaptee(tb, t3, a, c, L, 3)
    val, vec = np.linalg.eig(H); nu = int(np.lexsort((val.real, -np.abs(vec[i0, :]) ** 2))[0]); Ev = float(val[nu].real)
    r = [-np.linalg.solve((Ev + dE) * np.eye(len(H)) - H, np.eye(len(H))[:, i0])[i0].imag / math.pi for dE in OFFS]
    LOGRHO.append(np.log(np.maximum(np.array(r), 1e-300)))
LOGRHO = np.median(np.array(LOGRHO), axis=0)


def boite_creuse(N):
    li, co, va = [], [], []
    di = np.array([-(i // N) + W2F * (i % N) for i in range(N * N)])
    for a in range(N):
        for b in range(N):
            i = a * N + b
            for (k, l) in SAUTS:
                a2, b2 = a + k, b + l
                if 0 <= a2 < N and 0 <= b2 < N:
                    V = (g / P5) * M.X_saut_reel(P5, k, l, float(a), float(b), W2)
                    if V:
                        j = a2 * N + b2; li += [i, j]; co += [j, i]; va += [V, V]
    return (sp.csr_matrix((va, (li, co)), shape=(N * N, N * N)) + sp.diags(di)).tocsc()


def lecture(H, Ev, sigma_AD, lo, hi):
    """Niveaux de la fenetre ]lo, hi[ autour de sigma = Ev - sigma_AD |delta| ; k double tant que la fenetre n'est pas strictement contenue dans les niveaux trouves."""
    sig = Ev - sigma_AD * AD; rayon = max(abs(sig - lo), abs(sig - hi)) + 0.5 * AD; k = 40
    while True:
        E, V = eigsh(H, k=k, sigma=sig, which='LM')
        if np.max(np.abs(E - sig)) > rayon or k >= 800:
            break
        k *= 2
    m = (E > lo) & (E < hi); o = np.argsort(E[m])
    return E[m][o], (V[0, :] ** 2)[m][o], k


out = open(JSONL, 'a', encoding='ascii')
print('# barreaux %d  g = %.5e  w2 = 101/50  delta = %+.4f   deux lectures (sigma a 2 et 5 |delta| sous le vide) ; fiable = y d\'accord a 2 pour cent' % (NB, g, W2F - 2.0))
print('# cote  dim    w0         niveaux  fiables  Somme/larg (avec 1/w0)  participation(y)  k1/k2   secondes')
for N in COTES:
    t0 = time.time(); H = boite_creuse(N)
    Ev0, V0 = eigsh(H, k=6, sigma=0.0, which='LM'); nu = int(np.argmax(V0[0, :] ** 2)); Ev = float(Ev0[nu]); w0 = float(V0[0, nu] ** 2)
    lo, hi = Ev - 8.0 * AD, Ev - 0.05 * AD
    E1, c1, k1 = lecture(H, Ev, 2.0, lo, hi); E2, c2, k2 = lecture(H, Ev, 5.0, lo, hi)
    rho = lambda E: np.exp(np.interp(E - Ev, OFFS, LOGRHO))
    y1 = c1 / (w0 * rho(E1)); y2 = c2 / (w0 * rho(E2))
    niv, fiables = [], 0
    if len(E1) != len(E2) or (len(E1) and np.max(np.abs(E1 - E2)) > 1e-9):
        print('ATTENTION cote %d : les deux lectures ne trouvent pas les memes niveaux (%d contre %d)' % (N, len(E1), len(E2)), flush=True)
    for e, a_, b_ in zip(E1, y1, y2[:len(y1)]):
        ok = bool(abs(a_ - b_) <= 0.02 * max(abs(a_), 1e-300)); fiables += ok
        niv.append(dict(off=float((e - Ev) / AD), y1=float(a_ / AD), y2=float(b_ / AD), fiable=ok))
    y = np.array([x['y1'] for x in niv]); S = float(y.sum()) / 7.95 if len(y) else 0.0; part = float(y.sum() ** 2 / np.sum(y ** 2)) if len(y) else 0.0
    out.write(json.dumps(dict(cote=N, barreaux=NB, w0=w0, n=len(niv), fiables=fiables, somme=S, participation=part, niveaux=niv), sort_keys=True) + '\n'); out.flush()
    print('%-5d %-6d %.8f  %-7d  %-7d  %-22.4f  %-16.3f  %d/%d   %.0f' % (N, N * N, w0, len(niv), fiables, S, part, k1, k2, time.time() - t0), flush=True)
