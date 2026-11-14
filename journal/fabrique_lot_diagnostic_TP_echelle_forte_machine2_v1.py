# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'diagnostic du temoin positif a barreaux plus forts' -- manifeste + ZIP. 2026-11-13.
Usage : python -P fabrique_lot_diagnostic_TP_echelle_forte_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le nombre de decompositions (20) et les durees LUS dans les deux JSON ; les
nombres cites dans la note (ratios, etalements, ancres, plus longues suites) RELUS dans le journal d'analyse, jamais
tapes ; les canons de CHAQUE piece RECALCULES et ceux des entrants nommes dans la note ; le manifeste ne se porte pas
lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'diagnostic_TP_echelle_forte'
NOM = 'lot_machine2_2026-11-13_diagnostic_TP_echelle_forte_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_diagnostic_TP_echelle_forte_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_diagnostic_TP_echelle_forte_machine2_v1.md'
SELF = 'fabrique_lot_diagnostic_TP_echelle_forte_machine2_v1.py'
PIECES = [NOTE, 'diagnostic_TP_echelle_forte_machine2_v1.py', 'analyse_diagnostic_TP_echelle_forte_machine2_v1.py',
          D + '/diag_G20.json', D + '/diag_G20.log', D + '/diag_G30.json', D + '/diag_G30.log',
          D + '/analyse_diagnostic_TP_echelle_forte_machine2_v1.log', SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


for p in PIECES:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = open(os.path.join(ICI, NOTE), encoding='utf-8').read()
nn = re.sub(r'\s+', ' ', note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
d20 = json.load(open(os.path.join(ICI, D, 'diag_G20.json')))
d30 = json.load(open(os.path.join(ICI, D, 'diag_G30.json')))
if len(d20) + len(d30) != 20:
    arrets.append('%d decompositions lues, la note en annonce vingt' % (len(d20) + len(d30)))
if 'Vingt decompositions' not in note:
    arrets.append('la note n annonce pas vingt decompositions')
m20 = sum(r['duree_s'] for r in d20) / len(d20)
m30 = sum(r['duree_s'] for r in d30) / len(d30)
if not ('%d s en moyenne a N = 60, %d s a N = 70' % (round(m20), round(m30))) in nn:
    arrets.append('durees moyennes de la note != celles des JSON (%.1f, %.1f)' % (m20, m30))
if min(r['recouvrement'] for r in d20 + d30) < 0.9998 or any(r['k'] > -2 for r in d20 + d30):
    arrets.append('recouvrements ou barreaux inattendus dans les JSON')
log = open(os.path.join(ICI, D, 'analyse_diagnostic_TP_echelle_forte_machine2_v1.log'), encoding='ascii').read()
# les nombres de la note, relus dans le journal d'analyse
att = ['8 valeurs, k = -6 a 1, etalement 0.0397', '7 valeurs, k = -6 a 0, etalement 0.0096',
       '9 valeurs, k = -6 a 2, etalement 0.0307', '9 valeurs, k = -6 a 2, etalement 0.0347',
       'PLATEAU k0 = -6 etalement 0.0034', 'PLATEAU k0 = -6 etalement 0.0008', 'PLATEAU k0 = -4 etalement 0.0067',
       'PLATEAU k0 = -4 etalement 0.0005', 'diagnostic / sonde - 1 = +2.28e-04', 'diagnostic / sonde - 1 = -1.06e-04',
       'diagnostic / sonde - 1 = -3.61e-03', 'diagnostic / sonde - 1 = +6.40e-05']
for a in att:
    if a not in log:
        arrets.append('le journal d analyse ne porte pas : %s' % a)
for a in ('etalement 0.0397', 'etalement 0.0096', '0.0307', '0.0347', '0.0034', '0.0008', '0.0067', '0.0005', '+2.3e-04',
          '-1.1e-04', '-3.6e-03', '+6.4e-05'):
    if a not in nn:
        arrets.append('la note ne porte pas : %s' % a)
if 'BILAN' in log:
    pass
CANONS = {}
for p in PIECES:
    if p in (NOTE, SELF):
        continue
    c = emp(open(os.path.join(ICI, p), 'rb').read())[0]
    CANONS[p] = c
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, p))
for nom, c in (('moteur', '82a0be882568fe0c'), ('liste', '69b3bab3bb8480b7'), ('table', '4d51dd58ef456fe9'),
               ('sortie de la nuit', 'ab31334aea5c444a'), ('acte v2', '569ccbd0d1adb927')):
    if c not in note:
        arrets.append('la note ne nomme pas %s %s' % (nom, c))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- DIAGNOSTIC DU TEMOIN POSITIF (JUMEAU H+ SEUL) A BARREAUX PLUS FORTS, k = -6 A -2, G20 ET G30, '
    'j = 6 ET 8 : %d decompositions, HORS GEL, NON OPPOSABLE. Resultat : le palier du temoin se prolonge du cote fort ; '
    'sur l echelle etendue le temoin tient aux quatre configurations. Aucune mesure du fantome ni de M17. '
    'machine 2, classe B\n' % (NOM, len(d20) + len(d30)),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : moteur v17 82a0be882568fe0c ; liste 69b3bab3bb8480b7 ; table 4d51dd58ef456fe9 ; sortie de la '
              'nuit ab31334aea5c444a ; acte nn v2 569ccbd0d1adb927\n')
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
