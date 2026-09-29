"""controle_erratum_proj4_machine2_v1.py -- machine 2, 2026-09-29.

CONTROLE DES DEUX AFFIRMATIONS VERIFIABLES du lot machine 1 802a84bb706b6124 (erratum E-v9-1 et
cloture de la dette proj4), avant contreseing. Rien n'est cru sur parole :
  1. la CAUSE que l'erratum allegue est cherchee dans le journal lui-meme (deux lignes "bilan",
     le motif a pris la premiere) -- et dans MON journal, pour etablir si c'est une propriete de
     l'instrument ou un accident de sa machine ;
  2. le REJEU de ma derivation du plancher corrige est diffe ligne a ligne contre mon propre log :
     l'affirmation est "identique sauf la ligne de plateforme", elle se mesure ;
  3. les neuf proj4 et les six planchers sont confrontes valeur par valeur ;
  4. ce que l'erratum promet de NE PAS toucher est verifie intact (les quatre canons).
Deux verbes : chk (peut mordre), note (ne peut pas). E19 : aucun run joue.
"""
import hashlib
import os
import re
import sys
import unicodedata

ERR = 'ERRATUM_manifeste_lot_gel_v9_banc_v15_machine1_v1.md'
NOTE_M1 = 'note_machine1_reponse_certification_v9_v15_v1.md'
LOG_M1 = 'm1_rejeu_derivation_plancher_corrige_v3.log'
LOG_M2 = 'derivation_plancher_corrige_machine2_v3.log'
BANC_M1, BANC_M2 = 'm1_v15_banc.log', 'm2_v15_banc.log'
CANON = {'constante_A_pre_enregistrement_v9.md': 'b515abc5a6da73c5',
         'banc_qualification_machine1_v15.py': 'a1553f6eb5cc74b8',
         'constante_A_pre_enregistrement_v8.md': '800fc6a9a8e56e49',
         'banc_qualification_machine1_v14.py': 'dc91676c640d4323',
         'derivation_plancher_corrige_machine2_v3.json': '3b12117a58dde698',
         'note_machine1_gel_v9_banc_v15_v1.md': '630be06efa686b38'}
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


def lire(p):
    return open(p, encoding='utf-8', errors='replace').read()


def plat(p):
    """texte a blancs normalises et en minuscules : les pieces sont repliees a 72 colonnes,
    une phrase y est coupee par un retour a la ligne et commence par une majuscule."""
    return ' '.join(lire(p).split()).lower()


out('CONTROLE MACHINE 2 DE L ERRATUM E-v9-1 ET DE LA CLOTURE DE LA DETTE proj4')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out()
out('0. LES PIECES DU LOT ENTRANT')
for f, c in (('erratum', ERR), ('note de reponse', NOTE_M1), ('rejeu proj4', LOG_M1)):
    chk('0 %s present' % f, os.path.isfile(c), B(c) if os.path.isfile(c) else 'absent')

# ---------------------------------------------------------------- 1. LA CAUSE ALLEGUEE
out()
out('1. E-v9-1 : LA CAUSE QUE L ERRATUM ALLEGUE, CHERCHEE DANS LE JOURNAL')
terr = lire(ERR)
chk('1.1 : l erratum dit bien que le VRAI compte du banc est 58/58',
    '58/58' in terr and '103/103' in terr)
bl1 = re.findall(r'bilan (\d+/\d+)', lire(BANC_M1))
bl2 = re.findall(r'bilan (\d+/\d+)', lire(BANC_M2))
chk('1.2 : son journal du banc porte bien DEUX lignes "bilan", dans cet ordre',
    bl1 == ['103/103', '58/58'], str(bl1))
note('1.2 la cause est donc exacte', 'un motif "bilan N/N" non ancre prend la PREMIERE : celle du '
     'selftest que le banc rejoue avant ses scenarios. C est ce qu elle decrit.')
chk('1.3 : MON journal du banc a la MEME structure -- c est une propriete de l instrument, '
    'pas un accident de sa machine', bl2 == bl1, 'moi %s | elle %s' % (bl2, bl1))
sc1 = re.findall(r'bilan (\d+/\d+) scenarios mordent', lire(BANC_M1))
sc2 = re.findall(r'bilan (\d+/\d+) scenarios mordent', lire(BANC_M2))
chk('1.4 : le motif ANCRE ("scenarios mordent") rend 58/58 des deux cotes, sans ambiguite',
    sc1 == sc2 == ['58/58'], 'moi %s | elle %s' % (sc2, sc1))
chk('1.5 : l erratum cite la ligne qui porte le vrai compte ([0447])', '0447' in terr)
perr = plat(ERR)
chk('1.6 : l erratum declare que sa portee est nulle et qu aucun canon ne bouge',
    'aucun canon ne bouge' in perr and 'portee : aucune' in perr)

# ---------------------------------------------------------------- 2. LE REJEU DE MA DERIVATION
out()
out('2. LA DETTE proj4 : SON REJEU DE MA DERIVATION, DIFFE LIGNE A LIGNE')
a, b = lire(LOG_M2).splitlines(), lire(LOG_M1).splitlines()
chk('2.1 : les deux journaux ont le meme nombre de lignes', len(a) == len(b),
    'moi %d | elle %d' % (len(a), len(b)))
diff = [(i + 1, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
for i, x, y in diff:
    out('  [DIFF ligne %d]' % i)
    out('      moi  : %s' % x)
    out('      elle : %s' % y)
chk('2.2 : UNE SEULE ligne differe', len(diff) == 1, '%d ligne(s)' % len(diff))
platef = len(diff) == 1 and 'python' in diff[0][1] and 'python' in diff[0][2]
chk('2.3 : et cette ligne est bien la ligne de PLATEFORME', platef,
    'ligne %d' % diff[0][0] if diff else 'aucune')
if platef:
    mpm = [re.search(r'mpmath ([\d.]+)', s) for s in (diff[0][1], diff[0][2])]
    chk('2.4 : mpmath est la MEME version des deux cotes (la precision etendue ne change pas)',
        all(mpm) and mpm[0].group(1) == mpm[1].group(1),
        'moi %s | elle %s' % (mpm[0].group(1) if mpm[0] else '?', mpm[1].group(1) if mpm[1] else '?'))
for nom, t in (('moi', lire(LOG_M2)), ('elle', lire(LOG_M1))):
    m = re.search(r'BILAN : (\d+) controles, (\d+) mordent (\[.*\])', t)
    note('2.5 bilan %s' % nom, m.group(0)[:130] if m else 'introuvable')
m2b = re.search(r'BILAN : (\d+) controles, (\d+) mordent (\[.*\])', lire(LOG_M2))
m1b = re.search(r'BILAN : (\d+) controles, (\d+) mordent (\[.*\])', lire(LOG_M1))
chk('2.6 : meme bilan, et la SEULE morsure est la meme (C1, la reserve sur proj2)',
    m2b and m1b and m2b.group(0) == m1b.group(0) and 'C1' in m2b.group(3))
note('2.6 portee de C1', 'mon outil rend proj2 = 0.655-0.660 quand l instrument rend 0.6727 : '
     '2.6 pour cent, de composition de fenetre. La reserve mord chez elle comme chez moi -- elle '
     'est donc REPRODUITE, pas seulement declaree. Sans portee devant quatre ordres.')

# ---------------------------------------------------------------- 3. LES VALEURS
out()
out('3. LES NEUF proj4 ET LES SIX PLANCHERS, VALEUR PAR VALEUR')
RGP = re.compile(r'C2c (\d\|[\d.]+) -- terme tau\^4 : biais ([\d.e+-]+) ; c2 tau_dom\^4 ([\d.e+-]+) ; proj4 = ([\d.]+)')
p2, p1 = dict((m[0], m[1:]) for m in RGP.findall(lire(LOG_M2))), dict((m[0], m[1:]) for m in RGP.findall(lire(LOG_M1)))
chk('3.1 : les neuf points sont presents des deux cotes', len(p2) == len(p1) == 9,
    'moi %d | elle %d' % (len(p2), len(p1)))
chk('3.2 : les neuf (biais, c2 tau^4, proj4) coincident AU CHIFFRE IMPRIME', p2 == p1,
    'points en ecart : %s' % [k for k in p2 if p2.get(k) != p1.get(k)])
vals = sorted(set(v[2] for v in p2.values()))
chk('3.3 : proj4 ne prend que les deux valeurs qu elle cite (0.219452 et 0.223764)',
    vals == ['0.219452', '0.223764'], str(vals))
chk('3.4 : et elles encadrent bien l intervalle que MA prescription annoncait (0.2195 a 0.2238)',
    abs(float(vals[0]) - 0.2195) < 5e-5 and abs(float(vals[1]) - 0.2238) < 5e-5, str(vals))
RGPL = re.compile(r'p=(\d) n = (\d+) -- plancher CORRIGE ([\d.e+-]+)')
l2, l1 = RGPL.findall(lire(LOG_M2)), RGPL.findall(lire(LOG_M1))
chk('3.5 : les six planchers corriges (n = 18 et n = 21) coincident au chiffre',
    l2 == l1 and len(l2) == 6, '%d de chaque cote' % len(l2))
note('3.6 planchers du log', str({'p=%s n=%s' % (p, n): v for p, n, v in l2}))
note('3.7 portee', 'le log rend le plancher par w2 = 1.73 avec son proj4 propre (5.0940e-14 a '
     'p=4, n=18) ; le gel 7bis prend la BORNE HAUTE 0.2238 sur le max en w2 (5.1949e-14). '
     'Le rapport 1.0198 == 0.223764/0.219452 : les deux se deduisent l un de l autre, rien ne cloche.')
note('3.8 ce qui N EST PAS verifie directement', 'elle affirme que son JSON de sortie est '
     'IDENTIQUE AU BIT a mon 3b12117a58dde698, mais elle n a PAS joint le JSON. Je verifie le '
     'log, qui porte tous les nombres qui entrent dans ce JSON : l identite du JSON est donc '
     'etablie INDIRECTEMENT, et je l ecris ainsi plutot que de la donner pour mesuree.')

# ---------------------------------------------------------------- 4. CE QUI NE DOIT PAS AVOIR BOUGE
out()
out('4. CE QUE L ERRATUM PROMET DE NE PAS TOUCHER')
for f, c in sorted(CANON.items()):
    chk('4 %s intact' % f, os.path.isfile(f) and B(f) == c, B(f) if os.path.isfile(f) else 'absent')
tn = lire(NOTE_M1)
chk('4.7 : elle reconnait que la ligne de 7bis qui declare la dette est PERIMEE',
    'perimee' in plat(NOTE_M1))
chk('4.8 : et qu elle ne peut PAS l editer dans le v9 certifie (PB-1)',
    'pb-1' in plat(NOTE_M1) and 'prochaine version' in plat(NOTE_M1))
pnote = plat(NOTE_M1).replace(chr(39), ' ')
chk('4.9 : la consigne --base est prise comme CONSIGNE, sans modifier la feuille',
    'la feuille n est pas modifiee' in pnote)

# ---------------------------------------------------------------- BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
with open('controle_erratum_proj4_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('controle_erratum_proj4_machine2_v1.log'))
