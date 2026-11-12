# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing du v2 de l'acte nn de la qualification E-B' -- manifeste + ZIP. 2026-11-12.
Usage : python -P fabrique_lot_contreseing_acte_nn_EB_machine2_v2.py
Gardes AVANT ecriture : pieces presentes ; le bilan LU dans le JSON de la verification (jamais tape) == le compte
annonce dans la note ET dans le journal, 0 morsure ; la contre-epreuve sur le v1 : son bilan et les noms des morsures
LUS dans son JSON == ceux de la note ; les canons de CHAQUE piece RECALCULES et nommes dans la note ; le canon de l'acte
v2 et celui du lot de machine 1 RECALCULES depuis leur zip et nommes ; mon lot et ma note du v1 nommes ; le manifeste ne
se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-12_contreseing_acte_nn_EB_v2'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_nn_EB_v2.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v2.md'
SELF = 'fabrique_lot_contreseing_acte_nn_EB_machine2_v2.py'
V = 'verification_acte_nn_qualification_EB_machine2_v2'
PIECES = [NOTE, V + '.py', V + '.log', V + '.json', V + '_sur_acte_v1.log', V + '_sur_acte_v1.json',
          'diff_verification_machine2_v1_v2.txt', SELF]
LOT_M1 = 'lot_machine1_2026-11-12_acte_qualification_EB_v2_recu.zip'
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


for p in PIECES + [LOT_M1]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = open(os.path.join(ICI, NOTE), encoding='utf-8').read()
cj = json.load(open(os.path.join(ICI, V + '.json'), encoding='ascii'))
NCHK, NMORD, NOMS = cj['bilan']['chk'], cj['bilan']['mord'], cj['bilan']['noms']
if NMORD != len(NOMS) or NCHK != len(cj['controles']):
    arrets.append('bilan incoherent dans le JSON')
if NMORD != 0:
    arrets.append('la note annonce 0 morsure sur le v2 ; le JSON en porte %d : %s' % (NMORD, NOMS))
if ('%d controles, %d morsure' % (NCHK, NMORD)) not in note:
    arrets.append('la note n annonce pas "%d controles, %d morsure"' % (NCHK, NMORD))
log = open(os.path.join(ICI, V + '.log'), encoding='ascii').read()
if ('BILAN : %d controles, %d mordent' % (NCHK, NMORD)) not in log:
    arrets.append('le journal ne porte pas le meme bilan')
cv = json.load(open(os.path.join(ICI, V + '_sur_acte_v1.json'), encoding='ascii'))
if cv['bilan']['noms'] != ['C26', 'C27', 'C28'] or cv['bilan']['mord'] != 3:
    arrets.append('la contre-epreuve sur le v1 devait mordre sur C26 a C28 : %s' % cv['bilan'])
if ('%d controles, %d morsures' % (cv['bilan']['chk'], cv['bilan']['mord'])) not in note:
    arrets.append('la note n annonce pas le bilan de la contre-epreuve')
lv = open(os.path.join(ICI, V + '_sur_acte_v1.log'), encoding='ascii').read()
if ('BILAN : %d controles, %d mordent' % (cv['bilan']['chk'], cv['bilan']['mord'])) not in lv:
    arrets.append('le journal de la contre-epreuve ne porte pas son bilan')
for n in ('C26', 'C27', 'C28', 'C29', 'C30'):
    if n not in note:
        arrets.append('la note ne nomme pas %s' % n)

CANONS = {}
for p in PIECES:
    if p in (NOTE, SELF):
        continue
    c = emp(open(os.path.join(ICI, p), 'rb').read())[0]
    CANONS[p] = c
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, p))
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_m1 = [n for n in zl.namelist() if n.startswith('MANIFEST_')]
acte = emp(zl.read('journal_delta_nn_qualification_EB_v2.md'))[0]
lot_m1 = emp(zl.read(man_m1[0]))[0] if len(man_m1) == 1 else None
for nom, c in (('acte v2', acte), ('lot de machine 1 v2', lot_m1), ('mon lot du v1', '33fa99640756efba'),
               ('ma note du v1', '850767f40a770f1b'), ('mon script de verification v1', '261ed59a1781d7d3'),
               ('ma note du 93', 'ec04b9e5dddee5f3'), ('le lot de ma certification de reference', '7b64b1b7d86c0591')):
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, c))
if acte != '569ccbd0d1adb927' or lot_m1 != 'd01cf16c3708f45a':
    arrets.append('canons de l acte v2 ou du lot de machine 1 differents de ceux annonces : %s %s' % (acte, lot_m1))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 SUR LE v2 DE L ACTE nn DE LA QUALIFICATION E-B (acte %s, lot de machine 1 %s). '
    'VERDICT : CONTRESIGNE. VERIFICATION : %d controles, %d morsure ; contre-epreuve sur le v1 : %d controles, %d morsures '
    '(%s, la numerotation et le compte des regles candidates). Aucun nombre mesure ne change entre le v1 et le v2. '
    'machine 2, classe B\n' % (NOM, acte, lot_m1, NCHK, NMORD, cv['bilan']['chk'], cv['bilan']['mord'],
                                ', '.join(cv['bilan']['noms'])),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte nn v2 %s ; lot de machine 1 v2 %s ; mon contreseing du v1 33fa99640756efba ; gel v2 '
              'cde0cd11a763f26d ; feuille b3ac958a1a2b915b ; moteur v17 82a0be882568fe0c ; lot de la nuit '
              '72f65ad8a898fbb5\n' % (acte, lot_m1))
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % len(PIECES))

with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in PIECES:
        attendu[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)

print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES), os.path.getsize(ZIP)))
