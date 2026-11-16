# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'mon tirage sur la graine de l'operateur (200482)' -- manifeste + ZIP. 2026-11-15. Meme squelette que fabrique_lot_certification_gel_loi_partie1_machine2_v1.py (non edite).
Usage : py -3.11 -I fabrique_lot_tirage_graine_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; mes journaux LUS (douze cellules, tous au rang 0, vingt hachages ; le script de machine 1 rend les memes douze cellules) ; les canons des scripts et des tables cites
(tirage_complet_machine2_v1.py, tirage_gel_loi_machine2_v1.py, ma table, la table commune, la table de machine 1) recalcules et nommes dans la note ; le lot de machine 1 recalcule ; note ASCII ; les canons de
CHAQUE piece nommes dans la note ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NOM = 'lot_machine2_2026-11-15_tirage_graine_200482_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_tirage_graine_200482_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_tirage_graine_machine2_v1.md'
SELF = 'fabrique_lot_tirage_graine_machine2_v1.py'
D = 'controle_carte_machine2/'
LIV = 'livraison_15g_gel_loi_partie1/'
PIECES = [D + x for x in ('tirage_graine_200482_machine2_v1.log', 'tirage_graine_200482_sha256_machine2_v1.log', 'tirage_graine_200482_script_machine1_sur_ma_machine_v1.log')] + [SELF]
CITES = ((D + 'tirage_complet_machine2_v1.py', None), (D + 'tirage_gel_loi_machine2_v1.py', 'c3128f277ef97d26'), (D + 'eligibilite_machine2_v1.json', None), (D + 'table_commune_machine2_v1.json', None),
         (LIV + 'lot_m1/eligibilite_candidates_v1.json', 'f11ac4458a336650'), (LIV + 'lot_m1/tirage_machine1_v1.py', '0f608f8ade6ff378'))
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


for p in PIECES + [NOTE, LIV + 'MANIFEST_lot_machine1_gel_loi_partie1_regle_tirage_v1.txt'] + [c[0] for c in CITES]:
    if not os.path.isfile(os.path.join(ICI, p)):
        arrets.append('piece absente : %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = lit(NOTE)
if '@@PIECES@@' in note:
    ls = ['    cette note']
    for p in PIECES:
        ls.append('    %s  %s' % ('(ce script)' if p == SELF else emp(open(os.path.join(ICI, p), 'rb').read())[0], p))
    note = note.replace('@@PIECES@@', '\n'.join(ls))
    open(os.path.join(ICI, NOTE), 'w', encoding='ascii', newline='\n').write(note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')
nn = re.sub(r'\s+', ' ', note)
l1, l2, l3 = lit(D + 'tirage_graine_200482_machine2_v1.log'), lit(D + 'tirage_graine_200482_sha256_machine2_v1.log'), lit(D + 'tirage_graine_200482_script_machine1_sur_ma_machine_v1.log')
for nom, lg, xs in (
        ('mon tirage', l1, ('creneau N  rang 0 : w2 = 387/200 (1.935) : ELIGIBLE, retenu', 'creneau P  rang 0 : w2 = 407/200 (2.035) : ELIGIBLE, retenu', 'creneau BN rang 0 : w2 = 481/250 (1.924) : ELIGIBLE, retenu',
                            'creneau BP rang 0 : w2 = 2067/1000 (2.067) : ELIGIBLE, retenu', 'N1  w2 = 387/200 (1.935) facteur 3/4', 'N5  w2 = 387/200 (1.935) facteur 4/3',
                            'P1  w2 = 407/200 (2.035) facteur 3/4', 'P5  w2 = 407/200 (2.035) facteur 4/3', 'BN  w2 = 481/250 (1.924) facteur 1', 'BP  w2 = 2067/1000 (2.067) facteur 1')),
        ('hachages', l2, ('sha256("200482|N|0") = 2d61afb169b59923... ; modulo  9 =  4 -> w2 = 1.935', 'sha256("200482|P|0") = 35f444e55404a3de... ; modulo 18 =  4 -> w2 = 2.035',
                          'sha256("200482|BN|0") = ff076ee62cb2ee1d... ; modulo  8 =  7 -> w2 = 1.924', 'sha256("200482|BP|0") = 7de072e8e10b9d93... ; modulo  9 =  6 -> w2 = 2.067')),
        ('script de machine 1', l3, ('graine : 200482', 'creneau N  rang 0 : numero 4 sur 9 -> w2 = 387/200 (1.935)', 'creneau P  rang 0 : numero 4 sur 18 -> w2 = 407/200 (2.035)',
                                    'creneau BN rang 0 : numero 7 sur 8 -> w2 = 481/250 (1.924)', 'creneau BP rang 0 : numero 6 sur 9 -> w2 = 2067/1000 (2.067)', 'TIRAGE : douze cellules'))):
    for x in xs:
        if x not in lg:
            arrets.append('journal %s : %r absent' % (nom, x))
for x in ('200482', '1.935', '2.035', '1.924', '2.067', 'RANG 0', 'N 4 sur 9', 'P 4 sur 18', 'BN 7 sur 8', 'BP 6 sur 9', '2d61afb169b59923', '35f444e55404a3de', 'ff076ee62cb2ee1d', '7de072e8e10b9d93',
          '11/7/4', '14/6/8', 'tirage_machine1_v1.py', 'section 6', 'E19', 'PAS ton tirage', 'aucun zero de tete'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for p, att in CITES:
    c = emp(open(os.path.join(ICI, p), 'rb').read())[0]
    if att is not None and c != att:
        arrets.append('canon de %s : %s, attendu %s' % (p, c, att))
    if c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, p))
man1 = open(os.path.join(ICI, LIV + 'MANIFEST_lot_machine1_gel_loi_partie1_regle_tirage_v1.txt'), 'rb').read()
if emp(man1)[0] != '596a45bf6d4f97d7':
    arrets.append('le lot de machine 1 n a plus le canon 596a45bf6d4f97d7')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- TIRAGE DE MACHINE 2 SUR LA GRAINE DE L OPERATEUR (200482), par MON code, table commune (le ET de nos deux tables) : N 1.935, P 2.035, BN 1.924, BP 2.067, tous au rang 0 ; douze cellules ; '
    'le script de tirage de machine 1, lance sur ma machine, rend les memes douze cellules (ce n est pas son tirage). Rien n est gele, rien n est joue, aucune largeur 2D. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel b56ca5cb2dd25da1 ; lot de machine 1 596a45bf6d4f97d7 ; ma certification 4fb1dc66f96f57f6 ; la graine, donnee par l operateur a machine 2 : 200482\n')
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
