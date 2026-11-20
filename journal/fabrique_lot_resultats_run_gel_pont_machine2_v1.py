# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'RESULTATS DU RUN DU GEL PONT, SECONDE PARTIE' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-18. Meme squelette que fabrique_lot_certification_gel_pont_partie2_machine2_v1.py (non edite).
Le lot porte : les sorties du run (dossier run_gel_pont_machine2_2026-11-18 entier), le pilote et les scripts de comparaison, l'essai du pilote au point sacrifie, les journaux. Aucune sortie synthetique. Aucun depot.
Usage : py -3.11 -I fabrique_lot_resultats_run_gel_pont_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII, nomme le canon de CHAQUE piece ; les blocs que la note recopie (verdict, comparaisons, journal du run) sont LUS dans les journaux, non retapes ;
les nombres que la note cite d'elle-meme sont relus dans le journal qui les porte ; aucune fuite de vie privee (noms, lettres de lecteur avec barre ET antislash, adresses) ; CRLF -> LF dans le ZIP (canon B inchange, verifie piece par piece) ;
ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
RUN = 'run_gel_pont_machine2_2026-11-18'
D = 'certif_gel_pont_partie2_machine2/'
NOM = 'lot_machine2_2026-11-18_resultats_run_gel_pont_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultats_run_gel_pont_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultats_run_gel_pont_machine2_v1.md'
GAB = 'POUR_MACHINE1_resultats_run_gel_pont_machine2_v1.gabarit.txt'      # le gabarit (avec ses marques @@) ; la note finale est ECRITE a partir de lui, il ne va pas dans le lot
SELF = 'fabrique_lot_resultats_run_gel_pont_machine2_v1.py'
SCRIPTS = ['run_pont_machine2_v1.py', 'essai_feuilles_pilote_machine2_v1.py', 'chaine_pont_machine2_v1.py', 'feuilles_pont_machine2_v1.py', 'compare_feuilles_machine2_v1.py', 'compare_run_machine2_v1.py',
           'compare_densite_verdict_run_machine2_v1.py', 'verifie_pieces_m1_machine2_v1.py']
JOURNAUX = ['journaux/' + n for n in (
    'run_pont_stdout_machine2_v1.log', 'run_pont_selftest_machine2_v1.log', 'run_pont_plan_machine2_v1.log', 'run_pont_essai_stdout_machine2_v1.log', 'essai_feuilles_pilote_machine2_v1.log',
    'compare_run_machine2_v1.log', 'compare_densite_verdict_run_machine2_v1.log', 'compare_feuilles_sur_run_premiere_passe_cle_defectueuse_machine2_v1.log', 'verifie_pieces_m1_machine2_v1.log')]
arrets = []


def parcourt(rel):
    base = os.path.join(ICI, rel)
    return sorted(os.path.relpath(os.path.join(d, f), ICI).replace(os.sep, '/') for d, _, fs in os.walk(base) for f in fs)


# nom dans le lot -> chemin source (relatif a ICI)
SRC = {}
for p in parcourt(RUN):
    SRC[p] = p
for n in SCRIPTS + JOURNAUX:
    SRC[D + n] = D + n
for p in parcourt(D + 'essai_pilote'):
    SRC[p] = p
SRC[SELF] = SELF
PIECES = sorted(SRC)
for p in PIECES + [GAB]:
    if not os.path.isfile(os.path.join(ICI, SRC.get(p, p))):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

SUFFIXES_TEXTE = ('.py', '.md', '.json', '.jsonl', '.log', '.txt')


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


# contenu tel qu'il ira dans le ZIP : LF (CRLF -> LF) pour les textes ; le canon B doit etre inchange
CONT = {}
for p in PIECES:
    brut = open(os.path.join(ICI, SRC[p]), 'rb').read()
    if p.endswith(SUFFIXES_TEXTE) and b'\r\n' in brut:
        lf = brut.replace(b'\r\n', b'\n')
        if emp(lf)[0] != emp(brut)[0]:
            arrets.append('le canon B change a la normalisation LF : %s' % p)
        brut = lf
    CONT[p] = brut
nb_crlf = sum(1 for p in PIECES if open(os.path.join(ICI, SRC[p]), 'rb').read() != CONT[p])


def lit(p):
    return CONT[p].decode('utf-8')


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'), ('PANIER', 'CLIENT'))]
# seule exception, nommee : le selftest du pilote essaie son masque de chemins sur deux chemins FACTICES (ni personnels ni reels)
EXC_FICHIER = D + 'run_pont_machine2_v1.py'
EXC = b"masque('ecrit C:" + b'\\\\' + b'a' + b'\\\\' + b"b.json et D" + b":/x/y')"


def fuites(nom, octets):
    if nom == EXC_FICHIER:
        if octets.count(EXC) != 1:
            return [(nom, 'litteral factice du selftest absent ou multiple')]
        octets = octets.replace(EXC, b'')
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'(?<![a-z0-9])[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


note = open(os.path.join(ICI, GAB), encoding='ascii', newline='').read()
if '\r' in note:
    arrets.append('la note a des CRLF')
RJ = RUN + '/journaux/'
# blocs recopies TELS QUELS depuis les journaux
verdict = [l for l in lit(RJ + 'verdict.log').split('\n') if l.strip() and not l.startswith('ecrit')]
note = note.replace('@@VERDICT@@', '\n'.join('    ' + l for l in verdict))
logrun = lit(RUN + '/run_pont_machine2.log').split('\n')
sel = [l for l in logrun if l.startswith('[     0 s]') or l.endswith('] 48 jobs') or '48 jobs' in l or 'RUN TERMINE' in l]
note = note.replace('@@LOGRUN@@', '\n'.join('    ' + l for l in sel))
mem = [float(m) for m in re.findall(r'memoire estimee ([0-9.]+) Go', '\n'.join(logrun))]
note = note.replace('@@MEMMAX@@', '%.1f' % max(mem))
ndens = sum(1 for l in logrun if 'complete (12 barreaux)' in l)
nboi = sum(1 for l in logrun if 'toutes les boites sont la' in l)
if (ndens, nboi) != (24, 24):
    arrets.append('comptes du journal du run : %d densites completes et %d jobs de boites complets, attendu 24 et 24 (6 x 4, 6 x 4)' % (ndens, nboi))
note = note.replace('@@NDENS@@', str(ndens)).replace('@@NBOITES@@', str(nboi))
if any(('INCOMPLET' in l or 'ECHEC' in l or 'NON TERMINES' in l or 'ARRET' in l) for l in logrun):
    arrets.append('le journal du run porte INCOMPLET, ECHEC, NON TERMINES ou ARRET')
etat = lit(RUN + '/etat_run.json')
if etat.count('"etat": "fait"') != 48 or '"relances": 0' not in etat or re.search(r'"relances": [1-9]', etat):
    arrets.append('etat_run.json : 48 jobs faits et aucune relance attendus')
cmp1 = [l for l in lit(D + 'journaux/compare_run_machine2_v1.log').split('\n') if l.strip() and l.startswith('boites')]
cmp2 = [l for l in lit(D + 'journaux/compare_densite_verdict_run_machine2_v1.log').split('\n') if l.strip() and not l.startswith(('MG', 'PG'))]
note = note.replace('@@COMPARE@@', '\n'.join('    ' + l for l in cmp1 + cmp2))
# nombres cites par la note d'elle-meme : relus dans le journal qui les porte
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
PREM = D + 'journaux/compare_feuilles_sur_run_premiere_passe_cle_defectueuse_machine2_v1.log'
PIEC = 'pieces au manifeste : 84 ; presentes dans le lot a plat : 84 ; absentes : 0 ; de canon different : 0'
# (piece qui porte le nombre, texte dans cette piece, texte dans la note)
NOMBRES = [(RUN + '/run_pont_machine2.log', '[ 11185 s] RUN TERMINE', '[ 11185 s] RUN TERMINE'),
           (RUN + '/verdict.json', '"pire_part_de_tolerance": 1.0047352980829771', '1.0047352980829771'),
           (RJ + 'verdict.log', 'MG3 (L) TOMBE pire -0.0502 a x = 8 (1.00 de la tolerance)', 'MG3 (L) TOMBE pire -0.0502 a x = 8 (1.00 de la tolerance)'),
           (D + 'journaux/verifie_pieces_m1_machine2_v1.log', PIEC, PIEC),
           (PREM, 'boites : 60 chez moi, 60 chez lui', 'boites : 60 chez moi, 60 chez lui'),
           (PREM, '3.07e-01', '3.07e-01')]
for j, sj, sn in NOMBRES:
    if norm(sj) not in norm(lit(j)):
        arrets.append('la piece %s ne porte pas %r' % (j, sj))
    if norm(sn) not in norm(note):
        arrets.append('la note ne porte pas %r' % sn)
for s_ in ('11185 s', '48 jobs', 'RUN TERMINE', '"relances": 0', 'MG3', 'tolerance'):
    if s_ not in note:
        arrets.append('la note ne porte pas %r' % s_)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(CONT[p])[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
if '@@' in note:
    arrets.append('marque non remplacee dans la note')
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(CONT[p])[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
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
    'MANIFESTE %s -- LES RESULTATS par machine 2 du run du gel "pont", seconde partie (piece de machine 1 de canon 428ac47649de31f3, lot 7bf7982cceade968, rectificatif 5d75dd59784d3811) : sorties du run '
    '(six cellules, 48 jobs), journaux, pilote, comparaison de mes feuilles aux siennes, essai du pilote au point sacrifie. AUCUN depot ; aucune sortie synthetique. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : la piece de machine 1 de canon 428ac47649de31f3 (lot 7bf7982cceade968) et son rectificatif (lot 5d75dd59784d3811) ; ma certification (lot a77b27f763fb69cd) ; la graine 456823 ; la table commune 0c10ddbf2813d809 ; "
              "le registre public en tete 2988237\n")
lignes.append('pieces : %d (compte etabli APRES le dernier ajout) ; %d d\'entre elles ont ete ecrites sous Windows en CRLF et sont portees en LF par le zip (canon B inchange)\n' % (len(PIECES) + 1, nb_crlf))
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
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets ; %d pieces portees en LF' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP), nb_crlf))
