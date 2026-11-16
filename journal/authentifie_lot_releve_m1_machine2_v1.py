# -*- coding: ascii -*-
"""Authentifie le lot de m1 'releve apres les depots 99 et 100' (livraison 16d) : canon du manifeste, 8 pieces, zip interne = pieces a plat. Derive de authentifie_lot_acte_v2_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_lot_releve_m1_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16d_releve_apres_depot\ext'
MAN = os.path.join(R, 'MANIFEST_lot_machine1_releve_apres_depot_99_100_v1.txt')
ZIP = os.path.join(R, 'lot_machine1_2026-11-16_releve_apres_depot_99_100_v1.zip')
LOT = os.path.join(R, 'lot_m1')


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


man = open(MAN, 'rb').read()
print('CANON du manifeste :', emp(man)[0], '(annonce 860c0ca980977935)')
lignes = [l for l in man.decode('utf-8').split('\n') if re.match(r'^[0-9a-f]{16}  [0-9a-f]{16}  ', l)]
print('lignes de pieces :', len(lignes), '(annoncees 8)')
mauv = []
if emp(man)[0] != '860c0ca980977935':
    mauv.append('canon du manifeste')
if len(lignes) != 8:
    mauv.append('nombre de pieces')
vus = set()
os.makedirs(LOT, exist_ok=True)
with zipfile.ZipFile(ZIP) as z:
    noms = set(z.namelist())
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        vus.add(nom)
        if nom not in noms:
            mauv.append('absente du zip : ' + nom)
            continue
        raw = z.read(nom)
        e = emp(raw)
        if e[0] != h or e[1] != hb or str(e[2]) != ob or str(e[3]) != obr:
            mauv.append('empreinte/octets : %s : %s vs %s' % (nom, e, (h, hb, ob, obr)))
        p = os.path.join(LOT, nom)
        if not os.path.isfile(p) or open(p, 'rb').read() != raw:
            open(p, 'wb').write(raw)
    print('pieces du zip :', len(noms), '; en trop dans le zip :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
    if noms != vus:
        mauv.append('pieces du zip et du manifeste differentes')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
