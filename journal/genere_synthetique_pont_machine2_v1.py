# -*- coding: ascii -*-
"""SORTIES SYNTHETIQUES DES SONDES pour eprouver les feuilles du gel "pont" (seconde partie), les miennes et celles de machine 1, sur les SIX cellules tirees. Machine 2, 2026-11-17.
Ce ne sont PAS des 2D : ce sont des fichiers au format des sorties des sondes, fabriques a partir d'un tirage aleatoire a graine fixee et de la chaine (rho_3(x) de ma chaine), avec des regimes
choisis pour que chaque seuil des enonces (7) soit franchi dans un sens ou dans l'autre : residu du lisse, ecart entre absorbeurs, plateau a 1.05, parts non fiables a 5 pour cent,
boites sans compte valide, somme S, compte reduit, rapport des comptes. Aucune 2D reelle n'est calculee ; aucun nombre d'ici ne dit quoi que ce soit des cellules.
Usage : py -3.11 -P genere_synthetique_pont_machine2_v1.py <graine> <dossier neuf> <registre> <chaine du lot (json de machine 1)>"""
import json
import math
import os
import sys
from fractions import Fraction as F
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chaine_pont_machine2_v1 as C

SEED, DST, REG, CHAINE_M1 = int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4]
os.makedirs(DST, exist_ok=False)
rng = np.random.default_rng(SEED)
CH1 = json.load(open(CHAINE_M1))
X = CH1['ecarts']
ch = C.Chaine(REG)
CELL = {'MG3': ('397/200', 3, '3.63872e-03'), 'MG4': ('397/200', 4, '2.77765e-03'), 'MG5': ('397/200', 5, '2.20823e-03'),
        'PG3': ('2019/1000', 3, '5.23478e-03'), 'PG4': ('2019/1000', 4, '3.99601e-03'), 'PG5': ('2019/1000', 5, '3.17683e-03')}
REGIME = dict(seed=SEED, cellules={})
for nom, (w2, m, g) in CELL.items():
    cel = ch.cellule(w2, m, g)
    c1 = CH1['cellules'][nom]
    delta = cel.delta; AD = abs(delta)
    ln_rho3 = [cel.lisse(x, 3) for x in X]; pas = [cel.lisse(x, 2) - cel.lisse(x, 3) for x in X]
    # regime de la cellule
    a0, b0, p0 = rng.uniform(-0.03, 0.03), rng.uniform(-0.09, 0.09), rng.choice([1.0, 2.0, 3.0])
    sig_abs = rng.choice([0.001, 0.003, 0.006, 0.012])
    amp_barreau = rng.choice([0.004, 0.012, 0.025, 0.05])
    p_nonsuivi = rng.choice([0.0, 0.0, 0.03, 0.1])
    S0 = rng.uniform(0.80, 1.22); dS_groupe = rng.uniform(-0.12, 0.12)
    red0 = rng.uniform(0.31, 0.58); rap0 = rng.uniform(1.15, 1.95)
    p_nonfiable = rng.choice([0.0, 0.01, 0.03, 0.08]); p_invalide = rng.choice([0.0, 0.0, 0.03, 0.15])
    REGIME['cellules'][nom] = dict(a0=a0, b0=b0, p0=p0, sig_abs=sig_abs, amp_barreau=amp_barreau, p_nonsuivi=p_nonsuivi, S0=S0, dS_groupe=dS_groupe, red0=red0, rap0=rap0, p_nonfiable=p_nonfiable, p_invalide=p_invalide)
    w0_dens = 0.9990 + 0.0008 * rng.random()
    offs = rng.normal(0.0, sig_abs, 4)
    for ia, ab in enumerate('ABCD'):
        out = dict(N=108, X=X, absorbeur=ab, bord=c1['r_c'], couches=80, delta=delta, eta0=AD, forme='F2', g=g, m=m, r_c=c1['r_c'], w2=w2)
        ks = {}
        for k in range(-3, 9):
            suivi = bool(rng.random() >= p_nonsuivi)
            if not suivi:
                ks[str(k)] = dict(suivi=False)
                continue
            rho = []
            for i, x in enumerate(X):
                vrai = a0 + b0 * (x / 8.0) ** p0                                 # ln R3 vrai du lisse
                ln_rho = vrai + math.log(w0_dens) + ln_rho3[i] + offs[ia] * (1.0 + 0.1 * x)
                f = amp_barreau * (math.cos(0.9 * (k - 1.5)) * 0.5 + 0.15 * (k - 2.5) ** 2 / 10.0)      # forme de barreau : creux autour de k ~ 2-4
                rho.append(math.exp(ln_rho + f + 0.0 * rng.normal()))
            ks[str(k)] = dict(E_vide=-5e-6, eta=AD * 2.0 ** (-k), gamma_vide=1.5e-12 * (1.0 + 0.002 * rng.normal()), rho_direct=rho, rho_flux=rho, suivi=True, w0=w0_dens + 1e-6 * rng.normal())
        out['k'] = ks
        json.dump(out, open(os.path.join(DST, 'densite_%s_%s.json' % (nom, ab)), 'w'), sort_keys=True)
    # boites : vingt cotes
    lignes = []
    for cote in list(range(180, 190)) + list(range(291, 301)):
        groupe = 'UN' if cote < 200 else 'DEUX'
        n_att = red0 * cote * 7.95 * AD * (1.0 if groupe == 'UN' else rap0 * 184.5 / 295.5)
        n = int(max(2, round(n_att + rng.normal(0, 0.12 * n_att ** 0.5 + 0.3))))
        xs = np.sort(rng.uniform(0.051, 7.99, n))
        Sb = S0 + (dS_groupe if groupe == 'DEUX' else 0.0) + rng.normal(0, 0.05)
        parts = rng.chisquare(1, n) + 1e-3; parts = parts / parts.sum() * Sb * 7.95
        w0 = 0.999 + 0.0005 * rng.random()
        niv = []
        for x, y in zip(xs, parts):
            rho3 = math.exp(cel.lisse(float(x), 3))
            c2a = float(y * w0 * rho3 * AD)
            eps = 0.0 if rng.random() >= p_nonfiable else rng.choice([-1, 1]) * rng.uniform(0.021, 0.2)
            niv.append(dict(x=float(x), E=float(-delta * x * 0 - 1e-3 * x), c2_a=c2a, c2_b=c2a * (1.0 + eps), c2_a_large=c2a, brut_a=c2a, brut_b=c2a, fiable=bool(abs(eps) <= 0.02 * 1.0)))
        invalide = rng.random() < p_invalide
        mode = rng.integers(4) if invalide else -1
        lignes.append(dict(cote=cote, w2=w2, m=m, g=g, delta=delta, r_c=c1['r_c'], E_vide=-5e-6, w0=(0.4 if mode == 0 else w0), residu_vide=float(1e-8 if mode == 1 else 1e-14), iterations_vide=3, k_a=48, k_b=48,
                           couverte_a=bool(mode != 2), couverte_b=True, listes_identiques=bool(mode != 3), n=len(niv), n_b=len(niv), fiables=sum(v['fiable'] for v in niv), niveaux=niv, secondes=1.0))
    with open(os.path.join(DST, 'boites_%s.jsonl' % nom), 'w') as f:
        for l in lignes:
            f.write(json.dumps(l, sort_keys=True) + '\n')
json.dump(REGIME, open(os.path.join(DST, 'regime.json'), 'w'), indent=1, sort_keys=True)
print('scenario %d ecrit' % SEED)
