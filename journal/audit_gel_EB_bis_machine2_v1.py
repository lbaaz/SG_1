# -*- coding: ascii -*-
"""AUDIT machine 2 du GEL E-B BIS v1 (dcda1611adf5f8fd) et de son instrument -- sonde v3 555146abd2192f79, feuille de
lecture v2 c14dafffc5f84c97, banc qui tue v3 3f2ef4d35af630c2 -- lot de machine 1 du 2026-11-13. Classe B.
Derive de mon audit de la sonde v2 (audit_sonde_EB_v2_machine2_v1.py, canon au lot 6bed68e12ec21e18).

E19 : AUCUN RUN DE L'ETAGE 1 NI 2 REEL JOUE. Calcule ici, et declare : les pre-vols (geometrie reduite, NON OPPOSABLES), le
banc, les portes de l'etage 2 par sentinelle (sans calcul), G-Q3 a taille reelle (matrices seulement, dans un etage 1 reel
qui doit REFUSER au premier fichier repris), et des LECTURES par la feuille (aucune decomposition) de sorties DEJA
EXISTANTES : celles de la nuit du 12/11 et mon diagnostic du 13/11. Rien du fantome n'est calcule.

Usage : python -P audit_gel_EB_bis_machine2_v1.py LOT_BIS REGISTRE MOTEUR DOSSIER_RUN MANIFESTE_RUN SORTIE_DIR
  LOT_BIS = le lot de machine 1 EXTRAIT ; REGISTRE = clone frais du registre (fe10bfe : mes exemplaires certifies de la
  sonde v2, de la feuille v1 et du banc v2, et le gel v2, y sont DEPOSES) ; SORTIE_DIR = dossier NEUF.
  Les scripts de machine 1 sont lances par 'python -P' depuis SORTIE_DIR."""
import collections
import difflib
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import unicodedata
from fractions import Fraction

sys.dont_write_bytecode = True
if len(sys.argv) != 7:
    print(__doc__)
    sys.exit(2)
LOT, REG, MOTEUR, RUN, MANIF, OUT = [os.path.abspath(x) for x in sys.argv[1:7]]
if os.path.exists(OUT) and os.listdir(OUT):
    sys.exit('SORTIE_DIR doit etre un dossier neuf et vide : %s' % OUT)
os.makedirs(OUT, exist_ok=True)
ICI = os.path.dirname(os.path.abspath(__file__))
PY = [sys.executable, '-P']
GEL = os.path.join(LOT, 'qualification_EB_bis_pre_enregistrement_v1.md')
SONDE = os.path.join(LOT, 'sonde_qualification_EB_machine1_v3.py')
LECT = os.path.join(LOT, 'lecture_qualification_EB_machine1_v2.py')
BANC = os.path.join(LOT, 'banc_qui_tue_qualification_EB_machine1_v3.py')
V2 = {'gel': os.path.join(REG, 'gels', 'qualification_EB_pre_enregistrement_v2.md'),
      'sonde': os.path.join(REG, 'scripts', 'sonde_qualification_EB_machine1_v2.py'),
      'lecture': os.path.join(REG, 'scripts', 'lecture_qualification_EB_machine1_v1.py'),
      'banc': os.path.join(REG, 'scripts', 'banc_qui_tue_qualification_EB_machine1_v2.py')}
NUIT = os.path.join(ICI, 'nuit_EB', 'sortie', 'sonde_etage1.json')
TABLE = os.path.join(ICI, 'tp_reference_machine2_v1.json')
RETENUS = os.path.join(ICI, 'tp_retenus_machine2_v1.json')
DIAGD = os.path.join(ICI, 'diagnostic_TP_echelle_forte')
LOG, CHK, CONS = [], [], {}


def say(s):
    LOG.append(s)
    print(s, flush=True)


def chk(nom, ok, detail=''):
    CHK.append((nom, bool(ok), detail))
    say('%-5s %s%s' % ('OK' if ok else 'MORD', nom, (' : ' + detail) if detail else ''))


def eb(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode('utf-8')
    return hashlib.sha256(t).hexdigest()[:16]


def lire(p):
    return open(p, 'rb').read()


def norm(s):
    return re.sub(r'\s+', ' ', s)


def courir(args, nom_log, cwd=OUT, timeout=3000):
    r = subprocess.run(PY + args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    txt = r.stdout + (('\n[stderr]\n' + r.stderr) if r.stderr.strip() else '')
    with open(os.path.join(OUT, nom_log), 'w', encoding='ascii', errors='replace', newline='\n') as fh:
        fh.write(txt)
    return r.returncode, r.stdout


def arrondi(ligne):
    return re.sub(r'[-+]?\d+\.\d+(?:[eE][-+]?\d+)?', lambda m: '%.3g' % float(m.group(0)), ligne)


def sonde_args(sortie, etage, extra=()):
    return [SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF, '--sortie', sortie,
            '--etage', str(etage)] + list(extra)


def lignes_changees(a, b):
    return [l for l in difflib.unified_diff(a.decode().splitlines(), b.decode().splitlines(), lineterm='', n=0)
            if l[:1] in '+-' and l[:3] not in ('+++', '---') and l[1:].strip()]


def lignes_diff(p):
    return [l for l in lire(p).decode().splitlines()
            if l[:1] in '+-' and l[:3] not in ('+++', '---') and l[1:].strip()]


def reconstruit(v1, v2, lignes):
    c = collections.Counter(l for l in v1.decode().splitlines() if l.strip())
    for l in lignes:
        c[l[1:]] += -1 if l[0] == '-' else 1
    return +c == collections.Counter(l for l in v2.decode().splitlines() if l.strip()) and min(c.values()) >= 0


# ================================================================ 1. le lot, les bases, les diffs
say('=== 1. LE LOT ENTRANT, MES BASES CERTIFIEES, LES DIFFS ===')
man = lire(os.path.join(LOT, 'MANIFEST_lot_machine1_gel_EB_bis_v1.txt'))
CONS['canon_lot_bis'] = eb(man)
pieces = [l.split() for l in man.decode('utf-8').splitlines()
          if not l.startswith('#') and len(l.split()) == 5 and len(l.split()[0]) == 16]
mal = []
for e, br, ob, obr, nom in pieces:
    r = lire(os.path.join(LOT, nom))
    try:
        ok = eb(r) == e
    except UnicodeDecodeError:
        ok = hashlib.sha256(r).hexdigest()[:16] == e
    if not ok or hashlib.sha256(r).hexdigest()[:16] != br or len(r) != int(obr):
        mal.append(nom)
chk('C01 lot bis : %d pieces au canon B, a l empreinte brute et a la taille (canon du lot %s)' % (
    len(pieces), CONS['canon_lot_bis']), len(pieces) == 29 and not mal, 'ecarts : %s' % (mal or 'aucun'))
BASES = {'gel': 'cde0cd11a763f26d', 'sonde': 'facc7536ba4637cb', 'lecture': 'b3ac958a1a2b915b', 'banc': '4e46744fe4e8a8be'}
ok_b = all(eb(lire(V2[k])) == c for k, c in BASES.items())
nouv = {'gel': GEL, 'sonde': SONDE, 'lecture': LECT, 'banc': BANC}
cn = {k: eb(lire(p)) for k, p in nouv.items()}
asc = all(all(b < 128 for b in lire(p)) and b'\r' not in lire(p) and cn['gel'].encode() in lire(p)
          for k, p in nouv.items() if k != 'gel')
chk('C02 mes bases du REGISTRE (fe10bfe) sont mes exemplaires certifies : gel v2 cde0cd11a763f26d, sonde v2 '
    'facc7536ba4637cb, feuille v1 b3ac958a1a2b915b, banc v2 4e46744fe4e8a8be ; les trois scripts livres sont ASCII, LF '
    'seul, et portent le canon du gel bis', ok_b and asc and cn['gel'] == 'dcda1611adf5f8fd',
    'gel bis %s, sonde v3 %s, feuille v2 %s, banc v3 %s' % (cn['gel'], cn['sonde'], cn['lecture'], cn['banc']))
CONS['canons'] = cn
ddiff = {'gel': 'diff_gel_EB_v2_bis_v1.txt', 'sonde': 'diff_sonde_EB_v2_v3.txt', 'lecture': 'diff_lecture_EB_v1_v2.txt',
         'banc': 'diff_banc_EB_v2_v3.txt'}
ok_d = {}
for k in ('gel', 'sonde', 'lecture', 'banc'):
    mes = collections.Counter(lignes_changees(lire(V2[k]), lire(nouv[k])))
    ses = collections.Counter(lignes_diff(os.path.join(LOT, ddiff[k])))
    ok_d[k] = (mes == ses, reconstruit(lire(V2[k]), lire(nouv[k]), lignes_diff(os.path.join(LOT, ddiff[k]))))
chk('C03 les quatre diffs joints sont exacts : memes lignes ajoutees et retirees que les MIENS (hors lignes vides), et '
    'chacun reconstruit son nouveau fichier depuis MA base du registre', all(a and b for a, b in ok_d.values()),
    '; '.join('%s : memes lignes %s, reconstruit %s' % (k, a, b) for k, (a, b) in ok_d.items()))
neutre = os.path.join(OUT, 'reconstruction')
os.makedirs(os.path.join(neutre, 'inst'))
rg = subprocess.run(PY + [os.path.join(LOT, 'construction_gel_EB_bis_machine1_v1.py'), REG, NUIT, TABLE, DIAGD,
                          os.path.join(REG, 'journal', 'lecture_piste0_etape0_machine1_v2.json'),
                          os.path.join(neutre, 'gel_bis.md'), os.path.join(neutre, 'construction_gel.log')],
                    cwd=neutre, capture_output=True, text=True, timeout=300)
ri = subprocess.run(PY + [os.path.join(LOT, 'construction_instrument_EB_bis_machine1_v1.py'),
                          os.path.join(REG, 'scripts'), GEL, os.path.join(neutre, 'inst'),
                          os.path.join(neutre, 'construction_instrument.log')],
                    cwd=neutre, capture_output=True, text=True, timeout=300)
with open(os.path.join(OUT, 'm2_reconstruction.log'), 'w', encoding='ascii', errors='replace', newline='\n') as fh:
    fh.write(rg.stdout + rg.stderr + ri.stdout + ri.stderr)
ig = os.path.join(neutre, 'gel_bis.md')
ii = {k: os.path.join(neutre, 'inst', os.path.basename(nouv[k])) for k in ('sonde', 'lecture', 'banc')}
ident = (rg.returncode == 0 and ri.returncode == 0 and os.path.isfile(ig) and lire(ig) == lire(GEL) and
         all(os.path.isfile(ii[k]) and lire(ii[k]) == lire(nouv[k]) for k in ii))
chk('C04 les DEUX constructions de machine 1, lues puis REJOUEES depuis MES exemplaires du registre (le gel v2 et les '
    'sources du gel : ma sortie de la nuit, ma table, mon diagnostic, la lecture de l etape 0), rendent le gel bis, la '
    'sonde v3, la feuille v2 et le banc v3 IDENTIQUES AU BIT a ceux livres ; chaque nombre tape par un hunk est affirme '
    'contre sa source par le script', ident,
    'gel %s ; sonde %s ; feuille %s ; banc %s ; %s' % (
        *('identique' if os.path.isfile(p) and lire(p) == lire(q) else 'DIFFERENT'
          for p, q in ((ig, GEL), (ii['sonde'], SONDE), (ii['lecture'], LECT), (ii['banc'], BANC))),
        (rg.stdout.strip().splitlines() or [''])[-2][:120]))

# ================================================================ 2. le gel : ses nombres, recalcules
say('=== 2. LE GEL BIS : SES NOMBRES, RECALCULES DE MES SOURCES ===')
gel_t = lire(GEL).decode('utf-8')
gel_n = norm(gel_t)
S1 = json.load(open(NUIT))
TAB = {r['j']: r for r in json.load(open(TABLE))['balayage']}
DIAG = {}
for g in ('G20', 'G30'):
    for r in json.load(open(os.path.join(DIAGD, 'diag_%s.json' % g))):
        DIAG[(r['j'], g, r['k'])] = r
PL = 1e-12


def serie_nuit(cle, cfg):
    out = {}
    for ks, rec in S1['TP'][cle]['traj'][cfg].items():
        e = rec['etats'][0]
        out[int(ks)] = e['gamma'] if e['suivi'] else None
    return out


def plateau(ser, kmin, kmax=12):
    best = None
    for k0 in range(kmin, kmax - 3):
        v = [ser.get(k) for k in range(k0, k0 + 5)]
        if any(x is None or x <= PL for x in v):
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


pire, tous = 0.0, True
for cle in ('j06', 'j08'):
    j = S1['TP'][cle]['j']
    for g in ('G20', 'G30'):
        ser = serie_nuit(cle, 'F1' + g)
        for k in (-5, -4, -3):
            ser[k] = DIAG[(j, g, k)]['gamma']
        p = plateau(ser, -5)
        tous = tous and bool(p and p['ok'])
        pire = max(pire, abs(math.log(p['Gamma_pl'] / TAB[j]['Gamma_ref'])))
chk('C05 gel 4 : sur mes series (la nuit pour k >= -2, mon diagnostic pour k = -5 a -3), la regle 3.11 rend PLATEAU aux '
    'quatre (g, geometrie), accord a la reference au pire %.4f (le gel dit 0.0012)' % pire,
    tous and '%.4f' % pire == '0.0012' and 'rend PLATEAU aux quatre' in gel_n, '')
ok51 = all(norm(s) in gel_n for s in (
    'j = 6 (g = %.5f, Gamma_ref %.4e, u_ref %.1e)' % (S1['TP']['j06']['g'], TAB[6]['Gamma_ref'], TAB[6]['u_ref']),
    'j = 8 (g = %.5f, Gamma_ref %.4e, u_ref %.1e)' % (S1['TP']['j08']['g'], TAB[8]['Gamma_ref'], TAB[8]['u_ref']),
    'j = 5 (Gamma_ref %.3e)' % TAB[5]['Gamma_ref']))
dep5 = TAB[5]['u_ref'] - 0.01
chk('C06 gel 5.1 : les couplages retenus et le bord j = 5 recalcules de MA table (j = 6 et 8 ; j = 5 hors liste, depasse le '
    'plafond de %.2e)' % dep5, ok51 and '%.2e' % dep5 == '1.96e-05' and '1.96e-05' in gel_n, '')
ov = [S1['TN']['traj'][k]['etats'][t]['ov'] for k in ('2', '4') for t in range(3)]
fen4 = []
for cle in ('j06', 'j08'):
    for cfg in ('F1G20', 'F1G30'):
        ser = serie_nuit(cle, cfg)
        for k0 in range(4, 9):
            v = [ser.get(k) for k in range(k0, k0 + 5)]
            if all(x is not None and x > PL for x in v) and Fraction(max(v)) <= Fraction(21, 20) * Fraction(min(v)):
                fen4.append((cle, cfg, k0))
chk('C07 gel 5.2 : TN attendu NON JOUE : recouvrements %.3f a %.3f (sous 0.90) ; au TP AUCUNE fenetre de depart k0 >= 4 '
    'ne rend PLATEAU (%d trouvee) sur mes series de la nuit' % (min(ov), max(ov), len(fen4)),
    min(ov) < 0.9 and max(ov) < 0.9 and not fen4 and '0.766 a 0.884' in gel_n, str(fen4))
pas0 = {}
for n, w in (('39_20', '1.95'), ('197_100', '1.97'), ('99_50', '1.98'), ('101_50', '2.02'), ('203_100', '2.03'),
             ('41_20', '2.05')):
    d = json.load(open(os.path.join(ICI, 'manche_m17_v17', 'pt_%s_f070.json' % n)))
    cr = d['EB']['critere_absorbeur']
    pas0[w] = [e for e in cr['essais'] if e['L'] == cr['L_retenu']][0]['pas'][0]
autres = max(v for w, v in pas0.items() if w not in ('2.02', '2.03'))
chk('C08 gel 11 A-3 : le premier pas de descente du run vaut %.3f a 2.02 et %.3f a 2.03, %.3f au plus aux quatre autres '
    '(lu dans les pt_*_f070.json)' % (pas0['2.02'], pas0['2.03'], autres),
    '%.3f' % pas0['2.02'] == '0.090' and '%.3f' % pas0['2.03'] == '0.115' and '%.3f' % autres == '0.026' and
    '0.090 et 0.115 a 2.02 et 2.03, 0.026 au plus aux quatre autres' in gel_n, '')
n_k = len(re.search(r'K_ECH = \[([^\]]*)\]', lire(SONDE).decode()).group(1).split(','))
kech = [int(x) for x in re.search(r'K_ECH = \[([^\]]*)\]', lire(SONDE).decode()).group(1).split(',')]
tp, tn, pl = 4 * n_k, n_k, 30
f1, fo, tr = 12 * n_k, 12 * n_k, 6 * n_k
tmp = 30.1 * 1 + 0  # durees mesurees la nuit du 12/11 : 30.1 s (N = 60), 68.2 s (N = 70)
e1 = 36 * 30.1 + 36 * 68.2 + 18 * 30.1 + 12 * 68.2 + 3 * 30.1
e2 = 324 * 30.1 + 216 * 68.2
chk('C09 gel 3.6, 8 et 12 : K_ECH de la sonde v3 = %s (%d valeurs, ordre de parcours du gel) ; comptes %d + %d + %d = %d '
    'a l etage 1, %d + %d + %d = %d a l etage 2, total %d ; cout recompte sur 30.1 s et 68.2 s : etage 1 %.2f h, etage 2 '
    '%.2f h' % (kech, n_k, tp, tn, pl, tp + tn + pl, f1, fo, tr, f1 + fo + tr, tp + tn + pl + f1 + fo + tr, e1 / 3600,
                e2 / 3600),
    kech == [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 1, 0, -1, -2, -3, -4, -5] and
    (tp, tn, pl, f1, fo, tr) == (72, 18, 30, 216, 216, 108) and tp + tn + pl == 120 and f1 + fo + tr == 540 and
    'k = 3, puis 4 a 12, puis 2, 1, 0, -1, ..., -5' in gel_n and round(1.0 + math.log10(2 ** 17) - 1.0, 1) == 5.1 and
    1.2 < e1 / 3600 < 1.6 and 6.5 < e2 / 3600 < 7.5 and 'etage 1 environ 1 h 30' in gel_n and 'etage 2 environ 7 h' in gel_n,
    '')
somme = Fraction(50, 100) + Fraction(27, 100) + Fraction(13, 100) + Fraction(7, 100) + Fraction(3, 100)
chk('C10 gel 11 : les cinq probabilites de A-1 (0.50, 0.27, 0.13, 0.07, 0.03) somment a %s ; B8 : la fenetre de cinq '
    'contient k = 3 exactement pour -1 <= k0 <= 3 : %s' % (somme, [k0 for k0 in range(-6, 9) if k0 <= 3 <= k0 + 4]),
    somme == 1 and [k0 for k0 in range(-6, 9) if k0 <= 3 <= k0 + 4] == [-1, 0, 1, 2, 3] and
    'QUALIFIE PAR POINT 0.50 ; NON QUALIFIE 0.27 ; ESTIMATEUR QUALIFIE 0.13 ; NON CONCLUANT D\'INSTRUMENT 0.07 ; NON '
    'LISIBLE 0.03' in gel_n, '')
# les canons cites par le gel : chacun doit resoudre chez moi (BOCAL4, registre, entrants)
idx = set()
for racine in (ICI, REG):
    for rep, dirs, fics in os.walk(racine):
        dirs[:] = [d for d in dirs if d not in ('__pycache__', 'reprise', '.git') and not d.startswith('T' + chr(233) + 'l')]
        for f in fics:
            p = os.path.join(rep, f)
            try:
                if os.path.getsize(p) > 30 * 1024 * 1024:
                    continue
                d = lire(p)
            except OSError:
                continue
            try:
                idx.add(eb(d))
            except UnicodeDecodeError:
                pass
            idx.add(hashlib.sha256(d).hexdigest()[:16])
tok = sorted(set(re.findall(r'(?<![0-9a-f])[0-9a-f]{16}(?![0-9a-f])', gel_t)))
absents = [t for t in tok if t not in idx]
chk('C11 gel 2 : les %d empreintes distinctes citees par le gel resolvent TOUTES chez moi (BOCAL4 et registre fe10bfe)' %
    len(tok), not absents, 'non resolues : %s' % (absents or 'aucune'))

# ================================================================ 3. la feuille v2
say('=== 3. LA FEUILLE DE LECTURE v2 ===')
rc, so = courir([LECT, '--selftest'], 'm2_bis_selftest.log')
chk('C12 selftest G-Q7 de la feuille v2 : 14 tenus sur 14 (le cas neuf, plateau au bord fort, en est le quatorzieme)',
    rc == 0 and '14 tenus sur 14' in so, so.strip().splitlines()[-1] if so.strip() else '')
# contre-epreuve : le cas neuf MORD sur ma feuille v1, et sur la v2 AVEC SES BORNES ANCIENNES (mutation)
cas = ("import sys, importlib.util\n"
       "spec = importlib.util.spec_from_file_location('f', sys.argv[1]); F = importlib.util.module_from_spec(spec); "
       "spec.loader.exec_module(F)\n"
       "eta = {k: 0.05 * 2.0 ** (-k) for k in range(-5, 13)}\n"
       "f = {k: (2e-10 if k <= -1 else 2e-10 * eta[k] / eta[-1]) for k in eta}\n"
       "p = F.plateau(f)\nprint('STATUT', p['statut'], p.get('k0'))\n")
open(os.path.join(OUT, 'cas_bord_fort.py'), 'w', encoding='ascii', newline='\n').write(cas)
mut = lire(LECT).decode().replace('K_MIN, K_MAX = -5, 12', 'K_MIN, K_MAX = -2, 12')
assert mut != lire(LECT).decode()
open(os.path.join(OUT, 'feuille_v2_bornes_anciennes.py'), 'w', encoding='ascii', newline='\n').write(mut)
r1 = courir([os.path.join(OUT, 'cas_bord_fort.py'), V2['lecture']], 'm2_bis_cas_v1.log')
r2 = courir([os.path.join(OUT, 'cas_bord_fort.py'), LECT], 'm2_bis_cas_v2.log')
r3 = courir([os.path.join(OUT, 'cas_bord_fort.py'), os.path.join(OUT, 'feuille_v2_bornes_anciennes.py')], 'm2_bis_cas_mut.log')
rs, ss = courir([os.path.join(OUT, 'feuille_v2_bornes_anciennes.py'), '--selftest'], 'm2_bis_selftest_mutee.log')
chk('C13 les dents du cas neuf : sur ma feuille v1 il rend PAS DE PLATEAU, sur la v2 PLATEAU a k0 = -5 ; sur la v2 dont '
    'je remets les bornes a -2 (mutation) il rend PAS DE PLATEAU ET le selftest ne tient plus 14 sur 14',
    'STATUT PAS DE PLATEAU' in r1[1] and 'STATUT PLATEAU -5' in r2[1] and 'STATUT PAS DE PLATEAU' in r3[1] and
    '14 tenus sur 14' not in ss, 'v1 : %s | v2 : %s | mutee : %s | selftest mute : %s' % (
        r1[1].strip(), r2[1].strip(), r3[1].strip(), ss.strip().splitlines()[-1] if ss.strip() else ''))

# les deux refus a l'entree : peuvent-ils refuser a tort ? sur la vraie sortie de la nuit modifiee, jamais recalculee
GBIS = 'dcda1611adf5f8fd'


def lecture_sur(nom, modif, etage=1, extra_files=None):
    d = os.path.join(OUT, 'lect_' + nom)
    os.makedirs(d)
    j = json.load(open(NUIT))
    modif(j)
    json.dump(j, open(os.path.join(d, 'sonde_etage1.json'), 'w'), indent=1, sort_keys=True)
    rc_, so_ = courir([LECT, '--etage', '1', '--sortie', d, '--reference', TABLE], 'm2_bis_lecture_%s.log' % nom)
    return rc_, so_, os.path.exists(os.path.join(d, 'verdict_etage1.json')), d


rc_a, so_a, v_a, _ = lecture_sur('gelv2', lambda j: None)
rc_b, so_b, v_b, d_b = lecture_sur('legitime', lambda j: j.__setitem__('gel', GBIS))
rc_c, so_c, v_c, _ = lecture_sur('galtere', lambda j: (j.__setitem__('gel', GBIS),
                                                      j['TP']['j06'].__setitem__('g', j['TP']['j06']['g'] * 1.0000001)))
rc_d, so_d, v_d, _ = lecture_sur('gelinconnu', lambda j: j.pop('gel'))
chk('C14 refus 1 : la sortie de la NUIT du 12/11 (gel v2) est REFUSEE (code 2), sans verdict ecrit ; une sortie sans champ '
    'gel aussi', rc_a == 2 and 'LECTURE REFUSEE' in so_a and not v_a and rc_d == 2 and 'LECTURE REFUSEE' in so_d and not v_d,
    so_a.strip().splitlines()[-1][:130] if so_a.strip() else '')
chk('C15 refus 2 (O-2) : un g de la sonde qui n est pas celui de la table est refuse (code 2), sans verdict, en nommant le '
    'couplage', rc_c == 2 and 'O-2' in so_c and 'j06' in so_c and not v_c, so_c.strip().splitlines()[-1][:130])
vj = json.load(open(os.path.join(d_b, 'verdict_etage1.json'))) if v_b else {}
chk('C16 PAS DE FAUX REFUS : la meme sortie de la nuit, avec le seul champ gel porte au canon du gel bis (ce que ferait une '
    'sortie de la sonde v3), n est refusee par AUCUN des deux refus : la feuille la juge (code 0, verdict ecrit)',
    rc_b == 0 and v_b and vj.get('etage1') in ('TIENT', 'NE TIENT PAS'), 'verdict %s' % vj.get('etage1'))

# l'essai a blanc, refait par moi : la nuit completee par mon diagnostic a k = -5, -4, -3, jugee par la feuille v2
def etendre(j):
    j['gel'] = GBIS
    for cle in ('j06', 'j08'):
        jj = S1['TP'][cle]['j']
        for g in ('G20', 'G30'):
            tr_ = j['TP'][cle]['traj']['F1' + g]
            for k in (-3, -4, -5):
                d = DIAG[(jj, g, k)]
                tr_[str(k)] = {'k': k, 'eta': 0.05 * 2.0 ** (-k), 'saute': False, 'etats': [
                    {'suivi': True, 'ov': d['recouvrement'], 'E_re': d['E_re'], 'E_im': d['E_im'], 'gamma': d['gamma']}]}


rc_e, so_e, v_e, d_e = lecture_sur('etendu', etendre)
ve = json.load(open(os.path.join(d_e, 'verdict_etage1.json'))) if v_e else {}
ses = open(os.path.join(LOT, 'essai_feuille_v2_series_etendues_machine1_v1.log'), encoding='ascii').read()
lignes_tp = [l for l in so_e.splitlines() if l.startswith('TP j')]
chk('C17 ESSAI A BLANC refait par moi (non opposable : la nuit + mes douze largeurs, la feuille v2) : etage 1 TIENT, les quatre '
    'lignes TP tiennent, TN NON JOUE sans motif ; et il retombe sur celui de machine 1 (memes Gamma_pl a quatre chiffres)',
    rc_e == 0 and ve.get('etage1') == 'TIENT' and len(lignes_tp) == 4 and all(l.endswith('TIENT') for l in lignes_tp) and
    all(re.search(r'Gamma_pl (\S+)', l).group(1) in ses for l in lignes_tp) and 'TN : NON JOUE' in so_e,
    ' | '.join(l[:70] for l in lignes_tp))
# etage 2 : le refus d'un etage 2 d'un autre gel (apres le pre-vol, plus bas)

# ================================================================ 4. le pre-vol de l'etage 1 sous la sonde v3
say('=== 4. PRE-VOL DE L ETAGE 1 SOUS LA SONDE v3 (NON OPPOSABLE) ===')
PV = os.path.join(OUT, 'pv3')
RET = os.path.join(LOT, 'prevol_bis', 'tp_retenus_prevol.json')
REFP = os.path.join(LOT, 'prevol_bis', 'tp_reference_prevol.json')
rc, so = courir(sonde_args(PV, 1, ['--retenus', RET, '--prevol']), 'm2_bis_prevol_etage1_passage1.log')
s1a = json.load(open(os.path.join(PV, 'sonde_etage1.json')))
shutil.copy(os.path.join(PV, 'sonde_etage1.json'), os.path.join(OUT, 'sonde_etage1_passage1.json'))
nj = nid = 0
for d, _, fs in os.walk(os.path.join(PV, 'reprise')):
    for f in fs:
        if f.endswith('.json'):
            nj += 1
            nid += 1 if 'identite_reprise' in json.load(open(os.path.join(d, f))) else 0
c = s1a['comptes']
chk('C18 pre-vol etage 1, premier passage : G-Q3 six sur six ; TN 18, TP 36 (un couplage : 2 x 18), plancher 30 TOUS JOUES ; '
    'G-Q10 ; %d fichiers de reprise, %d portent une identite' % (nj, nid),
    rc == 0 and all(s1a['GQ3'].values()) and c['TN']['joues'] == 18 and c['TP']['joues'] == 36 and
    c['plancher']['joues'] == 30 and s1a['GQ10'] and nj == 84 and nid == nj and s1a['gel'] == GBIS, 'comptes %s' % c)
ks_ = sorted(int(k) for k in s1a['TP']['j08']['traj']['F1G20'])
chk('C19 les trajectoires du pre-vol portent les DIX-HUIT barreaux (k = %d a %d), eta_k * 2^k == eta0 exact a chacun (G-Q6 '
    'ne s est pas declenchee)' % (ks_[0], ks_[-1]),
    ks_ == list(range(-5, 13)) and all(abs(s1a['TP']['j08']['traj']['F1G20'][str(k)]['eta'] * 2.0 ** k - 0.05) < 1e-17
                                       for k in ks_), '')
rc, so = courir(sonde_args(PV, 1, ['--retenus', RET, '--prevol']), 'm2_bis_prevol_etage1_passage2.log')
s1b = json.load(open(os.path.join(PV, 'sonde_etage1.json')))
cb2 = s1b['comptes']
mem = all(json.dumps(s1a[k], sort_keys=True) == json.dumps(s1b[k], sort_keys=True) for k in ('TP', 'TN', 'GQ5', 'GQ3'))
chk('C20 second passage dans le MEME dossier : 0 joue + 84 repris == 84, mmes trajectoires', rc == 0 and
    sum(v['joues'] for v in cb2.values()) == 0 and sum(v['repris'] for v in cb2.values()) == 84 and s1b['GQ10'] and mem,
    'comptes %s ; trajectoires identiques : %s' % (cb2, mem))
rc, so = courir([LECT, '--etage', '1', '--sortie', PV, '--reference', REFP], 'm2_bis_prevol_etage1_lecture.log')
mien = [arrondi(l) for l in lire(os.path.join(PV, 'lecture_etage1.log')).decode().splitlines() if 'canon' not in l]
sien = [arrondi(l) for l in lire(os.path.join(LOT, 'prevol_bis', 'lecture_etage1.log')).decode().splitlines()
        if 'canon' not in l]
chk('C21 lecture de l etage 1 sur MA sortie de pre-vol == celle de machine 1 (hors canon ; nombres a 3 chiffres)',
    rc == 0 and mien == sien, '%d lignes' % len(mien))
shutil.copy(os.path.join(PV, 'verdict_etage1.json'), os.path.join(PV, 'verdict_etage1_reel.json'))

# ================================================================ 5. le pre-vol de l'etage 2
say('=== 5. PRE-VOL DE L ETAGE 2 SOUS VERDICT FACTICE DE MON CANON (NON OPPOSABLE) ===')
json.dump({'canon_sonde_etage1': eb(lire(os.path.join(PV, 'sonde_etage1.json'))), 'etage1': 'TIENT',
           'factice': True, 'note': 'verdict FACTICE (m2)', 'prevol': True},
          open(os.path.join(PV, 'verdict_etage1.json'), 'w'), sort_keys=True)
rc, so = courir(sonde_args(PV, 2, ['--verdict1', os.path.join(PV, 'verdict_etage1.json'), '--prevol']),
                'm2_bis_prevol_etage2_sonde.log')
s2 = json.load(open(os.path.join(PV, 'sonde_etage2.json')))
c = s2['comptes']
perdus = tot = 0
idmin = 9.0
for n, p in s2['points'].items():
    for cfg, cc in p['cfg'].items():
        idmin = min(idmin, cc['identite'])
        for rec in cc['traj'].values():
            for e in rec['etats']:
                tot += 1
                perdus += 0 if e['suivi'] else 1
s2m1 = json.load(open(os.path.join(LOT, 'prevol_bis', 'sonde_etage2.json')))
tot1 = sum(len(rec['etats']) for p in s2m1['points'].values() for cc in p['cfg'].values() for rec in cc['traj'].values())
chk('C22 pre-vol etage 2 : F1 210 + 6 repris == 216, formes 216, translation 108, ouverture 6 ; %d etats-pas (machine 1 : '
    '%d), %d perdus ; identite min %.4f' % (tot, tot1, perdus, idmin),
    rc == 0 and c['F1'] == {'joues': 210, 'repris': 6, 'sautes': 0} and sum(c['formes'].values()) == 216 and
    sum(c['translation'].values()) == 108 and c['ouverture']['joues'] == 6 and tot == tot1 and perdus == 0 and
    idmin > 0.999 and s2['GQ10'] and s2['gel'] == GBIS, 'comptes %s' % c)
rc, so = courir([LECT, '--etage', '2', '--sortie', PV], 'm2_bis_prevol_etage2_lecture.log')
mien = [l for l in lire(os.path.join(PV, 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
sien = [l for l in lire(os.path.join(LOT, 'prevol_bis', 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
chk('C23 lecture de l etage 2 sur MA sortie de pre-vol IDENTIQUE a celle de machine 1', rc == 0 and mien == sien,
    '%d lignes' % len(mien))
# refus de la feuille a l'etage 2 : une sortie d'etage 2 d'un autre gel
D2 = os.path.join(OUT, 'lect_etage2_autre_gel')
shutil.copytree(PV, D2, ignore=shutil.ignore_patterns('reprise'))
j2 = json.load(open(os.path.join(D2, 'sonde_etage2.json')))
j2['gel'] = 'cde0cd11a763f26d'
json.dump(j2, open(os.path.join(D2, 'sonde_etage2.json'), 'w'), sort_keys=True)
if os.path.exists(os.path.join(D2, 'verdict_qualification_EB.json')):
    os.remove(os.path.join(D2, 'verdict_qualification_EB.json'))
rc, so = courir([LECT, '--etage', '2', '--sortie', D2], 'm2_bis_lecture_etage2_autre_gel.log')
chk('C24 refus a l etage 2 : une sortie d etage 2 qui porte le gel v2 est REFUSEE (code 2), sans verdict de qualification '
    'ecrit', rc == 2 and 'LECTURE REFUSEE' in so and not os.path.exists(os.path.join(D2, 'verdict_qualification_EB.json')),
    so.strip().splitlines()[-1][:130] if so.strip() else '')

# ================================================================ 6. le banc v3
say('=== 6. LE BANC QUI TUE v3, TEL QUE LIVRE ===')
rc, so = courir([BANC, '--lecture', LECT, '--sonde', SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF,
                 '--prevol', PV, '--retenus', RET, '--sortie', os.path.join(OUT, 'banc_v3')], 'm2_bis_banc.log')
dern = so.strip().splitlines()[-1] if so.strip() else ''
chk('C25 le banc v3 TEL QUE LIVRE (feuille v2, sonde v3) rend 6 mordues sur 6, base saine, 4 refus sur 4 sur ce poste',
    rc == 0 and '6 mordues == 6 attendues' in dern and '4 refus == 4' in dern and 'PASSE' in dern, dern)

# ================================================================ 7. D-1 : l'identite de reprise, attaquee sous la v3
say('=== 7. D-1 : L IDENTITE DE REPRISE, ATTAQUEE SOUS LA v3 ===')


def attaque(nom, modif):
    d = os.path.join(OUT, 'attaque_' + nom)
    os.makedirs(os.path.join(d, 'reprise'))
    shutil.copytree(os.path.join(PV, 'reprise', 'TP_j08_F1G20'), os.path.join(d, 'reprise', 'TP_j08_F1G20'))
    fj = os.path.join(d, 'reprise', 'TP_j08_F1G20', 'k_+03.json')
    j = json.load(open(fj))
    modif(j)
    json.dump(j, open(fj, 'w'), sort_keys=True)
    rc_, so_ = courir(sonde_args(d, 1, ['--retenus', RET, '--prevol']), 'm2_bis_attaque_%s.log' % nom)
    arr = [l for l in so_.splitlines() if l.startswith('ARRET')]
    return rc_, (arr[0] if arr else ''), 'G-Q10' in so_


rc_a, arr_a, gq_a = attaque('legacy', lambda j: j.pop('identite_reprise'))
rc_b, arr_b, gq_b = attaque('g', lambda j: j['identite_reprise'].__setitem__('g', j['identite_reprise']['g'] * 1.001))
rc_c, arr_c, gq_c = attaque('gelv2', lambda j: j['identite_reprise'].__setitem__('gel', 'cde0cd11a763f26d'))
rc_d, arr_d, gq_d = attaque('sondev2', lambda j: j['identite_reprise'].__setitem__('sonde', 'facc7536ba4637cb'))
chk('C26 D-1 sous la v3 : une reprise au format v1 (sans identite) est refusee ; une reprise dont l identite porte un g '
    'different, le GEL v2, ou la SONDE v2 est refusee (code 2) en nommant la cle en ecart',
    rc_a == 2 and 'reprise refusee (D-1)' in arr_a and not gq_a and rc_b == 2 and "['g']" in arr_b and rc_c == 2 and
    "['gel']" in arr_c and rc_d == 2 and "['sonde']" in arr_d,
    "g : ...%s ; gel : ...%s ; sonde : ...%s" % (arr_b[-14:], arr_c[-16:], arr_d[-18:]))
# le cas decisif : le DOSSIER REEL de la nuit du 12/11 (gel v2, sonde v2) presente a la sonde v3 en etage 1 REEL
CT = os.path.join(OUT, 'nuit_du_12_11_sous_v3')
os.makedirs(CT)
shutil.copytree(os.path.join(ICI, 'nuit_EB', 'sortie', 'reprise'), os.path.join(CT, 'reprise'))
rc, so = courir(sonde_args(CT, 1, ['--retenus', RETENUS]), 'm2_bis_nuit_12_11_sous_v3.log')
gq3 = re.findall(r'G-Q3 (\S+)\s+N = (\d+) : (\w+)', so)
arr = [l for l in so.splitlines() if l.startswith('ARRET')]
chk('C27 le DOSSIER REEL de la nuit du 12/11, presente a la sonde v3 en etage 1 reel, est REFUSE au premier fichier repris '
    '(code 2, cles en ecart gel et sonde), apres G-Q3 a taille reelle six sur six, sans G-Q10 ni sonde_etage1.json',
    rc == 2 and [(a, int(b), c3) for a, b, c3 in gq3] == [('39_20', 60, 'OK'), ('197_100', 60, 'OK'), ('99_50', 60, 'OK'),
                                                          ('101_50', 61, 'OK'), ('203_100', 61, 'OK'), ('41_20', 61, 'OK')]
    and len(arr) == 1 and 'reprise refusee (D-1)' in arr[0] and "'gel'" in arr[0] and "'sonde'" in arr[0] and
    'G-Q10' not in so and not os.path.exists(os.path.join(CT, 'sonde_etage1.json')), arr[0][-90:] if arr else so[-200:])

# ================================================================ 8. D-2 : la porte, sept cas
say('=== 8. D-2 : LA PORTE DE L ETAGE 2, SEPT CAS, PAR SENTINELLE (AUCUN CALCUL) ===')
with open(os.path.join(OUT, 'd2_portes_v3.py'), 'w', encoding='ascii', newline='\n') as fh:
    fh.write('''# Portes de l'etage 2 SANS calcul : etage2 est remplace par une sentinelle. Sept cas.
import sys, os, json, shutil, hashlib, unicodedata, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN, MANIF, SRC, BASE = sys.argv[1:7]
def canon(raw):
    return hashlib.sha256(unicodedata.normalize("NFC", raw.decode()).replace("\\r\\n", "\\n").encode()).hexdigest()[:16]
CAS = [("1 reel / verdict pre-vol / etage1 pre-vol (D-2 d'origine)", False, True, True, None, False, False, "FERMEE"),
       ("2 reel / verdict reel / etage1 pre-vol (croise)", False, False, True, None, False, False, "FERMEE"),
       ("3 pre-vol / verdict reel / etage1 reel (inverse)", True, False, False, None, False, False, "FERMEE"),
       ("4 TOUT REEL (le chemin legitime de la nuit)", False, False, False, None, False, False, "OUVERTE"),
       ("5 TOUT PRE-VOL, verdict factice (le chemin legitime du pre-vol)", True, True, True, None, True, False, "OUVERTE"),
       ("6 etage 1 MUTE (M-4) sous verdict pre-vol", True, True, True, "M-4", True, False, "FERMEE"),
       ("7 sonde_etage1.json ABSENT", True, True, True, None, True, True, "FERMEE")]
for i, (nom, cmd_pv, v_pv, s_pv, mut, fact, absent, attendu) in enumerate(CAS):
    d = os.path.join(BASE, "porte_%d" % (i + 1)); shutil.rmtree(d, ignore_errors=True); os.makedirs(d)
    spec = importlib.util.spec_from_file_location("sonde_qeb_%d" % i, SONDE)
    S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    def sentinelle(*a, **k): raise RuntimeError("OUVERTE")
    S.etage2 = sentinelle
    j = json.load(open(SRC)); j["prevol"] = s_pv; j["mutation"] = mut
    if not absent:
        json.dump(j, open(os.path.join(d, "sonde_etage1.json"), "w"), indent=1, sort_keys=True)
    c = canon(open(os.path.join(d, "sonde_etage1.json"), "rb").read()) if not absent else "0" * 16
    v = {"canon_sonde_etage1": c, "etage1": "TIENT", "prevol": v_pv}
    if fact: v["factice"] = True
    json.dump(v, open(os.path.join(d, "v.json"), "w"))
    argv = ["sonde", "--moteur", MOTEUR, "--run", RUN, "--manifeste", MANIF, "--sortie", d, "--etage", "2",
            "--verdict1", os.path.join(d, "v.json")] + (["--prevol"] if cmd_pv else [])
    sys.argv = argv
    out = None
    try:
        S.main()
        out = "TERMINEE SANS SENTINELLE"
    except RuntimeError as e:
        out = str(e)
    except SystemExit as e:
        out = "FERMEE"
    except Exception as e:
        out = "EXCEPTION %s" % type(e).__name__
    print("PORTE %s : %s (attendu %s) : %s" % (nom, out, attendu, "OK" if out == attendu else "MORD"), flush=True)
''')
rc, so = courir([os.path.join(OUT, 'd2_portes_v3.py'), SONDE, MOTEUR, RUN, MANIF,
                 os.path.join(PV, 'sonde_etage1.json'), OUT], 'm2_bis_D2_portes.log')
lp = [l for l in so.splitlines() if l.startswith('PORTE ')]
chk('C28 D-2 sous la v3 : sur sept cas, la porte de l etage 2 se FERME aux cinq cas interdits et reste OUVERTE aux deux '
    'chemins legitimes (tout reel, tout pre-vol)', rc == 0 and len(lp) == 7 and all(l.endswith(': OK') for l in lp),
    '%d cas, %d OK' % (len(lp), sum(1 for l in lp if l.endswith(': OK'))))

# ================================================================ bilan
nchk = len(CHK)
noms = [n.split()[0] for n, ok, _ in CHK if not ok]
say('=== BILAN : %d controles, %d mordent ===' % (nchk, len(noms)))
for n, ok, d in CHK:
    if not ok:
        say('  MORD : ' + n[:120])
with open(os.path.join(OUT, 'audit_gel_EB_bis_machine2_v1.log'), 'w', encoding='ascii', errors='replace',
          newline='\n') as fh:
    fh.write('\n'.join(LOG) + '\n')
with open(os.path.join(OUT, 'audit_gel_EB_bis_machine2_v1.json'), 'w', encoding='ascii', newline='\n') as fh:
    json.dump({'bilan': {'chk': nchk, 'mord': len(noms), 'noms': noms},
               'controles': [{'nom': n, 'ok': ok, 'detail': d} for n, ok, d in CHK], 'consignes': CONS},
              fh, indent=1, ensure_ascii=True)
