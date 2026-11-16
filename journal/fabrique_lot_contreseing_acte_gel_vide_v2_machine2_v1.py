# -*- coding: ascii -*-
"""FABRIQUE DU LOT de CONTRESEING de machine 2 : acte du gel 'largeur du vide', VERSION 2 de machine 1 (16ba5e594ab18717) -- manifeste + ZIP. 2026-11-16.
Meme squelette que fabrique_lot_contreseing_acte_gel_vide_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_contreseing_acte_gel_vide_v2_machine2_v1.py
Gardes AVANT ecriture : aucune piece vide ; chaque nombre que la note cite est RELU dans un journal (authentification et son premier passage, releve v2 et son premier passage, contre-epreuve v2, verification du point (c)) ;
le diff des deux actes compte 13 blocs ; la note est ASCII (verifie AVANT d'ouvrir un fichier en ecriture) et nomme le canon de CHAQUE piece ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_contreseing_acte_gel_vide_v2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_contreseing_acte_gel_vide_v2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_contreseing_acte_gel_vide_v2_machine2_v1.md'
SELF = 'fabrique_lot_contreseing_acte_gel_vide_v2_machine2_v1.py'
L = 'livraison_16k_acte_gel_vide_v2/'
PIECES = [L + 'authentifie_acte_v2_m1_machine2_v1.py', L + 'authentifie_acte_v2_m1_machine2_v1.log', L + 'authentifie_acte_v2_m1_machine2_v1_premier_passage.log',
          L + 'releve_contreseing_acte_vide_machine2_v2.py', L + 'releve_contreseing_acte_vide_machine2_v2.log', L + 'releve_contreseing_acte_vide_machine2_v2.json', L + 'releve_contreseing_acte_vide_machine2_v2_premier_passage.log', L + 'diff_releve_v1_v2_machine2.txt',
          L + 'contre_epreuve_releve_acte_vide_machine2_v2.py', L + 'contre_epreuve_releve_acte_vide_machine2_v2.log', L + 'diff_acte_v1_v2_machine2.txt',
          L + 'verifie_part_manquee_c_machine2_v1.py', L + 'verifie_part_manquee_c_machine2_v1.log', SELF]
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
exige(L + 'authentifie_acte_v2_m1_machine2_v1.log', 'CANON du manifeste (calcule, non annonce) : fb6db25d1f5ae190', 'lignes de pieces : 6 (attendues 6)', 'pieces du zip : 7 ; en trop : [] ; manquantes : []', 'octets identiques : True',
      'section 4 de la note d accompagnement : pieces citees avec canon : 4', 'canon 464ba00a6905e3a5 : mon fichier journal_delta_nn_largeur_vide_v1.md -> OK', 'canon e1dfb7ba7b18196e : mon fichier MANIFEST_lot_machine2_contreseing_acte_gel_vide_v1.txt -> OK',
      'canon 700a39a9a7223fd0 : mon fichier POUR_MACHINE1_contreseing_acte_gel_vide_machine2_v1.md -> OK', 'MORSURES : 0')
exige(L + 'authentifie_acte_v2_m1_machine2_v1_premier_passage.log', 'attendus 5', 'MORSURES : 1')
exige(L + 'releve_contreseing_acte_vide_machine2_v2.log', '35 CONTROLES : 35 TIENNENT, 0 MORDENT', 'R35 TIENT', '13 blocs')
exige(L + 'releve_contreseing_acte_vide_machine2_v2_premier_passage.log', '35 CONTROLES : 33 TIENNENT, 2 MORDENT', 'R34 MORD', 'R35 MORD')
exige(L + 'contre_epreuve_releve_acte_vide_machine2_v2.log', 'copie intacte : 0 morsure(s) [] -> TENU', 'CONTRE-EPREUVE : 61 corruptions sur 61 mordues sur le controle vise', 'ECHECS : []')
exige(L + 'verifie_part_manquee_c_machine2_v1.log', '"part": (-x["ln_q"] / x["r3"]) / (1.0 - x["ln_q"] / x["r3"])', 'note v2 de m1 (section 2) : 0.0229, 0.0250, 0.0239, 0.0230', 'la formule de m1 (f = rho / (1 + rho)) redonne ses 0.0229 0.0250 0.0239 0.0230, soit 0.023 0.025 0.024 0.023 a trois decimales : True',
      'rho tronque 0.023', 'rho tronque 0.025', 'rho tronque 0.024')
nb = len([l for l in lit(L + 'diff_acte_v1_v2_machine2.txt').split('\n') if re.match(r'^\d+(,\d+)?[acd]\d+(,\d+)?$', l)])
if nb != 13:
    arrets.append('le diff des deux actes compte %d blocs, attendus 13' % nb)
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note) and not arrets:
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for x in ('fb6db25d1f5ae190', '16ba5e594ab18717', '464ba00a6905e3a5', 'e1dfb7ba7b18196e', '700a39a9a7223fd0', '35 TIENNENT', '61 sur 61', '13 blocs', '1517 + 59 = 1576', '0.0229, 0.0250, 0.0239, 0.0230', '49a40d9098b55361', 'Tu peux deposer'):
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
    'MANIFESTE %s -- CONTRESEING de machine 2 de la VERSION 2 de l\'acte du gel "largeur du vide" (16ba5e594ab18717, lot fb6db25d1f5ae190) : authentification, releve v2 de 35 controles (35 tiennent), sa contre-epreuve (61 corruptions sur 61 mordues), '
    'mes premiers passages conserves, la correction de mon erreur sur le point (c). Je contresigne sans condition. Aucune 2D. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : l'acte de machine 1, version 2 (lot fb6db25d1f5ae190) ; mon contreseing de la version 1 (lot e1dfb7ba7b18196e) ; le registre en tete dee73bd (clone frais, lu, non ecrit)\n")
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
