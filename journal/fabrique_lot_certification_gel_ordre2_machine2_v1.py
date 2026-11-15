# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel la chaine E-A au second ordre' (41153158190cf7f1) -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_certification_gel_ordre2_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les chiffres cles de la note (22 controles 0 morsure, bloc recalcule a part 17 controles 0 morsure, banc 4000 sondes / 0 ecart /
repartition / mutations et survivants, garde et boites aux 16 points, essais aux ancres, selftest) RELUS dans les journaux ; les canons des pieces recalcules et ecrits dans la
section des pieces de la note (gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'ordre2/'
NOM = 'lot_machine2_2026-11-14_certification_gel_ordre2_chaine_EA_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_ordre2_chaine_EA_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_ordre2_machine2_v1.py'
PIECES = [D + x for x in (
    'controles_gel_ordre2_machine2_v1.py', 'controles_gel_ordre2_machine2_v1.log', 'controles_gel_ordre2_machine2_v1.json',
    'bloc_independant_machine2_v1.py', 'bloc_independant_machine2_v1.log',
    'garde_et_boites_machine2_v1.py', 'garde_et_boites_machine2_v1.log', 'garde_et_boites_machine2_1fil.log',
    'banc_feuille_ordre2_machine2_v1.py', 'banc_feuille_ordre2_machine2_v1.log', 'banc_feuille_ordre2_machine2_v1_premier_jet.log',
    'essai_ancres_machine2.json', 'essai_ancres_machine2.log', 'lecture_essai_ancres_machine2.log',
    'essai_ancres_machine2_1fil.json', 'essai_ancres_machine2_1fil.log', 'lecture_essai_ancres_machine2_1fil.log',
    'compare_essais_16fils_machine1.log', 'compare_essais_1fil_machine1.log', 'compare_essais_16fils_1fil_machine2.log',
    'selftest_machine2.log', 'lancer_ordre2_machine2_v1.py', 'lecture_resultat_ordre2_machine2_v1.py',
    'relecture_independante_ordre2_machine2_v1.py', 'stabilite_cascade_machine2_v1.py')] + [SELF]
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


for p in PIECES + [NOTE]:
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
if '@@' in note:
    arrets.append('la note porte un gabarit non pose')
nn = re.sub(r'\s+', ' ', note)
# chiffres cles RELUS dans les journaux
cj = json.load(open(os.path.join(ICI, D + 'controles_gel_ordre2_machine2_v1.json'), encoding='ascii'))
if cj['bilan']['controles'] != 22 or cj['bilan']['mord'] != 0:
    arrets.append('controles : %s' % cj['bilan'])
jb = lit(D + 'bloc_independant_machine2_v1.log')
if 'BILAN : 17 controles, 0 mordent []' not in jb:
    arrets.append('bloc recalcule a part : bilan')
for x in ('t 0.00e+00 ; Sigma2 5.22e-13 ; u 4.60e-13', 'Gamma_flux 6.97e-09', 'ecart relatif maximal 4.52e-15', '122 etats', 'q2 (-2 Im E) de 0.998 a 1.512',
          '88 etats, plus grand q2 1.101', '118 etats, plus grand q2 1.512', '37 etats, plus grand q2 1.474', 'mediane 0.0011, pire 0.0050', 'de 0.375 a 6.987',
          "dans un facteur 1.5 a l'ordre 2 : 242 sur 243", 'ecart 8.28e-12'):
    if x not in jb:
        arrets.append('journal du bloc : %r absent' % x)
for x in ('5.2e-13', '4.6e-13', '7e-9', '8e-12', '4.5e-15', '1.2e-14', '5.2e-15', '7.5e-5 a 4.6e-6', '4.5e-4 a 2.7e-5', '0.998 ; 1.512', '1.101, 1.512 et 1.474', '6.987', '242', '1.4948'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
bl = lit(D + 'banc_feuille_ordre2_machine2_v1.log')
m = re.search(r'(\d+) sondes synthetiques aux bords des seuils ; verdicts du lecteur independant : (\{.*?\})\n\s+ecarts feuille / lecteur : (\d+)', bl)
if not m or m.group(3) != '0' or m.group(1) != '4000':
    arrets.append('banc, partie A : %s' % (m.groups() if m else None))
else:
    rep = dict((k, int(v)) for k, v in re.findall(r"'(\w+)': (\d+)", m.group(2)))
    if sorted(rep) != ['J06', 'J10', 'NCI', 'NL', 'NTP', 'TIENT']:
        arrets.append('banc : les six issues ne sont pas toutes representees : %s' % rep)
    for k, nom in (('NCI', "NON CONCLUANT D'INSTRUMENT"), ('NL', 'NON LISIBLE'), ('NTP', 'NE TIENT PAS'), ('J06', "TIENT JUSQU'A 0.06"), ('J10', "TIENT JUSQU'A 0.10"), ('TIENT', 'TIENT')):
        if '%s %d' % (nom, rep.get(k, -1)) not in nn:
            arrets.append('la note ne porte pas la repartition %s %s' % (nom, rep.get(k)))
mb = re.search(r'BILAN : (\d+) alterations ; motifs absents \[(.*?)\] ; survivent au selftest de machine 1 : \[(.*?)\] ; survivent a mon banc : \[(.*?)\] ; survivent aux deux : \[(.*?)\]', bl)
if not mb or mb.group(2) != '':
    arrets.append('banc, partie B : %s' % (mb.groups() if mb else None))
else:
    n_mut, s1, s2, s12 = mb.group(1), mb.group(3), mb.group(4), mb.group(5)
    for x in ('%s alterations' % n_mut, 'survivent au selftest de machine 1 : [%s]' % s1, 'survivent a mon banc : [%s]' % s2, 'survivent aux deux : [%s]' % s12):
        if x not in nn:
            arrets.append('la note ne porte pas %r' % x)
    if len(s1.split(',')) != 22 or len(s2.split(',')) != 3 or len(s12.split(',')) != 2:
        arrets.append('les comptes de survivants de la note (22, 3, 2) ne sont pas ceux du journal')
if not re.search(r'tableau de la feuille == tableau du gel, aux 16 points \(role, w2, facteur, bande, garde, D1, c_max\) : True ; ecarts \[\]', bl):
    arrets.append('banc : tableau de la feuille != gel')
bp = re.sub(r'\s+', ' ', lit(D + 'banc_feuille_ordre2_machine2_v1_premier_jet.log'))
if 'survivent a mon banc : [45, 56, 69, 109, 114]' not in bp:
    arrets.append('premier jet du banc : les cinq survivants annonces (45, 56, 69, 109, 114) ne sont pas ceux du journal')
gl = lit(D + 'garde_et_boites_machine2_v1.log')
if 'BILAN : 0 ecart(s) a la table des seize points' not in gl:
    arrets.append('garde et boites : bilan')
g16, g1 = lit(D + 'garde_et_boites_machine2_v1.log'), lit(D + 'garde_et_boites_machine2_1fil.log')
f = lambda t: t[t.index('TOUS CHIFFRES'):t.index('GROUPES')]
if f(g16) != f(g1) or len([l for l in f(g16).split('\n') if l.strip()]) != 17:
    arrets.append('garde a 16 fils et a 1 fil : differente ou incomplete')
if 'SELFTEST : 160 cas, 160 tenus' not in lit(D + 'selftest_machine2.log'):
    arrets.append('selftest')
for nom, attendu in (('compare_essais_16fils_machine1.log', 'ecart absolu max de Gamma_2D (k = 2, 3, 4) 6.72e-14'), ('compare_essais_1fil_machine1.log', 'ecart absolu max de Gamma_2D (k = 2, 3, 4) 1.72e-13'),
                     ('compare_essais_16fils_1fil_machine2.log', 'ecart absolu max de Gamma_2D (k = 2, 3, 4) 1.19e-13')):
    cl = lit(D + nom)
    if 'BILAN : 28 etats, 0 etiquettes differentes' not in cl or attendu not in cl:
        arrets.append('compare des essais %s : bilan' % nom)
for x in ('22', '17 controles', '4000', '531441', '115 alterations', '122 etats', '160 cas', '29 couples', '3bc363266957de56', '41153158190cf7f1', '24315c52b234319c', '0dc8241c680eb1ff',
          '7cd5977bc27bebc1', '940a21b1d562bb49', '0a760e3a244e547d', '79e77d2', '737 champs', '7.7e-14'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
# canons des lots et pieces de machine 1
zl = zipfile.ZipFile(os.path.join(ICI, 'lot_machine1_2026-11-14_gel_ordre2_chaine_EA_v1_recu.zip'))
man_m1 = open(os.path.join(ICI, 'MANIFEST_lot_machine1_gel_ordre2_chaine_EA_v1.txt'), 'rb').read()
for nom, (got, att) in {'lot de machine 1': (emp(man_m1)[0], '3bc363266957de56'),
                        'gel': (emp(zl.read('gel_ordre2_chaine_EA_pre_enregistrement_v1.md'))[0], '41153158190cf7f1'),
                        'sonde': (emp(zl.read('sonde_ordre2_machine1_v1.py'))[0], '24315c52b234319c'),
                        'feuille': (emp(zl.read('lecture_ordre2_machine1_v1.py'))[0], '0dc8241c680eb1ff'),
                        'bloc': (emp(zl.read('chaine_ordre2_bloc_machine1_v1.py'))[0], '7cd5977bc27bebc1')}.items():
    if got != att:
        arrets.append('canon %s : %s, annonce %s' % (nom, got, att))
    if att not in note:
        arrets.append('la note ne nomme pas le canon %s : %s' % (nom, att))
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION DE MACHINE 2 DU GEL LA CHAINE E-A AU SECOND ORDRE (41153158190cf7f1, lot de machine 1 '
    '3bc363266957de56), DE SA SONDE (24315c52b234319c), DE SA FEUILLE (0dc8241c680eb1ff) ET DE SON BLOC (7cd5977bc27bebc1) : 22 controles, 0 morsure ; bloc recalcule a part '
    '17 controles, 0 morsure ; banc independant 4000 sondes, 0 ecart ; garde et boites aux 16 points == la table du gel ; CERTIFIE, des reserves. Faite AVANT le run. '
    'machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 3bc363266957de56 ; mes lots d92a200ac348f0a3, 86a677dc0ff8ba9d et 86e73729505a610e\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % (len(PIECES) + 1))
with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for p in [NOTE] + PIECES:
        z.write(os.path.join(ICI, p), p)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for p in [NOTE] + PIECES:
        attendu[p] = open(os.path.join(ICI, p), 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
