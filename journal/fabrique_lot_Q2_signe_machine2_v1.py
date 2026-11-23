# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'Q2 SIGNE' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-22. Derive de fabrique_lot_Q_sommet_machine2_v1.py (non edite).
Contenu : l'epreuve "Q2" (sa 22h, sections 3 et 4) jouee aux quatre points sacrifies (w2 = 20001/10000 a g = 6e-05 et 4e-05, r_c = 20 et 22 ; w2 = 19999/10000 a g = 3e-04 et 1.5e-04, r_c = 18), ses attendus Q2-1 a Q2-4 ecrits avant, ma lecture a la lettre ;
ma verification a une dimension de sa declaration ; le recoupement apres coup du lecteur et de deux chaines aux neuf points lus. Classe 3 : aucun gel, aucun depot, aucun verdict.
Usage : py -3.11 -I fabrique_lot_Q2_signe_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII et nomme le canon de CHAQUE piece ; les blocs recopies sont LUS dans les journaux ; les nombres cites sont relus dans le journal qui les porte ;
aucune fuite de vie privee ; chemins de disque masques ; CRLF -> LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-22_Q2_signe_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_Q2_signe_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_Q2_signe_machine2_v1.md'
GAB = 'POUR_MACHINE1_Q2_signe_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_Q2_signe_machine2_v1.py'
C = 'certif_relecteur_machine2/'
EP_LOG, V1D_LOG, AC_LOG = C + 'epreuve_Q2_machine2_v1.log', C + 'verifie_Q2_1d_machine2_v1.log', C + 'apres_coup_Q_Q2_ordre1_machine2_v1.log'
SO = C + 'Q2_sorties/'
IDS = ['Q2a', 'Q2b', 'Q2c', 'Q2d']
JSON_Q = [SO + 'lect2D_%s_%s.json' % (i, q) for i in IDS for q in ('fantome', 'jumeau')]
LOGS_Q = [SO + 'log_%s_%s.txt' % (i, q) for i in IDS for q in ('fantome', 'jumeau')]
PIECES = [C + 'epreuve_Q2_machine2_v1.py', EP_LOG, C + 'verifie_Q2_1d_machine2_v1.py', V1D_LOG, C + 'apres_coup_Q_Q2_ordre1_machine2_v1.py', AC_LOG,
          C + 'chaine_premier_ordre_machine2_v1.py', C + 'jobs_Q2_machine2_v1.txt', C + 'lance_Q2_machine2_v1.out', C + 'lance_lect2D_machine2_v3_abs.sh', C + 'lecteur_2D_pilote_machine2_v1.py', SO + 'debut.txt'] + JSON_Q + LOGS_Q + [SELF]
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


ind = lambda ls: '\n'.join(('    ' + l) if l else '' for l in ls)
note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('le gabarit a des CRLF')
for marque, chemin in (('@@EP2@@', EP_LOG), ('@@AC2@@', AC_LOG), ('@@V1D@@', V1D_LOG)):
    bloc = [l for l in lit(chemin).split('\n') if l.strip()]
    if not bloc:
        arrets.append('bloc vide : %s' % marque)
    note = note.replace(marque, ind(bloc))
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
LOGS = ' '.join(norm(lit(p)) for p in (EP_LOG, V1D_LOG, AC_LOG))
NOMBRES = [('Q2-1 quatre points QUALIFIES : TENU', 'QUALIFIES par la feuille deposee'),
           ('Q2-a 0.00019 ; Q2-b 0.00034 ; Q2-c 0.00002 ; Q2-d 0.00008', '0.00019 (Q2-a), 0.00034 (Q2-b), 0.00002 (Q2-c), 0.00008 (Q2-d)'),
           ('ln[Gamma_pl(Q2c) / Gamma_pl(Q-e)] = +0.00121', '= +0.00121'),
           ('ln[Gamma_pl(Q2d) / Gamma_pl(Q-f)] = +0.00212', '= +0.00212'),
           ('ecarts de mes lectures a ces valeurs : +0.00000 et +0.00001', 'ecarts de +0.00000 et +0.00001'),
           ('-> NON REALISE', "N'EST REALISE NULLE PART"),
           ('Gamma_pl(A) / g = 0.000825 ; / t_0 = 0.008082', 'Gamma_pl / g = 0.000825 et 0.000051 ; Gamma_pl / t_0 = 0.008082'),
           ('Gamma_pl(A) / g = 0.000051 ; / t_0 = 0.000504', '0.000504'),
           ('mini dans la fenetre de A : 0.9943', '0.9943'), ('mini dans la fenetre de A : 0.9980', '0.9980'),
           ('(= 8.46e-36 Gamma_pl)', '8.46e-36 Gamma_pl'),
           ('Q2-a 20001/10000 6e-05 4.94717e-08 4.94741e-08 4.94622e-08 | -0.00005 +0.00019 -0.00024', '-0.00024'),
           ('Q2-b 20001/10000 4e-05 2.05518e-09 2.05525e-09 2.05449e-09 | -0.00003 +0.00034 -0.00037', '-0.00037'),
           ('plus grand ecart relatif sur eta0 : 0.0e+00', 'ecart relatif 0'),
           ('ln[G1er(Q2-c) / G1er(Q-e, w2 = 2.0001)] = +0.00117', '+0.00117'),
           ('ln[G1er(Q2-d) / G1er(Q-f, w2 = 2.0001)] = +0.00205', '+0.00205')]
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
for cle in ('074b131287ad2b6f', '82a0be882568fe0c', 'd5cc48f48e37af99', '83701094e6a2b965', '47a84eae6052f006'):
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

lignes = [
    'MANIFESTE %s -- EPREUVE "Q2" (sa 22h, sections 3 et 4) jouee aux quatre points sacrifies (w2 = 20001/10000 a g = 6e-05 et 4e-05, r_c = 20 et 22 ; w2 = 19999/10000 a g = 3e-04 et 1.5e-04, r_c = 18), ses attendus Q2-1 a Q2-4 ecrits avant et lus a la lettre ; ma verification a une dimension de sa declaration ; '
    'le recoupement apres coup du lecteur et de deux chaines aux neuf points lus. HORS CHAINE, classe 3, non certifie ; aucun gel ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : son enveloppe 22h (lot 074b131287ad2b6f), lue comme donnees ; mon lot c58c2b3f533c516b (Q) et ses JSON ; le registre public en tete 055be58 : moteur 82a0be882568fe0c, bloc LECTEUR CREUX d5cc48f48e37af99, feuille 83701094e6a2b965 ; mon pilote 47a84eae6052f006\n")
lignes.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d portees en LF ; %d pieces dont des chemins de disque ont ete masques\n' % (len(PIECES) + 1, nb_lf, nmask))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
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
