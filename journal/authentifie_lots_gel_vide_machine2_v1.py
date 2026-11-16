# -*- coding: ascii -*-
"""Authentifie les DEUX lots neufs de l'enveloppe 16f de m1 (gel du vide, partie 1 ; note 'loi d'echelle') : canon du manifeste,
pieces aux DEUX canons et aux deux tailles, zip = manifeste + le manifeste (rien en trop, rien en moins), extraction ext/x_* identique au zip.
Pour le lot du gel : la section 13 du gel (md) cite chaque piece par son canon B -> recoupement avec le manifeste ; le md du lot = le md a plat.
Pour le lot de la loi d'echelle : canon annonce par le gel (408b8a595cad0040). Le lot du vide, deja authentifie (livraison 16e), est compare par octets.
Derive de authentifie_lot_vide_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_lots_gel_vide_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

R = r'd:\devs\bocal\BOCAL4\livraison_16f_gel_vide_partie1'
EXT = os.path.join(R, 'ext')
MD_A_PLAT = os.path.join(R, 'gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md')


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def authentifie(nom_lot, dossier_x, canon_annonce):
    mauv = []
    zp = os.path.join(EXT, nom_lot + '.zip')
    pref = nom_lot + '/'
    nom_man = pref + 'MANIFESTE_' + nom_lot + '.txt'
    with zipfile.ZipFile(zp) as z:
        noms = set(n for n in z.namelist() if not n.endswith('/'))
        man = z.read(nom_man)
        c = emp(man)[0]
        print('LOT', nom_lot)
        print('  CANON du manifeste (calcule) :', c, '; annonce :', canon_annonce)
        if canon_annonce and c != canon_annonce:
            mauv.append('canon du manifeste')
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
            p = os.path.join(EXT, dossier_x, nom.replace('/', os.sep))
            if not os.path.isfile(p) or open(p, 'rb').read() != raw:
                mauv.append('ext/ differe du zip : ' + nom)
        print('  pieces du zip :', len(noms), '; en trop :', sorted(noms - vus), '; manquantes :', sorted(vus - noms))
        if noms != vus:
            mauv.append('pieces du zip et du manifeste differentes')
    print('  MORSURES :', len(mauv))
    for m in mauv:
        print('    -', m)
    return piece, mauv, c


tot = 0
piece_g, m1, canon_gel = authentifie('lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1', 'x_gel_vide_partie1_regle_tirage', None)
piece_l, m2, canon_loi = authentifie('lot_machine1_2026-11-16_loi_echelle_etape0_v1', 'x_loi_echelle_etape0', '408b8a595cad0040')
tot += len(m1) + len(m2)

# le md a plat est la piece du lot, et son canon est celui que la note POUR_MACHINE2 annonce
md_nom = 'gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md'
a_plat = open(MD_A_PLAT, 'rb').read()
dans_lot = open(os.path.join(EXT, 'x_gel_vide_partie1_regle_tirage', 'lot_machine1_2026-11-16_gel_vide_partie1_regle_tirage_v1', md_nom), 'rb').read()
print('md a plat == md du lot (octets) :', a_plat == dans_lot, '; canon', emp(a_plat)[0], '(annonce : b57c9ccdd3946261)')
if a_plat != dans_lot or emp(a_plat)[0] != 'b57c9ccdd3946261':
    tot += 1

# section 13 du gel : chaque piece citee par son canon B -> le manifeste du lot doit porter le meme canon pour ce nom
txt = a_plat.decode('utf-8')
sec13 = txt[txt.index('13. PIECES DE CE LOT'):]
cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+)\s*$', sec13, flags=re.M)
print('section 13 : pieces citees avec canon :', len(cites))
mauv13 = []
for h, nom in cites:
    if nom not in piece_g:
        mauv13.append('citee mais absente du manifeste : ' + nom)
    elif piece_g[nom] != h:
        mauv13.append('canon different : %s : gel %s, manifeste %s' % (nom, h, piece_g[nom]))
print('  morsures section 13 :', len(mauv13))
for m in mauv13:
    print('    -', m)
tot += len(mauv13)
non_citees = sorted(n for n in piece_g if n not in set(x[1] for x in cites))
print('  pieces du manifeste NON citees en section 13 (attendues : le md lui-meme, la note POUR_MACHINE2, le script de construction) :', non_citees)

# lot du vide : identique par octets a celui deja authentifie (livraison 16e) ?
a = open(os.path.join(EXT, 'lot_machine1_2026-11-16_vide_etape_sans_run_v1.zip'), 'rb').read()
b = open(r'd:\devs\bocal\BOCAL4\livraison_16e_vide_etape_sans_run\lot_machine1_2026-11-16_vide_etape_sans_run_v1_recu.zip', 'rb').read()
print('lot du vide de l enveloppe == lot deja recu (octets) :', a == b)
if a != b:
    tot += 1
print('MORSURES TOTAL :', tot)
