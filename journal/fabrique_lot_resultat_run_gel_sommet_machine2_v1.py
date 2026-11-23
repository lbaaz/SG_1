# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'RESULTAT DU RUN, GEL SOMMET' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-23. Derive de fabrique_lot_certification_gel_sommet_partie2_machine2_v1.py (non edite).
Contenu : le dossier du run (joue UNE fois, sur l'ordre ecrit de l'operateur), le verdict de la feuille de machine 1 (S1 TENU), mon juge independant rejoue sur le run, la comparaison de l'etage A au pre-vol, les annonces recomptees. Aucun depot.
Usage : py -3.11 -I fabrique_lot_resultat_run_gel_sommet_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-23_resultat_run_gel_sommet_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_run_gel_sommet_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_run_gel_sommet_machine2_v1.md'
GAB = 'POUR_MACHINE1_resultat_run_gel_sommet_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_resultat_run_gel_sommet_machine2_v1.py'
C = 'certif_gel_sommet_partie2_machine2/'
RUN = C + 'run_sommet_2026-11-23/'
LG = {n: C + n for n in ('rejeu_juge_independant_run_machine2_v1.log', 'comparaison_etage_A_prevol_run_machine2_v1.log', 'comptes_annonces_run_machine2_v1.log')}
PV = RUN + 'pilote_gel_sommet.log'
PIECES = [RUN + f for f in sorted(os.listdir(os.path.join(ICI, C, 'run_sommet_2026-11-23')))]
PIECES += [C + 'lance_run_machine2_v1.out', C + 'certification_feuille_sommet_machine2_v1.py', C + 'rejeu_juge_independant_run_machine2_v1.py', LG['rejeu_juge_independant_run_machine2_v1.log'],
           C + 'comparaison_etage_A_prevol_run_machine2_v1.py', LG['comparaison_etage_A_prevol_run_machine2_v1.log'], C + 'comptes_annonces_run_machine2_v1.py', LG['comptes_annonces_run_machine2_v1.log'], SELF]
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
BLOCS = (('@@PILOTE@@', lignes(PV)), ('@@REJEU@@', lignes(LG['rejeu_juge_independant_run_machine2_v1.log'])), ('@@ETAGEA@@', lignes(LG['comparaison_etage_A_prevol_run_machine2_v1.log'])), ('@@ANNONCES@@', lignes(LG['comptes_annonces_run_machine2_v1.log'])))
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
LOGS = ' '.join(norm(lit(p)) for p in list(LG.values()) + [PV])
NOMBRES = [('VERDICT : S1 TENU', 'VERDICT : S1 TENU'), ('CANON DU VERDICT : 2c39171a593d95df', '2c39171a593d95df'),
           ('FIN DU PILOTE ; duree totale 2944 s', '(2944 s)'), ('TEMOINS POSITIFS : TIENNENT (9 sur 9)', 'TIENNENT, 9 sur 9'),
           ('plus grand |ln q| : 0.00025', '0.00025'), ('plus petite marge T - b - |ln q| : 0.00436', '0.00436'), ('plus grande bande b : 0.00556', '0.00556'), ('plus grand etalement s du lecteur : 0.00219', '0.00219'),
           ('lectures non suivies du fantome : 9 sur 2688 ; du jumeau : 0 sur 2688', 'neuf sur 2688 au fantome, zero sur 2688 au jumeau'),
           ('poids du site (0, 0) minimal sur toutes les lectures suivies du fantome : 0.7181', '0.7181'),
           ('ln q negatif (lecteur au-dessus de la chaine) a 32 cellules', 'a 32 cellules sur 56'),
           ('A-7 cellules de barriere (kappa 0.0363 et 0.0530) : 16 ; ln q negatif a 10', 'dix sur seize'),
           ('ecart du rapport lu au rapport de la chaine : 0.00003 0.00001 0.00006 0.00001 0.00003 0.00001 0.00003', 'de 0.00001 a 0.00006'),
           ('ACCORD DE MON JUGE ET DE SA FEUILLE SUR LE RUN REEL : OUI', 'rend le meme verdict'),
           ('18 fichiers compares : trajectoires identiques', "identiques a l'octet"),
           ('A-4 cellules lues (qualifiees et temoin tenu) : 56 sur 56', 'toutes QUALIFIEES')]
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
for cle in ('1e5039cade55d13f', '81a2febcfce49007', 'ed4c3886b17fcdc3', 'ac934e0caaa59c08', 'b7f328b916ba720d', '2c39171a593d95df'):
    if cle not in note:
        arrets.append('la note ne cite pas le canon %s' % cle)
for p in PIECES:
    for f in fuites(p, CONT[p]):
        arrets.append('FUITE de vie privee : %s' % (f,))
for f in fuites(NOTE, note.encode('ascii')):
    arrets.append('FUITE de vie privee : %s' % (f,))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets[:40]:
        print('  -', a)
    raise SystemExit(1)
open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
CONT_NOTE = note.encode('ascii')

lg = [
    'MANIFESTE %s -- LOT DE RESULTAT DU RUN DU GEL "SOMMET" (pieces 1e5039cade55d13f et 81a2febcfce49007) : le dossier du run joue UNE fois par le pilote de machine 1 (ed4c3886b17fcdc3) et sa feuille (ac934e0caaa59c08) le 23/11/2026, sur l\'ordre ecrit de l\'operateur : les fichiers de l\'etage A, les 130 fichiers de lecture et leurs consoles, la garde, le verdict (S1 TENU), '
    'les journaux et le journal du pilote ; mon juge independant rejoue sur le run ; la comparaison de l\'etage A au pre-vol ; les annonces recomptees. AUCUN DEPOT. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lg.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lg.append("\nentrants : son enveloppe 22k (lot a2dc5cb2b9c3da0d : la piece de gel 81a2febcfce49007, sa feuille ac934e0caaa59c08, son pilote ed4c3886b17fcdc3, sa table gelee 4238e2b262119f83) ; ma certification (lot b7f328b916ba720d) et son pre-vol ; le registre public en tete 055be58\n")
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
