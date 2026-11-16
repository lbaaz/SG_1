# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'ordre 3 rederive par mon code, et rejeu de l'etape 1' -- manifeste + ZIP. 2026-11-15. Derive de fabrique_lot_rectification_C07_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_ordre3_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque journal LU (le jouet : exposants et 'TIENT' ; les 132 etats avec chaine et leurs neuf ecarts maximaux ; la base tronquee : exposants 3.00 et 4.00, ecarts
des chemins, rapports des sauts lointains, 'TIENT' aux quatre epreuves ; le rejeu de l'etape 1 : 2921 feuilles, 4.441e-16, etendues, dependance a l'absorbeur) ; les canons du moteur et du bloc d'ordre 2
RECALCULES depuis le registre clone ; les canons de CHAQUE piece nommes dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-15_ordre3_rederive_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_ordre3_rederive_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_ordre3_rederive_machine2_v1.md'
SELF = 'fabrique_lot_ordre3_machine2_v1.py'
D = 'controle_ordre3_machine2/'
REG = r'C:/Users/bazil/AppData/Local/Temp/claude/75adcc7f3c1d08bf/7d33635e-8345-4a2c-a69e-f6a51f9d8fa7/scratchpad/reg_neuf98/scripts/'
PIECES = [D + x for x in ('formule_ordre3_jouet_machine2_v1.py', 'formule_ordre3_jouet_machine2_v1.log', 'ordre3_machine2_v1.py', 'ordre3_machine2_v1.log', 'ordre3_machine2_v1.json',
                          'ordre3_machine2_v1_base_tronquee.log', 'etape1_rejeu_machine2_v1.py', 'etape1_rejeu_machine2_v1.log', 'etape1_rejeu_machine2_v1.json')] + [SELF]
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


for p in PIECES + [NOTE]:
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
lj, lm, lb, le = lit(D + 'formule_ordre3_jouet_machine2_v1.log'), lit(D + 'ordre3_machine2_v1.log'), lit(D + 'ordre3_machine2_v1_base_tronquee.log'), lit(D + 'etape1_rejeu_machine2_v1.log')
for nom, lg, xs in (
        ('jouet', lj, ("['2.99', '2.97', '2.96'] ; avec ['3.98', '3.96', '3.90']", 'FORMULE 3.1 : TIENT sur le jouet')),
        ('132 etats', lm, ('RESUME : 132 etats, dont 132 avec chaine', 'herm   plus grand ecart relatif 1.425e-14', 'S2     plus grand ecart relatif 0.000e+00', 'U2     plus grand ecart relatif 0.000e+00',
                           'T3     plus grand ecart relatif 1.188e-11', 'T3_BB  plus grand ecart relatif 4.682e-16', 'T3_A   plus grand ecart relatif 5.913e-16',
                           'W3     plus grand ecart relatif 1.139e-11', 'W3max  plus grand ecart relatif 3.817e-13', 'W5max  plus grand ecart relatif 9.962e-15',
                           'G3     plus grand ecart relatif 5.753e-10', 'var    plus grand ecart relatif 1.951e-09')),
        ('base tronquee', lb, ("['3.00', '3.00', '3.00'] ; avec ['4.00', '4.00', '4.00']", 'plus grand ecart 1.810e-15', 'ecart relatif au saut lui-meme 4.224e-15', 'ecart relatif au saut lui-meme 3.268e-15',
                               'ecart relatif au saut lui-meme 1.235e-15', 'ecarts relatifs 4.71e-05 1.86e-04 7.35e-04 ; rapports 3.95 3.95', 'ecarts relatifs 7.44e-03 2.92e-02 1.13e-01 ; rapports 3.92 3.87',
                               'hermiticite de V sur le vrai operateur : ecart relatif max 0.000e+00', 'B 78 etats',
                               'EPREUVE SUR LA BASE TRONQUEE : hermiticite TIENT ; formule contre l exact TIENT ; chemins contre formule dense TIENT ; sauts lointains j = 3 et 5 contre l exact TIENT')),
        ('etape 1', le, ('2921 feuilles, 4 differentes (non numeriques : 0), plus grand ecart relatif 4.441e-16', 'mediane 0.0622 (de 0.0172 a 0.1155)', 'mediane 0.0205 (de 0.0063 a 0.0661)',
                         '136 etats, mediane 0.0008, p90 0.0087', 'max 0.0264', 'six points      C :  72 etats, mediane 0.0006, p90 0.0030, max 0.0057'))):
    for x in xs:
        if x not in lg:
            arrets.append('journal %s : %r absent' % (nom, x))
for x in ('1.2e-11', '1.1e-11', '1.0e-14', '6e-16', '5.8e-10', '2.0e-9', '3.00', '4.00', '1.8e-15', '1.4e-14', '3.8e-13', '0.0622', '0.0205', '0.0264', '0.0057', '4.4e-16', '2921', '3.92, 3.87', '3.95, 3.95',
          'des Cloizeaux', 'D-LOI-4', 'M-1', 'ne contresigne rien', 'attend la carte', 'E19'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for nom, p, att in (('moteur', REG + 'm17_chaine_v17.py', '82a0be882568fe0c'), ('bloc d ordre 2', REG + 'chaine_ordre2_bloc_machine1_v1.py', '7cd5977bc27bebc1')):
    got = emp(open(p, 'rb').read())[0]
    if got != att:
        arrets.append('canon %s : %s, attendu %s' % (nom, got, att))
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
    'MANIFESTE %s -- CONTROLE (i) DE MACHINE 2 : LE TERME D ORDRE 3 DE LA NOTE HORS CHAINE DE MACHINE 1 REDERIVE PAR MON CODE (formule 3.1 contre l effectif exact d un jouet et d une base tronquee du '
    'vrai operateur ; chemins explicites ; T3, W3, W5 contre ses tables aux 132 etats juges du delta 98 : 1.2e-11 au pire ; sa chaine d ordre 3 : G_c3 a 5.8e-10) ET REJEU DE L ETAPE 1 sur mes pieces. '
    '1D seulement, aucune largeur 2D ; ne contresigne rien. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : note hors chaine de machine 1 84fce9a6faf99c5b ; son lot e93f1898dcd78a8f ; moteur 82a0be882568fe0c ; bloc d ordre 2 7cd5977bc27bebc1 ; registre 8d54bf9 ; mon verdict 2cd1f84efa02f2ab\n')
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
