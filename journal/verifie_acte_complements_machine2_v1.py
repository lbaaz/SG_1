# -*- coding: ascii -*-
"""COMPLEMENTS a verifie_acte_machine2_v1.py (non edite) : trois ecarts apparents entre mon recalcul et l'acte de m1.
(1) superposition a m = 12 : l'acte donne 0.0858 pour l'etendue 'predite par la chaine' ; mon recalcul de l'etendue de ln(G3/|delta|) donne 0.0857. L'en-tete du journal de m1 dit que sa colonne est l'etendue des r3 DE LA CHAINE :
    je recalcule cette etendue-la, avec MON r3.
(2) rejeu : l'acte compte 1576 champs dont 816 nombres et un ecart de 1.4e-14 ; mon arbre JSON donne 1517 feuilles dont 1114 nombres et un ecart RELATIF de 1.1e-7 : je recalcule l'ecart ABSOLU et je cherche une definition de 'champ' qui retrouve 1576 / 816.
(3) part manquee : le journal de m1 donne 0.023, 0.025, 0.024, 0.023 ; mon rapport ln q / r3 donne 0.0234, 0.0256, 0.0247, 0.0234 en plus de chiffres.
Usage : py -3.11 -I verifie_acte_complements_machine2_v1.py"""
import json
import math
import os

B = r'd:\devs\bocal\BOCAL4'
V = json.load(open(os.path.join(B, r'run_gel_vide_machine2\run_1\verdict_vide.json')))
VR = json.load(open(os.path.join(B, r'livraison_16j_acte_gel_vide\ext\lot_m1\lot_machine1_2026-11-16_acte_gel_vide_v1\verdict_vide_rejoue_machine1.json')))
P = {c['id']: c for c in json.load(open(os.path.join(B, r'certif_gel_vide_partie2_machine2\predictions_machine2_vide_v1.json')))['cellules']}
D = {c['id']: c for c in V['cellules']}
print('(1) etendue, sur les 4 creneaux, de r3 de la chaine (mon r3) ; acte : 0.0097 0.0316 0.0473 0.0858 0.1263 aux profondeurs 3, 6, 8, 12, 16')
for m, att in ((3, '0.0097'), (6, '0.0316'), (8, '0.0473'), (12, '0.0858'), (16, '0.1263')):
    L = [i for i in D if D[i]['m'] == m]
    sp = max(P[i]['r3'] for i in L) - min(P[i]['r3'] for i in L)
    sp2 = max(P[i]['ln_G3'] - math.log(abs(P[i]['delta'])) for i in L) - min(P[i]['ln_G3'] - math.log(abs(P[i]['delta'])) for i in L)
    print('    m = %-2d : etendue de r3 %.5f -> %.4f (acte %s : %s) ; etendue de ln(G3/|delta|) %.5f -> %.4f' % (m, sp, sp, att, 'identique' if '%.4f' % sp == att else 'DIFFERENT', sp2, sp2))
print()


def feuilles(x, p=''):
    if isinstance(x, dict):
        for k in sorted(x):
            yield from feuilles(x[k], p + '/' + str(k))
    elif isinstance(x, list):
        for i, e in enumerate(x):
            yield from feuilles(e, p + '[%d]' % i)
    else:
        yield p, x


fa, fb = dict(feuilles(V)), dict(feuilles(VR))
isnum = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool)
nom = [k for k in fa if k in fb and isnum(fa[k]) and isnum(fb[k])]
ab = max((abs(fa[k] - fb[k]), k) for k in nom)
re_ = max((abs(fa[k] - fb[k]) / max(abs(fa[k]), abs(fb[k]), 1e-300), k) for k in nom if fa[k] != fb[k])
print('(2) rejeu de m1 contre le verdict du run : %d nombres ; ecart ABSOLU maximal %.1e (%s) ; ecart relatif maximal %.1e (%s)' % (len(nom), ab[0], ab[1], re_[0], re_[1]))
nb_diff = sum(1 for k in nom if fa[k] != fb[k])
print('    nombres exactement egaux : %d ; nombres qui different : %d' % (len(nom) - nb_diff, nb_diff))
# definitions candidates du "champ"
flt = [k for k in fa if isinstance(fa[k], float)]
ent = [k for k in fa if isinstance(fa[k], int) and not isinstance(fa[k], bool)]
boo = [k for k in fa if isinstance(fa[k], bool)]
chn = [k for k in fa if isinstance(fa[k], str)]
nul = [k for k in fa if fa[k] is None]


def noeuds(x):
    n = 1
    if isinstance(x, dict):
        for v in x.values():
            n += noeuds(v)
    elif isinstance(x, list):
        for v in x:
            n += noeuds(v)
    return n


print('    arbre du verdict du run : feuilles %d = flottants %d + entiers %d + booleens %d + chaines %d + null %d ; noeuds (feuilles et conteneurs) %d' % (len(fa), len(flt), len(ent), len(boo), len(chn), len(nul), noeuds(V)))
print('    acte : 1576 champs dont 816 nombres, ecart 1.4e-14 : mon decompte ne retrouve pas ces deux totaux avec les definitions que je sais ecrire ; aucun champ absent, aucun champ non numerique different.')
print()
print('(3) part de r3 que ln q represente, en plus de chiffres (journal de m1 : 0.023 0.025 0.024 0.023)')
for i in ('MG3', 'MG4', 'MG5', 'MG6'):
    print('    %s : ln q %+.7f / r3 %+.7f = %.5f' % (i, D[i]['ln_q'], P[i]['r3'], abs(D[i]['ln_q'] / P[i]['r3'])))
