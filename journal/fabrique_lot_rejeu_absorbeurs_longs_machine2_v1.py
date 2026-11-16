# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'rejeu (i) sous absorbeurs longs, par le lecteur creux de machine 2, hors chaine' -- manifeste + ZIP. 2026-11-15.
Derive de fabrique_lot_lecteur_creux_machine2_v1.py (non edite). Usage : py -3.11 -P fabrique_lot_rejeu_absorbeurs_longs_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le lot de machine 1 (4103eae43f989877) et sa note (42c822811167b826) RECALCULES depuis son zip et son
manifeste ; MON lot precedent (c8164e6d80ee0b60) recalcule de son manifeste et de son zip, et le canon du lecteur importe par le rejeu relu dans ce
manifeste ; les totaux du rejeu relus dans le JSON ET dans les journaux ; chaque chiffre de la note relu dans le JSON ou un journal ; chaque canon de
piece nomme dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'lecteur_creux_m2/'
S = D + 'sortie/'
NOM = 'lot_machine2_2026-11-15_rejeu_absorbeurs_longs_hors_chaine_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_rejeu_absorbeurs_longs_hors_chaine_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_rejeu_absorbeurs_longs_machine2_v1.md'
SELF = 'fabrique_lot_rejeu_absorbeurs_longs_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-15_note_piste0_reprise_v1_recu.zip'
MAN_M1 = 'MANIFEST_lot_machine1_note_piste0_reprise_v1.txt'
LOT_M2 = 'lot_machine2_2026-11-15_lecteur_creux_hors_chaine_v1.zip'
MAN_M2 = 'MANIFEST_lot_machine2_lecteur_creux_hors_chaine_v1.txt'
PIECES = [D + x for x in ('rejeu_absorbeurs_longs_machine2_v1.py', 'comparaison_rejeu_note_machine1_machine2_v1.py',
                          'ecart_deux_lectures_rejeu_machine2_v1.py', 'marges_ancrage_rejeu_machine2_v1.py')] + \
         [S + x for x in ('rejeu_absorbeurs_longs_machine2_v1.log', 'rejeu_absorbeurs_longs_machine2_v1.json',
                          'comparaison_rejeu_note_machine1_machine2_v1.log', 'ecart_deux_lectures_rejeu_machine2_v1.log',
                          'marges_ancrage_rejeu_machine2_v1.log')] + [SELF]
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


def lire_manifeste(raw):
    att = {}
    for l in raw.decode('utf-8').split('\n'):
        p = l.split()
        if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
            att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
    return att


for p in PIECES + [NOTE, LOT_M1, MAN_M1, LOT_M2, MAN_M2, 'lecteur_creux_m2/lecteur_2D_creux_machine2_v1.py']:
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

# --- les deux entrants, recalcules : le lot de machine 1 et mon lot du lecteur
for nomlot, lot, man, canon_att, nb in (('machine 1', LOT_M1, MAN_M1, '4103eae43f989877', 34), ('machine 2 (lecteur)', LOT_M2, MAN_M2, 'c8164e6d80ee0b60', 14)):
    mraw = open(os.path.join(ICI, man), 'rb').read()
    zl = zipfile.ZipFile(os.path.join(ICI, lot))
    att = lire_manifeste(mraw)
    noms = [n for n in zl.namelist() if not n.startswith('MANIFEST_')] if nomlot != 'machine 1' else zl.namelist()
    if emp(mraw)[0] != canon_att or len(att) != nb or sorted(att) != sorted(noms):
        arrets.append('lot %s : canon %s, %d pieces' % (nomlot, emp(mraw)[0], len(att)))
    if [n for n in att if n in zl.namelist() and emp(zl.read(n)) != att[n]]:
        arrets.append('lot %s : des pieces ne sont pas au canon' % nomlot)
    if nomlot == 'machine 1' and emp(zl.read('note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md'))[0] != '42c822811167b826':
        arrets.append('la note de machine 1 n est pas 42c822811167b826')
    if nomlot != 'machine 1':
        att_m2 = att
# le lecteur importe par le rejeu est celui du lot scelle
lec = 'lecteur_creux_m2/lecteur_2D_creux_machine2_v1.py'
if att_m2.get(lec, ('',))[0] != emp(open(os.path.join(ICI, lec), 'rb').read())[0] or att_m2[lec][0] != '851ba46a01c023ef':
    arrets.append('le lecteur sur le disque n est pas celui du lot c8164e6d80ee0b60 (851ba46a01c023ef)')
for c in ('4103eae43f989877', '42c822811167b826', 'c8164e6d80ee0b60', '8d54bf9', '82a0be882568fe0c', 'c110c6286157b025', '1ae4b5b2f9ff0e70', '4d51dd58ef456fe9'):
    if c not in nn:
        arrets.append('la note ne nomme pas %s' % c)

# --- le journal principal et le JSON
rj = json.load(open(os.path.join(ICI, S + 'rejeu_absorbeurs_longs_machine2_v1.json'), encoding='ascii'))
rl = lit(S + 'rejeu_absorbeurs_longs_machine2_v1.log')
for x in ('canon du moteur : 82a0be882568fe0c (attendu 82a0be882568fe0c)', 'canon de sonde2 : c110c6286157b025 (attendu c110c6286157b025)',
          'canon de sonde1 : 1ae4b5b2f9ff0e70 (attendu 1ae4b5b2f9ff0e70)', 'canon de tp_ref : 4d51dd58ef456fe9 (attendu 4d51dd58ef456fe9)',
          'taches : 34', 'duree totale : 826.3 s', 'R2 : 49 sur 74 configurations ; R3 : 74 sur 74', 'python 3.11.9, numpy 2.2.6, scipy 1.15.3'):
    if x not in rl:
        arrets.append('journal du rejeu : %r absent' % x)
ntot = npt = ntp = nperdus = 0
res_max, ident_min, plA, plB, n_mord, abs_max, rel_hors3, n_hors3 = 0.0, 2.0, 0, 0, 0, 0.0, 0.0, 0
mord_k = set()
tp = {}
for r in rj['resultats']:
    for c, x in r['configs'].items():
        ntot += 1
        m = x['resume']
        nperdus += len(m['perdus'])
        res_max = max(res_max, m['pire_residu'])
        if r['nature'] == 'pt':
            npt += 1
            ident_min = min(ident_min, x['identite_M17'])
            plA += bool(m['plateau_A']['plateau'])
            plB += bool(m['plateau_B']['plateau'])
        else:
            ntp += 1
            tp[(r['nom'], c)] = (x['consecutifs_depuis_m5'], x['pire_ecart_consecutifs'], m['plateau_A']['Gamma_pl'] / r['Gamma_ref'], r['u_ref'])
        mord = False
        for ks, rec in x['lect'].items():
            if not rec.get('suivi'):
                continue
            dr = abs(rec['gamma_E'] - rec['gamma_W']) / rec['gamma_W']
            if int(ks) == 3:
                abs_max = max(abs_max, abs(rec['gamma_E'] - rec['gamma_W']))
                if dr > 1e-6:
                    mord = True
                    mord_k.add(int(ks))
            else:
                rel_hors3 = max(rel_hors3, dr)
                n_hors3 += 1
                if dr > 1e-6:
                    mord_k.add(int(ks))
        n_mord += mord
if (ntot, npt, ntp, nperdus) != (74, 66, 8, 0):
    arrets.append('trajectoires %d (points %d, temoin %d), suivis perdus %d' % (ntot, npt, ntp, nperdus))
if not (7.3e-13 <= res_max < 7.4e-13) or ident_min < 0.9999999999 or (plA, plB) != (65, 65) or n_mord != 25 or mord_k != {3} or not (2.0e-15 < abs_max < 2.2e-15) \
        or n_hors3 != 1406 or not (8.1e-12 < rel_hors3 < 8.3e-12):
    arrets.append('chiffres du JSON hors de la note : residu %.2e identite %.12f plateaux %d %d morsures %d k %s abs %.2e hors k = 3 : %d lectures, %.2e' %
                  (res_max, ident_min, plA, plB, n_mord, sorted(mord_k), abs_max, n_hors3, rel_hors3))
attendu_tp = {('j06', 'F1_60'): (9, 0.00071), ('j06', 'F2_60'): (8, 0.00071), ('j06', 'F1_80'): (11, 0.00103), ('j06', 'F2_80'): (10, 0.00103),
              ('j08', 'F1_60'): (9, 0.00128), ('j08', 'F2_60'): (8, 0.00046), ('j08', 'F1_80'): (10, 0.00060), ('j08', 'F2_80'): (9, 0.00008)}
for k, (n_, p_) in attendu_tp.items():
    if tp[k][0] != n_ or abs(tp[k][1] - p_) > 6e-6:
        arrets.append('temoin %s : %s, la note dit %s' % (k, tp[k][:2], (n_, p_)))
for j, (lo, hi, u) in (('j06', (1.00070, 1.00072, 0.0021)), ('j08', (1.00005, 1.00007, 0.00017))):
    for k, v in tp.items():
        if k[0] == j and not (lo <= v[2] <= hi and abs(v[3] - u) < 0.00005):
            arrets.append('temoin %s : rapport %.5f, incertitude %.5f' % (k, v[2], v[3]))
rapports = {j: [v[2] for k, v in tp.items() if k[0] == j] for j in ('j06', 'j08')}
if max(max(v) - min(v) for v in rapports.values()) > 1e-5:
    arrets.append('les quatre plateaux d un meme j different de plus de 1e-5 : %s' % rapports)

# --- le comparateur, l'ecart des deux lectures, les marges
cl = lit(S + 'comparaison_rejeu_note_machine1_machine2_v1.log')
for x in ('canon de la note : 42c822811167b826 (attendu 42c822811167b826) OK',
          'C1 valeurs a 0.2 % : 30 sur 30 (pire 4.54e-05) ; C2 verdict PLATEAU : 30 sur 30 ; etalement a 0.10 point : 30 sur 30 ; compte (a) egal : 30 sur 30',
          'C3 cellules egales a l arrondi : echelle B 60 sur 60, echelle A 60 sur 60', 'C4 : 8 trajectoires sur 8 dans la description de la note',
          '  ident   66 sur 66', '  R3      74 sur 74', '  residu  74 sur 74', '  EW      49 sur 74', '  suivi   74 sur 74',
          'identite minimale avec l etat de M17 : 1.000000'):
    if x not in cl:
        arrets.append('journal de la comparaison : %r absent' % x)
if 'ECART' in cl.split('TABLEAU 5')[0]:
    arrets.append('une cellule du tableau 4 est marquee ECART')
el = lit(S + 'ecart_deux_lectures_rejeu_machine2_v1.log')
for x in ('trajectoires : 74 ; dont au moins un barreau a plus de 1e-6 relatif : 25', 'pire ecart absolu : 2.080e-15', 'k concernes : [3]'):
    if x not in el:
        arrets.append('journal de l ecart des deux lectures : %r absent' % x)
ml = lit(S + 'marges_ancrage_rejeu_machine2_v1.log')
att_marges = {'39_20': ('1.093', '1.034', '1.093'), '197_100': ('1.013', '1.013', '1.092'), '99_50': ('1.003', '1.003', '1.082'),
              '101_50': ('1.031', '1.031', '1.031'), '203_100': ('1.019', '1.019', '1.019'), '41_20': ('1.004', '1.004', '1.004')}
for nom, (a, b, c) in att_marges.items():
    m = re.search(r'^%s\s+([\d.]+)\s+\|\s+([\d.]+)\s+([\d.]+) \(' % nom, ml, re.M)
    if not m or m.groups() != (a, b, c):
        arrets.append('marges %s : %s, attendu %s' % (nom, m.groups() if m else None, (a, b, c)))
for x in ('j06 F1_60  rec 0.9999 second 0.0001 rapport 16381.380', 'j08 F1_60  rec 0.9999 second 0.0001 rapport 11518.007'):
    if x not in ml:
        arrets.append('journal des marges : %r absent' % x)
for x in ('74 trajectoires', '30 cellules sur 30', '4.5e-5', '60 cellules sur 60', '65 trajectoires sur 66', '0.128 %', '1.00071', '1.00006', '0.21 %',
          '0.016 %', '0.9999999999', '7.3e-13', '49 sur 74', '25 trajectoires sur 74', '2.1e-15', '8.2e-12', '1406 barreaux', '826 s', '16381', '11518',
          '1.093, 1.013, 1.003, 1.031, 1.019, 1.004', 'de 1.034 a 1.093 (1.95), 1.013 a 1.092 (1.97), 1.003 a 1.082 (1.98), 1.031 (2.02), 1.019 (2.03), 1.004 (2.05)',
          'F2 60 : 0.22 % ; F2 80 : 0.06 % ; F1 80 : 1.52 % ; F3 60 : 1.48 % ; F1 translate : 0.56 %', '9.13 %', '14400 etats', '74 s', '407 s'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- REJEU (i) PAR LE LECTEUR 2D CREUX DE MACHINE 2 (lot c8164e6d80ee0b60, NON CERTIFIE), HORS CHAINE, POST HOC, NON OPPOSABLE, sur l ordre de '
    'l operateur ("Oui rejoue") : absorbeurs longs de la note de machine 1 (42c822811167b826), aux seuls six points de M17 et au jumeau H+ (74 trajectoires). '
    '30 cellules sur 30 du tableau 4 et 60 sur 60 du tableau 5 de la note de machine 1 retrouvees, temoin 8 sur 8 ; l ancrage designe l etat de M17 dans les 66 '
    'cas ; une epreuve declaree d avance mord (ecart des deux lectures au barreau d ancrage, 2.1e-15 absolu). Aucun point des deltas 96, 97, 98, aucun point '
    'neuf (E19). Rien a certifier ni a contresigner. machine 2\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 4103eae43f989877 (note 42c822811167b826) ; mon lot du lecteur c8164e6d80ee0b60 ; sonde dense deposee, lots '
              'a01598ec24237921 (sonde_etage2 c110c6286157b025, sonde_etage1 1ae4b5b2f9ff0e70) ; reference du temoin 4d51dd58ef456fe9 ; moteur 82a0be882568fe0c ; '
              'gel bis dcda1611adf5f8fd ; registre 8d54bf9\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu_zip = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu_zip[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu_zip.get(n)]
    manque = sorted(set(attendu_zip) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
