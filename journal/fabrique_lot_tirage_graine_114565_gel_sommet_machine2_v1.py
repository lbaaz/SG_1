# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'TIRAGE, GRAINE 114565, GEL SOMMET' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-22. Derive de fabrique_lot_certification_gel_sommet_partie1_machine2_v1.py (non edite).
Contenu : mon tirage reel (graine donnee par l'operateur) de la premiere partie du gel "sommet" : huit w2, cinquante-six cellules ; sa verification par une seconde ecriture ; une observation sur eta0. Aucun calcul 2D, aucun gel, aucun depot.
Usage : py -3.11 -I fabrique_lot_tirage_graine_114565_gel_sommet_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-22_tirage_graine_114565_gel_sommet_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_tirage_graine_114565_gel_sommet_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_tirage_graine_114565_gel_sommet_machine2_v1.md'
GAB = 'POUR_MACHINE1_tirage_graine_114565_gel_sommet_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_tirage_graine_114565_gel_sommet_machine2_v1.py'
C = 'certif_gel_sommet_partie1_machine2/'
L = {n: C + n for n in ('tirage_graine_114565_sommet_machine2_v1.log', 'verifie_tirage_graine_114565_sommet_machine2_v1.log', 'verifie_eta0_forme_sommet_machine2_v1.log')}
PIECES = [C + 'table_commune_sommet_machine2_v1.json', C + 'tirage_sommet_machine2_v1.py', L['tirage_graine_114565_sommet_machine2_v1.log'], C + 'verifie_tirage_graine_sommet_machine2_v1.py', L['verifie_tirage_graine_114565_sommet_machine2_v1.log'],
          C + 'verifie_eta0_forme_sommet_machine2_v1.py', L['verifie_eta0_forme_sommet_machine2_v1.log'], SELF]
arrets = []
for p in PIECES + [GAB]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if len(set(PIECES)) != len(PIECES):
    arrets.append('doublon dans la liste des pieces')
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


MASQUE = re.compile(rb'(?<![A-Za-z0-9])[A-Za-z]:[\\/][^\s"\']*')
CONT = {}
nmask = 0
for p in PIECES:
    brut = open(os.path.join(ICI, p), 'rb').read()
    if b'\r\n' in brut:
        lf = brut.replace(b'\r\n', b'\n')
        if emp(lf)[0] != emp(brut)[0]:
            arrets.append('le canon B change a la normalisation LF : %s' % p)
        brut = lf
    if p.endswith(('.log', '.md', '.txt', '.out')) and MASQUE.search(brut):
        brut = MASQUE.sub(b'<chemin>', brut)
        nmask += 1
    CONT[p] = brut
nb_lf = sum(1 for p in PIECES if open(os.path.join(ICI, p), 'rb').read() != CONT[p])


def lit(p):
    return CONT[p].decode('utf-8')


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'), ('PANIER', 'CLIENT'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


def lignes(p):
    return [l for l in lit(p).split('\n') if l.strip()]


ind = lambda ls: '\n'.join(('    ' + l) if l else '' for l in ls)
note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('le gabarit a des CRLF')
BLOCS = (('@@TIR@@', lignes(L['tirage_graine_114565_sommet_machine2_v1.log'])), ('@@VER@@', lignes(L['verifie_tirage_graine_114565_sommet_machine2_v1.log'])), ('@@ETA@@', lignes(L['verifie_eta0_forme_sommet_machine2_v1.log'])))
for marque, bloc in BLOCS:
    if not bloc:
        arrets.append('bloc vide : %s' % marque)
    note = note.replace(marque, ind(bloc))
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
LOGS = ' '.join(norm(lit(p)) for p in L.values())
NOMBRES = [('sha256("114565|MP|0") = 075d562d52484be8... ; modulo 15 = 9 -> w2 = 1.99989', 'MPa = 199989/100000 (1.99989)'),
           ('=> MPb : w2 = 199993/100000 = 1.99993', 'MPb = 199993/100000 (1.99993)'),
           ('=> PPa : w2 = 25001/12500 = 2.00008', 'PPa = 25001/12500 (2.00008)'),
           ('=> PPb : w2 = 200011/100000 = 2.00011', 'PPb = 200011/100000 (2.00011)'),
           ('=> MGa : w2 = 6249/3125 = 1.99968', 'MGa = 6249/3125 (1.99968)'),
           ('=> MGb : w2 = 49989/25000 = 1.99956', 'MGb = 49989/25000 (1.99956)'),
           ('=> PGa : w2 = 200039/100000 = 2.00039', 'PGa = 200039/100000 (2.00039)'),
           ('=> PGb : w2 = 12503/6250 = 2.00048', 'PGb = 12503/6250 (2.00048)'),
           ('(2) cellules du journal : 56 ; retrouvees identiques dans ma table : 56 ; dans la table de machine 1 : 56', '56 cellules sont retrouvees'),
           ('(1) seconde ecriture contre le journal de mon tirage : IDENTIQUES', 'seconde ecriture'),
           ('cellules ou |w2 - 2| l emporterait : 0', "emporte a aucune des 560 cellules")]
for sj, sn in NOMBRES:
    if norm(sj) not in LOGS:
        arrets.append('le journal ne porte pas %r' % sj)
    if norm(sn) not in norm(note):
        arrets.append('la note ne porte pas %r' % sn)
if '@@' in note:
    arrets.append('marque non remplacee dans la note')
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(CONT[p])[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for cle in ('21e9bddfe5db83b2', '1e5039cade55d13f', '77ce2a6c7e867011'):
    if cle not in note:
        arrets.append('la note ne cite pas le canon %s' % cle)
for p in PIECES:
    for f in fuites(p, CONT[p]):
        arrets.append('FUITE de vie privee : %s' % (f,))
for f in fuites(NOTE, note.encode('ascii')):
    arrets.append('FUITE de vie privee : %s' % (f,))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
CONT_NOTE = note.encode('ascii')

lg = [
    'MANIFESTE %s -- MON TIRAGE REEL DE LA PREMIERE PARTIE DU GEL "SOMMET" (piece 1e5039cade55d13f), graine 114565 donnee par l operateur : huit w2, cinquante-six cellules, aux rangs 0 et 1 des quatre creneaux ; verification par une seconde ecriture ; observation sur eta0. '
    'AUCUN CALCUL 2D ; aucun gel ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lg.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lg.append("\nentrants : ma certification (lot 21e9bddfe5db83b2) et sa table commune ; la table JSON de machine 1 77ce2a6c7e867011 (lue pour comparer les cellules, pas son tirage) ; le registre public en tete 055be58\n")
lg.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d portees en LF ; %d pieces dont des chemins de disque ont ete masques\n' % (len(PIECES) + 1, nb_lf, nmask))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lg)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    z.writestr(NOTE, CONT_NOTE)
    for p in PIECES:
        z.writestr(p, CONT[p])
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read(), NOTE: CONT_NOTE}
    attendu.update(CONT)
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets ; %d portees en LF ; %d masquees' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP), nb_lf, nmask))
