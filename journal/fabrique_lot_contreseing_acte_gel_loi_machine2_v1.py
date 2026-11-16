# -*- coding: ascii -*-
"""FABRIQUE DU LOT DE CONTRESEING machine 2 'acte du run du gel loi de la largeur, ordre 3' -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_resultat_gel_loi_partie2_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_contreseing_acte_gel_loi_machine2_v1.py
Ne lance rien et ne mesure rien. Gardes AVANT ecriture : le releve est LU (68 controles, une seule morsure, R08c) ; la contre-epreuve est LUE (28 essais sur 28) ; l'authentification du lot de m1 est LUE (0 morsure, canon d9250297bf7d2f77) ;
le canon de l'acte lu est a3f7d5d6809dcfe5 ; ma seconde feuille du dossier de travail est octet pour octet celle de mon dossier de certification ; la note est ASCII et nomme le canon de CHAQUE piece ;
le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_contreseing_acte_gel_loi_ordre3_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_gel_loi_ordre3_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_gel_loi_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_gel_loi_machine2_v1.py'
D = 'certif_acte_gel_loi_machine2/'
R = D + 'releve_contreseing_acte_gel_loi_machine2_v1'
ACTE = 'livraison_16b_acte_gel_loi_ordre3/ext/lot_m1/journal_delta_nn_loi_largeur_ordre3_v1.md'
PIECES = [D + 'authentifie_lot_acte_machine2_v1.py', D + 'authentifie_lot_acte_machine2_v1.log',
          R + '.py', R + '.log', R + '.json', R + '_premier_passage.log', R + '_second_passage.log', R + '_second_jet.py', R + '_troisieme_passage.log',
          D + 'contre_epreuve_releve_acte_machine2_v1.py', D + 'contre_epreuve_releve_acte_machine2_v1.log', D + 'contre_epreuve_releve_acte_machine2_v1.json',
          D + 'etiquettes_predites_machine2_v1.py', D + 'etiquettes_predites_machine2_v1.log', D + 'etiquettes_predites_machine2_v1.json',
          D + 'feuille_independante_gel_loi_machine2_v1.py', D + 'ma_feuille_sur_verdict_lecteur_machine1_v1.json', D + 'ma_feuille_sur_verdict_lecteur_machine1_v1.log',
          D + 'plateau_bp_machine2_v1.py', D + 'plateau_bp_machine2_v1.log', SELF]
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


for p in PIECES + [NOTE, ACTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
if "RELEVE DU CONTRESEING : 68 controles, 1 mordent : ['R08c']" not in lit(R + '.log'):
    arrets.append("le releve n'a pas la forme attendue (68 controles, une seule morsure R08c)")
if 'CONTRE-EPREUVE : 28 essais, 28 comme attendu' not in lit(D + 'contre_epreuve_releve_acte_machine2_v1.log'):
    arrets.append("la contre-epreuve n'est pas 28 sur 28")
a_ = lit(D + 'authentifie_lot_acte_machine2_v1.log')
if 'MORSURES : 0' not in a_ or 'CANON du manifeste : d9250297bf7d2f77' not in a_:
    arrets.append("l'authentification du lot de m1 n'est pas a zero morsure au canon d9250297bf7d2f77")
if emp(open(os.path.join(ICI, ACTE), 'rb').read())[0] != 'a3f7d5d6809dcfe5':
    arrets.append("l'acte lu n'est pas a3f7d5d6809dcfe5")
if open(os.path.join(ICI, D + 'feuille_independante_gel_loi_machine2_v1.py'), 'rb').read() != open(os.path.join(ICI, 'certif_gel_loi_partie2_machine2/feuille_independante_gel_loi_machine2_v1.py'), 'rb').read():
    arrets.append("ma seconde feuille n'est pas celle de mon dossier de certification")
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note):
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('a3f7d5d6809dcfe5', 'd9250297bf7d2f77', '0.173', '0.174', 'aucun appel'):
    if x not in re.sub(r'\s+', ' ', note):
        arrets.append('la note ne porte pas %r' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTRESEING de machine 2 sur l\'acte du run du gel "loi de la largeur, ordre 3" (projet v1 a3f7d5d6809dcfe5, lot de machine 1 d9250297bf7d2f77) : releve a 68 controles, sa contre-epreuve, '
    'la seconde feuille rejouee sur le verdict du lecteur de machine 1, mes quatorze etiquettes predites (1D), la description du plateau a BP. Une morsure de description (E3, 0.173 pour 0.174). machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : acte a3f7d5d6809dcfe5 ; lot de machine 1 d9250297bf7d2f77 ; mes lots 5a5ba910be8b3b29 et 54ccae1713f92bc9 ; le run (verdict d'ordre 3 87e9221cfc5f8f9b)\n")
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
