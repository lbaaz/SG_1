# -*- coding: ascii -*-
"""FABRIQUE DU LOT machine 2 'resultat du run juge du gel E-B ter (432319b9feb34b82)' -- manifeste + ZIP. 2026-11-15.
Derive de fabrique_lot_certification_gel_EB_ter_machine2_v1.py (non edite). Usage : py -3.11 -P fabrique_lot_resultat_EB_ter_machine2_v1.py
Gardes AVANT ecriture : pieces presentes ; mon lot de certification (d2f50caa808cfb1c) RECALCULE de son manifeste, et SCELLE AVANT le debut du pilote (heures de fichier contre heure du journal) ;
les douze sorties de point, les trois sorties d'instrument, les verdicts et le journal du pilote relus ; chaque chiffre de la note relu dans le JSON ou le journal qui le porte ; chaque canon de piece
nomme dans la note ; note ASCII ; le manifeste ne se porte pas lui-meme ; ZIP relu bit-identique."""
import hashlib
import json
import os
import re
import time
import unicodedata
import zipfile

ICI = os.path.dirname(os.path.abspath(__file__))
R = 'run_EB_ter/'
CT = 'certif_EB_ter/controles/'
NOM = 'lot_machine2_2026-11-15_resultat_EB_ter_v1'
MAN = os.path.join(ICI, 'MANIFEST_lot_machine2_resultat_EB_ter_v1.txt')
ZIP = os.path.join(ICI, NOM + '.zip')
NOTE = 'POUR_MACHINE1_resultat_EB_ter_machine2_v1.md'
SELF = 'fabrique_lot_resultat_EB_ter_machine2_v1.py'
MAN_CERT = 'MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt'
JUGES = ['C1', 'C2', 'C3', 'C4', 'M1', 'M2', 'M3', 'M4', 'L1', 'L2', 'L3', 'L4']
PIECES = [R + 'pilote_EB_ter.log', 'certif_EB_ter/pilote_console.log'] + \
         [R + 'console_%s.log' % x for x in ['etage0', 'ancres', 'etage1'] + ['point_' + i for i in JUGES]] + \
         [R + x for x in ('sonde_ter_etage0.json', 'sonde_ter_ancres.json', 'sonde_ter_etage1.json')] + [R + 'sonde_ter_point_%s.json' % i for i in JUGES] + \
         [R + x for x in ('lecture_ter_instrument.log', 'lecture_ter_instrument.console.log', 'verdict_ter_instrument.json', 'lecture_ter.log', 'lecture_ter.console.log', 'verdict_ter.json')] + \
         [CT + 'relecture_independante_EB_ter_machine2_v1.py', CT + 'relecture_independante_EB_ter_machine2_v1.log', CT + 'relecture_independante_EB_ter_machine2_v1.json', SELF]
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


def js(p):
    return json.load(open(os.path.join(ICI, p), encoding='utf-8'))


for p in PIECES + [NOTE, MAN_CERT, 'lot_machine2_2026-11-15_certification_gel_EB_ter_v1.zip']:
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

# --- ma certification : canon, et scellee avant le pilote
mc = open(os.path.join(ICI, MAN_CERT), 'rb').read()
if emp(mc)[0] != 'd2f50caa808cfb1c':
    arrets.append('le manifeste de ma certification est %s, attendu d2f50caa808cfb1c' % emp(mc)[0])
pil = lit(R + 'pilote_EB_ter.log')
t_deb = time.mktime(time.strptime(re.search(r'^(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d) DEBUT DU PILOTE', pil, re.M).group(1), '%Y-%m-%d %H:%M:%S'))
t_cert = os.path.getmtime(os.path.join(ICI, 'lot_machine2_2026-11-15_certification_gel_EB_ter_v1.zip'))
if not (t_cert < t_deb and t_deb - t_cert < 120):
    arrets.append('le lot de certification n est pas scelle juste avant le pilote : %.0f s' % (t_deb - t_cert))
# --- le journal du pilote
codes = re.findall(r'FIN  (\S+)\s+code=(\d+) duree=(\d+) s', pil)
attendus = ['etage0', 'ancres', 'etage1'] + ['point_' + i for i in JUGES]
if sorted(c[0] for c in codes) != sorted(attendus) or any(c[1] != '0' for c in codes):
    arrets.append('journal du pilote : appels %s' % codes)
dur = {c[0]: int(c[2]) for c in codes}
if dur['etage0'] != 14 or dur['ancres'] != 362 or dur['etage1'] != 396 or min(dur['point_' + i] for i in JUGES) != 3772 or max(dur['point_' + i] for i in JUGES) != 3981 or dur['point_M3'] != 3772:
    arrets.append('durees du pilote hors de la note : %s' % dur)
for x in ('DUREE TOTALE DU RUN : 4377 s', 'VERDICT DE L INSTRUMENT : TIENT', 'FIN  feuille instrument code=0', 'FIN  feuille verdict code=0', 'FIN DU PILOTE',
          "batterie (BatteryStatus WMI, 2 = secteur, 1 = batterie, vide = pas de batterie) : '2'", 'Windows 10.0.26300, 16 coeurs'):
    if x not in pil:
        arrets.append('journal du pilote : %r absent' % x)
if 'ECART' in pil or 'RUN INTERROMPU' in pil or 'ARRET' in pil:
    arrets.append('le journal du pilote porte un ECART, une interruption ou un ARRET')
if len(re.findall(r'canon \S.*\bOK$', pil, re.M)) != 10:
    arrets.append('le pilote n a pas verifie dix canons OK')
# --- le verdict de la feuille et les sorties
v = js(R + 'verdict_ter.json')
vi = js(R + 'verdict_ter_instrument.json')
pts = v['points']
cmp_ = [(i, pts[i]['n_juges'], pts[i]['n_qualifies'], pts[i]['n_lus_sur_le_plateau'], pts[i]['etat_lu']) for i in JUGES]
att = [('C1', 8, 8, 8), ('C2', 11, 11, 11), ('C3', 14, 14, 14), ('C4', 13, 13, 13), ('M1', 12, 12, 12), ('M2', 14, 14, 14), ('M3', 8, 8, 8), ('M4', 9, 9, 8),
       ('L1', 14, 14, 14), ('L2', 11, 11, 10), ('L3', 14, 13, 12), ('L4', 9, 9, 6)]
if [(a, b, c, d) for a, b, c, d, e in cmp_] != att or any(e != 'QUALIFIE' for a, b, c, d, e in cmp_):
    arrets.append('comptes par point : %s' % cmp_)
if (v['verdict'], v['issue_depot'], v['n_juges'], v['n_qualifies'], v['n_plateau_A'], v['n_lus_sur_le_plateau'], v['instrument']) != \
        ('ESTIMATEUR QUALIFIE', 'LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS', 137, 136, 137, 130, 'TIENT'):
    arrets.append('verdict de la feuille : %s' % ((v['verdict'], v['issue_depot'], v['n_juges'], v['n_qualifies'], v['n_plateau_A'], v['n_lus_sur_le_plateau']),))
nq = [(i, e['rang'], e['echecs']) for i in JUGES for e in pts[i]['etats'] if e['statut'] != 'QUALIFIE']
if len(nq) != 1 or nq[0][0] != 'L3' or nq[0][1] != 5 or 'accord C / A' not in nq[0][2][0] or '0.0659' not in nq[0][2][0]:
    arrets.append('les etats non qualifies : %s' % nq)
if vi['instrument'] != 'TIENT' or vi['etage0']['lectures'] != 84 or vi['ancres']['lectures'] != 192 or not (4.3e-16 < vi['ancres']['pire_ecart_ln'] < 4.5e-16):
    arrets.append('verdict de l instrument du run : pas ce que la note dit')
n, non, it, pm, rm = 0, 0, {}, 1.0, 0.0
sansplat = 0
for i in JUGES:
    s = js(R + 'sonde_ter_point_%s.json' % i)
    if s['sonde_canon'] != 'b5616dcf858e8801' or s['mode'] != 'point' or s['ids'] != [i]:
        arrets.append('en-tete de la sortie du point %s' % i)
    for e in s['points'][0]['etats']:
        for x in 'ABCD':
            for k, t in e['traj'][x].items():
                n += 1
                non += not t['suivi']
                it[t['iterations']] = it.get(t['iterations'], 0) + 1
                pm = min(pm, t['poids_site'])
                rm = max(rm, t['residu'] / max(1.0, abs(t['E_re'])))
if (n, non, it) != (6576, 0, {2: 6461, 3: 110, 4: 5}) or not (0.656 < pm < 0.658) or not (9.7e-12 < rm < 9.9e-12):
    arrets.append('lectures du run : %d, %d non suivies, iterations %s, poids %.3f, residu %.2e' % (n, non, it, pm, rm))
rj = js(CT + 'relecture_independante_EB_ter_machine2_v1.json')
if not (rj['accord_complet'] is True and rj['ecarts'] == [] and rj['comptes'] == [137, 136, 137, 130] and rj['verdict_ma'] == rj['verdict_m1'] and rj['issue_ma'] == rj['issue_m1']):
    arrets.append('ma relecture : pas un accord complet')
if not all(rj['annonces']['A-%d' % k][0] == 'True' for k in range(3, 11)):
    arrets.append('annonces A-3 a A-10 : pas toutes vraies par ma lecture')
rl = lit(CT + 'relecture_independante_EB_ter_machine2_v1.log')
for x in ('etalement de la meilleure fenetre sous A : mediane 0.0001, plus grand 0.0234', 'etalement de la meilleure fenetre sous B : mediane 0.0000, plus grand 0.0204',
          'etalement de la meilleure fenetre sous C : mediane 0.0025, plus grand 0.0376', 'etalement de la meilleure fenetre sous D : mediane 0.0001, plus grand 0.0416',
          'accord B / A : |ln| mediane 0.0000, plus grand 0.0129 (137 etats)', 'accord C / A : |ln| mediane 0.0008, plus grand 0.0659 (137 etats)', 'accord D / A : |ln| mediane 0.0000, plus grand 0.0264 (137 etats)',
          'consigne (e) : |ln(G_dep / Gamma_pl(A))| mediane 0.0193, plus grand 0.1023, au-dessus de tau : 7 sur 137', "ACCORD COMPLET : True",
          "{'A': 0, 'B': 0, 'C': 0, 'D': 0}"):
    if x not in rl:
        arrets.append('journal de ma relecture : %r absent' % x)
for x in ('13:42:11', '3772 s (M3) a 3981 s', '4377 s', '136 etats sur 137', '130 sur 137', '0.0686', '0.0659', 'L3 rang 5', '2.3e-9', '2.3e-4', '6576', '6461', 'poids au site au moins 0.657',
          '9.8e-12', '42110a3d1eabdaa0', 'd2f50caa808cfb1c', '13 h 42 min 03 s', 'M4 rang 12, L2 rang 5, L3 rangs 7 et 13, L4 rangs 0, 1 et 4', '+0.0686', '-0.0373', '14 s', '362 s', '396 s',
          '2657206', 'A-9 mediane 0.0193', 'dix canons verifies OK', 'BatteryStatus 2'):
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
    'MANIFESTE %s -- RESULTAT DU RUN JUGE DU GEL E-B TER (432319b9feb34b82), joue UNE fois sur BOCAL4 le 15/11/2026 de 13 h 42 a 14 h 55 (4377 s), tous les appels a code 0 : l instrument TIENT ; '
    'verdict de la feuille de machine 1 : ESTIMATEUR QUALIFIE (etat lu QUALIFIE aux douze points, 136 etats sur 137 ; la lecture deposee est sur le plateau a 130 sur 137) ; '
    'ma feuille, independante, rejuge les 137 etats et rend le meme verdict, la meme issue, les memes comptes : 0 ecart. Lot scelle APRES ma certification (d2f50caa808cfb1c, 13 h 42 min 03 s). '
    'Pas d acte (il est a machine 1), pas de depot, aucun numero. machine 2\n' % NOM,
    'colonnes : empreinte_B (sha256 NFC+LF, 16 hex)  empreinte_brute  octets_B  octets_bruts  fichier\n',
    "Le CANON du lot est l'empreinte B de CE manifeste ; il ne se porte pas lui-meme.\n\n"]
for p in [NOTE] + PIECES:
    b, br, ob, obr = emp(open(os.path.join(ICI, p), 'rb').read())
    lignes.append('%s %s %8d %8d  %s\n' % (b, br, ob, obr, p))
lignes.append('\nentrants : lot de machine 1 42110a3d1eabdaa0 (gel 432319b9feb34b82) ; ma certification d2f50caa808cfb1c ; registre 8d54bf9 ; moteur 82a0be882568fe0c ; depot 10887c60d5f55bcf ; '
              'retenus 69b3bab3bb8480b7 ; reference du temoin 4d51dd58ef456fe9\n')
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
    mauvais = [n_ for n_ in z.namelist() if z.read(n_) != attendu_zip.get(n_)]
    manque = sorted(set(attendu_zip) - set(z.namelist()))
if mauvais or manque:
    print('ZIP NON BIT-IDENTIQUE : %s ; manquants %s' % (mauvais, manque))
    raise SystemExit(1)
print('manifeste %s' % MAN)
print('CANON DU LOT (empreinte B du manifeste) : %s' % emp(open(MAN, 'rb').read())[0])
print('ZIP %s -- %d pieces + manifeste, relu bit-identique, %d octets' % (ZIP, len(PIECES) + 1, os.path.getsize(ZIP)))
