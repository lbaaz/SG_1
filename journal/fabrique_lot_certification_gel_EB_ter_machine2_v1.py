# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel E-B ter (432319b9feb34b82), de sa sonde, de son bloc, de sa feuille, de son banc et de sa reference des ancres' -- manifeste + ZIP. 2026-11-15.
Derive de fabrique_lot_rejeu_absorbeurs_longs_machine2_v1.py (non edite). Usage : py -3.11 -P fabrique_lot_certification_gel_EB_ter_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le lot de machine 1 (42110a3d1eabdaa0) RECALCULE depuis son zip et son manifeste ; mon lot du rejeu (29073aa2ac4decac) recalcule de son manifeste ;
chaque chiffre de la note relu dans le JSON ou le journal qui le porte ; chaque canon de piece nomme dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
C = 'certif_EB_ter/'
CT = C + 'controles/'
PV = C + 'prevol/'
NOM = 'lot_machine2_2026-11-15_certification_gel_EB_ter_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_EB_ter_machine2_v1.py'
LOT_M1, MAN_M1 = 'lot_machine1_2026-11-15_gel_EB_ter_v1_recu.zip', 'MANIFEST_lot_machine1_gel_EB_ter_v1.txt'
MAN_REJEU = 'MANIFEST_lot_machine2_rejeu_absorbeurs_longs_hors_chaine_v1.txt'
PIECES = [CT + x for x in ('feuille_independante_ter_machine2_v1.py', 'confrontation_feuilles_ter_machine2_v1.py', 'confrontation_feuilles_ter_machine2_v1.log',
                           'confrontation_feuilles_ter_machine2_v1.json', 'controles_gel_ter_machine2_v1.py', 'controles_gel_ter_machine2_v1.log',
                           'controles_gel_ter_machine2_v1.json', 'banc_sorties_ter_machine2_v1.py', 'banc_sorties_ter_machine2_v1.log', 'banc_sorties_ter_machine2_v1.json',
                           'bloc_et_lecteur_ter_machine2_v1.py', 'bloc_et_lecteur_ter_machine2_v1.log', 'bloc_et_lecteur_ter_machine2_v1.json',
                           'selftest_feuille_ter_rejoue_machine2.log', 'banc_feuille_ter_rejoue_machine2.log')] + \
         [PV + x for x in ('lancer.sh', 'console_etage0.log', 'console_ancres.log', 'console_etage1.log', 'sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json',
                           'console_feuille_instrument.log', 'lecture_ter_instrument.log', 'verdict_ter_instrument.json')] + \
         [C + 'lancer_EB_ter_machine2_v1.py', SELF]
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


def js(p):
    return json.load(open(os.path.join(ICI, p), encoding='utf-8'))


def lire_manifeste(raw):
    att = {}
    for l in raw.decode('utf-8').split('\n'):
        p = l.split()
        if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
            att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
    return att


for p in PIECES + [NOTE, LOT_M1, MAN_M1, MAN_REJEU]:
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

# --- le lot de machine 1 et mon lot du rejeu, recalcules
mraw = open(os.path.join(ICI, MAN_M1), 'rb').read()
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
att = lire_manifeste(mraw)
if emp(mraw)[0] != '42110a3d1eabdaa0' or len(att) != 55 or sorted(att) != sorted(zl.namelist()):
    arrets.append('lot de machine 1 : canon %s, %d pieces' % (emp(mraw)[0], len(att)))
if [n for n in att if emp(zl.read(n)) != att[n]]:
    arrets.append('lot de machine 1 : des pieces ne sont pas au canon')
if emp(open(os.path.join(ICI, MAN_REJEU), 'rb').read())[0] != '29073aa2ac4decac':
    arrets.append('le manifeste du rejeu n est pas 29073aa2ac4decac')
for c in ('42110a3d1eabdaa0', '432319b9feb34b82', 'b5616dcf858e8801', '9b0f95f3e10e9b0d', 'b2d6d7cfaf30f1cf', '6b63a9de25107ae4', '6600fb8418c79930', '29073aa2ac4decac', '4103eae43f989877'):
    if c not in nn:
        arrets.append('la note ne nomme pas %s' % c)
for nom, c in (('sonde', 'b5616dcf858e8801'), ('bloc', '9b0f95f3e10e9b0d'), ('feuille', 'b2d6d7cfaf30f1cf'), ('banc', '6b63a9de25107ae4'), ('ancres', '6600fb8418c79930')):
    f = [n for n in att if att[n][0] == c]
    if len(f) != 1:
        arrets.append('le canon %s (%s) n est pas au manifeste de machine 1' % (c, nom))

# --- les journaux et les JSON
if 'selftest : 68 tenus sur 68' not in lit(CT + 'selftest_feuille_ter_rejoue_machine2.log') or \
        'BANC : 43 alterations, 43 mordues, 0 survivantes [], 0 cibles refusees [] ; base saine : True' not in lit(CT + 'banc_feuille_ter_rejoue_machine2.log'):
    arrets.append('selftest ou banc de la feuille : pas 68 sur 68 et 43 sur 43')
cj = js(CT + 'confrontation_feuilles_ter_machine2_v1.json')
if not (cj['desaccords_total'] == 0 and cj['F1']['etats'] == 38 and (cj['F1']['QUALIFIES'], cj['F1']['NON_QUALIFIES'], cj['F1']['NON_LISIBLES']) == (35, 3, 0)
        and cj['F2']['accord'] == 20000 and cj['F3']['cas'] == 2657206 and cj['F3']['desaccords'] == 0 and cj['F3']['consigne_desaccords'] == 0):
    arrets.append('confrontation des feuilles : pas 0 desaccord')
gj = js(CT + 'controles_gel_ter_machine2_v1.json')
faux = [x['nom'] for x in gj if not x['tient']]
if len(gj) != 13 or faux != ['K11']:
    arrets.append('controles du gel : %d controles, qui mordent : %s (attendu 13, K11 seul)' % (len(gj), faux))
bj = js(CT + 'banc_sorties_ter_machine2_v1.json')
if len(bj) != 38 or not all(x['ok'] for x in bj) or sum(1 for x in bj if x['nom'].startswith('I')) != 24 or sum(1 for x in bj if x['nom'].startswith('V')) != 14:
    arrets.append('banc de sorties : pas 38 sur 38 (24 + 14)')
lj = js(CT + 'bloc_et_lecteur_ter_machine2_v1.json')
b5 = lj['B5']
if not (lj['B1'] is True and lj['B2']['ecart_max'] == 0.0 and lj['B3'] == 0.0 and lj['B4'] == {'deux_echecs': True, 'un_echec': True}
        and all(v['lectures'] == 192 and v['hors'] == 0 and 1.9e-10 < v['ecart_max'] < 2.1e-10 for v in b5.values()) and len(b5) == 2):
    arrets.append('bloc et lecteur : chiffres hors de la note : %s' % (lj,))
bl = lit(CT + 'bloc_et_lecteur_ter_machine2_v1.log')
if '16 trajectoires en 323 s' not in bl:
    arrets.append('duree de mon lecteur : 323 s absente du journal')
# pre-vol
n_lect = n_non = n_it2 = 0
res_max, poids_min = 0.0, 1.0
dur = []
for f in ('sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json'):
    o = js(PV + f)
    dur.append(o['duree_s'])
    pile = [o]
    while pile:
        x = pile.pop()
        if isinstance(x, dict):
            if 'gamma' in x and 'suivi' in x:
                n_lect += 1
                n_non += not x['suivi']
                n_it2 += x['iterations'] == 2
                res_max = max(res_max, x['residu'])
                poids_min = min(poids_min, x['poids_site'])
            else:
                pile.extend(x.values())
        elif isinstance(x, list):
            pile.extend(x)
if (n_lect, n_non, n_it2) != (468, 0, 451) or not (1.03e-11 < res_max < 1.05e-11) or not (0.667 < poids_min < 0.669) or [round(d) for d in dur] != [11, 379, 413]:
    arrets.append('pre-vol : %d lectures, %d non suivies, %d a deux iterations, residu %.2e, poids %.3f, durees %s' % (n_lect, n_non, n_it2, res_max, poids_min, dur))
vi = js(PV + 'verdict_ter_instrument.json')
if vi['instrument'] != 'TIENT' or vi['motifs'] != [] or not vi['etage0']['tient'] or not vi['ancres']['tient'] or not vi['etage1']['tient'] or vi['etage0']['lectures'] != 84 or vi['ancres']['lectures'] != 192 \
        or not (4.3e-16 < vi['ancres']['pire_ecart_ln'] < 4.5e-16) or not (5.7e-13 < vi['etage0']['pire_ecart_absolu'] < 5.9e-13) or not (2.8e-4 < vi['etage0']['pire_ecart_relatif_au_dessus_de_mille_planchers'] < 3.0e-4):
    arrets.append('verdict de l instrument du pre-vol : pas ce que la note dit')
lt = lit(PV + 'lecture_ter_instrument.log')
if 'selftest : 68 tenus sur 68' not in lt or 'VERDICT DE L\'INSTRUMENT : TIENT []' not in lt:
    arrets.append('journal de la feuille instrument : pas TIENT')
for x in ('42110a3d1eabdaa0', '55 pieces', '68 sur 68', '43 sur 43', '38 etats reels', '20000 etats', '2657206', '10011', '35, 3, 0', '38 cas', '23 alterations', '14 scenarios',
          '84 sur 84', '192 sur 192', '4.4e-16', '1e-6', '8 sur 8', '12 sur 13', 'K11', '0.0044', '0.0022', '192 lectures', '2.0e-10', '3.5e-11', '1.6e-13', '5.5e-12', '323 s', '468', '451 lectures',
          '1.04e-11', '2.5e-12', '6.4e-12', '0.668', '11 s, 379 s, 413 s', 'py -3.11 -P', 'tu peux certifier et jouer si c\'est ok ?', 'O-6', 'dix canons'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION PAR MACHINE 2 du gel E-B ter (432319b9feb34b82, lot de machine 1 42110a3d1eabdaa0), de sa sonde, de son bloc, de sa feuille, de son banc et de sa reference des ancres : '
    'CERTIFIE, 0 morsure ; ma feuille (ecrite du texte du gel apres avoir lu la tienne) a 0 desaccord sur 38 etats reels, 20000 synthetiques et 2657206 cas de cascade ; banc de sorties 38 sur 38 ; '
    'pre-vol sur BOCAL4 : etage 0 84 sur 84, ancres 192 sur 192 a 4.4e-16, temoins 8 sur 8 et 8 sur 8, instrument TIENT ; mon lecteur retrouve le bloc a 2.0e-10 sur 192 lectures. '
    'Aucun calcul 2D aux douze points avant ce lot (E19). Le run suit, second lot. machine 2\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 42110a3d1eabdaa0 (gel 432319b9feb34b82) ; mon lot du rejeu 29073aa2ac4decac ; registre 8d54bf9 ; moteur 82a0be882568fe0c ; depot 10887c60d5f55bcf ; '
              'retenus 69b3bab3bb8480b7 ; reference du temoin 4d51dd58ef456fe9\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu_zip = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu_zip[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu_zip.get(n)]
    manque = sorted(set(attendu_zip) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
