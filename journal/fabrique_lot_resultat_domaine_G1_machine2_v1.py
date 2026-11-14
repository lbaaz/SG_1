# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat du run du gel la garde G-1 du moteur et la chaine E-A par etat' (b59651f99e60707a) -- manifeste + ZIP. 2026-11-14.
Usage : python -P fabrique_lot_resultat_domaine_G1_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; les chiffres cles de la note (heures, code, duree, verdict, a, b, rivale, ecarts de ma lecture et de mon lecteur
independant, ancres au bit, robustesse sous le bruit, annonces) RELUS dans le JSON du verdict et dans les journaux ; le JSON de la sonde porte 14 points
de 14 etats, la sonde 940a21b1d562bb49 et le moteur 82a0be882568fe0c ; les canons des pieces recalcules et ecrits dans la section des pieces de la note
(gabarit @@PIECES@@) ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
D = 'domaine_G1/'
SO = D + 'sortie/'
NOM = 'lot_machine2_2026-11-14_resultat_domaine_G1_chaine_EA_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_domaine_G1_chaine_EA_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md'
SELF = 'fabrique_lot_resultat_domaine_G1_machine2_v1.py'
PIECES = [SO + x for x in ('console_domaine_G1.log', 'sonde_domaine_G1.log', 'sonde_domaine_G1.json', 'lecture_domaine_G1.log', 'verdict_domaine_G1.json',
                           'lecture_resultat_machine2.log', 'relecture_independante_machine2.log', 'compare_run_essai_ancres_machine2.log',
                           'stabilite_sous_bruit_machine2.log', 'stabilite_cascade_machine2.log')] + [
    D + 'relecture_independante_domaine_G1_machine2_v1.py', D + 'stabilite_cascade_machine2_v1.py'] + [SELF]
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
# le JSON de la sonde et le verdict
S = json.load(open(os.path.join(ICI, SO + 'sonde_domaine_G1.json'), encoding='ascii'))
V = json.load(open(os.path.join(ICI, SO + 'verdict_domaine_G1.json'), encoding='ascii'))
if not (len(S['points']) == 14 and all(len(p['etats']) == 14 for p in S['points']) and S['sonde_canon'] == '940a21b1d562bb49' and S['moteur_canon'] == '82a0be882568fe0c'):
    arrets.append('JSON de la sonde : 14 points de 14 etats, sonde, moteur')
if not (V['verdict'] == 'LA GARDE NE TIENT PAS' and V['a_EN_tombes'] == 3 and V['b_HORS_tenus'] == 3 and V['rivale'] == 'NON TENUE' and V['motifs'] == []
        and V['paires'] == {'P1': 'HETEROGENE', 'P2': 'HOMOGENE', 'P3': 'HOMOGENE', 'P4': 'HOMOGENE', 'P5': 'HOMOGENE'}):
    arrets.append('verdict : %s a %s b %s rivale %s' % (V['verdict'], V['a_EN_tombes'], V['b_HORS_tenus'], V['rivale']))
cl = lit(SO + 'console_domaine_G1.log')
for x in ('18:59:46 LANCEMENT DE LA SONDE', '19:50:14 FIN DE LA SONDE code=0 duree=3028 s', 'FIN DE LA FEUILLE code=0'):
    if x not in cl:
        arrets.append('console : %r absent' % x)
ll = lit(SO + 'lecture_domaine_G1.log')
for x in ('SELFTEST : 74 cas, 74 tenus', 'VERDICT : LA GARDE NE TIENT PAS', 'RIVALE, le desaccord seul au-dessus de 2.00 (P1, P2, P3) : NON TENUE',
          'EN DOMAINE lisibles 6, dont tombes a = 3 ; HORS DOMAINE lisibles 6, dont tenus b = 3'):
    if x not in ll:
        arrets.append('lecture : %r absent' % x)
rl = lit(SO + 'lecture_resultat_machine2.log')
for x in ('BILAN DE MA LECTURE : 0 ecart(s)', 'A-6 (0.70) H1 est TENU : FAUSSE', 'A-8 (0.40) la rivale est TENUE : FAUSSE', 'A-9 (0.60) a E3 le q median est entre 3.0 et 4.5 : FAUSSE',
          'A-11 (0.50) H4 ou H5, l un au moins, est HORS DECADE : FAUSSE'):
    if x not in rl:
        arrets.append('ma lecture : %r absent' % x)
if len(re.findall(r': VRAIE', rl)) + len(re.findall(r'VRAIES?\b', rl)) < 8 or 'FAUSSE' not in rl:
    arrets.append('ma lecture : comptes des annonces')
ri = lit(SO + 'relecture_independante_machine2.log')
if 'ECARTS : 0' not in ri or 'NTP -> MEME' not in ri:
    arrets.append('relecture independante : ecarts')
cp = lit(SO + 'compare_run_essai_ancres_machine2.log')
if 'BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00 ; relatif max 0.00e+00' not in cp:
    arrets.append('ancres : bilan')
sb = lit(SO + 'stabilite_sous_bruit_machine2.log')
sc = lit(SO + 'stabilite_cascade_machine2.log')
if '154 etats juges' not in sb or '5.47e-02' not in sb or 'VERDICT INCHANGE ; RIVALE PEUT CHANGER' not in sc or "['HETEROGENE', 'HOMOGENE']" not in sc:
    arrets.append('robustesse sous le bruit')
for x in ('3028 s', 'LA GARDE NE TIENT PAS', 'a = 3', 'b = 3', 'NON TENUE', '0.21 pour cent', '5.24e-12', 'Neuf sur treize', 'SUR BATTERIE', 'd92a200ac348f0a3',
          '154 etats juges', '5.5 pour cent', '28 etats', '2516 MHz'):
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
    'MANIFESTE %s -- RESULTAT DU RUN DE MACHINE 2 DU GEL LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT (b59651f99e60707a ; sonde 940a21b1d562bb49 ; feuille '
    '0a760e3a244e547d ; certification d92a200ac348f0a3) : 14 points, 42 decompositions, un seul run ; verdict de la feuille LA GARDE NE TIENT PAS (a = 3, b = 3), '
    'rivale NON TENUE (a un etat pres de H1) ; ma lecture ecrite avant le run et mon lecteur independant : 0 ecart. machine 2, classe B\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : mon lot de certification d92a200ac348f0a3 ; le lot de machine 1 1aafb301d7d0ebb3\n')
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
