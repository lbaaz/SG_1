# -*- coding: ascii -*-
"""Authentifie le lot de m1 'rectificatif de texte a la seconde partie du gel du vide (C-1, C-2)' (livraison 16i) :
canon du manifeste (pas d'ENVOI : calcule), 7 pieces aux DEUX canons et aux deux tailles, zip = manifeste + pieces, ext/ identique au zip,
note du lot = note a plat de Downloads (canon 336913aecc732cdf annonce par le manifeste), pas de piece en trop.
Puis REJEU du script de m1 (verifie_C1_C2_machine1_v1.py) sur ses entrees, dont les canons sont recoupes aux manifestes deja authentifies
(table gelee b71206e5daf6c741, superposition aeb9fc40ecc43899, verifie_variantes e9a0a3812de6ad16) : sa sortie console et son json doivent etre ceux de son lot.
Derive de authentifie_lot_reception_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_rectificatif_m1_machine2_v1.py"""
import hashlib
import os
import re
import subprocess
import sys
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16i_rectificatif_gel_vide_partie2'
B = r'd:\devs\bocal\BOCAL4'
NOM = 'lot_machine1_2026-11-16_rectificatif_gel_vide_partie2_C1_C2_v1'
ZIP = os.path.join(R, NOM + '.zip')
MD_PLAT = os.path.join(R, 'rectificatif_gel_vide_partie2_C1_C2_machine1_v1.md')
NOM_MAN = 'MANIFESTE_' + NOM + '.txt'
ENTREES = {
    'table gelee': (os.path.join(B, r'livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1\table_cellules_gel_vide_v1.json'), 'b71206e5daf6c741'),
    'verifie_variantes_joues': (os.path.join(B, r'livraison_16g_reception_certification_vide\ext\lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1\verifie_variantes_joues_v1.json'), 'e9a0a3812de6ad16'),
    'superposition': (os.path.join(B, r'livraison_16e_vide_etape_sans_run\ext\lot_machine1_2026-11-16_vide_etape_sans_run_v1\superposition_v1.json'), 'aeb9fc40ecc43899'),
}


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


mauv = []
piece_zip = {}
with zipfile.ZipFile(ZIP) as z:
    noms = set(n for n in z.namelist() if not n.endswith('/'))
    print('contenu du zip :', sorted(noms))
    cand = [n for n in noms if n.endswith(NOM_MAN)]
    if len(cand) != 1:
        mauv.append('manifeste introuvable ou multiple : %s' % cand)
        raise SystemExit('MORSURES : %s' % mauv)
    NOM_MAN_Z = cand[0]
    PREF = NOM_MAN_Z[:len(NOM_MAN_Z) - len(NOM_MAN)]
    print('prefixe des pieces dans le zip : %r' % PREF)
    man = z.read(NOM_MAN_Z)
    print('CANON du manifeste (calcule, non annonce) :', emp(man)[0], '; brut', emp(man)[1])
    lignes = [l for l in man.decode('utf-8').split('\n') if re.match(r'^[0-9a-f]{16} [0-9a-f]{16} ', l)]
    print('lignes de pieces :', len(lignes), '(attendues 7)')
    if len(lignes) != 7:
        mauv.append('nombre de pieces : %d' % len(lignes))
    vus = set([NOM_MAN_Z])
    piece = {}
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        piece[nom] = h
        nz = PREF + nom
        vus.add(nz)
        if nz not in noms:
            mauv.append('absente du zip : ' + nz)
            continue
        raw = z.read(nz)
        piece_zip[nom] = raw
        e = emp(raw)
        if e[0] != h or e[1] != hb or str(e[2]) != ob or str(e[3]) != obr:
            mauv.append('empreinte/octets : %s : %s vs %s' % (nz, e, (h, hb, ob, obr)))
        p = os.path.join(R, 'ext', 'lot_m1', nz.replace('/', os.sep))
        if not os.path.isfile(p) or open(p, 'rb').read() != raw:
            mauv.append('ext/ differe du zip : ' + nz)
    print('pieces du zip :', len(noms), '; en trop :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
    if noms != vus:
        mauv.append('pieces du zip et du manifeste differentes')
    nm = 'rectificatif_gel_vide_partie2_C1_C2_machine1_v1.md'
    plat = open(MD_PLAT, 'rb').read()
    print('note a plat (Downloads) : canon', emp(plat)[0], '; note du lot :', emp(piece_zip[nm])[0], '; octets identiques :', plat == piece_zip[nm], '; annonce par le manifeste (ligne de description) : 336913aecc732cdf')
    if plat != piece_zip[nm] or emp(plat)[0] != '336913aecc732cdf':
        mauv.append('note a plat != note du lot ou canon annonce')
    # la note cite en section 5 cinq canons : ils doivent etre ceux du manifeste
    note = piece_zip[nm].decode('utf-8')
    cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+\.(?:py|log|json))\s*$', note[note.index('5. PIECES'):], flags=re.M)
    print('section 5 de la note : pieces citees avec canon :', len(cites))
    for h, nomc in cites:
        if piece.get(nomc) != h:
            mauv.append('canon cite par la note != manifeste : %s %s vs %s' % (nomc, h, piece.get(nomc)))

# entrees du script de m1 : canons recoupes
for k, (p, attendu) in ENTREES.items():
    e = emp(open(p, 'rb').read())
    print('entree %-26s canon %s (attendu %s) %s' % (k, e[0], attendu, 'OK' if e[0] == attendu else 'DIFFERENT'))
    if e[0] != attendu:
        mauv.append('entree %s : canon %s != %s' % (k, e[0], attendu))

# rejeu du script de m1 (code livre par m1, lance isole -I -B sur ses entrees)
sortie_dir = os.path.join(R, 'rejeu_machine2')
os.makedirs(sortie_dir, exist_ok=True)
script = os.path.join(R, 'ext', 'lot_m1', PREF.replace('/', os.sep), 'verifie_C1_C2_machine1_v1.py')
sortie_json = os.path.join(sortie_dir, 'verifie_C1_C2_rejoue_machine2.json')
r = subprocess.run([sys.executable, '-I', '-B', script, ENTREES['table gelee'][0], ENTREES['verifie_variantes_joues'][0], ENTREES['superposition'][0], sortie_json],
                   capture_output=True, text=True, cwd=sortie_dir)
print('rejeu : code de retour', r.returncode)
open(os.path.join(sortie_dir, 'verifie_C1_C2_rejoue_machine2.log'), 'w', newline='\n').write(r.stdout)
if r.returncode != 0:
    mauv.append('rejeu en echec : ' + r.stderr[-500:])
log_m1 = piece_zip['verifie_C1_C2_machine1_v1.log'].decode('utf-8').replace('\r\n', '\n')
print('console rejouee == log de m1 :', r.stdout.replace('\r\n', '\n') == log_m1)
if r.stdout.replace('\r\n', '\n') != log_m1:
    mauv.append('console rejouee differente du log de m1')
if os.path.isfile(sortie_json):
    j2 = emp(open(sortie_json, 'rb').read())
    j1 = emp(piece_zip['verifie_C1_C2_v1.json'])
    print('json rejoue canon %s ; json de m1 canon %s ; identiques : %s' % (j2[0], j1[0], j2[0] == j1[0]))
    if j2[0] != j1[0]:
        mauv.append('json rejoue != json de m1')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
