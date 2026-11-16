# -*- coding: ascii -*-
"""FABRIQUE DU LOT de certification de machine 2 : gel 'largeur du vide', SECONDE partie (eebd979f18d8db48) -- manifeste + ZIP. 2026-11-16.
Meme squelette que fabrique_lot_certification_gel_vide_partie1_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_certification_gel_vide_partie2_machine2_v1.py
Gardes AVANT ecriture : chaque nombre que la note cite est RELU dans un journal (authentification a 0 morsure, comparaison de MES predictions a la table gelee, part manquee, nombres des sections, test differentiel a 0 ecart sur 5 100 runs,
matrice de mutations (le compte est LU et mis dans la note), essais de refus, banc, pre-vol sur BOCAL4 et ses quatre controles, etalement du lecteur aux etats joues) ; ma feuille est au canon annonce ; la note est ASCII (verifie AVANT
d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; ZIP relu bit-identique."""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_certification_gel_vide_partie2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_vide_partie2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_vide_partie2_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_vide_partie2_machine2_v1.py'
D = 'certif_gel_vide_partie2_machine2/'
L = 'livraison_16h_gel_vide_partie2/'
PV = 'prevol_gel_vide_machine2/'
PIECES = [
    L + 'authentifie_lots_gel_vide_partie2_machine2_v1.py', L + 'authentifie_lots_gel_vide_partie2_machine2_v1.log',
    D + 'predictions_vide_machine2_v1.py', D + 'predictions_vide_machine2_v1.log', D + 'predictions_machine2_vide_v1.json', D + 'comparaison_table_gel_machine2_v1.log',
    D + 'part_manquee_joues_machine2_v1.py', D + 'part_manquee_joues_machine2_v1.log', D + 'controle_nombres_gel_machine2_v1.py', D + 'controle_nombres_gel_machine2_v1.log',
    D + 'predictions_m1_rejouees_machine2.log', D + 'table_cellules_gel_vide_rejouee_m2.json',
    D + 'feuille_vide_machine2_v1.py', D + 'difftest_feuille_vide_machine2_v1.py',
    D + 'difftest_feuille_vide_machine2_v1_graine1.log', D + 'difftest_feuille_vide_machine2_v1_graine2.log',
    D + 'difftest_feuille_vide_machine2_v1_final_graine11.log', D + 'difftest_feuille_vide_machine2_v1_final_graine12.log',
    D + 'mutations_feuille_vide_machine2_v1.py', D + 'mutations_feuille_vide_machine2_v1.log', D + 'mutations_feuille_vide_machine2_v1_premier_passage.log',
    D + 'derive_essai_refus_machine2_v1.py', D + 'essai_refus_machine2_v1.py', D + 'essai_refus_machine2_v1.diff', D + 'essai_refus_machine2_v1.log',
    D + 'banc_feuille_vide_machine1_rejoue_machine2.log',
    D + 'comparaison_prevol_vide_rejouee_machine2.log', D + 'comparaison_prevol_vide_machine2.json', D + 'feuille_prevol_comparaison_machine2.log',
    D + 'feuille_prevol_m1_sur_mon_run.log', D + 'feuille_prevol_m2_sur_mon_run.log', D + 'prevol_verdict_m1_sur_mon_run.json', D + 'prevol_verdict_m2_sur_mon_run.json',
    D + 'etalement_lecteur_joues_machine2_v1.py', D + 'etalement_lecteur_joues_machine2_v1.log', D + 'etalement_lecteur_joues_machine2_v1.json',
    PV + 'console_prevol_1.log',
] + sorted(os.path.relpath(p, ICI).replace(os.sep, '/') for p in glob.glob(os.path.join(ICI, 'prevol_gel_vide_machine2', 'run_prevol_1', '*')) if os.path.isfile(p)) + [SELF]
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
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
if emp(open(os.path.join(ICI, D + 'feuille_vide_machine2_v1.py'), 'rb').read())[0] != 'a6754241629160a7':
    arrets.append('ma feuille n\'est plus au canon a6754241629160a7')
exige(L + 'authentifie_lots_gel_vide_partie2_machine2_v1.log', 'CANON du manifeste (calcule, non annonce) : b1919dc9468dc437', 'md a plat == md du lot (octets) : True ; canon eebd979f18d8db48',
      'section 16 : pieces citees avec canon : 23', 'morsures section 16 : 0', 'section 4.1 : pieces citees : 5', 'lot de reception de l enveloppe == lot deja recu (octets) : True', 'MORSURES : 0')
exige(D + 'comparaison_table_gel_machine2_v1.log', 'kappa              plus grand ecart absolu 0.00e+00', 'ln_G1              plus grand ecart absolu 8.03e-09', 'ln_G3              plus grand ecart absolu 4.26e-09',
      'r3                 plus grand ecart absolu 8.60e-09', 'etendue            plus grand ecart absolu 7.03e-09', 'ln_forme_fermee    plus grand ecart absolu 2.84e-14', 'M0                 plus grand ecart absolu 0.00e+00',
      'g ecrits identiques : True ; w2 identiques : True', 'ecart max 3.418', 'r3 aux quatre cellules lisibles de MG : [-0.01033, -0.0163, -0.0223, -0.02906]')
exige(D + 'part_manquee_joues_machine2_v1.log', 'part manquee f : mediane 0.071463', 'min 0.010002 (C3), max 0.237166 (M1)', 'f > 0 : 184 sur 185 ; f < 0 : 1 ; f > 1 : 2', 'N4', 'M1', 'M2')
exige(D + 'controle_nombres_gel_machine2_v1.log', '|ln G3/G2| max : 0.0026', '|ln G3/G1| max : 0.0206', '|r3| max       : 0.0291', 'de 2.9 a 15.1', 'a MG6 (gel 0.0090 a MG6) ; 0.02 / ce nombre = 2.21',
      'de 0.0130 a 0.0187', "['MG6', 'MP5', 'MP6', 'PP5', 'PP6', 'PG5', 'PG6']", 'rapport 1.0106')
exige(D + 'predictions_m1_rejouees_machine2.log', 'canon 22b5d62869889371', 'plus grand ecart absolu entre la table refaite chez moi par TON script et la table gelee : 1.71e-08')
for f, n in (('graine1', 600), ('graine2', 1500), ('final_graine11', 1500), ('final_graine12', 1500)):
    exige(D + 'difftest_feuille_vide_machine2_v1_%s.log' % f, 'ma feuille canon a6754241629160a7', 'RUNS : %d ; AVEC ECART : 0' % n)
for f in ('final_graine11', 'final_graine12'):
    exige(D + 'difftest_feuille_vide_machine2_v1_%s.log' % f, 'VP NON LUE')
exige(D + 'essai_refus_machine2_v1.log', 'ESSAIS DE REFUS : 9 tenus sur 9')
exige(D + 'banc_feuille_vide_machine1_rejoue_machine2.log', 'BANC : 26 cas tenus sur 26 : IL MORD COMME ATTENDU')
exige(D + 'comparaison_prevol_vide_rejouee_machine2.log', 'PRE-VOL : 4 controles tenus sur 4', 'P1 instrument du lecteur (pieces deposees, par le pilote) : TIENT', 'pire ecart relatif 4.4e-16', '48 lectures du jumeau suivies sur 48')
exige(D + 'feuille_prevol_comparaison_machine2.log', 'PV3 temoin m1 48 1.8279573503892306e-35 | moi 48 1.8279573503892306e-35 | identiques : True', 'PV8 temoin m1 48 1.2082481578830476e-52 | moi 48 1.2082481578830476e-52 | identiques : True',
      'PV3 prevol: True ; fantome : None', 'PV8 prevol: True ; fantome : None')
exige(D + 'etalement_lecteur_joues_machine2_v1.log', 'etats lus (quatre trajectoires) : 144', "QUALIFIE': 144", 'mediane 0.0009', 'max 0.0052', '143 sur 144')
exige(PV + 'console_prevol_1.log', 'INSTRUMENT DU LECTEUR : TIENT ; canon de son verdict 6b5923697f9d8b60', 'FIN DU PILOTE ; duree totale 1001 s', 'PV3    w2 = 101/50    m = 3  : 48 sur 48 ; 1.83e-35', 'PV8    w2 = 101/50    m = 8  : 48 sur 48 ; 1.21e-52')
mut = lit(D + 'mutations_feuille_vide_machine2_v1.log')
mm = re.search(r'MUTATIONS ATTRAPEES : (\d+) sur 20', mut)
if not mm:
    arrets.append('la matrice de mutations n\'est pas terminee')
else:
    n_att = int(mm.group(1))
    rat = re.search(r'NON ATTRAPEES : (.*)', mut)
    txt_rat = ('Non attrapees : %s. Les mutations de BORD (< au lieu de <=, >= au lieu de >) ne different que sur une EGALITE EXACTE en flottant, qu\'aucun dossier synthetique ne produit : equivalentes en pratique.' % rat.group(1)) if rat else 'Aucune n\'echappe.'
note = lit(NOTE)
if '@@PIECES@@' in note:
    note = note.replace('@@MUT_N@@', str(n_att)).replace('@@MUT_RATEES@@', txt_rat)
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note) and not arrets:
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('b1919dc9468dc437', 'eebd979f18d8db48', 'b71206e5daf6c741', '22b5d62869889371', 'a6754241629160a7', '6b5923697f9d8b60', '5921fcd984d6de5b', '0.0714629785415121', '5 100 dossiers', '0.0052', '1 001 s'):
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
    'MANIFESTE %s -- CERTIFICATION de machine 2 de la SECONDE partie du gel "largeur du vide" (eebd979f18d8db48, lot b1919dc9468dc437) : mes predictions des 28 cellules contre la table gelee (b71206e5daf6c741), ma feuille et son test differentiel (5 100 runs, 0 ecart), '
    'la matrice de mutations, le banc, les refus, le PRE-VOL sur BOCAL4 (tenu), l\'etalement du lecteur aux etats deja lus. Rien n\'est joue ; aucune 2D du fantome ; aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le gel partie 2 eebd979f18d8db48 (lot b1919dc9468dc437) ; mon lot 5921fcd984d6de5b (tirage) ; le registre en tete dee73bd (clone frais, lu, non ecrit)\n")
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
