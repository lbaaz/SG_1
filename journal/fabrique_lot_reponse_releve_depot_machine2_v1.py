# -*- coding: ascii -*-
"""FABRIQUE DU LOT DE REPONSE machine 2 au releve de machine 1 apres les depots 99 et 100 -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_contreseing_acte_gel_loi_v2_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_reponse_releve_depot_machine2_v1.py
Gardes AVANT ecriture : le releve independant est LU (aucun ecart a machine 1 sur les sept lots) ; les deux journaux du controle des lots extraits sont LUS (1 lot a manque au 99, 2 au 100) ; l'authentification du lot de m1 est
LUE (0 morsure, 860c0ca980977935) ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_reponse_releve_depot_99_100_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_reponse_releve_depot_99_100_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_reponse_releve_depot_99_100_machine2_v1.md'
SELF = 'fabrique_lot_reponse_releve_depot_machine2_v1.py'
D = 'certif_depot_99_100_machine2/'
PIECES = [D + 'authentifie_lot_releve_m1_machine2_v1.py', D + 'authentifie_lot_releve_m1_machine2_v1.log',
          D + 'releve_apres_depot_machine2_v1.py', D + 'releve_apres_depot_machine2_v1.log', D + 'releve_apres_depot_machine2_v1.json',
          D + 'controle_lots_entrants_machine2_v1.py', D + 'controle_lots_entrants_delta99_avant_complement_machine2_v1.log', D + 'controle_lots_entrants_delta100_avant_complement_machine2_v1.log', SELF]
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


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
if 'ECARTS A CE QUE DIT MACHINE 1 (sur les sept lots) : aucun' not in lit(D + 'releve_apres_depot_machine2_v1.log'):
    arrets.append('le releve independant n\'est pas sans ecart a machine 1')
if 'LOTS A MANQUE : 1 ' not in lit(D + 'controle_lots_entrants_delta99_avant_complement_machine2_v1.log'):
    arrets.append('le controle des lots extraits ne rend pas 1 lot a manque au delta 99')
if 'LOTS A MANQUE : 2 ' not in lit(D + 'controle_lots_entrants_delta100_avant_complement_machine2_v1.log'):
    arrets.append('le controle des lots extraits ne rend pas 2 lots a manque au delta 100')
a_ = lit(D + 'authentifie_lot_releve_m1_machine2_v1.log')
if 'MORSURES : 0' not in a_ or 'CANON du manifeste : 860c0ca980977935' not in a_:
    arrets.append('l\'authentification du lot de m1 n\'est pas a zero morsure au canon 860c0ca980977935')
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
for x in ('860c0ca980977935', '26b3912297b31713', 'd9250297bf7d2f77', '0a5741ff95e7136c', 'aucun appel'):
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
    'MANIFESTE %s -- REPONSE de machine 2 au releve de machine 1 apres les depots 99 et 100 (lot 860c0ca980977935) : mon releve independant (memes comptes sur les sept lots absents), le controle des lots extraits qui m\'a manque '
    'et ses deux journaux d\'avant le complement, l\'authentification du lot de machine 1. Aucun nombre d\'acte touche. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : le releve de machine 1 860c0ca980977935 ; les depots 99 (91dd503) et 100 (54da87a) ; le registre au clone neuf 54da87a\n")
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
