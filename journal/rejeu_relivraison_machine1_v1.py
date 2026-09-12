#!/usr/bin/env python3
# -*- coding: ascii -*-
"""REJEU DU FOND RE-LIVRE -- machine 1, v1, 12/09/2026 (nuit).

Le lot de re-livraison (canon d0ab94382e1b5808, 158 pieces, arbre du poste machine 2 preserve)
est deplie tel quel, sans edition (PB-1). Ce driver, chemin de la racine en argument :
  1. authentifie par CANON (convention B) chaque feuille avant de la jouer, et chaque log
     de machine 2 avant de le comparer ;
  2. rejoue derivation v3 et relecture v1 dans leur repertoire (les feuilles resolvent leurs
     entrees par __file__), et R-G2-5 v2 sur le repertoire de la chaine (banc v8 certifie) ;
  3. compare chaque rejeu au log de machine 2, CRLF normalise en LF, et NOMME les lignes qui
     different -- un log de rejeu est cite par le canon de la feuille jouee.
Compte declare avant de compter : 3 feuilles, 3 logs de machine 2 (deux a comparer, le
troisieme -- R-G2-5 sur le v8 -- n'a pas de log machine 2 : ses comptes sont dans sa note
57d8dd320c5a2837 : EXPOSABLE 42, CARRE 9, CONST 6).
"""
import hashlib, os, subprocess, sys, unicodedata

if len(sys.argv) != 2:
    sys.exit('usage : rejeu_relivraison_machine1_v1.py <racine du lot deplie>')
R = os.path.abspath(sys.argv[1])
ICI = os.path.dirname(os.path.abspath(__file__))
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-60s %s' % ('PASSE' if c else 'MORD ', n[:60], d))


def canon(p):
    raw = open(p, 'rb').read()
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()
    except UnicodeDecodeError:
        t = raw
    return hashlib.sha256(t).hexdigest()[:16]


def lf(p):
    return open(p, 'rb').read().replace(b'\r\n', b'\n').decode('utf-8', errors='replace').split('\n')


FEUILLES = (
    ('derivation v3', 'ACTE_constante_A/derivation_fenetre_delta_machine2_v3.py', '4353c80e60cef87c',
     'ACTE_constante_A/derivation_fenetre_delta_machine2_v3.log', 'f60104c0c3ba7ec4', None),
    ('relecture v1', 'ACTE_constante_A/relecture_nombres_acte_machine2_v1.py', '6e1409b06e887d97',
     'ACTE_constante_A/relecture_nombres_acte_machine2_v1.log', '484da81013182f02', None),
    ('R-G2-5 v2 sur le v8', 'entrant_machine1_2026-09-12_R_G2_5_v2/r_g2_5_pow_tableau_machine1_v2.py',
     '1c93be84b611e43b', None, None, 'chaine_constante_A_pour_machine1'),
)
print('racine %s' % R)
chk('le manifeste du lot resout a d0ab94382e1b5808',
    canon(os.path.join(R, 'MANIFEST_lot_machine2_RELIVRAISON_v1.txt')) == 'd0ab94382e1b5808')
chk('le banc v8 certifie est au poste, meme canon a la racine et dans la chaine',
    canon(os.path.join(R, 'banc_qualification_machine1_v8.py')) == '4d8882a2223a5c74'
    == canon(os.path.join(R, 'chaine_constante_A_pour_machine1', 'banc_qualification_machine1_v8.py')),
    '4d8882a2223a5c74')

for etq, feuille, cf, logm2, cl, cible in FEUILLES:
    print('\n== %s ==' % etq)
    pf = os.path.join(R, feuille)
    chk('feuille authentifiee par canon avant execution : %s' % cf, canon(pf) == cf, feuille)
    args = [sys.executable, pf] + ([os.path.join(R, cible)] if cible else [])
    sortie = os.path.join(ICI, 'rejeu_%s_machine1_v1.log' % etq.replace(' ', '_').replace('-', '_'))
    with open(sortie, 'wb') as f:
        rc = subprocess.call(args, cwd=os.path.dirname(pf), stdout=f, stderr=subprocess.STDOUT)
    chk('rejeu termine, code de retour 0', rc == 0, os.path.basename(sortie))
    mien = lf(sortie)
    bilan = [l for l in mien if l.startswith('BILAN')]
    print('   bilan du rejeu : %s' % (bilan[0] if bilan else 'AUCUN'))
    if logm2:
        pl = os.path.join(R, logm2)
        chk('log machine 2 authentifie par canon avant comparaison : %s' % cl, canon(pl) == cl, logm2)
        sien = lf(pl)
        dif = [(i + 1, a, b) for i, (a, b) in enumerate(zip(sien, mien)) if a != b]
        chk('meme nombre de lignes', len(sien) == len(mien), '%d / %d' % (len(sien), len(mien)))
        print('   lignes differentes : %d' % len(dif))
        for i, a, b in dif:
            print('      l.%-4d m2 | %s' % (i, a.strip()[:120]))
            print('             m1 | %s' % (b.strip()[:120]))
        # la seule difference admise entre les deux postes est le separateur ou l'emplacement d'un chemin
        seul_chemin = all(a.replace('\\', '/') == b or ('Downloads' in a and 'Downloads' in b) for _, a, b in dif)
        chk('toute difference est un chemin (separateur ou emplacement), aucun nombre',
            seul_chemin, '%d ligne(s), toutes des chemins' % len(dif) if dif else 'identique au bit')
    else:
        # section 1 du log seulement : "CLASSE  n" ; la section 5 repete les classes avec des chemins
        cl_ = {t[0]: int(t[1]) for t in (l.split() for l in mien)
               if len(t) == 2 and t[0] in ('EXPOSABLE', 'CARRE', 'CONST', 'SANS-NUMPY') and t[1].isdigit()}
        chk('comptes de machine 2 reproduits : EXPOSABLE 42, CARRE 9, CONST 6',
            cl_.get('EXPOSABLE') == 42 and cl_.get('CARRE') == 9 and cl_.get('CONST') == 6,
            'EXPOSABLE %s, CARRE %s, CONST %s, SANS-NUMPY %s' % (cl_.get('EXPOSABLE'), cl_.get('CARRE'),
                                                                   cl_.get('CONST'), cl_.get('SANS-NUMPY')))

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN DU DRIVER : %d/%d controles PASSENT' % (k, n))
print('=====================================================================')
