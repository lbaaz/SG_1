# -*- coding: ascii -*-
"""Le VERDICT, la RIVALE, les PAIRES, a et b du run du gel b59651f99e60707a tiennent-ils sous le bruit des fils BLAS mesure a la certification ?
Meme methode que stabilite_sous_bruit_machine2_v1.py (celle du run precedent), prolongee de l'etat au point, du point a la cascade :
 - le bruit de la cible est 7.32e-14 en absolu sur Gamma_2D(3) (ecart maximal vu entre 16 et 4 fils, aux deux ancres, N = 60 et 61 ; NON mesure aux boites
   de N = 72 et 74 : le gel interdit de rejouer un point) ; celui de la chaine est nul (identique a tous les fils, meme comparaison) ;
 - un etat dont q est a moins de son bruit relatif d'une borne du gel (1/2, 2, 0.3162, 3.1623) peut changer de palier : on lui donne ses trois valeurs
   possibles (q / (1 + b), q, q / (1 - b)) ;
 - un etat dont Gamma_2D(3) est a moins du bruit du plancher (1.33e-12) peut entrer ou sortir des etats juges (les autres criteres lus comme la feuille, a
   rapport constant) : on lui donne les deux options ;
 - pour chaque point, tous les cas sont enumeres : les classes possibles (TENU, TOMBE, aucune) et le nombre d'etats juges ; puis, sur le produit des
   classes possibles des douze points juges, les verdicts, les rivales et les etats des cinq paires possibles.
Ne juge rien, ne relit rien : un controle de robustesse de la lecture de la feuille. Usage (depuis BOCAL4) : python -P ce_script <sonde.json> <verdict.json>"""
import copy
import importlib.util
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(sys.argv[1], encoding='ascii'))
V = json.load(open(sys.argv[2], encoding='ascii'))
sp = importlib.util.spec_from_file_location('feuille', os.path.join(HERE, 'lecture_domaine_G1_machine1_v1.py'))
F = importlib.util.module_from_spec(sp)
sp.loader.exec_module(F)
BRUIT = 7.32e-14
PLANCHER = 1.33e-12
BORNES = (0.5, 2.0, 10 ** -0.5, 10 ** 0.5)
RANG = {'FACTEUR 2': 0, 'DECADE': 1, 'HORS DECADE': 2}


def classe_pire(qs):
    if len(qs) < 6:
        return None
    pire = max(F.palier(q) for q in qs) if qs else None
    return 'TOMBE' if pire == 'HORS DECADE' else 'TENU'


poss = {}
for p in S['points']:
    pid = p['id']
    if pid not in F.ATTENDUS or F.ATTENDUS[pid][0] != 'juge':
        continue
    sans_incert, incert = [], []
    for e in p['etats']:
        g3 = e['Gamma_2D']['3']
        m = F.motif_exclusion(e)
        e2 = copy.deepcopy(e)
        e2['Gamma_2D'] = {k: v * (1e-9 / g3) for k, v in e['Gamma_2D'].items()} if g3 > 0 else e['Gamma_2D']
        m2 = F.motif_exclusion(e2) if g3 > 0 else m
        q = e['chaine']['gammas'][2] / g3 if (g3 > 0 and not e['chaine'].get('erreur') and e['chaine'].get('gammas')) else None
        rb = BRUIT / g3 if g3 > 0 else 1.0
        near_floor = abs(g3 - PLANCHER) <= BRUIT
        if m is None:
            opts = ([q] if not near_floor else [q, None])
            if any(abs(q / b - 1) < rb for b in BORNES):
                opts = [q / (1 + rb), q, q / (1 - rb)] + ([None] if near_floor else [])
            (incert if len(opts) > 1 else sans_incert).append(opts if len(opts) > 1 else q)
        elif m == 'sous dix planchers' and m2 is None and near_floor and q is not None:
            incert.append([None, q, q / (1 + rb), q / (1 - rb)])          # peut entrer
        # sinon : exclu pour un autre motif, ou loin du plancher : fixe
    ensembles = set()
    for combo in itertools.product(*incert) if incert else [()]:
        qs = sans_incert + [x for x in combo if x is not None]
        ensembles.add((classe_pire(qs), len(qs) >= 6))
    classes = {c if c is not None else 'NL' for c, _ in ensembles}          # moins de 6 etats juges : NON LISIBLE
    poss[pid] = classes
    obs = [x for x in V['points'] if x['id'] == pid][0]
    print('%s %-5s classe %-5s ; possibles sous le bruit %-22s ; %d etat(s) incertain(s) -> %s' % (
        pid, p['role'], obs['classe'], sorted(poss[pid]), len(incert), 'INCHANGEE' if poss[pid] == {obs['classe']} else 'PEUT CHANGER'))

EN = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
HO = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6']
PAIRES = F.PAIRES
verdicts, rivales, paires = {}, {}, {k: set() for k in PAIRES}
ids = EN + HO
for choix in itertools.product(*[sorted(poss[k], key=str) for k in ids]):
    c = dict(zip(ids, [None if x == 'NL' else x for x in choix]))
    en_l = [k for k in EN if c[k] is not None]
    ho_l = [k for k in HO if c[k] is not None]
    a = sum(1 for k in en_l if c[k] == 'TOMBE')
    b = sum(1 for k in ho_l if c[k] == 'TENU')
    if len(en_l) < 4 or len(ho_l) < 4:
        v = 'NON LISIBLE'
    elif a == 0 and b == 0:
        v = 'LA GARDE SEPARE'
    elif a == 0:
        v = 'LA GARDE SUFFIT'
    else:
        v = 'LA GARDE NE TIENT PAS'
    pa = {}
    for nom, (x, y) in PAIRES.items():
        pa[nom] = 'NON LISIBLE' if (c[x] is None or c[y] is None) else ('HOMOGENE' if c[x] == c[y] else 'HETEROGENE')
        paires[nom].add(pa[nom])
    lis = [pa[k] for k in ('P1', 'P2', 'P3') if pa[k] != 'NON LISIBLE']
    riv = 'NON LISIBLE' if len(lis) < 2 else ('TENUE' if all(x == 'HOMOGENE' for x in lis) else 'NON TENUE')
    verdicts[v] = verdicts.get(v, 0) + 1
    rivales[riv] = rivales.get(riv, 0) + 1
print()
print('verdicts possibles sous le bruit : %s (rendu : %s)' % (sorted(verdicts), V['verdict']))
print('rivales possibles sous le bruit : %s (rendue : %s)' % (sorted(rivales), V['rivale']))
print('paires possibles : %s' % {k: sorted(v) for k, v in paires.items()})
print('VERDICT %s ; RIVALE %s' % ('INCHANGE' if sorted(verdicts) == [V['verdict']] else 'PEUT CHANGER', 'INCHANGEE' if sorted(rivales) == [V['rivale']] else 'PEUT CHANGER'))
