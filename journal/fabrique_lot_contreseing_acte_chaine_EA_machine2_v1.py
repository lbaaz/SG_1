# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn du run de la chaine E-A par etat, projet v1' -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_contreseing_acte_chaine_EA_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan de la verification LU dans son JSON (22 controles, 0 morsure) ; le bilan de la contre-epreuve
LU dans son JSON (18 morsures, dont les 14 controles que les quinze mutations visent, et C01 C02 C03 C05) ; les canons de l'acte et du lot de
machine 1 RECALCULES depuis son zip ; les canons de CHAQUE piece nommes dans la note ; la note ne porte pas de nombre que ses journaux ne portent
pas (22, 18, 14, 131, 168) ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'acte_chaine_contreseing/'
NOM = 'lot_machine2_2026-11-14_contreseing_acte_chaine_EA_par_etat_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_chaine_EA_par_etat_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_chaine_EA_par_etat_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_chaine_EA_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-14_acte_chaine_EA_par_etat_v1_recu.zip'
V = 'verification_acte_chaine_EA_par_etat_machine2_v1'
PIECES = [D + x for x in (V + '.py', V + '.log', V + '.json', 'mutation_acte_chaine_contre_epreuve_machine2_v1.py',
                          V + '_sur_acte_mute.log', V + '_sur_acte_mute.json')] + [SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


for p in PIECES + [NOTE, LOT_M1]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = open(os.path.join(ICI, NOTE), encoding='ascii', errors='replace').read()
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
if len(v['controles']) != 22 or v['bilan']['mord'] != 0 or v['canon'] != 'aed8677322e20e0d':
    arrets.append('verification sur l acte : %d controles, %d mordent (attendu 22, 0) ; canon %s' % (len(v['controles']), v['bilan']['mord'], v['canon']))
m = json.load(open(os.path.join(ICI, D + V + '_sur_acte_mute.json'), encoding='ascii'))
vises = {'C04', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20'}
mord = set(m['bilan']['ids'])
if len(m['controles']) != 22 or m['bilan']['mord'] != 18 or not vises <= mord or mord - vises != {'C01', 'C02', 'C03', 'C05'}:
    arrets.append('contre-epreuve : %d mordent %s (attendu 18 : les 14 vises + C01 C02 C03 C05)' % (m['bilan']['mord'], sorted(mord)))
if m['canon'] == 'aed8677322e20e0d':
    arrets.append('la copie mutee a le canon de l acte : la contre-epreuve ne mute rien')
for x in ('22 controles et 0 morsure', '18 morsures, dont les 14 controles', 'quinze chiffres', '131 etats juges sur 168', '0.0152', '39955', '38133'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
vl = open(os.path.join(ICI, D + V + '.log'), encoding='ascii').read()
for x in ('BILAN : 22 controles, 0 mordent []', '131 etats juges sur 168', '(J2, rang 10, q = 3.1141, DANS la demi-decade)', 'tete du registre public lue par git ls-remote : fe10bfe',
          'mes octets bruts 39955, les siens 38133'):
    if x not in vl:
        arrets.append('journal de la verification : %r absent' % x)
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_raw = open(os.path.join(ICI, 'MANIFEST_lot_machine1_acte_chaine_EA_par_etat_v1.txt'), 'rb').read()
canons = {'acte': (emp(zl.read('journal_delta_nn_chaine_EA_par_etat_v1.md'))[0], 'aed8677322e20e0d'), 'lot de machine 1': (emp(man_raw)[0], 'bb7db90c75d6935e'),
          'verdict': (emp(zl.read('verdict_rejoue_machine1.json'))[0], '4fbc5f7115002054')}
for nom, (got, att) in canons.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
for x in ('9322566db2546adb', 'def35e82df8b2e68', '7fb9026014ad0c93'):
    if x not in note:
        arrets.append('la note ne nomme pas %s' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 DE L ACTE nn DU RUN DE LA CHAINE E-A PAR ETAT, HORS PLAGE, PROJET v1 (aed8677322e20e0d, lot de machine 1 '
    'bb7db90c75d6935e). 22 controles recalcules de mes sources, 0 morsure ; contre-epreuve sur une copie mutee : 18 morsures, dont les 14 controles '
    'vises. CONTRESIGNE tel quel ; trois observations, aucune ne demande de v2. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte aed8677322e20e0d ; lot de machine 1 bb7db90c75d6935e ; mes lots 3381564852ba6fe4 (certification) et 9143062c481ad267 (resultat)\n')
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
