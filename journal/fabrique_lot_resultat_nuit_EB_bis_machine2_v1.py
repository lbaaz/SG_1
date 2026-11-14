# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat de la nuit E-B bis' -- manifeste + ZIP. 2026-11-13.
Usage : python -P fabrique_lot_resultat_nuit_EB_bis_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; le verdict, les statuts des six points, les etalements du tableau, les 18
Gamma de reference du rejeu et les durees LUS dans les JSON et le journal du pilote (jamais tapes) et retrouves dans la
note ; le journal du pilote porte VERDICT DE LA QUALIFICATION, FIN DE LA NUIT et AUCUN ARRET ; G-Q10 vrai aux deux
etages, G-Q4 au bit aux six points ; les canons de CHAQUE piece RECALCULES et nommes dans la note ; sonde, feuille, moteur
et gel relus dans les journaux ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
NUIT = os.path.join(ICI, 'nuit_EB_bis')
SORTIE = os.path.join(NUIT, 'sortie')
NOM = 'lot_machine2_2026-11-13_resultat_nuit_EB_bis_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_nuit_EB_bis_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_nuit_EB_bis_machine2_v1.md'
SELF = 'fabrique_lot_resultat_nuit_EB_bis_machine2_v1.py'
D = 'nuit_EB_bis/'
DONNEES = [(SORTIE, 'sonde_etage1.json'), (SORTIE, 'sonde_etage1.log'), (SORTIE, 'verdict_etage1.json'),
           (SORTIE, 'lecture_etage1.log'), (SORTIE, 'sonde_etage2.json'), (SORTIE, 'sonde_etage2.log'),
           (SORTIE, 'verdict_qualification_EB.json'), (SORTIE, 'lecture_etage2.log')]
PIECES = ([(os.path.join(ICI, NOTE), NOTE)]
          + [(os.path.join(r, f), D + ('sortie/' if r == SORTIE else '') + f) for r, f in DONNEES]
          + [(os.path.join(NUIT, 'console_nuit.log'), D + 'console_nuit.log'),
             (os.path.join(NUIT, 'lancer_nuit_EB_bis_machine2_v1.py'), D + 'lancer_nuit_EB_bis_machine2_v1.py'),
             (os.path.join(NUIT, 'lecture_resultat_machine2_v1.log'), D + 'lecture_resultat_machine2_v1.log'),
             (os.path.join(ICI, 'lecture_resultat_nuit_EB_bis_machine2_v1.py'), 'lecture_resultat_nuit_EB_bis_machine2_v1.py'),
             (os.path.join(ICI, SELF), SELF)])
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
if arrets:
    print('ARRET AVANT ECRITURE :')
    for a in arrets:
        print('  -', a)
    raise SystemExit(1)

note = open(os.path.join(ICI, NOTE), encoding='utf-8').read()
nn = re.sub(r'\s+', ' ', note)
if any(ord(c) > 127 for c in note):
    arrets.append('la note n est pas ASCII')


def lire(nom):
    return json.load(open(os.path.join(SORTIE, nom), encoding='ascii'))


v1, vq, s1, s2 = lire('verdict_etage1.json'), lire('verdict_qualification_EB.json'), lire('sonde_etage1.json'), lire('sonde_etage2.json')
journal = open(os.path.join(NUIT, 'console_nuit.log'), encoding='ascii').read()
l1 = open(os.path.join(SORTIE, 'lecture_etage1.log'), encoding='ascii', errors='replace').read()
l2 = open(os.path.join(SORTIE, 'lecture_etage2.log'), encoding='ascii', errors='replace').read()
c1 = open(os.path.join(SORTIE, 'sonde_etage1.log'), encoding='ascii', errors='replace').read()
c2 = open(os.path.join(SORTIE, 'sonde_etage2.log'), encoding='ascii', errors='replace').read()

# verdicts
if v1.get('etage1') != 'TIENT' or v1.get('prevol') or v1.get('motifs'):
    arrets.append('le verdict de l etage 1 lu n est pas TIENT sans motif : %r' % v1)
if vq.get('verdict') != 'NON QUALIFIE' or vq.get('prevol'):
    arrets.append('le verdict lu n est pas NON QUALIFIE hors pre-vol : %r' % vq.get('verdict'))
if '**VERDICT : %s**' % vq['verdict'] not in note:
    arrets.append('la note ne nomme pas le verdict lu')
ORDRE = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
for n in ORDRE:
    if vq['detail']['points'][n]['statut'] != 'NON QUALIFIE':
        arrets.append('le point %s n est pas NON QUALIFIE' % n)
    if vq['detail']['points'][n]['non_lisibles']:
        arrets.append('le point %s porte des non lisibles' % n)
if 'VERDICT : NON QUALIFIE' not in l2 or "VERDICT DE L'ETAGE 1 : TIENT" not in l1:
    arrets.append('les journaux de la feuille ne portent pas les verdicts')
for marque in ('VERDICT ETAGE 1 : TIENT', 'VERDICT DE LA QUALIFICATION : NON QUALIFIE', 'FIN DE LA NUIT'):
    if marque not in journal:
        arrets.append('le journal du pilote ne porte pas %r' % marque)
if 'ARRET' in journal:
    arrets.append('le journal du pilote porte un ARRET')
d1 = int(re.search(r'FIN etage1 code=0 duree=(\d+) s', journal).group(1))
d2 = int(re.search(r'FIN etage2 code=0 duree=(\d+) s', journal).group(1))
for d in (d1, d2):
    if ('duree=%d s' % d) not in note:
        arrets.append('la note ne nomme pas la duree %d s' % d)
# garde-fous
if s1.get('GQ10') is not True or s2.get('GQ10') is not True:
    arrets.append('G-Q10 n est pas vrai aux deux etages')
if not all(v['au_bit'] for v in s2['GQ4'].values()) or len(s2['GQ4']) != 6:
    arrets.append('G-Q4 n est pas au bit aux six points')
if s2['gel'] != 'dcda1611adf5f8fd' or s1['gel'] != 'dcda1611adf5f8fd':
    arrets.append('le gel des JSON n est pas dcda1611adf5f8fd')
n_non_suivis = sum(1 for p in s2['points'].values() for c in p['cfg'].values() for r in c['traj'].values()
                   if not r['etats'][0].get('suivi'))
if n_non_suivis:
    arrets.append('%d trajectoires de l etat 0 non suivies' % n_non_suivis)
for canon in ('555146abd2192f79', 'c14dafffc5f84c97', '82a0be882568fe0c', 'dcda1611adf5f8fd'):
    if canon not in c1 + c2 + l1 + l2 + journal:
        arrets.append('canon %s absent des journaux' % canon)
    if canon not in note:
        arrets.append('la note ne nomme pas le canon %s' % canon)
for sec, txt in (('sonde_etage1.json', c1), ('sonde_etage2.json', c2)):
    if ('sortie %s canon %s' % (sec, emp(open(os.path.join(SORTIE, sec), 'rb').read())[0])) not in txt:
        arrets.append('le canon de %s n est pas celui que la sonde a relu du disque' % sec)
# le tableau de la section 4 : statut et etalement de chaque cellule, retrouves dans la ligne du point
for n in ORDRE:
    ligne = [x for x in note.split('\n') if x.strip().startswith(n + ' ')]
    if len(ligne) != 1:
        arrets.append('la note n a pas exactement une ligne de tableau pour %s' % n)
        continue
    cellules = re.findall(r'(PLAT|PAS)\s+\.(\d{4})\s+(-?\d+)', ligne[0])
    attendu = []
    for cfg in ('F1G20', 'F1G30', 'F2G20', 'F3G20', 'F1GT'):
        pl = vq['detail']['points'][n]['plateaux'][cfg]
        attendu.append(('PLAT' if pl['statut'] == 'PLATEAU' else 'PAS', ('%.4f' % pl['etalement'])[2:], str(pl['k0'])))
    if cellules != attendu:
        arrets.append('tableau, point %s : note %s, JSON %s' % (n, cellules, attendu))
# les 18 Gamma de reference du rejeu (39_20, F1G20, etat 0)
tr = s2['points']['39_20']['cfg']['F1G20']['traj']
for k in range(-5, 13):
    g = repr(tr[str(k)]['etats'][0]['gamma'])
    if g not in note:
        arrets.append('la note ne porte pas Gamma(k = %d) = %s' % (k, g))
# A-6 a A-8 comptes du JSON
f1 = [n for n in ORDRE if vq['detail']['points'][n]['plateaux']['F1G20']['statut'] == 'PLATEAU']
if f1 != ['39_20'] or vq['detail']['points']['39_20']['plateaux']['F1G20']['k0'] != 0 or \
        vq['detail']['points']['39_20']['M17_sur_plateau'] is not True:
    arrets.append('A-7 / A-8 : le JSON ne rend plus un seul point, k0 = 0, (e) tient : %s' % f1)
if 'S_w lus 0 sur 6' not in nn or any(vq['detail']['T_etats'][n]['S_w'] is not None for n in ORDRE):
    arrets.append('A-4 : la note annonce S_w lus 0 sur 6, le JSON dit autre chose')
if 'FIN DE LA NUIT' not in note and 'FIN DE LA NUIT' not in nn:
    arrets.append('la note ne dit pas la fin de la nuit')

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
    'MANIFESTE %s -- RESULTAT DE LA NUIT E-B BIS (gel dcda1611adf5f8fd, sonde v3 555146abd2192f79, feuille v2 '
    'c14dafffc5f84c97, moteur v17 82a0be882568fe0c). ETAGE 1 : %s (TP aux quatre configurations). ETAGE 2 : VERDICT lu : %s '
    '(zero point QUALIFIE sur six). Plateforme : Windows AMD64, python 3.11.9, numpy 2.2.6. machine 2, classe B\n'
    % (NOM, v1['etage1'], vq['verdict']),
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for src, nom in PIECES:
    b, br, ob, obr = emp(open(src, 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, nom))
lignes.append('\nnon joint : nuit_EB_bis/sortie/reprise/ (fichiers de reprise, dont les vecteurs propres .npy) : contenu utile '
              'consolide dans sonde_etage1.json et sonde_etage2.json ; console_etage1.log / console_etage2.log et '
              'console_lecture_etage*.log identiques (meme canon) aux journaux joints\n')
lignes.append('entrants : lot de certification de machine 2 4de461538a1b694d ; lot de machine 1 25276846153bacff ; '
              'reference TP 4d51dd58ef456fe9\n')
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
