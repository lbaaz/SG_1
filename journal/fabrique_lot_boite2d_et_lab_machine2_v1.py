# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'BOITE 2D NUE ET LABORATOIRE 1D' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-16 (nuit). Meme squelette que fabrique_lot_pont_controle_machine2_v1.py (non edite ; diff joint).
Hors chaine, classe 3 : aucune cellule tiree, aucun gel, aucun run au sens du gel, aucun depot.
Usage : py -3.11 -I fabrique_lot_boite2d_et_lab_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; la note est ASCII (verifie AVANT d'ouvrir
un fichier en ecriture), nomme le canon de CHAQUE piece ; aucune fuite de vie privee (identifiant du poste, prenom, nom, messagerie, chemins personnels) dans les pieces ni dans la note ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D1 = 'certif_boite2d_machine2/'
D2 = 'lab1d_machine2/'
NOM = 'lot_machine2_2026-11-16_boite2d_et_laboratoire_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_boite2d_et_laboratoire_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_boite2d_et_laboratoire_machine2_v1.md'
SELF = 'fabrique_lot_boite2d_et_lab_machine2_v1.py'
PIECES = [D1 + n for n in (
    'entrees_boite2d_machine2_v1.py', 'entrees_boite2d_machine2_v1.log',
    'boite2d_nue_machine2_v1.py', 'test_boite_vs_moteur_machine2_v1.log',
    'boite2d_3barreaux_c21_64_machine2_v1.log', 'boite2d_4barreaux_c21_45_machine2_v1.log', 'boite2d_5barreaux_c21_45_machine2_v1.log',
    'boite2d_creux_3barreaux_machine2_v1.log', 'boite2d_creux_4barreaux_machine2_v1.log', 'boite2d_creux_5barreaux_machine2_v1.log',
    'agrege_boite2d_machine2_v1.py', 'agrege_boite2d_machine2_v1.log')] + [D2 + n for n in (
    'lab1d_vide_couloir_machine2_v1.py', 'lab1d_A_machine2_v1.log', 'lab1d_C_machine2_v1.log', 'lab1d_D_machine2_v1.log',
    'diagnostic_lorentzienne_machine2_v1.py', 'diagnostic_lorentzienne_L4096_machine2_v1.log')] + [SELF]
# (journal, chaine qui doit y figurer ET figurer dans la note) : les nombres de la note, relus dans leur source
NOMBRES = [
    (D1 + 'entrees_boite2d_machine2_v1.log', 'Gamma = 3.2661e-09 (note : 3.2661e-09) | rapport 1.00000'),
    (D1 + 'entrees_boite2d_machine2_v1.log', 'Gamma = 7.2530e-11 (note : 7.2530e-11) | rapport 1.00000'),
    (D1 + 'entrees_boite2d_machine2_v1.log', 'Gamma = 1.5154e-12 (note : 1.5154e-12) | rapport 0.99998'),
    (D1 + 'test_boite_vs_moteur_machine2_v1.log', 'barreaux 3 : N = 7, max |H(moi) - Re H_2D(moteur)| = 0.000e+00, max |Im H_2D| = 0.000e+00, symetrie de ma boite 0.000e+00'),
    (D1 + 'agrege_boite2d_machine2_v1.log', '25 boites | Somme/largeur (avec 1/w0) 1.017 +- 0.065 (sans 1.016) | niveaux/boite 2.20 | participation 1.80'),
    (D1 + 'agrege_boite2d_machine2_v1.log', '19 boites | Somme/largeur (avec 1/w0) 1.048 +- 0.041 (sans 1.047) | niveaux/boite 4.00 | participation 2.78'),
    (D1 + 'agrege_boite2d_machine2_v1.log', '25 boites | Somme/largeur (avec 1/w0) 1.020 +- 0.085 (sans 1.020) | niveaux/boite 1.96 | participation 1.58'),
    (D1 + 'agrege_boite2d_machine2_v1.log', '25 boites | Somme/largeur (avec 1/w0) 1.021 +- 0.078 (sans 1.021) | niveaux/boite 1.84 | participation 1.55'),
    (D1 + 'agrege_boite2d_machine2_v1.log', 'pente du nombre de niveaux selon le cote, 3 barreaux, cotes 21-64 : +0.0844 par quantum'),
    (D1 + 'boite2d_creux_3barreaux_machine2_v1.log', '201 40401 0.99926824 -0.000014 13 13 1.0699 1.0691 5.210'),
    (D1 + 'boite2d_creux_3barreaux_machine2_v1.log', '150 22500 0.99927500 -0.000014 11 11 0.9930 0.9922 5.879'),
    (D1 + 'boite2d_creux_4barreaux_machine2_v1.log', '150 22500 0.99958773 -0.000008 10 10 1.0387 1.0383 8.562'),
    (D2 + 'lab1d_A_machine2_v1.log', 'L(Gamma=D) = 2pi/Gamma = 359.8'),
    (D2 + 'lab1d_A_machine2_v1.log', '8 11 6.9813e-01 0.0250 1.631'),
    (D2 + 'lab1d_A_machine2_v1.log', '4.3608e-02 1.0041 0.9900 (0.434, 0.455)'),
    (D2 + 'lab1d_A_machine2_v1.log', '256 259 2.4448e-02 0.7143 4.590'),
    (D2 + 'lab1d_A_machine2_v1.log', '6.9154e-03 0.6481 0.8389 (0.314, 0.317)'),
    (D2 + 'lab1d_A_machine2_v1.log', '4096 4099 1.5336e-03 11.3865 37.144'),
    (D2 + 'lab1d_A_machine2_v1.log', '7.1704e-04 0.0859 0.3473 (0.047, 0.047)'),
    (D2 + 'lab1d_A_machine2_v1.log', '0.2068 0.9975'),
    (D2 + 'lab1d_C_machine2_v1.log', '1 1027 1024 2.8459 12.160 1.3921'),
    (D2 + 'lab1d_C_machine2_v1.log', '32 1031 1028 2.8571 2.695'),
    (D2 + 'lab1d_C_machine2_v1.log', '64 1028 1025 2.8487 3.566'),
    (D2 + 'lab1d_D_machine2_v1.log', 'regulier 1 2 300 2.01 1.0028 0.0468'),
    (D2 + 'lab1d_D_machine2_v1.log', 'regulier 1 4 300 3.97 0.9977 0.0396'),
    (D2 + 'lab1d_D_machine2_v1.log', 'alea Porter-Th 4 4 150 3.97 0.8441 0.5319'),
    (D2 + 'diagnostic_lorentzienne_L4096_machine2_v1.log', 'poids a |E - E_r| > 1.00 : 0.10279 | cote bas 0.00023 cote haut 0.10256'),
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
for p in PIECES + [NOTE]:
    if b'\r' in open(os.path.join(ICI, p), 'rb').read() and p.endswith(('.py', '.md')):
        arrets.append('fins de ligne CRLF dans %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- LA BOITE 2D NUE REFAITE PAR machine 2 au point sacrifie w2 = 101/50 (compte, somme repondere, participation ; ses nombres retombent) et LE LABORATOIRE 1D (vide, barriere, couloir uniforme ; '
    'Gamma exact sans absorbeur) : reponse a la proposition de machine 1 (lot 359e2fb28b7e09d3). HORS CHAINE, classe 3 : aucune cellule tiree, aucun gel, aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le lot de machine 1 lot_machine1_2026-11-16_pont_v3_et_reponse_controle_v1 (359e2fb28b7e09d3, authentifie, 0 morsure) ; le registre public en tete 2988237 (clone frais, lu, non ecrit)\n")
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
