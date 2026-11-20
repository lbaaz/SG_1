# -*- coding: ascii -*-
"""Confronte mes sorties des sondes de machine 1 au point sacrifie (w2 = 101/50), rejouees sur BOCAL4, aux sorties de son lot. Machine 2, 2026-11-17.
Usage : py -3.11 -P compare_sondes_sacrifie_machine2_v1.py boite <mon.jsonl> <son.jsonl> <cote>
        py -3.11 -P compare_sondes_sacrifie_machine2_v1.py densite <mon.json> <son.json>
Rien n'est juge : on rend les plus grands ecarts, relatifs ou absolus, et les memes comptes."""
import json
import math
import sys


def boite(mon, son, cote):
    def charge(p):
        out = {}
        for l in open(p):
            if l.strip():
                b = json.loads(l)
                out[b['cote']] = b
        return out
    A, B = charge(mon), charge(son)
    a, b = A[cote], B[cote]
    print('cote %d : n %d / %d ; fiables %d / %d ; listes identiques %s / %s ; couverte a/b %s %s / %s %s' % (
        cote, a['n'], b['n'], a['fiables'], b['fiables'], a['listes_identiques'], b['listes_identiques'], a['couverte_a'], a['couverte_b'], b['couverte_a'], b['couverte_b']))
    print('E_vide : %.15e / %.15e (ecart %.2e) ; w0 : %.12f / %.12f (ecart %.2e) ; residu_vide %.2e / %.2e' % (
        a['E_vide'], b['E_vide'], abs(a['E_vide'] - b['E_vide']), a['w0'], b['w0'], abs(a['w0'] - b['w0']), a['residu_vide'], b['residu_vide']))
    if a['n'] != b['n']:
        print('COMPTES DIFFERENTS')
        return
    dE = dx = dca = dcb = dcal = dbr = 0.0
    for u, v in zip(a['niveaux'], b['niveaux']):
        dE = max(dE, abs(u['E'] - v['E'])); dx = max(dx, abs(u['x'] - v['x']))
        dca = max(dca, abs(u['c2_a'] / v['c2_a'] - 1)); dcb = max(dcb, abs(u['c2_b'] / v['c2_b'] - 1))
        dcal = max(dcal, abs(u['c2_a_large'] / v['c2_a_large'] - 1)); dbr = max(dbr, abs(u['brut_a'] / v['brut_a'] - 1))
    print('niveaux appaires : plus grand ecart sur E %.2e, sur x %.2e ; relatif sur c2_a %.2e, c2_b %.2e, c2_a_large %.2e, brut_a %.2e' % (dE, dx, dca, dcb, dcal, dbr))
    print('flags fiable identiques : %s' % all(u['fiable'] == v['fiable'] for u, v in zip(a['niveaux'], b['niveaux'])))


def densite(mon, son):
    a, b = json.load(open(mon)), json.load(open(son))
    for k in sorted(a['k'], key=int):
        u, v = a['k'][k], b['k'][k]
        if not (u.get('suivi') and v.get('suivi')):
            print('k = %s : suivi %s / %s' % (k, u.get('suivi'), v.get('suivi')))
            continue
        d = max(abs(math.log(x / y)) for x, y in zip(u['rho_flux'], v['rho_flux']))
        dd = max(abs(math.log(x / y)) for x, y in zip(u['rho_direct'], v['rho_direct']))
        print('k = %2s : E_vide %.12e / %.12e (ecart %.1e) ; w0 ecart %.1e ; gamma %.4e / %.4e ; plus grand |ln(rho_flux ma/sa)| %.2e (direct %.2e)' % (
            k, u['E_vide'], v['E_vide'], abs(u['E_vide'] - v['E_vide']), abs(u['w0'] - v['w0']), u['gamma_vide'], v['gamma_vide'], d, dd))


if sys.argv[1] == 'boite':
    boite(sys.argv[2], sys.argv[3], int(sys.argv[4]))
else:
    densite(sys.argv[2], sys.argv[3])
