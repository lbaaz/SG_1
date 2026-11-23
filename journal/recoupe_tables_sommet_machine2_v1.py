# -*- coding: ascii -*-
"""Recoupe MA table (table_machine2_sommet_v1.json + detail_machine2_sommet_v1.json) avec celle de machine 1 (eligibilite_candidates_sommet_v1.json, 77ce2a6c7e867011 ; detail eligibilite_sommet_v1.json, 882f55d07d03dfff), APRES avoir fini la mienne.
Compare, cellule par cellule : liste des w2, TROIS NOMBRES ECRITS (g, eta0, r_c : chaines identiques), kappa, m_bord, eligibilite, e_bord, etendue, ln du plateau (G3), poids du site 0.
Ecrit la TABLE COMMUNE (section 5 : le ET ; un w2 est eligible si et seulement s'il l'est dans les deux tables ET si les trois nombres ecrits de ses sept cellules sont les memes dans les deux) : table_commune_sommet_machine2_v1.json, au format de la section 5.
Usage : py -3.11 -I recoupe_tables_sommet_machine2_v1.py <dossier de ma sortie> <table JSON de machine 1> <detail JSON de machine 1>"""
import json
import os
import sys
from fractions import Fraction as F

D, T1, DET1 = sys.argv[1], sys.argv[2], sys.argv[3]
t1 = json.load(open(T1))['creneaux']
t2 = json.load(open(os.path.join(D, 'table_machine2_sommet_v1.json')))['creneaux']
d1 = json.load(open(DET1))['creneaux']
det2 = json.load(open(os.path.join(D, 'detail_machine2_sommet_v1.json')))
mauv = []
pire = {'e_bord': 0.0, 'etendue': 0.0, 'ln_G3': 0.0, 'poids': 0.0}
n_cel = 0
commune = {'creneaux': {}}
for nom in ('MP', 'PP', 'MG', 'PG'):
    c1, c2, e1 = t1[nom]['candidats'], t2[nom]['candidats'], d1[nom]['candidats']
    if [x['w2'] for x in c1] != [x['w2'] for x in c2]:
        mauv.append('%s : listes de w2 differentes' % nom)
    cand = []
    for a, b, e in zip(c1, c2, e1):
        if not (a['w2'] == b['w2'] == e['w2']):
            mauv.append('%s : w2 differents %s %s %s' % (nom, a['w2'], b['w2'], e['w2']))
        k = round((F(b['w2']) - 2) * 100000)
        r2 = det2['%s|%d' % (nom, abs(k))]
        cel = []
        memes = True
        for ca, cb, ce, cd in zip(a['cellules'], b['cellules'], e['cellules'], r2['cellules']):
            n_cel += 1
            if ca['kappa'] != cb['kappa']:
                mauv.append('%s %s : kappa %s / %s' % (nom, b['w2'], ca['kappa'], cb['kappa']))
            for cle in ('g', 'eta0', 'r_c'):
                if ca[cle] != cb[cle]:
                    mauv.append('%s %s kappa %s : NOMBRE ECRIT %s differe : m1 %s, moi %s' % (nom, b['w2'], cb['kappa'], cle, ca[cle], cb[cle]))
                    memes = False
            if ce['m_bord'] != cd['m_bord']:
                mauv.append('%s %s kappa %s : m_bord m1 %s, moi %s' % (nom, b['w2'], cb['kappa'], ce['m_bord'], cd['m_bord']))
            if ca['eligible'] != cb['eligible']:
                mauv.append('%s %s kappa %s : eligibilite m1 %s, moi %s' % (nom, b['w2'], cb['kappa'], ca['eligible'], cb['eligible']))
            pire['e_bord'] = max(pire['e_bord'], abs(ce['e_bord'] - cd['e_bord']))
            pire['etendue'] = max(pire['etendue'], abs(ce['etendue'] - cd['etendue']))
            pire['ln_G3'] = max(pire['ln_G3'], abs(ce['ln_G3'] - cd['ln_plateau']))
            pire['poids'] = max(pire['poids'], abs(ce['poids_min'] - cd['poids_site0_min']))
            cel.append({'kappa': cb['kappa'], 'g': cb['g'], 'eta0': cb['eta0'], 'r_c': cb['r_c'], 'eligible': bool(ca['eligible'] and cb['eligible'] and ca['g'] == cb['g'] and ca['eta0'] == cb['eta0'] and ca['r_c'] == cb['r_c'])})
        elig = bool(a['eligible'] and b['eligible'] and memes and all(c['eligible'] for c in cel))
        cand.append({'w2': b['w2'], 'eligible': elig, 'cellules': cel})
    commune['creneaux'][nom] = {'candidats': cand}
json.dump(commune, open(os.path.join(D, 'table_commune_sommet_machine2_v1.json'), 'w'), indent=1, sort_keys=True)
print('cellules comparees :', n_cel)
print('DESACCORDS (trois nombres ecrits, kappa, m_bord, eligibilite, w2) :', len(mauv))
for m in mauv[:30]:
    print('  -', m)
print('plus grands ecarts entre ses nombres et les miens : e_bord %.2e ; etendue %.2e ; ln du plateau G3 %.2e ; poids du site 0 %.2e' % (pire['e_bord'], pire['etendue'], pire['ln_G3'], pire['poids']))
for nom in ('MP', 'PP', 'MG', 'PG'):
    cs = commune['creneaux'][nom]['candidats']
    print('table commune %s : %d w2 eligibles sur %d' % (nom, sum(1 for c in cs if c['eligible']), len(cs)))
print('TABLE COMMUNE : %d w2 eligibles sur 80 ; cellules eligibles %d sur 560' % (sum(1 for n in commune['creneaux'] for c in commune['creneaux'][n]['candidats'] if c['eligible']), sum(1 for n in commune['creneaux'] for c in commune['creneaux'][n]['candidats'] for x in c['cellules'] if x['eligible'])))
