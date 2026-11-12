# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat de l'etage 1 de la nuit E-B' -- manifeste + ZIP. 2026-11-12.
Usage : python -P fabrique_lot_resultat_etage1_nuit_EB_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le verdict et ses motifs LUS dans verdict_etage1.json (jamais tapes) et
nommes dans la note ; le code de sortie 0 lu dans la console ; les canons de CHAQUE piece RECALCULES et nommes dans
la note ; les canons de la sonde et de la feuille relus dans les journaux ; pas d'etage 2 (aucun sonde_etage2.json) ;
le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NUIT = os.path.join(ICI, 'nuit_EB')
SORTIE = os.path.join(NUIT, 'sortie')
NOM = 'lot_machine2_2026-11-12_resultat_etage1_nuit_EB_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_etage1_nuit_EB_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1.md'
SELF = 'fabrique_lot_resultat_etage1_nuit_EB_machine2_v1.py'
DOSSIER = 'nuit_EB_etage1/'
# (chemin source, nom dans le lot)
DONNEES = [(os.path.join(SORTIE, 'sonde_etage1.json'), DOSSIER + 'sonde_etage1.json'),
           (os.path.join(SORTIE, 'sonde_etage1.log'), DOSSIER + 'sonde_etage1.log'),
           (os.path.join(NUIT, 'console_etage1.log'), DOSSIER + 'console_etage1.log'),
           (os.path.join(SORTIE, 'verdict_etage1.json'), DOSSIER + 'verdict_etage1.json'),
           (os.path.join(SORTIE, 'lecture_etage1.log'), DOSSIER + 'lecture_etage1.log')]
PIECES = [(os.path.join(ICI, NOTE), NOTE), (os.path.join(ICI, SELF), SELF)] + DONNEES
arrets = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


for src, _ in PIECES:
    if not os.path.isfile(src):
        arrets.append('piece absente : %s' % src)
if os.path.exists(os.path.join(SORTIE, 'sonde_etage2.json')):
    arrets.append('un sonde_etage2.json existe : la note annonce que l etage 2 n a PAS ete lance')
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = open(os.path.join(ICI, NOTE), encoding='utf-8').read()
verdict = json.load(open(os.path.join(SORTIE, 'verdict_etage1.json'), encoding='ascii'))
if verdict.get('etage1') != 'NE TIENT PAS' or verdict.get('prevol'):
    arrets.append('le verdict lu n est pas "NE TIENT PAS" hors pre-vol : %r' % verdict.get('etage1'))
if ('VERDICT DE L\'ETAGE 1 : %s' % verdict['etage1']) not in note and ('**VERDICT DE L\'ETAGE 1 : %s**' % verdict['etage1']) not in note:
    arrets.append('la note ne nomme pas le verdict lu')
for m in verdict['motifs']:
    if m.replace('TP ne tient pas a ', "'TP ne tient pas a ") not in note:
        arrets.append('la note ne nomme pas le motif %r' % m)
console = open(os.path.join(NUIT, 'console_etage1.log'), encoding='ascii', errors='replace').read()
if 'CODE DE SORTIE ETAGE 1 = 0' not in console:
    arrets.append('la console ne porte pas le code de sortie 0')
lect = open(os.path.join(SORTIE, 'lecture_etage1.log'), encoding='ascii', errors='replace').read()
for canon in ('facc7536ba4637cb', 'b3ac958a1a2b915b'):
    if canon not in console + lect:
        arrets.append('canon %s absent des journaux' % canon)
    if canon not in note:
        arrets.append('la note ne nomme pas le canon %s' % canon)
if 'VERDICT DE L\'ETAGE 1 : NE TIENT PAS' not in lect:
    arrets.append('le journal de la feuille ne porte pas le verdict')

CANONS = {}
for src, nom in PIECES:
    if nom == NOTE:
        continue
    c = emp(open(src, 'rb').read())[0]
    CANONS[nom] = c
    if nom != SELF and c not in note:
        arrets.append('la note ne nomme pas le canon %s de %s' % (c, nom))
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

lignes = [
    'MANIFESTE %s -- RESULTAT DE L\'ETAGE 1 DE LA NUIT E-B (gel cde0cd11a763f26d, sonde v2 facc7536ba4637cb, '
    'feuille b3ac958a1a2b915b, reference TP 4d51dd58ef456fe9 / liste 69b3bab3bb8480b7). VERDICT lu : %s (%s). '
    'ETAGE 2 NON LANCE. Plateforme : Windows AMD64, python 3.11.9, numpy 2.2.6. machine 2, classe B\n'
    % (NOM, verdict['etage1'], '; '.join(verdict['motifs'])),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for src, nom in PIECES:
    b, br, ob, obr = emp(open(src, 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, nom))
lignes.append('\nnon joint : nuit_EB/sortie/reprise/ (279 fichiers de reprise, dont les vecteurs propres .npy) : '
              'contenu utile consolide dans sonde_etage1.json\n')
lignes.append('pieces : %d (compte etabli APRES le dernier ajout)\n' % len(PIECES))

with open(MAN, 'w', encoding='utf-8', newline='\n') as fh:
    fh.writelines(lignes)
with zipfile.ZipFile(ZIP, 'w', zipfile.ZIP_DEFLATED) as z:
    z.write(MAN, os.path.basename(MAN))
    for src, nom in PIECES:
        z.write(src, nom)
with zipfile.ZipFile(ZIP) as z:
    attendu = {os.path.basename(MAN): open(MAN, 'rb').read()}
    for src, nom in PIECES:
        attendu[nom] = open(src, 'rb').read()
    mauvais = [n for n in z.namelist() if z.read(n) != attendu.get(n)]
    manque = sorted(set(attendu) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)

print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES), os.path.getsize(ZIP)))
