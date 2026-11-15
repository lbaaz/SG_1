# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'contreseing de l'acte nn du run du gel la chaine E-A au second ordre, projet v1' -- manifeste + ZIP. 2026-11-15.
Usage : python -P fabrique_lot_contreseing_acte_ordre2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le bilan de la verification LU dans son JSON (16 controles, 1 morsure : C16) ; le bilan de la contre-epreuve LU dans son JSON
(14 morsures : les 10 controles que les 19 mutations visent, plus C01 C02 C04 et la morsure permanente C16) ; les canons de l'acte, du lot de machine 1 et du verdict
RECALCULES depuis son zip ; les canons de CHAQUE piece nommes dans la note ; les chiffres cles de la note relus dans mes journaux ; note ASCII ; le manifeste ne se porte
pas lui-meme ; l'en-tete du manifeste porte le canon de l'acte (le perimetre du depot en derive les lots du delta) ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'acte_ordre2_contreseing/'
NOM = 'lot_machine2_2026-11-15_contreseing_acte_ordre2_chaine_EA_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_ordre2_chaine_EA_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_ordre2_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_ordre2_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-15_acte_ordre2_chaine_EA_v1_recu.zip'
V = 'verification_acte_ordre2_machine2_v1'
PIECES = [D + x for x in (V + '.py', V + '.log', V + '.json', 'mutation_acte_ordre2_contre_epreuve_machine2_v1.py', V + '_sur_acte_mute.log', V + '_sur_acte_mute.json')] + [SELF]
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
if len(v['controles']) != 16 or v['bilan']['ids'] != ['C16'] or v['canon'] != 'c2f3e5c9102dc1a7':
    arrets.append('verification sur l acte : %d controles, mordent %s (attendu 16, C16 seul) ; canon %s' % (len(v['controles']), v['bilan']['ids'], v['canon']))
m = json.load(open(os.path.join(ICI, D + V + '_sur_acte_mute.json'), encoding='ascii'))
vises = {'C05', 'C06', 'C08', 'C09', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15'}
mord = set(m['bilan']['ids'])
if len(m['controles']) != 16 or m['bilan']['mord'] != 14 or not vises <= mord or mord - vises != {'C01', 'C02', 'C04', 'C16'}:
    arrets.append('contre-epreuve : %d mordent %s (attendu 14 : les 10 vises + C01 C02 C04 C16)' % (m['bilan']['mord'], sorted(mord)))
if m['canon'] == 'c2f3e5c9102dc1a7':
    arrets.append('la copie mutee a le canon de l acte : la contre-epreuve ne mute rien')
for x in ('16 controles et UNE morsure', '19 chiffres ou mots', '14 morsures, dont les 10', '123764', '119390', '4195583a970eaf70', '79e77d2', '3177 s', '1346 s', '4.90e-07',
          '8.2e-11', '2.6e-12', '0.027', '1.136, 1.447, 1.679', '4.08 et 4.01', 'etat_machine_machine2.log', 'Cinq de mes controles', 'preferent donc'.replace('preferent donc', 'Les energies preferent donc')):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
vl = lit(D + V + '.log')
for x in ('BILAN : 16 controles, 1 mordent [\'C16\']', 'mes octets bruts 123764, les siens 119390', 'registre', '4.44e-07', '4.90e-07', 'G-8 : Gamma_flux a 8.2e-11, dE a 2.6e-12',
          'NON ; la note ecrit : "Les energies preferent donc la somme des deux termes a chacun pris seul"', "RELEVE : 18 controles, 18 tenus", 'CONTRE-EPREUVE : 43 copies alterees, 43 mordues'):
    if x not in vl:
        arrets.append('journal de la verification : %r absent' % x)
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
man_raw = open(os.path.join(ICI, 'MANIFEST_lot_machine1_acte_ordre2_chaine_EA_v1.txt'), 'rb').read()
canons = {'acte': (emp(zl.read('journal_delta_nn_ordre2_chaine_EA_v1.md'))[0], 'c2f3e5c9102dc1a7'), 'lot de machine 1': (emp(man_raw)[0], 'da1c2668d317b9d5'),
          'verdict': (emp(zl.read('verdict_rejoue_machine1.json'))[0], '4195583a970eaf70')}
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
    'MANIFESTE %s -- CONTRESEING DE MACHINE 2 DE L ACTE nn DU RUN DU GEL LA CHAINE E-A AU SECOND ORDRE, PROJET v1 (c2f3e5c9102dc1a7, lot de machine 1 '
    'da1c2668d317b9d5). 16 controles recalcules de mes sources, une morsure (C16 : une citation de la note de machine 1 amputee du mot donc, sans consequence) ; '
    'contre-epreuve sur une copie mutee : 14 morsures, dont les 10 controles vises. CONTRESIGNE tel quel ; aucune v2 demandee. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : acte c2f3e5c9102dc1a7 ; lot de machine 1 da1c2668d317b9d5 ; mes lots 59a583a640112891 (certification) et 6dfdfe8fd0b8eaad (resultat)\n')
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
