# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' du run du gel "la chaine E-A au second ordre" (journal_delta_nn_ordre2_chaine_EA_v1.md, canon c2f3e5c9102dc1a7,
projet version 1, lot da1c2668d317b9d5), 2026-11-15. Chaque affirmation CHIFFREE de l'acte est RECALCULEE ici depuis MES sources (le JSON de la sonde et le verdict de
la feuille rendus par MON run, MON lecteur independant ecrit du texte du gel, mes journaux de certification, de bloc, de banc, de bruit, le registre public), jamais
lue dans le script d'ecriture ni dans le releve de machine 1. Les phrases attendues sont CONSTRUITES depuis les donnees puis cherchees dans l'acte (blancs normalises) :
un nombre tape a la main et faux est une morsure. Meme methode que verification_acte_domaine_G1_machine2_v1.py (acte du delta 97), adaptee a la cascade par bandes.
Usage (depuis BOCAL4) : python -P acte_ordre2_contreseing/verification_acte_ordre2_machine2_v1.py
Variables : LOT_ALT (contre-epreuve sur une copie mutee du lot), SUFFIXE_SORTIE, REGISTRE_CLONE. Ce script ne modifie rien d'autre que ses deux sorties."""
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import unicodedata
import zipfile
from fractions import Fraction as F

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DG = os.path.join(ROOT, 'ordre2')
SO = os.path.join(DG, 'sortie')
ACTE_NOM = 'journal_delta_nn_ordre2_chaine_EA_v1.md'
LOT = os.environ.get('LOT_ALT', 'lot_machine1_2026-11-15_acte_ordre2_chaine_EA_v1_recu.zip')
SUFFIXE = os.environ.get('SUFFIXE_SORTIE', '')
MANIF = 'MANIFEST_lot_machine1_acte_ordre2_chaine_EA_v1.txt'
CLONE = os.environ.get('REGISTRE_CLONE', os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', 'claude', '75adcc7f3c1d08bf', '7d33635e-8345-4a2c-a69e-f6a51f9d8fa7',
                                                      'scratchpad', 'reg_verif97'))
LOG = os.path.join(HERE, 'verification_acte_ordre2_machine2_v1%s.log' % SUFFIXE)
JSN = os.path.join(HERE, 'verification_acte_ordre2_machine2_v1%s.json' % SUFFIXE)
FH = open(LOG, 'w', encoding='ascii', newline='\n')
CHK, INFO = [], []


def dire(s=''):
    s = s.encode('ascii', 'replace').decode('ascii')
    print(s, flush=True)
    FH.write(s + '\n')
    FH.flush()


def chk(nom, ok, msg):
    CHK.append({'id': nom, 'ok': bool(ok), 'msg': msg})
    dire('%s %-6s %s' % (nom, 'TIENT' if ok else 'MORD', msg))


def info(msg):
    INFO.append(msg)
    dire('     info   ' + msg)


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def norm(s):
    return re.sub(r'\s+', ' ', s)


def rd(p):
    return open(p, 'rb').read()


def rt(p):
    return open(p, encoding='utf-8', errors='replace').read()


def manque(phrases, texte):
    return [p for p in phrases if norm(p) not in texte]


# ------------------------------------------------------------------ l'acte et son lot
zl = zipfile.ZipFile(os.path.join(ROOT, LOT))
RAW = zl.read(ACTE_NOM)
ACTE = RAW.decode('utf-8')
AN = norm(ACTE)
LIGNES = ACTE.split('\n')
dire('VERIFICATION de l acte %s par machine 2' % ACTE_NOM)
c_act = emp(RAW)[0]
chk('C01', c_act == 'c2f3e5c9102dc1a7' and len(RAW) == 24888 and len(LIGNES) - 1 == 345
    and ACTE.startswith("DELTA nn -- LA CHAINE E-A AU SECOND ORDRE : RUN DES 14 ET 15/11/2026 SOUS LE GEL 41153158190cf7f1.\n")
    and '-- PROJET, VERSION 1' in ACTE and ACTE.rstrip().endswith('-- FIN journal_delta_nn_ordre2_chaine_EA_v1 --'),
    'acte : canon %s (annonce c2f3e5c9102dc1a7), %d octets (24888), %d lignes (345), en-tete et ligne de FIN, VERSION 1' % (c_act, len(RAW), len(LIGNES) - 1))
man = rd(os.path.join(ROOT, MANIF))
bad, n_l = [], 0
for ln in man.decode('utf-8').split('\n'):
    p = ln.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        n_l += 1
        if emp(zl.read(p[4])) != (p[0], p[1], int(p[2]), int(p[3])):
            bad.append(p[4])
canon_lot = emp(man)[0]
chk('C02', n_l == 10 and not bad and len([n for n in zl.namelist() if not n.startswith('MANIFEST_')]) == 10 and canon_lot == 'da1c2668d317b9d5',
    '%d pieces sur 10 au canon, a l empreinte brute et aux deux tailles ; ecarts %s ; CANON DU LOT %s (annonce da1c2668d317b9d5)' % (n_l, bad, canon_lot))
n_asc = sum(1 for c in ACTE if ord(c) > 127)
long_max = max(len(x) for x in LIGNES)
chk('C03', n_asc == 0 and long_max <= 100 and '%' not in ACTE and '\t' not in ACTE,
    'forme de l acte : non ASCII %d, plus longue ligne %d colonnes (<= 100), pour cent %d, tabulations %d' % (n_asc, long_max, ACTE.count('%'), ACTE.count('\t')))

# ------------------------------------------------------------------ index de TOUT ce que je detiens
IDX = {}


def ajoute(h, chemin):
    IDX.setdefault(h, []).append(chemin)


def zip_membres(octets, label, prof):
    try:
        z = zipfile.ZipFile(io.BytesIO(octets))
    except zipfile.BadZipFile:
        return
    for i in z.infolist():
        if i.is_dir():
            continue
        b = z.read(i.filename)
        ajoute(emp(b)[0], '%s!%s' % (label, i.filename))
        if prof < 1 and i.filename.lower().endswith('.zip'):
            zip_membres(b, '%s!%s' % (label, i.filename), prof + 1)


n_f = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in ('__pycache__', '.git')]
    for f in fn:
        p = os.path.join(dp, f)
        try:
            if os.path.getsize(p) > 80 * 1024 * 1024:
                continue
            b = rd(p)
        except OSError:
            continue
        n_f += 1
        rel = os.path.relpath(p, ROOT).replace('\\', '/')
        ajoute(emp(b)[0], rel)
        if f.lower().endswith('.zip'):
            zip_membres(b, rel, 0)
n_reg = 0
try:                                                       # les fichiers du registre public (clone), indexes sous leur chemin au registre
    subprocess.run(['git', '-C', CLONE, 'fetch', '-q', 'origin'], capture_output=True, text=True, timeout=120)
    subprocess.run(['git', '-C', CLONE, 'checkout', '-q', 'origin/main'], capture_output=True, text=True, timeout=120)
    for f in subprocess.run(['git', '-C', CLONE, 'ls-files'], capture_output=True, text=True, timeout=120).stdout.splitlines():
        if f:
            ajoute(emp(rd(os.path.join(CLONE, f)))[0], 'registre:' + f)
            n_reg += 1
except Exception:
    pass
info('index : %d fichiers, %d empreintes distinctes (fichiers et membres de zip), dont %d fichiers du registre public' % (n_f, len(IDX), n_reg))

paires = sorted(set(re.findall(r'^\s+([\w./-]+\.(?:py|md|json|log|txt))\s+([0-9a-f]{16})\s*$', ACTE, re.M)))
non_res, mauvais_nom, mauvais_reg = [], [], []
for nom, c in paires:
    if c not in IDX:
        non_res.append((nom, c))
    elif not any(re.split(r'[/!:]', x)[-1] == nom.split('/')[-1] for x in IDX[c]):
        mauvais_nom.append((nom, c))
    elif nom.split('/')[0] in ('scripts', 'gels', 'journal') and ('registre:' + nom) not in IDX[c]:
        mauvais_reg.append((nom, c))
chk('C04', len(paires) == 28 and not non_res and not mauvais_nom and not mauvais_reg,
    'nn.1 : %d couples (nom, canon) lus dans l acte, tous retrouves chez moi, le nom est celui d une piece de ce canon, les trois du registre sous leur chemin public ; '
    'non resolus %s ; noms differents %s ; chemins du registre faux %s' % (len(paires), non_res, mauvais_nom, mauvais_reg))
tous = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', ACTE)))
non_res_tous = [c for c in tous if c not in IDX]
chk('C05', len(tous) >= 30 and not non_res_tous,
    '%d empreintes de 16 chiffres citees dans tout l acte, toutes recalculees de pieces ou de manifestes que je detiens ; non resolues %s' % (len(tous), non_res_tous))

# ------------------------------------------------------------------ donnees de MON run, lues par MON lecteur
S = json.load(open(os.path.join(SO, 'sonde_ordre2.json'), encoding='ascii'))
V = json.load(open(os.path.join(SO, 'verdict_ordre2.json'), encoding='ascii'))
GEL = open(os.path.join(DG, 'gel_ordre2_chaine_EA_pre_enregistrement_v1.md'), encoding='ascii').read()
GN = norm(GEL)
argv0 = sys.argv
sys.argv = ['banc', os.path.join(DG, 'lecture_ordre2_machine1_v1.py'), os.path.join(DG, 'gel_ordre2_chaine_EA_pre_enregistrement_v1.md')]
sp = importlib.util.spec_from_file_location('banc_m2', os.path.join(DG, 'banc_feuille_ordre2_machine2_v1.py'))
B = importlib.util.module_from_spec(sp)
sp.loader.exec_module(B)
sys.argv = argv0
mien, RM = B.lecteur(S)
PT = {x['id']: x for x in S['points']}
VP = {x['id']: x for x in V['points']}
ORDRE = [p['id'] for p in S['points']]
TAB = {}
for m in re.finditer(r'^\s+([CMLAW]\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+delta ([+-][0-9.]+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+(EN DOMAINE|HORS DOMAINE)\s+N (\d+)$', GEL, re.M):
    TAB[m.group(1)] = {'w2': m.group(2), 'f': m.group(3), 'delta': m.group(4), 'D1': float(m.group(5)), 'c': float(m.group(6)), 'st': m.group(7), 'N': int(m.group(8))}
BANDE = {'C': ('proche', 1.25), 'M': ('moyenne', 1.6), 'L': ('lointaine', 2.0)}
JUG = [k for k in ORDRE if k[0] in 'CML']
D = {}
for pid in ORDRE:
    r = RM[pid]
    D[pid] = r
ok_lect = (mien['v'] == 'TIENT' and mien['bandes'] == {'proche': 'T', 'moyenne': 'T', 'lointaine': 'T'} and mien['comp'] == 'MIEUX' and mien['ener'] == 'T' and mien['vnu'] == 'TIENT'
           and mien['marge'] == [] and V['verdict'] == "L'ORDRE 2 TIENT" and len(TAB) == 16 and len(ORDRE) == 16)
fmt_pal = lambda x: 'aucun' if x is None else ('%g' % x)
manq1, manq2 = [], []
for pid in ORDRE:
    d, t = D[pid], TAB[pid]
    fac = t['f']
    if d['statut'] == 'NL':
        row1 = '%s %s %s %s temoin - %d NON LISIBLE (moins de 6 etats juges)' % (pid, t['w2'], fac, t['delta'], d['nj'])
        if norm(row1) not in AN:
            manq1.append(row1)
        continue
    bnd, bor = BANDE.get(pid[0], ('ancre' if pid[0] == 'A' else 'temoin', None))
    q2 = d['q2']
    row1 = '%s %s %s %s %s %s %d %.3f %.3f %.3f %s %s' % (pid, t['w2'], fac, t['delta'], bnd, '-' if bor is None else '%g' % bor, d['nj'], q2[0], q2[2], q2[1],
                                                           fmt_pal(d['pal']), 'TENU' if pid[0] in 'CML' else 'LU')
    if norm(row1) not in AN:
        manq1.append(row1)
    q1 = d['q1']
    row2 = '%s %.3f %.3f %.3f %.3f %.3f %s %.2e %s' % (pid, q1[0], q1[2], q1[1], d['pire'][1], d['pire'][0], d['comp'], d['ecart_max'], 'TENUE' if d['ener'] == 'T' else 'NON TENUE')
    if norm(row2) not in AN:
        manq2.append(row2)
nj12 = sum(D[k]['nj'] for k in JUG)
mot = {}
for k in JUG:
    for m in D[k]['motifs']:
        if m is not None:
            mot[m] = mot.get(m, 0) + 1
n_et12 = sum(len(D[k]['motifs']) for k in JUG)
phr = ['Aux douze points juges : %d etats, %d juges, %d exclus (%d sous dix planchers, %d a J flou, %d a barriere vide).' % (n_et12, nj12, n_et12 - nj12, mot.get(4, 0), mot.get(1, 0), mot.get(7, 0)),
       'A W2 : %d etats juges, %d exclus sous dix planchers.' % (D['W2']['nj'], sum(1 for m in D['W2']['motifs'] if m == 4)),
       'Reponse de la feuille : L\'ORDRE 2 TIENT. Les trois bandes sont TENUES ; aucun des douze points ne tombe ; %d etats juges.' % nj12,
       'seize points, %d etats' % sum(len(p['etats']) for p in S['points'])]
mq = manque(phr, AN)
chk('C06', ok_lect and not manq1 and not manq2 and not mq and nj12 == 132 and n_et12 == 168 and mot == {4: 31, 1: 4, 7: 1},
    'nn.0, nn.4 : mon lecteur independant (ecrit du texte du gel) lit TIENT / 3 bandes T / MIEUX / energie T / sans marge TIENT sur mon JSON ; les 15 lignes du premier tableau '
    '(w2, facteur, delta, bande, borne, juges, q2 min med max, palier, statut) et les 15 du second (q1, pires ecarts, comparaison, ecart d energie) recalculees ; '
    '%d etats juges sur %d, exclus %s ; absentes %s %s %s' % (nj12, n_et12, mot, manq1, manq2, mq))

# ------------------------------------------------------------------ C07 : le verdict rejoue, les journaux
mon_v = rd(os.path.join(SO, 'verdict_ordre2.json')).replace(b'\r\n', b'\n')
v_m1 = zl.read('verdict_rejoue_machine1.json')
l_m1 = zl.read('lecture_rejouee_machine1.log').decode('utf-8').split('\n')
l_m2 = open(os.path.join(SO, 'lecture_ordre2.log'), encoding='utf-8').read().split('\n')
diff = [(a, b) for a, b in zip(l_m1, l_m2) if a != b]
chk('C07', emp(rd(os.path.join(SO, 'verdict_ordre2.json')))[0] == '4195583a970eaf70' == emp(v_m1)[0] and mon_v == v_m1.replace(b'\r\n', b'\n') and len(l_m1) == len(l_m2)
    and len(diff) <= 1 and (not diff or diff[0][0].startswith('LECTURE DU GEL')) and 'SELFTEST : 160 cas, 160 tenus' in l_m1
    and emp(rd(os.path.join(SO, 'lecture_ordre2.log')))[0] == 'c8a03a393d95cebf' and emp(zl.read('lecture_rejouee_machine1.log'))[0] == '616799ab3deb89c2',
    'verdict de mon run == verdict rejoue par machine 1, octet pour octet apres CRLF -> LF (mes octets bruts %d, les siens %d), canon 4195583a970eaf70 ; journaux : %d lignes de '
    'part et d autre, %d ligne qui differe ; canons des deux journaux c8a03a393d95cebf et 616799ab3deb89c2' % (len(rd(os.path.join(SO, 'verdict_ordre2.json'))), len(v_m1), len(l_m1), len(diff)))

# ------------------------------------------------------------------ C08 : nn.2, ce que j'ai joue (mes journaux)
cj = json.load(open(os.path.join(DG, 'controles_gel_ordre2_machine2_v1.json'), encoding='ascii'))
bl = open(os.path.join(DG, 'banc_feuille_ordre2_machine2_v1.log'), encoding='ascii').read()
bloc = rt(os.path.join(DG, 'bloc_independant_machine2_v1.log'))
con = open(os.path.join(SO, 'console_ordre2.log'), encoding='utf-8').read()
cmp_ = open(os.path.join(SO, 'compare_run_essai_ancres_machine2.log'), encoding='ascii').read()
etm = open(os.path.join(SO, 'etat_machine_machine2.log'), encoding='ascii').read()
pf = S['plateforme']
dur = {p['id']: p['duree_s'] for p in S['points']}
durs = ', '.join('%s %d' % (k, int(dur[k] + 0.5)) for k in ORDRE)               # une demi-seconde exacte (A2 = 156.5) est arrondie vers le haut
somme15 = sum(dur[k] for k in ORDRE if k != 'W2')
nb_bloc = len(re.findall(r'^\s+\w+\s+TIENT\s', bloc, re.M))
phr = ['(22 controles, 0 morsure ; le bloc recalcule a part, 17 controles, 0 morsure)',
       'sonde lancee le 14/11 a 23 h 26, finie le 15/11 a 0 h 41, 4524 secondes, code 0',
       'BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs, variables de fils non fixees.',
       'batterie a 100 pour cent au lancement, a 62 a la fin, processeur a 2516 MHz pour un maximum de 3801 (journal de l\'etat de la machine)',
       'le run en a pris %.0f et %.0f.' % (somme15, dur['W2']), 'Durees par point, en secondes : %s.' % durs,
       'Aux deux ancres, le run rend au bit les valeurs de l\'essai de sa certification (28 etats, chaines comprises).',
       'W2 en dernier, 14 etats chacun ; aucun arret, aucune reprise, aucun point rejoue ; puis la feuille (selftest 160 sur 160, code 0).']
mq = manque(phr, AN)
ok8 = (cj['bilan']['controles'] == 22 and cj['bilan']['mord'] == 0 and nb_bloc == 17 and 'ecarts feuille / lecteur : 0' in bl
       and 'BILAN : 28 etats, 0 etiquettes differentes ; ecart absolu max de Gamma_2D (k = 2, 3, 4) 0.00e+00 ; relatif max 0.00e+00' in cmp_ and 'chaine : ecart relatif max 0.00e+00' in cmp_
       and '2026-11-14 23:26:01 LANCEMENT DE LA SONDE' in con and '2026-11-15 00:41:24 FIN DE LA SONDE code=0 duree=4524 s' in con and 'FIN DE LA FEUILLE code=0' in con
       and pf['systeme'] == 'Windows' and pf['machine'] == 'AMD64' and pf['python'] == '3.11.9' and pf['numpy'] == '2.2.6' and pf['coeurs'] == 16
       and all(v is None for v in pf['fils'].values()) and pf['temoin_arrondi'] == '0x1.a483018a169c6p+64'
       and 'BatteryStatus 1' in etm and '62 pour cent' in etm and 'a 23:26 au lancement : batterie en decharge a 100 pour cent' in etm and 'CurrentClockSpeed 2516 MHz ; MaxClockSpeed 3801 MHz' in etm
       and 'de l\'ordre de 3100 secondes pour les quinze premiers points, de 1500 pour W2 seul' in GN and round(somme15) == 3177 and round(dur['W2']) == 1346
       and all(len(p['etats']) == 14 for p in S['points']) and ORDRE[-1] == 'W2')
chk('C08', ok8 and not mq, 'nn.2 : mes journaux (22 controles / 0 mordent ; bloc %d controles TIENT ; 4000 sondes / 0 ecart ; 28 etats des ancres chaines comprises ; heures, code, duree, plateforme, '
    'temoin ; batterie et frequence sur la piece etat_machine ; durees par point recalculees du JSON, somme des quinze %.1f s, W2 %.1f s ; le gel annonce 3100 et 1500) == l acte ; phrases absentes %s' % (
        nb_bloc, somme15, dur['W2'], mq))

# ------------------------------------------------------------------ C09 : nn.3, les gardes
dmax = max(abs(p['garde_moteur']['D1'] - TAB[p['id']]['D1']) for p in S['points'])
cmax_ = max(abs(p['garde_moteur']['c_max'] - TAB[p['id']]['c']) for p in S['points'])
refs = {'A1': ((7, 2), 2.1623273017950654e-10), 'A2': ((8, 2), 2.6613925716641374e-09)}
ancre_ok = all([e for e in PT[a]['etats'] if (e['n1'], e['n2']) == refs[a][0]][0]['Gamma_2D']['3'] == refs[a][1] for a in refs)
stat_ok = all(PT[k]['garde_moteur']['statut'] == TAB[k]['st'] for k in ORDRE)
hors = [k for k in ORDRE if TAB[k]['st'] == 'HORS DOMAINE']
G8 = {'A1': ((7, 2), 2.3236497766513317e-10, 0.002118984943055927), 'A2': ((8, 2), 2.794344791699548e-09, -0.0028201377357584354)}
g8f, g8e = 0.0, 0.0
for a, (et, rf, re_) in G8.items():
    e = [e for e in PT[a]['etats'] if (e['n1'], e['n2']) == et][0]
    g8f = max(g8f, abs(e['chaine2']['gammas_flux'][2] / rf - 1))
    g8e = max(g8e, abs(e['chaine2']['dE'][2] / re_ - 1))
phr = ['G-1 et G-7 : le moteur et la sonde lus au JSON sont aux canons 82a0be882568fe0c et 24315c52b234319c.',
       'G-4 : les etats (7,2) de A1 et (8,2) de A2 rendent la lecture du run de M17 au bit (ecart relatif 0, tolerance 1e-2).',
       'G-5 : selftest 160 sur 160, sur BOCAL4 et chez machine 1.',
       'ses D1 et c_max en different de moins de 1e-6 (tolerance 5e-5) ; elle dit HORS DOMAINE a M4, L1, L2, L4, W1, W2.',
       'G-8 : aux deux memes etats, la chaine d\'ordre 2 de BOCAL4 rend les references de machine 1 a %s pres pour Gamma_flux (tolerance 1e-3) et a %s pres pour dE (tolerance 1e-6).' % (
           ('%.0e' % g8f).replace('e-0', 'e-'), ('%.0e' % g8e).replace('e-0', 'e-'))]
mq = manque(phr, AN)
chk('C09', S['sonde_canon'] == '24315c52b234319c' and S['moteur_canon'] == '82a0be882568fe0c' and dmax < 1e-6 and cmax_ < 1e-6 and V['motifs'] == [] and ancre_ok and stat_ok
    and hors == ['M4', 'L1', 'L2', 'L4', 'W1', 'W2'] and g8f < 1e-3 and g8e < 1e-6 and not mq,
    'nn.3 : canons du moteur et de la sonde au JSON ; ecart maximal de D1 %.2e et de c_max %.2e entre la garde consignee et la table du gel (< 1e-6) ; motifs %s ; ancres au bit : %s ; '
    'statut de la garde == la table aux 16 points : %s, HORS DOMAINE %s ; G-8 : Gamma_flux a %.1e, dE a %.1e des references du gel ; phrases absentes %s' % (
        dmax, cmax_, V['motifs'], ancre_ok, stat_ok, hors, g8f, g8e, mq))

# ------------------------------------------------------------------ C10 : nn.5 et nn.6, le verdict, la comparaison, les energies
bmax = {}
for k in JUG:
    b = BANDE[k[0]][0]
    if b not in bmax or D[k]['q2'][1] > bmax[b][0]:
        bmax[b] = (D[k]['q2'][1], k)
qmin_k = min(JUG, key=lambda k: D[k]['q2'][0])
qmax_k = max(JUG, key=lambda k: D[k]['q2'][1])
q1min = min(D[k]['q1'][0] for k in JUG)
q1max = max(D[k]['q1'][1] for k in JUG)
mince = sorted(JUG, key=lambda k: D[k]['pire'][0] - D[k]['pire'][1])[:3]
emax = {}
for k in JUG:
    b = BANDE[k[0]][0]
    if b not in emax or D[k]['ecart_max'] > emax[b][0]:
        emax[b] = (D[k]['ecart_max'], k)
gel13 = ('sur douze points neufs, aux facteurs de 2/3 a 3/2, la chaine completee par son second ordre et ses sites bas a rendu la lecture de E-B a k = 3 a un facteur 1.25 pres '
         'pour |delta| <= 0.06, 1.6 pres jusqu\'a 0.10, 2 pres jusqu\'a 0.12 ; rien de plus. C\'est un domaine, borne par bande, de cette chaine-la contre cette lecture-la.')
gel13b = 'sur douze points neufs, aux facteurs de 2/3 a 3/2, la chaine completee par son second ordre et ses sites bas a rendu la lecture de E-B a k = 3 a un facteur 1.25 pres pour |delta| <= 0.06, 1.6 pres jusqu\'a 0.10, 2 pres jusqu\'a 0.12.'
d2 = lambda k: D[k]['pire']
phr = ['Plus grand q2 par bande : %.3f pour une borne de 1.25, %.3f pour 1.6, %.3f pour 2 ; ils sont a %s, %s et %s.' % (bmax['proche'][0], bmax['moyenne'][0], bmax['lointaine'][0],
                                                                                                         bmax['proche'][1], bmax['moyenne'][1], bmax['lointaine'][1]),
       'le plus petit q2 des %d etats juges est %.3f (a %s), le plus grand %.3f (a %s).' % (nj12, D[qmin_k]['q2'][0], qmin_k, D[qmax_k]['q2'][1], qmax_k),
       'La lecture SANS MARGE (gel, section 11) rend le meme verdict : aucun etat n\'est garde par la marge d\'un plancher, la borne nue les contient tous.',
       gel13b + ' C\'est un domaine, borne par bande, de cette chaine-la contre cette lecture-la.',
       'Comparaison au pire etat : les douze points sont MIEUX. La chaine du moteur va, sur les memes %d etats, de q1 = %.3f a q1 = %.3f ; l\'ordre 2 de %.3f a %.3f.' % (
           nj12, q1min, q1max, D[qmin_k]['q2'][0], D[qmax_k]['q2'][1]),
       'Les trois points ou l\'ecart entre les deux pires est le plus mince : %s' % ', '.join(('%s (%.3f pour l\'ordre 2 contre %.3f)' if i == 0 else '%s (%.3f contre %.3f)') % (k, d2(k)[1], d2(k)[0]) for i, k in enumerate(mince)),
       'l\'ecart de L2, %.3f en logarithme' % (d2('L2')[0] - d2('L2')[1]),
       'Ce que le gel autorise a ecrire : le second ordre est ce qui manquait a la chaine du moteur, aux points lus.',
       'Energies : les douze points sont tenus. Plus grand ecart relatif entre le decalage d\'energie de la chaine d\'ordre 2 et celui de l\'etat 2D : %.4f a la bande proche, %.4f a la moyenne, '
       '%.4f a la lointaine (a %s), pour une tolerance de 0.01.' % (emax['proche'][0], emax['moyenne'][0], emax['lointaine'][0], emax['lointaine'][1]),
       'Ce que le gel autorise a ecrire : la chaine d\'ordre 2 rend aussi le decalage d\'energie des etats, a un pour cent pres, ce que les largeurs ne controlent pas.']
mq = manque(phr, AN)
gel_ph = ['sur douze points neufs, aux facteurs de 2/3 a 3/2, la chaine completee par son second ordre et ses sites bas a rendu la lecture de E-B a k = 3 a un facteur 1.25 pres',
          'l\'acte pourra ecrire que le second ordre est ce qui manquait a la chaine du moteur, aux points lus', 'la chaine d\'ordre 2 rend aussi le decalage d\'energie des etats, a un pour cent pres, ce que les largeurs ne controlent pas']
mq_gel = [p for p in gel_ph if norm(p) not in GN]
chk('C10', not mq and not mq_gel and mince == ['L2', 'L1', 'C3'] and bmax['proche'][1] == 'C2' and bmax['moyenne'][1] == 'M4' and bmax['lointaine'][1] == 'L4',
    'nn.5, nn.6 : plus grand q2 par bande (%.3f, %.3f, %.3f aux points %s %s %s), plus petit et plus grand des %d etats, q1 de %.3f a %.3f, les trois comparaisons les plus minces %s, '
    'les ecarts d energie par bande, recalcules de mon lecteur ; les trois phrases "ce que le gel autorise" == section 13 de mon gel (absentes du gel : %s) ; absentes de l acte %s' % (
        bmax['proche'][0], bmax['moyenne'][0], bmax['lointaine'][0], bmax['proche'][1], bmax['moyenne'][1], bmax['lointaine'][1], nj12, q1min, q1max, mince, mq_gel, mq))

# ------------------------------------------------------------------ C11 : nn.6 (energie, controle de machine 2), nn.9 (reserves)
phr = ['l\'erreur relative de la chaine d\'ordre 2 est divisee par quatre a chaque moitie de g (7.50e-05, 1.84e-05, 4.59e-06 a l\'etat d\'ancre de A1) ; a g, l\'ordre 1 est a 4.37e-02, '
       '"u seul" a 4.40e-02, "Sigma2 seul" a 4.40e-04.', 'L\'energie tient donc Sigma2 ; elle ne tient pas le saut au second voisin, qui n\'y entre qu\'a l\'ordre suivant.',
       'machine 2 le retrouve a 5e-13 pres par une somme sur les 36 sauts de x^5, et a 5e-15 pres en le lisant sur la matrice H_2D du moteur, sans enumerer aucun saut.']
mq = manque(phr, AN)
ligA1 = [l for l in bloc.split('\n') if l.strip().startswith('A1 (7,2)')][0]
nums = re.findall(r'erreur / \|dE\| de la chaine d\'ordre 2 : ([0-9.e+-]+), ([0-9.e+-]+), ([0-9.e+-]+) ; ordre 1 : ([0-9.e+-]+) ; Sigma2 seul : ([0-9.e+-]+) ; u seul : ([0-9.e+-]+)', ligA1)[0]
rap = float(nums[0]) / float(nums[1]), float(nums[1]) / float(nums[2])
m_u = re.search(r'plus grand ecart relatif : t [0-9.e+-]+ ; Sigma2 ([0-9.e+-]+) ; u ([0-9.e+-]+)', bloc)
m_b = re.search(r'ecart relatif : t [0-9.e+-]+ ; Sigma2 ([0-9.e+-]+) ; u ([0-9.e+-]+) ; termes nuls', bloc)
u_sum, u_mat = float(m_u.group(2)), float(m_b.group(2))
ok11 = (nums == ('7.50e-05', '1.84e-05', '4.59e-06', '4.37e-02', '4.40e-04', '4.40e-02') and 3.9 < rap[0] < 4.2 and 3.9 < rap[1] < 4.2 and u_sum < 5.5e-13 and u_mat < 5.5e-15
        and float(nums[4]) < 0.02 * float(nums[3]) and float(nums[5]) > 0.9 * float(nums[3]))
chk('C11', ok11 and not mq, 'nn.6 : l energie contre l energie exacte, lue dans mon journal du bloc : %s ; rapports %.2f et %.2f (quatre par moitie de g) ; le saut au second voisin u retrouve a %.1e '
    '(somme) et %.1e (matrice) ; Sigma2 seul 100 fois plus proche que u seul ; phrases absentes %s' % (nums, rap[0], rap[1], u_sum, u_mat, mq))

# ------------------------------------------------------------------ C12 : nn.7, lectures sans verdict, temoins, bruit
def q2_etats(pid):
    out = []
    for e, m in zip(PT[pid]['etats'], D[pid]['motifs']):
        if m is None:
            out.append(e['chaine2']['gammas_flux'][2] / e['Gamma_2D']['3'])
    return out


w1 = q2_etats('W1')
pal = {}
for k in JUG:
    pal.setdefault(D[k]['pal'], []).append(k)
loi = {k: D[k]['loi'] for k in JUG}
loi_min = min(loi, key=loi.get)
loi_max = max(JUG, key=lambda k: round(loi[k], 3))
fim_k = max(JUG, key=lambda k: D[k]['fim'])
sc = open(os.path.join(SO, 'stabilite_cascade_machine2.log'), encoding='ascii').read()
sb = open(os.path.join(SO, 'sensibilite_bruit_machine2.log'), encoding='ascii').read()
x8 = [l for l in sb.split('\n') if l.startswith('x8 ')][0]
phr = ['Le palier atteint est en nn.4 : 1.25 a huit points juges, les quatre de la bande proche, M1, M2, M3 et L1 ; 1.6 a M4, L2 et L3 ; 2 a L4.',
       'la mediane de q2 / loi va de %.3f (%s) a %.3f (M4 et L3). Elle surestime au point le plus bas, 1.88.' % (loi[loi_min], loi_min, loi[loi_max]),
       'le plus grand ecart relatif entre -2 Im E et Gamma_flux de la chaine d\'ordre 2, a un point juge, est %.3f (%s).' % (D[fim_k]['fim'], fim_k),
       'q2 de %.3f a %.3f a A1, de %.3f a %.3f a A2.' % (D['A1']['q2'][0], D['A1']['q2'][1], D['A2']['q2'][0], D['A2']['q2'][1]),
       'Le temoin W1 (2.14, facteur 1, hors enonce) : %d etats juges, q2 de %.3f a %.3f ; sept sont au-dela de 1.6, deux au-dela de 2 ; aucun palier. Il est MIEUX (%.3f contre %.3f) et tenu en energie (%.4f).' % (
           D['W1']['nj'], min(w1), max(w1), D['W1']['pire'][1], D['W1']['pire'][0], D['W1']['ecart_max']),
       'boite de 89, 1346 secondes sur batterie, et il est NON LISIBLE : 3 etats juges sur 14, les 11 autres sous dix planchers.',
       'au bruit mesure, aucun statut de point ne change et un seul verdict est possible.', 'Un etat de L4 peut entrer ou sortir des etats juges ; le point est TENU dans les deux cas.',
       'Le verdict est inchange jusqu\'a sept fois ce bruit (5.12e-13) ; a partir de huit fois (5.86e-13), NE TIENT PAS, TIENT JUSQU\'A 0.10 et TIENT sont tous possibles.',
       'il ne l\'a pas ete a celles de 73 et 74 (C1, M3, L4)']
mq = manque(phr, AN)
ok12 = (sorted(pal.get(1.25, [])) == sorted(['C1', 'C2', 'C3', 'C4', 'M1', 'M2', 'M3', 'L1']) and sorted(pal.get(1.6, [])) == ['L2', 'L3', 'M4'] and pal.get(2.0) == ['L4'] and D['W1']['pal'] is None
        and len(w1) == 11 and sum(1 for q in w1 if q > 1.6) == 7 and sum(1 for q in w1 if q > 2.0) == 2 and max(w1) < 2.5
        and TAB['C1']['N'] == 73 and TAB['M3']['N'] == 74 and TAB['L4']['N'] == 74 and TAB['A1']['N'] == 60 and TAB['A2']['N'] == 61 and TAB['W2']['N'] == 89
        and 'VERDICT INCHANGE' in sc and 'L4 bande lointaine statut TENU  ; possibles sous le bruit [\'TENU\']               ; 1 etat(s) incertain(s) -> INCHANGE' in sc
        and re.search(r'x7 .*5\.12e-13.*VERDICT INCHANGE', sb) and re.search(r'x8 .*5\.86e-13.*NE TIENT PAS.*TIENT JUSQU\'A 0\.10.*VERDICT PEUT CHANGER', sb) and '7.32e-14' in sb)
chk('C12', ok12 and not mq, 'nn.7 : paliers (1.25 : %s ; 1.6 : %s ; 2 : %s), loi apres coup de %.3f (%s) a %.3f, arithmetique %.3f a %s, ancres, W1 (%d etats, %d au-dela de 1.6, %d au-dela de 2, '
    'plus grand %.3f), W2, boites 73 et 74, mon enumeration sous le bruit (inchange jusqu a sept fois, 5.12e-13 ; peut changer des huit fois) recalcules ; phrases absentes %s' % (
        pal.get(1.25), pal.get(1.6), pal.get(2.0), loi[loi_min], loi_min, loi[loi_max], D[fim_k]['fim'], fim_k, len(w1), sum(1 for q in w1 if q > 1.6), sum(1 for q in w1 if q > 2.0), max(w1), mq))

# ------------------------------------------------------------------ C13 : nn.8, les annonces
rl = open(os.path.join(SO, 'lecture_resultat_machine2.log'), encoding='ascii').read()
mes = []
for ln in rl.split('\n'):
    m = re.match(r'^\s+(A-\d+)b? \((0\.\d+)\) .*? : (VRAIE|FAUSSE)', ln)
    if m:
        mes.append((m.group(1), m.group(2), m.group(3)))
for ln in rl.split('\n'):
    if ln.strip().startswith('A-15'):
        mes = [x for x in mes if x[0] != 'A-15']
        mes += [('A-15', p, 'VRAIE' if v == 'VRAIE' else 'FAUSSE') for p, v in re.findall(r'\((0\.\d+)\) la garde G-\d tient : (VRAIE|FAUSSE)', ln)]
act8 = []
for ln in LIGNES:
    m = re.match(r'^\s+(A-\d+)\s+\((0\.\d+)\) .*?\s(VRAIE|FAUSSE)(\s|$)', ln)
    if m:
        act8.append((m.group(1), m.group(2), m.group(3)))
somme = sum(float(p) for _, p, _ in mes)
nv = sum(1 for x in mes if x[2] == 'VRAIE')
fx = sorted(x[0] for x in mes if x[2] == 'FAUSSE')
pa = re.findall(r"la plume donnait (0\.\d+) a L'ORDRE 2 TIENT, (0\.\d+) a TIENT JUSQU'A 0\.10, (0\.\d+) a TIENT JUSQU'A 0\.06, (0\.\d+) a NE TIENT PAS, (0\.\d+) a NON LISIBLE, (0\.\d+) a NON CONCLUANT", AN)
gel_a1 = re.findall(r"L'ORDRE 2 TIENT (0\.\d+) ; TIENT JUSQU'A 0\.10 (0\.\d+) ; TIENT JUSQU'A 0\.06 (0\.\d+) ; NE TIENT PAS (0\.\d+) ; NON LISIBLE (0\.\d+) ; NON CONCLUANT D'INSTRUMENT (0\.\d+)", GN)
phr = ['A-5  (0.70) L2 est TENU VRAIE (plus petit q2 %.3f)' % D['L2']['q2'][0], 'A-6 (0.65) son plus grand q2 est entre 1.5 et 1.9 VRAIE (%.3f)' % D['L4']['q2'][1],
       'A-7 (0.65) son plus grand q2 est entre 1.35 et 1.55 VRAIE (%.3f)' % D['M4']['q2'][1], 'A-9 (0.70) le plus grand ecart d\'energie est < 0.006 VRAIE (%.4f, a %s)' % (max(D[k]['ecart_max'] for k in JUG), emax['lointaine'][1]),
       'A-10 (0.70) a chaque point le plus petit q2 est >= 0.95 VRAIE (le plus petit : %.3f, a %s)' % (D[qmin_k]['q2'][0], qmin_k),
       'A-11 (0.60) la mediane de q2 / loi est entre 0.93 et 1.15 FAUSSE (%s : %.3f)' % (loi_min, loi[loi_min]), 'A-12 (0.75) W1 a un etat juge hors de 1.6 VRAIE (sept sur onze)',
       'A-12 (0.70) tous ses etats juges sont sous 2.5 VRAIE (le plus grand : %.3f)' % max(w1), 'A-13 (0.65) W2 est joue et lisible FAUSSE (joue, 3 etats juges)',
       'A-14 (0.65) -2 Im E et Gamma_flux a moins de 0.05 VRAIE (le plus grand : %.3f, a %s)' % (D[fim_k]['fim'], fim_k),
       '%d annonces jugees sur %d sont vraies ; les deux fausses sont A-11 (la loi apres coup, a L2) et A-13 (W2 n\'est pas lisible).' % (nv, len(mes)),
       'La somme des probabilites annoncees est %.1f pour %d vraies' % (somme, nv)]
mq = manque(phr, AN)
gel_p = all(('(%s)' % p) in GEL for p in ('0.85', '0.80', '0.60', '0.70', '0.65', '0.90', '0.95', '0.93', '0.97'))
chk('C13', sorted(mes) == sorted(act8) and len(mes) == 20 and nv == 18 and fx == ['A-11', 'A-13'] and abs(somme - 15.2) < 1e-9 and pa and pa == gel_a1 and gel_p and not mq,
    'nn.8 : les %d annonces jugees (identifiant, probabilite, sort) de ma lecture ecrite avant le run == celles de l acte, %d vraies, fausses %s, somme des probabilites %.1f ; '
    'les six probabilites de A-1 de l acte == section 12 du gel ; valeurs entre parentheses recalculees ; absentes %s' % (len(mes), nv, fx, somme, mq))

# ------------------------------------------------------------------ C14 : le registre, les citations, nn.0, nn.9, nn.10, nn.12
head, act97, msg97, jr = 'indisponible', '', '', []
try:
    head = subprocess.run(['git', 'ls-remote', 'https://github.com/lbaaz/SG_1', 'HEAD'], capture_output=True, text=True, timeout=60).stdout.split()[0][:7]
    act97 = subprocess.run(['git', '-C', CLONE, 'show', 'origin/main:journal/journal_delta_97_domaine_G1_chaine_EA_v1.md'], capture_output=True, text=True).stdout
    msg97 = subprocess.run(['git', '-C', CLONE, 'log', '-1', '--format=%B', 'origin/main'], capture_output=True, text=True).stdout
    jr = subprocess.run(['git', '-C', CLONE, 'ls-tree', '--name-only', 'origin/main', 'journal/'], capture_output=True, text=True).stdout.split()
except Exception as ex:
    head = 'indisponible (%s)' % type(ex).__name__
plafond = max([int(m.group(1)) for x in jr for m in [re.match(r'journal/journal_delta_(\d+)_', x)] if m] or [0])
n97 = norm(act97)
note_m1 = norm(''.join(c for c in unicodedata.normalize('NFD', rt(os.path.join(DG, 'note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md'))) if unicodedata.category(c) != 'Mn'))   # la note est accentuee, l acte l est pas
cert_note = norm(rt(os.path.join(ROOT, 'POUR_MACHINE1_certification_gel_ordre2_machine2_v1.md')))
rel = rt(os.path.join(DG, 'releve_gel_ordre2_machine1_v1.log'))
phr = ['Registre a l\'ecriture : origin/main 79e77d2, plafond 97 (releve du 15/11 au matin).',
       'D-O2-2 (m1 ; reserve R-1 de machine 2) : le selftest de la feuille laisse passer 22 des 115 alterations d\'une ligne que machine 2 lui oppose ; son banc en mord 20, les deux dernieres etant equivalentes.',
       'La table est tenue (131 alterations sur 131)', '7.00 pour 6.987 (repris par le gel, section 2 (i)), et 241 etats sur 243 dans un facteur 1.5 pour 242.',
       'Le run le dement : le palier de L4 est 2, son plus grand q2, 1.679, est au-dela de 1.6.', 'W2 a coute 1346 secondes sur batterie pour 3 etats juges.',
       'elle annoncait 0.65 (A-13)', 'la marge d\'un plancher vaut 1.7 fois le bruit qu\'elle mesure sur Gamma_2D(3) ; le verdict, lui, tient jusqu\'a sept fois ce bruit (nn.7).',
       'm2 : six de ses controles ont mordu a ses premiers jets'.replace('m2 : ', 'De machine 2, declares par elle : '),
       'trente-quatre attendent la revue', 'Aucune regle nouvelle']
mq = manque(phr, AN)
survit = re.search(r'survivent au selftest de machine 1 : \[(.*?)\] ; survivent a mon banc : \[(.*?)\] ; survivent aux deux : \[(.*?)\]', bl)
n115 = re.search(r'BILAN : (\d+) alterations', bl)
c14 = {'tete 79e77d2': head == '79e77d2', 'plafond 97': plafond == 97, 'acte 97 : deriver le residuel': 'deriver le residuel' in n97, 'acte 97 : change de sens': 'change de sens' in n97,
       'commit 97 : 32 a 34 sur 31': 'numbered 32 to 34, join the thirty-one' in msg97,
       'banc : 115 alterations': bool(n115) and n115.group(1) == '115', 'banc : 22 survivent au selftest, 2 aux deux': bool(survit) and len(survit.group(1).split(',')) == 22 and len(survit.group(3).split(',')) == 2,
       'releve m1 : table 131 sur 131': 'R14 banc : table 131 sur 131' in rel, 'note m1 : la phrase existe (avec donc)': 'preferent donc la somme des deux termes a chacun pris seul' in note_m1,
       'ma note : 0.2 a 0.3 pour cent': '0.2 a 0.3 pour cent' in cert_note, 'ma note : 7.00 contre 6.987': '7.00 contre 6.987' in cert_note, 'ma note : 241 contre 242': '241 contre 242' in cert_note,
       'ma note : six controles': 'Six de mes controles ont mordu' in cert_note, 'ma note : 1.7 fois': '1.7 fois le bruit' in cert_note,
       'gel (iii) : 0.85 et 1.6': bool(re.search(r"\(iii\) La plume a ecrit a l'operateur, AVANT de calculer la grille de ce gel, qu'elle donnait 0\.85 .*?1\.6", GN)),
       'gel A-13 0.65': 'A-13 (0.65) W2 est joue et lisible' in GN}
ok14 = all(c14.values())
faux14 = [k for k, v in c14.items() if not v]
chk('C14', ok14 and not mq, 'nn.0, nn.9, nn.10, nn.12 : tete publique du registre %s, plafond %d (journaux au registre) ; l acte 97 au registre porte "deriver le residuel" et "change de sens" ; '
    'message du commit 97 : regles 32 a 34 sur 31, soit 34 ; mon banc : 115 alterations, 22 survivent au selftest de machine 1, 2 aux deux (donc 20 mordues par mon banc) ; releve de machine 1 : "table 131 sur 131" ; '
    'la note de machine 1 porte la phrase des energies ; ma note de certification dit 0.2 a 0.3 pour cent, 7.00 contre 6.987, 241 contre 242, six controles, 1.7 fois ; le gel (iii) dit 0.85 et 1.6 ; '
    'conditions fausses %s ; phrases absentes %s' % (head, plafond, faux14, mq))

# ------------------------------------------------------------------ C15 : nn.13, nn.15, nn.12 (les trois regles), les lots cites
noms15 = ['journal_delta_nn_ordre2_chaine_EA_v1.md', 'ecrire_acte_ordre2_machine1_v1.py', 'verdict_rejoue_machine1.json', 'lecture_rejouee_machine1.log',
          'releve_acte_ordre2_machine1_v1.py', 'releve_acte_ordre2_machine1_v1.log', 'contre_epreuve_releve_acte_ordre2_machine1_v1.py', 'contre_epreuve_releve_acte_ordre2_machine1_v1.log',
          'POUR_MACHINE2_acte_ordre2_machine1_v1.md', 'fabrique_lot_machine1_v2.py']
manifs = re.findall(r'^[0-9a-f]{16}\s+[0-9a-f]{16}\s+\d+\s+\d+\s+(\S+)$', man.decode('utf-8'), re.M)
absents = [n for n in noms15 if n not in manifs or (n not in AN and not (n.endswith('.log') and n[:-4] + '.py / .log' in AN))]
rel_m1 = zl.read('releve_acte_ordre2_machine1_v1.log').decode('utf-8')
cer_m1 = zl.read('contre_epreuve_releve_acte_ordre2_machine1_v1.log').decode('utf-8')
phr = ['(a) le selftest porte sa propre copie de la table : la table est tenue (131 sur 131), le reste du selftest ne l\'est pas (D-O2-2)',
       '(b) la borne porte une marge d\'un plancher et la lecture sans marge est rendue : ici la marge n\'a garde aucun etat, et machine 2 mesure que le verdict tient jusqu\'a sept fois le bruit.',
       '(c) la tete du registre a ete relevee, et le gel n\'a rien cite a tort hors registre ; mais la plume a encore conseille un gel avec un chiffre avant de calculer (D-O2-1).',
       'machine 1 -- le gel et ses instruments 3bc363266957de56 ; machine 2 -- la certification 59a583a640112891, le resultat 6dfdfe8fd0b8eaad.']
mq = manque(phr, AN)
lots_ok = (emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine2_certification_gel_ordre2_chaine_EA_v1.txt')))[0] == '59a583a640112891'
           and emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine2_resultat_ordre2_chaine_EA_v1.txt')))[0] == '6dfdfe8fd0b8eaad'
           and emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine1_gel_ordre2_chaine_EA_v1.txt')))[0] == '3bc363266957de56')
chk('C15', not absents and sorted(manifs) == sorted(noms15) and not mq and lots_ok,
    'nn.15 : les 10 pieces nommees == les 10 lignes du manifeste ; nn.13 : les canons des trois lots cites, recalcules de leurs manifestes : %s ; nn.12 : les trois regles candidates du delta 97, appliquees '
    'sans etre adoptees ; absents %s %s' % (lots_ok, absents, mq))
# ------------------------------------------------------------------ C16 : les citations entre guillemets de l'acte, comparees mot pour mot aux pieces citees
cite = 'preferent la somme des deux termes a chacun pris seul'
verbatim = cite in note_m1
m_ctx = re.search(r'Les energies (\w+ )?preferent (donc )?la somme des deux termes a chacun pris seul', note_m1)
chk('C16', verbatim, 'nn.9 D-O2-5 : la citation de la note de machine 1, entre guillemets dans l acte ("%s"), est-elle MOT POUR MOT dans la note ? %s ; la note ecrit : "%s"' % (
    cite, 'oui' if verbatim else 'NON', m_ctx.group(0) if m_ctx else 'phrase introuvable'))
info('journaux de machine 1, lus et non rejoues : releve "%s" ; contre-epreuve "%s"' % (rel_m1.strip().split('\n')[-1][:100], cer_m1.strip().split('\n')[-1][:120]))
info('NON VERIFIABLE par machine 2 (attestations de machine 1 ou de l operateur) : (a) nn.0 et nn.11 (ii), l ouverture du chantier, "ok go", 14/11 a 22 h 04 ; (b) nn.2, machine 1 n a joue la sonde '
     'a aucun point juge ni temoin ; (c) nn.9 D-O2-1, ce que la plume a ecrit a l operateur avant la grille (0.85) ; (d) nn.9 D-O2-3, la raison pour laquelle la plume a estime W2 lisible')
mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'acte': ACTE_NOM, 'canon': c_act, 'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}},
          open(JSN, 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
