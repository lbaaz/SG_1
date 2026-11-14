# -*- coding: ascii -*-
"""Controle par machine 2 des deux ancres du gel (G-4) et des affirmations de la section 5 du gel sur l'essai a blanc, sur trois JSON :
mon essai a 16 fils (par defaut), mon essai A1 a 4 fils, l'essai de machine 1. Usage depuis BOCAL4 :
python -P chaine_EA_par_etat/controle_ancres_machine2_v1.py > chaine_EA_par_etat/controle_ancres_machine2_v1.log"""
import json
REFS = {'A1': ((7, 2), 2.1623273017950654e-10), 'A2': ((8, 2), 2.6613925716641374e-09)}
for nom, f in (('m2, defaut (16 fils)', 'chaine_EA_par_etat/essai_ancres_machine2.json'), ('m2, 4 fils', 'chaine_EA_par_etat/essai_ancres_machine2_4fils.json'),
               ('m1, 1 fil, X86_V4', 'chaine_EA_par_etat/sonde_essai_ancres_machine1.json')):
    S = json.load(open(f, encoding='ascii'))
    print('== %s : fils %s, coeurs %s, levier %s' % (nom, S['plateforme']['fils'], S['plateforme']['coeurs'], S['plateforme']['levier']))
    for p in S['points']:
        (n1, n2), ref = REFS[p['id']]
        tr = [e for e in p['etats'] if (e['n1'], e['n2']) == (n1, n2)]
        e = tr[0]
        print('  %s etat (%d,%d) vu %d fois, rang %d : Gamma_2D(3) %.12e ; lecture du run de M17 %.12e ; ecart relatif %.3e' % (
            p['id'], n1, n2, len(tr), e['rang'], e['Gamma_2D']['3'], ref, abs(e['Gamma_2D']['3'] / ref - 1)))
        suiv = min(min(x['suivi']['2'], x['suivi']['4']) for x in p['etats'])
        stab = max(max(x['Gamma_2D'].values()) / min(x['Gamma_2D'].values()) for x in p['etats'] if x['Gamma_2D']['3'] > 1.33e-12)
        etal = [max(x['chaine']['gammas']) / min(x['chaine']['gammas']) for x in p['etats'] if x['chaine']['gammas'] and x['Gamma_2D']['3'] > 1.33e-12]
        vides = [(x['n1'], x['n2']) for x in p['etats'] if x['chaine']['vide']]
        print('     suivi min %.6f ; stabilite de la cible max (etats au-dessus de dix planchers) %.3f ; etalement de la chaine max %.3f ; barrieres vides %s ; '
              'sigma_J max %.3f ; poids sur le site min %.3f' % (suiv, stab, max(etal), vides, max(x['J_ecart_type'] for x in p['etats']), min(x['poids_site'] for x in p['etats'])))
        e0 = p['etats'][0]
        print('     etat lu (rang 0) : <n2> - n2 = %+.4f, <n1> - n1 = %+.4f (rapport %.3f), poids sur le site %.3f' % (
            e0['n2_moyen'] - e0['n2'], e0['n1_moyen'] - e0['n1'], (e0['n1_moyen'] - e0['n1']) / (e0['n2_moyen'] - e0['n2']), e0['poids_site']))
