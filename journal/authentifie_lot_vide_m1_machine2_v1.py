# -*- coding: ascii -*-
"""Authentifie le lot HORS CHAINE de m1 'vide, etape sans run' (livraison 16e) : canon du manifeste (aucun canon annonce : pas d'ENVOI, on le CALCULE et on le dit), pieces aux DEUX canons et aux deux tailles, zip = manifeste + le manifeste lui-meme (rien en trop, rien en moins), note a plat = piece du lot.
Derive de authentifie_lot_releve_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_lot_vide_m1_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16e_vide_etape_sans_run'
ZIP = os.path.join(R, 'lot_machine1_2026-11-16_vide_etape_sans_run_v1_recu.zip')
NOTE_A_PLAT = os.path.join(R, 'note_machine1_vide_etape_sans_run_2026-11-16_v1.md')
PREFIXE = 'lot_machine1_2026-11-16_vide_etape_sans_run_v1/'
NOM_MAN = PREFIXE + 'MANIFESTE_lot_machine1_2026-11-16_vide_etape_sans_run_v1.txt'
NB_ATTENDU = 30  # pieces listees dans le manifeste (lues a l'oeil : lignes 5 a 34)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


mauv = []
with zipfile.ZipFile(ZIP) as z:
    noms = set(n for n in z.namelist() if not n.endswith('/'))
    man = z.read(NOM_MAN)
    print('CANON du manifeste (calcule, non annonce) :', emp(man)[0], '; brut', emp(man)[1])
    lignes = [l for l in man.decode('utf-8').split('\n') if re.match(r'^[0-9a-f]{16} [0-9a-f]{16} ', l)]
    print('lignes de pieces :', len(lignes), '(attendues %d)' % NB_ATTENDU)
    if len(lignes) != NB_ATTENDU:
        mauv.append('nombre de pieces')
    vus = set([NOM_MAN])
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        nom = PREFIXE + nom
        vus.add(nom)
        if nom not in noms:
            mauv.append('absente du zip : ' + nom)
            continue
        raw = z.read(nom)
        e = emp(raw)
        if e[0] != h or e[1] != hb or str(e[2]) != ob or str(e[3]) != obr:
            mauv.append('empreinte/octets : %s : %s vs %s' % (nom, e, (h, hb, ob, obr)))
        # coherence avec l'extraction deja faite sous ext/ (Expand-Archive)
        p = os.path.join(R, 'ext', nom.replace('/', os.sep))
        if not os.path.isfile(p) or open(p, 'rb').read() != raw:
            mauv.append('ext/ differe du zip : ' + nom)
    print('pieces du zip :', len(noms), '; en trop dans le zip :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
    if noms != vus:
        mauv.append('pieces du zip et du manifeste differentes')
    # la note a plat est la piece du lot ?
    a_plat = open(NOTE_A_PLAT, 'rb').read()
    en_lot = z.read(PREFIXE + 'note_machine1_vide_etape_sans_run_2026-11-16_v1.md')
    print('note a plat == note du lot (octets) :', a_plat == en_lot, '; canon', emp(a_plat)[0], '(annonce par le manifeste : 15641e09a351d56d)')
    if a_plat != en_lot or emp(a_plat)[0] != '15641e09a351d56d':
        mauv.append('note a plat')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
