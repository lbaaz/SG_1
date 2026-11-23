# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CONTRESEING DE L'ACTE DU GEL SOMMET' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-23. Derive de fabrique_lot_resultat_run_gel_sommet_machine2_v1.py (non edite).
Contenu : mon controle de l'acte (journal_delta_nn_sommet_v1, 417cf051cc04671b, lot fcfeb710fc3910cc) : 36 nombres et faits refaits de mes fichiers ; deux morsures de texte, deux suggestions ; le calcul a une dimension, apres le run, qui donne la cause du residu par kappa. Aucun calcul 2D, aucun depot.
Usage : py -3.11 -I fabrique_lot_contreseing_acte_gel_sommet_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-23_contreseing_acte_gel_sommet_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_gel_sommet_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_gel_sommet_machine2_v1.md'
GAB = 'POUR_MACHINE1_contreseing_acte_gel_sommet_machine2_v1.gabarit.txt'
SELF = 'fabrique_lot_contreseing_acte_gel_sommet_machine2_v1.py'
C = 'certif_acte_gel_sommet_machine2/'
LG = {n: C + n for n in ('verifie_acte_gel_sommet_machine2_v1.log', 'residu_par_kappa_apres_coup_machine2_v1.log')}
PIECES = [C + 'verifie_acte_gel_sommet_machine2_v1.py', LG['verifie_acte_gel_sommet_machine2_v1.log'], C + 'verifie_acte_gel_sommet_machine2_v1_premier_passage_deux_criteres_faux.log',
          C + 'residu_par_kappa_apres_coup_machine2_v1.py', LG['residu_par_kappa_apres_coup_machine2_v1.log'], 'certif_relecteur_machine2/chaine_premier_ordre_machine2_v1.py',
          'livraison_23a_acte_gel_sommet/authentification_lots_machine2_v2.log', SELF]
arrets = []
for p in PIECES + [GAB]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
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
for marque, chemin in (('@@ACTE@@', LG['verifie_acte_gel_sommet_machine2_v1.log']), ('@@RESIDU@@', LG['residu_par_kappa_apres_coup_machine2_v1.log'])):
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
LOGS = ' '.join(norm(lit(p)) for p in list(LG.values()) + [C + 'verifie_acte_gel_sommet_machine2_v1_premier_passage_deux_criteres_faux.log'])
NOMBRES = [('BILAN : 36 controles tenus, 0 morsures', 'Trente-six controles refaits, trente-six tenus'),
           ('BILAN : 34 controles tenus, 2 morsures', 'deux criteres de MON test etaient faux'),
           ('plus grand |ln(lu / ma chaine du premier ordre)| aux 56 cellules : 0.00019 ; mediane : 0.00005', 'son plus grand ecart est 0.00019 (mediane 0.00005)'),
           ('correlation, cellule par cellule, entre ln q (residu de l acte) et ln(G3* / ma chaine) : 0.7881', 'est de 0.7881'),
           ('plus grand |ln(G3* / ma chaine du premier ordre)| : 0.00043 (cellule PGb2)', 'ecart entre la colonne G3* et une chaine'),
           ('-0.00043 -0.00002 -0.00024', '-0.00024 a kappa = 0.0530'),
           ('-0.00018 +0.00018 +0.00000', 'va de -0.00002 a +0.00001'),
           ('plus grand ecart relatif sous A, k = -3 a 4, aux 56 cellules : 0.00486', '0.00486 au plus'),
           ('|delta| en 1e-5 : [7, 8, 11, 32, 39, 44, 48] ; 7 valeurs distinctes pour huit w2', '7, 8, 11, 32, 39, 44, 48'),
           ('journal : etage0 20 s, ancres 846 s, etage1 897 s', 'etage A 20 s, 846 s, 897 s'),
           ('moi : bande max 0.00556 ; cellule MGb1, marge 0.00436', 'marge de MGb1'),
           ('moi : champ poids_min 0.5348 ; lectures suivies 0.7181', '0.5348 et 0.7181')]
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
for cle in ('417cf051cc04671b', 'fcfeb710fc3910cc', 'c462991d2484064c', 'b7f328b916ba720d', 'c58c2b3f533c516b'):
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
    'MANIFESTE %s -- CONTRESEING DE L\'ACTE DU GEL "SOMMET" (journal_delta_nn_sommet_v1, 417cf051cc04671b, lot fcfeb710fc3910cc) : trente-six nombres et faits refaits de mes fichiers, tous tenus ; deux morsures de texte et deux suggestions ; le calcul a une dimension, apres le run, de la cause du residu par kappa (la colonne G3*, pas le lecteur). '
    'AUCUN CALCUL 2D ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_du_zip (octets portes par le zip, fins de ligne LF, chemins de disque masques dans les journaux)  octets_B  octets_zip  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(CONT_NOTE if p == NOTE else CONT[p])
    lg.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lg.append("\nentrants : son enveloppe 23a (lot fcfeb710fc3910cc : l'acte 417cf051cc04671b et sa note) lue comme un texte ; mon lot de resultat 735b9394013b02db et le dossier du run ; la table gelee 4238e2b262119f83 ; le delta 102 depose (registre 055be58)\n")
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
