# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'rectification de ma morsure C07' -- manifeste + ZIP. 2026-11-15. Derive de fabrique_lot_contreseing_acte_EB_ter_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_rectification_C07_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le journal de la rectification LU (344 flottants, 7.188730e-15 a C2 rang 3 plateau B, 7.391657e-15 a L4 rang 2 plateau C, 7.216450e-15 en
flottants a M3 rang 6 plateau C, conclusion : les deux phrases de l'acte TIENNENT) ; le lot scelle e8ff4d600edf89ef RELU (canon recalcule de son manifeste) ; le canon de CHAQUE piece
nomme dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-15_rectification_C07_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_rectification_C07_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_rectification_C07_machine2_v1.md'
SELF = 'fabrique_lot_rectification_C07_machine2_v1.py'
D = 'acte_EB_ter_contreseing/'
R = 'rectification_C07_fractions_exactes_machine2_v1'
PIECES = [D + R + '.py', D + R + '.log', SELF]
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


for p in PIECES + [NOTE, 'MANIFEST_lot_machine2_contreseing_acte_EB_ter_v1.txt']:
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
lg = lit(D + R + '.log')
for x in ('flottants differents : 344', '7.188730e-15', "['points', 'C2', 'etats', 3, 'plateaux', 'B', 'Gamma_pl']", '7.391657e-15', "['points', 'L4', 'etats', 2, 'plateaux', 'C', 'ecart_ln_A']",
          '7.216450e-15', "['points', 'M3', 'etats', 6, 'plateaux', 'C', 'Gamma_pl']", '7.179758e-15', '7.105427e-15',
          'CONCLUSION : "7.2e-15 au plus" (relatif) TIENT ; "7.4e-15 au plus" (absolu) TIENT'):
    if x not in lg:
        arrets.append('journal de la rectification : %r absent' % x)
for x in ('7.188730e-15', '7.391657e-15', '7.216450e-15', '7.179758e-15', '7.105', '65 * 2^-53', '4.270038719466424e-12', '4.2700387194663935e-12', 'e8ff4d600edf89ef', 'RETIREE', 'C12',
          'quatre', '17 autres', 'ouvre', 'go'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
mp = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_EB_ter_v1.txt')
if emp(open(mp, 'rb').read())[0] != 'e8ff4d600edf89ef':
    arrets.append('le lot scelle e8ff4d600edf89ef n a plus ce canon')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- RECTIFICATION DE MACHINE 2 : MA MORSURE C07 DU CONTRESEING e8ff4d600edf89ef EST RETIREE (calcul en fractions exactes : l ecart relatif maximal est 7.188730e-15, '
    'a C2 rang 3 plateau B, l ecart absolu maximal 7.391657e-15 ; "7.2e-15 au plus" et "7.4e-15 au plus" de l acte tiennent). Il reste une morsure d ecriture vraie, C12. '
    'Le lot e8ff4d600edf89ef est scelle et n est pas edite. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : mon contreseing e8ff4d600edf89ef ; acte 751165a3eee613d9 ; lot de machine 1 26b3912297b31713 ; message de machine 1 du 15/11 (contestation de C07)\n')
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
