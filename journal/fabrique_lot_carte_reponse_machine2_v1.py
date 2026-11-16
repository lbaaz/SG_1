# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'reponse a la carte du gel de la loi' -- manifeste + ZIP. 2026-11-15. Derive de fabrique_lot_ordre3_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_carte_reponse_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le lot de machine 1 (1e8413aed149429f) et sa note (1f6cfb5f9472b1b4) RECALCULES depuis les fichiers recus ; chaque journal LU (couples joues : 39 / 39, aucun ecart ;
exemple : dix lignes, ecarts, 'TIENT') ; le moteur et le bloc d'ordre 2 recalcules depuis le registre clone ; les chiffres de la note presents ; les canons de CHAQUE piece nommes dans la note ; note ASCII ;
le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-15_carte_reponse_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_carte_reponse_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_carte_reponse_machine2_v1.md'
SELF = 'fabrique_lot_carte_reponse_machine2_v1.py'
D = 'controle_carte_machine2/'
REG = r'C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad/reg_neuf98/scripts/'
LIV = 'livraison_15f_carte_gel_loi/'
PIECES = [D + x for x in ('verif_couples_joues_machine2_v1.py', 'verif_couples_joues_machine2_v1.log', 'verif_couples_joues_machine2_v1.json',
                          'verif_exemple_carte_machine2_v1.py', 'verif_exemple_carte_machine2_v1.log', 'verif_exemple_carte_machine2_v1.json')] + [SELF]
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


for p in PIECES + [NOTE, LIV + 'MANIFEST_lot_machine1_note_carte_gel_loi_v1.txt', LIV + 'lot_machine1_2026-11-15_note_carte_gel_loi_v1.zip']:
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
lc, le = lit(D + 'verif_couples_joues_machine2_v1.log'), lit(D + 'verif_exemple_carte_machine2_v1.log')
for nom, lg, xs in (
        ('couples joues', lc, ('lignes de la grille lues : 22 (attendu 22)', 'couples joues connus de moi : 42 (dont 16 points du depot) ; sur la grille de machine 1 : 39 ; marques j de machine 1 : 39',
                               'joues par moi sur la grille mais SANS marque j chez machine 1 : 0', 'marques j chez machine 1 que je ne connais pas comme joues : 0',
                               '(37/20, 1), (107/50, 1), (43/20, 1)', 'M-4 : LA LISTE DE MACHINE 1 EST EXACTE')),
        ('exemple', le, ('lignes du tableau d exemple lues chez machine 1 : 10 (attendu 10)', 'plus grands ecarts : couplage (relatif) 1.64e-04 ; largeur d ordre 3 (relatif) 3.95e-03',
                         'marque "d" (discriminant a 5 pour cent) : IDENTIQUE aux dix lignes', 'EXEMPLE DE LA CARTE : TIENT',
                         '|ln(ordre 2 / ordre 3)| 0.092', '|ln(ordre 2 / ordre 3)| 0.073', '|ln(ordre 2 / ordre 3)| 0.064', '|ln(ordre 2 / ordre 3)| 0.054', '|ln(ordre 2 / ordre 3)| 0.046'))):
    for x in xs:
        if x not in lg:
            arrets.append('journal %s : %r absent' % (nom, x))
for x in ('1e8413aed149429f', '1f6cfb5f9472b1b4', '39 couples', '1.6e-04', '3.9e-03', '0.092, 0.073, 0.064, 0.054, 0.046', '4524', '4377', '2 h 10', 'UN run', 'C1.', 'C2.', 'C3.', 'C4.', '3.1', '3.2', '3.3',
          '3.4', '3.5', '3.6', '3.7', 'sha256', 'graine', 'OPERATEUR', 'ne tire', 'b42a63640f1c566a', 'C12', 'E19', '21 h 54', '18 h 50', 'Je ne contresigne rien'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
man1 = open(os.path.join(ICI, LIV + 'MANIFEST_lot_machine1_note_carte_gel_loi_v1.txt'), 'rb').read()
if emp(man1)[0] != '1e8413aed149429f':
    arrets.append('le lot de machine 1 n a plus le canon 1e8413aed149429f : %s' % emp(man1)[0])
z1 = zipfile.ZipFile(os.path.join(ICI, LIV + 'lot_machine1_2026-11-15_note_carte_gel_loi_v1.zip'))
if emp(z1.read('note_machine1_carte_gel_loi_2026-11-15_v1.md'))[0] != '1f6cfb5f9472b1b4':
    arrets.append('la note de machine 1 n a plus le canon 1f6cfb5f9472b1b4')
for nom, p, att in (('moteur', REG + 'm17_chaine_v17.py', '82a0be882568fe0c'), ('bloc d ordre 2', REG + 'chaine_ordre2_bloc_machine1_v1.py', '7cd5977bc27bebc1')):
    if emp(open(p, 'rb').read())[0] != att:
        arrets.append('canon %s : %s, attendu %s' % (nom, emp(open(p, 'rb').read())[0], att))
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- REPONSE DE MACHINE 2 A LA CARTE DU GEL DE LA LOI (note 1f6cfb5f9472b1b4, lot de machine 1 1e8413aed149429f) : liste des couples deja joues EXACTE (39 sur 39) ; tableau d exemple '
    'de la section 4 reproduit par ma chaine d ordre 3 (dix lignes sur dix) ; (ii) enchainement des deux etages : un run, quatre conditions ; (iii) la section 5 n est pas jugeable telle quelle '
    '(une feuille d ordre 3 manque) ; regle de tirage proposee, graine a l operateur, rien de tire. 1D seulement, aucune largeur 2D ; ne contresigne rien. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : note de machine 1 1f6cfb5f9472b1b4 ; son lot 1e8413aed149429f ; moteur 82a0be882568fe0c ; bloc d ordre 2 7cd5977bc27bebc1 ; depot du delta 98 10887c60d5f55bcf ; gel du delta 98 41153158190cf7f1 ; '
              'mon ordre3_machine2_v1.py (lot 889fe9b4c1c1c60a)\n')
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
