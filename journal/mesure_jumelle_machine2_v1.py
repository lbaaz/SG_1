#!/usr/bin/env python3
# -*- coding: ascii -*-
"""D-v11-1 -- LA TRAJECTOIRE JUMELLE EST JOUEE A PAS MOITIE ET SES COMPTES SONT COMPARES AUX
INTERVALLES DU PAS NOMINAL : G-dt REND G-fen A TOUT RUN. machine 2, v1, 13/09/2026.

Le run reel du volet A (v11, gel v7, delta' = 1/44100) rend NON CONCLUANT DE FENETRE, branche 3,
"degres exploitables []". Cette feuille MESURE ou est la fenetre manquante. Quatre jambes :
  (1) QUI tombe : les 18 trajectoires du plan, les 18 a k = 4, les 9 sous le seuil, les 18 de la
      jumelle -- combien rendent un POINT FIXE ?
  (2) SUR QUOI : la morsure porte-t-elle sur la fenetre d'ajustement (trop peu de points) ou sur
      un COMPTE d'etage ?
  (3) LE GEL : le compte mesure tombe-t-il dans l'intervalle que le gel v7 4.8 derive POUR LA
      JUMELLE (bornes doublees), ou seulement hors de celui du pas NOMINAL ?
  (4) LA CAUSE DANS LE CODE : l'instrument a-t-il le mecanisme (facteur de jumelle) et l'a-t-il
      arme a l'appel ?
Et ce que les enregistrements portent DEJA, quoique la cascade n'ait pas pu le lire.
Aucune piece n'est editee. Deux verbes : chk mesure et compte ; note porte la prose.
"""
import ast, json, math, os, re, sys
from fractions import Fraction as F

OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def note(n, d=''):
    print('  [ note] %-58s %s' % (n[:58], d))


J = json.load(open('out_run_delta91/alpha/resultats_alpha.json', encoding='utf-8'))
SRC = open('banc_qualification_machine1_v11.py', encoding='utf-8').read()
GEL = open('constante_A_pre_enregistrement_v7.md', encoding='utf-8').read()

# --------------------------------------------------------------------------------
print('\n1. JAMBE (1) -- QUI TOMBE, ET QUI TIENT')
# --------------------------------------------------------------------------------
compte = {}
for nom in ('plan', 'G_dt', 'G_k', 'seuil'):
    st = {}
    for v in J[nom].values():
        st[v.get('statut')] = st.get(v.get('statut'), 0) + 1
    compte[nom] = st
    print('   %-6s %s' % (nom, ', '.join('%s : %d' % kv for kv in sorted(st.items()))))
chk('les 18 trajectoires du PLAN rendent toutes un POINT FIXE', compte['plan'] == {'POINT_FIXE': 18}, '18/18')
chk('les 18 trajectoires a k = 4 (G-k) aussi', compte['G_k'] == {'POINT_FIXE': 18}, '18/18')
chk('les 9 trajectoires sous le seuil sont AJUSTEES', compte['seuil'] == {'AJUSTE': 9}, '9/9')
chk('les 18 trajectoires de la JUMELLE (G-dt) rendent toutes G-fen', all(s.startswith('G-fen') for s in compte['G_dt']),
    '18/18 ; seule la jumelle tombe')
chk('le verdict est branche 3, aucun degre exploitable',
    J['verdict'].endswith('NON CONCLUANT DE FENETRE') and 'exploitables []' in J['branche'], J['branche'][-40:])

# --------------------------------------------------------------------------------
print('\n2. JAMBE (2) -- SUR QUOI LA JUMELLE MORD : FENETRE, OU COMPTE D ETAGE ?')
# --------------------------------------------------------------------------------
motifs, comptes_2b = {}, []
for v in J['G_dt'].values():
    m = re.match(r'G-fen \(compte (\w+) = (\d+) hors \[(\d+), (\d+)\]\)', v['statut'])
    if m:
        motifs.setdefault(m.group(1), 0)
        motifs[m.group(1)] += 1
        comptes_2b.append((int(m.group(2)), int(m.group(3)), int(m.group(4))))
chk('les 18 morsures portent sur un COMPTE D ETAGE, pas sur la fenetre d ajustement',
    len(comptes_2b) == 18 and set(motifs) == {'n_2b'}, ', '.join('%s : %d' % kv for kv in motifs.items()))
lo, hi = comptes_2b[0][1], comptes_2b[0][2]
chk('l intervalle oppose est le meme pour les 18 : [%d, %d]' % (lo, hi),
    all((a, b) == (lo, hi) for _, a, b in comptes_2b), 'l intervalle du PAS NOMINAL (gel 4.6)')
note('les 18 comptes mesures', 'de %d a %d' % (min(c for c, _, _ in comptes_2b), max(c for c, _, _ in comptes_2b)))
chk('tous les comptes mesures sont a peu pres DOUBLES de la borne haute nominale',
    all(1.85 * hi <= c <= 2.05 * hi for c, _, _ in comptes_2b), '~2 x %d' % hi)

# --------------------------------------------------------------------------------
print('\n3. JAMBE (3) -- LE GEL v7 4.8 : L INTERVALLE DE LA JUMELLE')
# --------------------------------------------------------------------------------
chk('le gel v7 4.8 dit que la jumelle divise par 2 le pas de CHAQUE etage',
    'divise par 2 le pas de' in re.sub(r'\s+', ' ', GEL) and 'CHAQUE etage' in re.sub(r'\s+', ' ', GEL), '4.8')
chk('et que ses DEUX bornes sont multipliees par 2',
    'leurs DEUX bornes sont multipliees par 2' in re.sub(r'\s+', ' ', GEL), 'forme derivee, jamais recopiee')
m = re.search(r'n_2b jumelle : \[(\d+), (\d+)\]', GEL)
loj, hij = int(m.group(1)), int(m.group(2))
chk('n_2b jumelle au gel = [%d, %d] = 2 x [%d, %d]' % (loj, hij, lo, hi), (loj, hij) == (2 * lo, 2 * hi), 'derive')
dedans = [c for c, _, _ in comptes_2b if loj <= c <= hij]
chk('les 18 comptes mesures tombent DANS l intervalle de la jumelle du gel', len(dedans) == 18,
    '%d/18 dans [%d, %d]' % (len(dedans), loj, hij))
note('portee exacte', 'la mesure est conforme au gel ; c est la COMPARAISON qui ne l est pas')

# --------------------------------------------------------------------------------
print('\n4. JAMBE (4) -- LA CAUSE DANS LE CODE : LE MECANISME EXISTE, IL N EST PAS ARME')
# --------------------------------------------------------------------------------
chk('trajectoire_plan a un parametre jumelle, par defaut False',
    'def trajectoire_plan(' in SRC and 'jumelle=False' in SRC, 'signature')
chk('et il commande le facteur des intervalles', 'fac = 2 if jumelle else 1' in SRC, 'fac')
appels = re.findall(r'^\s*(plan|gdt|gk)\[cle\] = trajectoire_plan\((.+)$', SRC, re.M)
gdt_reels = [a for nom, a in appels if nom == 'gdt' and 'sortie,' in a]
chk('le run REEL appelle la jumelle a dt2 / 2 SANS armer jumelle=True', len(gdt_reels) == 1 and 'dt2 / 2' in gdt_reels[0]
    and 'jumelle' not in gdt_reels[0], gdt_reels[0][:96] if gdt_reels else 'appel introuvable')
chk('aucun appel du fichier n arme jumelle=True', 'jumelle=True' not in SRC, '0 occurrence')
chk('le PRE-VOL ne pouvait pas l attraper : son synthetique declare les gardes de compte NON JOUEES',
    'gardes de compte NON JOUEES' in SRC, 'une phase, pas d etages')
note('consequence', 'G-dt rend G-fen a tout run reel : exploitable = False aux trois degres, branche 3, '
                    'AUCUN run ne pouvait conclure -- meme famille que D-v10-1')

# --------------------------------------------------------------------------------
print('\n5. CE QUE LES ENREGISTREMENTS PORTENT DEJA, QUOIQUE LA CASCADE N AIT RIEN PU LIRE')
# --------------------------------------------------------------------------------
AL = {4: 2.0, 5: 4.0 / 3.0, 7: 4.0 / 5.0}
for nom in ('plan', 'G_k'):
    for p in (4, 5, 7):
        a = [v['ajustement']['alpha'] for k, v in J[nom].items() if k.startswith('%d|' % p)]
        d = [abs(x - AL[p]) for x in a]
        print('   %-5s p = %d : alpha de %.6f a %.6f  (4/(p-2) = %.6f)  ecart max %.2e sur %d trajectoires'
              % (nom, p, min(a), max(a), AL[p], max(d), len(a)))
for p in (4, 5, 7):
    a = [v['ajustement']['alpha'] for k, v in J['plan'].items() if k.startswith('%d|' % p)]
    chk('p = %d : les 6 alpha du plan collent a 4/(p-2) a mieux que 1e-4' % p, max(abs(x - AL[p]) for x in a) < 1e-4,
        'ecart max %.2e' % max(abs(x - AL[p]) for x in a))
lnA = [v['ajustement'].get('gA_II_sur_K') for v in J['plan'].values() if v['ajustement'].get('gA_II_sur_K')]
if lnA:
    note('gA^(p-2)/K au plan (II)', 'de %.6f a %.6f sur %d trajectoires' % (min(lnA), max(lnA), len(lnA)))
note('ce que cela ne dit PAS', 'P-alpha et P-A sont des lectures de la cascade, sur des grandeurs que G-dt alimente : '
                               'elles ne se prononcent pas ici. Le run se REJOUE apres correction, il ne se lit pas a la main.')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('D-v11-1 : la jumelle G-dt est jouee a pas moitie et ses comptes d etage sont compares aux')
print('intervalles du pas NOMINAL ; le mecanisme (jumelle=True) existe et n est jamais arme.')
print('=====================================================================')
sys.exit(0 if k == n else 1)
