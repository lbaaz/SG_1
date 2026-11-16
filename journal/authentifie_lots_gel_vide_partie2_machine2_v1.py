# -*- coding: ascii -*-
"""Authentifie l'enveloppe 16g de m1 (gel du vide, SECONDE partie) : lot de la partie 2 (canon du manifeste CALCULE : pas d'ENVOI), pieces aux DEUX canons et aux deux tailles, zip = manifeste + le manifeste,
extraction ext/x_gel_vide_partie2 identique au zip ; recoupe de la section 16 du gel (24 lignes, chaque piece citee par son canon B) avec le manifeste ; recoupe des canons de la section 4.1 ; le .md a plat = le .md du lot ;
le lot de reception de l'enveloppe = celui deja recu (octets). Derive de authentifie_lots_gel_vide_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_lots_gel_vide_partie2_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16h_gel_vide_partie2'
EXT = os.path.join(R, 'ext')
NOM = 'lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1'
MD = 'gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md'


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


mauv = []
pref = NOM + '/'
nom_man = pref + 'MANIFESTE_' + NOM + '.txt'
with zipfile.ZipFile(os.path.join(EXT, NOM + '.zip')) as z:
    noms = set(n for n in z.namelist() if not n.endswith('/'))
    man = z.read(nom_man)
    print('LOT', NOM)
    print('  CANON du manifeste (calcule, non annonce) :', emp(man)[0])
    lignes = [l for l in man.decode('utf-8').split('\n') if re.match(r'^[0-9a-f]{16} [0-9a-f]{16} ', l)]
    print('  lignes de pieces :', len(lignes))
    vus = set([nom_man])
    piece = {}
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        piece[nom] = h
        nom = pref + nom
        vus.add(nom)
        if nom not in noms:
            mauv.append('absente du zip : ' + nom)
            continue
        raw = z.read(nom)
        e = emp(raw)
        if e[0] != h or e[1] != hb or str(e[2]) != ob or str(e[3]) != obr:
            mauv.append('empreinte/octets : %s : %s vs %s' % (nom, e, (h, hb, ob, obr)))
        p = os.path.join(EXT, 'x_gel_vide_partie2', nom.replace('/', os.sep))
        if not os.path.isfile(p) or open(p, 'rb').read() != raw:
            mauv.append('ext/ differe du zip : ' + nom)
    print('  pieces du zip :', len(noms), '; en trop :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
    if noms != vus:
        mauv.append('pieces du zip et du manifeste differentes')
    dans_lot = z.read(pref + MD)
a_plat = open(os.path.join(R, MD), 'rb').read()
print('md a plat == md du lot (octets) :', a_plat == dans_lot, '; canon', emp(a_plat)[0], '; (dans le manifeste : %s)' % piece.get(MD))
if a_plat != dans_lot or emp(a_plat)[0] != piece.get(MD):
    mauv.append('md a plat')
txt = a_plat.decode('utf-8')
sec16 = txt[txt.index('16. PIECES DE CE LOT'):]
cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+)\s*$', sec16, flags=re.M)
print('section 16 : pieces citees avec canon :', len(cites))
m16 = []
for h, nom in cites:
    if nom not in piece:
        m16.append('citee mais absente du manifeste : ' + nom)
    elif piece[nom] != h:
        m16.append('canon different : %s : gel %s, manifeste %s' % (nom, h, piece[nom]))
print('  morsures section 16 :', len(m16))
for m in m16:
    print('    -', m)
mauv += m16
print('  pieces du manifeste NON citees en section 16 (attendues : le md, POUR_MACHINE2, le script de construction) :', sorted(n for n in piece if n not in set(x[1] for x in cites)))
# section 4.1 : les cinq pieces nommees
sec41 = txt[txt.index('4.1 Les pieces'):txt.index('4.2 Le deroulement')]
c41 = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+\.(?:json|py))\b', sec41, flags=re.M)
print('section 4.1 : pieces citees :', len(c41))
for h, nom in c41:
    if piece.get(nom) != h:
        mauv.append('section 4.1 : %s %s vs manifeste %s' % (nom, h, piece.get(nom)))
# lot de reception de l'enveloppe = celui deja recu
a = open(os.path.join(EXT, 'lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1.zip'), 'rb').read()
b = open(r'd:\devs\bocal\BOCAL4\livraison_16g_reception_certification_vide\lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1_recu.zip', 'rb').read()
print('lot de reception de l enveloppe == lot deja recu (octets) :', a == b)
if a != b:
    mauv.append('lot de reception')
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
