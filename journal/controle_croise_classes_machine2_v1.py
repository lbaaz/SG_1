#!/usr/bin/env python3
# -*- coding: ascii -*-
"""D-ACA-2 -- LE CONTROLE CROISE DES CLASSES, JOUE SUR LES JSON. machine 2, 12/09/2026.

MACHINE 1 A ECRIT CE CONTROLE (sa note a1b4bab69cff979c, section 3) ET NE PEUT PAS LE
JOUER : son conteneur est reinitialise, les JSON sont a mon poste. Je le joue.

SON ENONCE, VERBATIM : "aux trois cellules fines (4|2.27, 5|1.73, 5|2.80), comparer noyau
contre libm les etats finaux (x1, x2) des flots dt2/2 et dt2/4 et champ_forces_empreinte.
Issue qui mord : etats identiques ET e differents -> la classe se definit sur e au bit,
pas sur x1 a la paire ; etats differents -> '0 basculement net' etait faux."

CE QUE LES PIECES NE PORTENT PAS, ET IL FAUT LE DIRE AVANT DE CONCLURE :
  -- il n'y a PAS de `dt2/4` dans ces JSON. `/T2/points/<pt>/err` porte `dt2` et `dt2/2`,
     rien d'autre. La moitie "dt2/4" de son controle est INJOUABLE en l'etat.
  -- il n'y a PAS d'etats finaux `x1, x2` par cellule. Les grandeurs d'ETAT presentes sont
     `x_bascule`, `bascule/x_b_num`, `bascule/tau_b`, `tau_CAP`, `tau_dom`, `dt2`, les
     compteurs de pas, et les grandeurs derivees `R_composantes`, `plancher_*`, `seuil_5_4`.
  -- `champ_forces_empreinte` est GLOBAL au run, pas par cellule : il ne discrimine aucune
     cellule (et il est deja connu : 0491b83e6893dbbf noyau, f150f2685187b9d2 libm).
SON OBJET EST DONC JOUE SUR LES FEUILLES QUE LES PIECES PORTENT : toutes les feuilles de
chaque point, partagees en ETAT et en ERREUR. C'est la meme question -- l'ecart touche-t-il
la trajectoire, ou seulement l'erreur ? -- posee aux grandeurs qui existent.

PB-1 : aucune piece recue n'est editee. Ses deux JSON sont lus tels que recus.
"""
import json, os

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-54s %s' % ('PASSE' if c else 'MORD ', n[:54], d))


def pts(*a):
    return json.load(open(P(*a), encoding='utf-8'))['T2']['points']


def glob(*a):
    return json.load(open(P(*a), encoding='utf-8'))


LOT = ('entrant_machine1_2026-09-12_reponse_globale', 'lot')
N = pts(*(LOT + ('resultats_temoin_prevol_noyau_machine1.json',)))
L = pts(*(LOT + ('resultats_temoin_prevol_libm_machine1.json',)))
GN = glob(*(LOT + ('resultats_temoin_prevol_noyau_machine1.json',)))
GL = glob(*(LOT + ('resultats_temoin_prevol_libm_machine1.json',)))
M = pts('m2_v8_prevol_temoin_resultats.json')

# Grandeurs de TRAJECTOIRE (etat du flot et geometrie du pas), par opposition aux
# grandeurs d'ERREUR (e et tout ce qui se calcule a partir de e).
ETAT = {'x_bascule', 'tau_CAP', 'tau_dom', 'dt2', 'A', 'CAP_p', 'alpha', 'C_effectif',
        'R_composantes', 'plancher_composantes', 'plancher_accum', 'seuil_5_4',
        'tol_ordre', 'tol_ordre_sur_1', 'plafond_ordre', 'x_b_num', 'tau_b', 'n_g1',
        'n_g2', 'n_pas_phase2', 'intervalle_g2', 'n_pas', 'tau_fin', 'evenement',
        'g2_dans_intervalle'}

FINES = ['4|2.27', '5|1.73', '5|2.80']
GROSSES = ['4|1.73', '4|2.80', '7|1.73']
RATIO_EGAL = ['5|2.27', '7|2.27', '7|2.80']


def feuilles(d, pre=''):
    for k in sorted(d):
        v, c = d[k], pre + '/' + k
        if isinstance(v, dict):
            for x in feuilles(v, c):
                yield x
        else:
            yield c, v


def partage(a, b):
    da, db = dict(feuilles(a)), dict(feuilles(b))
    dif = [c for c in da if da[c] != db[c]]
    return ([c for c in dif if c.split('/')[-1] in ETAT],
            [c for c in dif if c.split('/')[-1] not in ETAT], len(da))


# =====================================================================
print("\n0. CE QUE SON CONTROLE NOMME ET QUE LES PIECES NE PORTENT PAS")
# =====================================================================
pas = sorted(N['5|1.73']['err'])
chk('les pieces ne portent PAS de pas dt2/4', 'dt2/4' not in pas, 'err porte : ' + ','.join(pas))
chk('les pieces ne portent PAS d etats finaux x1, x2 par cellule',
    not any(k in N['5|1.73'] for k in ('x1', 'x2')), 'etats presents : x_bascule, x_b_num')
chk('champ_forces_empreinte est GLOBAL, donc ne discrimine aucune cellule',
    GN['champ_forces_empreinte'] != GL['champ_forces_empreinte'],
    '%s / %s' % (GN['champ_forces_empreinte'], GL['champ_forces_empreinte']))

# =====================================================================
print("\n1. SON CONTROLE, AUX TROIS CELLULES FINES QU'ELLE NOMME")
# =====================================================================
for k in FINES:
    e, r, n = partage(N[k], L[k])
    print('   %-8s %d feuilles | ETAT %d : %s | ERREUR %d'
          % (k, n, len(e), ','.join(x.split('/')[-1] for x in e) or 'aucune', len(r)))
etats_diff = [k for k in FINES if partage(N[k], L[k])[0]]
chk('aux 3 FINES, des grandeurs d ETAT different', len(etats_diff) == 3,
    ','.join(etats_diff))
chk('donc son issue (b) mord : "0 basculement net" etait FAUX',
    len(etats_diff) == 3, 'ce n est pas l issue (a)')

# =====================================================================
print("\n2. ET LE RESULTAT VA PLUS LOIN QUE SA QUESTION -- LES NEUF CELLULES")
# =====================================================================
for titre, grp in (('GROSSIERES', GROSSES), ('FINES', FINES),
                   ('RATIO EGAL AU BIT', RATIO_EGAL)):
    print('   -- %s' % titre)
    for k in grp:
        e, r, n = partage(N[k], L[k])
        print('      %-8s ETAT %d  ERREUR %d   x_b_num %s'
              % (k, len(e), len(r),
                 'DIFFERE' if N[k]['bascule']['x_b_num'] != L[k]['bascule']['x_b_num']
                 else 'identique'))
aucune = [k for k in N if N[k] == L[k]]
chk('AUCUNE des 9 cellules n est integralement identique', not aucune,
    ','.join(sorted(aucune)) or '0 cellule intacte')
xb = sorted(k for k in N if N[k]['bascule']['x_b_num'] != L[k]['bascule']['x_b_num'])
chk('x_b_num differe sur 7 des 9 cellules', len(xb) == 7, ','.join(xb))
rs = sorted(k for k in N if N[k]['ratio_seuil'] != L[k]['ratio_seuil'])
chk('ratio_seuil ne differe que sur 6 -- l absorption est EN AVAL', len(rs) == 6,
    ','.join(rs))
inter = sorted(set(RATIO_EGAL) & set(xb))
chk('les 3 cellules a ratio EGAL portent quand meme un ecart d ETAT',
    len(inter) == 3, ','.join(inter))

# =====================================================================
print("\n3. CE QUE LA CLASSE 'ABSORBEE' DEVIENT")
# =====================================================================
# Mordrait si une seule cellule etait intacte de bout en bout : la classe aurait un membre.
chk('la classe ABSORBEE (aucun ecart au bit) est VIDE a T2', not aucune,
    '0 membre sur 9 ; l absorption vaut par FEUILLE, pas par CELLULE')
chk('tau_CAP est identique noyau/libm aux 9 points',
    all(N[k]['tau_CAP'] == L[k]['tau_CAP'] for k in N), 'le pas n est pas touche')

# =====================================================================
print("\n4. LA RESIDUELLE ENTRE MON POSTE ET SON RUN SANS NOYAU")
# =====================================================================
res = {}
for k in M:
    e, r, n = partage(M[k], L[k])
    for c in e + r:
        res.setdefault(c.split('/')[-1], []).append(k)
chk('mon poste == son LIBM sur les 9 ratio_seuil AU BIT',
    all(M[k]['ratio_seuil'] == L[k]['ratio_seuil'] for k in M), '9/9')
entiers = sorted(k for k in M if M[k] == L[k])
chk('mais seulement 6 des 9 POINTS ENTIERS sont identiques', len(entiers) == 6,
    'differents : ' + ','.join(sorted(set(M) - set(entiers))))
chk('et la residuelle est UNE seule grandeur, une tolerance', set(res) == {'tol_ordre',
    'tol_ordre_sur_1'}, ','.join(sorted(res)))
for g, ks in sorted(res.items()):
    k0 = ks[0]
    print('      %-18s %d cellules (%s) ecart %.1e'
          % (g, len(ks), ','.join(sorted(ks)),
             abs(L[k0][g] - M[k0][g]) / M[k0][g]))
chk('elle est degre-selective : tout p=7, aucun p=4 ni p=5',
    all(k.startswith('7|') for ks in res.values() for k in ks), 'meme famille que tol_int')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('VERDICT D-ACA-2 : son issue (b) -- les etats DIFFERENT, "0 basculement net"')
print('etait faux ; et la classe ABSORBEE est VIDE a T2 (0 cellule intacte sur 9).')
print('=====================================================================')
