# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'certification du gel la chaine E-A par etat, hors plage' -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_certification_gel_chaine_EA_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les chiffres cles de la note (11 controles 0 morsure, banc 4000 / 0 ecart / repartition /
mutations, garde G-1 par point, ecarts des essais, ancres a zero, selftest) RELUS dans les journaux ; les canons des pieces
recalcules et ecrits dans la section 7 de la note (gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se porte pas lui-meme ;
ZIP relu bit-identique."""
import hashlib
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'chaine_EA_par_etat/'
NOM = 'lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_chaine_EA_par_etat_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md'
SELF = 'fabrique_lot_certification_gel_chaine_EA_machine2_v1.py'
PIECES = [D + x for x in (
    'controles_gel_machine2_v1.py', 'controles_gel_machine2_v1.log', 'reconstruction_gel_machine2.log', 'selftest_machine2.log',
    'banc_feuille_machine2_v1.py', 'banc_feuille_machine2_v1.log', 'boites_attendues_machine2_v1.py', 'boites_attendues_machine2_v1.log',
    'garde_G1_domaine_machine2_v1.py', 'garde_G1_domaine_machine2_v1.log', 'conception_points_chaine_seule_machine2.log',
    'essai_ancres_machine2.json', 'essai_ancres_machine2.log', 'lecture_essai_ancres_machine2.log', 'essai_ancres_machine2_4fils.json',
    'essai_ancres_machine2_4fils.log', 'compare_essais_machine2_v1.py', 'compare_essais_machine2_v1.log',
    'compare_16fils_4fils_machine2_v1.log', 'controle_ancres_machine2_v1.py', 'controle_ancres_machine2_v1.log',
    'lancer_chaine_par_etat_machine2_v1.py', 'lecture_resultat_chaine_par_etat_machine2_v1.py')] + [SELF]
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


def exige(piece, motifs, dans_note=()):
    t = lit(D + piece)
    for m in motifs:
        if m not in t:
            arrets.append('%s ne porte pas %r' % (piece, m))
    for m in dans_note:
        if m not in nn:
            arrets.append('la note ne porte pas %r' % m)


exige('controles_gel_machine2_v1.log', ['BILAN : 11 controles, 0 mordent : []'], ['11 controles de lecture, 0 morsure'])
exige('banc_feuille_machine2_v1.log',
      ['4000 sondes synthetiques', "'NCI': 2522", "'NL': 619", "'PARTIE': 271", "'TENU': 588", 'ecarts feuille / lecteur : 0',
       'survivent au selftest de machine 1 : [1, 3, 4, 9, 11, 15, 21, 23, 24] ; survivent a mon banc : [11] ; survivent aux deux : [11]',
       'q = sqrt(10) = 3.1622776601683795 ; feuille : HORS DECADE'],
      ['NON CONCLUANT 2522', 'NON LISIBLE 619', 'TENU EN PARTIE 271', 'ORDRE DE GRANDEUR TENU 588', 'mon banc en mord 23',
       'ton selftest en mord 15 sur 24', '3.1622776601683795'])
g1 = lit(D + 'garde_G1_domaine_machine2_v1.log')
for motif in (r'J2 .* c_max=0\.1042 site 4 .* HORS DOMAINE', r'T3 .* D1=0\.2143 .* c_max=0\.1550 .* HORS DOMAINE',
              r'T4 .* c_max=0\.1610 .* HORS DOMAINE', r'J1 .* c_max=0\.0912 .* EN DOMAINE'):
    if not re.search(motif, g1):
        arrets.append('garde G-1 : %s absent du journal' % motif)
for pid in ('J3', 'J4', 'J5', 'J6', 'T1', 'T2', 'A1', 'A2'):
    if not re.search(r'^%s .*EN DOMAINE' % pid, g1, re.M):
        arrets.append('garde G-1 : %s n est pas EN DOMAINE dans le journal' % pid)
if len(re.findall(r'^M17-\S+ .*EN DOMAINE', g1, re.M)) != 6:
    arrets.append('garde G-1 : les six points de M17 ne sont pas tous EN DOMAINE')
for x in ('D2a 0.1042', 'D1 0.2143', 'D2a 0.155', 'D2a 0.161', 'D2a 0.0912'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
exige('compare_essais_machine2_v1.log',
      ['28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 6.72e-14 ; relatif max 9.18e-01 ; '
       'relatif max au-dessus de 1e-10 2.99e-04'], ['6.7e-14', '3.0e-04'])
exige('compare_16fils_4fils_machine2_v1.log',
      ['14 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 7.32e-14 ; relatif max 2.21e-01 ; '
       'relatif max au-dessus de 1e-10 3.20e-04 ; chaine : ecart relatif max 0.00e+00'], ['7.3e-14', '3.2e-04'])
ca = lit(D + 'controle_ancres_machine2_v1.log')
if len(re.findall(r'ecart relatif 0\.000e\+00', ca)) != 2 or '2.239e-04' not in ca or '1.606e-07' not in ca or 'stabilite de la cible max (etats au-dessus de dix planchers) 1.135' not in ca:
    arrets.append('controle des ancres : zero, zero, 2.239e-04, 1.606e-07 ou 1.135 absent')
for x in ('2.2e-04', '1.6e-07', '1.135', '+0.0448', '+0.0671', '0.935', '0.901', '2.002'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
if '26 cas, 26 tenus' not in lit(D + 'selftest_machine2.log'):
    arrets.append('selftest : 26 / 26 absent')
if 'GEL RECONSTRUIT == GEL DU LOT, OCTET POUR OCTET' not in lit(D + 'reconstruction_gel_machine2.log'):
    arrets.append('reconstruction du gel : identite absente')
la = lit(D + 'essai_ancres_machine2.log')
if 'A1 ancre' not in la or '102.6 s' not in la or '134.4 s' not in la or 'code=0' not in la or '103 s' not in nn or '134 s' not in nn:
    arrets.append('durees des essais : 102.6 s et 134.4 s absentes du journal ou de la note')
cm = lit(D + 'conception_points_chaine_seule_machine2.log')
for x in ('Gamma_chaine=1.61e-13', 'Gamma_chaine=2.92e-12', 'Gamma_chaine=4.95e-13'):
    if x not in cm:
        arrets.append('conception rejouee : %s absent' % x)
if 'GARDE' in note and False:
    pass
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
for canon in ('b3d3e23e98914a95', '9df2702af59adbbc', '82a0be882568fe0c'):
    if canon not in note:
        arrets.append('la note ne nomme pas le canon %s' % canon)
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- CERTIFICATION PAR MACHINE 2 DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc, lot de machine 1 '
    'b3d3e23e98914a95 ; moteur 82a0be882568fe0c). 11 controles de lecture, 0 morsure ; feuille independante : 4000 sondes, 0 ecart ; '
    'ancres rejouees au bit ; quatre reserves (R-1 : la garde G-1 du moteur dit HORS DOMAINE a J2, T3, T4 et la sonde ne la consulte pas). '
    'Faite AVANT le run. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 b3d3e23e98914a95 (13 pieces) ; moteur v17 82a0be882568fe0c ; mon dossier du run manche_m17_v17\n')
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
