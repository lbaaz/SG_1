# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' du run du gel "la garde G-1 du moteur et la chaine E-A par etat" (journal_delta_nn_domaine_G1_chaine_EA_v1.md,
canon e718d2db619af9b1, projet version 1, lot bf07ec23b0209ffc), 2026-11-14. Chaque affirmation CHIFFREE de l'acte est RECALCULEE ici depuis MES sources (le JSON de
la sonde et le verdict de la feuille rendus par MON run, mes journaux de garde, de banc, de bruit et de certification, le registre public), jamais lue dans le
script d'ecriture ni dans le releve de machine 1. Les phrases attendues sont CONSTRUITES depuis les donnees puis cherchees dans l'acte (blancs normalises) : un
nombre tape a la main et faux est une morsure.
Usage (depuis BOCAL4) : python -P acte_domaine_contreseing/verification_acte_domaine_G1_machine2_v1.py
Variables : LOT_ALT (contre-epreuve sur une copie mutee du lot), SUFFIXE_SORTIE. Ce script ne modifie rien d'autre que ses deux sorties."""
import hashlib
import io
import json
import os
import re
import statistics
import subprocess
import sys
import unicodedata
import zipfile
from fractions import Fraction as F

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DG = os.path.join(ROOT, 'domaine_G1')
SO = os.path.join(DG, 'sortie')
OLD = os.path.join(ROOT, 'chaine_EA_par_etat')
ACTE_NOM = 'journal_delta_nn_domaine_G1_chaine_EA_v1.md'
LOT = os.environ.get('LOT_ALT', 'lot_machine1_2026-11-14_acte_domaine_G1_chaine_EA_v1_recu.zip')
SUFFIXE = os.environ.get('SUFFIXE_SORTIE', '')
MANIF = 'MANIFEST_lot_machine1_acte_domaine_G1_chaine_EA_v1.txt'
LOG = os.path.join(HERE, 'verification_acte_domaine_G1_machine2_v1%s.log' % SUFFIXE)
JSN = os.path.join(HERE, 'verification_acte_domaine_G1_machine2_v1%s.json' % SUFFIXE)
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
chk('C01', c_act == 'e718d2db619af9b1' and len(RAW) == 20265 and len(LIGNES) - 1 == 292
    and ACTE.startswith('DELTA nn -- LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT : RUN DU 14/11/2026 SOUS LE GEL\nb59651f99e60707a.')
    and '-- PROJET, VERSION 1' in ACTE and ACTE.rstrip().endswith('-- FIN journal_delta_nn_domaine_G1_chaine_EA_v1 --'),
    'acte : canon %s (annonce e718d2db619af9b1), %d octets (20265), %d lignes (292), en-tete et ligne de FIN, VERSION 1' % (c_act, len(RAW), len(LIGNES) - 1))
man = rd(os.path.join(ROOT, MANIF))
bad, n_l = [], 0
for ln in man.decode('utf-8').split('\n'):
    p = ln.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        n_l += 1
        if emp(zl.read(p[4])) != (p[0], p[1], int(p[2]), int(p[3])):
            bad.append(p[4])
canon_lot = emp(man)[0]
chk('C02', n_l == 10 and not bad and len([n for n in zl.namelist() if not n.startswith('MANIFEST_')]) == 10 and canon_lot == 'bf07ec23b0209ffc',
    '%d pieces sur 10 au canon, a l empreinte brute et aux deux tailles ; ecarts %s ; CANON DU LOT %s (annonce bf07ec23b0209ffc)' % (n_l, bad, canon_lot))
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
CLONE = os.environ.get('REGISTRE_CLONE', os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', 'claude', '75adcc7f3c1d08bf', '7d33635e-8345-4a2c-a69e-f6a51f9d8fa7', 'scratchpad', 'reg_verif'))
n_reg = 0
try:                                                       # les fichiers du registre public (clone frais), indexes sous leur chemin au registre
    for f in subprocess.run(['git', '-C', CLONE, 'ls-files'], capture_output=True, text=True, timeout=120).stdout.splitlines():
        if f:
            ajoute(emp(rd(os.path.join(CLONE, f)))[0], 'registre:' + f)
            n_reg += 1
except Exception:
    pass
info('index : %d fichiers, %d empreintes distinctes (fichiers et membres de zip), dont %d fichiers du registre public' % (n_f, len(IDX), n_reg))

paires = sorted(set(re.findall(r'^\s+([\w./-]+\.(?:py|md|json|log|txt))\s+([0-9a-f]{16})\s*$', ACTE, re.M)))
non_res, mauvais_nom = [], []
for nom, c in paires:
    if c not in IDX:
        non_res.append((nom, c))
    elif not any(re.split(r'[/!:]', x)[-1] == nom.split('/')[-1] for x in IDX[c]):
        mauvais_nom.append((nom, c))
chk('C04', len(paires) >= 18 and not non_res and not mauvais_nom,
    'nn.1 : %d couples (nom, canon) lus dans l acte, tous retrouves chez moi, le nom est celui d une piece de ce canon ; non resolus %s ; noms differents %s' % (
        len(paires), non_res, mauvais_nom))
tous = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', ACTE)))
non_res_tous = [c for c in tous if c not in IDX]
chk('C05', len(tous) >= 20 and not non_res_tous,
    '%d empreintes de 16 chiffres citees dans tout l acte, toutes recalculees de pieces ou de manifestes que je detiens ; non resolues %s' % (len(tous), non_res_tous))

# ------------------------------------------------------------------ donnees de MON run
S = json.load(open(os.path.join(SO, 'sonde_domaine_G1.json'), encoding='ascii'))
V = json.load(open(os.path.join(SO, 'verdict_domaine_G1.json'), encoding='ascii'))
PT = {x['id']: x for x in V['points']}
ORDRE = [p['id'] for p in S['points']]
V_OLD = json.load(open(os.path.join(OLD, 'sortie', 'verdict_chaine_par_etat.json'), encoding='ascii'))
PO = {x['id']: x for x in V_OLD['points']}
GEL = open(os.path.join(DG, 'gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md'), encoding='ascii').read()
TAB = {}
for m in re.finditer(r'^\s+(E\d|H\d|A\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)\s+D1 ([0-9.]+)\s+c_max ([0-9.]+)\s+N (\d+)$', GEL, re.M):
    TAB[m.group(1)] = (m.group(2), m.group(3) if '/' in m.group(3) else m.group(3) + '/1', float(m.group(4)), float(m.group(5)))


def W2(k):
    return float(F(TAB[k][0]))


def FACT(k):
    return float(F(TAB[k][1]))


def palier(q):
    return 'FACTEUR 2' if 0.5 <= q <= 2.0 else ('DECADE' if 0.1 <= q * q <= 10.0 else 'HORS DECADE')


R10 = 10 ** 0.5
D = {}
ecart_q, n_jug = 0.0, 0
for pid in ORDRE:
    x = PT[pid]
    jug = [e for e in x['etats'] if e['exclu'] is None]
    qs = [e['Gamma_chaine'] / e['Gamma_2D'] for e in jug]
    for e, q in zip(jug, qs):
        ecart_q = max(ecart_q, abs(q / e['q'] - 1))
    n_jug += len(jug)
    st = max((palier(q) for q in qs), key=lambda s: ['FACTEUR 2', 'DECADE', 'HORS DECADE'].index(s))
    ex = {}
    for e in x['etats']:
        if e['exclu']:
            ex[e['exclu']] = ex.get(e['exclu'], 0) + 1
    D[pid] = {'role': x['role'], 'w2': x['w2'], 'g': x['facteur'], 'statut_f': x['statut'], 'statut': st, 'n': len(jug), 'qs': qs, 'qmin': min(qs), 'qmax': max(qs),
              'med': statistics.median(qs), 'prem': (jug[0]['n1'], jug[0]['n2'], qs[0]), 'ex': ex, 'etats': jug,
              'classe': 'TOMBE' if st == 'HORS DECADE' else 'TENU'}
chk('C06', ecart_q < 1e-12 and all(D[p]['statut'] == D[p]['statut_f'] for p in ORDRE) and n_jug == 154 and sum(len(PT[p]['etats']) for p in ORDRE) == 196
    and V['verdict'] == 'LA GARDE NE TIENT PAS' and V['a_EN_tombes'] == 3 and V['b_HORS_tenus'] == 3 and V['rivale'] == 'NON TENUE',
    'mon recalcul de q = Gamma_chaine / Gamma_2D(3) sur le verdict de mon run : ecart relatif max %.1e ; les quatorze statuts == ceux de la feuille ; %d etats juges sur 196 ; '
    'verdict %s, a %d, b %d, rivale %s' % (ecart_q, n_jug, V['verdict'], V['a_EN_tombes'], V['b_HORS_tenus'], V['rivale']))

# ------------------------------------------------------------------ C07 : le verdict rejoue, les journaux
mon_v = rd(os.path.join(SO, 'verdict_domaine_G1.json')).replace(b'\r\n', b'\n')
v_m1 = zl.read('verdict_rejoue_machine1.json')
l_m1 = zl.read('lecture_rejouee_machine1.log').decode('utf-8').split('\n')
l_m2 = open(os.path.join(SO, 'lecture_domaine_G1.log'), encoding='utf-8').read().split('\n')
diff = [(a, b) for a, b in zip(l_m1, l_m2) if a != b]
chk('C07', emp(rd(os.path.join(SO, 'verdict_domaine_G1.json')))[0] == '955c4ee53bc2e5d5' == emp(v_m1)[0] and mon_v == v_m1 and len(l_m1) == len(l_m2) and len(diff) == 1
    and diff[0][0].startswith('LECTURE DU GEL') and 'SELFTEST : 74 cas, 74 tenus' in l_m1
    and emp(rd(os.path.join(SO, 'lecture_domaine_G1.log')))[0] == '1ee031ea89823525' and emp(zl.read('lecture_rejouee_machine1.log'))[0] == '31aa65c9983b79a4',
    'verdict de mon run == verdict rejoue par machine 1, octet pour octet apres CRLF -> LF (mes octets bruts %d, les siens %d), canon 955c4ee53bc2e5d5 ; journaux : %d lignes de '
    'part et d autre, %d ligne qui differe (le titre) ; canons des deux journaux 1ee031ea89823525 et 31aa65c9983b79a4' % (
        len(rd(os.path.join(SO, 'verdict_domaine_G1.json'))), len(v_m1), len(l_m1), len(diff)))

# ------------------------------------------------------------------ C08 : nn.2, ce que j'ai joue (mes journaux)
cj = json.load(open(os.path.join(DG, 'controles_gel_domaine_G1_machine2_v1.json'), encoding='ascii'))
bl = open(os.path.join(DG, 'banc_feuille_domaine_G1_machine2_v1.log'), encoding='ascii').read()
mb = re.search(r'BILAN : (\d+) alterations ; motifs absents \[\] ; survivent au selftest de machine 1 : \[(.*?)\] ; survivent a mon banc : \[(.*?)\] ; survivent aux deux', bl)
ctl = open(os.path.join(DG, 'controles_gel_domaine_G1_machine2_v1.log'), encoding='ascii').read()
con = open(os.path.join(SO, 'console_domaine_G1.log'), encoding='utf-8').read()
cmp_ = open(os.path.join(SO, 'compare_run_essai_ancres_machine2.log'), encoding='ascii').read()
pf = S['plateforme']
note_res = norm(open(os.path.join(ROOT, 'POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md'), encoding='ascii').read())
ok8 = (cj['bilan']['controles'] == 11 and cj['bilan']['mord'] == 0 and mb and mb.group(1) == '59' and len(mb.group(2).split(',')) == 9 and mb.group(3) == '15'
       and '531441' in ctl and re.search(r'4000 sondes synthetiques.*', bl) and 'ecarts feuille / lecteur : 0' in bl and 'BILAN : 28 etats, 0 etiquettes differentes' in cmp_
       and '2026-11-14 18:59:46 LANCEMENT DE LA SONDE' in con and '19:50:14 FIN DE LA SONDE code=0 duree=3028 s' in con and '19:50:14 FIN DE LA FEUILLE code=0' in con
       and pf['systeme'] == 'Windows' and pf['machine'] == 'AMD64' and pf['python'] == '3.11.9' and pf['numpy'] == '2.2.6' and pf['coeurs'] == 16
       and all(v is None for v in pf['fils'].values()) and pf['temoin_arrondi'] == '0x1.a483018a169c6p+64'
       and '70 pour cent en decharge' in note_res and '2516 MHz pour un maximum de 3801' in note_res)
phr = ['11 controles de lecture du gel, 0 morsure ; la garde du moteur et la boite recalculees aux quatorze points, egales a la table du gel a six decimales, et la garde identique au bit a 16 fils et a 1 fil',
       'la cascade enumeree sur les 531441 vecteurs de classes des douze points', '59 alterations d\'une ligne de la feuille, dont 9 survivent au selftest de la feuille et une seule a son banc (equivalente en pratique)',
       'l\'essai aux deux ancres rejoue, 28 etats au bit', 'BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs, variables de fils non fixees ; le 14/11 de 18:59:46 a 19:50:14 ; sonde code 0 en 3028 s,',
       'feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point rejoue. Temoin d\'arrondi 0x1.a483018a169c6p+64.',
       'Le run a ete joue sur batterie (70 pour cent en decharge a 19:45, processeur a 2516 MHz pour un maximum de 3801)', 'chaque point dure de 1.5 a 1.6 fois un point de meme boite du run precedent, d\'ou 3028 s contre l\'ordre de 2000 s']
mq = manque(phr, AN)
chk('C08', ok8 and not mq, 'nn.2 : mes journaux de certification (11 controles / 0 mordent ; 4000 sondes / 0 ecart ; 531441 ; 59 alterations, 9 au selftest, [15] a mon banc ; 28 etats des ancres) '
    'et du run (heures, code, duree, plateforme, temoin ; batterie et frequence, tels que ma note les dit) == l acte ; phrases absentes %s' % mq)
info('la batterie (70 pour cent, en decharge) et la frequence (2516 / 3801 MHz) ne sont dans aucune PIECE de mes lots : elles sont dans ma note du resultat, qui les tient d une interrogation de Windows faite pendant le run ; l acte les reprend de ma note')

# ------------------------------------------------------------------ C09 : nn.3, les gardes
dmax = max(abs(p['garde_moteur']['D1'] - TAB[p['id']][2]) for p in S['points'])
cmax_ = max(abs(p['garde_moteur']['c_max'] - TAB[p['id']][3]) for p in S['points'])
phr = ['G-3 chacun porte 14 etats (196).', 'et ses D1 et c_max sont ceux de la table a moins de 5e-7 pres (tolerance du gel : 5e-5). Aucune garde ne mord.',
       'G-4 les deux ancres rendent la lecture du run de M17 avec un ecart relatif NUL sur BOCAL4 (etat (7,2) a A1, etat (8,2) a A2).']
mq = manque(phr, AN)
refs = {'A1': ((7, 2), 2.1623273017950654e-10), 'A2': ((8, 2), 2.6613925716641374e-09)}
ancre_ok = all([e for e in p['etats'] if (e['n1'], e['n2']) == refs[p['id']][0]][0]['Gamma_2D']['3'] == refs[p['id']][1] for p in S['points'] if p['id'] in refs)
stat_ok = all(p['garde_moteur']['statut'] == ('EN DOMAINE' if p['id'][0] in 'EA' else 'HORS DOMAINE') for p in S['points'])
chk('C09', dmax < 5e-7 and cmax_ < 5e-7 and V['motifs'] == [] and ancre_ok and stat_ok and not mq,
    'nn.3 : ecart maximal de D1 %.2e et de c_max %.2e entre la garde consignee dans mon JSON et la table du gel (< 5e-7) ; motifs de la feuille %s ; ancres au bit des lectures de M17 : %s ; '
    'statut de la garde a chaque point == la table : %s ; phrases absentes %s' % (dmax, cmax_, V['motifs'], ancre_ok, stat_ok, mq))

# ------------------------------------------------------------------ C10 : nn.4, le tableau et les exclusions
manq, manq_ex = [], []
for pid in ORDRE:
    d = D[pid]
    f = TAB[pid][1]
    gard = 'EN' if (pid[0] in 'EA') else 'HORS'
    cl = '(ancre)' if pid[0] == 'A' else d['classe']
    row = '%s %s %.2f %s %s %s %d %.3f %.3f %.3f (%d,%d) q = %.3f' % (pid, gard, W2(pid), 'x1' if f == '1/1' else 'x' + f, d['statut'], cl, d['n'], d['qmin'], d['qmax'], d['med'],
                                                                   d['prem'][0], d['prem'][1], d['prem'][2])
    if norm(row) not in AN:
        manq.append(row)
    txt = ' ; '.join('%s %d' % (m, d['ex'][m]) for m in sorted(d['ex'])) if d['ex'] else 'aucun'
    if norm('%s %s' % (pid, txt)) not in AN:
        manq_ex.append('%s %s' % (pid, txt))
chk('C10', not manq and not manq_ex and '154 etats juges sur 196' in AN,
    'nn.4 : les 14 lignes du tableau et les 14 lignes d exclusion (premier motif) recalculees de mon verdict ; absentes %s %s ; 154 etats juges sur 196 : %s' % (manq, manq_ex, '154 etats juges sur 196' in AN))


# ------------------------------------------------------------------ C11 : nn.5, les comptes par point
def hors_dd(pid):
    return sum(1 for q in D[pid]['qs'] if not (0.1 <= q * q <= 10.0))


m2 = (max(D['E2']['qs']) / R10 - 1) * 100
m3 = (max(D['E3']['qs']) / R10 - 1) * 100
m4 = (min(D['E4']['qs']) / R10 - 1) * 100
phr = ['E2 (2.09, facteur 1) : la chaine surestime la lecture d\'un facteur %.3f a %.3f sur ses %d etats juges, dont %d hors de la demi-decade ; le plus grand q depasse la borne de %.1f pour cent.' % (
           D['E2']['qmin'], D['E2']['qmax'], D['E2']['n'], hors_dd('E2'), m2),
       'E3 (2.10, facteur 3/2) : de %.3f a %.3f, %d etats sur %d hors de la demi-decade, le plus grand la depassant de %.1f pour cent.' % (D['E3']['qmin'], D['E3']['qmax'], hors_dd('E3'), D['E3']['n'], m3),
       'E4 (2.12, facteur 3/2) : de %.3f a %.3f, les %d etats juges hors de la demi-decade, le plus petit la depassant de %.1f pour cent.' % (D['E4']['qmin'], D['E4']['qmax'], hors_dd('E4'), m4),
       'E1 (2.08, facteur 1) est DECADE : q de %.3f a %.3f, %d etats juges sur %d au-dessus de 2.' % (D['E1']['qmin'], D['E1']['qmax'], sum(1 for q in D['E1']['qs'] if q > 2.0), D['E1']['n']),
       'H4 (1.91, facteur 2/3) est DECADE : q de %.3f a %.3f, %d etats juges sur %d sous 1/2.' % (D['H4']['qmin'], D['H4']['qmax'], sum(1 for q in D['H4']['qs'] if q < 0.5), D['H4']['n']),
       'H5 (1.90, facteur 2/3) est FACTEUR 2 avec %d etats juges, le minimum du gel.' % D['H5']['n'],
       'tous leurs etats juges sont hors de la demi-decade (%d et %d)' % (hors_dd('H2'), hors_dd('H3')),
       'a = 3 : E2, E3 et E4, EN DOMAINE, sont TOMBES. b = 3 : H4, H5 et H6, HORS DOMAINE, sont TENUS.']
mq = manque(phr, AN)
ok11 = (hors_dd('H2') == D['H2']['n'] and hors_dd('H3') == D['H3']['n'] and hors_dd('E4') == D['E4']['n'] and hors_dd('H1') == 1 and D['H1']['statut'] == 'HORS DECADE'
        and sorted(k for k in D if D[k]['role'] == 'juge' and D[k]['classe'] == 'TOMBE' and k[0] == 'E') == ['E2', 'E3', 'E4']
        and sorted(k for k in D if D[k]['role'] == 'juge' and D[k]['classe'] == 'TENU' and k[0] == 'H') == ['H4', 'H5', 'H6'])
chk('C11', ok11 and not mq, 'nn.5 : comptes par point recalcules de mon verdict (etats hors de la demi-decade, marges %.1f, %.1f et %.1f pour cent, etats au-dessus de 2 a E1, sous 1/2 a H4, '
    'minimum de H5) ; phrases absentes %s' % (m2, m3, m4, mq))

# ------------------------------------------------------------------ C12 : nn.6, la rivale
e1 = [e for e in D['H1']['etats'] if (e['n1'], e['n2']) == (11, 2)][0]
q1 = e1['Gamma_chaine'] / e1['Gamma_2D']
rb = 7.32e-14 / e1['Gamma_2D']
PAIRES = {'P1': ('E1', 'H1', '2.08'), 'P2': ('E3', 'H2', '2.10'), 'P3': ('E4', 'H3', '2.12'), 'P4': ('E5', 'H4', '1.91'), 'P5': ('E6', 'H5', '1.90')}


def FAC2(k):
    return 'facteur 1' if TAB[k][1] == '1/1' else 'facteur ' + TAB[k][1]


manq = []
for nom, (a, b, w) in PAIRES.items():
    lect = 'HETEROGENE' if D[a]['classe'] != D[b]['classe'] else 'HOMOGENE'
    row = '%s %s %s %s %.3f %s %s %.3f %s' % (nom, w, a, FAC2(a), D[a]['med'], b, FAC2(b), D[b]['med'], lect)
    if norm(row) not in AN:
        manq.append(row)
loin = True
for a, b, w in PAIRES.values():
    petit = min((a, b), key=FACT)
    loin = loin and abs(D[petit]['med'] - 1) == max(abs(D[a]['med'] - 1), abs(D[b]['med'] - 1))
med_old = {k: PO[k]['q_median'] for k in ('J2', 'J4', 'A2', 'J6')}
r205 = med_old['J6'] / med_old['J4']
r210 = D['H2']['med'] / D['E3']['med']
sc = open(os.path.join(SO, 'stabilite_cascade_machine2.log'), encoding='ascii').read()
phr = ['H1 tombe par un seul de ses 8 etats juges : rang 1, etiquette (11,2), Gamma_2D(3) = %.2e, q = %.4f, a %.2f pour cent au-dessus de la borne de la demi-decade (3.1623).' % (
           e1['Gamma_2D'], q1, (q1 / R10 - 1) * 100),
       'Le bruit des fils sur la cible, 7.32e-14 en absolu, vaut %.1f pour cent de cette lecture' % (rb * 100),
       'A 2.10 le run precedent avait lu %.3f a facteur 1 (J2) : ce w2 porte donc trois facteurs, %.3f (3/2), %.3f (1) et %.3f (2/3).' % (med_old['J2'], D['E3']['med'], med_old['J2'], D['H2']['med']),
       'A 2.05 il avait lu %.3f (3/2), %.3f (1) et %.3f (2/3).' % (med_old['J4'], med_old['A2'], med_old['J6']),
       'le rapport des q medians vaut %.2f a 2.05 et %.2f a 2.10' % (r205, r210),
       'Si cet etat passait sous la borne, H1 serait DECADE, P1 HOMOGENE, et la rivale TENUE.']
mq = manque(phr, AN)
chk('C12', not manq and not mq and loin and 'VERDICT INCHANGE ; RIVALE PEUT CHANGER' in sc and "'P1': ['HETEROGENE', 'HOMOGENE']" in sc
    and "E2 juge  classe TOMBE ; possibles sous le bruit ['TOMBE']              ; 0 etat(s) incertain(s)" in sc and e1['rang'] == 1 and q1 > R10 and D['H1']['n'] == 8,
    'nn.6 : l etat de H1 (rang %d, (11,2), Gamma_2D(3) %.3e, q %.4f, %.2f pour cent au-dessus de la borne, bruit relatif %.1f pour cent) ; les cinq lignes de paires (q medians, lecture) ; '
    '"le point au plus petit facteur a le q median le plus loin de 1" aux cinq paires : %s ; rapports %.3f et %.3f ; mon enumeration sous bruit (verdict inchange, rivale peut changer, '
    'E2 E3 E4 sans etat incertain) ; absentes %s %s' % (e1['rang'], e1['Gamma_2D'], q1, (q1 / R10 - 1) * 100, rb * 100, loin, r205, r210, manq, mq))

# ------------------------------------------------------------------ C13 : nn.7
au_dessous = [k for k in D if D[k]['role'] == 'juge' and W2(k) < 2]
au_dessus = [k for k in D if D[k]['role'] == 'juge' and W2(k) > 2]
ok_sens = all((W2(k) < 2) == (D[k]['med'] < 1) for k in D)
sb = open(os.path.join(SO, 'stabilite_sous_bruit_machine2.log'), encoding='ascii').read()
n_inch = sum(1 for k in ORDRE if re.search(r'^%s .*-> INCHANGE$' % k, sb, re.M))
phr = ['Au-dessous, les cinq points juges (E5, E6, H4, H5, H6) sont TENUS', 'Au-dessus, des sept points juges un seul est TENU, E1, et il est DECADE.',
       'Aux quatorze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 > 2.',
       'ecarte de 5 a 7 etats sur 14 (H1 %d, H2 %d, H4 %d, H5 %d)' % tuple(D[k]['ex'].get('sous dix planchers', 0) for k in ('H1', 'H2', 'H4', 'H5')),
       'H5 n\'a que 6 etats juges', 'Le bruit relatif maximal sur les 154 etats juges est 5.5 pour cent, a E6 rang 8, sans effet sur une classe.',
       'les statuts de onze points juges sur douze et des deux ancres ne changent ni dans le pire ni dans le meilleur sens ; le douzieme est H1',
       'q de 0.587 a 0.882 a A1, de 1.292 a 1.629 a A2']
mq = manque(phr, AN)
anc_old = (round(PO['A1']['q_min'], 3), round(PO['A1']['q_max'], 3), round(PO['A2']['q_min'], 3), round(PO['A2']['q_max'], 3))
chk('C13', sorted(k for k in au_dessous if D[k]['classe'] == 'TENU') == sorted(au_dessous) and len(au_dessous) == 5 and len(au_dessus) == 7
    and [k for k in au_dessus if D[k]['classe'] == 'TENU'] == ['E1'] and D['E1']['statut'] == 'DECADE' and ok_sens and n_inch == 13 and re.search(r'^H1 juge\s+statut HORS DECADE', sb, re.M)
    and '154 etats juges' in sb and '5.47e-02' in sb and "('E6', 8)" in sb and not mq and anc_old == (0.587, 0.882, 1.292, 1.629),
    'nn.7 : cinq points juges au-dessous de 2.00, tous TENUS ; sept au-dessus, un seul TENU (E1, DECADE) ; le signe des q medians aux 14 points ; les exclus a facteur 2/3 ; mon journal de bruit '
    '(%d statuts inchanges sur 14, H1 excepte ; 154 etats ; 5.47e-02 a E6 rang 8) ; les ancres == celles du run precedent ; phrases absentes %s' % (n_inch, mq))

# ------------------------------------------------------------------ C14 : nn.8, les annonces
rl = open(os.path.join(SO, 'lecture_resultat_machine2.log'), encoding='ascii').read()
lig = ['A-1 (0.74) le verdict est LA GARDE NE TIENT PAS REALISEE', 'A-2 (0.75) E3 est HORS DECADE VRAIE', 'A-3 (0.85) E4 est HORS DECADE VRAIE', 'A-4 (0.55) E2 est HORS DECADE VRAIE',
       'A-5 (0.75) E1 est DECADE VRAIE', 'A-6 (0.70) H1 est TENU FAUSSE (HORS DECADE, par un etat)', 'A-7 (0.75) H6 est TENU VRAIE', 'A-8 (0.40) la rivale est TENUE FAUSSE (NON TENUE, par un etat)',
       'A-9 (0.60) a E3, le q median entre 3.0 et 4.5 FAUSSE (%.3f)' % D['E3']['med'], 'A-10 (0.80) E5 et E6 tous les deux TENUS VRAIE', 'A-11 (0.50) H4 ou H5, l\'un au moins, HORS DECADE FAUSSE (DECADE et FACTEUR 2)',
       'A-12 (0.85) signe du q median aux points juges lisibles VRAIE', 'A-13 (0.95) la garde G-4 tient ; (0.97) la garde G-6 tient VRAIES', 'Neuf sur treize, comme machine 2 les compte.']
sens = {'A-1': True, 'A-2': D['E3']['statut'] == 'HORS DECADE', 'A-3': D['E4']['statut'] == 'HORS DECADE', 'A-4': D['E2']['statut'] == 'HORS DECADE', 'A-5': D['E1']['statut'] == 'DECADE',
        'A-6': D['H1']['classe'] == 'TENU', 'A-7': D['H6']['classe'] == 'TENU', 'A-8': V['rivale'] == 'TENUE', 'A-9': 3.0 <= D['E3']['med'] <= 4.5,
        'A-10': D['E5']['classe'] == 'TENU' and D['E6']['classe'] == 'TENU', 'A-11': 'HORS DECADE' in (D['H4']['statut'], D['H5']['statut']), 'A-12': ok_sens, 'A-13': V['motifs'] == []}
mq = manque(lig, AN)
gn = norm(GEL)
gel_ok = all(('A-%d' % n) in GEL for n in range(1, 14)) and 'LA GARDE NE TIENT PAS 0.74' in gn and all(('(%s)' % p) in GEL for p in ('0.75', '0.85', '0.55', '0.70', '0.40', '0.60', '0.80', '0.50', '0.95', '0.97'))
chk('C14', not mq and gel_ok and sum(1 for v in sens.values() if v) == 9 and [k for k, v in sens.items() if not v] == ['A-6', 'A-8', 'A-9', 'A-11']
    and 'A-6 (0.70) H1 est TENU : FAUSSE' in rl and 'BILAN DE MA LECTURE : 0 ecart(s)' in rl,
    'nn.8 : probabilites et intervalles des annonces == section 11 de mon exemplaire du gel : %s ; sort de chacune recalcule de mon verdict, %d vraies sur 13, fausses %s ; lignes absentes %s' % (
        gel_ok, sum(1 for v in sens.values() if v), [k for k, v in sens.items() if not v], mq))

# ------------------------------------------------------------------ C15 : nn.0, nn.9, nn.10, nn.12 : le registre, les dates, les citations
CL = os.environ.get('REGISTRE_CLONE', os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', 'claude', '75adcc7f3c1d08bf', '7d33635e-8345-4a2c-a69e-f6a51f9d8fa7', 'scratchpad', 'reg_verif'))
dates = {}
try:
    subprocess.run(['git', '-C', CL, 'fetch', '-q', 'origin'], capture_output=True, text=True, timeout=120)
    for h in ('3c26420', '04053e0'):
        dates[h] = subprocess.run(['git', '-C', CL, 'log', '-1', '--format=%ad|%s', '--date=format:%Y-%m-%d %H:%M', h], capture_output=True, text=True).stdout.strip()
    head = subprocess.run(['git', 'ls-remote', 'https://github.com/lbaaz/SG_1', 'HEAD'], capture_output=True, text=True, timeout=60).stdout.split()[0][:7]
    act96 = subprocess.run(['git', '-C', CL, 'show', 'origin/main:journal/journal_delta_96_chaine_EA_par_etat_v1.md'], capture_output=True, text=True).stdout
    msg96 = subprocess.run(['git', '-C', CL, 'log', '-1', '--format=%B', '04053e0'], capture_output=True, text=True).stdout
    msg95 = subprocess.run(['git', '-C', CL, 'log', '-1', '--format=%B', '3c26420'], capture_output=True, text=True).stdout
except Exception as ex:
    head, act96, msg96, msg95 = 'indisponible (%s)' % type(ex).__name__, '', '', ''
info('registre public : tete %s ; commits : %s' % (head, dates))
n96 = norm(act96)
phr = ['Registre a l\'ecriture : origin/main 04053e0, plafond 96 (releve du 14/11 au soir). Les deltas 95 et 96 y sont depuis le 14/11 a 14 h 12 et 14 h 13.',
       'un verdict a J2 est un verdict hors du domaine declare de la chaine', 'D-G1-1 (m1 ; reserve R-1 de machine 2)', 'Neuf des 59 alterations de machine 2 le montrent.',
       'six points sur douze contredisent la garde, trois dans chaque sens', 'trente et une attendent deja la revue']
mq = manque(phr, AN)
ok15 = (head == '04053e0' and dates.get('3c26420', '').startswith('2026-11-14 14:12') and dates.get('04053e0', '').startswith('2026-11-14 14:13')
        and 'un verdict a J2 est un verdict hors du domaine declare de la chaine' in n96 and 'coincidence' in n96 and 'D-CH-7' in n96
        and 'numbered 26 to 28, join the twenty-five' in msg95 and 'numbered 29 to 31, join the twenty-eight' in msg96 and 25 + 3 + 3 == 31
        and 'fe10bfe' in GEL and 'Hors registre' in GEL)
chk('C15', ok15 and not mq, 'nn.0, nn.9, nn.10, nn.12 : tete publique du registre %s ; commits 3c26420 (%s) et 04053e0 (%s) ; le gel dit fe10bfe et "Hors registre" ; l acte 96 au registre porte "coincidence", '
    'D-CH-7 et la phrase de J2 que l acte cite ; messages des commits : regles 26 a 28 sur 25, 29 a 31 sur 28, soit 31 ; phrases absentes %s' % (head, dates.get('3c26420'), dates.get('04053e0'), mq))

# ------------------------------------------------------------------ C16 : nn.12, nn.13, nn.15 ; les journaux de machine 1
noms15 = ['journal_delta_nn_domaine_G1_chaine_EA_v1.md', 'ecrire_acte_domaine_G1_machine1_v1.py', 'verdict_rejoue_machine1.json', 'lecture_rejouee_machine1.log',
          'releve_acte_domaine_G1_machine1_v1.py', 'releve_acte_domaine_G1_machine1_v1.log', 'contre_epreuve_releve_machine1_v1.py', 'contre_epreuve_releve_machine1_v1.log',
          'POUR_MACHINE2_acte_domaine_G1_machine1_v1.md', 'fabrique_lot_machine1_v2.py']
manifs = re.findall(r'^[0-9a-f]{16}\s+[0-9a-f]{16}\s+\d+\s+\d+\s+(\S+)$', man.decode('utf-8'), re.M)
absents = [n for n in noms15 if n not in manifs or (n not in AN and not (n.endswith('.log') and n[:-4] + '.py / .log' in AN))]
rel = zl.read('releve_acte_domaine_G1_machine1_v1.log').decode('utf-8')
cer = zl.read('contre_epreuve_releve_machine1_v1.log').decode('utf-8')
phr = ['(a) (m2, m1) Un selftest ne construit pas ses cas depuis la table qu\'il doit eprouver', '(b) (m2, m1) Un critere qui fait tomber un point ou une issue sur un seul etat dit sa marge au bruit de l\'instrument',
       '(c) (m1) Avant d\'ecrire un gel, la plume releve la tete du registre',
       'machine 1 -- le gel et ses instruments 1aafb301d7d0ebb3 ; machine 2 -- la certification d92a200ac348f0a3, le resultat 86a677dc0ff8ba9d.']
mq = manque(phr, AN)
lots_ok = (emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine2_certification_gel_domaine_G1_chaine_EA_v1.txt')))[0] == 'd92a200ac348f0a3'
           and emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine2_resultat_domaine_G1_chaine_EA_v1.txt')))[0] == '86a677dc0ff8ba9d'
           and emp(rd(os.path.join(ROOT, 'MANIFEST_lot_machine1_gel_domaine_G1_chaine_EA_v1.txt')))[0] == '1aafb301d7d0ebb3')
chk('C16', not absents and sorted(manifs) == sorted(noms15) and not mq and lots_ok,
    'nn.15 : les 10 pieces nommees == les 10 lignes du manifeste ; nn.13 : les canons des trois lots cites, recalcules de leurs manifestes : %s ; nn.12 : les trois regles candidates et leurs origines ; absents %s %s' % (
        lots_ok, absents, mq))
info('journaux de machine 1, lus et non rejoues : releve "%s" ; contre-epreuve "%s"' % (rel.strip().split('\n')[-1][:100], cer.strip().split('\n')[-1][:120]))

info('NON VERIFIABLE par machine 2 (attestations de machine 1 ou de l operateur) : (a) nn.0 et nn.11 (ii), l ouverture du chantier, "Ouvre !", 14/11 a 14 h 57 ; (b) nn.2, machine 1 n a joue la sonde '
     'a aucun des douze points E1 a E6 et H1 a H6 ; (c) nn.9 D-G1-3, ce que la plume a dit a l operateur (70 chances sur 100, puis 0.74 de l inverse) ; (d) nn.9 D-G1-2, l heure a laquelle machine 1 '
     'a relu le registre : l acte dit que la plume ne l a pas fait')
mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'acte': ACTE_NOM, 'canon': c_act, 'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}},
          open(JSN, 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
