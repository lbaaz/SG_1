# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'lecteur 2D creux de machine 2, hors chaine, non certifie' -- manifeste + ZIP. 2026-11-15. Derive de
fabrique_lot_contreseing_acte_ordre2_machine2_v1.py (non edite). Usage : python -P fabrique_lot_lecteur_creux_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le lot de machine 1 (4103eae43f989877) et sa note (42c822811167b826) RECALCULES depuis son zip et
son manifeste ; les totaux V1 a V8 relus dans le JSON ET dans le journal ; les chiffres de la note relus dans les journaux et le JSON (612 barreaux,
ecarts au pire, la seule morsure, les marges d'ancrage, le bruit de la dense, le tableau 5, les plateaux, le temoin) ; chaque canon de piece
nomme dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'lecteur_creux_m2/'
S = D + 'sortie/'
NOM = 'lot_machine2_2026-11-15_lecteur_creux_hors_chaine_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_lecteur_creux_hors_chaine_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_lecteur_creux_machine2_v1.md'
SELF = 'fabrique_lot_lecteur_creux_machine2_v1.py'
LOT_M1 = 'lot_machine1_2026-11-15_note_piste0_reprise_v1_recu.zip'
MAN_M1 = 'MANIFEST_lot_machine1_note_piste0_reprise_v1.txt'
PIECES = [D + x for x in ('lecteur_2D_creux_machine2_v1.py', 'validation_lecteur_creux_machine2_v1.py',
                          'comparaison_tableau5_machine2_v1.py', 'bruit_dense_par_barreau_machine2_v1.py',
                          'plateaux_et_temoin_machine2_v1.py', 'ancrage_marges_machine2_v1.py')] + \
         [S + x for x in ('validation_lecteur_creux_machine2_v1.log', 'validation_lecteur_creux_machine2_v1.json',
                          'comparaison_tableau5_machine2_v1.log', 'bruit_dense_par_barreau_machine2_v1.log',
                          'plateaux_et_temoin_machine2_v1.log', 'ancrage_marges_machine2_v1.log')] + [SELF]
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


for p in PIECES + [NOTE, LOT_M1, MAN_M1]:
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

# --- l'entrant : le lot de machine 1, recalcule
man_raw = open(os.path.join(ICI, MAN_M1), 'rb').read()
zl = zipfile.ZipFile(os.path.join(ICI, LOT_M1))
att = {}
for l in man_raw.decode('utf-8').split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
if emp(man_raw)[0] != '4103eae43f989877' or len(att) != 34 or sorted(att) != sorted(zl.namelist()):
    arrets.append('lot de machine 1 : canon %s, %d pieces, noms du zip %s' % (emp(man_raw)[0], len(att), 'identiques' if sorted(att) == sorted(zl.namelist()) else 'DIFFERENTS'))
if [n for n in att if emp(zl.read(n)) != att[n]]:
    arrets.append('lot de machine 1 : des pieces ne sont pas au canon')
if emp(zl.read('note_machine1_piste0_reprise_absorbeur_long_2026-11-15_v1.md'))[0] != '42c822811167b826':
    arrets.append('la note de machine 1 n est pas 42c822811167b826')
for c in ('4103eae43f989877', '42c822811167b826', '8d54bf9'):
    if c not in nn:
        arrets.append('la note ne nomme pas %s' % c)

# --- les totaux et les chiffres, relus dans le JSON et les journaux
vj = json.load(open(os.path.join(ICI, S + 'validation_lecteur_creux_machine2_v1.json'), encoding='ascii'))
vl = lit(S + 'validation_lecteur_creux_machine2_v1.log')
attendu = {'V1': (6, 6), 'V2': (34, 34), 'V3': (34, 34), 'V4': (34, 34), 'V5': (33, 34), 'V6': (34, 34), 'V7': (34, 34), 'V8': (30, 30)}
for v, (a, b) in attendu.items():
    if vj['totaux'][v] != [a, b] or ('TOTAL %s : %d sur %d' % (v, a, b)) not in vl:
        arrets.append('total %s : json %s, attendu %d sur %d' % (v, vj['totaux'][v], a, b))
if 'AU MOINS UNE EPREUVE MORD' not in vl:
    arrets.append('le journal de validation ne dit pas qu une epreuve mord')
pire = {'dE': 0.0, 'rel': 0.0, 'res': 0.0, 'EW': 0.0, 'marge': 0.0}
nb, mord = 0, []
for r in vj['resultats']:
    for cfg, c in r['configs'].items():
        m = c['cmp']
        if not m['V5']:
            mord.append((r['nom'], cfg, m['plateau_dense']['k0'], m['plateau_W']['k0'], m['plateau_dense']['etalement'], m['plateau_W']['etalement']))
        p = m['pire']
        pire['dE'] = max(pire['dE'], p['V3'])
        pire['rel'] = max(pire['rel'], p['V4rel'])
        pire['res'] = max(pire['res'], p['V7'])
        pire['EW'] = max(pire['EW'], p['EW'])
        pire['marge'] = max(pire['marge'], p['V4'])
        nb += sum(1 for l in m['lignes'] if 'gamma_W' in l)
if nb != 612:
    arrets.append('barreaux compares : %d, attendu 612' % nb)
if not (1.7e-12 < pire['dE'] < 1.85e-12 and 6.2e-3 < pire['rel'] < 6.35e-3 and 1.3e-14 < pire['res'] < 1.45e-14 and 6.6e-6 < pire['EW'] < 6.8e-6
        and 0.55 < pire['marge'] < 0.57):
    arrets.append('pires ecarts hors de ce que la note dit : %s' % pire)
if len(mord) != 1 or mord[0][:4] != ('j06_F1G30', 'F1G30', -4, -5) or not (0.0060 < mord[0][4] < 0.0061) or mord[0][5] > 2e-6:
    arrets.append('la morsure de V5 n est pas celle que la note decrit : %s' % (mord,))
for x in ('612 barreaux', '34 trajectoires', 'k0 = -4 (etalement 0.608 %)', 'k0 = -5 (0.000 %', '1.6e-6', '6.7e-4', '6.7e-6', '1.8e-12', '6.3e-3', '0.56', '1.4e-14',
          '30 sur 30', '5.340e-10', '5.373e-10'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
# marges d'ancrage : les six rapports de la note recalcules du JSON, puis lus dans le journal des marges
rap = {}
for r in vj['resultats']:
    if r['genre'] == 'pt':
        a = r['configs']['F1G20']['ancre']
        rap[r['nom']] = a['recouvrement_graine'] / a['recouvrement_second']
for nom, s in (('39_20', '1.093'), ('197_100', '1.013'), ('99_50', '1.003'), ('101_50', '1.031'), ('203_100', '1.019'), ('41_20', '1.004')):
    if '%.3f' % rap[nom] != s or s not in nn:
        arrets.append('marge d ancrage %s : %.3f, la note dit %s' % (nom, rap[nom], s))
ml = lit(S + 'ancrage_marges_machine2_v1.log')
for x in ('39_20      2     -2.09861   0.02636      7.3462e-12        0.034', '99_50      2     -4.03879   0.02742      1.8807e-09        22.274',
          '41_20      2     -2.90193   0.04288      1.2084e-10        0.045', '197_100    2     -4.05817   0.02760      2.9188e-09        22.494',
          '101_50     2     -3.96116   0.04238      1.4579e-09        22.213', '203_100    2     -3.94173   0.04264      1.9867e-09        22.064'):
    if x not in ml:
        arrets.append('journal des marges : ligne absente %r' % x)
for x in ('29 fois plus etroit', '22 fois plus etroit', '22.5', '22.3', '22.2', '22.1'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
# tableau 5, plateaux, temoin, bruit
cl = lit(S + 'comparaison_tableau5_machine2_v1.log')
if '18 sur 18 ; ecart max 0.0047 point de pourcentage ; comptes de plateau identiques : 3 sur 3' not in cl or 'OK' not in cl.split('\n')[0]:
    arrets.append('journal de la comparaison au tableau 5 : pas 18 sur 18')
pl = lit(S + 'plateaux_et_temoin_machine2_v1.log')
for x in ('verdict (PLATEAU ou non) identique : 34 sur 34 ; meme depart k0 de la fenetre retenue : 33 sur 34 ; Gamma_pl : 15 plateaux de part et d autre, ecart relatif max 6.69e-04',
          'mien 1.3e-03   dense 1.5e-03', 'mien 7.1e-04   dense 1.4e-03', 'mien 4.9e-04   dense 5.1e-04', 'mien 5.8e-05   dense 3.5e-05'):
    if x not in pl:
        arrets.append('journal des plateaux : %r absent' % x)
bl = lit(S + 'bruit_dense_par_barreau_machine2_v1.log')
for x in ('3.27e-12', '2.46e-14', 'ecart relatif median 4.23e-04', 'ecart relatif median 9.05e-05'):
    if x not in bl:
        arrets.append('journal du bruit : %r absent' % x)
for x in ('3.3e-12', '2.5e-14', '4.2e-4', '9.1e-5', '18 cellules sur 18', '1.3e-3, 7.1e-4, 4.9e-4, 5.8e-5', '1.5e-3, 1.4e-3, 5.1e-4, 3.5e-5'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
if 'Python 3.11.9, numpy 2.2.6' not in nn or 'scipy 1.15.3' not in nn or 'python 3.11.9' not in lit(S + 'validation_lecteur_creux_machine2_v1.log') or 'scipy 1.15.3' not in vl:
    arrets.append('versions : la note et le journal de validation ne disent pas la meme chose')
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- LECTEUR 2D CREUX DE MACHINE 2, HORS CHAINE, NON CERTIFIE, NON OPPOSABLE. Ecrit du gel bis et du moteur avant d ouvrir le code de machine 1 ; '
    'valide contre la sonde dense deposee aux seules configurations de la nuit bis (34 trajectoires, 612 barreaux, huit epreuves declarees d avance : une morsure, '
    'un depart de fenetre k0 du au bruit de la dense) ; 18 cellules sur 18 du tableau 5 de la note de machine 1 (42c822811167b826) ; l etat lu par M17 est '
    'departage du suivant par 0.3 a 9 pour cent de recouvrement, le suivant ayant une largeur 22 a 30 fois differente. Rien joue sous absorbeur long (E19). '
    'Rien a certifier ni a contresigner. machine 2\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 4103eae43f989877 (note 42c822811167b826) ; sonde dense deposee, lots a01598ec24237921 (sonde_etage2 c110c6286157b025, '
              'sonde_etage1 1ae4b5b2f9ff0e70) ; moteur 82a0be882568fe0c ; gel bis dcda1611adf5f8fd ; registre 8d54bf9\n')
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
