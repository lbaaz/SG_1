# -*- coding: ascii -*-
"""LECTURE DES POIDS PAR PARTITION, REFAITE PAR MACHINE 2 DEPUIS LE TEXTE (section 5.3 du gel, seconde partie), avant d'avoir lu sonde_boite_fermee_pont_machine1_v1.py. Machine 2, 2026-11-17.
Boite N x N au point sacrifie w2 = 101/50 (meme boite que ma certification precedente : grandes_boites_machine2_v1.py), trois profondeurs. Pour chaque niveau de la fenetre 0.05 < x < 8,
lu par deux decalages-inversions (2 et 5 |delta| sous le vide) :
  - le poids BRUT |V[(0,0)]|^2 du vecteur d'ARPACK (comme ma certification precedente) ;
  - le poids PAR PARTITION : I = sites max(a, b) <= r_c, O = le reste, r_c = 2 (m + max(8, m)) + 2 ; (H_II - E) psi_I = - H_IO psi_O (dense, ordre naturel) ; c^2 = psi_I(0,0)^2 / (|psi_I|^2 + |psi_O|^2) ;
    refait avec r_c + 6, r_c + 12 et une coupure d'une AUTRE FORME (diamant a + b <= 40 + 2 m) ; E = la valeur propre de la lecture.
Sortie : un fichier JSON par boite (liste de niveaux : E, x, brut_2, brut_5, part_<coupure>_<decalage>).
Usage : py -3.11 -P partition_independante_machine2_v1.py <registre> <barreaux> <sortie.json> <cote>"""
import importlib.util
import json
import math
import sys
import time
from fractions import Fraction as F
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

executer = exec
REG = sys.argv[1].rstrip('/\\'); NB = int(sys.argv[2]); SORTIE = sys.argv[3]; N = int(sys.argv[4])
spec = importlib.util.spec_from_file_location("moteur", REG + "/scripts/m17_chaine_v17.py"); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
W2 = F(101, 50); W2F = float(W2); AD = abs(W2F - 2.0); P5 = 5
G_DE = {3: 5.53067e-03, 4: 4.22189e-03, 5: 3.35640e-03}
g = G_DE[NB]
RC = 2 * (NB + max(8, NB)) + 2
SAUTS = sorted((k, l) for k in range(-P5, P5 + 1) for l in range(-P5, P5 + 1) if abs(k) + abs(l) <= P5 and (k + l) % 2 == P5 % 2 and (k, l) > (0, 0))


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
    sig = Ev - sigma_AD * AD; rayon = max(abs(sig - lo), abs(sig - hi)) + 0.5 * AD; k = 40
    while True:
        E, V = eigsh(H, k=k, sigma=sig, which='LM')
        if np.max(np.abs(E - sig)) > rayon or k >= 800:
            break
        k *= 2
    m = (E > lo) & (E < hi); o = np.argsort(E[m])
    return E[m][o], V[:, m][:, o], k


def partition(Hcsr, E, v, I):
    """c^2 par partition pour l'ensemble I (indices tries) : psi_O = v|O ; (H_II - E) psi_I = - H_IO psi_O ; c^2 = psi_I(site 0)^2 / norme^2. Le site (0, 0) est l'indice 0, donc la premiere place de I."""
    masque = np.ones(len(v), dtype=bool); masque[I] = False; O = np.nonzero(masque)[0]
    HII = Hcsr[I][:, I].toarray() - E * np.eye(len(I)); HIO = Hcsr[I][:, O]
    psiI = np.linalg.solve(HII, -(HIO @ v[O]))
    return float(psiI[0] ** 2 / (psiI @ psiI + v[O] @ v[O]))


t0 = time.time(); H = boite_creuse(N); Hc = H.tocsr()
Ev0, V0 = eigsh(H, k=6, sigma=0.0, which='LM'); nu = int(np.argmax(V0[0, :] ** 2)); Ev = float(Ev0[nu]); w0 = float(V0[0, nu] ** 2)
lo, hi = Ev - 8.0 * AD, Ev - 0.05 * AD
idx = np.arange(N * N); a_ = idx // N; b_ = idx % N
COUPURES = {'carre_rc': np.nonzero((a_ <= RC) & (b_ <= RC))[0], 'carre_rc+6': np.nonzero((a_ <= RC + 6) & (b_ <= RC + 6))[0],
            'carre_rc+12': np.nonzero((a_ <= RC + 12) & (b_ <= RC + 12))[0], 'diamant': np.nonzero(a_ + b_ <= 40 + 2 * NB)[0]}
for nom, I in COUPURES.items():
    assert I[0] == 0 and len(I) < N * N - 1000, (nom, len(I))
res = {}
for nom_l, s in (('2', 2.0), ('5.5', 5.5)):
    E, V, k = lecture(H, Ev, s, lo, hi)
    for j in range(len(E)):
        v = V[:, j]; ligne = dict(E=float(E[j]), x=float((Ev - E[j]) / AD * (1.0 if W2F > 2 else -1.0)), brut=float(v[0] ** 2 / (v @ v)))
        for nom, I in COUPURES.items():
            ligne[nom] = partition(Hc, float(E[j]), v, I)
        res.setdefault(nom_l, []).append(ligne)
    print('decalage %s |delta| : %d niveaux (k = %d) ; %.0f s' % (nom_l, len(E), k, time.time() - t0), flush=True)
json.dump(dict(cote=N, barreaux=NB, rc=RC, w0=w0, E_vide=Ev, lectures=res), open(SORTIE, 'w', encoding='ascii'), indent=1, sort_keys=True)
a, b = res['2'], res['5.5']
print('niveaux : %d et %d ; ecart relatif entre les deux decalages, par lecture :' % (len(a), len(b)))
if len(a) == len(b):
    for cle in ('brut', 'carre_rc', 'carre_rc+6', 'carre_rc+12', 'diamant'):
        print('   %-12s plus grand %.2e' % (cle, max(abs(u[cle] / v[cle] - 1.0) for u, v in zip(a, b))))
    print('   coupures entre elles (decalage 2) : carre_rc+6 / carre_rc %.2e ; carre_rc+12 / carre_rc %.2e ; diamant / carre_rc %.2e' % (
        max(abs(u['carre_rc+6'] / u['carre_rc'] - 1.0) for u in a), max(abs(u['carre_rc+12'] / u['carre_rc'] - 1.0) for u in a), max(abs(u['diamant'] / u['carre_rc'] - 1.0) for u in a)))
