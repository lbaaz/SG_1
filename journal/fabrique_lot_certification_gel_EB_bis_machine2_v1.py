# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel E-B bis v1 et de son instrument' -- manifeste + ZIP. 2026-11-13.
Usage : python -P fabrique_lot_certification_gel_EB_bis_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan LU dans le JSON de l'audit (jamais tape), 0 morsure, == le compte
annonce dans la note ET dans le journal ; les canons des pieces cles RECALCULES et nommes dans la note ; les canons du gel,
de la sonde v3, de la feuille v2, du banc v3 et du lot de machine 1 RECALCULES depuis son zip et nommes ; le manifeste ne
se porte pas lui-meme ; ZIP relu bit-identique."""
import glob
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
A = 'audit_gel_EB_bis_sortie/'
NOM = 'lot_machine2_2026-11-13_certification_gel_EB_bis_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_EB_bis_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_EB_bis_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_EB_bis_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-13_gel_EB_bis_v1_recu.zip'
cles = ['audit_gel_EB_bis_machine2_v1.py', A + 'audit_gel_EB_bis_machine2_v1.log', A + 'audit_gel_EB_bis_machine2_v1.json',
        'nuit_EB_bis/lancer_nuit_EB_bis_machine2_v1.py']
autres = sorted(os.path.relpath(p, ICI).replace(os.sep, '/') for p in
                glob.glob(os.path.join(ICI, A, 'm2_*.log')) + [os.path.join(ICI, A, f) for f in (
                    'cas_bord_fort.py', 'd2_portes_v3.py', 'feuille_v2_bornes_anciennes.py', 'sonde_etage1_passage1.json')])
PIECES = [NOTE] + cles + autres + [SELF]
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
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
cj = json.load(open(os.path.join(ICI, A, 'audit_gel_EB_bis_machine2_v1.json'), encoding='ascii'))
NCHK, NMORD, NOMS = cj['bilan']['chk'], cj['bilan']['mord'], cj['bilan']['noms']
if NMORD != len(NOMS) or NCHK != len(cj['controles']):
    arrets.append('bilan incoherent dans le JSON')
if NMORD != 0:
    arrets.append('la note annonce 0 morsure ; le JSON en porte %d : %s' % (NMORD, NOMS))
if ('%d controles, %d morsure' % (NCHK, NMORD)) not in note:
    arrets.append('la note n annonce pas "%d controles, %d morsure"' % (NCHK, NMORD))
log = open(os.path.join(ICI, A, 'audit_gel_EB_bis_machine2_v1.log'), encoding='ascii').read()
if ('BILAN : %d controles, %d mordent' % (NCHK, NMORD)) not in log:
    arrets.append('le journal ne porte pas le meme bilan')
for p in cles:
    c = emp(open(os.path.join(ICI, p), 'rb').read())[0]
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, p))
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_m1 = [n for n in zl.namelist() if n.startswith('MANIFEST_')]
canons = {'gel bis': (emp(zl.read('qualification_EB_bis_pre_enregistrement_v1.md'))[0], 'dcda1611adf5f8fd'),
          'sonde v3': (emp(zl.read('sonde_qualification_EB_machine1_v3.py'))[0], '555146abd2192f79'),
          'feuille v2': (emp(zl.read('lecture_qualification_EB_machine1_v2.py'))[0], 'c14dafffc5f84c97'),
          'banc v3': (emp(zl.read('banc_qui_tue_qualification_EB_machine1_v3.py'))[0], '3f2ef4d35af630c2'),
          'lot de machine 1': (emp(zl.read(man_m1[0]))[0], '25276846153bacff')}
for nom, (got, att) in canons.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
if 'LE RUN EST LANCE' not in re.sub(r'\s+', ' ', note):
    arrets.append('la note n annonce pas le lancement')
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION DE MACHINE 2 DU GEL E-B BIS v1 (dcda1611adf5f8fd) ET DE SON INSTRUMENT : sonde v3 '
    '555146abd2192f79, feuille v2 c14dafffc5f84c97, banc v3 3f2ef4d35af630c2 (lot de machine 1 25276846153bacff). '
    'VERIFICATION : %d controles, %d morsure. CERTIFIE. Run reel lance le 13/11 a 00h52 sous cette certification et le feu '
    'vert ecrit de l operateur ; resultats dans un lot a part. machine 2, classe B\n' % (NOM, NCHK, NMORD),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel bis dcda1611adf5f8fd ; lot de machine 1 25276846153bacff ; gel v2 cde0cd11a763f26d ; sonde v2 '
              'facc7536ba4637cb ; feuille v1 b3ac958a1a2b915b ; banc v2 4e46744fe4e8a8be ; moteur v17 82a0be882568fe0c ; '
              'registre fe10bfe\n')
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
