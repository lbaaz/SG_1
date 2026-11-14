# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat du run du gel la chaine E-A par etat, hors plage' -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_resultat_chaine_EA_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le pilote relu (heures, codes 0, 1480 s) ; le verdict, le selftest, les douze statuts et tous les
q cites par la note RELUS dans le journal de la feuille ; les annonces, le G-1 et les boites relus dans ma lecture ; la relecture independante
(meme verdict, 3 ecarts) ; la comparaison run / essai (ecart nul) ; la robustesse sous le bruit (131 etats, 12 statuts inchanges) ; le JSON de
la sonde (canons du moteur et de la sonde, 12 points) ; les canons de CHAQUE piece nommes dans la note ; note ASCII ; le manifeste ne se porte
pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'chaine_EA_par_etat/'
SO = D + 'sortie/'
NOM = 'lot_machine2_2026-11-14_resultat_chaine_EA_par_etat_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_chaine_EA_par_etat_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_chaine_EA_par_etat_machine2_v1.md'
SELF = 'fabrique_lot_resultat_chaine_EA_machine2_v1.py'
PIECES = [SO + x for x in ('console_chaine_par_etat.log', 'sonde_chaine_par_etat.json', 'sonde_chaine_par_etat.log', 'lecture_chaine_par_etat.log',
                           'verdict_chaine_par_etat.json', 'lecture_resultat_machine2.log', 'relecture_independante_machine2.log',
                           'compare_run_essai_ancres_machine2.log', 'stabilite_sous_bruit_machine2.log')] + \
         [D + x for x in ('lancer_chaine_par_etat_machine2_v1.py', 'lecture_resultat_chaine_par_etat_machine2_v1.py', 'relecture_independante_machine2_v1.py',
                          'stabilite_sous_bruit_machine2_v1.py')] + [SELF]
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

con = lit(SO + 'console_chaine_par_etat.log')
for x in ('DEBUT DU PILOTE', '10:12:51', '10:37:31', 'FIN DE LA SONDE code=0 duree=1480 s', 'FIN DE LA FEUILLE code=0', 'FIN DU PILOTE'):
    if x not in con:
        arrets.append('console : %r absent' % x)
if con.count('OK') != 4 or 'ECART' in con:
    arrets.append('console : les quatre canons ne sont pas tous OK')
for x in ('10:12:51', '10:37:31', '1480 s'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
fe = lit(SO + 'lecture_chaine_par_etat.log')
for x in ('SELFTEST : 26 cas, 26 tenus', 'VERDICT : TENU EN PARTIE'):
    if x not in fe:
        arrets.append('feuille : %r absent' % x)
STAT = {'J1': ('FACTEUR 2', 11), 'J2': ('HORS DECADE', 13), 'J3': ('FACTEUR 2', 11), 'J4': ('FACTEUR 2', 14), 'J5': ('DECADE', 8), 'J6': ('FACTEUR 2', 8),
        'T1': ('DECADE', 12), 'T2': ('FACTEUR 2', 12), 'T3': ('HORS DECADE', 11), 'T4': ('HORS DECADE', 8), 'A1': ('FACTEUR 2', 11), 'A2': ('FACTEUR 2', 12)}
for pid, (st, nj) in STAT.items():
    if not re.search(r'^  %s \w+\s+w2=\S+ x\S+ : %s\s+%d etats juges' % (pid, st, nj), fe, re.M):
        arrets.append('feuille : %s %s %d juges absent' % (pid, st, nj))
for q in ('0.621', '1.161', '0.897', '0.950', '2.945', '4.168', '3.735', '3.711', '0.756', '0.926', '0.842', '0.854', '1.269', '1.511', '1.418', '1.444',
          '0.395', '0.653', '0.545', '0.619', '1.292', '1.641', '1.503', '1.590', '0.498', '0.866', '1.153', '1.404', '1.334', '1.347', '0.064', '1.358',
          '0.979', '0.662', '12.327', '26.380', '18.348', '17.665', '0.587', '0.882', '1.629', '0.819', '0.758'):
    if q not in fe or q not in note:
        arrets.append('q %s absent du journal de la feuille ou de la note' % q)
lr = lit(SO + 'lecture_resultat_machine2.log')
for x in ('ecarts : 0', 'A-2 (0.55) J2 est HORS DECADE : VRAIE', 'A-3 (0.55) q du juge de plus grand recouvrement a J2 dans [2.3, 4.6] : q = 3.711 -> VRAIE',
          'A-4 (0.60) q du juge de plus grand recouvrement a J1 dans [0.70, 0.85] : q = 0.950 -> FAUSSE', 'A-5 (0.40) J3 et J4 tous deux FACTEUR 2 : J3 FACTEUR 2, J4 FACTEUR 2 -> VRAIE',
          'A-6 (0.75) signe du q median (sous 1 si w2 < 2, au-dessus si w2 > 2) : VRAIE', 'A-7 (0.65) J5 est lisible : VRAIE', 'A-8 (0.95) la garde G-4 tient : VRAIE'):
    if x not in lr:
        arrets.append('ma lecture : %r absent' % x)
if len(re.findall(r'-> IDENTIQUE', lr)) != 12:
    arrets.append('ma lecture : les douze boites ne sont pas toutes IDENTIQUES')
for pid, g in (('J2', 'HORS DOMAINE'), ('T3', 'HORS DOMAINE'), ('T4', 'HORS DOMAINE'), ('J1', 'EN DOMAINE'), ('J3', 'EN DOMAINE'), ('J4', 'EN DOMAINE'),
               ('J5', 'EN DOMAINE'), ('J6', 'EN DOMAINE'), ('T1', 'EN DOMAINE'), ('T2', 'EN DOMAINE'), ('A1', 'EN DOMAINE'), ('A2', 'EN DOMAINE')):
    if not re.search(r'^  %s w2=\S+ x\S+ : D1 \S+ c_max \S+ \(site \d+\) -> %s$' % (pid, g), lr, re.M):
        arrets.append('ma lecture : G-1 %s %s absent' % (pid, g))
for x in ('rang 10 (5,1) Gamma_2D(3) 2.3009e-12 exclu : chaine instable', 'rang 13 (4,2) Gamma_2D(3) 2.9921e-12 exclu : chaine instable',
          'rang  5 (9,2) Gamma_2D(3) -3.8858e-14 exclu : sous dix planchers'):
    if re.sub(r'\s+', ' ', x) not in re.sub(r'\s+', ' ', lr):
        arrets.append('ma lecture : %r absent' % x)
ri = lit(SO + 'relecture_independante_machine2.log')
if 'MEME' not in ri.splitlines()[0] or 'ECARTS : 3' not in ri or 'T3 : feuille HORS DECADE (11 juges) ; lecteur HD (13 juges) -> DIFFERENT' not in ri:
    arrets.append('relecture independante : meme verdict / 3 ecarts / T3 absents')
if ri.count('-> MEME') != 12:      # 1 ligne de verdict + 11 points sur 12 (T3 differe)
    arrets.append('relecture independante : %d lignes MEME (attendu 12 : verdict + 11 points)' % ri.count('-> MEME'))
cr = lit(SO + 'compare_run_essai_ancres_machine2.log')
if 'BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00 ; relatif max 0.00e+00' not in cr:
    arrets.append('comparaison run / essai : ecart nul absent')
sb = lit(SO + 'stabilite_sous_bruit_machine2.log')
if sb.count('-> INCHANGE') != 12 or 'POURRAIT' in sb or '131 etats juges ; bruit relatif maximal de la cible 2.38e-02' not in sb or 'Gamma_2D(3) = 3.078e-12' not in sb \
        or '(0.49766202641908697, 0.5)' not in sb.replace("'T1', 12, ", ''):
    arrets.append('stabilite sous le bruit : 12 INCHANGE, 131 etats, 2.38e-02, 3.078e-12 ou T1 0.4977 absents')
for x in ('131 etats', '2.4 pour cent', '3.078e-12', '0.4977'):
    if x not in nn:
        arrets.append('la note ne porte pas %r' % x)
S = json.load(open(os.path.join(ICI, SO + 'sonde_chaine_par_etat.json'), encoding='ascii'))
if S['moteur_canon'] != '82a0be882568fe0c' or S['sonde_canon'] != 'acf7e26dedfa8abc' or len(S['points']) != 12 or sorted(p['id'] for p in S['points']) != sorted(STAT):
    arrets.append('JSON de la sonde : canons ou points')
if any(len(p['etats']) != 14 for p in S['points']) or sum(len(p['etats']) for p in S['points']) != 168:
    arrets.append('JSON de la sonde : 168 etats attendus')
V = json.load(open(os.path.join(ICI, SO + 'verdict_chaine_par_etat.json'), encoding='ascii'))
if V['verdict'] != 'TENU EN PARTIE' or V['motifs'] != [] or V['points_juges'] != {k: STAT[k][0] for k in ('J1', 'J2', 'J3', 'J4', 'J5', 'J6')}:
    arrets.append('JSON du verdict : verdict, motifs ou statuts des points juges')
for canon in ('9df2702af59adbbc', 'acf7e26dedfa8abc', 'f94ab05f69e9bf2f', '82a0be882568fe0c', 'b3d3e23e98914a95', '3381564852ba6fe4'):
    if canon not in note:
        arrets.append('la note ne nomme pas le canon %s' % canon)
for p in PIECES:
    if p != SELF and emp(open(os.path.join(ICI, p), 'rb').read())[0] not in note:
        arrets.append('la note ne nomme pas le canon de %s' % p)
# le canon du lot de certification cite = celui de son manifeste
if emp(open(os.path.join(ICI, 'MANIFEST_lot_machine2_certification_gel_chaine_EA_par_etat_v1.txt'), 'rb').read())[0] != '3381564852ba6fe4':
    arrets.append('le canon du lot de certification n est plus 3381564852ba6fe4')
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- RESULTAT DU RUN DU GEL "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc ; sonde acf7e26dedfa8abc, feuille '
    'f94ab05f69e9bf2f, moteur 82a0be882568fe0c ; certification de machine 2 3381564852ba6fe4, faite avant). Un seul run, douze points, '
    '10:12:51 a 10:37:31. Verdict de la feuille de machine 1 : TENU EN PARTIE (J1 J3 J4 J6 FACTEUR 2, J5 DECADE, J2 HORS DECADE). '
    'Ancres au bit, G-4 tenue, statuts robustes au bruit des fils. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : gel 9df2702af59adbbc ; lot de machine 1 b3d3e23e98914a95 ; lot de certification de machine 2 3381564852ba6fe4 ; moteur v17 82a0be882568fe0c\n')
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
