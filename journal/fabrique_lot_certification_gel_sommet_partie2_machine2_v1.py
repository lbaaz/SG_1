# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CERTIFICATION DU GEL SOMMET, PARTIE 2' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-23. Derive de fabrique_lot_certification_gel_sommet_partie1_machine2_v1.py (non edite).
Contenu : ma certification (a) a (f) de la seconde partie du gel "sommet" (piece 81a2febcfce49007, lot a2dc5cb2b9c3da0d) : sa table gelee contre mon tirage et ma table, sa feuille contre mon juge independant (38 scenarios), ses deux bancs rejoues, ses fichiers de travail contre la table,
le PRE-VOL reel de son pilote (aucune cellule lue). Aucune cellule lue, aucun gel, aucun depot.
Usage : py -3.11 -I fabrique_lot_certification_gel_sommet_partie2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; la note est ASCII et nomme le canon de CHAQUE piece ; les blocs recopies sont LUS dans les journaux ; les nombres cites sont relus dans le journal qui les porte ;
aucune fuite de vie privee ; chemins de disque masques ; CRLF -> LF ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-23_certification_gel_sommet_partie2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_sommet_partie2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_sommet_partie2_machine2_v1.md'
GAB = 'POUR_MACHINE1_certification_gel_sommet_partie2_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_certification_gel_sommet_partie2_machine2_v1.py'
C = 'certif_gel_sommet_partie2_machine2/'
LG = {n: C + n for n in ('verifie_table_gelee_sommet_machine2_v1.log', 'certification_feuille_sommet_machine2_v1.log', 'banc_feuille_gel_sommet_rejoue_machine2_v1.log',
                         'banc_pilote_gel_sommet_rejoue_machine2_v1.log', 'verifie_jobs_et_annonces_sommet_machine2_v1.log')}
PV = C + 'prevol_run/pilote_gel_sommet.log'
PIECES = [C + 'verifie_table_gelee_sommet_machine2_v1.py', LG['verifie_table_gelee_sommet_machine2_v1.log'],
          C + 'certification_feuille_sommet_machine2_v1.py', LG['certification_feuille_sommet_machine2_v1.log'],
          C + 'certification_feuille_sommet_machine2_v1_premier_passage.log', C + 'certification_feuille_sommet_machine2_v1_deuxieme_passage_critere_de_refus_et_signes.log',
          LG['banc_feuille_gel_sommet_rejoue_machine2_v1.log'], LG['banc_pilote_gel_sommet_rejoue_machine2_v1.log'],
          C + 'verifie_jobs_et_annonces_sommet_machine2_v1.py', LG['verifie_jobs_et_annonces_sommet_machine2_v1.log'], C + 'lance_prevol_machine2_v1.out']
PIECES += [C + 'prevol_run/' + f for f in sorted(os.listdir(os.path.join(ICI, C, 'prevol_run')))]
PIECES += ['livraison_22k_gel_sommet_partie2/authentification_lots_machine2_v2.log', SELF]
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
BLOCS = (('@@TG@@', lignes(LG['verifie_table_gelee_sommet_machine2_v1.log'])), ('@@CF@@', lignes(LG['certification_feuille_sommet_machine2_v1.log'])),
         ('@@BF@@', lignes(LG['banc_feuille_gel_sommet_rejoue_machine2_v1.log'])[-1:]), ('@@BP@@', lignes(LG['banc_pilote_gel_sommet_rejoue_machine2_v1.log'])[-1:]),
         ('@@JA@@', lignes(LG['verifie_jobs_et_annonces_sommet_machine2_v1.log'])), ('@@PV@@', lignes(PV)))
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
LOGS = ' '.join(norm(lit(p)) for p in list(LG.values()) + [PV, C + 'certification_feuille_sommet_machine2_v1_premier_passage.log'])
NOMBRES = [('RESUME : (a) TIENT ; (b) TIENT ; (e) TIENT', '(a) TIENT : mon tirage'),
           ('plus grand ecart etendue 1.02e-11', "1.0e-11 sur l'etendue"),
           ('ln G3* 1.76e-11', '1.8e-11 sur ln G3*'),
           ('SCENARIOS : 38 ; TIENNENT 38 ; ECHOUENT 0', 'sur 38 scenarios'),
           ('SCENARIOS : 38 ; TIENNENT 37 ; ECHOUENT 1', '37 sur 38'),
           ('BANC DE LA FEUILLE : 30 cas, 30 tenus', '30 cas, 30 tenus'), ('BANC DU PILOTE : 12 cas, 12 tenus', '12 cas, 12 tenus'),
           ('jobs des cellules : 112 lignes generees de la table, 112 dans son fichier ; identiques ligne pour ligne : OUI', '112 + 18 appels'),
           ('appels distincts : 130 sur 130', 'aucun doublon'),
           ('PRE-VOL : la garde tient ; aucune cellule n\'est lue ; rien n\'est juge ; duree totale 1120 s', 'duree 1120 s'),
           ('GARDE : TIENT : les cellules peuvent etre lues', 'la garde TIENT'),
           ('lecteur ancres code=0 duree=750 s', 'ancres 750 s'), ('lecteur etage1 code=0 duree=795 s', 'etage 1 795 s'),
           ('0.00004 ; 0.00032 ; 0.00048 ; 0.00022 ; 0.00028 ; 0.00027 ; 0.00035', 'de 0.00004 a 0.00048'),
           ('-0.00001 ; +0.00006 ; +0.00014 ; +0.00005 ; +0.00008 ; +0.00005 ; +0.00008', 'A-8 : sept rapports miroirs'),
           ('TEMOINS POSITIFS : TIENNENT (9 sur 9)', 'neuf temoins positifs rendent leur reference')]
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
for cle in ('81a2febcfce49007', 'a2dc5cb2b9c3da0d', '47a84eae6052f006', '5b835ce079ce2cf4', '3db782eea5023b31', '83701094e6a2b965'):
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
    'MANIFESTE %s -- CERTIFICATION (a) A (f) DE LA SECONDE PARTIE DU GEL "SOMMET" (piece 81a2febcfce49007, lot a2dc5cb2b9c3da0d) : sa table gelee contre mon tirage et ma table ; sa feuille contre mon juge independant (38 scenarios, cellule par cellule) ; ses deux bancs rejoues ; ses fichiers de travail contre la table ; '
    'le PRE-VOL reel de son pilote (instrument du depot, neuf temoins positifs, garde ; AUCUNE cellule lue). AUCUN CALCUL 2D A UNE CELLULE ; aucun gel ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lg.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lg.append("\nentrants : son enveloppe 22k (lot a2dc5cb2b9c3da0d : la piece de gel 81a2febcfce49007, sa feuille ac934e0caaa59c08, son pilote ed4c3886b17fcdc3, sa table gelee 4238e2b262119f83, ses deux bancs) ; ma certification de la premiere partie (lot 21e9bddfe5db83b2) ; mon tirage (lot 3db782eea5023b31) ; mes sorties de Q et de Q2 ; le registre public en tete 055be58\n")
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
