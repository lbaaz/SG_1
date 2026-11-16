# -*- coding: ascii -*-
"""Authentifie le lot de m1 'reception de la certification de la premiere partie du gel du vide' (livraison 16g) : canon du manifeste (pas d'ENVOI : calcule), 10 pieces aux DEUX canons et aux deux tailles,
zip = manifeste + le manifeste, extraction ext/ identique au zip ; recoupe : le canon de la table commune de m1 (84bffbbd2f675181, annonce dans sa note) = le canon de la MIENNE ; sa note a le canon que son manifeste annonce.
Derive de authentifie_lot_vide_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_lot_reception_m1_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16g_reception_certification_vide'
NOM = 'lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1'
ZIP = os.path.join(R, NOM + '_recu.zip')
PREF = NOM + '/'
NOM_MAN = PREF + 'MANIFESTE_' + NOM + '.txt'
MIENNE = r'd:\devs\bocal\BOCAL4\certif_gel_vide_partie1_machine2\table_commune_vide_machine2_v1.json'


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
    print('lignes de pieces :', len(lignes), '(attendues 11 : la note, neuf pieces, le script de construction)')
    if len(lignes) != 11:
        mauv.append('nombre de pieces : %d' % len(lignes))
    vus = set([NOM_MAN])
    piece = {}
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        piece[nom] = h
        nom = PREF + nom
        vus.add(nom)
        if nom not in noms:
            mauv.append('absente du zip : ' + nom)
            continue
        raw = z.read(nom)
        e = emp(raw)
        if e[0] != h or e[1] != hb or str(e[2]) != ob or str(e[3]) != obr:
            mauv.append('empreinte/octets : %s : %s vs %s' % (nom, e, (h, hb, ob, obr)))
        p = os.path.join(R, 'ext', nom.replace('/', os.sep))
        if not os.path.isfile(p) or open(p, 'rb').read() != raw:
            mauv.append('ext/ differe du zip : ' + nom)
    print('pieces du zip :', len(noms), '; en trop :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
    if noms != vus:
        mauv.append('pieces du zip et du manifeste differentes')
    note = z.read(PREF + 'POUR_MACHINE2_reception_certification_gel_vide_partie1_machine1_v1.md').decode('utf-8')
    # les canons que la note cite en section 6 doivent etre ceux du manifeste
    cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+)\s*$', note[note.index('## 6.'):], flags=re.M)
    print('section 6 de la note : pieces citees avec canon :', len(cites))
    for h, nom in cites:
        if piece.get(nom) != h:
            mauv.append('canon cite par la note != manifeste : %s %s vs %s' % (nom, h, piece.get(nom)))
    # table commune de m1 vs la mienne
    tm1 = z.read(PREF + 'table_commune_vide_machine1_v1.json')
tmoi = open(MIENNE, 'rb').read()
print('canon de la table commune de m1 :', emp(tm1)[0], '; la mienne :', emp(tmoi)[0], '; annonce par m1 : 84bffbbd2f675181')
print('octets identiques :', tm1 == tmoi)
if emp(tm1)[0] != '84bffbbd2f675181' or emp(tmoi)[0] != '84bffbbd2f675181':
    mauv.append('canon de la table commune')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
