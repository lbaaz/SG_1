# -*- coding: ascii -*-
"""CONTROLES DE LECTURE par machine 2 du gel "la chaine E-A au second ordre" (41153158190cf7f1), de sa sonde et de sa feuille, 2026-11-14.
Chaque controle est recalcule de MES sources (le lot recu, le registre public clone a 79e77d2, mes runs et mes journaux), pas des scripts de construction ni du releve de
machine 1, sauf C03 et C04 qui REJOUENT ses constructions pour comparer octet a octet. Ce script ne modifie rien d'autre que ses sorties (controles_gel_ordre2_machine2_v1.log/.json).
Usage (depuis BOCAL4) : python -P ordre2/controles_gel_ordre2_machine2_v1.py <clone du registre>"""
import ast
import hashlib
import importlib.util
import io
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
import zipfile

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REG = os.path.abspath(sys.argv[1])
LOG = os.path.join(HERE, 'controles_gel_ordre2_machine2_v1.log')
JSN = os.path.join(HERE, 'controles_gel_ordre2_machine2_v1.json')
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


def charger(chemin, nom):
    sp = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m


GEL_NOM = 'gel_ordre2_chaine_EA_pre_enregistrement_v1.md'
GEL = lit(GEL_NOM)
GN = re.sub(r'\s+', ' ', GEL)
dire('CONTROLES DE MACHINE 2 : gel %s, sa sonde et sa feuille' % GEL_NOM)

# ------------------------------------------------------------------ C01 : le lot
man = rd(os.path.join(ROOT, 'MANIFEST_lot_machine1_gel_ordre2_chaine_EA_v1.txt'))
zl = zipfile.ZipFile(os.path.join(ROOT, 'lot_machine1_2026-11-14_gel_ordre2_chaine_EA_v1_recu.zip'))
att, bad = {}, []
for l in man.decode().split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
        if emp(zl.read(p[4])) != att[p[4]] or emp(rd(os.path.join(HERE, p[4]))) != att[p[4]]:
            bad.append(p[4])
chk('C01', len(att) == 34 and not bad and emp(man)[0] == '3bc363266957de56' and emp(zl.read(GEL_NOM))[0] == '41153158190cf7f1' and len(zl.namelist()) == 34,
    '34 pieces sur 34 au canon, a l empreinte brute et aux deux tailles (zip et copie de travail) ; ecarts %s ; CANON DU LOT %s (annonce 3bc363266957de56) ; gel %s' % (
        bad, emp(man)[0], emp(zl.read(GEL_NOM))[0]))

# ------------------------------------------------------------------ C02 : les canons cites par le gel
head = subprocess.run(['git', '-C', REG, 'rev-parse', '--short=7', 'HEAD'], capture_output=True, text=True).stdout.strip()
paires = re.findall(r'^\s+([\w./-]+\.(?:py|md|json|log|txt))\s+([0-9a-f]{16})$', GEL, re.M)
mauvais, resolus = [], 0
for nom, c in paires:
    if '/' in nom:
        p = os.path.join(REG, nom)
        ok = os.path.isfile(p) and emp(rd(p))[0] == c
    else:
        ok = nom in att and att[nom][0] == c and emp(rd(os.path.join(HERE, nom)))[0] == c
    resolus += ok
    if not ok:
        mauvais.append((nom, c))
cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', re.sub(r'[0-9]\.[0-9]+e-[0-9]+', ' ', GEL))))       # sans les litteraux flottants (les constantes de G-4 et G-8)
connus = {c for _, c in paires} | {emp(man)[0]}
for dp, dn, fn in os.walk(os.path.join(REG, 'journal')):
    for f in fn:
        if f.endswith('.md'):
            connus.add(emp(rd(os.path.join(dp, f)))[0])
nonres = [c for c in cites if c not in connus]
chk('C02', head == '79e77d2' and not mauvais and len(paires) == 29 and set(nonres) <= {'119f4e4dcbb4baba', 'b59651f99e60707a', 'e718d2db619af9b1'},
    'tete du registre lue : %s (le gel : 79e77d2) ; %d couples (nom, canon) de la section 1 : %d relus (registre au chemin donne, lot au manifeste et a ma copie) ; ecarts %s ; '
    'empreintes de 16 chiffres citees : %d, non resolues par un couple : %s' % (head, len(paires), resolus, mauvais, len(cites), nonres))
info('119f4e4dcbb4baba (la note d anteriorite hors chaine) est citee par le gel et ne m a pas ete remise : je ne l ai pas lue ; le gel n en tire rien ("ce gel ne revendique rien sur la methode") ; '
     'b59651f99e60707a et e718d2db619af9b1 sont citees sans couple de nom : le gel precedent et son acte, au registre aux chemins gels/ et journal/, canons relus a part ci-dessous')
g_prec = emp(rd(os.path.join(REG, 'gels', 'gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md')))[0]
a_prec = emp(rd(os.path.join(REG, 'journal', 'journal_delta_97_domaine_G1_chaine_EA_v1.md')))[0]
chk('C02b', g_prec == 'b59651f99e60707a' and a_prec == 'e718d2db619af9b1', 'le gel precedent et son acte, relus au registre : %s %s' % (g_prec, a_prec))

# ------------------------------------------------------------------ C03 : la reconstruction du gel depuis le gabarit (par le script de machine 1, rejoue)
stage = tempfile.mkdtemp(prefix='stage_gel_', dir=os.environ.get('TMPDIR_M2') or None)
os.makedirs(os.path.join(stage, 'essai'))
for f in os.listdir(HERE):
    if os.path.splitext(f)[1] in ('.py', '.log', '.txt', '.json') and os.path.isfile(os.path.join(HERE, f)) and not f.startswith(('controles_', 'bloc_independant', 'banc_feuille_ordre2_machine2', 'garde_et')):
        shutil.copyfile(os.path.join(HERE, f), os.path.join(stage, f))
for f in ('sonde_essai_ancres_machine1.json', 'lecture_essai_ancres_machine1.log'):
    shutil.copyfile(os.path.join(HERE, f), os.path.join(stage, 'essai', f))
out = os.path.join(stage, 'gel_reconstruit.md')
note_nom = 'note_machine1_residuel_chaine_EA_second_ordre_2026-11-14_v1.md'
r = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'construction_gel_ordre2_machine1_v1.py'), os.path.join(HERE, 'gel_ordre2_chaine_EA_gabarit.txt'), stage,
                    os.path.join(HERE, note_nom), os.path.join(HERE, 'ordre2_par_etat_v3.json'), out], capture_output=True, text=True)
egal = os.path.isfile(out) and rd(out) == rd(os.path.join(HERE, GEL_NOM))
chk('C03', r.returncode == 0 and egal, 'rejeu de la construction du gel (gabarit + 23 canons poses depuis les pieces, comptes lus dans les journaux de selftest et de banc) : code %d ; '
    'gel reconstruit == gel du lot, octet pour octet : %s ; canon %s' % (r.returncode, egal, emp(rd(out))[0] if os.path.isfile(out) else None))
shutil.rmtree(stage, ignore_errors=True)

# ------------------------------------------------------------------ C04 : la sonde = la sonde du registre + les blocs du diff, appliques par MON code
old_s = open(os.path.join(REG, 'scripts', 'sonde_domaine_G1_machine1_v1.py'), encoding='ascii').read().split('\n')
new_txt = lit('sonde_ordre2_machine1_v1.py')
new_s = new_txt.split('\n')
dif = lit('diff_sonde_sur_940a21b1d562bb49.txt').split('\n')
res, pos, i, nblocs = [], 0, 0, 0
removed, added = [], []
while i < len(dif):
    m = re.match(r'^(\d+)(?:,(\d+))?([acd])(\d+)(?:,(\d+))?$', dif[i])
    if not m:
        i += 1
        continue
    nblocs += 1
    a1 = int(m.group(1))
    a2 = int(m.group(2) or m.group(1))
    op = m.group(3)
    i += 1
    olds, news = [], []
    while i < len(dif) and not re.match(r'^\d+(?:,\d+)?[acd]\d+(?:,\d+)?$', dif[i]):
        l = dif[i]
        if l.startswith('< '):
            olds.append(l[2:])
        elif l.startswith('> '):
            news.append(l[2:])
        i += 1
    debut = a1 if op == 'a' else a1 - 1                 # indice (base 0) de la premiere ligne touchee ; 'a' : apres la ligne a1
    res += old_s[pos:debut]
    if op != 'a':
        assert old_s[debut:a2] == olds, 'lignes otees != lignes du fichier (bloc %d)' % nblocs
        pos = a2
    else:
        pos = debut
    res += news
    removed += olds
    added += news
res += old_s[pos:]
base_ok = emp(('\n'.join(old_s)).encode())[0] == '940a21b1d562bb49'
chk('C04', res == new_s and nblocs == 8 and base_ok and emp(new_txt.encode())[0] == '24315c52b234319c',
    'sonde : la sonde du registre 940a21b1d562bb49 (relue au chemin scripts/) + les %d blocs du diff de machine 1 (6 hunks de construction), appliques par mon code, == la sonde du lot '
    '24315c52b234319c (%d lignes) : %s ; lignes otees %d, ajoutees %d' % (nblocs, len(new_s), res == new_s, len(removed), len(added)))
guillemets = [i for i, l in enumerate(old_s) if '"""' in l]
i_doc = guillemets[1] if old_s[guillemets[0]].count('"""') == 1 else guillemets[0]            # fin de la docstring de la sonde du registre : la 2e ligne qui porte les guillemets triples
i_sortie = next(i for i, l in enumerate(old_s) if l.strip().startswith('sortie = {'))
i_fin_sortie = next(i for i, l in enumerate(old_s) if i > i_sortie and '"points": []}' in l)
etrangeres = []
for l in removed:
    k = old_s.index(l)
    en_doc = k <= i_doc
    en_points = l.strip().startswith('("') and l.strip().endswith(('),', ')),'))
    en_sortie = i_sortie <= k <= i_fin_sortie
    if not (en_doc or en_points or en_sortie):
        etrangeres.append(l)
mes_sortie = [l for l in removed if i_sortie <= old_s.index(l) <= i_fin_sortie and re.search(r'decomposer|np\.linalg|M\.H_2D|gamma_chaine|barriere|garde_domaine', l)]
chk('C04b', not etrangeres and not mes_sortie,
    'sonde : les %d lignes otees par le diff sont toutes ou de la docstring (jusqu a la ligne %d), ou des lignes de la table POINTS, ou du dictionnaire de consignation "sortie" (metadonnees : '
    'lignes %d a %d) ; aucune ne porte une mesure (decomposition, H_2D, chaine du moteur, garde) ; lignes otees hors de ces trois endroits : %s' % (len(removed), i_doc + 1, i_sortie + 1, i_fin_sortie + 1, etrangeres))
bloc_txt = lit('chaine_ordre2_bloc_machine1_v1.py')
chk('C04c', bloc_txt.rstrip('\n') in new_txt and emp(bloc_txt.encode())[0] == '7cd5977bc27bebc1',
    'sonde : le bloc 7cd5977bc27bebc1 y est insere tel quel (texte contenu dans la sonde, au caractere pres)')
lectures = [i + 1 for i, l in enumerate(new_s) if 'statut' in l]
ok_nobranche = all(not re.search(r'^\s*(if|elif|while)\b.*statut', new_s[i - 1]) for i in lectures)
seuils = [l for l in added if re.search(r'\b(1\.25|1\.6|0\.06|0\.10|0\.12|1\.33e-1[23]|0\.01\b|TENU|TOMBE|MIEUX)\b', l)]
chk('C05', ok_nobranche and not seuils,
    'sonde : aucune condition ne porte sur le statut de la garde (la garde est CONSIGNEE, JAMAIS APPLIQUEE) ; aucune ligne ajoutee ne porte un seuil, une borne ou un verdict du gel : %s' % seuils)

# ------------------------------------------------------------------ C06 : la feuille, les criteres herites au caractere pres (arbres ast)
src_old = open(os.path.join(REG, 'scripts', 'lecture_domaine_G1_machine1_v1.py'), encoding='ascii').read()
src_new = lit('lecture_ordre2_machine1_v1.py')


def fonction(src, nom):
    t = ast.parse(src)
    return [n for n in ast.walk(t) if isinstance(n, ast.FunctionDef) and n.name == nom][0]


def corps(f):
    b = list(f.body)
    if b and isinstance(b[0], ast.Expr) and isinstance(getattr(b[0], 'value', None), ast.Constant) and isinstance(b[0].value.value, str):
        b = b[1:]
    return b


co, cn = corps(fonction(src_old, 'motif_exclusion')), corps(fonction(src_new, 'motif_exclusion'))
herites = [ast.dump(x) for x in co[:-1]]
neufs = [ast.dump(x) for x in cn[:len(co) - 1]]
suite = cn[len(co) - 1:]
ev_o, ev_n = ast.dump(fonction(src_old, 'eval_fraction')), ast.dump(fonction(src_new, 'eval_fraction'))
n_if_neufs = sum(1 for x in suite if isinstance(x, ast.If))
chk('C06', herites == neufs and len(suite) == 6 and n_if_neufs == 3 and ast.dump(co[-1]) == ast.dump(cn[-1])
    and emp(rd(os.path.join(REG, 'scripts', 'lecture_domaine_G1_machine1_v1.py')))[0] == '0a760e3a244e547d',
    'feuille : les %d instructions de motif_exclusion qui portent les huit criteres du gel precedent sont celles de la feuille du registre 0a760e3a244e547d, au caractere pres (arbres ast) : %s ; '
    'suivent 3 criteres neufs (9) a (11), avec leurs deux affectations, et le meme "return None" : %d instructions, dont %d conditions' % (len(co) - 1, herites == neufs, len(suite), n_if_neufs))
chk('C06b', ev_o == ev_n, 'feuille : eval_fraction == celle du registre (arbre ast)')

# ------------------------------------------------------------------ C07 : la cascade du gel par enumeration exhaustive (3^12 vecteurs de statuts) contre lire_bandes de la feuille
F = charger(os.path.join(HERE, 'lecture_ordre2_machine1_v1.py'), 'feuille_m1')
STAT = ['TENU', 'TOMBE', 'NON LISIBLE']
JUG = [k for k in sorted(F.ATTENDUS) if F.ATTENDUS[k][0] == 'juge']
BANDE_DE = {k: F.ATTENDUS[k][3] for k in JUG}
cnt, desaccord = {}, 0
for vec in itertools.product(STAT, repeat=12):
    st = dict(zip(JUG, vec))
    bandes = {}
    for b in ('proche', 'moyenne', 'lointaine'):
        lis = [k for k in JUG if BANDE_DE[k] == b and st[k] != 'NON LISIBLE']
        bandes[b] = 'NL' if len(lis) < 3 else ('T' if all(st[k] == 'TENU' for k in lis) else 'N')
    if bandes['proche'] == 'NL':
        v = 'NON LISIBLE'
    elif bandes['proche'] == 'N':
        v = "L'ORDRE 2 NE TIENT PAS"
    elif bandes['moyenne'] != 'T':
        v = "L'ORDRE 2 TIENT JUSQU'A 0.06"
    elif bandes['lointaine'] != 'T':
        v = "L'ORDRE 2 TIENT JUSQU'A 0.10"
    else:
        v = "L'ORDRE 2 TIENT"
    cnt[v] = cnt.get(v, 0) + 1
    v_f, b_f = F.lire_bandes([{'id': k, 'bande': BANDE_DE[k], 'statut': st[k], 'x': st[k]} for k in JUG], 'x')
    if v_f != v or any({'TENUE': 'T', 'NON TENUE': 'N', 'NON LISIBLE': 'NL'}[b_f[b]['issue']] != bandes[b] for b in bandes):
        desaccord += 1
chk('C07', desaccord == 0 and sum(cnt.values()) == 531441,
    'sections 6 et 7 : sur les 3^12 = 531441 vecteurs de statuts (TENU, TOMBE, NON LISIBLE) des douze points juges, la cascade que j ai ecrite du texte du gel (premiere bande qui n est pas TENUE '
    'arrete la lecture) == lire_bandes de la feuille, verdict et issue de chaque bande (desaccords %d) ; repartition %s' % (desaccord, dict(sorted(cnt.items()))))

# ------------------------------------------------------------------ C08 : les annonces
a1 = re.search(r'A-1\s+le verdict : (.*?)\n\s+A-2', GEL, re.S).group(1)
p_a1 = [float(re.findall(r'\b0\.\d\d\b', item)[-1]) for item in re.sub(r'\s+', ' ', a1).split(';')]       # la probabilite est le dernier nombre de chaque issue
ann = re.findall(r'^\s+A-(\d+)\s+', GEL, re.M)
noms_pts = set(re.findall(r'^\s+(C\d|M\d|L\d|A\d|W\d)\s+w2 = ', GEL, re.M))
cit = set(re.findall(r'\b[CMLW]\d\b', ' '.join(re.findall(r'^\s+A-\d+.*$', GEL, re.M))))
chk('C08', abs(sum(p_a1) - 1.0) < 1e-9 and len(p_a1) == 6 and len(ann) == 15 and cit <= noms_pts and len(noms_pts) == 16,
    'annonces : A-1, six issues %s, somme %.2f ; %d annonces A-1 a A-15 ; les points qu elles nomment %s sont des points de la section 4' % (p_a1, sum(p_a1), len(ann), sorted(cit)))

# ------------------------------------------------------------------ C09 : les couples (w2, facteur) neufs
J1 = json.load(open(os.path.join(REG, 'journal', 'sonde_chaine_par_etat.json'), encoding='ascii'))
J2 = json.load(open(os.path.join(REG, 'journal', 'sonde_domaine_G1.json'), encoding='ascii'))
joues = {(p['w2'], p['facteur']) for p in J1['points'] + J2['points']}
joues |= {(w, '1/1') for w in ('39/20', '197/100', '99/50', '101/50', '203/100', '41/20')}        # les six points de M17, a facteur 1
tab = {}
for m in re.finditer(r'^\s+(C\d|M\d|L\d|A\d|W\d)\s+w2 = (\d+/\d+)\s+facteur (\S+)', GEL, re.M):
    tab[m.group(1)] = (m.group(2), m.group(3) if '/' in m.group(3) else m.group(3) + '/1')
neufs_ids = [k for k in tab if k[0] in 'CMLW']
rec = [k for k in neufs_ids if tab[k] in joues]
facs = {f for (_, f) in joues}
chk('C09', len(tab) == 16 and len(neufs_ids) == 14 and not rec and not ({'3/4', '4/3', '1/2'} & facs) and len(joues) == 24 + 6 - 2,
    'les quatorze couples (w2, facteur) juges et temoins sont neufs : communs avec M17 ou les deux runs deja joues (JSON du registre) : %s ; les facteurs 3/4, 4/3 et 1/2 ne sont dans aucun '
    'couple joue (facteurs joues : %s) ; %d couples joues au total' % (rec, sorted(facs), len(joues)))

# ------------------------------------------------------------------ C10 : mes essais aux deux ancres (16 fils et 1 fil), contre ceux de machine 1, contre les constantes du gel
E_M2 = json.load(open(os.path.join(HERE, 'essai_ancres_machine2.json'), encoding='ascii'))
E_M2_1 = json.load(open(os.path.join(HERE, 'essai_ancres_machine2_1fil.json'), encoding='ascii'))
E_M1 = json.load(open(os.path.join(HERE, 'sonde_essai_ancres_machine1.json'), encoding='ascii'))
E_PREC = json.load(open(os.path.join(ROOT, 'domaine_G1', 'essai_ancres_machine2.json'), encoding='ascii'))
REFS = {'A1': ((7, 2), 2.1623273017950654e-10, 2.3236497766513317e-10, 0.002118984943055927), 'A2': ((8, 2), 2.6613925716641374e-09, 2.794344791699548e-09, -0.0028201377357584354)}
ok_refs = all(repr(x) in GN for v in REFS.values() for x in v[1:])


def ancre(E, pid):
    p = [x for x in E['points'] if x['id'] == pid][0]
    (n1, n2) = REFS[pid][0]
    return [e for e in p['etats'] if (e['n1'], e['n2']) == (n1, n2)]


def ecarts_ancres(E):
    o = []
    for pid, (_, r2d, rf, rde) in REFS.items():
        t = ancre(E, pid)
        if len(t) != 1:
            return None
        e = t[0]
        o.append((abs(e['Gamma_2D']['3'] / r2d - 1), abs(e['chaine2']['gammas_flux'][2] / rf - 1), abs(e['chaine2']['dE'][2] / rde - 1)))
    return o


ecs = {n: ecarts_ancres(E) for n, E in (('16 fils', E_M2), ('1 fil', E_M2_1), ('machine 1', E_M1))}
tol_ok = all(e is not None and all(a < 1e-2 and b < 1e-3 and c < 1e-6 for a, b, c in e) for e in ecs.values())
chk('C10', ok_refs and tol_ok and all(E['moteur_canon'] == '82a0be882568fe0c' and E['sonde_canon'] == '24315c52b234319c' for E in (E_M2, E_M2_1, E_M1)),
    'aux deux ancres, l etat (7,2) de A1 et l etat (8,2) de A2 existent une seule fois et rendent, a 1e-2 (G-4), 1e-3 et 1e-6 (G-8) : ecarts relatifs (Gamma_2D(3), Gamma d ordre 2, dE) '
    '[A1, A2] : mon essai a 16 fils %s ; a 1 fil %s ; celui de machine 1 %s ; les quatre constantes sont dans le texte du gel : %s' % (
        [tuple('%.1e' % x for x in t) for t in ecs['16 fils']], [tuple('%.1e' % x for x in t) for t in ecs['1 fil']], [tuple('%.1e' % x for x in t) for t in ecs['machine 1']], ok_refs))
# la garde du moteur consignee aux ancres == la table
gm_ok = all(abs(p['garde_moteur']['D1'] - d1) < 5e-7 and abs(p['garde_moteur']['c_max'] - cm) < 5e-7 and p['garde_moteur']['statut'] == 'EN DOMAINE'
            for p, (d1, cm) in zip(E_M2['points'], ((0.055556, 0.040917), (0.050000, 0.051012))))
# les champs de l'essai du gel precedent, retrouves a l'identique (gel, section 15 : 737 champs)


def aplat(x, pre=''):
    if isinstance(x, dict):
        for k in sorted(x):
            yield from aplat(x[k], pre + '/' + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from aplat(v, '%s[%d]' % (pre, i))
    else:
        yield pre, x


def champs_communs(Enew, Eold):
    a = {k: v for p in Enew['points'] for k, v in aplat({kk: vv for kk, vv in p.items() if kk not in ('duree_s',)}, '/' + p['id'])}
    b = {k: v for p in Eold['points'] for k, v in aplat({kk: vv for kk, vv in p.items() if kk not in ('duree_s',)}, '/' + p['id'])}
    comm = [k for k in a if k in b and '/chaine2' not in k and '/E_libre' not in k]
    return len(comm), sum(1 for k in comm if a[k] != b[k])
nc, nd = champs_communs(E_M2, E_PREC)
n1c, n1d = champs_communs(E_M2_1, E_M1)
chk('C10b', gm_ok and nc >= 700 and nd == 0,
    'mon essai avec la sonde neuve, compare champ a champ a mon essai du gel precedent (meme machine, memes fils) : %d champs communs hors chaine d ordre 2 et energie libre, %d different(s) '
    '(le gel, section 15 : 737 champs a l identique, annonce par machine 1 sur ses propres essais) ; garde du moteur consignee aux ancres == la table : %s' % (nc, nd, gm_ok))
etiq = all([(e['n1'], e['n2']) for e in a['etats']] == [(e['n1'], e['n2']) for e in b['etats']] for a, b in zip(E_M2['points'], E_M1['points']))
etiq1 = all([(e['n1'], e['n2']) for e in a['etats']] == [(e['n1'], e['n2']) for e in b['etats']] for a, b in zip(E_M2_1['points'], E_M1['points']))
dmax, rel_haut, ch2max, dmax_j, dmax_j3 = 0.0, 0.0, 0.0, 0.0, 0.0
for a, b in zip(E_M2_1['points'], E_M1['points']):
    for ea, eb in zip(a['etats'], b['etats']):
        for k in ('2', '3', '4'):
            dmax = max(dmax, abs(ea['Gamma_2D'][k] - eb['Gamma_2D'][k]))
            if min(ea['Gamma_2D']['3'], eb['Gamma_2D']['3']) > 1.33e-12:
                dmax_j = max(dmax_j, abs(ea['Gamma_2D'][k] - eb['Gamma_2D'][k]))
                if k == '3':
                    dmax_j3 = max(dmax_j3, abs(ea['Gamma_2D'][k] - eb['Gamma_2D'][k]))
            if min(ea['Gamma_2D'][k], eb['Gamma_2D'][k]) > 1e-10:
                rel_haut = max(rel_haut, abs(ea['Gamma_2D'][k] - eb['Gamma_2D'][k]) / ea['Gamma_2D'][k])
        if ea['Gamma_2D']['3'] > 1.33e-12:
            ca, cb = ea['chaine2'], eb['chaine2']
            if ca['definie'] and cb['definie']:
                ch2max = max(ch2max, abs(ca['gammas_flux'][2] - cb['gammas_flux'][2]) / cb['gammas_flux'][2])
info('essai a 1 fil contre celui de machine 1 (machines differentes : Windows, numpy 2.2.6, 16 coeurs contre Linux, numpy 2.5.3, levier X86_V4) : memes etiquettes aux 28 etats %s ; '
     'ecart absolu maximal de Gamma_2D(3) aux etats de Gamma_2D(3) > 1.33e-12 : %.2e ; aux trois barreaux k = 2, 3, 4 : %.2e aux memes etats, %.2e sur tous les etats (le bruit de fils que mon run precedent a mesure : 7.32e-14, le plancher du gel : 1.33e-13) ; '
     'relatif maximal au-dessus de 1e-10 : %.2e ; Gamma_flux de l ordre 2 aux etats juges (Gamma_2D > 1.33e-12) : ecart relatif maximal %.2e' % (etiq1, dmax_j3, dmax_j, dmax, rel_haut, ch2max))
chk('C10c', etiq and etiq1 and dmax_j3 < 1.33e-13 and dmax_j < 2.5e-13 and rel_haut < 2e-3 and ch2max < 0.1,
    'mes essais (16 fils et 1 fil) et celui de machine 1 portent les memes etiquettes aux 28 etats ; aux etats de Gamma_2D(3) > 1.33e-12, Gamma_2D(3) differe de moins de 1.33e-13 en absolu (le plancher, la marge de bruit de la borne : '
    'machines differentes, fils differents), et les trois barreaux k = 2, 3, 4 de moins de 2.5e-13 ; de moins de 2e-3 en relatif au-dessus de 1e-10 ; Gamma_flux de l ordre 2 aux etats juges a moins de 10 pour cent')

# ------------------------------------------------------------------ C11 : le selftest, le banc et le releve de machine 1, REJOUES
st = subprocess.run([sys.executable, '-P', os.path.join(HERE, 'lecture_ordre2_machine1_v1.py'), '--selftest'], capture_output=True, text=True, cwd=ROOT)
lg = lit('lecture_selftest_machine1.log')
ligne_st = 'SELFTEST : 160 cas, 160 tenus'
chk('C11', ligne_st in st.stdout and ligne_st in lg and st.returncode == 0 and len(re.findall(r'^  TIENT  ', st.stdout, re.M)) == 160 and len(re.findall(r'^  MORD ', st.stdout, re.M)) == 0,
    'selftest de la feuille rejoue par moi : %s ; le journal de machine 1 dit la meme ligne : %s' % (st.stdout.strip().split('\n')[-1], ligne_st in lg))
bn = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'banc_feuille_ordre2_machine1_v1.py'), os.path.join(HERE, 'lecture_ordre2_machine1_v1.py')], capture_output=True, text=True, cwd=HERE)
bnl = lit('banc_feuille_ordre2_machine1_v1.log')
lignes_b = [l for l in bn.stdout.split('\n') if l.startswith('BANC') or l.startswith('survivantes')]
chk('C11b', 'BANC, famille T (la table) : 131 alterations, 131 mordues, 0 survivantes' in bn.stdout and 'BANC, famille C (le code)  : 109 alterations, 108 mordues, 1 survivantes' in bn.stdout
    and 'survivantes : C82b' in bn.stdout, 'banc de machine 1 REJOUE par moi sur la feuille : %s' % ' | '.join(lignes_b))
rl = subprocess.run([sys.executable, '-I', os.path.join(HERE, 'releve_gel_ordre2_machine1_v1.py'), os.path.join(HERE, GEL_NOM), HERE, REG,
                     os.path.join(HERE, note_nom), os.path.join(HERE, 'ordre2_par_etat_v3.json'), os.path.join(ROOT, 'domaine_G1', 'sonde_essai_ancres_machine1.json')],
                    capture_output=True, text=True, cwd=HERE)
rl_fin = [l for l in rl.stdout.split('\n') if l.startswith('RELEVE')]
chk('C11c', rl_fin == ['RELEVE : 24 controles, 24 tenus'], 'releve de machine 1 REJOUE par moi (ses 24 controles, sur le gel, le lot, MON clone du registre a 79e77d2 et le journal d essai du gel precedent) : %s' % rl_fin)

# ------------------------------------------------------------------ C12 : mes autres journaux de certification
def journal(nom):
    p = os.path.join(HERE, nom)
    return open(p, encoding='ascii').read() if os.path.isfile(p) else ''


jb = journal('bloc_independant_machine2_v1.log')
jg = journal('garde_et_boites_machine2_v1.log')
jg1 = journal('garde_et_boites_machine2_1fil.log')
ja = journal('banc_feuille_ordre2_machine2_v1.log')
mj = re.search(r'BILAN : (\d+) controles, 0 mordent \[\]', jb)
chk('C12', bool(mj) and int(mj.group(1)) >= 16 and 'BILAN : 0 ecart(s) a la table des seize points' in jg, 'mes journaux : le bloc recalcule a part (%s) ; la garde G-1 du moteur et les boites aux seize points (%s)' % (
    jb.strip().split('\n')[-1], jg.strip().split('\n')[-1]))
tous = lambda t: t[t.index('TOUS CHIFFRES'):t.index('GROUPES')] if 'TOUS CHIFFRES' in t else None
chk('C12b', tous(jg) is not None and tous(jg) == tous(jg1), 'la garde du moteur aux seize points, imprimee a tous les chiffres : identique a 16 fils (defaut) et a 1 fil (OMP_NUM_THREADS = OPENBLAS_NUM_THREADS = MKL_NUM_THREADS = 1) : %s' % (tous(jg) == tous(jg1)))
mA = re.search(r'ecarts feuille / lecteur : (\d+)', ja)
mB = re.search(r'BILAN : (\d+) alterations ; motifs absents (\[.*?\]) ; survivent au selftest de machine 1 : (\[.*?\]) ; survivent a mon banc : (\[.*?\]) ; survivent aux deux : (\[.*?\])', ja)
chk('C12c', bool(mA) and mA.group(1) == '0' and bool(mB) and mB.group(2) == '[]' and mB.group(5) == '[69, 109]' and mB.group(4) == '[45, 69, 109]',
    'mon banc de la feuille : ecarts lecteur independant / feuille %s ; %s' % (mA.group(1) if mA else None, mB.group(0) if mB else None))

mauv = [c['id'] for c in CHK if not c['ok']]
dire('BILAN : %d controles, %d mordent %s' % (len(CHK), len(mauv), mauv))
json.dump({'controles': CHK, 'info': INFO, 'bilan': {'controles': len(CHK), 'mord': len(mauv), 'ids': mauv}}, open(JSN, 'w', encoding='ascii', newline='\n'), indent=1, sort_keys=True, ensure_ascii=True)
FH.close()
