# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn de la qualification E-B bis, projet v1' -- manifeste + ZIP. 2026-11-13.
Usage : python -P fabrique_lot_contreseing_acte_nn_EB_bis_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan LU dans le JSON de la verification (jamais tape) : 34 controles, 0 morsure, ==
ce que la note annonce ; la contre-epreuve LUE : 9 morsures sur 7 mutations ; le premier jet LU : 6 morsures ; les canons de
l'acte et du lot de machine 1 RECALCULES depuis son zip et nommes dans la note ; les valeurs de l'experience O-BIS-2 lues dans
les journaux et retrouvees dans la note ; les canons de CHAQUE piece recalcules et nommes dans la note ; note ASCII ; le manifeste
ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-13_contreseing_acte_nn_EB_bis_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_nn_EB_bis_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_qualification_EB_bis_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_nn_EB_bis_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-13_acte_qualification_EB_bis_v1_recu.zip'
V = 'verification_acte_nn_qualification_EB_bis_machine2_v1'
PIECES = [NOTE, V + '.py', V + '.log', V + '.json', V + '_premier_jet.log', V + '_sur_acte_mute.log', V + '_sur_acte_mute.json',
          'mutation_acte_bis_contre_epreuve_machine2_v1.py', 'experience_O_BIS_2_machine2_v1.py',
          'experience_O_BIS_2_threads_machine2_v1.py', 'experience_O_BIS_2/experience_O_BIS_2.log',
          'experience_O_BIS_2/experience_O_BIS_2_threads.log', SELF]
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
nn = re.sub(r'\s+', ' ', note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
v = json.load(open(os.path.join(ICI, V + '.json'), encoding='ascii'))
vm = json.load(open(os.path.join(ICI, V + '_sur_acte_mute.json'), encoding='ascii'))
NCHK, NMORD = v['bilan']['chk'], v['bilan']['mord']
if NMORD != 0 or NCHK != len(v['controles']) or NCHK != 34:
    arrets.append('bilan de la verification : %d controles, %d morsures (attendu 34 / 0)' % (NCHK, NMORD))
if ('%d controles, 0 morsure' % NCHK) not in note:
    arrets.append('la note n annonce pas "%d controles, 0 morsure"' % NCHK)
if vm['bilan']['mord'] != 9 or vm['bilan']['chk'] != NCHK or '**9 controles mordent**' not in note:
    arrets.append('contre-epreuve : %s morsures lues, la note annonce 9' % vm['bilan']['mord'])
pj = open(os.path.join(ICI, V + '_premier_jet.log'), encoding='ascii', errors='replace').read()
if 'BILAN : 34 controles, 6 mordent' not in pj or '**6 mordaient**' not in note:
    arrets.append('premier jet : "34 controles, 6 mordent" absent du journal ou de la note')
lm = open(os.path.join(ICI, V + '.log'), encoding='ascii', errors='replace').read()
if 'BILAN : 34 controles, 0 mordent' not in lm:
    arrets.append('le journal de la verification ne porte pas 34 / 0')
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_m1 = [n for n in zl.namelist() if n.startswith('MANIFEST_')][0]
canons = {'acte': (emp(zl.read('journal_delta_nn_qualification_EB_bis_v1.md'))[0], 'c396a00095a0b9e3'),
          'lot de machine 1': (emp(zl.read(man_m1))[0], 'ff93d708547f8ec0'),
          'scelle': (emp(zl.read('rejeu_point_39_20_F1G20_machine1.json'))[0], '7fb9026014ad0c93')}
for nom, (got, att) in canons.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
# l'experience O-BIS-2 : les valeurs de la note viennent des journaux
e1 = open(os.path.join(ICI, 'experience_O_BIS_2', 'experience_O_BIS_2.log'), encoding='ascii').read()
e2 = open(os.path.join(ICI, 'experience_O_BIS_2', 'experience_O_BIS_2_threads.log'), encoding='ascii').read()
for val, lieu in (('5.398020792141e-10', e1), ('5.378534999046e-10', e2), ('5.366965337872e-10', e2), ('-1.484993826469327e-04', e1),
                  ('-1.484993810995113e-04', e2)):
    if val not in lieu:
        arrets.append('valeur %s absente de son journal' % val)
    if val not in note:
        arrets.append('la note ne porte pas la valeur %s' % val)
if 'plus grand |HA - HB| = 0.000e+00 ; nombre d elements differents = 0' not in e1 or 'A - A2 = 0.000e+00' not in e1:
    arrets.append('l experience ne rend pas 0 element different et le determinisme')
if 'fils OPENBLAS=4 OMP=4 ; pool [(\'openblas\', 4)]' not in e2 or 'fils OPENBLAS=2 OMP=2' not in e2:
    arrets.append('le journal des fils ne porte pas les deux configurations')
sonde = json.load(open(os.path.join(ICI, 'nuit_EB_bis', 'sortie', 'sonde_etage1.json'), encoding='ascii'))
gs = repr(sonde['TP']['j06']['traj']['F1G30']['-2']['etats'][0]['gamma'])
diag = [r for r in json.load(open(os.path.join(ICI, 'diagnostic_TP_echelle_forte', 'diag_G30.json'), encoding='ascii'))
        if r['j'] == 6 and r['k'] == -2][0]
if gs not in note or repr(diag['gamma']) not in note:
    arrets.append('la note ne porte pas les deux valeurs de la nuit : sonde %s, diagnostic %r' % (gs, diag['gamma']))
if gs[:14] not in e1.replace('5.398020792141e-10', gs[:14]) or abs(float(gs) - 5.398020792141e-10) > 1e-22 or \
        abs(diag['gamma'] - 5.378534999046e-10) > 1e-21:
    arrets.append('l experience ne retrouve pas les valeurs de la nuit a 12 chiffres')
CANONS = {}
for nom in PIECES:
    if nom == NOTE:
        continue
    c = emp(open(os.path.join(ICI, nom), 'rb').read())[0]
    CANONS[nom] = c
    if nom != SELF and c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, nom))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 DE L ACTE nn DE LA QUALIFICATION E-B BIS, PROJET v1 (c396a00095a0b9e3, lot de '
    'machine 1 ff93d708547f8ec0). VERIFICATION : %d controles, %d morsure ; contre-epreuve : 9 morsures sur 7 mutations ; premier '
    'jet : 6 morsures, defauts de mon script. CONTRESIGNE sur les nombres, la structure et les citations ; une morsure de '
    'description (M-1, nn.4) ; cause d O-BIS-2 trouvee (fils BLAS). machine 2, classe B\n' % (NOM, NCHK, NMORD),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte c396a00095a0b9e3 ; lot de machine 1 ff93d708547f8ec0 ; lot de machine 2 a01598ec24237921 (resultat) ; '
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
