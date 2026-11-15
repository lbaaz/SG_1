# -*- coding: ascii -*-
"""Le VERDICT, les issues de bande, la comparaison au pire etat et les energies du run du gel 41153158190cf7f1 tiennent-ils sous le bruit des fils BLAS ?
Meme methode que stabilite_cascade_machine2_v1.py du gel precedent (domaine_G1/), adaptee a la cascade par bandes de ce gel :
 - le bruit de la cible est 7.32e-14 en absolu sur Gamma_2D(3) (mesure au run precedent, ecart maximal vu entre 16 et 4 fils, aux deux ancres, N = 60 et 61 ;
   ce gel : l'ecart entre mon essai a 1 fil et celui de machine 1, 1.72e-13 sur tous les etats, 4.0e-14 aux etats de Gamma_2D(3) > 1.33e-12 -- controles C10c) ;
   le bruit de la chaine du moteur et de la chaine d'ordre 2 (Gamma_flux) est pris nul (identique a tous les fils : memes tables, meme solveur sur de petites matrices) ;
 - un etat dont Gamma_2D(3) est a moins du bruit du plancher des dix planchers (1.33e-12) peut entrer ou sortir des etats juges (les autres criteres lus comme la feuille) ;
 - un etat juge dont la position dans la borne de sa bande (avec la marge d'un plancher) change quand Gamma_2D(3) varie de plus ou moins le bruit peut etre DANS ou HORS
   la borne : on lui donne les deux options ;
 - pour chaque point, tous les cas sont enumeres : classes possibles (TENU, TOMBE, NON LISIBLE) ; puis, sur le produit des classes possibles des douze points juges, les
   verdicts possibles, les issues de bande possibles.
Ne juge rien, ne relit rien : un controle de robustesse de la lecture de la feuille. DERIVE de la v1 (scellee, canon dans le lot 59a583a640112891) apres le run : un seul changement, un etat dont Gamma_2D(3) est <= 0 sous tout le bruit (M3, -7.4e-14) n'est pas juge ;
la v1 lui laissait zero option et vidait les classes du point. Usage (depuis BOCAL4) : python -P ordre2/stabilite_cascade_machine2_v2.py <sonde.json> <verdict.json> [multiple du bruit]"""
import copy
import importlib.util
import itertools
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(sys.argv[1], encoding='ascii'))
V = json.load(open(sys.argv[2], encoding='ascii'))
sp = importlib.util.spec_from_file_location('feuille', os.path.join(HERE, 'lecture_ordre2_machine1_v1.py'))
F = importlib.util.module_from_spec(sp)
sp.loader.exec_module(F)
BRUIT = 7.32e-14 * (float(sys.argv[3]) if len(sys.argv) > 3 else 1.0)       # v2 : troisieme argument facultatif = multiple du bruit (defaut 1, le bruit mesure aux ancres)
PLANCHER_DIX = 1.33e-12
BORNE = {b[0]: b[1] for b in F.BANDES}


def etat_ok_a(e, g3x):
    """Les criteres de la feuille lus avec Gamma_2D(3) remplace par g3x (les trois barreaux de k suivent a rapport constant)."""
    e2 = copy.deepcopy(e)
    s = g3x / e['Gamma_2D']['3']
    e2['Gamma_2D'] = {k: v * s for k, v in e['Gamma_2D'].items()}
    return e2


poss, details = {}, {}
for p in S['points']:
    pid = p['id']
    if pid not in F.ATTENDUS or F.ATTENDUS[pid][0] != 'juge':
        continue
    borne = BORNE[F.ATTENDUS[pid][3]]
    fixes_dans, incert = [], []                     # chaque element : liste d'options pour 'cet etat est-il juge et dans la borne ?' : 'D' (dans), 'H' (hors), None (non juge)
    n_fixes_juges = 0
    for e in p['etats']:
        g3 = e['Gamma_2D']['3']
        m = F.motif_exclusion(e)
        opts = set()
        for g3x in (g3 - BRUIT, g3, g3 + BRUIT):
            if g3x <= 0:
                continue
            e2 = etat_ok_a(e, g3x)
            m2 = F.motif_exclusion(e2)
            if m2 is not None:
                opts.add(None)
                continue
            g2 = e['chaine2']['gammas_flux'][2]
            opts.add('D' if F.dans_borne(g2, g3x, borne) else 'H')
        if not opts:                                  # v2 : Gamma_2D(3) <= 0 sous tout le bruit : l'etat n'est jamais juge (v1 le laissait sans option)
            opts.add(None)
        if len(opts) == 1:
            o = next(iter(opts))
            if o is not None:
                fixes_dans.append(o)
        else:
            incert.append(sorted(opts, key=str))
    cl = set()
    for combo in itertools.product(*incert) if incert else [()]:
        etats = fixes_dans + [x for x in combo if x is not None]
        if len(etats) < F.MIN_JUGES:
            cl.add('NL')
        else:
            cl.add('TENU' if all(x == 'D' for x in etats) else 'TOMBE')
    poss[pid] = cl
    obs = [x for x in V['points'] if x['id'] == pid][0]
    o = {'TENU': 'TENU', 'TOMBE': 'TOMBE', 'NON LISIBLE': 'NL'}[obs['statut']]
    details[pid] = (o, sorted(cl), len(incert))
    print('%s bande %-9s statut %-5s ; possibles sous le bruit %-22s ; %d etat(s) incertain(s) -> %s' % (
        pid, F.ATTENDUS[pid][3], o, sorted(cl), len(incert), 'INCHANGE' if cl == {o} else 'PEUT CHANGER'))

JUG = [k for k in sorted(F.ATTENDUS) if F.ATTENDUS[k][0] == 'juge']
verdicts, issues = {}, {b: set() for b in ('proche', 'moyenne', 'lointaine')}
for choix in itertools.product(*[sorted(poss[k]) for k in JUG]):
    st = dict(zip(JUG, choix))
    bandes = {}
    for b in ('proche', 'moyenne', 'lointaine'):
        lis = [k for k in JUG if F.ATTENDUS[k][3] == b and st[k] != 'NL']
        bandes[b] = 'NL' if len(lis) < F.MIN_LISIBLES_BANDE else ('T' if all(st[k] == 'TENU' for k in lis) else 'N')
        issues[b].add(bandes[b])
    if bandes['proche'] == 'NL':
        v = 'NON LISIBLE'
    elif bandes['proche'] == 'N':
        v = "L'ORDRE 2 NE TIENT PAS"
    elif bandes['moyenne'] != 'T':
        v = "L'ORDRE 2 TIENT JUSQU'A 0.06"
    elif bandes['lointaine'] != 'T':
        v = "L'ORDRE 2 TIENT JUSQU'A 0.10"
    else:
        v = "L'ORDRE 2 TIENT"
    verdicts[v] = verdicts.get(v, 0) + 1
print()
print('verdicts possibles sous le bruit : %s (rendu : %s)' % (sorted(verdicts), V['verdict']))
print('issues de bande possibles : %s' % {b: sorted(x) for b, x in issues.items()})
print('VERDICT %s' % ('INCHANGE' if sorted(verdicts) == [V['verdict']] else 'PEUT CHANGER'))
