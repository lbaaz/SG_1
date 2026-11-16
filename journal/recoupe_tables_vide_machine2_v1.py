# -*- coding: ascii -*-
"""Recoupe MA table (table_machine2_vide_v1.json + detail) avec celle de m1 (eligibilite_candidates_vide_v1.json), APRES avoir fini la mienne.
Compare, cellule par cellule : couplage ecrit (chaine exacte), m_bord, eligibilite, e_bord, etendue, ln du plateau de Gamma.
Ecrit la TABLE COMMUNE (section 5 : le ET ; un w2 est eligible ssi il l'est dans les deux ET si les couplages ecrits de ses sept cellules sont les
memes ; une cellule profonde est retenue ssi elle l'est dans les deux) : table_commune_vide_machine2_v1.json.
Usage : py -3.11 -I recoupe_tables_vide_machine2_v1.py"""
import json
import math

BASE = r'd:\devs\bocal\BOCAL4'
M1 = BASE + r'\livraison_16f_gel_vide_partie1\ext\x_gel_vide_partie1_regle_tirage\lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1\eligibilite_candidates_vide_v1.json'
D = BASE + r'\certif_gel_vide_partie1_machine2'
t1 = json.load(open(M1))['creneaux']
t2 = json.load(open(D + r'\table_machine2_vide_v1.json'))['creneaux']
det = json.load(open(D + r'\detail_machine2_vide_v1.json'))
mauv = []
pire = {'e_bord': 0.0, 'etendue': 0.0, 'ln_G3': 0.0}
n_cel = 0
commune = {'creneaux': {}}
for nom in ('MG', 'MP', 'PP', 'PG'):
    c1, c2 = t1[nom]['candidats'], t2[nom]['candidats']
    if [x['w2'] for x in c1] != [x['w2'] for x in c2]:
        mauv.append('%s : listes de w2 differentes (%s vs %s)' % (nom, [x['w2'] for x in c1], [x['w2'] for x in c2]))
    cand = []
    for a, b in zip(c1, c2):
        d = det['%s|%d' % (nom, round(float(__import__('fractions').Fraction(b['w2'])) * 1000))]
        cel = []
        meme_g = True
        for ca, cb, cd in zip(a['cellules'], b['cellules'], d['cellules']):
            n_cel += 1
            if ca['m'] != cb['m']:
                mauv.append('%s %s : profondeurs differentes' % (nom, b['w2']))
            if ca['g'] != cb['g']:
                mauv.append('%s %s m=%d : COUPLAGE ECRIT differe : m1 %s, moi %s' % (nom, b['w2'], cb['m'], ca['g'], cb['g']))
                meme_g = False
            if ca['m_bord'] != cd['m_bord']:
                mauv.append('%s %s m=%d : m_bord m1 %s, moi %s' % (nom, b['w2'], cb['m'], ca['m_bord'], cd['m_bord']))
            if ca['eligible'] != cb['eligible']:
                mauv.append('%s %s m=%d : eligibilite m1 %s, moi %s' % (nom, b['w2'], cb['m'], ca['eligible'], cb['eligible']))
            pire['e_bord'] = max(pire['e_bord'], abs(ca['e_bord'] - cd['e_bord']))
            pire['etendue'] = max(pire['etendue'], abs(ca['etendue'] - cd['etendue']))
            pire['ln_G3'] = max(pire['ln_G3'], abs(ca['ln_G3'] - cd['ln_plateau']))
            cel.append({'m': cb['m'], 'g': cb['g'], 'eligible': bool(ca['eligible'] and cb['eligible'] and ca['g'] == cb['g'])})
        lis = [c for c in cel if c['m'] in (3, 4, 5, 6)]
        elig = bool(a['eligible'] and b['eligible'] and meme_g and all(c['eligible'] for c in lis))
        cand.append({'w2': b['w2'], 'eligible': elig, 'cellules': cel})
    commune['creneaux'][nom] = {'candidats': cand}
json.dump(commune, open(D + r'\table_commune_vide_machine2_v1.json', 'w'), indent=1, sort_keys=True)
print('cellules comparees :', n_cel)
print('DESACCORDS (couplage, m_bord, eligibilite, w2) :', len(mauv))
for m in mauv[:20]:
    print('  -', m)
print('plus grands ecarts : e_bord %.2e ; etendue %.2e ; ln du plateau de Gamma %.2e' % (pire['e_bord'], pire['etendue'], pire['ln_G3']))
for nom in ('MG', 'MP', 'PP', 'PG'):
    cs = commune['creneaux'][nom]['candidats']
    print('table commune %s : %d w2 eligibles sur %d ; cellules profondes retenues %d sur %d' % (
        nom, sum(1 for c in cs if c['eligible']), len(cs), sum(1 for c in cs for x in c['cellules'] if x['m'] in (8, 12, 16) and x['eligible']), 3 * len(cs)))
