# -*- coding: ascii -*-
"""ANALYSE du diagnostic du temoin positif a barreaux plus forts -- machine 2, v1, 13/11/2026. HORS GEL, NON OPPOSABLE.
Recolle les barreaux k = -6 a -3 de diag_G20.json / diag_G30.json (etat de plus grand recouvrement avec le vide, SANS
suivi) aux valeurs de MA sonde de la nuit (sonde_etage1.json, k = -2 a 12, etat SUIVI), et applique, aux series ainsi
etendues, la regle de palier du gel (3.11) : fenetre de cinq valeurs lisibles a k consecutifs, max <= 21/20 min en
rationnels exacts ; plus longue suite de valeurs a 5 pour cent ; accord a la reference (table 4d51dd58ef456fe9).
k = -2 est calcule par les DEUX voies (diagnostic et sonde) : l'ecart est l'ancre. Un barreau dont le recouvrement avec le
vide est sous 0.90 est signale : la valeur lue n'est peut-etre plus celle du meme etat.
Usage : python -P analyse_diagnostic_TP_echelle_forte_machine2_v1.py"""
import json
import math
import os
from fractions import Fraction

ICI = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(ICI, 'diagnostic_TP_echelle_forte')
S1 = json.load(open(os.path.join(ICI, 'nuit_EB', 'sortie', 'sonde_etage1.json')))
REF = json.load(open(os.path.join(ICI, 'tp_reference_machine2_v1.json')))
TAB = {r['j']: r for r in REF['balayage']}
DIAG = {}
for g in ('G20', 'G30'):
    for r in json.load(open(os.path.join(SORTIE, 'diag_%s.json' % g))):
        DIAG[(r['j'], g, r['k'])] = r
LOG = open(os.path.join(SORTIE, 'analyse_diagnostic_TP_echelle_forte_machine2_v1.log'), 'w', encoding='ascii', newline='\n')


def dire(s=''):
    print(s)
    LOG.write(s + '\n')


PL = 1e-12


def lisible(x):
    return x is not None and x > PL


def sonde(cle, g, k):
    e = S1['TP'][cle]['traj']['F1' + g][str(k)]['etats'][0]
    return e['gamma'] if e['suivi'] else None


def plateau(ser, k_min):
    best = None
    for k0 in range(k_min, 9):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(not lisible(x) for x in v):
            continue
        mx, mn = Fraction(max(v)), Fraction(min(v))
        cand = (not (mx <= Fraction(21, 20) * mn), mx / mn, k0)
        if best is None or cand < best[0]:
            best = (cand, v)
    if best is None:
        return None
    (nok, rap, k0), v = best
    return {'ok': not nok, 'etalement': float(rap) - 1.0, 'k0': k0,
            'Gamma_pl': math.exp(sum(math.log(x) for x in v) / 5.0)}


def plus_longue(ser, k_min):
    best = None
    for k0 in range(k_min, 13):
        for n in range(1, 20):
            v = [ser.get(k) for k in range(k0, k0 + n)]
            if len(v) < n or any(not lisible(x) for x in v):
                break
            if Fraction(max(v)) <= Fraction(21, 20) * Fraction(min(v)):
                if best is None or n > best[0]:
                    best = (n, k0, max(v) / min(v) - 1.0)
            else:
                break
    return best


dire('ANALYSE du diagnostic du temoin positif a barreaux plus forts (hors gel, non opposable)')
resume = {}
for cle in ('j06', 'j08'):
    j = S1['TP'][cle]['j']
    gref = TAB[j]['Gamma_ref']
    for g in ('G20', 'G30'):
        dire()
        dire('== %s (j = %d, Gamma_ref %.4e) %s ==' % (cle, j, gref, g))
        ser_son = {k: sonde(cle, g, k) for k in range(-2, 13)}
        ser = dict(ser_son)
        lignes = []
        for k in (-6, -5, -4, -3, -2):
            d = DIAG.get((j, g, k))
            if d is None:
                lignes.append('   k = %2d : non calcule' % k)
                continue
            if k != -2:
                ser[k] = d['gamma']
            ec = ''
            if k == -2:
                ec = ' ; ANCRE : diagnostic / sonde - 1 = %+.2e' % (d['gamma'] / ser_son[-2] - 1.0)
            fiable = d['recouvrement'] >= 0.90
            lignes.append('   k = %2d : gamma %.4e  gamma/ref %.3f ; recouvrement %.4f (deuxieme %.1e)%s%s' % (
                k, d['gamma'], d['gamma'] / gref, d['recouvrement'], d['deuxieme_recouvrement'],
                '' if fiable else '  <-- SOUS 0.90 : etat peut-etre autre', ec))
        for l in lignes:
            dire(l)
        dire('   (k = -1 a 3 de la sonde, rappel) gamma/ref : ' + ' '.join(
            '%.3f' % (ser_son[k] / gref) for k in range(-1, 4)))
        kmin = min(k for k in ser if lisible(ser[k]))
        p_sonde = plateau(ser_son, -2)
        p_ext = plateau(ser, kmin)
        pl = plus_longue(ser, kmin)
        dire('   plateau, echelle du gel (k >= -2) : %s' % (
            'PLATEAU k0 = %d etalement %.4f' % (p_sonde['k0'], p_sonde['etalement']) if p_sonde and p_sonde['ok']
            else 'PAS DE PLATEAU, meilleur etalement %.4f (k0 = %d)' % (p_sonde['etalement'], p_sonde['k0'])))
        dire('   plateau, echelle ETENDUE (k >= %d) : %s' % (kmin, (
            'PLATEAU k0 = %d etalement %.4f Gamma_pl %.4e, |ln(Gamma_pl / ref)| = %.4f' % (
                p_ext['k0'], p_ext['etalement'], p_ext['Gamma_pl'], abs(math.log(p_ext['Gamma_pl'] / gref)))
            if p_ext and p_ext['ok'] else 'PAS DE PLATEAU, meilleur etalement %.4f (k0 = %d)' % (
                p_ext['etalement'], p_ext['k0']))))
        dire('   plus longue suite a 5 pour cent : %d valeurs, k = %d a %d, etalement %.4f' % (
            pl[0], pl[1], pl[1] + pl[0] - 1, pl[2]))
        resume[(cle, g)] = (p_sonde, p_ext, pl)
dire()
dire('RESUME')
for (cle, g), (ps, pe, pl) in resume.items():
    dire('  %s %s : gel %s ; etendue %s ; plus longue suite %d valeurs (k = %d a %d)' % (
        cle, g, 'PLATEAU' if ps['ok'] else 'PAS DE PLATEAU', 'PLATEAU' if pe['ok'] else 'PAS DE PLATEAU',
        pl[0], pl[1], pl[1] + pl[0] - 1))
dire('-- FIN analyse_diagnostic_TP_echelle_forte_machine2_v1 --')
LOG.close()
