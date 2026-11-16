# -*- coding: ascii -*-
"""FABRIQUE DU LOT de RESULTAT du run unique du gel 'largeur du vide' (machine 2) -- manifeste + ZIP. 2026-11-16.
Meme squelette que fabrique_lot_certification_gel_vide_partie2_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_resultat_run_gel_vide_machine2_v1.py
Gardes AVANT ecriture : aucune piece vide ; chaque nombre que la note cite est RELU dans un journal (console du pilote, journal du lanceur, comparaison des deux feuilles, analyse, authentification du rectificatif) ;
le verdict de la feuille de m1 est au canon que le pilote a annonce ; ma feuille est au canon annonce ; la table de la note est ECRITE depuis verdict_vide.json (rien n'y est tape a la main) ; la note est ASCII
(verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; ZIP relu bit-identique."""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile
import json

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_resultat_run_gel_vide_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_run_gel_vide_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_run_gel_vide_machine2_v1.md'
SELF = 'fabrique_lot_resultat_run_gel_vide_machine2_v1.py'
R = 'run_gel_vide_machine2/'
RES = 'resultats_run_vide_machine2/'
Z = 'livraison_16i_rectificatif_gel_vide_partie2/'
PIECES = [R + 'lance_run_vide_machine2_v1.py', R + 'lanceur_run_1.log', R + 'console_run_1.log'] \
    + sorted(os.path.relpath(p, ICI).replace(os.sep, '/') for p in glob.glob(os.path.join(ICI, 'run_gel_vide_machine2', 'run_1', '*')) if os.path.isfile(p)) \
    + [RES + 'verdict_vide_feuille_machine2.json', RES + 'compare_feuilles_run_1_machine2_v1.py', RES + 'compare_feuilles_run_1_machine2_v1.log', RES + 'analyse_run_vide_machine2_v1.py', RES + 'analyse_run_vide_machine2_v1.log',
       Z + 'authentifie_rectificatif_m1_machine2_v1.py', Z + 'authentifie_rectificatif_m1_machine2_v1.log', Z + 'rejeu_machine2/verifie_C1_C2_rejoue_machine2.log', Z + 'rejeu_machine2/verifie_C1_C2_rejoue_machine2.json', SELF]
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def lit(p):
    return open(os.path.join(ICI, p), encoding='utf-8', errors='replace').read().replace('\r\n', '\n')


def exige(p, *morceaux):
    t = lit(p)
    for m in morceaux:
        if m not in t:
            arrets.append('journal %s : %r absent' % (p.split('/')[-1], m))


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
    elif os.path.getsize(os.path.join(ICI, p)) == 0:
        arrets.append('piece VIDE : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
nrun = len([p for p in PIECES if p.startswith(R + 'run_1/')])
if nrun != 68:
    arrets.append('le dossier du run porte %d fichiers, attendu 68' % nrun)
if emp(open(os.path.join(ICI, 'certif_gel_vide_partie2_machine2/feuille_vide_machine2_v1.py'), 'rb').read())[0] != 'a6754241629160a7':
    arrets.append("ma feuille n'est plus au canon a6754241629160a7")
if emp(open(os.path.join(ICI, R + 'run_1/verdict_vide.json'), 'rb').read())[0] != '8472dba8919a9b6e':
    arrets.append('verdict_vide.json de la feuille de m1 n est pas au canon 8472dba8919a9b6e annonce par le pilote')
exige(R + 'console_run_1.log', 'INSTRUMENT DU LECTEUR : TIENT ; canon de son verdict cc54f4bc4e175143', 'lecteur etage0                     code=0 duree=20 s', 'lecteur ancres                     code=0 duree=659 s',
      'lecteur etage1                     code=0 duree=700 s', 'ETAGE B : sonde_vide, 28 cellules', 'VERDICT : V1 TENU ; VP TENU', 'CANON DU VERDICT : 8472dba8919a9b6e', 'FIN DU PILOTE ; duree totale 2597 s',
      'V1 (ligne lisible, 16 cellules) : TENU ; tenues 16, tombees 0 [], non jugeables 0, non lues 0', 'VP (ligne profonde, 12 cellules, hors de V1) : TENU ; tenues 12, tombees 0 [], non jugeables 0, non lues 0',
      "ln q du signe de delta a 12 ; du signe de la sous-correction a 19 ; ordre 3 plus pres que l'ordre 1 a 26, que la loi d'echelle a 27 ; plus grand |ln q| de la forme fermee 0.1136")
if lit(R + 'console_run_1.log').count('code=0') != 33 or 'code=1' in lit(R + 'console_run_1.log') or 'ARRET' in lit(R + 'console_run_1.log'):
    arrets.append('la console du pilote ne porte pas 33 codes 0 (4 etage A, 28 cellules, la feuille) ou porte un arret')
exige(R + 'lanceur_run_1.log', 'secteur ACLineStatus=1 (1 = branche) ; batterie 100 %', 'pilote lance, pid', 'FIN DU LANCEUR : le pilote a rendu le code 0 apres 2597 s', 'LANCEUR DU RUN', '2026-11-16 19:13:54', '2026-11-16 19:57:11')
if lit(R + 'lanceur_run_1.log').count(' ok\n') != 12:
    arrets.append('le journal du lanceur ne porte pas 12 canons ok')
exige(RES + 'compare_feuilles_run_1_machine2_v1.log', 'verdict m1 : V1 TENU ; VP TENU | verdict m2 : V1 TENU ; VP TENU | identiques : True', 'jugements, statuts du lecteur et temoins identiques : 28 sur 28',
      'ecart max entre les deux feuilles : ln q 0.00e+00 ; bande 0.00e+00 ; etalement 0.00e+00 ; ln Gamma_pl 0.00e+00', 'DESACCORDS : []')
exige(RES + 'analyse_run_vide_machine2_v1.log', 'ecart max entre les deux ln q sur 28 cellules : 4.26e-09', 'cellules QUALIFIEES : 28 sur 28 ; echecs : 0 ; non lisibles : 0 ; poids minimal sur toutes les cellules : 0.999',
      'temoin (jumeau sans fantome) : tient 28 sur 28 ; lectures suivies [(48, 48)] ; plus grande largeur du jumeau 3.89e-36 ; plus grand rapport au plateau 1.32e-27', 'etalement s du lecteur au vide : min 0.0001 ; mediane 0.0011 ; max 0.0031',
      'plus grand |ln q| 0.0007 (a MG6)', 'plus grand |ln q| 0.0013 (a PG16)', 'plus petite marge T - b - |ln q| 0.0101', 'plus petite marge T - b - |ln q| 0.0398',
      'sous l etendue de la chaine (le residu est alors a l interieur de ce que les 18 variantes d absorbeur laissent indetermine) : 28 sur 28', 'sous la bande b = etendue + s : 28 sur 28',
      "A-7 signe de ln q aux cellules lisibles de MG : positif a 4 ['MG3', 'MG4', 'MG5', 'MG6'] ; negatif a 0 [] -> branche (b)", "tailles : ln q aux MG lisibles = ['+0.0002', '+0.0004', '+0.0005', '+0.0007'] ; etendue de la chaine = ['0.0013', '0.0014', '0.0026', '0.0022']",
      'MG (delta <0) : ln q > 0 a 7 cellules sur 7', 'MP (delta <0) : ln q > 0 a 5 cellules sur 7', 'PP (delta >0) : ln q > 0 a 5 cellules sur 7', 'PG (delta >0) : ln q > 0 a 5 cellules sur 7',
      'ensemble : ln q > 0 a 22 cellules sur 28, ln q < 0 a 6 ; mediane de ln q : +0.00032', 'ln q du signe de delta a 12 cellules, du signe oppose a 16', 'ordre 3 plus pres de la mesure que l ordre 1 : 26 cellules ; que la loi d echelle : 27',
      'plus grand |ln q| de la forme fermee (consigne, non jugee) : 0.1136', 'A-6 plus grand |ln q| aux lisibles lues : 0.0007 -> OUI', 'V1 : TENU', 'VP : TENU')
exige(Z + 'authentifie_rectificatif_m1_machine2_v1.log', 'CANON du manifeste (calcule, non annonce) : 71ec801a5f86e068', 'MORSURES : 0', 'console rejouee == log de m1 : True', 'json rejoue canon d66a7349bae0e43b ; json de m1 canon d66a7349bae0e43b ; identiques : True',
      'canon 336913aecc732cdf', 'pieces du zip : 8 ; en trop : [] ; manquantes : []')
exige('certif_gel_vide_partie2_machine2/part_manquee_joues_machine2_v1.log', 'f > 0 : 184 sur 185 ; f < 0 : 1 ; f > 1 : 2', 'meme signe) : 182 sur 185')
# table de la note : ecrite depuis le verdict de la feuille de m1
V = json.load(open(os.path.join(ICI, R + 'run_1/verdict_vide.json'), encoding='utf-8'))
ordre = lambda c: (['MG', 'MP', 'PP', 'PG'].index(c['id'][:2]), int(c['id'][2:]))
cel = sorted(V['cellules'], key=ordre)
if len(cel) != 28:
    arrets.append('verdict_vide.json ne porte pas 28 cellules')
tab = ['    cellule  w2         m   ln Gamma_pl  etal.s  etendue  bande b  ln q       T     jugement']
for c in cel:
    tab.append('    %-7s  %-9s  %-2d  %11.4f  %.4f  %.4f   %.4f   %+.5f  %.2f  %s' % (c['id'], c['w2'], c['m'], c['ln_Gamma_pl'], c['etalement_du_lecteur'], c['etendue'], c['bande'], c['ln_q'], c['tolerance'], c['jugement']))
TABLE = '\n'.join(tab)
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@TABLE@@', TABLE).replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note) and not arrets:
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('8472dba8919a9b6e', 'cc54f4bc4e175143', 'a6754241629160a7', '71ec801a5f86e068', '336913aecc732cdf', 'a38b1550f8f5e3cf', 'ac39a24def6c7420', 'b71206e5daf6c741', '2597 s', '19:13:54', '19:57:11', '4.26e-09',
          '0.0007', '0.0013', '0.0101', '0.0398', '3.89e-36', '1.32e-27', '22 cellules sur 28', '+0.00032', '0.1136', 'dee73bd', 'V1 TENU ; VP TENU', '28 cellules sur 28', '28 sur 28'):
    if x not in re.sub(r'\s+', ' ', note):
        arrets.append('la note ne porte pas %r' % x)
if '@@' in note:
    arrets.append('la note porte encore un @@')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- RESULTAT du run unique du gel "largeur du vide" (seconde partie eebd979f18d8db48, lot b1919dc9468dc437), joue par machine 2 sur BOCAL4 le 16/11/2026 de 19:13:54 a 19:57:11 : les fichiers de l\'etage A, les 28 fichiers de cellule, '
    'le verdict de la feuille de machine 1 (V1 TENU ; VP TENU, canon 8472dba8919a9b6e), les journaux, le journal du pilote, mon lanceur, ma feuille rejouee, mon analyse, l\'authentification du rectificatif C-1 C-2. Aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le gel partie 2 eebd979f18d8db48 (lot b1919dc9468dc437) ; le rectificatif de machine 1 (lot 71ec801a5f86e068) ; mon lot de certification f989369a3ac22f98 ; le registre en tete dee73bd (clone frais, lu, non ecrit)\n")
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
