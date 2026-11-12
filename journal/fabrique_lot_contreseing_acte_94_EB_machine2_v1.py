# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn de la qualification E-B (projet v1)' -- manifeste + ZIP.
2026-11-12. Usage : python -P fabrique_lot_contreseing_acte_nn_EB_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan LU dans le JSON de la verification (jamais tape) == le compte
annonce dans la note ET dans le journal ; les noms des trois morsures lus dans le JSON et nommes dans la note ; le
bilan du premier jet lu dans son journal et annonce dans la note ; les canons de CHAQUE piece RECALCULES et nommes
dans la note ; le canon de l'acte et celui du lot de machine 1 RECALCULES depuis leur zip et nommes ; le lot de
certification de ma reference nomme ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-12_contreseing_acte_nn_EB_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_nn_EB_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_qualification_EB_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_nn_EB_machine2_v1.py'
V = 'verification_acte_nn_qualification_EB_machine2_v1'
PIECES = [NOTE, V + '.py', V + '.log', V + '.json', V + '_premier_jet.py', V + '_premier_jet.log', SELF]
LOT_M1 = 'lot_machine1_2026-11-12_acte_qualification_EB_v1_recu.zip'
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
if ('%d controles, %d morsures' % (NCHK, NMORD)) not in note:
    arrets.append('la note n annonce pas "%d controles, %d morsures"' % (NCHK, NMORD))
log = open(os.path.join(ICI, V + '.log'), encoding='ascii').read()
if ('BILAN : %d controles, %d mordent' % (NCHK, NMORD)) not in log:
    arrets.append('le journal ne porte pas le meme bilan')
for n in NOMS:
    if not re.search(r'\(%s\)' % n, note):
        arrets.append('la note ne renvoie pas a la morsure %s' % n)
if NOMS != ['C26', 'C27', 'C28']:
    arrets.append('la note annonce trois morsures C26 a C28 ; le JSON porte %s' % NOMS)
pj = open(os.path.join(ICI, V + '_premier_jet.log'), encoding='ascii').read()
m = re.search(r'BILAN : (\d+) controles, (\d+) mordent', pj)
if not m or ('%s controles, %s morsures' % m.groups()) not in note:
    arrets.append('la note n annonce pas le bilan du premier jet : %s' % (m.groups() if m else None))
mord_pj = sorted(set(re.findall(r'^(C\d\d) MORD', pj, re.M)))
if mord_pj != ['C06', 'C19'] or not all(c in note for c in mord_pj):
    arrets.append('morsures du premier jet : %s (la note nomme C06 et C19)' % mord_pj)

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
acte = emp(zl.read('journal_delta_nn_qualification_EB_v1.md'))[0]
lot_m1 = emp(zl.read(man_m1[0]))[0] if len(man_m1) == 1 else None
for nom, c in (('acte', acte), ('lot de machine 1', lot_m1), ('certification de ma reference', '7b64b1b7d86c0591'),
               ('note de cette certification', '0426e04ffcbcb953')):
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, c))
if acte != '0d7870ebad535303' or lot_m1 != '089c2c57b42dd4a0':
    arrets.append('canons de l acte ou du lot de machine 1 differents de ceux annonces : %s %s' % (acte, lot_m1))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 SUR L ACTE nn DE LA QUALIFICATION E-B, PROJET v1 (acte %s, lot de '
    'machine 1 %s). VERDICT : nombres et structure contresignes, texte NON contresigne en l etat, v2 demande. '
    'VERIFICATION : %d controles, %d morsures (%s, numerotation et compte des regles candidates, nn.9 / nn.10 (ii)) ; '
    'premier passage de mon script : %s controles, %s morsures, defauts du script. machine 2, classe B\n'
    % (NOM, acte, lot_m1, NCHK, NMORD, ', '.join(NOMS), m.group(1), m.group(2)),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte nn %s ; lot de machine 1 %s ; gel v2 cde0cd11a763f26d ; feuille b3ac958a1a2b915b ; '
              'moteur v17 82a0be882568fe0c ; lot de la nuit 72f65ad8a898fbb5\n' % (acte, lot_m1))
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
