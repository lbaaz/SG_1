# -*- coding: ascii -*-
"""VERIFICATION par machine 2 de l'ACTE 'nn' de la qualification E-B (journal_delta_nn_qualification_EB_v1.md,
canon 0d7870ebad535303), 2026-11-12. Chaque affirmation CHIFFREE de l'acte est RECALCULEE ici depuis MES sources
(sortie de la sonde de la nuit, table de reference, fichiers du run M17, moteur, feuille certifiee), jamais lue dans
le script d'ecriture de machine 1. Les phrases attendues sont CONSTRUITES depuis les donnees puis cherchees dans
l'acte (blancs normalises) : un nombre tape a la main dans l'acte et faux est une morsure.
Usage (depuis BOCAL4, jamais -I : numpy en user-site) : python -P verification_acte_nn_qualification_EB_machine2_v1.py
Sorties : verification_acte_nn_qualification_EB_machine2_v1.log et .json. Ce script ne modifie rien."""
import hashlib
import importlib.util
import io
import json
import math
import os
import re
import sys
import unicodedata
import zipfile
from fractions import Fraction

ICI = os.path.dirname(os.path.abspath(__file__))
DL = os.path.join(os.path.expanduser('~'), 'Downloads')
ACTE_NOM = 'journal_delta_nn_qualification_EB_v1.md'
LOT = 'lot_machine1_2026-11-12_acte_qualification_EB_v1_recu.zip'
LOG = os.path.join(ICI, 'verification_acte_nn_qualification_EB_machine2_v1.log')
JSN = os.path.join(ICI, 'verification_acte_nn_qualification_EB_machine2_v1.json')
NUIT = os.path.join(ICI, 'nuit_EB')
SORTIE = os.path.join(NUIT, 'sortie')
FH = open(LOG, 'w', encoding='ascii', newline='\n')
CHK = []
INFO = []


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


# ------------------------------------------------------------------ pieces et lot
zl = zipfile.ZipFile(os.path.join(ICI, LOT))
ACTE = zl.read(ACTE_NOM).decode('utf-8')
ACTE_N = norm(ACTE)
dire('VERIFICATION de l acte %s par machine 2' % ACTE_NOM)
c_act = emp(open(os.path.join(ICI, ACTE_NOM), 'rb').read())[0]
chk('C01', c_act == '0d7870ebad535303' == emp(zl.read(ACTE_NOM))[0] and
    open(os.path.join(ICI, ACTE_NOM), 'rb').read() == zl.read(ACTE_NOM),
    'acte hors zip == membre du zip, canon %s (annonce 0d7870ebad535303)' % c_act)
man = zl.read('MANIFEST_lot_machine1_acte_qualification_EB_v1.txt').decode('utf-8')
bad = []
n_lignes = 0
for ln in man.splitlines():
    m = re.match(r'^([0-9a-f]{16}) ([0-9a-f]{16}) +(\d+) +(\d+)  (\S+)$', ln)
    if not m:
        continue
    n_lignes += 1
    b, br, ob, obr = emp(zl.read(m.group(5)))
    if (b, br, ob, obr) != (m.group(1), m.group(2), int(m.group(3)), int(m.group(4))):
        bad.append(m.group(5))
chk('C02', n_lignes == 7 and not bad and len(zl.namelist()) == 8,
    '%d pieces sur 7 au canon, a l empreinte brute et a la taille ; membres du zip %d (attendu 8 avec le manifeste) ;'
    ' ecarts %s ; CANON DU LOT %s' % (n_lignes, len(zl.namelist()), bad, emp(man.encode())[0]))

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
        if i.is_dir() or i.file_size > 30 * 1024 * 1024:
            continue
        try:
            d = z.read(i.filename)
        except (RuntimeError, zipfile.BadZipFile, NotImplementedError):
            continue
        ajoute(emp(d)[0], '%s::%s' % (label, i.filename))
        if i.filename.lower().endswith('.zip') and prof < 3:
            zip_membres(d, '%s::%s' % (label, i.filename), prof + 1)


def parcourt(racine, recursif):
    for rep, dirs, fics in os.walk(racine):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', 'reprise', '.git') and not d.startswith('T' + chr(233) + 'l' + chr(233) + 'ch')]
        for f in fics:
            if racine == DL and not re.match(r'^(lot_machine|POUR_MACHINE|POUR_MACHINE2|qualification_EB|journal_delta|'
                                              r'note_machine|ERRATUM|files \(\d+\)\.zip)', f):
                continue                       # Downloads : SEULES les livraisons de l echange, rien d autre n est ouvert
            p = os.path.join(rep, f)
            try:
                if os.path.getsize(p) > 30 * 1024 * 1024:
                    continue
                d = open(p, 'rb').read()
            except OSError:
                continue
            rel = os.path.relpath(p, racine).replace('\\', '/')
            ajoute(emp(d)[0], rel if racine == ICI else 'Downloads/' + rel)
            if f.lower().endswith('.zip'):
                zip_membres(d, rel if racine == ICI else 'Downloads/' + rel, 1)
        if not recursif:
            break


parcourt(ICI, True)
parcourt(DL, False)
n_fic = sum(len(v) for v in IDX.values())
dire('index : %d fichiers ou membres, %d empreintes distinctes (BOCAL4 recursif, Downloads a plat, zips ouverts)'
     % (n_fic, len(IDX)))
TOK = sorted(set(re.findall(r'(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])', ACTE)))
non = [t for t in TOK if t not in IDX]
chk('C03', len(TOK) == 51,
    '%d empreintes distinctes citees dans l acte (machine 1 annonce 51)' % len(TOK))
dire('     resolues chez moi : %d ; NON resolues chez moi : %d' % (len(TOK) - len(non), len(non)))
for t in TOK:
    ou = IDX.get(t)
    ctx = ''
    m = re.search(r'([A-Za-z0-9_./-]+)\s+' + t, ACTE)
    if m:
        ctx = m.group(1)
    else:
        m = re.search(r'([^\n]{0,40})' + t, ACTE)
        ctx = norm(m.group(1)) if m else ''
    dire('     %s %-9s %s | %s' % (t, 'RESOLUE' if ou else 'ABSENTE', (ou[0] if ou else '-')[:90], ctx[-40:]))
NON_RESOLUES = non

# ------------------------------------------------------------------ mes sources de la nuit
S1 = json.load(open(os.path.join(SORTIE, 'sonde_etage1.json'), encoding='utf-8'))
VER = json.load(open(os.path.join(SORTIE, 'verdict_etage1.json'), encoding='utf-8'))
REF = json.load(open(os.path.join(ICI, 'tp_reference_machine2_v1.json'), encoding='utf-8'))
TAB = {r['j']: r for r in REF['balayage']}
PL = 1e-12
KS = list(range(-2, 13))


def gam(cle, cfg, k):
    e = S1['TP'][cle]['traj'][cfg][str(k)]['etats'][0]
    return e['gamma'] if e['suivi'] else None


def serie(cle, cfg):
    return {k: gam(cle, cfg, k) for k in KS}


def lisible(x):
    return x is not None and x > PL


def plateau_ind(ser):
    """3.11 du gel, reecrit ici : fenetre de cinq valeurs lisibles a k consecutifs ; max <= 21/20 min en rationnels."""
    best = None
    for k0 in range(-2, 9):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(not lisible(x) for x in v):
            continue
        mx, mn = Fraction(max(v)), Fraction(min(v))
        cand = (not (mx <= Fraction(21, 20) * mn), mx / mn, k0)
        if best is None or cand < best[0]:
            best = (cand, v)
    if best is None:
        return None
    (nok, rap, k0), v = best
    return {'ok': not nok, 'etalement': float(rap) - 1.0, 'k0': k0,
            'Gamma_pl': math.exp(sum(math.log(x) for x in v) / 5.0)}


TRAJ = [('j06', 'G20'), ('j06', 'G30'), ('j08', 'G20'), ('j08', 'G30')]
CFG = {'G20': 'F1G20', 'G30': 'F1G30'}
GREF = {c: TAB[S1['TP'][c]['j']]['Gamma_ref'] for c in ('j06', 'j08')}
UREF = {c: TAB[S1['TP'][c]['j']]['u_ref'] for c in ('j06', 'j08')}

# ------------------------------------------------------------------ nn.5 : l'etage 1 au chiffre
dire()
dire('--- nn.5 : l etage 1 au chiffre ---')
attendu = []
tient_tous = True
for cle in ('j06', 'j08'):
    j = S1['TP'][cle]['j']
    g = S1['TP'][cle]['g']
    tau_tp = 0.05 + UREF[cle]
    attendu.append('j = %d, g = %.5f, Gamma_ref %.4e, u_ref %.1e, tau_TP = tau + u_ref = %.4f' % (
        j, g, GREF[cle], UREF[cle], tau_tp))
    for cg in ('G20', 'G30'):
        p = plateau_ind(serie(cle, CFG[cg]))
        if p['ok']:
            e = abs(math.log(p['Gamma_pl'] / GREF[cle]))
            tient = e <= tau_tp
            attendu.append('%s : PLATEAU, k0 = %d, Gamma_pl %.4e, etalement %.4f, |ln| = %.4f -> %s' % (
                cg, p['k0'], p['Gamma_pl'], p['etalement'], e, 'TIENT' if tient else 'NE TIENT PAS'))
        else:
            tient = False
            attendu.append('%s : PAS DE PLATEAU ; meilleure fenetre de cinq k0 = %d, etalement %.4f -> NE TIENT PAS' % (
                cg, p['k0'], p['etalement']))
        v = VER['detail']['TP'][cle][CFG[cg]]
        if abs(v['etalement'] - p['etalement']) > 1e-12 or v['tient'] != tient:
            tient_tous = False
absents = [a for a in attendu if norm(a) not in ACTE_N]
chk('C04', not absents and tient_tous,
    'la table nn.5 du temoin positif recalculee de ma sortie (plateau exact, ma table de reference) : %d phrases '
    'attendues retrouvees dans l acte, accord avec mon verdict_etage1.json ; absentes : %s' % (
        len(attendu) - len(absents), absents))

ver_attendu = "VERDICT DE L'ETAGE 1 : %s, motifs %s." % (
    VER['etage1'], " ; ".join("'%s'" % m for m in VER['motifs']))
chk('C05', norm(ver_attendu) in ACTE_N,
    'verdict et motifs lus dans MON verdict_etage1.json retrouves mot pour mot : %s' % ver_attendu)

# gardes
cons = open(os.path.join(NUIT, 'console_etage1.log'), encoding='ascii', errors='replace').read()
m = re.search(r'max \|Gamma\(H\+\)\| = ([0-9.e+-]+)', ACTE_N)
pl_vals = [abs(v) for d in S1['GQ5'].values() for v in d.values()]
chk('C06', len(pl_vals) == 30 and '%.3e' % max(pl_vals) == (m.group(1) if m else None),
    'G-Q5 : %d valeurs, max |Gamma(H+)| = %.3e ; l acte dit %s' % (len(pl_vals), max(pl_vals), m.group(1) if m else None))
n_jou, n_sau = 0, 0
for fam, trajs in (('TP', [S1['TP'][c]['traj'][g] for c in S1['TP'] for g in ('F1G20', 'F1G30')]),
                   ('TN', [S1['TN']['traj']])):
    for t in trajs:
        for ks, rec in t.items():
            if rec.get('saute'):
                n_sau += 1
            else:
                n_jou += 1
n_jou += len(pl_vals)
chk('C07', (n_jou, n_sau) == (93, 12) and (n_jou + n_sau) == 105 and
    '93 decompositions jouees et 12 sautees sur 105' in ACTE_N,
    'comptes recomptes dans mon JSON : %d jouees (dont le plancher 30) + %d sautees = %d ; phrase de nn.4 retrouvee'
    % (n_jou, n_sau, n_jou + n_sau))
d60 = [rec['duree_s'] for c in S1['TP'] for rec in S1['TP'][c]['traj']['F1G20'].values() if not rec.get('saute')]
d70 = [rec['duree_s'] for c in S1['TP'] for rec in S1['TP'][c]['traj']['F1G30'].values() if not rec.get('saute')]
mo60, mo70 = sum(d60) / len(d60), sum(d70) / len(d70)
chk('C08', abs(mo60 - 30) <= 2 and abs(mo70 - 68) <= 2,
    'duree moyenne par decomposition du temoin positif : %.1f s a N = 60 (%d), %.1f s a N = 70 (%d) ; l acte dit '
    'environ 30 s et 68 s' % (mo60, len(d60), mo70, len(d70)))
pf = S1['plateforme']
chk('C09', ('%s %s, python %s, numpy %s' % (pf['systeme'], pf['machine'], pf['python'], pf['numpy'])) ==
    'Windows AMD64, python 3.11.9, numpy 2.2.6' and '(Windows AMD64, python 3.11.9, numpy 2.2.6)' in ACTE_N,
    'plateforme lue dans mon JSON == celle de nn.4')

# TN
cands = S1['TN']['candidats']
g3 = [S1['TN']['traj']['3']['etats'][t]['gamma'] for t in range(3)]
ov = [S1['TN']['traj'][k]['etats'][t]['ov'] for k in ('2', '4') for t in range(3)]
suivis = [S1['TN']['traj'][k]['etats'][t]['suivi'] for k in ('2', '4') for t in range(3)]
tn_attendu = ['(50, 25), (55, 27), (45, 22)', 'Gamma = %.3f, %.3f, %.3f' % tuple(g3),
              'recouvrements %.3f a %.3f, sous le seuil 0.90' % (min(ov), max(ov))]
absents = [a for a in tn_attendu if norm(a) not in ACTE_N]
chk('C10', cands == [[50, 25], [55, 27], [45, 22]] and not any(suivis) and not absents,
    'temoin negatif : candidats %s, Gamma a k = 3 %s, recouvrements k = 2 et 4 de %.3f a %.3f, aucun suivi ; '
    'phrases absentes de l acte : %s' % (cands, ['%.3f' % x for x in g3], min(ov), max(ov), absents))

# cascade par la feuille certifiee (importee, jamais executee en main)
fe_chemin = os.path.join(NUIT, 'scripts', 'lecture_qualification_EB_machine1_v1.py')
c_fe = emp(open(fe_chemin, 'rb').read())[0]
spec = importlib.util.spec_from_file_location('feuille_m1', fe_chemin)
FE = importlib.util.module_from_spec(spec)
spec.loader.exec_module(FE)
casc = FE.cascade(VER, None, {})
chk('C11', c_fe == 'b3ac958a1a2b915b' and casc == "NON CONCLUANT D'INSTRUMENT" and
    "NON CONCLUANT D'INSTRUMENT" in ACTE,
    'feuille %s : cascade(mon verdict, pas d etage 2) = %s' % (c_fe, casc))
# rang 1 du gel, section 9 (relue dans le gel v2)
gel = open(os.path.join(DL, 'qualification_EB_pre_enregistrement_v2.md'), 'rb').read()
gel_t = norm(gel.decode('utf-8'))
chk('C12', emp(gel)[0] == 'cde0cd11a763f26d' and
    "1. NON CONCLUANT D'INSTRUMENT : G-Q1 a G-Q7 ou G-Q10 mord ; TP ne tient pas" in gel_t and
    "NON CONCLUANT D'INSTRUMENT : rien n'est dit du fantome ; l'acte consigne le meilleur etalement atteint au TP"
    in gel_t,
    'gel %s : section 9 rang 1 (TP ne tient pas -> NON CONCLUANT D INSTRUMENT) et section 13 (consigner le meilleur '
    'etalement) relues ; l acte consigne 0.0276, 0.0344, 0.3847, 0.4214 : %s' % (
        emp(gel)[0], all(x in ACTE_N for x in ('0.0276 (j = 6) et 0.0344 (j = 8)', '0.3847 et 0.4214'))))

# ------------------------------------------------------------------ nn.6 : tableau, paliers, hors palier
dire()
dire('--- nn.6 : lectures apres coup ---')
lignes = ACTE.splitlines()
tab = {}
ent = None
for ln in lignes:
    mh = re.match(r'^\s+k =\s+([-\d ]+)$', ln)
    if mh:
        ent = [int(x) for x in mh.group(1).split()]
        continue
    mr = re.match(r'^\s+j = (\d)\s+(G\d\d)\s+([-\d. ]+)$', ln)
    if mr and ent:
        toks = mr.group(3).split()
        if len(toks) == len(ent):
            for k, t in zip(ent, toks):
                tab[(int(mr.group(1)), mr.group(2), k)] = t
nb = 0
ecarts = []
for cle, cg in TRAJ:
    j = S1['TP'][cle]['j']
    for k in KS:
        g = gam(cle, CFG[cg], k)
        att = '-' if not lisible(g) else '%.3f' % (g / GREF[cle])
        got = tab.get((j, cg, k))
        nb += 1
        if got != att:
            ecarts.append((j, cg, k, got, att))
chk('C13', nb == 60 and len(tab) == 60 and not ecarts,
    'tableau de nn.6 : %d cellules lues dans l acte, %d recalculees de mon JSON (Gamma / Gamma_ref ; "-" sous 1e-12) ;'
    ' ecarts %s' % (len(tab), nb, ecarts))

# (b) paliers
MOTS = {3: 'trois', 4: 'quatre', 5: 'cinq', 6: 'six'}
pal = []
for cle, cg in TRAJ:
    ser = serie(cle, CFG[cg])
    best = None
    for k0 in KS:
        for ln_ in range(1, 16):
            v = [ser.get(k) for k in range(k0, k0 + ln_)]
            if len(v) < ln_ or any(not lisible(x) for x in v):
                break
            if Fraction(max(v)) <= Fraction(21, 20) * Fraction(min(v)):
                if best is None or ln_ > best[0]:
                    best = (ln_, k0, max(v) / min(v) - 1.0)
            else:
                break
    j = S1['TP'][cle]['j']
    pal.append('j = %d %s : %s valeurs, k = %d a %d, etalement %.4f' % (
        j, cg, MOTS[best[0]], best[1], best[1] + best[0] - 1, best[2]))
absents = [p for p in pal if norm(p) not in ACTE_N]
chk('C14', not absents, 'paliers (plus longue suite de valeurs consecutives a 5 pour cent) recalcules : %s ; absents '
    'de l acte : %s' % ('; '.join(pal), absents))

# (a) bord fort
bord = max(abs(gam(c, CFG[g], -2) / GREF[c] - 1.0) for c, g in TRAJ)
chk('C15', '%.1f pour cent pres' % (bord * 100) in ACTE_N or '0.5 pour cent pres' in ACTE_N and abs(bord - 0.005) < 6e-4,
    '(a) k = -2 : ecart maximal a la reference %.2f pour cent (acte : 0.5) ; u_ref de j = 6 %.2f pour cent (acte : 0.2)'
    % (bord * 100, UREF['j06'] * 100))

# (c) hors palier
rap = []
for cle, cg in TRAJ:
    for k in range(9, 13):
        rap.append(gam(cle, CFG[cg], k) / gam(cle, CFG[cg], k - 1))
rap_lis = []
for cle, cg in TRAJ:
    for k in range(9, 13):
        if lisible(gam(cle, CFG[cg], k)) and lisible(gam(cle, CFG[cg], k - 1)):
            rap_lis.append(gam(cle, CFG[cg], k) / gam(cle, CFG[cg], k - 1))
r_att = 'rapports %.3f a %.3f de k = 8 a 12' % (min(rap_lis), max(rap_lis))
r_att_tous = 'rapports %.3f a %.3f' % (min(rap), max(rap))
k3 = ['%.3f' % (gam(c, CFG[g], 3) / GREF[c]) for c, g in TRAJ]
bosse = gam('j06', 'F1G30', 5) / GREF['j06']
c_att = ['%s, %s, %s, %s' % tuple(k3), '%.2f fois la reference (k = 5)' % bosse]
absents = [a for a in c_att if norm(a) not in ACTE_N]
chk('C16', norm('(' + r_att + ')') in ACTE_N and not absents,
    '(c) rapports de pas k = 9 a 12 : %.3f a %.3f (valeurs lisibles) ; avec les non lisibles %.3f a %.3f ; k = 3 : %s ;'
    ' bosse a j = 6 G30 : %.2f ; absents de l acte : %s' % (
        min(rap_lis), max(rap_lis), min(rap), max(rap), k3, bosse, absents))

# (d) critere de descente de M17 : les trois pas de k = 0 a 3, les deux derniers < 0.05, denominateur = pas precedent
TAU = 0.05


def pas(cle, cg, k):
    a, b = gam(cle, CFG[cg], k - 1), gam(cle, CFG[cg], k)
    return abs(b - a) / a


dd = []
acc_att = []
pire = 0.0
for cle, cg in TRAJ:
    j = S1['TP'][cle]['j']
    p = [pas(cle, cg, k) for k in (1, 2, 3)]
    refuse = not (p[1] < TAU and p[2] < TAU)
    dd.append('j = %d %s : pas %.3f, %.3f, %.3f -> %s' % (j, cg, p[0], p[1], p[2], 'REFUSE' if refuse else 'ACCEPTE'))
    ok_k = [k for k in range(0, 13) if pas(cle, cg, k) < TAU and pas(cle, cg, k - 1) < TAU]
    rr = [gam(cle, CFG[cg], k) / GREF[cle] for k in ok_k]
    pire = max([pire] + [abs(x - 1.0) for x in rr])
    acc_att.append('j = %d %s : accepte k = %s (Gamma / Gamma_ref : %s)' % (
        j, cg, ', '.join(str(k) for k in ok_k), ', '.join('%.3f' % x for x in rr)))
absents = [a for a in dd + acc_att if norm(a) not in ACTE_N]
chk('C17', not absents and '%.1f pour cent de la reference au pire' % (pire * 100) in ACTE_N,
    '(d) pas de descente et portes recalcules (denominateur = pas precedent, plancher du moteur ~1e-19 negligeable) : '
    '%s ; accepte (glisse) : %s ; ecart maximal des acceptes %.1f pour cent ; absents de l acte : %s' % (
        ' | '.join(dd), ' | '.join(acc_att), pire * 100, absents))

# les six points de M17 : les deux derniers pas valent au plus 0.0469 (fichiers du run, original BOCAL4)
PTS = ['39_20', '197_100', '99_50', '101_50', '203_100', '41_20']
pm = []
poids, recs_, rcs, larg = [], [], [], []
for n in PTS:
    d = json.load(open(os.path.join(ICI, 'manche_m17_v17', 'pt_%s_f070.json' % n), encoding='utf-8'))
    cr = d['EB']['critere_absorbeur']
    es = [e for e in cr['essais'] if e['L'] == cr['L_retenu']][0]
    pm.append(max(es['pas'][1], es['pas'][2]))
    h = d['EB']['Gamma_LS']['H']
    poids.append(h['poids_total'])
    recs_.append(h['recouvrement'])
    larg.append(h['Gamma_LS'])
    rcs.append(d['EB']['operatif_4_6']['Gamma'] if False else cr['essais'][0]['N'] - cr['essais'][0]['L'])
chk('C18', '%.4f' % max(pm) == '0.0469' and 'valent au plus 0.0469' in ACTE_N,
    'six points de M17 (pt_*_f070.json du run) : plus grand des deux derniers pas de descente %.4f (acte : 0.0469) ;'
    ' L retenus %s' % (max(pm), [json.load(open(os.path.join(ICI, 'manche_m17_v17', 'pt_%s_f070.json' % n)))
                                ['EB']['critere_absorbeur']['L_retenu'] for n in PTS]))

# nn.2 : grandeurs du run lisibles sans calcul neuf
l_att = ', '.join('%.3e' % x for x in larg)
e_run = math.log(max(larg) / min(larg))
chk('C19', l_att in ACTE_N and '%.4f' % e_run in ACTE_N,
    'nn.2 : six largeurs lues par M17 a eta0/8 : %s ; E_run = ln(max/min) = %.4f' % (l_att, e_run))
g_ = lambda a: '%.3f a %.3f' % (min(a[:3]), max(a[:3]))
d_ = lambda a: '%.3f a %.3f' % (min(a[3:]), max(a[3:]))
chk('C20', '%s' % ('poids total %s' % g_(poids)) in ACTE_N and ('poids total %.3f' % min(poids[3:])) in ACTE_N and
    ('recouvrement de l\'etat retenu %.2f a %.2f pour cent' % (min(recs_[:3]) * 100, max(recs_[:3]) * 100)) in ACTE_N and
    ('recouvrement %.2f a %.2f pour cent' % (min(recs_[3:]) * 100, max(recs_[3:]) * 100)) in ACTE_N,
    'nn.2 (constate) : poids total gauche %s, droite %s ; recouvrement gauche %.2f a %.2f pour cent, droite %.2f a '
    '%.2f pour cent, lus dans les pt_*_f070.json du run' % (
        g_(poids), d_(poids), min(recs_[:3]) * 100, max(recs_[:3]) * 100, min(recs_[3:]) * 100, max(recs_[3:]) * 100))

# ------------------------------------------------------------------ rejeu de machine 1 contre mes valeurs
dire()
dire('--- rejeu ponctuel de machine 1 contre ma sortie ---')
rj = zl.read('rejeu_ponctuel_TP_machine1_v1.log').decode('utf-8')
ok_rj, n_rj, pire_rj = True, 0, 0.0
for ln in rj.splitlines():
    mm = re.match(r'^TP (j\d\d) g = \S+ G20 k = +(-?\d+) eta = \S+ : Gamma m1 = (\S+) ; sonde m2 = (\S+) ;'
                  r' m1/m2 - 1 = (\S+) ;', ln)
    if not mm:
        continue
    n_rj += 1
    cle, k = mm.group(1), int(mm.group(2))
    mine = gam(cle, 'F1G20', k)
    e = float(mm.group(3)) / mine - 1.0
    pire_rj = max(pire_rj, abs(e))
    if ('%.10e' % mine) != mm.group(4) or ('%+.3e' % e) != mm.group(5):
        ok_rj = False
chk('C21', n_rj == 6 and ok_rj and '%.3e' % pire_rj == '2.856e-04',
    'rejeu de machine 1 : %d lignes ; la colonne "sonde m2" == MES gamma a 10 chiffres, les ecarts relatifs recalcules '
    'a leur affichage ; pire %.3e (acte : 2.856e-04)' % (n_rj, pire_rj))

# ------------------------------------------------------------------ mes propres pieces et mes propres mots
dire()
dire('--- mes pieces, telles que l acte les cite ---')
mes = {'a6c9daf3f3da3e41': 'lot reference TP', '72f65ad8a898fbb5': 'lot resultat nuit', 'fb72930ce5edb9fa': 'note ref TP',
       '113e5b84238203de': 'lot cert gel v1', '3b388a98d30695e3': 'lot cert gel v2', '123880c93b810d35': 'lot cert sonde v1',
       '6bed68e12ec21e18': 'lot cert sonde v2', '0d11d6866e3c5f37': 'note cert gel v1', 'a872e3d0e9000222': 'note cert gel v2',
       'c6629b3d4116cea7': 'note cert sonde v1', '9bc2d12f5b9a0524': 'note cert sonde v2',
       '5fd3a1897ca0442a': 'script ref', 'af73dfe9a648960a': 'premier jet', '69b3bab3bb8480b7': 'liste',
       '4d51dd58ef456fe9': 'table', 'fe25da36c3ad27fd': 'points bruts', 'd180e7c6eef55ca6': 'ma note de nuit',
       'ab31334aea5c444a': 'sonde_etage1.json', 'edafd162f58f9720': 'sonde_etage1.log',
       'baaccd2b3cad5a5b': 'console', 'aef856818424689a': 'verdict', '94e008b420e3ba38': 'lecture log',
       '4aecd0e2b23bc818': 'manifeste du run', '82a0be882568fe0c': 'moteur'}
manque = [(c, n) for c, n in mes.items() if c not in IDX or c not in ACTE]
chk('C22', not manque, 'mes %d pieces et lots cites par l acte : tous detenus chez moi ET cites dans l acte ; '
    'manquants %s' % (len(mes), manque))


def lit_note(canon):
    for ch in IDX.get(canon, []):
        if '::' not in ch and ch.endswith('.md'):
            return open(os.path.join(ICI, ch), 'rb').read().decode('utf-8', 'replace')
    return None


def compte(canon, motifs):
    t = lit_note(canon)
    if t is None:
        return False, 'note introuvable'
    t = norm(t)
    manq = [m for m in motifs if not re.search(m, t)]
    return not manq, 'motifs absents %s' % manq


reponses = []
for canon, motifs, nom in (
        ('0d11d6866e3c5f37', [r'21 controles', r'2 morsures'], 'gel v1'),
        ('a872e3d0e9000222', [r'11 controles', r'0 morsure', r'R-1', r'R-2'], 'gel v2'),
        ('c6629b3d4116cea7', [r'13 controles', r'3 morsures'], 'sonde v1'),
        ('9bc2d12f5b9a0524', [r'16 controles', r'0 morsure'], 'sonde v2')):
    ok, msg = compte(canon, motifs)
    reponses.append((nom, ok, msg))
chk('C23', all(r[1] for r in reponses),
    'comptes de controles et de morsures que l acte attribue a mes quatre certifications, relus dans mes notes : %s'
    % '; '.join('%s %s' % (r[0], 'ok' if r[1] else r[2]) for r in reponses))
ligne = "A-4 et A-5 : non aveugles (D-QEB-1), comptees, non creditees comme annonces aveugles ; A-1, A-2, A-3 non touchees"
hits = []
for rep, dirs, fics in os.walk(ICI):
    dirs[:] = [d for d in dirs if d not in ('reprise', '__pycache__', '.git') and not d.startswith('T' + chr(233) + 'l' + chr(233) + 'ch')]
    for f in fics:
        if f.endswith(('.md', '.txt')) and 'machine2' in f:
            try:
                if ligne in norm(open(os.path.join(rep, f), encoding='utf-8').read()):
                    hits.append(f)
            except (OSError, UnicodeDecodeError):
                pass
chk('C24', len(hits) >= 1, 'la ligne de machine 2 que nn.7 dit "reprise telle quelle" se trouve dans mes pieces : %s' % hits)
chk('C25', 'A-4 et A-5 : non aveugles (D-QEB-1), comptees, non creditees comme annonces aveugles ; A-1, A-2, A-3 non '
    'touchees' in ACTE_N, 'la meme ligne est citee dans l acte')

# ------------------------------------------------------------------ nn.9 : numerotation et compte des regles candidates (X)
dire()
dire('--- nn.9 : regles candidates sous (X) ---')
zm = zipfile.ZipFile(os.path.join(ICI, 'lot_machine2_2026-09-29_contreseing_acte_delta93_v1.zip'))
n93 = zm.read('POUR_MACHINE1_contreseing_acte_delta93_machine2_v1.md').decode('utf-8')
sec6 = n93.split('## 6. VERSE SOUS (X)')[1].split('## 7.')[0]
miens = sorted(int(x) for x in re.findall(r'^  (\d{2})  ', sec6, re.M))
nn9 = ACTE.split('nn.9 REGLES CANDIDATES')[1].split('nn.10 ')[0]
neufs = sorted(int(x) for x in re.findall(r'^  (\d{2}) \(m1', nn9, re.M))
chk('C26', not (set(miens) & set(neufs)),
    'numeros des regles candidates : les 4 nouvelles de l acte portent %s ; les 3 de MON contreseing du 93 (note '
    'scellee, lot_machine2_2026-09-29_contreseing_acte_delta93_v1, que machine 1 detient) portent %s ; communs : %s'
    % (neufs, miens, sorted(set(miens) & set(neufs))))
n_prec = 21                                          # mon contreseing du 93 (note v1 et v2) : "vingt et une candidates"
assert 'vingt et une candidates' in n93
dit = re.search(r'la revue \(X\), echue : ([a-z-]+) candidates', ACTE).group(1)
chk('C27', dit == 'vingt-cinq',
    'compte de la revue (X) : l acte dit "%s candidates" ; mon contreseing du 93 en compte %d, plus les %d de l acte = %d'
    % (dit, n_prec, len(neufs), n_prec + len(neufs)))
par = re.search(r'Les ([a-z-]+) precedentes \(([^)]*)\)', ACTE_N)
MOTS_N = {'une': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'huit': 8, 'dix-huit': 18, 'vingt et une': 21}
somme = sum(MOTS_N[w] for w in re.findall(r'(huit|quatre|une|trois|deux)', par.group(2)))
chk('C28', MOTS_N[par.group(1)] == somme,
    'la parenthese "Les %s precedentes (%s)" somme a %d ; le nombre annonce vaut %d (heredite : le delta 93 deposait '
    'deja "treize precedentes (huit du 90, quatre du 91, une du 92)" ; la numerotation 13, 14, 15 donne trois au 92)'
    % (par.group(1), par.group(2), somme, MOTS_N[par.group(1)]))

# ------------------------------------------------------------------ bilan
dire()
mord = [c for c in CHK if not c['ok']]
dire('NON RESOLUES chez moi (empreintes citees que je ne detiens sous aucune forme) : %d %s' % (len(NON_RESOLUES), NON_RESOLUES))
dire('BILAN : %d controles, %d mordent' % (len(CHK), len(mord)))
for c in mord:
    dire('  MORD %s : %s' % (c['id'], c['msg'][:200]))
dire('-- FIN verification_acte_nn_qualification_EB_machine2_v1 --')
json.dump({'acte': c_act, 'bilan': {'chk': len(CHK), 'mord': len(mord), 'noms': [c['id'] for c in mord]},
           'controles': CHK, 'non_resolues': NON_RESOLUES, 'info': INFO}, open(JSN, 'w', encoding='ascii'), indent=1)
FH.close()
sys.exit(0 if not mord else 1)
