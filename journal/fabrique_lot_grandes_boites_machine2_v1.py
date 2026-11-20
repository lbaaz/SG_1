# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'GRANDES BOITES : RESULTATS' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-17. Meme squelette que fabrique_lot_boite2d_et_lab_machine2_v1.py (non edite ; diff joint).
Hors chaine, classe 3, point sacrifie w2 = 101/50 : aucune cellule tiree, aucun gel, aucun depot.
Usage : py -3.11 -I fabrique_lot_grandes_boites_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; la note est ASCII (verifie AVANT d'ouvrir
un fichier en ecriture), nomme le canon de CHAQUE piece ; aucune fuite de vie privee (identifiant du poste, prenom, nom, messagerie, chemins personnels) dans les pieces ni dans la note ; LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D1 = 'grandes_boites_machine2/'
D2 = 'certif_boite2d_machine2/'
NOM = 'lot_machine2_2026-11-17_grandes_boites_resultats_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_grandes_boites_resultats_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_grandes_boites_resultats_machine2_v1.md'
SELF = 'fabrique_lot_grandes_boites_machine2_v1.py'
PIECES = ([D1 + 'gb200_w%d.%s' % (i, e) for i in (1, 2, 3, 4) for e in ('jsonl', 'log')]
          + [D1 + 'gb300_w%d.%s' % (i, e) for i in (1, 2, 3) for e in ('jsonl', 'log')]
          + [D1 + 'gb400_w%d.%s' % (i, e) for i in (1, 2) for e in ('jsonl', 'log')]
          + [D1 + 'agrege_attendus_cote%d_machine2_v1.log' % c for c in (200, 300, 400)]
          + [D1 + 'combine_R_machine2_v1.log']
          + [D2 + n for n in ('grandes_boites_machine2_v1.py', 'agrege_attendus_machine2_v1.py', 'combine_R_machine2_v1.py')] + [SELF])
# (journal, chaine qui doit y figurer ET figurer dans la note) : les nombres de la note, relus dans leur source
NOMBRES = [
    (D1 + 'gb200_w3.log', '200 40000 0.99927491 16 16 1.1181 5.417 40/40 55'),
    (D1 + 'gb200_w3.log', '201 40401 0.99926824 13 13 1.0699 5.210 40/40 43'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'niveaux par boite : moyenne 14.10 (attendu 14.4 +- 20 pour cent : 11.5 a 17.3) -> TIENT'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'niveaux non fiables (deux lectures en desaccord a plus de 2 pour cent) : 0 sur 282'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'somme / largeur : moyenne 1.034 (ecart-type par boite 0.088) -> TIENT (0.90-1.10)'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'participation : moyenne 6.32 (min 4.06 max 8.82)'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'R observe = 0.883 | Porter-Thomas aux memes n : R = 1.000 +- 0.070'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'exponentielle : R = 0.712 +- 0.035'),
    (D1 + 'agrege_attendus_cote200_machine2_v1.log', 'mediane 0.525 ; fraction sous 0.1 : 0.259 ; fraction au-dessus de 3 : 0.078'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'niveaux par boite : moyenne 20.83 (attendu 21.6 +- 20 pour cent : 17.3 a 25.9) -> TIENT'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'somme / largeur : moyenne 1.026 (ecart-type par boite 0.149) -> TIENT (0.90-1.10)'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'participation : moyenne 7.32 (min 5.53 max 10.44)'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'R observe = 1.082 | Porter-Thomas aux memes n : R = 0.999 +- 0.115'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'exponentielle : R = 0.697 +- 0.055'),
    (D1 + 'agrege_attendus_cote300_machine2_v1.log', 'mediane 0.352 ; fraction sous 0.1 : 0.320 ; fraction au-dessus de 3 : 0.088'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'niveaux par boite : moyenne 26.83 (attendu 28.8 +- 20 pour cent : 23.0 a 34.6) -> TIENT'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'niveaux non fiables (deux lectures en desaccord a plus de 2 pour cent) : 1 sur 161'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'somme / largeur : moyenne 1.090 (ecart-type par boite 0.082) -> TIENT (0.90-1.10)'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'participation : moyenne 12.34 (min 8.89 max 16.25)'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'R observe = 0.798 | Porter-Thomas aux memes n : R = 0.999 +- 0.107'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'exponentielle : R = 0.691 +- 0.050'),
    (D1 + 'agrege_attendus_cote400_machine2_v1.log', 'mediane 0.559 ; fraction sous 0.1 : 0.261 ; fraction au-dessus de 3 : 0.081'),
    (D1 + 'combine_R_machine2_v1.log', 'tranche cotes 190-209 (20 boites) : R = 0.883 ; Porter-Thomas 1.000 +- 0.070 -> ecart -1.67 sigma ; exponentielle 0.712 +- 0.035 -> ecart +4.89 sigma'),
    (D1 + 'combine_R_machine2_v1.log', 'tranche cotes 297-302 (6 boites) : R = 1.082 ; Porter-Thomas 0.999 +- 0.115 -> ecart +0.72 sigma ; exponentielle 0.697 +- 0.055 -> ecart +7.00 sigma'),
    (D1 + 'combine_R_machine2_v1.log', 'tranche cotes 397-402 (6 boites) : R = 0.798 ; Porter-Thomas 0.999 +- 0.107 -> ecart -1.88 sigma ; exponentielle 0.691 +- 0.050 -> ecart +2.14 sigma'),
    (D1 + 'combine_R_machine2_v1.log', 'R combine (trois tranches, ponderation 1 / sigma_PT^2) = 0.904 +- 0.052 ; ecart a Porter-Thomas (1) : -1.84 sigma ; a l exponentielle (~0.70) : +3.90 sigma'),
]
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


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
note = lit(NOTE)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
nn = norm(note)
for j, s in NOMBRES:
    if norm(s) not in norm(lit(j)):
        arrets.append('le journal %s ne porte pas %r' % (j, s))
    if norm(s) not in nn:
        arrets.append('la note ne porte pas %r' % s)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note):
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES + [NOTE]:
    for f in fuites(p, open(os.path.join(ICI, p), 'rb').read()):
        arrets.append('FUITE de vie privee : %s' % (f,))
    if b'\r' in open(os.path.join(ICI, p), 'rb').read() and p.endswith(('.py', '.md')):
        arrets.append('fins de ligne CRLF dans %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- LES GRANDES BOITES DEMANDEES PAR machine 1 (lot 4e15e302d97e26b8) : cotes 190-209 (20 boites), 297-302 (6), 397-402 (6) au point sacrifie w2 = 101/50, 3 barreaux, deux lectures de y par niveau ; '
    'ses attendus appliques tels quels (R, trois issues, bandes de compte et de somme) ; donnees niveau par niveau (JSONL), journaux, agregation. HORS CHAINE, classe 3 : aucune cellule tiree, aucun gel, aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le lot de machine 1 lot_machine1_2026-11-16_pont_attendus_grandes_boites_v1 (4e15e302d97e26b8, authentifie, 0 morsure) ; mon lot precedent 2eadae283fc04633 (recouvrement) ; le registre public en tete 2988237 (clone frais sur D:, lu, non ecrit)\n")
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
