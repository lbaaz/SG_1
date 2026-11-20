# -*- coding: ascii -*-
"""FABRIQUE DU LOT 'CONTROLE DU PONT' de machine 2 pour machine 1 -- manifeste + ZIP. 2026-11-16. Meme squelette que fabrique_lot_reponse_releve_depot_machine2_v1.py (non edite).
Hors chaine, classe 3, 1D seule : aucune 2D, aucun gel, aucun run, aucun depot.
Usage : py -3.11 -I fabrique_lot_pont_controle_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; chaque nombre cite par la note est RELU dans le journal qui le porte (et doit etre dans la note) ; la note est ASCII (verifie AVANT d'ouvrir
un fichier en ecriture), nomme le canon de CHAQUE piece ; aucune fuite de vie privee (identifiant du poste, prenom, nom, messagerie, chemins personnels) dans les pieces ni dans la note ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'certif_pont_machine2/'
NOM = 'lot_machine2_2026-11-16_pont_controle_ordres_1_et_3_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_pont_controle_ordres_1_et_3_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_pont_controle_machine2_v1.md'
SELF = 'fabrique_lot_pont_controle_machine2_v1.py'
PIECES = [D + n for n in (
    'controle_pont_machine2_v1.py', 'controle_pont_machine2_v1.log',
    'spectre_pont_machine2_v1.py', 'spectre_pont_MG3_N33_machine2_v1.log',
    'ecarts_vs_T_pont_machine2_v1.py', 'ecarts_vs_T_pont_MG3_N33_machine2_v1.log',
    'residu_vs_spectre_pont_machine2_v1.py', 'residu_vs_spectre_pont_machine2_v1.log',
    'releve_json_pont_machine2_v1.py', 'releve_json_pont_machine2_v1.log',
    'ordre3_pont_machine2_v1.py', 'ordre3_pont_machine2_v1.log',
    'stat_ordre3_machine2_v1.py', 'stat_ordre3_machine2_v1.log')] + [SELF]
# (journal, chaine qui doit y figurer ET figurer dans la note) : les nombres de la note, relus dans leur source
NOMBRES = [
    ('releve_json_pont_machine2_v1.log', 'croisements : 136 | paires (cellule, N) distinctes : 104 | configurations (profondeur, N) distinctes : 26'),
    ('releve_json_pont_machine2_v1.log', 'min -0.0171 max -0.0057  -> tous negatifs : True'),
    ('releve_json_pont_machine2_v1.log', 'ecart maximal du residu entre cellules : 4.40e-05 (sur 26 configurations)'),
    ('releve_json_pont_machine2_v1.log', 'G/(V^2 T) = 1.0172355247798288'),
    ('releve_json_pont_machine2_v1.log', 'paires (cellule, N) enregistrees plus d\'une fois : 32 | ecart maximal entre doublons : 0.0'),
    ('controle_pont_machine2_v1.log', 'croisements 104 paires (cellule,N) distinctes 104'),
    ('controle_pont_machine2_v1.log', 'spline_ln  ln(V^2T/G) : min -0.0187  max -0.0079  moyenne -0.0119'),
    ('controle_pont_machine2_v1.log', 'pchip_lin  ln(V^2T/G) : min -0.0195  max -0.0082  moyenne -0.0123'),
    ('controle_pont_machine2_v1.log', 'lin_ln     ln(V^2T/G) : min -0.0311  max -0.0160  moyenne -0.0223'),
    ('controle_pont_machine2_v1.log', 'spline_m   ln(V^2T/G) : min -0.0174  max -0.0078  moyenne -0.0116'),
    ('controle_pont_machine2_v1.log', 'MG3   3  25   1  4.9208e-06  2.910       -0.0187  -0.0195  -0.0306  -0.0174'),
    ('spectre_pont_MG3_N33_machine2_v1.log', ' 19     -0.9524   0.0007   0.9965   0.0028'),
    ('spectre_pont_MG3_N33_machine2_v1.log', ' 22     +4.0219'),
    ('spectre_pont_MG3_N33_machine2_v1.log', ' 23    +10.5715'),
    ('spectre_pont_MG3_N33_machine2_v1.log', ' 24    +19.9756'),
    ('ecarts_vs_T_pont_MG3_N33_machine2_v1.log', '-37.368     10.092               -32.322      10.237           0.986'),
    ('ecarts_vs_T_pont_MG3_N33_machine2_v1.log', '-27.276      7.840               -23.356       7.946           0.987'),
    ('ecarts_vs_T_pont_MG3_N33_machine2_v1.log', '+10.423      9.346               +15.096       9.533           0.980'),
    ('ecarts_vs_T_pont_MG3_N33_machine2_v1.log', '+19.770     12.650               +26.095      12.894           0.981'),
    ('residu_vs_spectre_pont_machine2_v1.log', 'MG3   3  31  4.8871e-06   -0.0172              0.9793  (0.9767..0.9823)  3   +0.0209           +0.0037'),
    ('residu_vs_spectre_pont_machine2_v1.log', 'MG6   6  34  1.5055e-08   -0.0084              0.9815  (0.9769..0.9862)  4   +0.0187           +0.0103'),
    ('stat_ordre3_machine2_v1.log', 'V identique a celui de m1 (chaine) : 86 sur 86'),
    ('stat_ordre3_machine2_v1.log', 'ordre 1 monotones     n=40  residu brut : min -0.0193 max -0.0081 moy -0.0129'),
    ('stat_ordre3_machine2_v1.log', 'ordre 3 monotones     n=45  residu brut : min -0.0201 max -0.0059 moy -0.0124'),
    ('stat_ordre3_machine2_v1.log', 'residu corrige : min -0.0022 max +0.0199 moy +0.0068'),
    ('stat_ordre3_machine2_v1.log', 'residu corrige : min -0.0063 max +0.0271 moy +0.0081'),
    ('stat_ordre3_machine2_v1.log', 'n=37  min -0.0058 max +0.0025 moy +0.0000 ; |ecart| > 0.01 : 0'),
    ('ordre3_pont_machine2_v1.log', '3     MG3   3  37  3.3700e-06   3.3700e-06'),
    ('ordre3_pont_machine2_v1.log', 'NON MONOTONE des x=34.9'),
    ('ordre3_pont_machine2_v1.log', 'NON MONOTONE des x=35.6'),
]
ENTRE = []   # (journal, regex a capturer, valeur attendue) : rempli apres lecture des journaux
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


TERMES = [''.join(p) for p in (('ba', 'zil'), ('le', 'beau'), ('gm', 'ail'), ('hot', 'mail'), ('Us', 'ers\\'), ('Us', 'ers/'), ('App', 'Data'), ('.cla', 'ude\\'), ('.cla', 'ude/'), ('Down', 'loads'))]


def fuites(nom, octets):
    t = octets.decode('latin-1').lower()
    out = [(nom, w) for w in TERMES if w.lower() in t]
    out += [(nom, m) for m in re.findall(r'[a-z]:[\\/]', t)]
    out += [(nom, m) for m in re.findall(r'[\w.+-]+@[\w-]+\.[\w.]+', t)]
    return out


for p in PIECES + [NOTE]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)
note = lit(NOTE)
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
nn = norm(note)
for j, s in NOMBRES:
    if norm(s) not in norm(lit(D + j)):
        arrets.append('le journal %s ne porte pas %r' % (j, s))
    if norm(s) not in nn:
        arrets.append('la note ne porte pas %r' % s)
for j, rx, attendu in ENTRE:
    m = re.search(rx, lit(D + j))
    if not m or m.group(1) != attendu:
        arrets.append('journal %s : %r attendu %r, lu %r' % (j, rx, attendu, m.group(1) if m else None))
    if attendu not in nn:
        arrets.append('la note ne porte pas %r' % attendu)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    if all(ord(c) < 128 for c in note):
        open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append("la note n'est pas ASCII (rien n'a ete ecrit)")
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for p in PIECES + [NOTE]:
    for f in fuites(p, open(os.path.join(ICI, p), 'rb').read()):
        arrets.append('FUITE de vie privee : %s' % (f,))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CONTROLE par machine 2 de la note du pont de machine 1 (pont_exploration_machine1_2026-11-16.zip, hors lot, empreinte du zip 7916f417f87d6175) : '
    'refait par mon code (V, temps classique, spectre), ordre 1 et ordre 3, 16 cellules lisibles, releve mecanique de ses JSON. HORS CHAINE, classe 3, 1D seule : aucune 2D, aucun gel, aucun run, aucun depot. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append("\nentrants : la livraison de machine 1 du 16/11 21:56 (8 pieces a plat, sans manifeste) ; le registre public en tete 2988237 (clone frais, lu, non ecrit)\n")
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
