# -*- coding: ascii -*-
"""FABRIQUE DU LOT DE CONTRESEING machine 2 de la VERSION 2 de l'acte du run du gel loi de la largeur, ordre 3 -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_contreseing_acte_gel_loi_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_contreseing_acte_gel_loi_v2_machine2_v1.py
Gardes AVANT ecriture : le releve v2 est LU (73 controles, aucune morsure) ; la contre-epreuve v2 est LUE (33 essais sur 33) ; l'authentification du lot de m1 est LUE (0 morsure, 0a5741ff95e7136c) ; le canon de l'acte v2 lu est
b205b14cdfc23ba3 ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; l'en-tete du manifeste porte le canon de l'acte v2 ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_contreseing_acte_gel_loi_ordre3_v2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_gel_loi_ordre3_v2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_gel_loi_v2_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_gel_loi_v2_machine2_v1.py'
D = 'certif_acte_gel_loi_machine2/'
R = D + 'releve_contreseing_acte_gel_loi_machine2_v2'
ACTE = 'livraison_16c_acte_gel_loi_ordre3_v2/ext/lot_m1/journal_delta_nn_loi_largeur_ordre3_v2.md'
PIECES = [D + 'authentifie_lot_acte_v2_machine2_v1.py', D + 'authentifie_lot_acte_v2_machine2_v1.log',
          D + 'derive_releve_v2_machine2.py', D + 'diff_releve_v1_v2.txt', D + 'diff_contre_epreuve_v1_v2.txt',
          R + '.py', R + '.log', R + '.json', R + '_premier_passage.log',
          D + 'contre_epreuve_releve_acte_machine2_v2.py', D + 'contre_epreuve_releve_acte_machine2_v2.log', D + 'contre_epreuve_releve_acte_machine2_v2.json', SELF]
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
if 'RELEVE DU CONTRESEING : 73 controles, 0 mordent : []' not in lit(R + '.log'):
    arrets.append("le releve v2 n'a pas la forme attendue (73 controles, aucune morsure)")
if 'CONTRE-EPREUVE : 33 essais, 33 comme attendu' not in lit(D + 'contre_epreuve_releve_acte_machine2_v2.log'):
    arrets.append("la contre-epreuve v2 n'est pas 33 sur 33")
a_ = lit(D + 'authentifie_lot_acte_v2_machine2_v1.log')
if 'MORSURES : 0' not in a_ or 'CANON du manifeste : 0a5741ff95e7136c' not in a_:
    arrets.append("l'authentification du lot de m1 n'est pas a zero morsure au canon 0a5741ff95e7136c")
if emp(open(os.path.join(ICI, ACTE), 'rb').read())[0] != 'b205b14cdfc23ba3':
    arrets.append("l'acte lu n'est pas b205b14cdfc23ba3")
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
for x in ('b205b14cdfc23ba3', '0a5741ff95e7136c', 'a3f7d5d6809dcfe5', 'aucun appel'):
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
    'MANIFESTE %s -- CONTRESEING de machine 2 sur la VERSION 2 (b205b14cdfc23ba3) de l\'acte du run du gel "loi de la largeur, ordre 3" (lot de machine 1 0a5741ff95e7136c ; la v1 est a3f7d5d6809dcfe5) : releve a 73 controles, '
    'sa contre-epreuve (33 essais), l\'authentification du lot de machine 1, les scripts derives et leurs diffs. Aucune morsure. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : acte v2 b205b14cdfc23ba3 ; lot de machine 1 0a5741ff95e7136c ; mon contreseing de la v1 bbb74a8df7697397 ; le run (verdict d'ordre 3 87e9221cfc5f8f9b)\n")
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
