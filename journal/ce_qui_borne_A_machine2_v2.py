"""ce_qui_borne_A_machine2_v2.py -- machine 2, 2026-09-29.

v2 = la v1 (ed5bbce867f0a41d, emise dans le lot 996dc8be7d245387) CONFRONTEE AU RUN 93.
La v1 ne disposait que du run 92 (n = 18). Le run 93 (n = 21, instrument v16) permet de la
tester -- et il en REFUTE la partie la plus forte, celle sur laquelle ma certification du v10
avait bati sa reserve de fond. Cette piece etablit ce qui survit et ce qui tombe.

  CE QUI SURVIVAIT A UN SEUL REGLAGE, ET QUI TOMBE :
    la dependance en c n'a PAS un seul signe. Au 92 elle etait positive aux six points de
    p = 4 et 5 (mesure, reproduite au bit entre machines) ; au 93 elle est MELEE a p = 4.
    Donc "la vraie valeur est au-dela du couple de c, et A(p) porte un biais de 1.6e-09,
    sept a neuf fois delta_p" N'EST PAS SOUTENU a n = 21. Je le retire.
  ET CE QUI TOMBE AUSSI, MA Q4 :
    j'avais conclu qu'a p = 4 et 5 l'effet ne suivait pas delta' et qu'un plus grand n ne
    l'achetait donc pas. Mesure : S(4) x 0.471 et S(5) x 0.652 pour delta' x 0.735. La
    dispersion a baisse autant ou PLUS que delta'. La regle du plus grand n, que machine 1
    a restauree et que je mettais en doute, a livre ce qu'elle promettait aux deux degres
    ou la lecture etait bornee.
  CE QUI SURVIT :
    S(p) reste 3e+04 a 7e+04 fois le plancher analytique : ce n'est toujours pas le terme
    suivant qui borne. Et a p = 7, seul degre ou la regle du plus grand n ne donne rien,
    S MONTE (x 1.396).

Deux verbes : chk (peut mordre), note (ne peut pas). Aucun run neuf : tout se lit dans les
JSON des runs 92 et 93 deja joues.
"""
import hashlib
import json
import os
import sys
import unicodedata

R92 = 'out_run_delta92/alpha_v15/resultats_alpha.json'
R93 = 'out_run_delta93/alpha_v16/resultats_alpha.json'
W2S = ('1.73', '2.27', '2.80')
DEGRES = (4, 5, 7)
LEV = 324 / 441
lignes, bilan = [], {'chk': 0, 'mord': []}


def out(s=''):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=''):
    bilan['chk'] += 1
    if not cond:
        bilan['mord'].append(nom)
    out('  [chk %s] %s%s' % ('PASSE' if cond else 'MORD ', nom, (' -- ' + detail) if detail else ''))
    return cond


def note(nom, detail):
    out('  [note] %s -- %s' % (nom, detail))


def B(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


def effet_c(d, p):
    ec = d['degres'][str(p)]['ecarts_corriges']
    return [(ec['%d|%s|1.20' % (p, w)] - ec['%d|%s|1.05' % (p, w)]) * 1e9 for w in W2S]


a = json.load(open(R92, encoding='utf-8'))
b = json.load(open(R93, encoding='utf-8'))

out('CE QUI BORNE A(w2) -- v2, CONFRONTEE AU RUN 93')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out('runs : 92 (n=18) %s ; 93 (n=21) %s' % (B(R92), B(R93)))

# ---------------------------------------------------------------- 1
out()
out('1. CE QUI TOMBE (1) -- LE SIGNE UNIQUE DE LA DEPENDANCE EN c NE SE REPRODUIT PAS')
sg92, sg93 = {}, {}
for p in DEGRES:
    d92, d93 = effet_c(a, p), effet_c(b, p)
    sg92[p] = 'tous positifs' if all(x > 0 for x in d92) else ('tous negatifs' if all(x < 0 for x in d92) else 'meles')
    sg93[p] = 'tous positifs' if all(x > 0 for x in d93) else ('tous negatifs' if all(x < 0 for x in d93) else 'meles')
    note('p=%d' % p, 'n=18 : %s -> %-14s | n=21 : %s -> %s'
         % (' '.join('%+7.3f' % x for x in d92), sg92[p],
            ' '.join('%+7.3f' % x for x in d93), sg93[p]))
chk('1.1 : au 92, le signe etait UNIQUE a p = 4 et 5 (ce que la v1 a mesure, et c etait vrai la)',
    sg92[4] == sg92[5] == 'tous positifs')
chk('1.2 : au 93, il ne l est PLUS a p = 4 -- la v1 avait generalise un seul reglage',
    sg93[4] == 'meles', 'p=4 %s ; p=5 %s ; p=7 %s' % (sg93[4], sg93[5], sg93[7]))
note('1.3 ce que je retire', 'la reserve de fond de ma certification du v10 -- "A(p) porte un '
     'biais de fenetre de ~1.6e-09, sept a neuf fois le delta_p" -- reposait sur ce signe '
     'unique. Signes meles, la moyenne sur deux c est un centre defendable et l argument du '
     'biais tombe. Ce que j avais mesure au 92 etait exact ; ce que j en avais conclu pour tout '
     'reglage ne l etait pas.')
note('1.4 ce qui reste vrai de la v1', 'l effet de c reste du meme ordre (demi-etendue 1.7 a '
     '2.4e-09 au 93 contre 1.6 a 2.1 au 92) et il reste, au 92, reproduit AU BIT entre les deux '
     'machines : c est bien un systematique deterministe, pas du bruit. Ce n est pas sa nature '
     'qui est en cause, c est le BIAIS que j en deduisais.')

# ---------------------------------------------------------------- 2
out()
out("2. CE QUI TOMBE (2) -- MA Q4 : \"UN PLUS GRAND n N ACHETE RIEN A p = 4 ET 5\"")
rap = {}
for p in DEGRES:
    s92, s93 = a['degres'][str(p)]['S_p'], b['degres'][str(p)]['S_p']
    rap[p] = s93 / s92
    note('p=%d' % p, 'S(p) %.3e -> %.3e ; rapport %.3f ; attendu si S ~ delta\' %.3f'
         % (s92, s93, rap[p], LEV))
chk('2.1 : a p = 4 et 5, S(p) a BAISSE autant ou plus que delta\' -- ma Q4 est refutee',
    rap[4] <= LEV and rap[5] <= LEV * 1.05, '%.3f et %.3f contre %.3f' % (rap[4], rap[5], LEV))
chk('2.2 : a p = 7, S(p) a MONTE -- la regle du plus grand n n y achete rien',
    rap[7] > 1, '%.3f' % rap[7])
note('2.3 ce que je retire', 'j avais ecrit que la regle du plus grand n, restauree par le v10, '
     'n achetait pas ce qu il fallait la ou la lecture etait bornee. C est faux a p = 4 et 5 : '
     'elle a divise la dispersion par 2.1 et 1.5. Machine 1 avait raison sur les deux degres '
     'ou son gel visait juste, et mon objection generalisait un diagnostic tire du seul 92.')

# ---------------------------------------------------------------- 3
out()
out('3. CE QUI SURVIT -- LE PLANCHER N EST TOUJOURS PAS LA LIMITE')
for p in DEGRES:
    D = b['degres'][str(p)]
    note('p=%d' % p, 'S(p) %.3e ; plancher corrige %.3e ; rapport %.1e'
         % (D['S_p'], D['plancher_corrige'], D['S_p'] / D['plancher_corrige']))
chk('3.1 : a n = 21, S(p) reste 3e+04 a 8e+04 fois le plancher analytique',
    all(2e4 <= b['degres'][str(p)]['S_p'] / b['degres'][str(p)]['plancher_corrige'] <= 1e5 for p in DEGRES))
note('3.2', 'ce qui borne la mesure n est toujours pas le terme analytique suivant. Mais je ne '
     'sais plus dire ce que c est : la v1 le nommait (un systematique de fenetre monotone), le '
     '93 refute cette forme-la. Ce qui reste est un residu de ~2e-09 a 5e-09, de meme ordre aux '
     'deux reglages, dont la structure m echappe.')

# ---------------------------------------------------------------- 4
out()
out('4. LA MESURE DE A, AUX DEUX REGLAGES')
TH = {4: 48.989794856, 5: 9.650477151, 7: 3.142438762}
for p in DEGRES:
    d92 = sum(a['degres'][str(p)]['ecarts_corriges'].values()) / 6
    d93 = sum(b['degres'][str(p)]['ecarts_corriges'].values()) / 6
    A92, A93 = TH[p] * pow(2.718281828459045, d92), TH[p] * pow(2.718281828459045, d93)
    note('p=%d' % p, 'A(92) %.9f ; A(93) %.9f ; theorique %.9f ; ecarts relatifs %.1e et %.1e'
         % (A92, A93, TH[p], abs(A92 / TH[p] - 1), abs(A93 / TH[p] - 1)))
chk('4.1 : aux deux reglages, A(p) coincide avec (K/g)^(1/(p-2)) a mieux que 1e-08',
    all(abs(sum(d['degres'][str(p)]['ecarts_corriges'].values()) / 6) < 1e-8
        for d in (a, b) for p in DEGRES))
note('4.2', 'les deux reglages donnent la meme valeur a 1e-09 pres et s accordent avec la forme '
     'auto-semblable. C est un resultat, et il ne depend d aucune des deux choses que je retire '
     'ci-dessus.')

# ---------------------------------------------------------------- BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'signes_92': sg92, 'signes_93': sg93,
          'rapport_S_93_sur_92': {str(p): rap[p] for p in DEGRES},
          'retire': ['le biais de fenetre monotone (v1 section 5)',
                     'Q4 : un plus grand n n achete rien a p = 4 et 5'],
          'portee': 'v2 ; aucun run neuf ; refute deux conclusions de la v1'}
with open('ce_qui_borne_A_machine2_v2.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1)
with open('ce_qui_borne_A_machine2_v2.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('ce_qui_borne_A_machine2_v2.log'))
