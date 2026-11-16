# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' du run du gel E-B ter (journal_delta_nn_qualification_EB_ter_v1.md, canon 751165a3eee613d9, projet version 1, lot de
machine 1 26b3912297b31713), 2026-11-15. Chaque affirmation CHIFFREE de l'acte est RECALCULEE ici depuis MES sources (les quinze sorties JSON de la sonde rendues par MON run, le
verdict de la feuille de machine 1 rendu sur BOCAL4, MA feuille independante ecrite du texte du gel, mes journaux de certification, de pre-vol, de bloc, de banc, le journal du pilote,
le depot et les verdicts du registre public), jamais lue dans le script d'ecriture ni dans le releve de machine 1. Les phrases attendues sont CONSTRUITES depuis les donnees puis
cherchees dans l'acte (blancs normalises) : un nombre tape a la main et faux est une morsure. Meme methode que verification_acte_ordre2_machine2_v1.py (acte du delta 98).
REGLES DECLAREES AVANT LE PREMIER PASSAGE (rien n'est ajuste apres) : (1) un nombre de l'acte est tenu s'il est celui que je calcule, ecrit au format de l'acte ; (2) pour les bornes dites
"au plus" ou "au moins", l'acte declare (POUR_MACHINE2, M-5) arrondir "au moins" vers le bas et "au plus" vers le haut : je tiens le nombre arrondi ainsi a deux chiffres significatifs
(ou a deux decimales pour 14.95 et 15.00) ET j'ecris, dans le message du controle, la valeur vraie ; (3) un controle mord si UNE de ses conditions est fausse, meme d'une unite du dernier
chiffre ; (4) ce que je ne puis pas recalculer est dit en "info", jamais compte comme tenu.
Usage (depuis BOCAL4) : py -3.11 -I acte_EB_ter_contreseing/verification_acte_EB_ter_machine2_v1.py
Variables : LOT_ALT (contre-epreuve sur une copie mutee du lot), SUFFIXE_SORTIE, REGISTRE_CLONE. Ce script ne modifie rien d'autre que ses deux sorties."""
import glob
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import statistics
import subprocess
import sys
import time
import unicodedata
import zipfile
from fractions import Fraction

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RUN = os.path.join(ROOT, 'run_EB_ter')
CTRL = os.path.join(ROOT, 'certif_EB_ter', 'controles')
GELM1 = os.path.join(ROOT, 'certif_EB_ter', 'lot_m1')
ACTE_NOM = 'journal_delta_nn_qualification_EB_ter_v1.md'
LOT = os.environ.get('LOT_ALT', 'lot_machine1_2026-11-15_acte_EB_ter_v1_recu.zip')
SUFFIXE = os.environ.get('SUFFIXE_SORTIE', '')
MANIF = 'MANIFEST_lot_machine1_acte_EB_ter_v1.txt'
CLONE = os.environ.get('REGISTRE_CLONE', os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp', 'claude', '75adcc7f3c1d08bf', '7d33635e-8345-4a2c-a69e-f6a51f9d8fa7',
                                                      'scratchpad', 'reg_neuf98'))
LOG = os.path.join(HERE, 'verification_acte_EB_ter_machine2_v1%s.log' % SUFFIXE)
JSN = os.path.join(HERE, 'verification_acte_EB_ter_machine2_v1%s.json' % SUFFIXE)
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


def haut(x, nd=2):
    e = math.floor(math.log10(abs(x)))
    f = 10.0 ** (e - nd + 1)
    return math.ceil(x / f - 1e-9) * f


def bas(x, nd=2):
    e = math.floor(math.log10(abs(x)))
    f = 10.0 ** (e - nd + 1)
    return math.floor(x / f + 1e-9) * f


def J(p):
    return json.load(open(p, encoding='utf-8'))


# ------------------------------------------------------------------ l'acte et son lot
zl = zipfile.ZipFile(os.path.join(ROOT, LOT))
RAW = zl.read(ACTE_NOM)
ACTE = RAW.decode('utf-8')
AN = norm(ACTE)
LIGNES = ACTE.split('\n')
dire('VERIFICATION de l acte %s par machine 2' % ACTE_NOM)
c_act = emp(RAW)[0]
chk('C01', c_act == '751165a3eee613d9' and ACTE.startswith("DELTA nn -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS), TER : RUN DU 15/11/2026 SOUS LE GEL\n432319b9feb34b82.")
    and '-- PROJET, VERSION 1' in ACTE and ACTE.rstrip().endswith('-- FIN journal_delta_nn_qualification_EB_ter_v1 --'),
    'acte : canon %s (annonce 751165a3eee613d9), %d octets, %d lignes, en-tete et ligne de FIN, VERSION 1' % (c_act, len(RAW), len(LIGNES) - 1))
man = rd(os.path.join(ROOT, MANIF))
bad, n_l = [], 0
for ln in man.decode('utf-8').split('\n'):
    p = ln.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        n_l += 1
        if emp(zl.read(p[4])) != (p[0], p[1], int(p[2]), int(p[3])):
            bad.append(p[4])
canon_lot = emp(man)[0]
mz = [n for n in zl.namelist() if n.startswith('MANIFEST_')]
chk('C02', n_l == 30 and not bad and len([n for n in zl.namelist() if not n.startswith('MANIFEST_')]) == 30 and canon_lot == '26b3912297b31713' and (not mz or zl.read(mz[0]) == man),
    '%d pieces sur 30 au canon, a l empreinte brute et aux deux tailles ; ecarts %s ; CANON DU LOT %s (annonce 26b3912297b31713) ; manifeste dans le zip : %s' % (
        n_l, bad, canon_lot, 'oui, identique' if mz else 'non (il est pose a cote du zip, comme le dit l enveloppe)'))
n_asc = sum(1 for c in ACTE if ord(c) > 127)
long_max = max(len(x) for x in LIGNES)
chk('C03', n_asc == 0 and long_max <= 100 and '%' not in ACTE and '\t' not in ACTE,
    'forme de l acte : non ASCII %d, plus longue ligne %d colonnes (<= 100), signes pour cent %d, tabulations %d' % (n_asc, long_max, ACTE.count('%'), ACTE.count('\t')))

# ------------------------------------------------------------------ index de TOUT ce que je detiens (fichiers, membres de zip, registre)
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
try:
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
chk('C04', len(paires) >= 30 and not non_res and not mauvais_nom and not mauvais_reg,
    'nn.1 : %d couples (nom, canon) lus dans l acte, tous retrouves chez moi, le nom est celui d une piece de ce canon, ceux du registre sous leur chemin public ; '
    'non resolus %s ; noms differents %s ; chemins du registre faux %s' % (len(paires), non_res, mauvais_nom, mauvais_reg))
tous = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', ACTE)))
non_res_tous = [c for c in tous if c not in IDX]
chk('C05', len(tous) >= 40 and not non_res_tous,
    '%d empreintes de 16 chiffres citees dans tout l acte (dont les 12 sorties de points, les lots et les pieces de m1), toutes recalculees de pieces ou de manifestes que je detiens ; non resolues %s' % (
        len(tous), non_res_tous))

# ------------------------------------------------------------------ mes sources
MAspec = importlib.util.spec_from_file_location('feuille_ma', os.path.join(CTRL, 'feuille_independante_ter_machine2_v1.py'))
MA = importlib.util.module_from_spec(MAspec)
MAspec.loader.exec_module(MA)
JU = list(MA.JUGES)
ABS = list(MA.ABSORBEURS)
DEP = J(os.path.join(CLONE, 'journal', 'sonde_ordre2.json'))
VO = J(os.path.join(CLONE, 'journal', 'verdict_ordre2.json'))
V1 = J(os.path.join(RUN, 'verdict_ter.json'))
VI = J(os.path.join(RUN, 'verdict_ter_instrument.json'))
GEL = rt(os.path.join(GELM1, 'qualification_EB_ter_pre_enregistrement_v1.md'))
GN = norm(GEL)
dep = {p['id']: p for p in DEP['points']}
PT, FIL = {}, {}
for f in sorted(glob.glob(os.path.join(RUN, 'sonde_ter_point_*.json'))):
    s = J(f)
    FIL[os.path.basename(f)] = s
    for p in s['points']:
        PT[p['id']] = p
E = {}       # (id, rang) -> jugement de MA feuille
for i in JU:
    for e in sorted(PT[i]['etats'], key=lambda x: x['rang']):
        idx = [x['rang'] for x in dep[i]['etats']].index(e['rang'])
        g = dep[i]['etats'][idx]['Gamma_2D']['3']
        E[(i, e['rang'])] = {'g': g, 'e': e, 'j': MA.juger_etat(e['traj'], g), 'n12': (e['n1'], e['n2']), 'g_sonde': e['G_dep']['3']}
CLES = sorted(E, key=lambda k: (JU.index(k[0]), k[1]))
GA = lambda k: E[k]['j']['plateaux']['A']['Gamma_pl']
LNDEP = {k: math.log(E[k]['g'] / GA(k)) for k in CLES}
par = {i: [k for k in CLES if k[0] == i] for i in JU}
nj = len(CLES)
nq = sum(1 for k in CLES if E[k]['j']['statut'] == 'QUALIFIE')
nlu = sum(1 for k in CLES if E[k]['j']['lu'] is True)
fmt_fact = lambda s: (str(Fraction(s).numerator) if Fraction(s).denominator == 1 else '%d/%d' % (Fraction(s).numerator, Fraction(s).denominator))
seuil9 = -(-nj * 9 // 10)

# ------------------------------------------------------------------ C06 : nn.0, nn.4, nn.5 (comptes)
rows1, rows2 = [], []
for i in JU:
    p = PT[i]
    ks = par[i]
    k0 = (i, 0)
    rows1.append('%s %s %s %+.2f %.2e %d %d %d %d %s %.3e %+.4f' % (i, p['w2'], fmt_fact(p['facteur']), float(Fraction(p['w2']) - 2), p['g'], p['r_c'], len(ks),
                                                                      sum(1 for k in ks if E[k]['j']['statut'] == 'QUALIFIE'), sum(1 for k in ks if E[k]['j']['lu'] is True),
                                                                      E[k0]['j']['statut'], GA(k0), LNDEP[k0]))
    et = {x: max(E[k]['j']['plateaux'][x]['etalement'] for k in ks) for x in ABS}
    ec = {x: max(abs(math.log(E[k]['j']['plateaux'][x]['Gamma_pl'] / GA(k))) for k in ks) for x in 'BCD'}
    cs = [abs(LNDEP[k]) for k in ks]
    rows2.append('%s %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f %.4f' % (i, et['A'], et['B'], et['C'], et['D'], ec['B'], ec['C'], ec['D'], statistics.median(cs), max(cs)))
n_dep = sum(len(dep[i]['etats']) for i in JU)
P10 = FIL['sonde_ter_point_C1.json']['reglage']['plancher10']
n_sous = sum(1 for i in JU for x in dep[i]['etats'] if not x['Gamma_2D']['3'] > P10)
n_pl = {x: sum(1 for k in CLES if E[k]['j']['plateaux'][x]['statut'] == 'PLATEAU') for x in ABS}
n_acc = {x: sum(1 for k in CLES if E[k]['j']['plateaux'][x]['statut'] == 'PLATEAU' and not MA.accord(E[k]['j']['plateaux'][x]['Gamma_pl'], GA(k))) for x in 'BCD'}
n_nl = sum(1 for k in CLES if E[k]['j']['statut'] == 'NON LISIBLE')
lus_q = {i: E[(i, 0)]['j']['statut'] for i in JU}
n_lu_pts = sum(1 for i in JU if E[(i, 0)]['j']['lu'] is True)
phr = ['Reponse de la feuille : ESTIMATEUR QUALIFIE. L\'etat lu est QUALIFIE aux douze points ; %d etats juges sur %d le sont, pour un seuil de %d. Issue separee : LA LECTURE DEPOSEE EST SUR '
       'LE PLATEAU A NEUF ETATS SUR DIX AU MOINS (%d sur %d) ; a l\'etat lu elle l\'est a %s points sur douze.' % (nq, nj, seuil9, nlu, nj, {11: 'onze', 12: 'douze'}.get(n_lu_pts, '?')),
       'Aux douze points : %d etats au depot, %d juges, %d sous dix planchers. Par absorbeur : PLATEAU a %d etats sur %d sous A, sous B, sous C et sous D ; accord a A manque a %d etat pour B, %d pour C, %d pour D.' % (
           n_dep, nj, n_dep - nj, n_pl['A'], nj, n_acc['B'], n_acc['C'], n_acc['D']),
       'La cascade (gel, section 8) : l\'instrument tient ; les douze points sont presents ; l\'etat lu est QUALIFIE aux douze points ; %d etats juges sur %d sont QUALIFIES, soit plus des neuf dixiemes '
       '(seuil %d) : ESTIMATEUR QUALIFIE. Aucun etat n\'est NON LISIBLE.' % (nq, nj, seuil9),
       'VERDICT : ESTIMATEUR QUALIFIE. ISSUE SEPAREE : LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS.']
mq1 = [r for r in rows1 if norm(r) not in AN]
mq2 = [r for r in rows2 if norm(r) not in AN]
mq = manque(phr, AN)
v_ma = MA.cascade(VI['instrument'] == 'TIENT', lus_q, nj, nq)
i_ma = MA.issue_consigne(n_pl['A'], nlu)
chk('C06', not mq1 and not mq2 and not mq and v_ma == 'ESTIMATEUR QUALIFIE' and i_ma == V1['issue_depot'] and n_nl == 0 and (nj, nq, nlu) == (137, 136, 130) and n_dep == 168 and n_sous == n_dep - nj
    and n_pl == {'A': 137, 'B': 137, 'C': 137, 'D': 137},
    'nn.0, nn.4, nn.5 : ma feuille (ecrite du texte du gel) rend %s / %s sur les sorties brutes (%d etats, %d QUALIFIES, %d sur le plateau de la consigne (e), %d NON LISIBLES) ; '
    'les 12 lignes du premier tableau (w2, facteur, delta, g, r_c, juges, qualifies, (e), etat lu, Gamma_pl(A), ln) et les 12 du second (etalements, ecarts a A, consigne (e)) recalculees ; '
    'lignes absentes %s %s ; phrases absentes %s' % (v_ma, i_ma, nj, nq, nlu, n_nl, mq1, mq2, mq))

# ------------------------------------------------------------------ C07 : les deux verdicts rejoues par machine 1
V1m = json.loads(zl.read('verdict_ter_rejoue_machine1.json'))
VIm = json.loads(zl.read('verdict_ter_instrument_rejoue_machine1.json'))


def feuilles(a, b, chemin, out):
    if isinstance(a, dict):
        if not isinstance(b, dict) or sorted(a) != sorted(b):
            out.append((chemin, 'STRUCTURE', None))
            return
        for k in a:
            feuilles(a[k], b[k], chemin + [k], out)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            out.append((chemin, 'STRUCTURE', None))
            return
        for n, (x, y) in enumerate(zip(a, b)):
            feuilles(x, y, chemin + [n], out)
    else:
        out.append((chemin, a, b))


nf, nd_, relG, absL, autres, struct = 0, 0, 0.0, 0.0, [], 0
for A_, B_ in ((V1, V1m), (VI, VIm)):
    out = []
    feuilles(A_, B_, [], out)
    for chemin, a, b in out:
        if a == 'STRUCTURE':
            struct += 1
            continue
        if isinstance(a, float):
            nf += 1
            if a != b:
                nd_ += 1
                cle = str(chemin[-1])
                if cle == 'Gamma_pl':
                    relG = max(relG, abs(a / b - 1.0))
                elif cle.startswith('ecart'):
                    absL = max(absL, abs(a - b))
                else:
                    autres.append((cle, a, b))
        elif a != b:
            struct += 1
log_ma = rd(os.path.join(RUN, 'lecture_ter.log')).replace(b'\r\n', b'\n')
log_ma_i = rd(os.path.join(RUN, 'lecture_ter_instrument.log')).replace(b'\r\n', b'\n')
l1 = zl.read('lecture_ter_rejouee_machine1.log').replace(b'\r\n', b'\n')
l2 = zl.read('lecture_ter_instrument_rejouee_machine1.log').replace(b'\r\n', b'\n')
fh = lambda x, nd=2: ('%.' + str(nd - 1) + 'e') % x
phr = ['Les deux verdicts JSON different de ceux de BOCAL4 par %d flottants sur %d : des Gamma_pl, de %s au plus en relatif, et des ecarts logarithmiques, de %s au plus en absolu' % (
    nd_, nf, fh(haut(relG)), fh(haut(absL)))]
mq = manque(phr, AN)
chk('C07', not mq and not autres and struct == 0 and l1 == log_ma and l2 == log_ma_i and emp(l1)[0] == '4db341d830781530' and emp(l2)[0] == 'a5cb7f6b8d14ffc5',
    'nn.2 (a) : mes deux verdicts JSON contre ceux que machine 1 a rejoues : %d flottants sur %d (les deux JSON), %d differents, plus grand ecart relatif de Gamma_pl %.3e, plus grand ecart '
    'absolu des ecarts logarithmiques %.3e, differences de structure %d, autres cles %s ; les deux journaux sont les miens a l octet pres (canons %s et %s) ; absentes %s' % (
        nd_, nf, nd_, relG, absL, struct, autres[:3], emp(l1)[0], emp(l2)[0], mq))

# ------------------------------------------------------------------ C08 : nn.2, mes journaux (pilote, plateforme, certification)
pil = rt(os.path.join(RUN, 'pilote_EB_ter.log'))
fins = re.findall(r'^(\S+ \S+) FIN\s+(\S+(?: \S+)?)\s+code=(\d+)(?: duree=(\d+) s)?', pil, re.M)
pts_d = {m.group(1): int(m.group(2)) for m in re.finditer(r'FIN\s+point_(\w+)\s+code=0 duree=(\d+) s', pil)}
t_deb = re.search(r'^(\S+ \S+) DEBUT DU PILOTE', pil, re.M).group(1)
t_fin = re.search(r'^(\S+ \S+) FIN DU PILOTE', pil, re.M).group(1)
t_vi = re.search(r'^(\S+ \S+) VERDICT DE L INSTRUMENT : TIENT', pil, re.M).group(1)
n_can = len(re.findall(r'^\S+ \S+ canon .* OK$', pil, re.M))
tot = int(re.search(r'DUREE TOTALE DU RUN : (\d+) s', pil).group(1))
d_et = {m.group(1): int(m.group(2)) for m in re.finditer(r'FIN\s+(etage0|ancres|etage1)\s+code=0 duree=(\d+) s', pil)}
f = lambda t: time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S'))
mm_c = os.path.getmtime(os.path.join(ROOT, 'MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt'))
hms = lambda t: '%d h %02d min %02d s' % (int(t[11:13]), int(t[14:16]), int(t[17:19]))
sc = time.localtime(mm_c)
scelle = '%d h %02d min %02d s' % (sc.tm_hour, sc.tm_min, sc.tm_sec)
sp0 = FIL['sonde_ter_point_L3.json']['plateforme']
pf_ok = (sp0['systeme'] == 'Windows' and sp0['machine'] == 'AMD64' and sp0['coeurs'] == 16 and sp0['python'] == '3.11.9' and sp0['numpy'] == '2.2.6' and sp0['scipy'] == '1.15.3'
         and all(v == '1' for v in sp0['fils'].values()) and sp0['levier'] is None)
secteur = re.search(r"batterie \(BatteryStatus WMI[^\n]*: '2'", pil) is not None
cj = rt(os.path.join(CTRL, 'controles_gel_ter_machine2_v1.log'))
selft = rt(os.path.join(CTRL, 'selftest_feuille_ter_rejoue_machine2.log'))
banc_r = rt(os.path.join(CTRL, 'banc_feuille_ter_rejoue_machine2.log'))
nb_codes0 = sum(1 for x in fins if x[2] == '0')
pmin = min(pts_d, key=pts_d.get)
phr = ['0 morsure, six observations ; ses 13 controles de lecture du gel, dont 12 tiennent, le treizieme etant son observation O-1',
       'lot scelle a %s' % scelle,
       'par un pilote qui verifie %d canons et refuse de jouer si le dossier de sortie existe : debut a %s, fin a %s, %d secondes ; les dix-sept appels a code 0 ; aucun appel interrompu, relance ou rejoue.' % (
           n_can, hms(t_deb), hms(t_fin), tot),
       'Etape 1 : etage0 (%d s), ancres (%d s), etage1 (%d s), trois processus' % (d_et['etage0'], d_et['ancres'], d_et['etage1']),
       'un processus par point, de %d s (%s) a %d s' % (min(pts_d.values()), pmin, max(pts_d.values())),
       'BOCAL4, Windows AMD64, 16 coeurs, python 3.11.9, numpy 2.2.6, scipy 1.15.3, un fil par processus, sur secteur.',
       'Selftest de la feuille : 68 sur 68, sur BOCAL4 et chez machine 1.']
mq = manque(phr, AN)
rf = rt(os.path.join(ROOT, 'certif_EB_ter', 'lancer_EB_ter_machine2_v1.py'))
dur_s = f(t_fin) - f(t_deb)
chk('C08', not mq and nb_codes0 == 17 and len(fins) == 17 and n_can == 10 and tot == round(dur_s) and f(t_deb) > mm_c and 'py -3.11 -P' in rt(os.path.join(ROOT, 'POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md'))
    and 'CONTROLES : 13, dont 12 tiennent, 1 mordent' in cj and 'selftest : 68 tenus sur 68' in selft and 'BANC : 43 alterations, 43 mordues' in banc_r and pf_ok and secteur and 'existe' in rf,
    'nn.2 : mon journal de pilote (debut %s, fin %s, %d s, %d appels dont %d a code 0, %d canons verifies, etage0 %s, point le plus court %s %d s, le plus long %d s), la plateforme consignee dans la sonde, '
    'le lot de certification scelle a %s (fichier manifeste) avant le debut ; mes 13 controles dont 12 tiennent ; selftest 68/68 ; banc 43/43 ; secteur %s ; phrases absentes %s' % (
        t_deb, t_fin, tot, len(fins), nb_codes0, n_can, d_et, pmin, min(pts_d.values()), max(pts_d.values()), scelle, secteur, mq))

# ------------------------------------------------------------------ C09 : nn.2 (b), le rejeu de machine 1 contre MON run
def lectures(traj_a, traj_b):
    n, relmax, dE, diff_it, nonsuiv, statut = 0, 0.0, 0.0, 0, 0, 0
    for x in ABS:
        for k in range(-3, 9):
            a, b = traj_a[x][str(k)], traj_b[x][str(k)]
            n += 1
            if not (a['suivi'] and b['suivi']):
                nonsuiv += 1
                continue
            relmax = max(relmax, abs(a['gamma'] / b['gamma'] - 1.0))
            dE = max(dE, abs(a['E_re'] - b['E_re']))
            if a['iterations'] != b['iterations']:
                diff_it += 1
    return n, relmax, dE, diff_it, nonsuiv


tot_l, rel_all, dE_all, dit_all, ns_all, n_et_l3, n_et_aut, lec_l3, lec_aut = 0, 0.0, 0.0, 0, 0, 0, 0, 0, 0
plat_m1 = set()
l3m = json.loads(zl.read('sonde_ter_point_L3_rejeu_machine1.json'))
plat_m1.add((l3m['plateforme']['systeme'], l3m['plateforme']['python'], l3m['plateforme']['numpy'], l3m['plateforme']['scipy']))
for e in l3m['points'][0]['etats']:
    mine = [x for x in PT['L3']['etats'] if x['rang'] == e['rang']][0]
    n, r, d, di, ns = lectures(mine['traj'], e['traj'])
    tot_l += n
    lec_l3 += n
    n_et_l3 += 1
    rel_all, dE_all, dit_all, ns_all = max(rel_all, r), max(dE_all, d), dit_all + di, ns_all + ns
choisis = {}
for i in JU:
    if i == 'L3':
        continue
    rj = json.loads(zl.read('rejeu_partiel_%s.json' % i))
    plat_m1.add((rj['plateforme']['systeme'], rj['plateforme']['python'], rj['plateforme']['numpy'], rj['plateforme']['scipy']))
    choisis[i] = [e['rang'] for e in rj['point']['etats']]
    for e in rj['point']['etats']:
        mine = [x for x in PT[i]['etats'] if x['rang'] == e['rang']][0]
        n, r, d, di, ns = lectures(mine['traj'], e['traj'])
        tot_l += n
        lec_aut += n
        n_et_aut += 1
        rel_all, dE_all, dit_all, ns_all = max(rel_all, r), max(dE_all, d), dit_all + di, ns_all + ns
hors_e = sorted({(k[0], k[1]) for k in CLES if abs(LNDEP[k]) > MA.TAU and k[0] != 'L3'})
attendu_ch = {i: sorted(set([0] + [r for (ii, r) in hors_e if ii == i])) for i in JU if i != 'L3'}
pl_txt = sorted(plat_m1)
phr = ['la sonde certifiee, telle quelle, au point L3 (%d etats, %d lectures)' % (n_et_l3, lec_l3), 'pour %d etats des onze autres points : l\'etat lu de chacun, et les etats ou la consigne (e) ne tient pas (%d lectures)' % (n_et_aut, lec_aut),
       'Sur les %d lectures, toutes suivies des deux cotes : memes statuts, plus grand ecart relatif de largeur %s, pour une tolerance de 1e-6 ; meme nombre d\'iterations a chaque lecture. Conteneur Linux, python 3.13.18, numpy 2.5.3, scipy 1.18.1.' % (
           tot_l, fh(haut(rel_all)))]
mq = manque(phr, AN)
chk('C09', not mq and tot_l == 1392 and ns_all == 0 and dit_all == 0 and rel_all < 1e-6 and choisis == attendu_ch and pl_txt == [('Linux', '3.13.18', '2.5.3', '1.18.1')],
    'nn.2 (b) : je compare, lecture par lecture, les 1392 lectures du rejeu de machine 1 (L3 en entier, 15 etats des onze autres points) a MES sorties : plus grand ecart relatif de largeur %.3e '
    '(l acte l ecrit arrondi vers le haut, 1.1e-13 ; son journal dit 1.02e-13), plus grand ecart d energie %.2e, lectures non suivies %d, nombres d iterations differents %d ; les etats '
    'rejoues sont l etat lu de chaque point plus les etats hors consigne (e) : %s ; plateformes lues %s ; phrases absentes %s' % (rel_all, dE_all, ns_all, dit_all, choisis == attendu_ch, pl_txt, mq))

# ------------------------------------------------------------------ C10 : nn.3, l'instrument et les gardes
e0, an, e1 = VI['etage0'], VI['ancres'], VI['etage1']
tp = e1['detail']['TP']
tn = e1['detail']['TN']
tp_max = {j: max(tp[j][x]['ecart_ln'] for x in ABS) for j in ('j06', 'j08')}
tp_born = {j: MA.TAU + tp[j]['u_ref'] for j in ('j06', 'j08')}
tn_et = [tn[a][x]['etalement'] for a in tn for x in ABS]
tn_g3 = []
for a in J(os.path.join(RUN, 'sonde_ter_etage1.json'))['temoin_negatif']:
    for x in ABS:
        tn_g3.append(a['traj'][x]['3']['gamma'])
it, pmn, rmx, n2, ns2 = {}, 9.0, 0.0, 0, 0
for i in JU:
    for e in PT[i]['etats']:
        for x in ABS:
            for k, rec in e['traj'][x].items():
                n2 += 1
                ns2 += 0 if rec['suivi'] else 1
                it[rec['iterations']] = it.get(rec['iterations'], 0) + 1
                pmn = min(pmn, rec['poids_site'])
                lam = math.hypot(rec['E_re'], rec['gamma_im'] / 2.0)
                rmx = max(rmx, rec['residu'] / max(1.0, lam))
lect_instr = e0['lectures'] + an['lectures'] + len(tp) * len(ABS) * 12 + len(tn) * len(ABS) * 12
cons = ''.join(rt(p) for p in glob.glob(os.path.join(RUN, 'console_*.log')))
sing = len(re.findall(r'singul', cons + pil, re.I))
phr = ['84 lectures sur 84 dans la tolerance ; plus grand ecart absolu %s, plus grand ecart relatif au-dessus de mille planchers %s.' % ('%.2e' % e0['pire_ecart_absolu'], '%.1e' % e0['pire_ecart_relatif_au_dessus_de_mille_planchers']),
       '%d lectures sur %d, memes statuts de suivi ; plus grand |ln| a la reference de machine 1 : %s, pour une tolerance de 1e-6.' % (an['lectures'], an['lectures'], '%.1e' % an['pire_ecart_ln']),
       'PLATEAU aux huit (couplage, absorbeur) ; |ln(Gamma_pl / Gamma_ref)| vaut au plus %.4f a j = 6 et %.4f a j = 8, pour des bornes de %.4f et %.4f.' % (tp_max['j06'], tp_max['j08'], tp_born['j06'], tp_born['j08']),
       'PAS DE PLATEAU aux huit (ancre, absorbeur). L\'etalement de sa meilleure fenetre va de %.2f a %.2f, la ou une largeur proportionnelle a eta donne 15 ; ses largeurs vont de %s a %s a k = 3.' % (
           math.floor(min(tn_et) * 100) / 100.0, math.ceil(max(tn_et) * 100) / 100.0, fh(bas(min(tn_g3))), fh(haut(max(tn_g3)))),
       'G-T5 : %d, %d, %d et %d lectures a l\'instrument, %d a l\'etage 2.' % (e0['lectures'], an['lectures'], len(tp) * len(ABS) * 12, len(tn) * len(ABS) * 12, n2),
       'Les %d lectures de l\'etage 2 sont toutes suivies : %d en deux iterations, %d en trois, %d en quatre ; poids au site au moins %.3f pour un seuil de 0.5 ; residu rapporte a max(1, |lambda|) au plus %s pour un critere de 1e-11. '
       'La garde de singularite du bloc ne s\'est declenchee a aucune des %d lectures du run.' % (n2, it[2], it[3], it[4], math.floor(pmn * 1000) / 1000.0, fh(haut(rmx)), n2 + lect_instr),
       'G-T8 : machine 2 retrouve la matrice du moteur dans l\'assemblage du bloc, ecart 0 sur 12 assemblages.']
mq = manque(phr, AN)
blog = rt(os.path.join(CTRL, 'bloc_et_lecteur_ter_machine2_v1.log'))
ok_g8 = ('ecart 0' in blog or re.search(r'12 assemblages', blog) is not None)
chk('C10', not mq and e0['lectures'] == 84 and an['lectures'] == 192 and ns2 == 0 and n2 == 6576 and pmn > 0.5 and rmx <= 1e-11 and sing == 0 and (it[2], it[3], it[4]) == (6461, 110, 5) and e0['tient'] and an['tient']
    and all(tp[j][x]['statut'] == 'PLATEAU' for j in tp for x in ABS) and all(tn[a][x]['statut'] == 'PAS DE PLATEAU' for a in tn for x in ABS) and ok_g8,
    'nn.3 : mon verdict d instrument (etage 0 : %d lectures, pire ecart absolu %.3e, relatif %.3e ; ancres : %d, pire |ln| %.3e ; temoin positif %.4f et %.4f pour des bornes %.4f et %.4f ; temoin negatif '
    'etalements de %.4f a %.4f, largeurs a k = 3 de %.2e a %.2e) ; les %d lectures de l etage 2 relues une a une (iterations %s, poids au site min %.6f, residu relatif max %.3e, non suivies %d) ; '
    'singularite : %d mention dans mes journaux ; mon bloc : ecart 0 sur 12 assemblages %s ; phrases absentes %s' % (
        e0['lectures'], e0['pire_ecart_absolu'], e0['pire_ecart_relatif_au_dessus_de_mille_planchers'], an['lectures'], an['pire_ecart_ln'], tp_max['j06'], tp_max['j08'], tp_born['j06'], tp_born['j08'],
        min(tn_et), max(tn_et), min(tn_g3), max(tn_g3), n2, dict(sorted(it.items())), pmn, rmx, ns2, sing, ok_g8, mq))

# ------------------------------------------------------------------ C11 : nn.5, nn.6, la non qualification de L3 rang 5
et_med = {x: statistics.median(E[k]['j']['plateaux'][x]['etalement'] for k in CLES) for x in ABS}
et_max = {x: max(E[k]['j']['plateaux'][x]['etalement'] for k in CLES) for x in ABS}
ec_all = {x: [abs(math.log(E[k]['j']['plateaux'][x]['Gamma_pl'] / GA(k))) for k in CLES] for x in 'BCD'}
q_ = [k for k in CLES if E[k]['j']['statut'] == 'QUALIFIE']
nonq = [k for k in CLES if E[k]['j']['statut'] != 'QUALIFIE']
gpl = [GA(k) for k in q_]
k5 = ('L3', 5)
j5 = E[k5]['j']
trajC = E[k5]['e']['traj']['C']
wins = [(rap, k0, v) for (rap, k0, v) in MA.fenetres(trajC) if rap <= MA.SEUIL_PLATEAU]
val = lambda v: math.exp(math.fsum(math.log(x) for x in v) / 5.0)
wins = sorted(wins, key=lambda t: (t[0], t[1]))
ln_autre = abs(math.log(val(wins[1][2]) / GA(k5))) if len(wins) > 1 else None
hors_l3 = [k for k in CLES if k[0] != 'L3']
n_hl3 = len(hors_l3)
mxl3 = {x: max(E[k]['j']['plateaux'][x]['etalement'] for k in CLES if k[0] == 'L3') for x in ABS}
mxo = {x: max(E[k]['j']['plateaux'][x]['etalement'] for k in hors_l3) for x in ABS}
arg_o = {x: [k[0] for k in hors_l3 if E[k]['j']['plateaux'][x]['etalement'] == mxo[x]] for x in ABS}
glob_max = max(((E[k]['j']['plateaux'][x]['etalement'], k, x) for k in CLES for x in ABS))
ec_C_sans5 = max(abs(math.log(E[k]['j']['plateaux']['C']['Gamma_pl'] / GA(k))) for k in CLES if k != k5)
phr = ['Etalement de la meilleure fenetre, mediane et plus grand, sur les %d etats : %.4f et %.4f sous A, %.4f et %.4f sous B, %.4f et %.4f sous C, %.4f et %.4f sous D, pour un seuil de 0.05.' % (
           nj, et_med['A'], et_max['A'], et_med['B'], et_max['B'], et_med['C'], et_max['C'], et_med['D'], et_max['D']),
       'Ecart a A, |ln|, mediane et plus grand : %.4f et %.4f pour B, %.4f et %.4f pour C, %.4f et %.4f pour D.' % (
           statistics.median(ec_all['B']), max(ec_all['B']), statistics.median(ec_all['C']), max(ec_all['C']), statistics.median(ec_all['D']), max(ec_all['D'])),
       'ces valeurs, de %s a %s, sont au verdict (verdict_ter.json)' % (fh(bas(min(gpl))), fh(haut(max(gpl)))),
       'Pour une largeur DEPOSEE, il n\'est leve que si, de plus, la consigne (e) tient a cet etat : %d etats (nn.7).' % sum(1 for k in q_ if E[k]['j']['lu'] is True),
       'Un seul etat n\'est pas QUALIFIE : L3, rang 5, etiquette (%d, %d), G_dep %.2e. Il a un PLATEAU sous les quatre absorbeurs ; il echoue a l\'epreuve (c) : |ln(Gamma_pl(C) / Gamma_pl(A))| = %.4f pour tau = 0.05. '
       'B et D s\'accordent a A a %.4f et %.4f.' % (E[k5]['n12'][0], E[k5]['n12'][1], E[k5]['g'], abs(math.log(j5['plateaux']['C']['Gamma_pl'] / GA(k5))),
                                                     abs(math.log(j5['plateaux']['B']['Gamma_pl'] / GA(k5))), abs(math.log(j5['plateaux']['D']['Gamma_pl'] / GA(k5)))),
       'sous C (F1, 100 couches), deux fenetres ont un PLATEAU. Celle que la regle retient, la plus plate, est du cote fort (k0 = %d, etalement %.4f, valeur %.3e) ; l\'autre (k0 = %d, etalement %.4f, valeur %.3e) est a %.4f de A.' % (
           wins[0][1], float(wins[0][0]) - 1, val(wins[0][2]), wins[1][1], float(wins[1][0]) - 1, val(wins[1][2]), ln_autre),
       'Les plus grands etalements du run y sont, sous les quatre absorbeurs : %.4f, %.4f, %.4f et %.4f ; aux onze autres points, sur %d etats, ils sont %.4f, %.4f, %.4f et %.4f (tous a L4).' % (
           mxl3['A'], mxl3['B'], mxl3['C'], mxl3['D'], n_hl3, mxo['A'], mxo['B'], mxo['C'], mxo['D']),
       'La plus petite marge du run est a %s, rang %d, sous %s : etalement %.4f pour un seuil de 0.05.' % (glob_max[1][0], glob_max[1][1], glob_max[2], glob_max[0]),
       'Apres le %.4f de L3 rang 5, le plus grand ecart de C a A est %.4f.' % (abs(math.log(j5['plateaux']['C']['Gamma_pl'] / GA(k5))), ec_C_sans5),
       'Les treize autres etats de L3 sont QUALIFIES, son etat lu compris.']
mq = manque(phr, AN)
chk('C11', not mq and nonq == [k5] and len(wins) == 2 and all(arg_o[x] and set(arg_o[x]) == {'L4'} for x in ABS) and glob_max[1:] == (('L3', 7), 'D')
    and sum(1 for k in par['L3'] if E[k]['j']['statut'] == 'QUALIFIE') == 13 and E[('L3', 0)]['j']['statut'] == 'QUALIFIE',
    'nn.5, nn.6 : etalements (mediane, plus grand) par absorbeur sur %d etats, ecarts a A, valeurs de plateau de %.2e a %.2e, 129 etats ou la consigne (e) tient parmi les qualifies ; '
    'L3 rang 5 (seul NON QUALIFIE : %s) ; ses deux fenetres sous C relues de mes douze barreaux (k0 %d et %d), la seconde a %.4f de A (MORSURE M-1 de l acte : lecture apres coup, dite par m1) ; '
    'maxima de L3 et des onze autres points (a %s) ; plus petite marge %s ; phrases absentes %s' % (nj, min(gpl), max(gpl), nonq, wins[0][1], wins[1][1], ln_autre, {x: arg_o[x] for x in ABS}, glob_max, mq))

# ------------------------------------------------------------------ C12 : nn.5, la phrase "plus plats que ceux des points de reglage"
rg = [float(x) for x in re.findall(r'etalement de la meilleure fenetre sous [ABCD] : mediane [0-9.]+, plus grand ([0-9.]+) ;', GEL)]
rg_med = [float(x) for x in re.findall(r'etalement de la meilleure fenetre sous [ABCD] : mediane ([0-9.]+), plus grand [0-9.]+ ;', GEL)]
plus_plats_max = [et_max[x] < rg[n] for n, x in enumerate(ABS)]
plus_plats_med = [et_med[x] < rg_med[n] for n, x in enumerate(ABS)]
phr = ['Les plateaux des douze points sont plus plats que ceux des points de reglage, dont les plus grands etalements etaient %.4f, %.4f, %.4f et %.4f.' % tuple(rg)]
mq = manque(phr, AN)
chk('C12', not mq and all(plus_plats_max),
    'nn.5 : la phrase "plus plats que ceux des points de reglage, dont les plus grands etalements etaient 0.0409, 0.0442, 0.0657 et 0.0410" (section 4 du gel : %s) ; mes plus grands etalements sous A, B, C, D : '
    '%.4f, %.4f, %.4f, %.4f ; plus plats par le plus grand : %s ; par la mediane (gel %s contre mes %.4f %.4f %.4f %.4f) : %s ; phrase de l acte presente : %s' % (
        rg, et_max['A'], et_max['B'], et_max['C'], et_max['D'], plus_plats_max, rg_med, et_med['A'], et_med['B'], et_med['C'], et_med['D'], plus_plats_med, not mq))

# ------------------------------------------------------------------ C13 : nn.7, la lecture deposee (consigne (e))
ab = sorted((abs(LNDEP[k]), k) for k in CLES)
hors = [k for k in CLES if abs(LNDEP[k]) > MA.TAU]
npos = sum(1 for k in CLES if LNDEP[k] > 0)
nneg = sum(1 for k in CLES if LNDEP[k] < 0)
lu_txt = ', '.join('%s %+.4f' % (i, LNDEP[(i, 0)]) for i in JU)
hors_txt = ', '.join('%s rang %d (%.4f)' % (k[0], k[1], abs(LNDEP[k])) for k in hors)
phr = ['|ln(G_dep / Gamma_pl(A))| a pour mediane %.4f et pour plus grande valeur %.4f.' % (statistics.median(abs(LNDEP[k]) for k in CLES), max(abs(LNDEP[k]) for k in CLES)),
       'Elle depasse tau a %d etats : %s. Tous les %d sont QUALIFIES' % (len(hors), hors_txt, len(hors)),
       'A l\'etat lu, ln(G_dep / Gamma_pl(A)) vaut : %s.' % lu_txt,
       'La lecture deposee de l\'etat lu est sur le plateau a onze points ; a L4 elle est au-dessus de son plateau de %d pour cent.' % round((math.exp(LNDEP[('L4', 0)]) - 1) * 100),
       'la lecture deposee est au-dessus du plateau a %d etats, au-dessous a %d ; la mediane de ln(G_dep / Gamma_pl(A)) est %.4f.' % (npos, nneg, statistics.median(LNDEP.values())),
       'elle est a tau pres la largeur du plateau a %d etats sur %d, et a un facteur %.2f pres partout.' % (nlu, nj, math.exp(max(abs(LNDEP[k]) for k in CLES)))]
mq = manque(phr, AN)
chk('C13', not mq and len(hors) == 7 and all(E[k]['j']['statut'] == 'QUALIFIE' for k in hors) and n_lu_pts == 11 and (npos, nneg) == (61, 76),
    'nn.7 : la consigne (e) recalculee des %d etats (G_dep du depot au registre, Gamma_pl(A) de mes sorties) : mediane, maximum, les %d etats au-dela de tau (%s), l etat lu aux douze points, signes %d et %d, '
    'a un facteur %.4f pres ; phrases absentes %s' % (nj, len(hors), hors_txt, npos, nneg, math.exp(max(abs(LNDEP[k]) for k in CLES)), mq))

# ------------------------------------------------------------------ C14 : nn.8, les annonces
sec11 = GN[GN.index('## 11. Annonces'):GN.index('## 12. Deroulement')]
pa1 = re.search(r"A-1 le verdict\. ESTIMATEUR QUALIFIE : (0\.\d+) ; QUALIFIE A L'ETAT LU : (0\.\d+) ; QUALIFIE PAR POINT : (0\.\d+) ; NON QUALIFIE : (0\.\d+) ; NON LISIBLE : (0\.\d+) ; NON CONCLUANT D'INSTRUMENT : (0\.\d+)\.", sec11)
pa2 = re.search(r"SUR LE PLATEAU a tous les etats : (0\.\d+) ; A NEUF ETATS SUR DIX AU MOINS : (0\.\d+) ; PAS PARTOUT : (0\.\d+)\.", sec11)
sec11r = GEL[GEL.index('## 11. Annonces'):GEL.index('## 12. Deroulement')]
prob = {}
for n in range(3, 11):
    m = re.search(r'^  A-%d\s+(?:.*?) : (0\.\d\d)\.' % n, sec11r, re.M | re.S)
    prob[n] = m.group(1)
neg = ('C1', 'C2', 'M1', 'M2', 'L1', 'L2')
nq_par = {i: sum(1 for k in par[i] if E[k]['j']['statut'] == 'NON QUALIFIE') for i in JU}
sans_pl = {x: sum(1 for k in CLES if E[k]['j']['plateaux'][x]['statut'] != 'PLATEAU') for x in ABS}
a5 = max(E[k]['j']['plateaux'][x]['etalement'] for k in CLES if k[0] in neg for x in 'AB')
a6 = max(abs(math.log(E[k]['j']['plateaux']['B']['Gamma_pl'] / GA(k))) for k in CLES)
a9 = statistics.median(abs(LNDEP[k]) for k in CLES)
VRAI = {3: all(lus_q[i] == 'QUALIFIE' for i in JU if i != 'L3'), 4: nq_par['L3'] == max(nq_par.values()), 5: a5 <= 0.02, 6: a6 <= 0.02, 7: VI['instrument'] == 'TIENT',
        8: sans_pl['C'] == max(sans_pl.values()) or max(sans_pl.values()) == 0, 9: 0.01 <= a9 <= 0.04, 10: n_nl <= 3}
mes = [('A-%d' % n, '(%s)' % prob[n], 'VRAIE' if VRAI[n] else 'FAUSSE') for n in range(3, 11)]
act8 = []
for ln in LIGNES:
    m = re.match(r'^\s+(A-\d+)\s+\((0\.\d+)\) .*?\s(VRAIE|FAUSSE)(\s|$)', ln)
    if m:
        act8.append((m.group(1), '(%s)' % m.group(2), m.group(3)))
somme = sum(float(prob[n]) for n in range(3, 11))
phr = ['A-1 : la plume donnait %s a ESTIMATEUR QUALIFIE, %s a QUALIFIE A L\'ETAT LU, %s a QUALIFIE PAR POINT, %s a NON QUALIFIE, %s a NON LISIBLE, %s a NON CONCLUANT D\'INSTRUMENT.' % pa1.groups(),
       'A-2 : elle donnait %s a SUR LE PLATEAU a tous les etats, %s a A NEUF ETATS SUR DIX AU MOINS, %s a PAS PARTOUT. L\'issue sortie est celle a %s : la plume s\'est trompee de cote.' % (pa2.groups() + (pa2.group(2),)),
       'VRAIE (%d ; 0 ailleurs)' % nq_par['L3'], 'VRAIE (%.4f au plus)' % a5, 'VRAIE (%.4f au plus)' % a6, 'VRAIE (%.4f)' % a9, 'VRAIE (zero partout)',
       'Les huit annonces a deux issues sont vraies, pour une somme de probabilites de %.2f.' % somme,
       'a L3, la lecture deposee est sur le plateau a %d etats sur %d.' % (sum(1 for k in par['L3'] if E[k]['j']['lu'] is True), len(par['L3'])),
       'aucun des douze points juges n\'en perd plus d\'un', '"a E4, la lecture deposee s\'ecarte du plateau de plus de tau a la majorite des etats"']
mq = manque(phr, AN)
chk('C14', sorted(mes) == sorted(act8) and len(act8) == 8 and all(VRAI.values()) and abs(somme - 5.96) < 1e-9 and max(nq_par.values()) == 1 and not mq and pa1 and pa2 and float(pa1.group(1)) == max(float(x) for x in pa1.groups()) and float(pa2.group(3)) == max(float(x) for x in pa2.groups()),
    'nn.8 : les 8 annonces a deux issues recalculees de mes sorties (probabilites lues dans la section 11 de mon gel, sort recalcule) == celles de l acte : %s ; somme %.2f ; A-1 et A-2 relues dans le gel ; absentes %s' % (
        sorted(mes) == sorted(act8), somme, mq))

# ------------------------------------------------------------------ C15 : nn.9, defauts et reserves
dur = [FIL[n]['duree_s'] for n in sorted(FIL)]
somme_d = sum(dur)
mn66 = (f(t_fin) - f(t_vi)) / 60.0
tnrap = []
for a in J(os.path.join(RUN, 'sonde_ter_etage1.json'))['temoin_negatif']:
    for x in ABS:
        gs = [a['traj'][x][str(k)]['gamma'] for k in range(-3, 9)]
        tnrap += [abs(gs[n] / gs[n + 1] - 2.0) for n in range(len(gs) - 1)]
rec01 = {}
for i in JU:
    r0, r1 = dep[i]['etats'][0], dep[i]['etats'][1]
    rec01[i] = (r0['recouvrement'] / r1['recouvrement'], max(r0['Gamma_2D']['3'] / r1['Gamma_2D']['3'], r1['Gamma_2D']['3'] / r0['Gamma_2D']['3']))
rmin, rmax_ = min(rec01, key=lambda i: rec01[i][0]), max(rec01, key=lambda i: rec01[i][0])
r1_juges = [i for i in JU if (i, 1) in E]
r1_q = [i for i in r1_juges if E[(i, 1)]['j']['statut'] == 'QUALIFIE']
sous = [i for i in JU if (i, 1) not in E]
note_m2 = norm(rt(os.path.join(ROOT, 'POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md')))
note_lc = norm(rt(os.path.join(ROOT, 'POUR_MACHINE1_lecteur_creux_machine2_v1.md')))
conf = rt(os.path.join(CTRL, 'confrontation_feuilles_ter_machine2_v1.log'))
phr = ['les douze processus de BOCAL4 en ont pris %.1f (%d s), pour %d minutes d\'horloge.' % (somme_d / 3600.0, round(somme_d), round(mn66)),
       'L\'ecart du rapport a 2 est de %.4f au plus dans le run, soit %.4f en relatif' % (max(tnrap), max(tnrap) / 2.0),
       'le rapport des recouvrements des rangs 0 et 1 va de %.3f (%s) a %.3f (%s) aux douze points, pour des largeurs deposees qui different d\'un facteur %.1f a %d.' % (
           rec01[rmin][0], rmin, rec01[rmax_][0], rmax_, math.floor(min(v[1] for v in rec01.values()) * 10) / 10.0, math.ceil(max(v[1] for v in rec01.values()))),
       'L\'etat de rang 1 est juge a dix points sur douze et y est QUALIFIE ; a M3 et M4 il est sous dix planchers.',
       '(38 etats reels, 20000 synthetiques, 2657206 cas de cascade : 0 desaccord)',
       'aux six points de M17 la regle du moteur departage l\'etat lu du suivant par une marge de recouvrement de 0.3 a 9 pour cent, pour des largeurs qui different d\'un facteur 22 a 30.',
       '(192 lectures, ecart relatif au pire %s)' % fh(float(re.search(r'192 lectures comparees, ecart relatif max ([0-9.e+-]+)', blog).group(1)))]
mq = manque(phr, AN)
chk('C15', not mq and len(r1_juges) == 10 and len(r1_q) == 10 and sous == ['M3', 'M4'] and 'DESACCORDS ENTRE LES DEUX FEUILLES, tous terrains : 0' in conf and '38' in conf and '20000' in conf and '2657206' in conf
    and 'de 0.3 % a 9 %' in note_lc and "d'un facteur 22 a 30" in note_lc and '0.0044' in note_m2 and '0.0022' in note_m2 and '38 fois sur 38' in note_m2,
    'nn.9 : D-TER-5 (somme des durees des douze sorties %.0f s = %.2f h, du verdict de l instrument a la fin du pilote %.1f min) ; D-TER-1 (ecart du rapport a 2 : %.4f au plus, %.4f en relatif) ; '
    'R-TER-2 : rapport des recouvrements des rangs 0 et 1 de %.4f (%s) a %.4f (%s), largeurs deposees d un facteur %.2f a %.2f (recalcules du depot au registre), rang 1 juge a %d points, '
    'QUALIFIE a %d, sous dix planchers a %s ; R-TER-1 et R-TER-3 relus dans mes journaux ; ma note hors chaine dit 0.3 a 9 pour cent et 22 a 30 ; absentes %s' % (
        somme_d, somme_d / 3600.0, mn66, max(tnrap), max(tnrap) / 2.0, rec01[rmin][0], rmin, rec01[rmax_][0], rmax_, min(v[1] for v in rec01.values()), max(v[1] for v in rec01.values()),
        len(r1_juges), len(r1_q), sous, mq))

# ------------------------------------------------------------------ C16 : nn.10, le delta 98
j98 = [(p['id'], x['rang']) for p in VO['points'] if p['id'] in JU for x in p['etats'] if x.get('exclu') is None]
q98 = [k for k in j98 if k in E and E[k]['j']['statut'] == 'QUALIFIE']
lu98 = [k for k in j98 if k in E and E[k]['j']['lu'] is True]
manq98 = [k for k in j98 if k not in E]
phr = ['De ses %d etats juges, %d sont QUALIFIES ici, et la lecture deposee est sur le plateau a %d d\'entre eux.' % (len(j98), len(q98), len(lu98))]
mq = manque(phr, AN)
chk('C16', not mq and len(j98) == 132 and len(q98) == 131 and len(lu98) == 124 and not manq98,
    'nn.10 (M-3) : les etats juges du delta 98 lus de journal/verdict_ordre2.json au registre (exclu = null, aux douze points) : %d ; parmi eux, QUALIFIES ici %d, sur le plateau de la consigne (e) %d, '
    'absents de mes 137 : %d ; phrase absente %s' % (len(j98), len(q98), len(lu98), len(manq98), mq))

# ------------------------------------------------------------------ C17 : le registre, nn.0, nn.12
head, plafond, msg98, j98t = 'indisponible', 0, '', ''
try:
    head = subprocess.run(['git', 'ls-remote', 'https://github.com/lbaaz/SG_1', 'HEAD'], capture_output=True, text=True, timeout=60).stdout.split()[0][:7]
    jr = subprocess.run(['git', '-C', CLONE, 'ls-tree', '--name-only', 'origin/main', 'journal/'], capture_output=True, text=True).stdout.split()
    plafond = max([int(m.group(1)) for x in jr for m in [re.match(r'journal/journal_delta_(\d+)_', x)] if m] or [0])
    j98t = norm(rt(os.path.join(CLONE, 'journal', 'journal_delta_98_ordre2_chaine_EA_v1.md')))
except Exception as ex:
    head = 'indisponible (%s)' % type(ex).__name__
phr = ['Registre a l\'ecriture : origin/main 8d54bf9, plafond 98. Aucun numero n\'est pris ici (E18).', 'Aucune regle nouvelle ; trente-quatre attendent la revue.']
mq = manque(phr, AN)
chk('C17', head == '8d54bf9' and plafond == 98 and 'trente-quatre attendent la revue' in j98t and not mq,
    'nn.0, nn.12 : tete publique du registre %s, plafond %d (journaux au registre) ; le journal 98 au registre dit "trente-quatre attendent la revue" : %s ; phrases absentes %s' % (
        head, plafond, 'trente-quatre attendent la revue' in j98t, mq))

# ------------------------------------------------------------------ C18 : nn.13, nn.15, les lots cites
manifs = re.findall(r'^[0-9a-f]{16}\s+[0-9a-f]{16}\s+\d+\s+\d+\s+(\S+)$', man.decode('utf-8'), re.M)
n15 = norm(ACTE[ACTE.index('nn.15 PIECES DU LOT'):])
absents = []
for n in manifs:
    base = n
    if base in n15 or re.sub(r'(rejeu_partiel_)(\w+)(\.json)', r'\1<id>\3', base) in n15 or (base.endswith('.log') and base[:-4] + '.py / .log' in n15) or (base.endswith('.log') and base[:-4] + '.py / .log / .json' in n15) \
            or (base.endswith('.json') and base[:-5] + '.py / .log / .json' in n15):
        continue
    absents.append(n)
lots_att = {'4103eae43f989877': None, '42110a3d1eabdaa0': 'MANIFEST_lot_machine1_gel_EB_ter_v1.txt', 'c8164e6d80ee0b60': 'MANIFEST_lot_machine2_lecteur_creux_hors_chaine_v1.txt',
            '29073aa2ac4decac': 'MANIFEST_lot_machine2_rejeu_absorbeurs_longs_hors_chaine_v1.txt', 'd2f50caa808cfb1c': 'MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt',
            '1f057651c8f69eb6': 'MANIFEST_lot_machine2_resultat_EB_ter_v1.txt'}
lots_ok = all(emp(rd(os.path.join(ROOT, v)))[0] == k for k, v in lots_att.items() if v)
phr = ['machine 1 -- la note hors chaine 4103eae43f989877, le gel et ses instruments 42110a3d1eabdaa0 ; machine 2 -- son lecteur creux c8164e6d80ee0b60 et son rejeu de la note 29073aa2ac4decac, hors chaine et non certifies, '
       'la certification d2f50caa808cfb1c, le resultat 1f057651c8f69eb6.', 'Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.']
mq = manque(phr, AN)
chk('C18', lots_ok and not absents and not mq and '4103eae43f989877' in IDX,
    'nn.13, nn.15 : les canons des lots cites, recalcules de leurs manifestes que je detiens : %s ; les %d pieces du manifeste de machine 1 sont toutes nommees en nn.15 (absentes %s) ; phrases absentes %s' % (
        lots_ok, len(manifs), absents, mq))

# ------------------------------------------------------------------ C19 : les citations entre guillemets, mot pour mot
bis = norm(rt(os.path.join(CLONE, 'gels', 'qualification_EB_bis_pre_enregistrement_v1.md')))
j95 = norm(rt(os.path.join(CLONE, 'journal', 'journal_delta_95_qualification_EB_bis_v2.md')))
cit = [('gel : la question', "La largeur Gamma_LS que la manche M17 a lue est-elle une largeur SORTANTE INTRINSEQUE -- independante de la force, de la forme, de la longueur et de la position de l'absorbeur -- ou depend-elle de la facon d'absorber ?", GN),
       ('gel : le temoin negatif', 'se divise par deux a chaque barreau (a 0.002 pres sur le rapport)', GN),
       ('gel : une suite', "une suite demanderait un autre gel et une autre decision de l'operateur", GN),
       ('gel : section 9', 'aux douze points et aux etats juges QUALIFIES, la largeur lue sous absorbeur long est une largeur sortante stable sous les variations jouees de force, de forme, de longueur et de position, a tau pres', GN),
       ('gel : raison de A-2', "a E4, la lecture deposee s'ecarte du plateau de plus de tau a la majorite des etats", GN),
       ('gel bis : DERNIER ESSAI', 'DERNIER ESSAI', bis), ('gel bis : le garde-fou', "L'operateur peut lever ce garde-fou ; les machines, non", bis),
       ('journal 95', 'toute phrase portant un Gamma depuis juillet est reclassee', j95), ('journal 98', "La lecture de E-B garde son statut : elle n'est pas qualifiee.", j98t)]
rat = [(n, 'dans la source' if norm(q) in src else 'ABSENT DE LA SOURCE', 'dans l acte' if norm(q) in AN else 'ABSENT DE L ACTE') for n, q, src in cit]
mauv = [r for r in rat if r[1].startswith('ABSENT') or r[2].startswith('ABSENT')]
chk('C19', not mauv, 'nn.0, nn.5, nn.8, nn.10, nn.14 : %d citations entre guillemets, chacune cherchee MOT POUR MOT (blancs normalises) dans sa source et dans l acte ; ecarts %s' % (len(cit), mauv))
try:
    tr = rt(os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'd--devs-bocal-BOCAL4', '7d33635e-8345-4a2c-a69e-f6a51f9d8fa7.jsonl'))
    info('le message de l operateur "tu peux certifier et jouer si c\'est ok ?" est %s dans la trace de cette session' % ('present' if "tu peux certifier et jouer si c'est ok ?" in tr else 'ABSENT'))
except OSError:
    info('trace de session non lue')
info('NON VERIFIABLE par machine 2 (attestations de machine 1 ou de l operateur) : (a) nn.0 et nn.11 (ii), "ouvre" 08 h 38 et "go" 10 h 28 ; (b) nn.2, qu\'aucun calcul 2D sous absorbeur long '
     'n\'a ete fait par machine 1 aux douze points avant le lot de resultat, ni ce que la plume avait vu aux six points de M17 et aux huit points de reglage (gel L-1) ; (c) la date et l heure '
     'a laquelle machine 1 a rejoue : je lis ses sorties, pas son horloge')
mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'acte': ACTE_NOM, 'canon': c_act, 'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}},
          open(JSN, 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
