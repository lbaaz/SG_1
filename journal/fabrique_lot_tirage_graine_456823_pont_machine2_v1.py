# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'TIRAGE DU GEL PONT SUR LA GRAINE 456823' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-17. Meme squelette que fabrique_lot_certification_gel_pont_partie1_machine2_v1.py (non edite).
Aucune 2D a ces w2 ; aucun depot.
Usage : py -3.11 -I fabrique_lot_tirage_graine_456823_pont_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture)
et nomme le canon de CHAQUE piece ; aucune fuite de vie privee ; LF dans les .py, .md et .json ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'certif_gel_pont_partie1_machine2/'
NOM = 'lot_machine2_2026-11-17_tirage_graine_456823_gel_pont_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_tirage_graine_456823_gel_pont_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_tirage_graine_456823_gel_pont_machine2_v1.md'
SELF = 'fabrique_lot_tirage_graine_456823_pont_machine2_v1.py'
PIECES = [D + n for n in (
    'tirage_graine_456823_machine2_v1.log', 'tirage_graine_456823_code_m1_machine2_v1.log', 'controle_hachage_sha256sum_graine_456823_machine2_v1.log',
    'cellules_tirees_machine2_v1.py', 'cellules_tirees_graine_456823_machine2_v1.log', 'cellules_tirees_graine_456823_machine2_v1_premier_passage_eligibilite_par_cellule.log',
    'table_commune_pont_v1.json', 'tirage_pont_machine2_v1.py')] + [SELF]
NOMBRES = [
    ('tirage_graine_456823_machine2_v1.log', 'MG rang 0 : sha256 = bab2ed478849ce6c... ; modulo 8 = 3 -> w2 = 1.985 ELIGIBLE'),
    ('tirage_graine_456823_machine2_v1.log', 'PG rang 0 : sha256 = 7ba5f5c18c4df1e2... ; modulo 8 = 7 -> w2 = 2.019 ELIGIBLE'),
    ('tirage_graine_456823_machine2_v1.log', 'RESULTAT : MG3 : w2 = 1.985, g = 3.63872e-03 ; MG4 : w2 = 1.985, g = 2.77765e-03 ; MG5 : w2 = 1.985, g = 2.20823e-03 ; PG3 : w2 = 2.019, g = 5.23478e-03 ; PG4 : w2 = 2.019, g = 3.99601e-03 ; PG5 : w2 = 2.019, g = 3.17683e-03'),
    ('tirage_graine_456823_code_m1_machine2_v1.log', 'tables : 2 ; w2 eligibles dans toutes : MG 5 sur 8, PG 8 sur 8'),
    ('tirage_graine_456823_code_m1_machine2_v1.log', 'creneau MG rang 0 : numero 3 sur 8 -> w2 = 397/200 (1.985) : ELIGIBLE, retenu'),
    ('tirage_graine_456823_code_m1_machine2_v1.log', 'TIRAGE : 6 cellules'),
    ('controle_hachage_sha256sum_graine_456823_machine2_v1.log', 'sha256sum(456823|MG|0) = bab2ed478849ce6c... ; modulo 8 = 3'),
    ('controle_hachage_sha256sum_graine_456823_machine2_v1.log', 'sha256sum(456823|PG|0) = 7ba5f5c18c4df1e2... ; modulo 8 = 7'),
    ('cellules_tirees_graine_456823_machine2_v1.log', 'PG5 2.019 0.019 3.17683e-03 5 0.0961 0.0063 0.0219 0.0384 | 27 +0.0616 | 1 +0.0081'),
    ('cellules_tirees_graine_456823_machine2_v1.log', 'MG5 1.985 0.015 2.20823e-03 5 0.0743 0.0026 0.0110 0.0869 | 9 +0.0131 | 21 +0.0190'),
    ('cellules_tirees_graine_456823_machine2_v1.log', 'le w2 tire de MG a le plus grand |delta| parmi les w2 eligibles de MG : True ; celui de PG a le plus grand |delta| parmi les w2 eligibles de PG : True'),
    ('cellules_tirees_graine_456823_machine2_v1_premier_passage_eligibilite_par_cellule.log', 'le w2 tire de MG a le plus grand |delta| parmi les eligibles de MG : False'),
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
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
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
for j, s in NOMBRES:
    if norm(s) not in norm(lit(D + j)):
        arrets.append('le journal %s ne porte pas %r' % (j, s))
    if norm(s) not in norm(note):
        arrets.append('la note ne porte pas %r' % s)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
elif not arrets:
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES + [NOTE]:
    brut = open(os.path.join(ICI, p), 'rb').read()
    for f in fuites(p, brut):
        arrets.append('FUITE de vie privee : %s' % (f,))
    if b'\r' in brut and p.endswith(('.py', '.md', '.json')):
        arrets.append('fins de ligne CRLF dans %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- LE TIRAGE du gel "pont" (premiere partie) sur la GRAINE 456823 par machine 2 : six cellules (MG3, MG4, MG5 a w2 = 1.985 ; PG3, PG4, PG5 a w2 = 2.019), recoupees par ton code et par sha256sum ; '
    'les nombres des six cellules lus dans mes details. AUCUNE 2D a ces w2 ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : la graine 456823 donnee par l'operateur dans ma session (17/11, vers 09 h 55) ; la table commune 0c10ddbf2813d809 ; ma certification (lot acfecb6da73f20ae) ; le registre public en tete 2988237\n")
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
