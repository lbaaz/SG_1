# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn du run du gel E-B ter, projet v1' -- manifeste + ZIP. 2026-11-15. Derive de fabrique_lot_contreseing_acte_ordre2_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_contreseing_acte_EB_ter_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan de la verification LU dans son JSON (19 controles, 2 morsures : C07 et C12) ; le bilan du PREMIER PASSAGE lu dans son JSON (5 morsures : C07, C11,
C12, C15, C16 ; les trois dernieres etaient les miennes) ; le bilan de la contre-epreuve LU dans son JSON (18 morsures : tous les controles sauf C04) ; les canons de l'acte, du lot de machine 1, de
son verdict rejoue et du mien RECALCULES depuis les fichiers ; les canons de CHAQUE piece nommes dans la note ; les chiffres cles de la note relus dans mes journaux ; note ASCII ; le manifeste ne se
porte pas lui-meme ; l'en-tete du manifeste porte le canon de l'acte ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'acte_EB_ter_contreseing/'
NOM = 'lot_machine2_2026-11-15_contreseing_acte_EB_ter_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_EB_ter_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_EB_ter_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_EB_ter_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-15_acte_EB_ter_v1_recu.zip'
V = 'verification_acte_EB_ter_machine2_v1'
PIECES = [D + x for x in (V + '.py', V + '.log', V + '.json', V + '_premier_jet.py', V + '_premier_passage.log', V + '_premier_passage.json',
                          'mutation_acte_EB_ter_contre_epreuve_machine2_v1.py', V + '_sur_acte_mute.log', V + '_sur_acte_mute.json')] + [SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read()


for p in PIECES + [NOTE, LOT_M1, 'MANIFEST_lot_machine1_acte_EB_ter_v1.txt', 'run_EB_ter/verdict_ter.json']:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
nn = re.sub(r'\s+', ' ', note)
v = json.load(open(os.path.join(ICI, D + V + '.json'), encoding='ascii'))
if len(v['controles']) != 19 or v['bilan']['ids'] != ['C07', 'C12'] or v['canon'] != '751165a3eee613d9':
    arrets.append('verification sur l acte : %d controles, mordent %s (attendu 19, C07 et C12) ; canon %s' % (len(v['controles']), v['bilan']['ids'], v['canon']))
p1 = json.load(open(os.path.join(ICI, D + V + '_premier_passage.json'), encoding='ascii'))
if len(p1['controles']) != 19 or p1['bilan']['ids'] != ['C07', 'C11', 'C12', 'C15', 'C16']:
    arrets.append('premier passage : %d controles, mordent %s (attendu 19 et C07 C11 C12 C15 C16)' % (len(p1['controles']), p1['bilan']['ids']))
m = json.load(open(os.path.join(ICI, D + V + '_sur_acte_mute.json'), encoding='ascii'))
vises = {'C03', 'C06', 'C08', 'C09', 'C10', 'C11', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19'}
tous = {'C%02d' % i for i in range(1, 20)}
mord = set(m['bilan']['ids'])
if len(m['controles']) != 19 or m['bilan']['mord'] != 18 or not vises <= mord or mord != tous - {'C04'}:
    arrets.append('contre-epreuve : %d mordent %s (attendu 18 : tous sauf C04, dont les 13 vises)' % (m['bilan']['mord'], sorted(mord)))
if m['canon'] == '751165a3eee613d9':
    arrets.append('la copie mutee a le canon de l acte : la contre-epreuve ne mute rien')
for x in ('19 controles recalcules', '17 tiennent, 2 mordent', '28 chiffres ou mots', '18 morsures, dont les 13', '7.216e-15', '7.3e-15', '0.0416', '0.0410', '0.0006', '45860.5', '125', '124',
          '1.019e-13', '8.44e-15', 'b5616dcf858e8801', '9.773e-12', '0.656987', '1.0025', '1.0554', '1.28 a 30.93', '1.598e-12', '2.247e-04', '2cd1f84efa02f2ab', 'ba1d309291033d97',
          'premier jet', 'CONTRESIGNE TEL QUEL', 'ouvre'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
vl = lit(D + V + '.log')
for x in ('BILAN : 19 controles, 2 mordent [\'C07\', \'C12\']', 'C09 TIENT', '1392 lectures du rejeu', 'plus grand ecart relatif de largeur 1.019e-13', 'plus grand ecart d energie 8.44e-15',
          '344 flottants sur 1828', '7.216e-15', 'a 124 (le chiffre de l acte)', 'a 125 (L3 rang 5', 'residu relatif max 9.773e-12', 'poids au site min 0.656987', '45860.5 s',
          'plus plats par le plus grand : [True, True, True, False]', 'b5616dcf858e8801', 'tete publique du registre 8d54bf9, plafond 98'):
    if x not in vl:
        arrets.append('journal de la verification : %r absent' % x)
pl = lit(D + V + '_premier_passage.log')
if "BILAN : 19 controles, 5 mordent ['C07', 'C11', 'C12', 'C15', 'C16']" not in pl:
    arrets.append('journal du premier passage : bilan attendu absent')
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_raw = open(os.path.join(ICI, 'MANIFEST_lot_machine1_acte_EB_ter_v1.txt'), 'rb').read()
canons = {'acte': (emp(zl.read('journal_delta_nn_qualification_EB_ter_v1.md'))[0], '751165a3eee613d9'), 'lot de machine 1': (emp(man_raw)[0], '26b3912297b31713'),
          'verdict rejoue par machine 1': (emp(zl.read('verdict_ter_rejoue_machine1.json'))[0], 'ba1d309291033d97'),
          'mon verdict': (emp(open(os.path.join(ICI, 'run_EB_ter/verdict_ter.json'), 'rb').read())[0], '2cd1f84efa02f2ab')}
for nom, (got, att) in canons.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 DE L ACTE nn DU RUN DU GEL E-B TER, PROJET v1 (751165a3eee613d9, lot de machine 1 26b3912297b31713). 19 controles recalcules '
    'de mes sources, deux morsures d ecriture sans consequence (C07 : 7.2e-15 pour 7.216e-15 ; C12 : "plus plats" faux pour D, 0.0416 contre 0.0410) ; trois autres, les miennes, '
    'corrigees avant de conclure (premier jet et premier passage joints) ; contre-epreuve sur une copie mutee : 18 morsures, dont les 13 controles vises. CONTRESIGNE TEL QUEL ; '
    'aucune v2 demandee. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte 751165a3eee613d9 ; lot de machine 1 26b3912297b31713 ; mes lots d2f50caa808cfb1c (certification), 1f057651c8f69eb6 (resultat), c8164e6d80ee0b60 et 29073aa2ac4decac (hors chaine)\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
