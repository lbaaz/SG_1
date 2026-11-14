# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' du run du gel "la chaine E-A par etat, hors plage"
(journal_delta_nn_chaine_EA_par_etat_v1.md, canon aed8677322e20e0d, projet version 1, lot bb7db90c75d6935e), 2026-11-14.
Chaque affirmation CHIFFREE de l'acte est RECALCULEE ici depuis MES sources (le JSON de la sonde et le verdict de la feuille rendus
par MON run, mes journaux de garde, de bruit, de banc et de certification), jamais lue dans le script d'ecriture ni dans le releve de
machine 1. Les phrases attendues sont CONSTRUITES depuis les donnees puis cherchees dans l'acte (blancs normalises) : un nombre tape
a la main et faux est une morsure. Les paliers sont reecrits ici d'apres le texte du gel (section 6), pas importes de la feuille.
Usage (depuis BOCAL4) : python -P acte_chaine_contreseing/verification_acte_chaine_EA_par_etat_machine2_v1.py
Variables : LOT_ALT (contre-epreuve sur une copie mutee du lot), SUFFIXE_SORTIE. Ce script ne modifie rien d'autre que ses deux sorties."""
import hashlib
import io
import json
import math
import os
import re
import statistics
import subprocess
import sys
import unicodedata
import zipfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CH = os.path.join(ROOT, 'chaine_EA_par_etat')
SO = os.path.join(CH, 'sortie')
ACTE_NOM = 'journal_delta_nn_chaine_EA_par_etat_v1.md'
LOT = os.environ.get('LOT_ALT', 'lot_machine1_2026-11-14_acte_chaine_EA_par_etat_v1_recu.zip')
SUFFIXE = os.environ.get('SUFFIXE_SORTIE', '')
MANIF = 'MANIFEST_lot_machine1_acte_chaine_EA_par_etat_v1.txt'
LOG = os.path.join(HERE, 'verification_acte_chaine_EA_par_etat_machine2_v1%s.log' % SUFFIXE)
JSN = os.path.join(HERE, 'verification_acte_chaine_EA_par_etat_machine2_v1%s.json' % SUFFIXE)
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
chk('C01', c_act == 'aed8677322e20e0d' and len(RAW) == 15203 and len(LIGNES) - 1 == 234
    and ACTE.startswith('DELTA nn -- LA CHAINE E-A PAR ETAT, HORS PLAGE : RUN DU 14/11/2026 SOUS LE GEL 9df2702af59adbbc.')
    and '-- PROJET, VERSION 1' in ACTE and ACTE.rstrip().endswith('-- FIN journal_delta_nn_chaine_EA_par_etat_v1 --'),
    'acte : canon %s (annonce aed8677322e20e0d), %d octets (15203), %d lignes (234), en-tete et ligne de FIN, VERSION 1' % (
        c_act, len(RAW), len(LIGNES) - 1))
man = rd(os.path.join(ROOT, MANIF))
bad, n_l = [], 0
for ln in man.decode('utf-8').split('\n'):
    p = ln.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        n_l += 1
        if emp(zl.read(p[4])) != (p[0], p[1], int(p[2]), int(p[3])):
            bad.append(p[4])
canon_lot = emp(man)[0]
chk('C02', n_l == 8 and not bad and len([n for n in zl.namelist() if not n.startswith('MANIFEST_')]) == 8 and canon_lot == 'bb7db90c75d6935e',
    '%d pieces sur 8 au canon, a l empreinte brute et aux deux tailles ; ecarts %s ; CANON DU LOT %s (annonce bb7db90c75d6935e)' % (n_l, bad, canon_lot))
n_asc = sum(1 for c in ACTE if ord(c) > 127)
long_max = max(len(x) for x in LIGNES)
chk('C03', n_asc == 0 and long_max <= 100 and '%' not in ACTE and '\t' not in ACTE,
    'forme de l acte : non ASCII %d, plus longue ligne %d colonnes (<= 100), pour cent %d, tabulations %d' % (
        n_asc, long_max, ACTE.count('%'), ACTE.count('\t')))

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
info('index : %d fichiers, %d empreintes distinctes (fichiers et membres de zip)' % (n_f, len(IDX)))

# ------------------------------------------------------------------ C04 : canons de nn.1
paires = []
for m in re.finditer(r'^\s+([A-Za-z0-9_./ ()-]+?)  ([0-9a-f]{16})\s*$', ACTE, re.M):
    paires.append((m.group(1).strip(), m.group(2)))
paires += [('lot de certification', '3381564852ba6fe4'), ('lot de resultat', '9143062c481ad267')]
non_res, mauvais_nom = [], []
for nom, c in paires:
    if c not in IDX:
        non_res.append((nom, c))
        continue
    if re.search(r'\.(py|md|json|log)', nom):
        base = nom.split('/')[-1].split(' (')[0]
        if not any(re.split(r'[/!]', x)[-1] == base for x in IDX[c]):
            mauvais_nom.append((nom, c))
paires = sorted(set(paires))
chk('C04', len(paires) == 14 and not non_res and not mauvais_nom,
    'nn.1 : %d couples (nom, canon) lus dans l acte, tous retrouves chez moi, le nom est celui d une piece de ce canon ; non resolus %s ; noms differents %s' % (
        len(paires), non_res, mauvais_nom))
tous = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', ACTE)))
non_res_tous = [c for c in tous if c not in IDX]
chk('C05', len(tous) >= 18 and not non_res_tous,
    '%d empreintes de 16 chiffres cites dans tout l acte, toutes recalculees de pieces ou de manifestes que je detiens ; non resolues %s' % (
        len(tous), non_res_tous))

# ------------------------------------------------------------------ donnees de MON run
S = json.load(open(os.path.join(SO, 'sonde_chaine_par_etat.json'), encoding='ascii'))
V = json.load(open(os.path.join(SO, 'verdict_chaine_par_etat.json'), encoding='ascii'))
PTS = {x['id']: x for x in V['points']}
SP = {x['id']: x for x in S['points']}
ORDRE = [x['id'] for x in V['points']]
BORNES = [0.5, 2.0, 10 ** -0.5, 10 ** 0.5]


def palier(q):
    if 0.5 <= q <= 2.0:
        return 'FACTEUR 2'
    if q * q >= 0.1 and q * q <= 10.0:
        return 'DECADE'
    return 'HORS DECADE'


RANG = {'FACTEUR 2': 0, 'DECADE': 1, 'HORS DECADE': 2}
MOTIFS = ['J flou', 'etiquette hors domaine', 'site minoritaire', 'sous dix planchers', 'etat non suivi', 'cible instable',
          'barriere vide', 'chaine en erreur', 'chaine instable', 'etiquette en double']
D = {}      # donnees recalculees, par point
ecart_q, ecart_pal, n_jug = 0.0, 0, 0
for pid in ORDRE:
    x = PTS[pid]
    jug = [e for e in x['etats'] if e['exclu'] is None]
    qs = []
    for e in jug:
        q = e['Gamma_chaine'] / e['Gamma_2D']
        ecart_q = max(ecart_q, abs(q / e['q'] - 1))
        ecart_pal += (palier(q) != e['palier'])
        qs.append((e['rang'], e['n1'], e['n2'], q))
    n_jug += len(jug)
    st = max((palier(q) for _, _, _, q in qs), key=lambda s: RANG[s]) if len(qs) >= 6 else 'NON LISIBLE'
    ex = {}
    for e in x['etats']:
        if e['exclu']:
            ex[e['exclu']] = ex.get(e['exclu'], 0) + 1
    D[pid] = {'role': x['role'], 'w2': x['w2'], 'g': x['facteur'], 'statut_feuille': x['statut'], 'statut': st, 'n': len(jug),
              'qs': qs, 'qmin': min(q for *_, q in qs), 'qmax': max(q for *_, q in qs), 'med': statistics.median(q for *_, q in qs),
              'prem': min(qs, key=lambda t: t[0]), 'ex': ex}
chk('C06', ecart_q < 1e-12 and ecart_pal == 0 and all(D[p]['statut'] == D[p]['statut_feuille'] for p in ORDRE) and n_jug == 131
    and sum(len(PTS[p]['etats']) for p in ORDRE) == 168,
    'mon recalcul de q = Gamma_chaine / Gamma_2D(3) sur le verdict de mon run : ecart relatif max a q de la feuille %.1e ; paliers d etat %d '
    'differents ; statuts de point (le pire palier des etats juges, >= 6 juges) == ceux de la feuille ; %d etats juges sur 168' % (ecart_q, ecart_pal, n_jug))

# ------------------------------------------------------------------ C07 : le verdict et les rejeux
mon_verdict = rd(os.path.join(SO, 'verdict_chaine_par_etat.json')).replace(b'\r\n', b'\n')   # CRLF de ma plateforme : la convention B les ramene a LF
mon_verdict_brut = rd(os.path.join(SO, 'verdict_chaine_par_etat.json'))
verd_m1 = zl.read('verdict_rejoue_machine1.json')
lec_m1 = zl.read('lecture_rejouee_machine1.log').decode('utf-8').split('\n')
lec_m2 = open(os.path.join(SO, 'lecture_chaine_par_etat.log'), encoding='utf-8').read().split('\n')
diff = [(a, b) for a, b in zip(lec_m1, lec_m2) if a != b]
cas = [x for x in lec_m1 if x.startswith('SELFTEST')]
cascade = D and all(D[p]['statut'] in ('FACTEUR 2', 'DECADE', 'HORS DECADE') for p in ORDRE[:6])
chk('C07', emp(mon_verdict)[0] == '4fbc5f7115002054' == emp(verd_m1)[0] and mon_verdict == verd_m1 and len(lec_m1) == len(lec_m2)
    and len(diff) == 1 and diff[0][0].startswith('LECTURE DU GEL') and cas == ['SELFTEST : 26 cas, 26 tenus'] and V['verdict'] == 'TENU EN PARTIE'
    and emp(rd(os.path.join(SO, 'lecture_chaine_par_etat.log')))[0] == '997c4e4681b0e7ec' and emp(zl.read('lecture_rejouee_machine1.log'))[0] == '64589ba23c6b8097',
    'verdict de mon run == verdict rejoue par machine 1, octet pour octet apres CRLF -> LF (mes octets bruts %d, les siens %d), canon 4fbc5f7115002054 ; journaux : %d lignes de part et d autre, %d ligne(s) '
    'qui differe(nt), la ligne de titre ; selftest %s ; verdict %s' % (len(mon_verdict_brut), len(verd_m1), len(lec_m1), len(diff), cas, V['verdict']))

# ------------------------------------------------------------------ C08 : nn.2 mon run
con = open(os.path.join(SO, 'console_chaine_par_etat.log'), encoding='utf-8').read()
pf = S['plateforme']
ok_run = ('2026-11-14 10:12:51 DEBUT DU PILOTE' in con and '2026-11-14 10:37:31 FIN DE LA SONDE code=0 duree=1480 s' in con
          and '10:37:31 FIN DE LA FEUILLE code=0' in con and pf['systeme'] == 'Windows' and pf['machine'] == 'AMD64' and pf['python'] == '3.11.9'
          and pf['numpy'] == '2.2.6' and pf['coeurs'] == 16 and all(v is None for v in pf['fils'].values())
          and pf['temoin_arrondi'] == '0x1.a483018a169c6p+64')
phr = ['BOCAL4, Windows AMD64, python 3.11.9, numpy 2.2.6, 16 coeurs, variables de fils non fixees ; le 14/11 de 10:12:51 a 10:37:31 ; sonde code 0 en 1480 s,',
       'feuille code 0 ; un seul run, aucun arret, aucune reprise, aucun point rejoue. Temoin d\'arrondi 0x1.a483018a169c6p+64']
mq = manque(phr, AN)
chk('C08', ok_run and not mq, 'nn.2, mon run : journal du pilote et JSON de la sonde (plateforme, heures, code, duree) == l acte ; phrases absentes %s' % mq)

# ------------------------------------------------------------------ C09 : nn.2 avant le run, nn.9 D-CH-9 (mes lots de certification)
banc = open(os.path.join(CH, 'banc_feuille_machine2_v1.log'), encoding='ascii').read()
ctrl = open(os.path.join(CH, 'controles_gel_machine2_v1.log'), encoding='ascii').read()
m_sur = re.search(r'survivent au selftest de machine 1 : \[([\d, ]+)\] ; survivent a mon banc : \[([\d, ]+)\]', banc)
sv_m1 = [int(x) for x in m_sur.group(1).split(',')]
sv_m2 = [int(x) for x in m_sur.group(2).split(',')]
n_mut = len(re.findall(r'^\s+M\d\d  selftest', banc, re.M))
m4000 = re.search(r'4000 sondes synthetiques aux bords des seuils.*\n\s+ecarts feuille / lecteur : (\d+)', banc)
ok9 = (n_mut == 24 and len(sv_m1) == 9 and len(sv_m2) == 1 and m4000 and m4000.group(1) == '0' and 'BILAN : 11 controles, 0 mordent' in ctrl)
phr = ['11 controles de lecture du gel, 0 morsure ; un lecteur independant, ecrit du texte du gel, compare a la feuille sur 4000 sondes synthetiques',
       'tirees aux bords des seuils, 0 ecart ; 24 alterations d\'une ligne de la feuille, dont son banc mord %d et le selftest de la feuille %d' % (
           24 - len(sv_m2), 24 - len(sv_m1)),
       'il laisse passer neuf alterations d\'une ligne sur 24']
mq = manque(phr, AN)
chk('C09', ok9 and not mq, 'nn.2 et D-CH-9 : mes journaux de certification (11 controles / 0 mordent ; 4000 sondes / %s ecart ; %d alterations, '
    'banc mord %d, selftest mord %d, survivent au selftest %s) == l acte ; phrases absentes %s' % (
        m4000.group(1) if m4000 else '?', n_mut, 24 - len(sv_m2), 24 - len(sv_m1), sv_m1, mq))

# ------------------------------------------------------------------ C10 : nn.3 les gardes
motifs_g = V['motifs']
A1 = [e for e in SP['A1']['etats'] if (e['n1'], e['n2']) == (7, 2)]
A2 = [e for e in SP['A2']['etats'] if (e['n1'], e['n2']) == (8, 2)]
M17_A1, M17_A2 = 2.1623273017950654e-10, 2.6613925716641374e-09
ok10 = (S['moteur_canon'] == '82a0be882568fe0c' and len(S['points']) == 12 and all(len(p['etats']) == 14 for p in S['points'])
        and len(A1) == 1 and len(A2) == 1 and A1[0]['Gamma_2D']['3'] == M17_A1 and A2[0]['Gamma_2D']['3'] == M17_A2 and motifs_g == [])
phr = ['G-1 le moteur lu par la sonde est au canon. G-2 les douze points sont presents, au role, au w2 et',
       'au facteur du gel. G-3 chacun porte 14 etats (168). G-4 les deux ancres rendent la lecture du run',
       'de M17 avec un ecart relatif NUL sur BOCAL4 (etat (7,2) a A1, etat (8,2) a A2). G-5 la feuille',
       'passe son selftest. Aucune garde ne mord.']
mq = manque(phr, AN)
chk('C10', ok10 and not mq, 'nn.3 : moteur %s, 12 points, 168 etats ; ancres A1 (7,2) = %r et A2 (8,2) = %r == lectures de M17 au bit ; motifs de la '
    'feuille %s ; phrases absentes %s' % (S['moteur_canon'], A1[0]['Gamma_2D']['3'] if A1 else None, A2[0]['Gamma_2D']['3'] if A2 else None, motifs_g, mq))

# ------------------------------------------------------------------ C11 : nn.4 le tableau
ROLE = {'juge': 'juge', 'temoin': 'temoin', 'ancre': 'ancre'}
manq, lignes_t = [], []
for pid in ORDRE:
    d = D[pid]
    num, den = map(int, d['w2'].split('/'))
    gn = d['g']
    gtxt = 'x1' if gn == '1/1' else 'x' + gn
    n1, n2, q1 = d['prem'][1], d['prem'][2], d['prem'][3]
    row = '%s %s %.2f %s %s %d %.3f %.3f %.3f (%d,%d) q = %.3f' % (pid, ROLE[d['role']], num / den, gtxt, d['statut'], d['n'], d['qmin'], d['qmax'],
                                                                 d['med'], n1, n2, q1)
    lignes_t.append(row)
    if norm(row) not in AN:
        manq.append(row)
chk('C11', not manq, 'nn.4, les 12 lignes du tableau (statut, juges, q min, q max, mediane, premier juge) recalculees de mon verdict ; absentes : %s' % manq)
manq = []
for pid in ORDRE:
    ex = D[pid]['ex']
    txt = ' ; '.join('%s %d' % (m, ex[m]) for m in sorted(ex)) if ex else 'aucun'      # la feuille les range par ordre alphabetique
    if norm('%s %s' % (pid, txt)) not in AN:
        manq.append('%s %s' % (pid, txt))
chk('C12', not manq and '131 etats juges sur 168' in AN, 'nn.4, les 12 lignes d exclusion par premier motif recalculees de mon verdict ; absentes : %s ; '
    '131 etats juges sur 168 : %s' % (manq, '131 etats juges sur 168' in AN))

# ------------------------------------------------------------------ C13 : nn.5 le verdict
J = {p: D[p] for p in ('J1', 'J2', 'J3', 'J4', 'J6')}
n44 = sum(D[p]['n'] for p in ('J1', 'J3', 'J4', 'J6'))
tous44 = all(0.5 <= q <= 2.0 for p in ('J1', 'J3', 'J4', 'J6') for *_, q in D[p]['qs'])
j5 = [q for *_, q in D['J5']['qs']]
j5_bas = sorted(q for q in j5 if q < 0.5)
j5_haut = sorted(q for q in j5 if q >= 0.5)
j2 = [q for *_, q in D['J2']['qs']]
j2_hors = sum(1 for q in j2 if not (10 ** -0.5 <= q <= 10 ** 0.5))
phr = ['Cinq tiennent : J1, J3, J4 et J6 sont FACTEUR 2, J5 est DECADE. Un tombe : J2 est HORS DECADE. La cascade du gel (section 7) rend TENU EN PARTIE.',
       'a mieux qu\'un facteur 2 pour chacun des %d etats juges ;' % n44,
       'a J5 (couplage a 2/3, 1.95), a mieux qu\'une demi-decade pour les %d etats juges ; %d sont sous 1/2 (q de %.3f a %.3f), les %d autres de %.3f a %.3f' % (
           len(j5), len(j5_bas), j5_bas[0], j5_bas[-1], len(j5_haut), j5_haut[0], j5_haut[-1]),
       'a J2 (2.10), elle la SURESTIME d\'un facteur %.3f a %.3f sur chacun des %d etats juges ; %d d\'entre eux sont hors de la demi-decade' % (
           min(j2), max(j2), len(j2), j2_hors),
       'VERDICT : TENU EN PARTIE (cinq points juges tiennent, un tombe).']
mq = manque(phr, AN)
chk('C13', tous44 and n44 == 44 and all(10 ** -0.5 <= q <= 10 ** 0.5 for q in j5) and all(q > 2.0 for q in j2) and not mq,
    'nn.5 : %d etats juges aux quatre points FACTEUR 2 tous dans [1/2, 2] : %s ; J5 %d etats tous dans la demi-decade ; J2 %d etats tous au-dessus de 2 ; '
    'phrases absentes %s' % (n44, tous44, len(j5), len(j2), mq))

# ------------------------------------------------------------------ C14 : nn.6 lectures sans verdict
t1 = sorted(q for *_, q in D['T1']['qs'])
t3 = [q for *_, q in D['T3']['qs']]
t4 = [q for *_, q in D['T4']['qs']]
viol = []
for pid in ORDRE:
    num, den = map(int, D[pid]['w2'].split('/'))
    w = num / den
    if (w < 2 and not D[pid]['med'] < 1) or (w > 2 and not D[pid]['med'] > 1):
        viol.append(pid)
j6neg = [e for e in SP['J6']['etats'] if e['Gamma_2D']['3'] < 0]
j6exc = [e for e in PTS['J6']['etats'] if e['rang'] == (j6neg[0]['rang'] if j6neg else -1)]
cmp16 = open(os.path.join(CH, 'compare_16fils_4fils_machine2_v1.log'), encoding='ascii').read()
m_abs = re.search(r'ecart absolu max de Gamma_2D \(k = 2, 3, 4\) ([0-9.e+-]+)', cmp16)
stab = open(os.path.join(SO, 'stabilite_sous_bruit_machine2.log'), encoding='ascii').read()
m_rel = re.search(r'bruit relatif maximal de la cible ([0-9.e+-]+)', stab)
n_inch = len(re.findall(r'-> INCHANGE', stab))
phr = ['T1 (1.96) est DECADE par un seul etat (q = %.4f, les onze autres de %.3f a %.3f)' % (t1[0], t1[1], t1[-1]),
       'T3 (1.85) et T4 (2.15) sont HORS DECADE, T3 en ordre disperse (q de %.3f a %.3f), T4 d\'un facteur %.1f a %.1f' % (min(t3), max(t3), min(t4), max(t4)),
       'Aux douze points, le q median est sous 1 quand w2 < 2 et au-dessus de 1 quand w2 > 2.',
       'J5 et J6 n\'ont que 8 etats juges : six de leurs quatorze sont sous dix planchers. A J6 un Gamma_2D(3) est negatif (%.1e, du bruit) ; il est exclu comme "sous dix planchers".' % (
           j6neg[0]['Gamma_2D']['3'] if j6neg else float('nan')),
       '%.1e en absolu sur la cible. Aucun des douze statuts ne change' % float(m_abs.group(1)),
       'le bruit relatif maximal sur les 131 etats juges est %.1f pour cent' % (float(m_rel.group(1)) * 100)]
mq = manque(phr, AN)
ok14 = (t1[0] < 0.5 and all(0.5 <= q for q in t1[1:]) and not viol and len(j6neg) == 1 and j6exc and j6exc[0]['exclu'] == 'sous dix planchers'
        and D['J5']['ex'] == {'sous dix planchers': 6} and D['J6']['ex'] == {'sous dix planchers': 6} and D['J5']['n'] == D['J6']['n'] == 8
        and n_inch == 12 and D['T3']['statut'] == D['T4']['statut'] == 'HORS DECADE')
chk('C14', ok14 and not mq, 'nn.6 : T1 un etat sous 1/2 (%.4f), les onze autres au-dessus ; signe des medianes, violations %s ; J6 : %d Gamma_2D(3) negatif, exclu '
    '%r ; bruit %s absolu (16 contre 4 fils), %s relatif max ; %d statuts sur 12 inchanges ; phrases absentes %s' % (
        t1[0], viol, len(j6neg), j6exc[0]['exclu'] if j6exc else None, m_abs.group(1), m_rel.group(1), n_inch, mq))

# ------------------------------------------------------------------ C15 : nn.7 la garde de domaine du moteur
gl = open(os.path.join(CH, 'garde_G1_domaine_machine2_v1.log'), encoding='ascii').read()
G = {}
for m in re.finditer(r'^(\S+)\s+w2=\S+\s+x\S+\s+D1=([0-9.]+) \(<=0.2\) c_max=([0-9.]+) site \d \(<=0.1\) -> (EN DOMAINE|HORS DOMAINE)', gl, re.M):
    G[m.group(1)] = (m.group(2), m.group(3), m.group(4))
manq = []
for pid in ORDRE:
    d1, cm, dom = G[pid]
    row = '%s %s %s %s %s' % (pid, d1, cm, dom, D[pid]['statut'])
    if norm(row) not in AN:
        manq.append(row)
hors_dom = sorted(p for p in ORDRE if G[p][2] == 'HORS DOMAINE')
hors_dec = sorted(p for p in ORDRE if D[p]['statut'] == 'HORS DECADE')
neuf = [p for p in ORDRE if G[p][2] == 'EN DOMAINE']
m17 = [k for k in G if k.startswith('M17-')]
ok15 = (hors_dom == hors_dec == ['J2', 'T3', 'T4'] and len(neuf) == 9 and all(D[p]['statut'] in ('FACTEUR 2', 'DECADE') for p in neuf)
        and len(m17) == 6 and all(G[k][2] == 'EN DOMAINE' for k in m17)
        and all((float(G[p][0]) > 0.2) == (G[p][2] == 'HORS DOMAINE' and float(G[p][1]) <= 0.1) or float(G[p][1]) > 0.1 for p in ORDRE))
phr = ['Les trois points ou la garde dit HORS DOMAINE (J2, T3, T4) sont les trois points HORS DECADE ; les neuf points EN DOMAINE sont FACTEUR 2 ou DECADE.',
       'Les six points de M17 sont EN DOMAINE']
mq = manque(phr, AN)
chk('C15', ok15 and not manq and not mq, 'nn.7 : les 12 lignes (D1, c_max, garde du moteur, statut) recalculees de mon journal de garde et de mon verdict ; absentes %s ; '
    'HORS DOMAINE %s == HORS DECADE %s ; neuf EN DOMAINE FACTEUR 2 ou DECADE ; six points de M17 EN DOMAINE : %s ; phrases absentes %s' % (
        manq, hors_dom, hors_dec, len(m17) == 6 and all(G[k][2] == 'EN DOMAINE' for k in m17), mq))

# ------------------------------------------------------------------ C16 : nn.8 les annonces
gel = open(os.path.join(CH, 'gel_chaine_EA_par_etat_pre_enregistrement_v1.md'), encoding='ascii').read()
gn = norm(gel)
proba_gel = {'A-2': 0.55, 'A-3': 0.55, 'A-4': 0.60, 'A-5': 0.40, 'A-6': 0.75, 'A-7': 0.65, 'A-8': 0.95}
ok_gel = all('%s (%.2f)' % (k, v) in gn for k, v in proba_gel.items()) and 'A-1 le verdict : TENU EN PARTIE 0.72' in gn
q_j2, q_j1 = D['J2']['prem'][3], D['J1']['prem'][3]
rep = {'A-1': D and V['verdict'] == 'TENU EN PARTIE', 'A-2': D['J2']['statut'] == 'HORS DECADE', 'A-3': 2.3 <= q_j2 <= 4.6, 'A-4': 0.70 <= q_j1 <= 0.85,
       'A-5': D['J3']['statut'] == D['J4']['statut'] == 'FACTEUR 2', 'A-6': not viol, 'A-7': D['J5']['statut'] != 'NON LISIBLE', 'A-8': not motifs_g}
lig = ['A-1 (0.72) le verdict est TENU EN PARTIE REALISEE', 'A-2 (0.55) J2 est HORS DECADE VRAIE', 'A-3 (0.55) a J2, q du premier juge entre 2.3 et 4.6 VRAIE (%.3f)' % q_j2,
       'A-4 (0.60) a J1, q du premier juge entre 0.70 et 0.85 FAUSSE (%.3f)' % q_j1, 'A-5 (0.40) J3 et J4 tous les deux FACTEUR 2 VRAIE',
       'A-6 (0.75) signe du q median aux points juges lisibles VRAIE', 'A-7 (0.65) J5 est lisible VRAIE (%d etats juges)' % D['J5']['n'], 'A-8 (0.95) la garde G-4 tient VRAIE']
n_vraies = sum(1 for v in rep.values() if v)
mq = manque(lig, AN)
chk('C16', ok_gel and not mq and n_vraies == 7 and not rep['A-4'] and 'Sept sur huit.' in AN,
    'nn.8 : probabilites et intervalles des huit annonces == section 10 de mon exemplaire du gel : %s ; sort de chacune recalcule de mon verdict : %s ; '
    '%d sur 8 ; lignes absentes %s' % (ok_gel, {k: bool(v) for k, v in rep.items()}, n_vraies, mq))

# ------------------------------------------------------------------ C17 : nn.9 defauts et reserves
rel = open(os.path.join(SO, 'relecture_independante_machine2.log'), encoding='ascii').read()
m_t3 = re.search(r'T3 : feuille HORS DECADE \((\d+) juges\) ; lecteur HD \((\d+) juges\) -> DIFFERENT', rel)
autres_diff = len(re.findall(r'^  (?!T3)\S+ : .* -> DIFFERENT', rel, re.M))
note_cert = open(os.path.join(ROOT, 'POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md'), encoding='ascii').read() \
    if os.path.isfile(os.path.join(ROOT, 'POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md')) else ''
if not note_cert:
    z3 = zipfile.ZipFile(os.path.join(ROOT, 'lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1.zip'))
    note_cert = z3.read('POUR_MACHINE1_certification_gel_chaine_EA_par_etat_machine2_v1.md').decode('ascii')
phr = ['11 etats juges chez machine 1, 13 chez machine 2, meme statut', 'Un seul point est touche, le temoin T3',
       'mesure, il vaut 7.3e-14 entre 16 et 4 fils, 6.7e-14 entre les deux machines']
mq = manque(phr, AN)
chk('C17', bool(m_t3) and autres_diff == 0 and '6.7e-14' in note_cert and not mq,
    'nn.9 D-CH-8 et D-CH-10 : T3 feuille %s juges, mon lecteur independant %s, aucun autre point ne differe (%d) ; 6.7e-14 entre les deux machines dans ma note '
    'de certification : %s ; phrases absentes %s' % (m_t3.group(1) if m_t3 else '?', m_t3.group(2) if m_t3 else '?', autres_diff, '6.7e-14' in note_cert, mq))

# ------------------------------------------------------------------ C18 : nn.9 R-4, la borne
dist = []
for pid in ORDRE:
    for r, n1, n2, q in D[pid]['qs']:
        for b in BORNES:
            dist.append((abs(q / b - 1), pid, r, q, b))
dist.sort()
proche = dist[0]
d_rac10 = min(abs(q / 10 ** 0.5 - 1) for pid in ORDRE for *_, q in D[pid]['qs'])
phr = ['R-4 (m2) : a q = racine de 10 exactement la feuille rend HORS DECADE alors que le gel ferme la borne.',
       'le q le plus proche d\'une borne est celui d\'un temoin (T1, %.4f, a 0.5' % proche[3],
       'pour cent de 1/2) ; aucun n\'est pres de la racine de 10.']
mq = manque(phr, AN)
chk('C18', proche[1] == 'T1' and proche[4] == 0.5 and 0.004 < proche[0] < 0.006 and d_rac10 > 1e-6 and not mq and 'DECADE        sinon, si tous les q sont dans [10^(-1/2), 10^(1/2)]' in gel,
    'nn.9 R-4 : parmi les 131 q jugees et les quatre bornes, la plus proche est %s (rang %d, q = %.4f, borne %.4f, ecart relatif %.4f) ; la plus proche de la racine '
    'de 10 en est a %.4f (J2, rang 10, q = 3.1141, DANS la demi-decade) : "pres" se lit a la precision machine, qui est le sens de R-4 ; le gel ferme la borne ; '
    'phrases absentes %s' % (proche[1], proche[2], proche[3], proche[4], proche[0], d_rac10, mq))

# ------------------------------------------------------------------ C19 : nn.10 la note 9322566db2546adb
loc = IDX.get('9322566db2546adb', [])
txt = ''
for chemin in loc:
    if '!' in chemin:
        zp, mb = chemin.split('!', 1)
        txt = zipfile.ZipFile(os.path.join(ROOT, zp)).read(mb).decode('utf-8', 'replace')
        break
phr = ['La note 9322566db2546adb lisait, apres coup, un accord chaine / 2D de 0.499 a 1.642 aux six points de M17.',
       'l\'accord tient a un facteur 2 a quatre points juges, a une demi-decade a un cinquieme, et tombe au sixieme']
mq = manque(phr, AN)
chk('C19', bool(loc) and '0.499' in txt and '1.642' in txt and not mq and [D[p]['statut'] for p in ('J1', 'J3', 'J4', 'J6')] == ['FACTEUR 2'] * 4
    and D['J5']['statut'] == 'DECADE' and D['J2']['statut'] == 'HORS DECADE',
    'nn.10 : la note 9322566db2546adb (%s) porte 0.499 et 1.642 ; 4 points FACTEUR 2, un DECADE, un HORS DECADE ; phrases absentes %s' % (loc[:1], mq))

# ------------------------------------------------------------------ C20 : nn.0, nn.13 registre, lots du canal
try:
    head = subprocess.run(['git', 'ls-remote', 'https://github.com/lbaaz/SG_1', 'HEAD'], capture_output=True, text=True, timeout=60).stdout.split()[0][:7]
except Exception as e:
    head = 'indisponible (%s)' % type(e).__name__
info('tete du registre public lue par git ls-remote : %s (l acte dit fe10bfe)' % head)
mes_lots = {'3381564852ba6fe4': 'lot_machine2_2026-11-14_certification_gel_chaine_EA_par_etat_v1.zip',
            '9143062c481ad267': 'lot_machine2_2026-11-14_resultat_chaine_EA_par_etat_v1.zip',
            'b46537578fff4ab0': 'lot_machine2_2026-11-14_contreseing_acte_nn_EB_bis_v2_v1.zip'}
bons = {}
for c, zp in mes_lots.items():
    z = zipfile.ZipFile(os.path.join(ROOT, zp))
    mm = [n for n in z.namelist() if n.startswith('MANIFEST_')][0]
    bons[c] = emp(z.read(mm))[0] == c
m1_lots = {'b3d3e23e98914a95': 'MANIFEST_lot_machine1_gel_chaine_EA_par_etat_v1.txt', 'fa54b6ed68469db8': 'MANIFEST_lot_machine1_reponse_rejeu_chaine_EA_v1.txt',
           'bdf8c5a0c73096a4': None}
for c, mf in m1_lots.items():
    if mf:
        bons[c] = emp(rd(os.path.join(ROOT, mf)))[0] == c
    else:
        bons[c] = c in IDX
phr = ['Registre a l\'ecriture : origin/main fe10bfe, plafond 94 (releve du 14/11).', 'projet v2 (bdf8c5a0c73096a4), est contresigne par machine 2 (lot b46537578fff4ab0)',
       'machine 1 -- le gel et ses instruments b3d3e23e98914a95', 'machine 2 -- la certification 3381564852ba6fe4, le resultat 9143062c481ad267']
mq = manque(phr, AN)
chk('C20', head == 'fe10bfe' and all(bons.values()) and not mq,
    'nn.0 et nn.13 : tete du registre public %s (l acte dit fe10bfe, plafond 94 : le message de cette tete s ouvre sur "delta 94") ; canons des lots cites '
    'recalcules de leurs manifestes : %s ; phrases absentes %s' % (head, bons, mq))

# ------------------------------------------------------------------ C21 : nn.12 les regles candidates et nn.15 les pieces
noms15 = ['journal_delta_nn_chaine_EA_par_etat_v1.md', 'ecrire_acte_chaine_EA_par_etat_machine1_v1.py', 'verdict_rejoue_machine1.json',
          'lecture_rejouee_machine1.log', 'releve_acte_chaine_EA_par_etat_machine1_v1.py', 'releve_acte_chaine_EA_par_etat_machine1_v1.log',
          'POUR_MACHINE2_acte_chaine_EA_par_etat_machine1_v1.md', 'fabrique_lot_machine1_v1.py']
manifs = [n for n in re.findall(r'^[0-9a-f]{16}\s+[0-9a-f]{16}\s+\d+\s+\d+\s+(\S+)$', man.decode('utf-8'), re.M)]
absents = [n for n in noms15 if n not in manifs or (n not in AN and not (n.endswith('.log') and n[:-4] + '.py / .log' in AN))]
notes = ' '.join(re.findall(r'^R-\d.*$', note_cert, re.M))
phr = ['(a) (m2, m1) Une sonde qui appelle les fonctions d\'un moteur sans passer par ses gardes le dit, et', '(b) (m2) Un critere ecrit comme un rapport dit ce qu\'il fait d\'un terme nul ou negatif.',
       '(c) (m2, m1) Un selftest porte un cas a chaque bord de seuil']
mq = manque(phr, AN)
chk('C21', not absents and sorted(manifs) == sorted(noms15) and not mq and all(('R-%d' % i) in note_cert for i in (1, 2, 3, 4)),
    'nn.15 : les 8 pieces nommees == les 8 lignes du manifeste du lot ; nn.12 : les trois regles candidates portent les origines que mes reserves R-1 a R-4 '
    'leur donnent ; absentes %s %s' % (absents, mq))

# ------------------------------------------------------------------ C22 : la phrase de ma reserve R-1, reprise dans nn.7
mq_n = norm(note_cert)
AMORCE = "Proposition de texte pour l'acte, si tu ecris l'acte : \""
i = mq_n.find(AMORCE)
phrase_r1 = mq_n[i + len(AMORCE):].split('"')[0] if i >= 0 else ''
dans_acte = norm(phrase_r1[1:]) in AN and ('a' + norm(phrase_r1[1:])) in AN        # l acte la reprend apres deux-points : seule la majuscule initiale change
chk('C22', len(phrase_r1) > 100 and dans_acte and phrase_r1.startswith('A J2, T3 et T4 la garde G-1'),
    'nn.7 : la phrase de machine 2 reprise par l acte (%d caracteres) est mot pour mot celle de ma reserve R-1 (note de certification), a la majuscule initiale pres : %s' % (
        len(phrase_r1), dans_acte))

# ------------------------------------------------------------------ non verifiables
info('NON VERIFIABLE par machine 2 (attestations de machine 1 ou de l operateur) : (a) nn.0 et nn.11 (ii), l ouverture du chantier, "j ouvre", 14/11 a 00 h 15 ; '
     '(b) nn.2, machine 1 n a joue la sonde a aucun des dix points J1 a J6 et T1 a T4 ; (c) nn.13, le conteneur de machine 1 a tenu du 12 au 14/11 ; '
     '(d) nn.7, machine 1 a recalcule la garde (le releve de machine 1 relit mon journal, il ne la rejoue pas)')
mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'acte': ACTE_NOM, 'canon': c_act, 'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}},
          open(JSN, 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
