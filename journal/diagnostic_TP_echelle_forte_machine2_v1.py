# -*- coding: ascii -*-
"""DIAGNOSTIC DU TEMOIN POSITIF A BARREAUX PLUS FORTS -- machine 2, v1, 13/11/2026. HORS GEL, NON OPPOSABLE.
Question : le palier du temoin a G20, qui n'a que quatre (j = 6) ou trois (j = 8) valeurs a 5 pour cent au bord fort
de l'echelle (k = -2), se prolonge-t-il du cote de l'absorbeur plus fort (k = -3 a -6) ? C'est la question que l'acte nn
laisse ouverte (nn.6 (e), nn.13). JUMEAU H+ SEUL (aucune decomposition du fantome, aucun point de M17).
Methode : celle de rejeu_ponctuel_TP_machine1_v1.py (non opposable aussi, mais deja confrontee a ma sonde a 3e-4) :
H_2D du moteur (absorbeur natif F1), r_c = 40, N = r_c + 20 (G20) ou + 30 (G30), eta = 0.05 * 2^(-k), etat de plus grand
recouvrement hermitien avec le vide de Fock, gamma = -2 Im E, SANS suivi par continuite. Le recouvrement est consigne :
c'est lui qui dit si l'etat lu est encore le meme. k = -2 est REJOUE comme ancre (a comparer a ma sonde, sonde_etage1.json).
Usage : python -P diagnostic_TP_echelle_forte_machine2_v1.py <moteur> <liste des retenus> <dossier de sortie> <G20|G30>
Une decomposition a la fois ; chaque resultat est ecrit des qu'il existe (reprise par fichier sous identite)."""
import hashlib
import importlib.util
import json
import os
import platform
import sys
import time
import unicodedata
from fractions import Fraction

import numpy as np

moteur, retenus, sortie, geom = sys.argv[1:5]
N = {'G20': 60, 'G30': 70}[geom]
R_C = 40
KS = [-2, -3, -4, -5, -6]
os.makedirs(sortie, exist_ok=True)
FJ = os.path.join(sortie, 'diag_%s.json' % geom)
FL = open(os.path.join(sortie, 'diag_%s.log' % geom), 'a', encoding='ascii', newline='\n')


def dire(s):
    print(s, flush=True)
    FL.write(s + '\n')
    FL.flush()


def cB(chemin):
    t = unicodedata.normalize('NFC', open(chemin, 'rb').read().decode('utf-8')).replace('\r\n', '\n')
    return hashlib.sha256(t.encode('utf-8')).hexdigest()[:16]


assert cB(moteur) == '82a0be882568fe0c', 'canon du moteur'
assert cB(retenus) == '69b3bab3bb8480b7', 'canon de la liste des retenus'
spec = importlib.util.spec_from_file_location('moteur_m17', moteur)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)
dire('plateforme : %s %s, python %s, numpy %s ; geometrie %s (N = %d, r_c = %d)' % (
    platform.system(), platform.machine(), platform.python_version(), np.__version__, geom, N, R_C))
dire('entrants : moteur %s ; liste %s' % (cB(moteur), cB(retenus)))
fait = json.load(open(FJ)) if os.path.exists(FJ) else []
cles = {(r['j'], r['k']) for r in fait}
w2 = Fraction(39, 20)
for r in json.load(open(retenus))['retenus']:
    for k in KS:
        if (r['j'], k) in cles:
            dire('j = %d k = %d : deja fait (repris)' % (r['j'], k))
            continue
        eta = 0.05 * 2.0 ** (-k)
        t0 = time.time()
        H = M.H_2D(N, w2, r['g'], +1, 'x5', eta, R_C)[0]
        vals, vecs = np.linalg.eig(H)
        ov = np.abs(vecs[0, :]) ** 2 / np.sum(np.abs(vecs) ** 2, axis=0)
        i = int(np.argmax(ov))
        second = float(np.sort(ov)[-2])
        rec = {'j': r['j'], 'g': r['g'], 'k': k, 'eta': eta, 'geom': geom, 'N': N, 'E_re': float(vals[i].real),
               'E_im': float(vals[i].imag), 'gamma': float(-2.0 * vals[i].imag), 'recouvrement': float(ov[i]),
               'deuxieme_recouvrement': second, 'duree_s': time.time() - t0}
        fait.append(rec)
        json.dump(fait, open(FJ, 'w'), indent=1)
        dire('j = %d g = %.6f %s k = %2d eta = %.4g : gamma = %.6e ; recouvrement %.6f (deuxieme %.2e) ; %.0f s' % (
            r['j'], r['g'], geom, k, eta, rec['gamma'], rec['recouvrement'], second, rec['duree_s']))
        del H, vals, vecs
dire('-- FIN diagnostic_TP_echelle_forte_machine2_v1 (%s) --' % geom)
