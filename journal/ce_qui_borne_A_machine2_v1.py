"""ce_qui_borne_A_machine2_v1.py -- machine 2, 2026-09-29.

CE QUI BORNE A(w2) APRES LE DELTA 92 -- mesure sur les runs deja deposes, aucun run neuf.

L'acte du 92 (nn.12) ecrit : "le run rend une porte et deux tests, pas une valeur ; la P-A
corrigee vraie aux trois degres est un test a tolerance d'instrument (~4e-09), pas une mesure
de A(w2)". Et nn.9 (iv) trace le chemin : gel v10, RESTAURER LA REGLE DU PLUS GRAND n avec le
plancher corrige. Cette piece demande ce que cette regle achete, en mesurant d'abord CE QUI
BORNE aujourd'hui -- car la reponse n'est pas celle qu'on attendait.

Quatre questions, dans l'ordre :
  Q1  La dispersion residuelle S(p) est-elle le plancher analytique ? (non : quatre ordres)
  Q2  Est-elle structuree en w2 -- c'est-a-dire est-ce DEJA A(w2) qu'on voit ?
  Q3  Est-elle du bruit, ou un systematique ? (test : se reproduit-elle entre les deux
      machines, dont les arithmetiques different ?)
  Q4  Depend-elle de delta' -- c'est-a-dire un plus grand n la reduirait-il ?
Rien n'est joue : tout se lit dans les JSON des runs 91 et 92, des deux machines.
Deux verbes : chk (peut mordre), note (ne peut pas).
"""
import hashlib
import json
import os
import statistics as st
import sys
import unicodedata

R92 = 'out_run_delta92/alpha_v15/resultats_alpha.json'
R92M1 = 'm1_run_delta92/m1_out_run_delta92/alpha_v15/resultats_alpha.json'
P92 = 'm2_lecture_v9_predictions_delta92.json'
P91 = 'm2_repetition_predictions_sur_91.json'
W2S = ('1.73', '2.27', '2.80')
DEGRES = (4, 5, 7)
LEV = 441 / 324
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


a92 = json.load(open(R92, encoding='utf-8'))
a92m1 = json.load(open(R92M1, encoding='utf-8'))
p92 = json.load(open(P92, encoding='utf-8'))
p91 = json.load(open(P91, encoding='utf-8'))

out('CE QUI BORNE A(w2) APRES LE DELTA 92 -- machine 2')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out('runs lus : 92 BOCAL4 %s ; 92 machine 1 %s ; 91 (par ma repetition) %s'
    % (B(R92), B(R92M1), B(P91)))

# ---------------------------------------------------------------- Q1
out()
out('Q1. S(p) EST-ELLE LE PLANCHER ANALYTIQUE ?')
for p in DEGRES:
    D = a92['degres'][str(p)]
    rap = D['S_p'] / D['plancher_corrige']
    note('p=%d' % p, 'S(p) %.4e ; plancher corrige %.4e ; S/plancher %.2e' % (D['S_p'], D['plancher_corrige'], rap))
chk('Q1 : S(p) est QUATRE A CINQ ORDRES au-dessus du plancher analytique, aux trois degres',
    all(1e4 <= a92['degres'][str(p)]['S_p'] / a92['degres'][str(p)]['plancher_corrige'] <= 1e6 for p in DEGRES))
note('Q1 conclusion', 'ce qui borne la lecture n est donc PAS le terme analytique suivant. '
     'Descendre delta\' ne touche pas a ce qui domine : le plancher est deja hors jeu.')

# ---------------------------------------------------------------- Q2
out()
out('Q2. LA DISPERSION EST-ELLE STRUCTUREE EN w2 -- EST-CE DEJA A(w2) ?')
rapports = {}
for p in DEGRES:
    ec = a92['degres'][str(p)]['ecarts_corriges']
    moys, intra = [], []
    for w in W2S:
        a, b = ec['%d|%s|1.05' % (p, w)] * 1e9, ec['%d|%s|1.20' % (p, w)] * 1e9
        moys.append((a + b) / 2)
        intra.append(abs(a - b))
    entre, dans = max(moys) - min(moys), max(intra)
    rapports[p] = entre / dans
    note('p=%d' % p, 'etendue ENTRE w2 %.3f e-09 ; etendue INTRA w2 (l indice c) %.3f e-09 ; '
         'rapport %.2f' % (entre, dans, entre / dans))
chk('Q2 : la dispersion N EST PAS structuree en w2 -- l etendue entre w2 est PLUS PETITE que '
    'celle entre les deux c, aux trois degres', all(r < 1 for r in rapports.values()),
    str({p: '%.2f' % rapports[p] for p in DEGRES}))
note('Q2 conclusion', 'A(w2) ne se lit pas encore : ce qu on voit dans les six points est '
     'domine par l INDICE DE FENETRE c, pas par w2. Une dependance en w2 plus petite que '
     '~2e-09 resterait invisible sous cette structure.')

# ---------------------------------------------------------------- Q3
out()
out('Q3. BRUIT, OU SYSTEMATIQUE ? -- LE TEST EST LA REPRODUCTION ENTRE MACHINES')
ident, total, ecarts = 0, 0, []
for p in DEGRES:
    e2 = a92['degres'][str(p)]['ecarts_corriges']
    e1 = a92m1['degres'][str(p)]['ecarts_corriges']
    for w in W2S:
        d2 = e2['%d|%s|1.20' % (p, w)] - e2['%d|%s|1.05' % (p, w)]
        d1 = e1['%d|%s|1.20' % (p, w)] - e1['%d|%s|1.05' % (p, w)]
        total += 1
        if d2 == d1:
            ident += 1
        else:
            ecarts.append('%d|%s (%.3e)' % (p, w, abs(d2 - d1)))
        note('p=%d w2=%s' % (p, w), 'effet de c : BOCAL4 %+.3f e-09 | machine 1 %+.3f e-09%s'
             % (d2 * 1e9, d1 * 1e9, '' if d2 == d1 else '   <- differe'))
chk('Q3 : l effet de c se reproduit AU BIT entre deux machines d arithmetiques differentes, '
    '8 fois sur 9', ident == 8 and total == 9, '%d/%d identiques ; exception : %s' % (ident, total, ecarts))
note('Q3 l exception', 'elle porte sur 4|2.27, exactement la cellule du seul lnA_R qui differe '
     'entre les machines (4|2.27|1.20, 9.15e-10, cellule EXPOSEE du geste (2) selon machine 1) : '
     'l exception confirme la regle plutot qu elle ne l entame.')
note('Q3 conclusion', 'ce n est pas du bruit de chaine. C est un SYSTEMATIQUE DETERMINISTE de '
     'la composition de la fenetre d ajustement. Un systematique deterministe se modelise et '
     'se retire -- c est ce qu on a fait de c1.')

# ---------------------------------------------------------------- Q4
out()
out("Q4. DEPEND-IL DE delta' ? -- AUTREMENT DIT, UN PLUS GRAND n LE REDUIRAIT-IL ?")
A, Bp = p92['lnA_R']['II'], p91['lnA_R']['II']
tab = {}
for p in DEGRES:
    for w in W2S:
        d18 = (A['%d|%s|1.20' % (p, w)] - A['%d|%s|1.05' % (p, w)]) * 1e9
        d21 = (Bp['%d|%s|1.20' % (p, w)] - Bp['%d|%s|1.05' % (p, w)]) * 1e9
        tab[(p, w)] = (d18, d21, (d18 / d21) if d21 else float('nan'))
        note('p=%d w2=%s' % (p, w), "effet de c sur l ajustement II : n=18 %+.3f e-09 ; "
             "n=21 %+.3f e-09 ; rapport %.3f" % (d18, d21, tab[(p, w)][2]))
gros = [abs(tab[(7, w)][0]) for w in W2S]
petits = [abs(tab[(p, w)][0]) for p in (4, 5) for w in W2S]
# Enonce d'apres la mesure, pas d'apres l'impression : le facteur va de 17 (le plus petit
# p=7 contre le plus grand p=4/5) a 600 (l'inverse). "Deux ordres" etait trop rond, et ce
# controle-ci a mordu sur ma propre formulation avant qu'elle ne parte.
chk('Q4a : sur l ajustement II, l effet de c a p = 7 est de 17 a 600 fois celui de p = 4 et 5',
    15 <= min(gros) / max(petits) and max(gros) / min(petits) >= 100,
    'p=7 : %.0f a %.0f e-09 ; p=4,5 : %.1f a %.1f e-09 ; facteur %.0f a %.0f'
    % (min(gros), max(gros), min(petits), max(petits),
       min(gros) / max(petits), max(gros) / min(petits)))
r7 = [tab[(7, w)][2] for w in W2S]
chk("Q4b : a p = 7 le rapport n=18/n=21 est de l ordre du levier (%.3f) : l effet y suit delta'"
    % LEV, all(0.7 * LEV <= r <= 1.4 * LEV for r in r7), str(['%.3f' % r for r in r7]))
r45 = [tab[(p, w)][2] for p in (4, 5) for w in W2S]
chk("Q4c : a p = 4 et 5 le rapport est ERRATIQUE (signes opposes, valeurs hors echelle) : "
    "l effet n y suit PAS delta'", not all(0.5 * LEV <= r <= 2 * LEV for r in r45),
    str(['%.2f' % r for r in r45]))
note('Q4 conclusion', "a p = 7 l effet de fenetre suit delta' et un plus grand n le reduirait ; "
     "a p = 4 et 5, la ou il borne DEJA la lecture corrigee, il ne le suit pas. "
     "RESERVE : la lecture corrigee n existe pas au 91 (deux niveaux, pas trois), "
     "la comparaison n=18/n=21 porte donc sur l ajustement II, pas sur M1/M2.")

# ---------------------------------------------------------------- CE QUE M2 RETIRE A p = 7
out()
out('CE QUE LE MODE LIBRE RETIRE DEJA, A p = 7')
for w in W2S:
    ii = abs(tab[(7, w)][0])
    ec = a92['degres']['7']['ecarts_corriges']
    m2 = abs((ec['7|%s|1.20' % w] - ec['7|%s|1.05' % w]) * 1e9)
    note('7|%s' % w, 'effet de c : %.1f e-09 sur II -> %.3f e-09 apres M2 (retire a %.1f pour cent)'
         % (ii, m2, 100 * (1 - m2 / ii)))
chk('a p = 7, M2 retire plus de 90 pour cent de l effet de fenetre',
    all(abs((a92['degres']['7']['ecarts_corriges']['7|%s|1.20' % w]
             - a92['degres']['7']['ecarts_corriges']['7|%s|1.05' % w]) * 1e9) < 0.1 * abs(tab[(7, w)][0])
        for w in W2S))
note('la piste', 'a p = 7 le modele porte un terme LIBRE (le mode, deux coefficients ajustes) et '
     'il absorbe la dependance de fenetre. A p = 4 et 5, M1 n a que c1, FIXE, et n absorbe rien : '
     'c est la que la lecture reste bornee a ~3e-09. Le gel v9 le disait de son cote ("a p = 4 '
     'et 5 le mode n apporte rien, il absorbe la troncature") -- le 92 montre que "absorber la '
     'troncature" est precisement ce dont la mesure de A a besoin.')

# ---------------------------------------------------------------- BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'rapport_entre_w2_sur_intra_c': {str(p): rapports[p] for p in DEGRES},
          'effet_c_reproduit_au_bit': '%d/%d' % (ident, total),
          'effet_c_n18_n21': {'%d|%s' % k: v for k, v in tab.items()},
          'portee': 'mesure sur les runs deja deposes ; aucun run neuf ; ne mesure pas A'}
with open('ce_qui_borne_A_machine2_v1.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1)
with open('ce_qui_borne_A_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('ce_qui_borne_A_machine2_v1.log'))
