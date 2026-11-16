# -*- coding: ascii -*-
"""Authentifie le lot de m1 'acte du gel largeur du vide, VERSION 2' (livraison 16k) : canon du manifeste (pas d'ENVOI : calcule), 6 pieces aux DEUX canons et aux deux tailles, zip = manifeste + pieces, ext/ identique au zip,
note de l'acte a plat (Downloads) = note du lot (16ba5e594ab18717), pas de piece en trop ; la section 4 de la note d'accompagnement cite des canons : ils doivent etre ceux du manifeste.
Recoupe aussi le canon de MON lot de contreseing que l'acte cite (e1dfb7ba7b18196e), celui de ma note (700a39a9a7223fd0) et celui de la v1 (464ba00a6905e3a5). Derive de authentifie_acte_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_acte_v2_m1_machine2_v1.py"""
import hashlib
import os
import re
import unicodedata
import zipfile

B = r'd:\devs\bocal\BOCAL4'
R = os.path.join(B, 'livraison_16k_acte_gel_vide_v2')
NOM = 'lot_machine1_2026-11-16_acte_gel_vide_v2'
ZIP = os.path.join(R, NOM + '.zip')
MD_PLAT = os.path.join(R, 'journal_delta_nn_largeur_vide_v2.md')
NOM_MAN = 'MANIFESTE_' + NOM + '.txt'
NOTE_ACTE = 'journal_delta_nn_largeur_vide_v2.md'
NOTE_ACC = 'POUR_MACHINE2_acte_gel_vide_machine1_v2.md'


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


mauv = []
piece_zip = {}
manifeste_canon = {}
with zipfile.ZipFile(ZIP) as z:
    noms = set(n for n in z.namelist() if not n.endswith('/'))
    cand = [n for n in noms if n.endswith(NOM_MAN)]
    if len(cand) != 1:
        raise SystemExit('manifeste introuvable ou multiple : %s' % cand)
    NOM_MAN_Z = cand[0]
    PREF = NOM_MAN_Z[:len(NOM_MAN_Z) - len(NOM_MAN)]
    print('prefixe des pieces dans le zip : %r ; fichiers dans le zip : %d' % (PREF, len(noms)))
    man = z.read(NOM_MAN_Z)
    print('CANON du manifeste (calcule, non annonce) :', emp(man)[0], '; brut', emp(man)[1])
    lignes = [l for l in man.decode('utf-8').split('\n') if re.match(r'^[0-9a-f]{16} [0-9a-f]{16} ', l)]
    print('lignes de pieces :', len(lignes), '(attendues 6)')
    if len(lignes) != 6:
        mauv.append('nombre de pieces : %d' % len(lignes))
    vus = set([NOM_MAN_Z])
    for l in lignes:
        h, hb, ob, obr, nom = re.split(r'\s+', l.strip(), maxsplit=4)
        manifeste_canon[nom] = h
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
    plat = open(MD_PLAT, 'rb').read()
    print('note de l acte a plat (Downloads) : canon', emp(plat)[0], '; note du lot :', emp(piece_zip[NOTE_ACTE])[0], '; octets identiques :', plat == piece_zip[NOTE_ACTE], '; annonce (description du manifeste) : 16ba5e594ab18717')
    if plat != piece_zip[NOTE_ACTE] or emp(plat)[0] != '16ba5e594ab18717':
        mauv.append('note a plat != note du lot ou canon annonce')
    acc = piece_zip[NOTE_ACC].decode('utf-8')
    cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+\.(?:py|log|json|md))\s*$', acc[acc.index('4. PIECES'):], flags=re.M)
    print('section 4 de la note d accompagnement : pieces citees avec canon :', len(cites))
    for h, nomc in cites:
        if manifeste_canon.get(nomc) != h:
            mauv.append('canon cite par la note d accompagnement != manifeste : %s %s vs %s' % (nomc, h, manifeste_canon.get(nomc)))
    if len(cites) != 4:
        mauv.append('la note d accompagnement cite %d canons, attendus 4 (la cinquieme ligne est "(ce script)", sans canon)' % len(cites))
# les trois canons nouveaux de nn.12, contre mes fichiers
CIB = {
    '464ba00a6905e3a5': os.path.join(B, r'livraison_16j_acte_gel_vide\journal_delta_nn_largeur_vide_v1.md'),
    'e1dfb7ba7b18196e': os.path.join(B, 'MANIFEST_lot_machine2_contreseing_acte_gel_vide_v1.txt'),
    '700a39a9a7223fd0': os.path.join(B, 'POUR_MACHINE1_contreseing_acte_gel_vide_machine2_v1.md'),
}
for h, p in CIB.items():
    c = emp(open(p, 'rb').read())[0]
    print('  canon %s : mon fichier %s -> %s' % (h, os.path.basename(p), 'OK' if c == h else 'DIFFERENT : ' + c))
    if c != h:
        mauv.append('canon cite %s != fichier %s (%s)' % (h, os.path.basename(p), c))
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
