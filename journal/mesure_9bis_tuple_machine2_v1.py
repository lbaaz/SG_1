#!/usr/bin/env python3
# -*- coding: ascii -*-
"""D-v10-1 -- LE CONTROLE 9bis NE PEUT PAS PASSER : IL COMPARE DES OBJETS PYTHON A UNE REFERENCE
JSON, ET UN TUPLE N'EST PAS UNE LISTE. machine 2, v1, 13/09/2026.

Le run reel du volet T (v10, gel v7, delta' = 1/44100) rend NON CONCLUANT D'INSTRUMENT, prononce
par le 9bis AVANT toute lecture, sur 9 ecarts. Cette feuille MESURE ce que ces 9 ecarts sont, et
ce qu'ils ne sont pas. Trois jambes, et il en faut trois :
  (1) VALEUR : chaque ecart oppose-t-il des NOMBRES, ou seulement deux TYPES ? (Compare les deux
      cotes de la chaine d'ecart apres retrait des delimiteurs -- aucune evaluation.)
  (2) SERIALISATION : le JSON de sortie du run, compare a la reference par la MEME fonction de
      marche que l'instrument, rend-il zero ecart ? (Si oui, la mesure est reproduite ; c'est la
      comparaison qui ne l'est pas.)
  (3) SATISFIABILITE : existe-t-il un run qui puisse passer ce controle ? Un fichier JSON ne
      porte pas de tuples ; toute cle du perimetre dont la valeur est un tuple en memoire mord
      donc a TOUT run, pour toujours. C'est la famille du controle M du gel v4 : une etiquette
      qu'aucun objet ne peut satisfaire.
Aucune piece n'est editee. Deux verbes : chk mesure et compte ; note porte la prose.
"""
import json, os, sys

OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-56s %s' % ('PASSE' if c else 'MORD ', n[:56], d))


def note(n, d=''):
    print('  [ note] %-56s %s' % (n[:56], d))


RUN = json.load(open('out_run_delta91/temoin/resultats_temoin.json', encoding='utf-8'))
REF = json.load(open('registre/runs/run_temoin_delta85/resultats_temoin.json', encoding='utf-8'))
C9 = RUN['controle_9bis']
PROF, EXEMPT, PERIM = C9['profondeur'], C9['exemptes'], C9['perimetre']


def au_chemin(o, ch):
    for part in ch.strip('/').replace('[', '/').replace(']', '').split('/'):
        o = o[int(part)] if part.isdigit() else o[part]
    return o


# --------------------------------------------------------------------------------
print('\n1. LE VERDICT, ET CE QUE LE 9bis A DIT')
# --------------------------------------------------------------------------------
chk('le run rend NON CONCLUANT D INSTRUMENT, prononce par le 9bis',
    RUN['verdict'] == "NON CONCLUANT D'INSTRUMENT" and RUN['branche'].startswith('9bis'), RUN['branche'][:70])
chk('la custody du 9bis est JOUEE et concordante (4/4)', C9['custody'].startswith('JOUE') and '4/4' in C9['custody'], C9['custody'][:60])
chk('le depot 9bis charge est bien c4310e33da6b9759', C9['depot_empreinte'] == 'c4310e33da6b9759', C9['depot_empreinte'])
chk('%d ecarts, tous dans /T1 et /T1b' % C9['n_ecarts'],
    len(C9['ecarts']) == C9['n_ecarts'] == 9 and all(e.startswith(('/T1/', '/T1b/')) for e in C9['ecarts']),
    ', '.join(sorted(set(e.split('/')[1] for e in C9['ecarts']))))

# --------------------------------------------------------------------------------
print('\n2. JAMBE (1) -- CHAQUE ECART : DES NOMBRES, OU DEUX TYPES ?')
# --------------------------------------------------------------------------------
valeurs, types = [], []
for e in C9['ecarts']:
    chemin, paire = e.split(' (', 1)
    g, d = paire.rstrip(')').split(' != ')
    # aucune evaluation : on retire les delimiteurs et on compare les deux textes
    gt, dt = g.strip('()[] '), d.strip('()[] ')
    memes = (gt == dt)
    (types if memes else valeurs).append((chemin, g[0], d[0]))
    print('   %-34s %s...%s contre %s...%s  contenu %s'
          % (chemin[-34:], g[0], g[-1], d[0], d[-1], 'IDENTIQUE' if memes else 'DIFFERENT'))
chk('aucun des 9 ecarts n oppose des nombres', not valeurs, ', '.join(c for c, _, _ in valeurs) or '0 ecart de valeur')
chk('les 9 opposent une parenthese (tuple, memoire) a un crochet (liste, JSON)',
    len(types) == 9 and all(tuple(x) == ('(', '[') for _, *x in types), '9/9')
note('FAIT VERSE CONTRE MOI, et il est la meilleure preuve du defaut',
     "la premiere version de CETTE feuille ecrivait x == ('(', '[') ou x est une LISTE issue d un"
     " deballage : elle a MORDU sur son propre controle, par la meme faute exactement -- une liste"
     " comparee a un tuple. Le defaut n est pas une etourderie de l instrument : c est un piege de"
     " la langue, et il attrape aussi qui le mesure.")

# --------------------------------------------------------------------------------
print('\n3. JAMBE (2) -- LE JSON DE SORTIE CONTRE LA REFERENCE, MEME MARCHE')
# --------------------------------------------------------------------------------
def marche(a, b, chemin, prof, ecarts):
    """La fonction de l'instrument, recopiee a la lettre (v10 l.1841-1868)."""
    if prof > PROF:
        return
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if str(k) in EXEMPT:
                continue
            if k not in a or k not in b:
                ecarts.append('%s/%s (cle absente d un cote)' % (chemin, k))
            else:
                marche(a[k], b[k], '%s/%s' % (chemin, k), prof + 1, ecarts)
        return
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            ecarts.append('%s (longueurs %d != %d)' % (chemin, len(a), len(b)))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            marche(x, y, '%s[%d]' % (chemin, i), prof + 1, ecarts)
        return
    if a != b:
        ecarts.append('%s (%r != %r)' % (chemin, a, b))


ec_json = []
for c in PERIM:
    marche(RUN.get(c), REF.get(c), '/' + c, 1, ec_json)
chk('le JSON du run, contre la reference, par la MEME marche : 0 ecart', not ec_json,
    ', '.join(ec_json[:3]) or '0 ecart sur /%s' % ', /'.join(PERIM))
note('ce que cela veut dire', 'la mesure EST reproduite sur le perimetre 9bis ; ce qui ne l est pas, c est la comparaison')

# --------------------------------------------------------------------------------
print('\n4. JAMBE (3) -- LE CONTROLE EST-IL SATISFIABLE PAR UN RUN QUELCONQUE ?')
# --------------------------------------------------------------------------------
memes = [(e.split(' (')[0], au_chemin(RUN, e.split(' (')[0]) == au_chemin(REF, e.split(' (')[0])) for e in C9['ecarts']]
chk('les 9 chemins portent, DANS LE JSON, la meme valeur des deux cotes', all(x for _, x in memes),
    ', '.join(c for c, x in memes if not x) or '9/9')
chk('un fichier JSON ne peut pas porter de tuple : le controle est INSATISFIABLE',
    json.loads(json.dumps({'x': (1, 2)}))['x'] == [1, 2] and json.loads(json.dumps({'x': (1, 2)}))['x'] != (1, 2),
    'json.dumps rend une liste ; aucune reference JSON ne rendra jamais un tuple')
note('portee exacte', 'tout run dont une cle du perimetre vaut un tuple en memoire MORD, quelle que soit sa mesure')
note('famille', 'meme defaut que le controle M du gel v4 : une etiquette qu aucun objet ne peut satisfaire')

# --------------------------------------------------------------------------------
print('\n5. CE QUE LA PHYSIQUE DU RUN A RENDU, MALGRE LE VERDICT')
# --------------------------------------------------------------------------------
pts = RUN['T2']['points']
chk('les 9 cellules de T-2 rendent W-pas PASSE et W-plancher PASSE',
    all(pts[k]['W_pas'] == 'PASSE' and pts[k]['W_plancher'] == 'PASSE' for k in pts), '9/9')
chk('W-comptes : comptes + sautes == attendus', RUN['W_comptes'] == 'PASSE', RUN['W_comptes'])
note('les neuf ratios e/seuil', ' '.join('%s %.3f' % (k, pts[k]['ratio_seuil']) for k in sorted(pts)))
note('les neuf p_obs', ' '.join('%s %.4f' % (k, pts[k]['p_obs']) for k in sorted(pts)))
note('ce que le verdict serait sans le 9bis', 'a re-derive par la cascade, apres correction de l instrument')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('D-v10-1 : le 9bis compare des objets Python a une reference JSON ; 9 cles du perimetre')
print('valent un tuple en memoire et une liste au JSON : le controle MORD A TOUT RUN.')
print('=====================================================================')
sys.exit(0 if k == n else 1)
