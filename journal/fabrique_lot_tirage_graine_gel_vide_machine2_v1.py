# -*- coding: ascii -*-
"""FABRIQUE DU LOT de machine 2 : mon tirage sur la graine 479579 (gel 'largeur du vide', partie 1) + l'authentification du lot de reception de m1 -- manifeste + ZIP. 2026-11-16.
Meme squelette que fabrique_lot_certification_gel_vide_partie1_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_tirage_graine_gel_vide_machine2_v1.py
Gardes AVANT ecriture : l'authentification du lot de m1 est LUE (0 morsure, 53c604647e78afa4, tables communes au meme canon B) ; mon tirage est LU (les quatre w2, 28 cellules) ; la comparaison a TON script rejoue
est LUE (0 morsure) ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_tirage_graine_gel_vide_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_tirage_graine_gel_vide_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_tirage_graine_gel_vide_machine2_v1.md'
SELF = 'fabrique_lot_tirage_graine_gel_vide_machine2_v1.py'
C = 'certif_gel_vide_partie1_machine2/'
L = 'livraison_16g_reception_certification_vide/'
PIECES = [L + 'authentifie_lot_reception_m1_machine2_v1.py', L + 'authentifie_lot_reception_m1_machine2_v1.log',
          C + 'tirage_graine_machine2_v1.py', C + 'tirage_graine_479579_machine2_v1.log', C + 'tirage_graine_479579_machine2_v1.json',
          C + 'tirage_m1_script_rejoue_graine_479579_machine2.log', C + 'compare_tirage_m1_machine2_v1.py', C + 'compare_tirage_m1_machine2_v1.log', SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read().replace('\r\n', '\n')


def exige(p, *morceaux):
    t = lit(p)
    for m in morceaux:
        if m not in t:
            arrets.append('journal %s : %r absent' % (p.split('/')[-1], m))


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
exige(L + 'authentifie_lot_reception_m1_machine2_v1.log', 'CANON du manifeste (calcule, non annonce) : 53c604647e78afa4', 'canon de la table commune de m1 : 84bffbbd2f675181 ; la mienne : 84bffbbd2f675181',
      'MORSURES : 0', 'section 6 de la note : pieces citees avec canon : 9')
exige(C + 'tirage_graine_479579_machine2_v1.log', 'table commune de m2 == table commune de m1 (contenu JSON) : True', 'graine : 479579',
      'MG rang 0 : sha256("479579|MG|0") = 8a8770380db1e388... ; modulo 9 = 1 -> w2 = 991/500 (1.982)',
      'MP rang 0 : sha256("479579|MP|0") = 8b8a966b211b0cb0... ; modulo 9 = 6 -> w2 = 1997/1000 (1.997)',
      'PP rang 0 : sha256("479579|PP|0") = e0926c5213125f3c... ; modulo 9 = 4 -> w2 = 401/200 (2.005)',
      'PG rang 0 : sha256("479579|PG|0") = d42c25e428a37bf7... ; modulo 9 = 6 -> w2 = 2017/1000 (2.017)',
      'cellules : 28 (lisibles 16, profondes retenues 12)', 'MG3   w2 = 991/500   (1.982)  m = 3   g = 4.31696e-03')
exige(C + 'tirage_m1_script_rejoue_graine_479579_machine2.log', 'graine : 479579')
exige(C + 'compare_tirage_m1_machine2_v1.log', 'identiques (identifiant, w2, m, couplage ecrit, ligne) : True', 'MORSURES : 0')
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note):
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('53c604647e78afa4', '84bffbbd2f675181', 'd6a8a74c8f14b06a', 'd4f95772710d545c', '479579', '991/500', '1997/1000', '401/200', '2017/1000', '13 h 34 min 38 s'):
    if x not in re.sub(r'\s+', ' ', note):
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
    'MANIFESTE %s -- TIRAGE de machine 2 sur la graine 479579 donnee par l\'operateur (gel "largeur du vide", partie 1 b57c9ccdd3946261) : 4 w2 au rang 0, 28 cellules, identiques a celles du script de machine 1 rejoue ; '
    'authentification du lot de reception de machine 1 (53c604647e78afa4). Aucune 2D, aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le lot de machine 1 53c604647e78afa4 (reception de ma certification d4f95772710d545c) ; la table commune 84bffbbd2f675181 ; la graine 479579 de l'operateur (16/11/2026, 13 h 34 min 38 s)\n")
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
