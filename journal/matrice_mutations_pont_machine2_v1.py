# -*- coding: ascii -*-
"""MATRICE DE MUTATIONS de ma chaine d'eligibilite du gel "pont" (machine 2, 2026-11-17). Pour chaque mutation (une faute introduite dans MON code par eligibilite_pont_machine2_v1.py --mutation NOM),
on rejoue la chaine et on la CONFRONTE a la reference : (1) l'eligibilite par w2 ; (2) les couplages ecrits g ; (3) les 144 nombres de la section 7 du gel (etendue au vide, plus grande etendue du lisse,
plus grand pas, par cellule, a 4 decimales). Une mutation est MORDUE si l'un des trois change. Une mutation non mordue est dite : la confrontation ne distingue pas cette faute sur ces 48 cellules (le plus
souvent parce que la condition ne lie aucune cellule : voir la marge). Les premiers passages sont gardes. Usage : py -3.11 -P matrice_mutations_pont_machine2_v1.py <registre> <gel.md> <dossier de sortie>"""
import json
import os
import re
import subprocess
import sys
from fractions import Fraction as F

REG, GEL, SORTIE = sys.argv[1], sys.argv[2], sys.argv[3]
ICI = os.path.dirname(os.path.abspath(__file__)); SCRIPT = os.path.join(ICI, 'eligibilite_pont_machine2_v1.py')
os.makedirs(SORTIE, exist_ok=True)
texte = open(GEL, encoding='utf-8').read()
lignes = re.findall(r'^\s{2}(\d\.\d{3})\s+m3 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)\s+m4 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)\s+m5 (\d\.\d{4}) (\d\.\d{4}) (\d\.\d{4})(!?)', texte, re.M)
SA = {}
for l in lignes:
    cle = str(F(int(round(float(l[0]) * 1000)), 1000))
    for m, k in ((3, 1), (4, 5), (5, 9)):
        SA[(cle, m)] = (float(l[k]), float(l[k + 1]), float(l[k + 2]))
BASE_T = json.load(open(os.path.join(ICI, 'table_eligibilite_pont_machine2_v1.json')))
BASE_D = {(d['w2'], d['m']): d for d in json.load(open(os.path.join(ICI, 'details_eligibilite_pont_machine2_v1.json')))}


def elig(t):
    return {(s, c['w2']): c['eligible'] for s, d in t['creneaux'].items() for c in d['candidats']}


def gs(t):
    return {(s, c['w2'], ce['m']): ce['g'] for s, d in t['creneaux'].items() for c in d['candidats'] for ce in c['cellules']}


MUTATIONS = [
    ('seuil_pas_15', "seuil (v) 0.10 -> 0.15"),
    ('sans_condition_v', "condition (v) supprimee"),
    ('seuil_lisse_04', "seuil (iv) 0.03 -> 0.04"),
    ('sans_condition_iv', "condition (iv) supprimee"),
    ('seuil_vide_03', "seuil (iii) 0.02 -> 0.03"),
    ('seuil_ebord_08', "seuil (ii) 0.7 -> 0.8"),
    ('ebord_inclus', "(ii) e_bord < 0.7 -> <= 0.7"),
    ('sans_condition_i', "condition (i) m_bord = m supprimee"),
    ('g_cinq_chiffres', "couplage arrondi a cinq chiffres (%.4e)"),
    ('kappa_permutes', "kappa_3 et kappa_5 permutes"),
    ('cote_oppose_inverse', "E = E_v + x delta (du cote du desaccord)"),
    ('ordre_2_pour_3', "rho_3 calcule avec la matrice d'ordre 2"),
    ('lisse_moyenne', "lisse = moyenne des 18 ln rho au lieu de la mediane"),
    ('ecarts_sans_8', "ecart x = 8 retire (11 ecarts)"),
    ('ecarts_sans_005', "ecart x = 0.05 retire (11 ecarts)"),
    ('gamma_double', "Gamma = -2 Im(E) en double precision (au lieu de la precision etendue)"),
    ('plus_grande_partie_reelle', "a poids egal, la PLUS GRANDE partie reelle (au lieu de la plus petite)"),
    ('e_bord_sans_sigma', "e_bord sans les termes Sigma2"),
]
print('%-28s %-62s %-9s eligibilite : w2 changes   couplages g changes   nombres changes (sur 144)' % ('mutation', 'faute', 'verdict'))
for nom, desc in MUTATIONS:
    t = os.path.join(SORTIE, 'table_%s.json' % nom); d = os.path.join(SORTIE, 'details_%s.json' % nom)
    r = subprocess.run([sys.executable, '-P', '-W', 'ignore', SCRIPT, REG, t, d, '--mutation', nom], capture_output=True, text=True)
    open(os.path.join(SORTIE, 'sortie_%s.log' % nom), 'w', encoding='ascii', errors='replace').write(r.stdout + r.stderr[-2000:])
    if r.returncode != 0:
        print('%-28s %-62s ECHEC (code %d) : %s' % (nom, desc, r.returncode, r.stderr.strip().splitlines()[-1][:120] if r.stderr.strip() else '')); continue
    T = json.load(open(t)); D = {(x['w2'], x['m']): x for x in json.load(open(d))}
    e0, e1 = elig(BASE_T), elig(T); flips = sorted(k for k in e0 if e0[k] != e1.get(k))
    g0, g1 = gs(BASE_T), gs(T); gch = sum(1 for k in g0 if g0[k] != g1.get(k))
    nch = 0
    for k, v in SA.items():
        x = D.get(k)
        if x is None or 'etendue_vide' not in x:
            nch += 3; continue
        mo = (x['etendue_vide'], x['etendue_lisse_max'], x['pas_max'])
        nch += sum(1 for a, b in zip(mo, v) if not (abs(round(a, 4) - b) < 5e-5))
    mord = bool(flips or gch or nch)
    print('%-28s %-62s %-9s %-26s %-22d %d' % (nom, desc, 'MORDUE' if mord else 'non mordue', ('%d (%s)' % (len(flips), ' '.join('%s:%s' % (k[0], k[1]) for k in flips))) if flips else '0', gch, nch), flush=True)
