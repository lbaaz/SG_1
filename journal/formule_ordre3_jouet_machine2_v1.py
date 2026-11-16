# -*- coding: ascii -*-
"""CONTROLE (i), PREMIER TEMPS -- machine 2, 2026-11-15. La formule du terme d'ordre 3 de la note de machine 1 (section 3.1, formes de Loewdin) est ecrite ICI, de ma main, a partir du texte
de la note seul (je n'ai pas lu son bloc ordre3_bloc_machine1_v1.py), et confrontee au hamiltonien effectif EXACT d'un modele jouet aleatoire : A (4 niveaux, quasi degeneres, ecarts de l'ordre de
0.03) et B (7 niveaux, ecarts a A de 1 a 3), couplage V = g R, R symetrique reel dense (blocs AA, AB, BB). Hamiltonien effectif exact = celui de des Cloizeaux : projections sur A des 4
etats propres de plus grand poids sur A, puis orthonormalisation symetrique. Attendu : le reste apres ordre 3 decroit comme g^4 (rapport 16 quand g double), sans l'ordre 3 comme g^3 (rapport 8).
Hors chaine, une plume, AUCUN calcul 2D. Usage : py -3.11 -P formule_ordre3_jouet_machine2_v1.py"""
import numpy as np

rng = np.random.default_rng(20261115)
nA, nB = 4, 7
EA = np.array([0.0, 0.031, 0.062, 0.017])
EB = np.array([1.3, -1.7, 2.2, -2.6, 1.9, -1.2, 2.9])
R = rng.normal(size=(nA + nB, nA + nB))
R = (R + R.T) / 2.0
A, B = list(range(nA)), list(range(nA, nA + nB))
E = np.concatenate([EA, EB])


def h_eff_exact(g):
    H = np.diag(E) + g * R
    w, v = np.linalg.eigh(H)
    poids = (v[:nA, :] ** 2).sum(axis=0)
    idx = np.argsort(-poids)[:nA]
    C = v[:nA, idx]
    S = C.T @ C
    ws, us = np.linalg.eigh(S)
    Ct = C @ (us @ np.diag(ws ** -0.5) @ us.T)
    return Ct @ np.diag(w[idx]) @ Ct.T


def ordres(g):
    V = g * R
    H1 = V[:nA, :nA].copy()
    H2 = np.zeros((nA, nA))
    H3 = np.zeros((nA, nA))
    for m in A:
        for mp in A:
            s2 = 0.0
            for l in B:
                s2 += 0.5 * V[m, l] * V[l, mp] * (1.0 / (E[m] - E[l]) + 1.0 / (E[mp] - E[l]))
            H2[m, mp] = s2
            s3 = 0.0
            for l in B:
                for mpp in A:                                   # premier bloc de la formule 3.1 (deux termes)
                    s3 += -0.5 * (V[m, l] * V[l, mpp] * V[mpp, mp] / ((E[mp] - E[l]) * (E[mpp] - E[l]))
                                  + V[m, mpp] * V[mpp, l] * V[l, mp] / ((E[m] - E[l]) * (E[mpp] - E[l])))
            for l in B:                                         # second bloc : somme sur deux niveaux de B
                for lp in B:
                    s3 += 0.5 * V[m, l] * V[l, lp] * V[lp, mp] * (1.0 / ((E[m] - E[l]) * (E[m] - E[lp])) + 1.0 / ((E[mp] - E[l]) * (E[mp] - E[lp])))
            H3[m, mp] = s3
    return np.diag(EA), H1, H2, H3


print('formule 3.1 de la note de machine 1 contre l effectif exact (jouet aleatoire, A 4 niveaux, B 7 niveaux)')
r2, r3 = [], []
for g in (0.0125, 0.025, 0.05, 0.1):
    ex = h_eff_exact(g)
    H0, H1, H2, H3 = ordres(g)
    a = np.abs(ex - (H0 + H1 + H2)).max()
    b = np.abs(ex - (H0 + H1 + H2 + H3)).max()
    r2.append(a)
    r3.append(b)
    print('  g = %.4f : reste sans l ordre 3 %.3e ; avec l ordre 3 %.3e ; |H3| max %.3e' % (g, a, b, np.abs(H3).max()))
p2 = [np.log2(r2[i + 1] / r2[i]) for i in range(len(r2) - 1)]
p3 = [np.log2(r3[i + 1] / r3[i]) for i in range(len(r3) - 1)]
print('  exposants de g (attendus : 3 sans l ordre 3, 4 avec) : sans %s ; avec %s' % (['%.2f' % x for x in p2], ['%.2f' % x for x in p3]))
ok = abs(p2[0] - 3) < 0.25 and abs(p3[0] - 4) < 0.25 and abs(p2[1] - 3) < 0.25 and abs(p3[1] - 4) < 0.25
print('FORMULE 3.1 : %s' % ('TIENT sur le jouet' if ok else 'NE TIENT PAS sur le jouet'))
