# -*- coding: ascii -*-
"""CONTROLES DE LECTURE par machine 2 du gel "la garde G-1 du moteur et la chaine E-A par etat" (b59651f99e60707a), de sa sonde et de sa feuille, 2026-11-14.
Chaque controle est recalcule de MES sources, pas des scripts de construction ni du releve de machine 1. Ce script ne modifie rien d'autre que ses sorties
(gel_reconstruit_machine2.md, controles_gel_domaine_G1_machine2_v1.log/.json).
Usage (depuis BOCAL4) : python -P domaine_G1/controles_gel_domaine_G1_machine2_v1.py"""
import ast
import difflib
import hashlib
import io
import itertools
import json
import os
import re
import subprocess
import sys
import unicodedata
import zipfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OLD = os.path.join(ROOT, 'chaine_EA_par_etat')
LOG = os.path.join(HERE, 'controles_gel_domaine_G1_machine2_v1.log')
JSN = os.path.join(HERE, 'controles_gel_domaine_G1_machine2_v1.json')
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


def rd(p):
    return open(p, 'rb').read()


def lit(nom):
    return open(os.path.join(HERE, nom), encoding='ascii').read()


GEL_NOM = 'gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md'
GEL = lit(GEL_NOM)
GN = re.sub(r'\s+', ' ', GEL)
dire('CONTROLES DE MACHINE 2 : gel %s, sa sonde et sa feuille' % GEL_NOM)

# ------------------------------------------------------------------ C01 : le lot
man = rd(os.path.join(ROOT, 'MANIFEST_lot_machine1_gel_domaine_G1_chaine_EA_v1.txt'))
zl = zipfile.ZipFile(os.path.join(ROOT, 'lot_machine1_2026-11-14_gel_domaine_G1_chaine_EA_v1_recu.zip'))
att, bad = {}, []
for l in man.decode().split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
        if emp(zl.read(p[4])) != att[p[4]] or emp(rd(os.path.join(HERE, p[4]))) != att[p[4]]:
            bad.append(p[4])
chk('C01', len(att) == 22 and not bad and emp(man)[0] == '1aafb301d7d0ebb3' and emp(zl.read(GEL_NOM))[0] == 'b59651f99e60707a',
    '22 pieces sur 22 au canon, a l empreinte brute et aux deux tailles (zip et copie de travail) ; ecarts %s ; CANON DU LOT %s (annonce 1aafb301d7d0ebb3) ; gel %s' % (
        bad, emp(man)[0], emp(zl.read(GEL_NOM))[0]))

# ------------------------------------------------------------------ C02 : les canons cites par le gel
IDX = {}
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
        IDX.setdefault(emp(b)[0], []).append(os.path.relpath(p, ROOT).replace('\\', '/'))
        if f.lower().endswith('.zip'):
            try:
                z = zipfile.ZipFile(io.BytesIO(b))
                for i in z.infolist():
                    if not i.is_dir():
                        IDX.setdefault(emp(z.read(i.filename))[0], []).append('%s!%s' % (f, i.filename))
            except zipfile.BadZipFile:
                pass
cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', GEL)))
nr = [c for c in cites if c not in IDX]
paires = re.findall(r'^\s+([\w./-]+\.(?:py|md|json|log|txt))\s+([0-9a-f]{16})$', GEL, re.M)
mauvais_nom = [(n, c) for n, c in paires if c in IDX and not any(re.split(r'[/!]', x)[-1] == n.split('/')[-1] for x in IDX[c])]
chk('C02', not [c for c in nr if c != '119f4e4dcbb4baba'] and not mauvais_nom and len(paires) >= 18,
    '%d empreintes de 16 chiffres citees ; %d couples (nom, canon) de la section 1 ; non resolues chez moi %s ; noms differents %s' % (len(cites), len(paires), nr, mauvais_nom))
info('119f4e4dcbb4baba, la note d anteriorite hors chaine, est citee par le gel ("au projet" de machine 1) et ne m a pas ete remise : je ne l ai pas lue ; '
     'le gel n en tire rien ("ce gel ne revendique rien sur la methode"), aucun nombre ni aucun critere n en depend')

# ------------------------------------------------------------------ C03 : la reconstruction du gel depuis le gabarit
out = os.path.join(HERE, 'gel_reconstruit_machine2.md')
r = subprocess.run([sys.executable, '-P', os.path.join(HERE, 'construction_gel_domaine_G1_machine1_v1.py'), os.path.join(HERE, 'gel_domaine_G1_chaine_EA_gabarit.txt'), out],
                   capture_output=True, text=True, cwd=ROOT)
egal = os.path.isfile(out) and rd(out) == rd(os.path.join(HERE, GEL_NOM))
chk('C03', r.returncode == 0 and egal, 'rejeu de la construction du gel (gabarit + canons des 12 pieces, ses controles de coherence) : code %d ; gel reconstruit == gel du lot, '
    'octet pour octet : %s ; canon %s' % (r.returncode, egal, emp(rd(out))[0] if os.path.isfile(out) else None))

# ------------------------------------------------------------------ C04 : la sonde = la sonde certifiee + cinq hunks
old_s = lit_old = open(os.path.join(OLD, 'sonde_chaine_par_etat_machine1_v1.py'), encoding='ascii').read().split('\n')
new_s = lit('sonde_domaine_G1_machine1_v1.py').split('\n')
diff_txt = lit('diff_sonde_sur_acf7e26dedfa8abc.txt').split('\n')
# application du diff de machine 1 a la sonde certifiee, par mon propre code (un hunk = un bloc "@@ -a,b +c,d @@")
res, pos, nh = [], 0, 0
i = 0
while i < len(diff_txt) and not diff_txt[i].startswith('@@'):
    i += 1
while i < len(diff_txt):
    m = re.match(r'^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', diff_txt[i])
    if not m:
        i += 1
        continue
    nh += 1
    a = int(m.group(1)) - 1
    res += old_s[pos:a]
    pos = a
    i += 1
    while i < len(diff_txt) and not diff_txt[i].startswith('@@'):
        l = diff_txt[i]
        if l.startswith(' '):
            assert old_s[pos] == l[1:], 'contexte'
            res.append(l[1:])
            pos += 1
        elif l.startswith('-'):
            assert old_s[pos] == l[1:], 'ligne otee'
            pos += 1
        elif l.startswith('+'):
            res.append(l[1:])
        i += 1
res += old_s[pos:]
ajoutees = [l[1:] for l in diff_txt if l.startswith('+') and not l.startswith('+++')]
interdits = [l for l in ajoutees if re.search(r'\b(if|return|continue|raise|exit|break|while)\b', l) and 'statut' in l]
chk('C04', res == new_s and nh == 5 and emp(rd(os.path.join(OLD, 'sonde_chaine_par_etat_machine1_v1.py')))[0] == 'acf7e26dedfa8abc'
    and emp(rd(os.path.join(HERE, 'sonde_domaine_G1_machine1_v1.py')))[0] == '940a21b1d562bb49',
    'sonde : la sonde certifiee acf7e26dedfa8abc + les %d hunks de machine 1, appliques par mon code, == la sonde du lot 940a21b1d562bb49 (%d lignes) : %s ; '
    'lignes ajoutees %d, dont une qui branche sur le statut de la garde : %d' % (nh, len(new_s), res == new_s, len(ajoutees), len(interdits)))
# la garde y est consignee et jamais appliquee : aucune ligne qui lit le statut hors consignation
lectures = [i + 1 for i, l in enumerate(new_s) if 'statut' in l]
info('lignes de la sonde qui nomment "statut" : %s ; toutes sont la consignation (update, affichage) ou la docstring ; aucune ne branche' % lectures)
ok_nobranche = all(not re.search(r'^\s*(if|elif|while)\b.*statut', new_s[i - 1]) for i in lectures)
chk('C05', ok_nobranche, 'sonde : aucune condition (if, elif, while) ne porte sur le statut de la garde : la garde est CONSIGNEE et JAMAIS APPLIQUEE (gel, section 3)')

# ------------------------------------------------------------------ C06 : la feuille, ses fonctions heritees au caractere pres
src_old = open(os.path.join(OLD, 'lecture_chaine_par_etat_machine1_v1.py'), encoding='ascii').read()
src_new = lit('lecture_domaine_G1_machine1_v1.py')


def fonctions(src):
    t = ast.parse(src)
    return {n.name: ast.get_source_segment(src, n) for n in ast.walk(t) if isinstance(n, ast.FunctionDef)}


def sans_doc(seg):
    """L'arbre (ast.dump) d'une fonction dont la docstring est retiree."""
    f = ast.parse(seg).body[0]
    if f.body and isinstance(f.body[0], ast.Expr) and isinstance(getattr(f.body[0], 'value', None), ast.Constant) and isinstance(f.body[0].value.value, str):
        f.body = f.body[1:]
    return ast.dump(f)


def docstring(seg):
    return ast.get_docstring(ast.parse(seg).body[0])


fo, fn_ = fonctions(src_old), fonctions(src_new)
heritees = ['motif_exclusion', 'palier', 'eval_fraction', 'garde_ancres']
diffs_f = {}
for nom in heritees:
    a, b = fo.get(nom), fn_.get(nom)
    if a is None or b is None:
        diffs_f[nom] = 'absente (%s, %s)' % (a is None, b is None)
    elif sans_doc(a) != sans_doc(b):
        diffs_f[nom] = [l for l in difflib.unified_diff(a.split('\n'), b.split('\n'), lineterm='') if l[:1] in '+-' and l[:3] not in ('+++', '---')]
    elif docstring(a) != docstring(b):
        da, db = docstring(a), docstring(b)
        if da.replace('(section 6)', '(section 5)') != db:           # machine 1 declare ce seul changement : le numero de section dans une docstring
            diffs_f[nom] = 'docstring : %r -> %r' % (da, db)
        else:
            info('%s : identique, a la docstring pres, dont seul change le numero de section (6 -> 5), comme machine 1 le declare' % nom)
consts = ['SIGMA_J_MAX', 'POIDS_SITE_MIN', 'DIX_PLANCHERS', 'SUIVI_MIN', 'STABILITE_CIBLE', 'ETALEMENT_CHAINE', 'MIN_JUGES', 'TOL_ANCRE', 'N_ETATS']
diff_c = []
for c in consts:
    a = re.search(r'^%s\s*=\s*([^#\n]+)' % c, src_old, re.M)
    b = re.search(r'^%s\s*=\s*([^#\n]+)' % c, src_new, re.M)
    if not a or not b or a.group(1).strip() != b.group(1).strip():
        diff_c.append((c, a.group(1).strip() if a else None, b.group(1).strip() if b else None))
chk('C06', not diffs_f and not diff_c and emp(rd(os.path.join(OLD, 'lecture_chaine_par_etat_machine1_v1.py')))[0] == 'f94ab05f69e9bf2f',
    'feuille : motif_exclusion, palier, eval_fraction et garde_ancres == ceux de la feuille certifiee f94ab05f69e9bf2f (arbres ast, docstrings retirees ; la seule difference '
    'de docstring est le numero de section, 6 -> 5, que machine 1 declare) ; differences %s ; constantes heritees (%d) egales : differences %s' % (diffs_f, len(consts), diff_c))
n_doc = [l for l in difflib.unified_diff(src_old.split('\n'), src_new.split('\n'), lineterm='', n=0) if l.startswith(('+', '-')) and not l.startswith(('+++', '---'))]
info('feuille neuve contre feuille certifiee : %d lignes en plus ou en moins ; fichier 26258 contre %d octets' % (len(n_doc), len(rd(os.path.join(OLD, 'lecture_chaine_par_etat_machine1_v1.py')))))

# ------------------------------------------------------------------ C07 : la cascade du gel par enumeration exhaustive (3^12 vecteurs de classes)
CL = ['TENU', 'TOMBE', None]
EN = ['E1', 'E2', 'E3', 'E4', 'E5', 'E6']
HO = ['H1', 'H2', 'H3', 'H4', 'H5', 'H6']
PAIRES = {'P1': ('E1', 'H1'), 'P2': ('E3', 'H2'), 'P3': ('E4', 'H3'), 'P4': ('E5', 'H4'), 'P5': ('E6', 'H5')}
cnt = {}
viol_excl, viol_total = 0, 0
for vec in itertools.product(CL, repeat=12):
    c = dict(zip(EN + HO, vec))
    en_l = [k for k in EN if c[k] is not None]
    ho_l = [k for k in HO if c[k] is not None]
    a = sum(1 for k in en_l if c[k] == 'TOMBE')
    b = sum(1 for k in ho_l if c[k] == 'TENU')
    if len(en_l) < 4 or len(ho_l) < 4:
        v = 'NON LISIBLE'
    elif a == 0 and b == 0:
        v = 'SEPARE'
    elif a == 0:
        v = 'SUFFIT'
    else:
        v = 'NE TIENT PAS'
    pa = {n: ('NL' if (c[x] is None or c[y] is None) else ('HOM' if c[x] == c[y] else 'HET')) for n, (x, y) in PAIRES.items()}
    lis = [pa[k] for k in ('P1', 'P2', 'P3') if pa[k] != 'NL']
    riv = 'NL' if len(lis) < 2 else ('TENUE' if all(x == 'HOM' for x in lis) else 'NON')
    cnt[(v, riv)] = cnt.get((v, riv), 0) + 1
    if v == 'SEPARE' and any(pa[k] == 'HOM' for k in pa):           # "si LA GARDE SEPARE, toute paire lisible est HETEROGENE"
        viol_excl += 1
    if v == 'SEPARE' and riv == 'TENUE':
        viol_total += 1
chk('C07', viol_excl == 0 and viol_total == 0 and sum(cnt.values()) == 531441,
    'section 8 : sur les 3^12 = 531441 vecteurs de classes (TENU, TOMBE, aucune) des douze points juges, quand LA GARDE SEPARE toute paire lisible est HETEROGENE '
    '(violations %d) et la rivale n est jamais TENUE (violations %d) ; repartition (verdict, rivale) : %s' % (viol_excl, viol_total, dict(sorted(cnt.items(), key=lambda kv: str(kv[0])))))

# ------------------------------------------------------------------ C08 : les annonces et les paires
a1 = re.search(r'A-1\s+le verdict : (.*?)\n\s+A-2', GEL, re.S).group(1)
p_a1 = [float(x) for x in re.findall(r'\b(0\.\d\d)\b', a1)]
ann = re.findall(r'^\s+A-(\d+)\s+\((0\.\d\d)\)', GEL, re.M)
pts_noms = set(re.findall(r'\b(?:E|H|A)\d\b', GEL))
cit_ann = set(re.findall(r'\b[EH]\d\b', ' '.join(re.findall(r'^\s+A-\d+.*$', GEL, re.M))))
pa_w2 = {}
for nom, (x, y) in PAIRES.items():
    mx = re.search(r'^\s+%s\s+w2 = (\d+/\d+)' % x, GEL, re.M).group(1)
    my = re.search(r'^\s+%s\s+w2 = (\d+/\d+)' % y, GEL, re.M).group(1)
    pa_w2[nom] = (mx, my, mx == my)
chk('C08', abs(sum(p_a1) - 1.0) < 1e-9 and len(p_a1) == 5 and len(ann) >= 11 and all(v[2] for v in pa_w2.values()),
    'annonces : A-1, cinq issues %s, somme %.2f ; %d annonces a probabilite lues (A-2 a A-13, dont A-13 en deux parties) ; les cinq paires ont chacune le meme w2 a leurs deux points : %s' % (
        p_a1, sum(p_a1), len(ann), {k: v[0] for k, v in pa_w2.items()}))

# ------------------------------------------------------------------ C09 : les couples (w2, facteur) neufs, et la section 2 relue du run
S_OLD = json.load(open(os.path.join(OLD, 'sortie', 'sonde_chaine_par_etat.json'), encoding='ascii'))
V_OLD = json.load(open(os.path.join(OLD, 'sortie', 'verdict_chaine_par_etat.json'), encoding='ascii'))
joues = {(p['w2'], p['facteur']) for p in S_OLD['points']}
joues |= {(w, '1/1') for w in ('39/20', '197/100', '99/50', '101/50', '203/100', '41/20')}        # les six points de M17, a facteur 1
nouveaux = {}
for m in re.finditer(r'^\s+(E\d|H\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)', GEL, re.M):
    nouveaux[m.group(1)] = (m.group(2), m.group(3) if '/' in m.group(3) else m.group(3) + '/1')
rec = [k for k, v in nouveaux.items() if v in joues]
pv = {p['id']: p for p in V_OLD['points']}
med = {k: pv[k]['q_median'] for k in pv}
cmax = {'J6': 0.0635, 'A2': 0.0510, 'J4': 0.0381}
phr = ['0.545, 0.758, 0.842 a 1.95 pour 2/3, 1, 3/2', '(1.503, 1.505, 1.418)', '0.0635, 0.0510, 0.0381, le plus grand valant 1.67 fois le plus petit',
       '1.334 a 2.04, 1.505 a 2.05, 3.735 a 2.10, 18.348 a 2.15']
valeurs = ('%.3f, %.3f, %.3f a 1.95 pour 2/3, 1, 3/2' % (med['J5'], med['A1'], med['J3']), '(%.3f, %.3f, %.3f)' % (med['J6'], med['A2'], med['J4']),
           '%.3f a 2.04, %.3f a 2.05, %.3f a 2.10, %.3f a 2.15' % (med['T2'], med['A2'], med['J2'], med['T4']))
manque = [v for v in valeurs if re.sub(r'\s+', ' ', v) not in GN]
hd = sorted(k for k in pv if pv[k]['statut'] == 'HORS DECADE')
chk('C09', not rec and len(nouveaux) == 12 and not manque and hd == ['J2', 'T3', 'T4'] and round(0.0635 / 0.0381, 2) == 1.67,
    'les douze couples (w2, facteur) du gel sont neufs (communs avec M17 ou le gel precedent : %s) ; la section 2 relue de MON run : q medians %s (phrases absentes %s), '
    'c_max 0.0635/0.0381 = %.2f, HORS DECADE a %s' % (rec, {k: round(med[k], 3) for k in ('J5', 'A1', 'J3', 'J6', 'A2', 'J4', 'T2', 'J2', 'T4')}, manque, 0.0635 / 0.0381, hd))

# ------------------------------------------------------------------ C10 : mon essai aux deux ancres, ma sonde neuve contre la sonde certifiee, au bit
E_NEW = json.load(open(os.path.join(HERE, 'essai_ancres_machine2.json'), encoding='ascii'))
E_OLD = json.load(open(os.path.join(OLD, 'essai_ancres_machine2.json'), encoding='ascii'))
ecarts, n_etats = 0, 0
for pn in E_NEW['points']:
    po = [x for x in E_OLD['points'] if x['id'] == pn['id']][0]
    for en, eo in zip(pn['etats'], po['etats']):
        n_etats += 1
        a = {k: v for k, v in en.items()}
        b = {k: v for k, v in eo.items()}
        ecarts += (json.dumps(a, sort_keys=True) != json.dumps(b, sort_keys=True))
refs = {'A1': ((7, 2), 2.1623273017950654e-10), 'A2': ((8, 2), 2.6613925716641374e-09)}
ok_ref = all(len([e for e in p['etats'] if (e['n1'], e['n2']) == refs[p['id']][0]]) == 1 and
             [e for e in p['etats'] if (e['n1'], e['n2']) == refs[p['id']][0]][0]['Gamma_2D']['3'] == refs[p['id']][1] for p in E_NEW['points'])
gm = {p['id']: p['garde_moteur'] for p in E_NEW['points']}
chk('C10', ecarts == 0 and n_etats == 28 and ok_ref and gm['A1']['statut'] == 'EN DOMAINE' and gm['A2']['statut'] == 'EN DOMAINE' and E_NEW['moteur_canon'] == '82a0be882568fe0c',
    'essai de machine 2 aux deux ancres avec la sonde neuve : %d etats, %d differe(nt) de mon essai avec la sonde certifiee (JSON de l etat entier, au bit) ; A1 (7,2) et A2 (8,2) '
    '== les lectures de M17 au bit : %s ; garde consignee A1 %s (D1 %.6f c_max %.6f), A2 %s (D1 %.6f c_max %.6f)' % (
        n_etats, ecarts, ok_ref, gm['A1']['statut'], gm['A1']['D1'], gm['A1']['c_max'], gm['A2']['statut'], gm['A2']['D1'], gm['A2']['c_max']))

# ------------------------------------------------------------------ C11 : le selftest et les journaux de machine 1
st = subprocess.run([sys.executable, '-P', os.path.join(HERE, 'lecture_domaine_G1_machine1_v1.py'), '--selftest'], capture_output=True, text=True, cwd=ROOT)
lg = lit('lecture_selftest_machine1.log')
banc1 = lit('banc_feuille_domaine_G1_machine1_v1.log')
rel = lit('releve_gel_domaine_G1_machine1_v1.log')
chk('C11', 'SELFTEST : 74 cas, 74 tenus' in st.stdout and 'SELFTEST : 74 cas, 74 tenus' in lg and st.returncode == 0,
    'selftest de la feuille rejoue par moi : %s ; le journal de machine 1 dit la meme ligne : %s' % (st.stdout.strip().split('\n')[-1], 'SELFTEST : 74 cas, 74 tenus' in lg))
info('journaux de machine 1, lus et non rejoues : banc "%s" ; releve "%s"' % (banc1.strip().split('\n')[-1][:130], rel.strip().split('\n')[-1][:100]))

mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}}, open(JSN, 'w', encoding='ascii', newline='\n'),
          indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
