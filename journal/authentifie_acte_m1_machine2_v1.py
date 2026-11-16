# -*- coding: ascii -*-
"""Authentifie le lot de m1 'acte du gel largeur du vide, projet v1 a contresigner' (livraison 16j) : canon du manifeste (pas d'ENVOI : calcule), 16 pieces aux DEUX canons et aux deux tailles, zip = manifeste + pieces,
ext/ identique au zip, note de l'acte a plat (Downloads) = note du lot (464ba00a6905e3a5), pas de piece en trop ; la section 3 de la note d'accompagnement cite des canons : ils doivent etre ceux du manifeste.
Puis RECOUPE les 23 canons que l'acte cite en nn.12 contre MES fichiers (ceux que je peux calculer) : un canon cite qui n'est pas celui du fichier est une morsure de l'acte.
Derive de authentifie_rectificatif_m1_machine2_v1.py (non edite).
Usage : py -3.11 -I authentifie_acte_m1_machine2_v1.py"""
import glob
import hashlib
import os
import re
import unicodedata
import zipfile

B = r'd:\devs\bocal\BOCAL4'
R = os.path.join(B, 'livraison_16j_acte_gel_vide')
NOM = 'lot_machine1_2026-11-16_acte_gel_vide_v1'
ZIP = os.path.join(R, NOM + '.zip')
MD_PLAT = os.path.join(R, 'journal_delta_nn_largeur_vide_v1.md')
NOM_MAN = 'MANIFESTE_' + NOM + '.txt'
NOTE_ACTE = 'journal_delta_nn_largeur_vide_v1.md'
NOTE_ACC = 'POUR_MACHINE2_acte_gel_vide_machine1_v1.md'
L = os.path.join(B, r'livraison_16h_gel_vide_partie2\ext\x_gel_vide_partie2\lot_machine1_2026-11-16_gel_vide_partie2_instrument_enonces_v1')


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def canon_fichier(p):
    return emp(open(p, 'rb').read())[0]


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
    print('lignes de pieces :', len(lignes), '(attendues 16 : la note d accompagnement, la note de l acte, quatorze autres)')
    if len(lignes) != 16:
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
    print('note de l acte a plat (Downloads) : canon', emp(plat)[0], '; note du lot :', emp(piece_zip[NOTE_ACTE])[0], '; octets identiques :', plat == piece_zip[NOTE_ACTE], '; annonce (ligne de description du manifeste) : 464ba00a6905e3a5')
    if plat != piece_zip[NOTE_ACTE] or emp(plat)[0] != '464ba00a6905e3a5':
        mauv.append('note a plat != note du lot ou canon annonce')
    acc = piece_zip[NOTE_ACC].decode('utf-8')
    cites = re.findall(r'^\s+([0-9a-f]{16})\s+(\S+\.(?:py|log|json|md))\s*$', acc[acc.index('3. PIECES'):], flags=re.M)
    print('section 3 de la note d accompagnement : pieces citees avec canon :', len(cites))
    for h, nomc in cites:
        if manifeste_canon.get(nomc) != h:
            mauv.append('canon cite par la note d accompagnement != manifeste : %s %s vs %s' % (nomc, h, manifeste_canon.get(nomc)))
    acte = piece_zip[NOTE_ACTE].decode('utf-8')

# recoupe : les canons cites par l'acte en nn.12
def un(motif, base=B):
    c = glob.glob(os.path.join(base, motif), recursive=True)
    if len(c) != 1:
        raise SystemExit('fichier introuvable ou multiple : %s -> %s' % (motif, c))
    return c[0]

lotp = lambda n: os.path.join(R, 'ext', 'lot_m1', NOM, n)
CIBLES = {
    'b57c9ccdd3946261': un(r'livraison_16f_gel_vide_partie1\gel_largeur_vide_partie1_regle_tirage_pre_enregistrement_v1.md'),
    'eebd979f18d8db48': un(r'livraison_16h_gel_vide_partie2\gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md'),
    'b71206e5daf6c741': os.path.join(L, 'table_cellules_gel_vide_v1.json'),
    '49a40d9098b55361': un(r'livraison_16f_gel_vide_partie1\ext\**\chaine_adaptee_bloc_machine1_v1.py'),
    '336913aecc732cdf': un(r'livraison_16i_rectificatif_gel_vide_partie2\rectificatif_gel_vide_partie2_C1_C2_machine1_v1.md'),
    'd4f95772710d545c': os.path.join(B, 'MANIFEST_lot_machine2_certification_gel_vide_partie1_v1.txt'),
    '5921fcd984d6de5b': os.path.join(B, 'MANIFEST_lot_machine2_tirage_graine_gel_vide_v1.txt'),
    'f989369a3ac22f98': os.path.join(B, 'MANIFEST_lot_machine2_certification_gel_vide_partie2_v1.txt'),
    '9a14bf95fa8c6d20': os.path.join(B, 'MANIFEST_lot_machine2_resultat_run_gel_vide_v1.txt'),
    '2913b7aa82184ef1': os.path.join(B, 'POUR_MACHINE1_certification_gel_vide_partie2_machine2_v1.md'),
    'bcaf377489a0e1ff': os.path.join(B, 'POUR_MACHINE1_resultat_run_gel_vide_machine2_v1.md'),
    'a38b1550f8f5e3cf': os.path.join(L, 'pilote_gel_vide_machine1_v1.py'),
    '5a73b5a492d5d4a2': os.path.join(B, r'run_gel_vide_machine2\lance_run_vide_machine2_v1.py'),
    '2d8e6692d862fa37': os.path.join(B, r'run_gel_vide_machine2\run_1\pilote_gel_vide.log'),
    'cc54f4bc4e175143': os.path.join(B, r'run_gel_vide_machine2\run_1\verdict_ter_instrument.json'),
    '8472dba8919a9b6e': os.path.join(B, r'run_gel_vide_machine2\run_1\verdict_vide.json'),
    '47bb39ef530a967c': lotp('verdict_vide_rejoue_machine1.json'),
    'c95df19ff2f16ff7': os.path.join(B, r'resultats_run_vide_machine2\verdict_vide_feuille_machine2.json'),
    'c815876f0ff7d66b': lotp('reception_resultat_gel_vide_machine1_v1.py'),
    '4adc285659120eb8': lotp('essai_reception_resultat_machine1_v1.py'),
    '957ce0b198a5f31b': lotp('reception_resultat_vide_v1.json'),
    'f1d08f97d5301157': lotp('lecture_resultat_vide_machine1_v1.py'),
    'af0b3d8cdd0b4fa5': lotp('lecture_resultat_vide_v1.json'),
}
nn12 = acte[acte.index('nn.12 PIECES'):]
cites12 = re.findall(r'^\s+([0-9a-f]{16})\s+(.+?)\s*$', nn12, flags=re.M)
print('nn.12 : canons cites :', len(cites12), '; attendus 23')
if len(cites12) != 23:
    mauv.append('nn.12 cite %d canons, attendus 23' % len(cites12))
ok = 0
for h, quoi in cites12:
    p = CIBLES.get(h)
    if p is None:
        mauv.append('canon cite par nn.12 que je ne sais pas relier a un fichier : %s (%s)' % (h, quoi))
        print('  ?? %s  %s : je ne sais pas le relier' % (h, quoi))
        continue
    c = canon_fichier(p)
    etat = 'OK' if c == h else 'DIFFERENT : le fichier a le canon %s' % c
    if c == h:
        ok += 1
    else:
        mauv.append('nn.12 : %s (%s) : fichier au canon %s' % (h, quoi, c))
    print('  %s  %-62s %s' % (h, quoi, etat))
print('canons de nn.12 recoupes contre les fichiers : %d sur %d' % (ok, len(cites12)))
print('MORSURES :', len(mauv))
for m in mauv:
    print('  -', m)
