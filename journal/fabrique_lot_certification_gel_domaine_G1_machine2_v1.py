# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel la garde G-1 du moteur et la chaine E-A par etat' (b59651f99e60707a) -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_certification_gel_domaine_G1_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les chiffres cles de la note (11 controles 0 morsure, banc 4000 sondes / 0 ecart / repartition / mutations et
survivants, garde et boites aux 14 points, essai aux ancres, selftest) RELUS dans les journaux ; les canons des pieces recalcules et ecrits dans la
section des pieces de la note (gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'domaine_G1/'
NOM = 'lot_machine2_2026-11-14_certification_gel_domaine_G1_chaine_EA_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_domaine_G1_chaine_EA_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_domaine_G1_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_domaine_G1_machine2_v1.py'
PIECES = [D + x for x in (
    'controles_gel_domaine_G1_machine2_v1.py', 'controles_gel_domaine_G1_machine2_v1.log', 'controles_gel_domaine_G1_machine2_v1.json',
    'selftest_machine2.log', 'banc_feuille_domaine_G1_machine2_v1.py', 'banc_feuille_domaine_G1_machine2_v1.log',
    'banc_feuille_domaine_G1_machine2_v1_premier_jet.log', 'garde_et_boites_machine2_v1.py', 'garde_et_boites_machine2_v1.log',
    'essai_ancres_machine2.json', 'essai_ancres_machine2.log', 'lecture_essai_ancres_machine2.log', 'compare_essais_machine2_v1.log',
    'garde_fils_machine2_v1.py', 'garde_fils_16_machine2_v1.log', 'garde_fils_1_machine2_v1.log',
    'lancer_domaine_G1_machine2_v1.py', 'lecture_resultat_domaine_G1_machine2_v1.py')] + [SELF]
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
nn = re.sub(r'\s+', ' ', note)
# chiffres cles RELUS dans les journaux
cj = json.load(open(os.path.join(ICI, D + 'controles_gel_domaine_G1_machine2_v1.json'), encoding='ascii'))
if cj['bilan']['controles'] != 11 or cj['bilan']['mord'] != 0:
    arrets.append('controles : %s' % cj['bilan'])
bl = lit(D + 'banc_feuille_domaine_G1_machine2_v1.log')
m = re.search(r'(\d+) sondes synthetiques aux bords des seuils ; verdicts du lecteur independant : (\{.*?\}) ; rivale : (\{.*?\})\n\s+ecarts feuille / lecteur : (\d+)', bl)
if not m or m.group(4) != '0' or m.group(1) != '4000':
    arrets.append('banc, partie A : %s' % (m.groups() if m else None))
mb = re.search(r'BILAN : (\d+) alterations ; motifs absents \[(.*?)\] ; survivent au selftest de machine 1 : \[(.*?)\] ; survivent a mon banc : \[(.*?)\] ; survivent aux deux : \[(.*?)\]', bl)
if not mb or mb.group(2) != '':
    arrets.append('banc, partie B : %s' % (mb.groups() if mb else None))
else:
    n_mut, s1, s2, s12 = mb.group(1), mb.group(3), mb.group(4), mb.group(5)
    for x in ('%s alterations' % n_mut, 'survivent au selftest de machine 1 : [%s]' % s1, 'survivent a mon banc : [%s]' % s2, 'survivent aux deux : [%s]' % s12):
        if x not in nn:
            arrets.append('la note ne porte pas %r' % x)
if not re.search(r'tableau de la feuille == tableau du gel, aux 14 points : True ; ecarts \[\] ; paires de la feuille == paires du gel : True', bl):
    arrets.append('banc : tableau de la feuille != gel')
gl = lit(D + 'garde_et_boites_machine2_v1.log')
if 'BILAN : 0 ecart(s) a la table des quatorze points ; phrases de (i) : tiennent' not in gl:
    arrets.append('garde et boites : bilan')
if 'SELFTEST : 74 cas, 74 tenus' not in lit(D + 'selftest_machine2.log'):
    arrets.append('selftest')
g16, g1 = lit(D + 'garde_fils_16_machine2_v1.log').split('\n')[1:], lit(D + 'garde_fils_1_machine2_v1.log').split('\n')[1:]
if g16 != g1 or len([l for l in g16 if l.strip()]) != 14:
    arrets.append('garde a 16 fils et a 1 fil : differente ou incomplete')
cl = lit(D + 'compare_essais_machine2_v1.log')
if 'BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00 ; relatif max 0.00e+00' not in cl:
    arrets.append('compare des essais : bilan')
for x in ('11 controles', '0 morsure', '4000 sondes', '531441', '156 points', '28 etats', '74 cas', 'b59651f99e60707a', '1aafb301d7d0ebb3'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
# canons des lots et pieces de machine 1
zl = zipfile.ZipFile(os.path.join(ICI, 'lot_machine1_2026-11-14_gel_domaine_G1_chaine_EA_v1_recu.zip'))
man_m1 = open(os.path.join(ICI, 'MANIFEST_lot_machine1_gel_domaine_G1_chaine_EA_v1.txt'), 'rb').read()
for nom, (got, att) in {'lot de machine 1': (emp(man_m1)[0], '1aafb301d7d0ebb3'),
                        'gel': (emp(zl.read('gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md'))[0], 'b59651f99e60707a'),
                        'sonde': (emp(zl.read('sonde_domaine_G1_machine1_v1.py'))[0], '940a21b1d562bb49'),
                        'feuille': (emp(zl.read('lecture_domaine_G1_machine1_v1.py'))[0], '0a760e3a244e547d')}.items():
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
    'MANIFESTE %s -- CERTIFICATION DE MACHINE 2 DU GEL LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT (b59651f99e60707a, lot de machine 1 '
    '1aafb301d7d0ebb3), DE SA SONDE (940a21b1d562bb49) ET DE SA FEUILLE (0a760e3a244e547d) : 11 controles, 0 morsure ; banc independant 4000 sondes, 0 ecart ; '
    'garde et boites aux 14 points == la table du gel ; CERTIFIE, des reserves. Faite AVANT le run. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 1aafb301d7d0ebb3 ; mes lots 3381564852ba6fe4, 9143062c481ad267, 3ae869c8c037dc21\n')
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
