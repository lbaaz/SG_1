# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn de la qualification E-B bis, projet v2' -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_contreseing_acte_nn_EB_bis_v2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan de la verification sur la v2 LU dans son JSON (34 controles, 5 morsures, les cinq que
la note annonce) ; le journal du diff (reconstruction == v2, 8 blocs, 9 otees, 28 posees, six canons nouveaux) ; les six canons et les
dates lus dans le journal des controles ; les valeurs d'O-BIS-2 retrouvees dans mes journaux et dans la note de machine 1 ; les canons de
l'acte v2 et du lot de machine 1 RECALCULES depuis son zip ; les canons de CHAQUE piece nommes dans la note ; note ASCII ; le manifeste ne
se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'acte_v2_contreseing/'
NOM = 'lot_machine2_2026-11-14_contreseing_acte_nn_EB_bis_v2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_nn_EB_bis_v2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_qualification_EB_bis_v2_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_nn_EB_bis_v2_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-13_acte_qualification_EB_bis_v2_recu.zip'
V = 'verification_acte_nn_qualification_EB_bis_machine2_v1_sur_v2'
PIECES = [D + x for x in ('controle_diff_v2_machine2_v1.py', 'controle_diff_v2_machine2_v1.log', 'fait_zip_v2_en_forme_v1_machine2_v1.py',
                          V + '.log', V + '.json', 'controles_v2_machine2_v1.py', 'controles_v2_machine2_v1.log')] + [SELF]
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


for p in PIECES + [NOTE, LOT_M1]:
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
mord = sorted(c['id'] for c in v['controles'] if not c['ok'])
if len(v['controles']) != 34 or mord != ['C01', 'C02', 'C04', 'C05', 'C34'] or v['bilan']['mord'] != 5:
    arrets.append('verification sur la v2 : %d controles, mordent %s (attendu 34, C01 C02 C04 C05 C34)' % (len(v['controles']), mord))
for x in ('34 controles de la v1', '29 qui tiennent et 5 qui mordent', 'C03 et C06 a C33'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
dl = lit(D + 'controle_diff_v2_machine2_v1.log')
for x in ('resultat == v2 : True ; contexte coherent : True', 'mon diff : 8 blocs ; lignes otees 9, posees 28', 'application du diff de m1 a la v1 : 7 blocs',
          'lignes posees : 28 ; non ASCII 0 ; > 100 col 0 ; avec % 0', "nouvelles ['05f8eed219631f63', '2b211d51fb8eb3f0', 'c396a00095a0b9e3', "
          "'df01461fc9b2b099', 'e58d01567a46b86a', 'ff93d708547f8ec0'] ; disparues []", 'v2 bdf8c5a0c73096a4 (attendu bdf8c5a0c73096a4)'):
    if x not in dl:
        arrets.append('journal du diff : %r absent' % x)
cl = lit(D + 'controles_v2_machine2_v1.log')
if len(re.findall(r'-> TIENT', cl)) != 6 or '-> MORD' in cl:
    arrets.append('les six canons nouveaux ne tiennent pas tous dans le journal des controles')
for x in ('09:45', '09:48', '10:33', '10:59', '19:35', '08:57', '"(e)crite pendant le run" : True', '"Ne contient rien du run" : True'):
    if x not in cl:
        arrets.append('journal des controles : %r absent' % x)
for x in ('08:57', '09:45', '09:48', '10:33', '10:59', '19:35', 'def35e82df8b2e68'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_raw = open(os.path.join(ICI, 'MANIFEST_lot_machine1_acte_qualification_EB_bis_v2.txt'), 'rb').read()
canons = {'acte v2': (emp(zl.read('journal_delta_nn_qualification_EB_bis_v2.md'))[0], 'bdf8c5a0c73096a4'),
          'lot de machine 1': (emp(man_raw)[0], '1af62634ba0068b6'), 'v1': (emp(zl.read('journal_delta_nn_qualification_EB_bis_v1.md'))[0], 'c396a00095a0b9e3'),
          'diff': (emp(zl.read('journal_delta_nn_qualification_EB_bis_v1_vers_v2.diff'))[0], '7a6e82e462d67e99')}
for nom, (got, att) in canons.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if nom != 'diff' and att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
e1 = open(os.path.join(ICI, 'experience_O_BIS_2', 'experience_O_BIS_2.log'), encoding='ascii').read()
e2 = open(os.path.join(ICI, 'experience_O_BIS_2', 'experience_O_BIS_2_threads.log'), encoding='ascii').read()
for val, lieu in (('5.398020792141e-10', e1), ('5.378534999046e-10', e2), ('5.366965337872e-10', e2)):
    if val not in lieu or val not in note:
        arrets.append('valeur %s absente de son journal ou de la note' % val)
nm1 = zl.read('POUR_MACHINE2_acte_qualification_EB_bis_v2_machine1_v1.md').decode('utf-8')
for val in ('5.39802079214111e-10', '5.378534999046463e-10'):
    if val not in nm1 or val not in note:
        arrets.append('valeur %s absente de la note de machine 1 ou de la mienne' % val)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 DE L ACTE nn DE LA QUALIFICATION E-B BIS, PROJET v2 (bdf8c5a0c73096a4, lot de machine 1 '
    '1af62634ba0068b6), SUR SON DIFF. La v2 == la v1 + le diff, a l octet ; 34 controles de la v1 rejoues sur la v2 : 29 tiennent, 5 mordent, '
    'les cinq que la v2 change. CONTRESIGNE ; une reserve non bloquante (R-4, nn.4). machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte v2 bdf8c5a0c73096a4 ; lot de machine 1 1af62634ba0068b6 ; mon contreseing de la v1 05f8eed219631f63\n')
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
