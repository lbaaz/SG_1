# -*- coding: ascii -*-
"""FABRIQUE DU LOT DE RESULTAT machine 2 'run du gel loi de la largeur, ordre 3, seconde partie' -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_certification_gel_loi_partie2_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_resultat_gel_loi_partie2_machine2_v1.py
Ne lance rien et ne mesure rien. Gardes AVANT ecriture : le journal du pilote est LU (FIN DU PILOTE, aucun ARRET, tous les appels au code 0, l'instrument du lecteur TIENT, les canons du pilote = ceux de la certification) ;
tous les fichiers du dossier du run sont dans le lot (aucun oublie) ; les canons de la sortie dense, du verdict du lecteur et du verdict d'ordre 3 ECRITS dans le journal du pilote sont recalcules sur les fichiers ;
la note est ASCII et nomme le canon de CHAQUE piece ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-16_resultat_gel_loi_partie2_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_gel_loi_partie2_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_gel_loi_partie2_machine2_v1.md'
SELF = 'fabrique_lot_resultat_gel_loi_partie2_machine2_v1.py'
RUN = 'run_gel_loi_ordre3/'
D = 'certif_gel_loi_partie2_machine2/'
AUTRES = [D + 'lanceur_run_gel_loi_machine2_v1.log', D + 'run_console.log', D + 'pilote_gel_loi_machine2_v2.py', D + 'pilote_gel_loi_machine2_v2.diff',
          # EXTRA hors verdict (apres la fin du run) : ma feuille independante sur les vrais fichiers, sa confrontation etat par etat au verdict du run, les marges aux seuils
          D + 'feuille_independante_gel_loi_machine2_v1.py', 'controle_ordre3_machine2/ordre3_machine2_v1.py', D + 'compare_retro_machine2_v1.py',
          D + 'concordance_run_machine2_v1.json', D + 'concordance_run_machine2_v1.log', D + 'concordance_run_comparaison_machine2_v1.log',
          D + 'marges_run_machine2_v1.py', D + 'marges_run_machine2_v1.log', D + 'marges_run_machine2_v1_calcul_en_ligne.log']
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


fichiers_run = sorted(os.path.relpath(f, ICI).replace('\\', '/') for f in glob.glob(os.path.join(ICI, RUN, '*')) if os.path.isfile(f))
if not fichiers_run:
    print('ARRET : le dossier du run est vide ou absent')
    raise SystemExit(1)
PIECES = fichiers_run + AUTRES + [SELF]
for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
# --- le journal du pilote, lu ---
j = lit(RUN + 'pilote_gel_loi.log')
for x in ('pilote pilote_gel_loi_machine2_v2.py canon 15998497f3422765', 'canon table             35fa7b73f2b7f8eb ', 'INSTRUMENT DU LECTEUR : TIENT', 'FIN DU PILOTE ; duree totale'):
    if x not in j:
        arrets.append('journal du pilote : %r absent' % x)
if 'ARRET DU PILOTE' in j or 'PRE-VOL' in j or 'NE TIENT PAS' in j:
    arrets.append('journal du pilote : un arret, un pre-vol ou un instrument qui ne tient pas')
codes = re.findall(r'code=(\d+)', j)
if not codes or any(c != '0' for c in codes):
    arrets.append('journal du pilote : un code de sortie non nul ou aucun code : %s' % codes)
for nom, fichier, motif in (('sortie dense', RUN + 'sonde_dense.json', r'CANON DE LA SORTIE DENSE : ([0-9a-f]{16})'), ('verdict du lecteur', RUN + 'verdict_ter.json', r'CANON DU VERDICT DU LECTEUR : ([0-9a-f]{16})'),
                            ('verdict d ordre 3', RUN + 'verdict_ordre3.json', r"CANON DU VERDICT D'ORDRE 3 : ([0-9a-f]{16})")):
    m = re.search(motif, j)
    c = emp(open(os.path.join(ICI, fichier), 'rb').read())[0]
    if not m or m.group(1) != c:
        arrets.append('canon de %s : journal %s, fichier %s' % (nom, m.group(1) if m else None, c))
note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
for x in ('5a5ba910be8b3b29', '15998497f3422765', '35fa7b73f2b7f8eb', 'E19', 'aucun appel'):
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
    'MANIFESTE %s -- RESULTAT DU RUN UNIQUE de machine 2 pour le gel "loi de la largeur, ordre 3", seconde partie (543d8b33e5c9afb8) : sortie dense, fichiers du lecteur, verdicts, journaux, journal du pilote. '
    'Le verdict est celui de la feuille d ordre 3 jouee dans le run ; machine 1 la rejoue. Certification : lot 5a5ba910be8b3b29. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel 543d8b33e5c9afb8 ; lot de machine 1 76ed746ef4db3b0c ; ma certification 5a5ba910be8b3b29 ; le feu vert ecrit de l operateur (session du 16/11) ; table gelee 35fa7b73f2b7f8eb\n')
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
