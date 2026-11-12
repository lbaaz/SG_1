# -*- coding: ascii -*-
"""AUDIT machine 2 de la SONDE v2 et du BANC QUI TUE v2 de qualification E-B (machine 1, 2026-11-11),
reponse a ma certification du v1 (lot 123880c93b810d35). Classe B.

E19 : AUCUN RUN DE L'ETAGE 1 NI 2 JOUE. Calcule ici, et declare : les pre-vols (geometrie reduite,
NON OPPOSABLES), le banc, les portes de l'etage 2 par sentinelle (sans calcul), G-Q3 a taille reelle
(matrices seulement, dans un etage 1 reel qui doit REFUSER au premier fichier repris), et UNE
decomposition (F1, G20, k = 3) au point 1.95 pour l'ancrage -- seul gamma de l'etat d'ancrage imprime.

Usage : python audit_sonde_EB_v2_machine2_v1.py LOT_V2 LOT_V1 MOTEUR DOSSIER_RUN MANIFESTE_RUN SORTIE_DIR
  LOT_V2 = lot de machine 1 (sonde v2) EXTRAIT dans un dossier neuf ; LOT_V1 = le lot v1 EXTRAIT (mes
  bases certifiees) ; SORTIE_DIR = dossier NEUF. Tous les chemins sont des ARGUMENTS ; les scripts de
  machine 1 sont lances par 'python -P' depuis SORTIE_DIR."""
import collections
import difflib
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata

sys.dont_write_bytecode = True
if len(sys.argv) != 7:
    print(__doc__)
    sys.exit(2)
LOT2, LOT1, MOTEUR, RUN, MANIF, OUT = [os.path.abspath(x) for x in sys.argv[1:7]]
if os.path.exists(OUT) and os.listdir(OUT):
    sys.exit('SORTIE_DIR doit etre un dossier neuf et vide : %s' % OUT)
os.makedirs(OUT, exist_ok=True)
PY = [sys.executable, '-P']
SONDE = os.path.join(LOT2, 'sonde_qualification_EB_machine1_v2.py')
BANC = os.path.join(LOT2, 'banc_qui_tue_qualification_EB_machine1_v2.py')
LECT = os.path.join(LOT2, 'lecture_qualification_EB_machine1_v1.py')
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


def courir(args, nom_log, cwd=OUT, timeout=1500):
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


# ---------------------------------------------------------------- 1. le lot et la reconstruction
say('=== 1. LE LOT ENTRANT ET LA RECONSTRUCTION ===')
man = lire(os.path.join(LOT2, 'MANIFEST_lot_machine1_sonde_EB_v2_v1.txt'))
CONS['canon_lot_v2'] = eb(man)
pieces = [l.split() for l in man.decode('utf-8').splitlines()
          if not l.startswith('#') and len(l.split()) == 5 and len(l.split()[0]) == 16]
mal = []
for e, br, ob, obr, nom in pieces:
    r = lire(os.path.join(LOT2, nom))
    try:
        ok = eb(r) == e
    except UnicodeDecodeError:
        ok = hashlib.sha256(r).hexdigest()[:16] == e
    if not ok or hashlib.sha256(r).hexdigest()[:16] != br or len(r) != int(obr):
        mal.append(nom)
chk('C01 lot v2 : %d pieces au canon B, a l empreinte brute et a la taille (canon du lot %s)' %
    (len(pieces), CONS['canon_lot_v2']), len(pieces) == 25 and not mal, 'ecarts : %s' % (mal or 'aucun'))
v1s = os.path.join(LOT1, 'sonde_qualification_EB_machine1_v1.py')
v1b = os.path.join(LOT1, 'banc_qui_tue_qualification_EB_machine1_v1.py')
cs, cb, cl = eb(lire(SONDE)), eb(lire(BANC)), eb(lire(LECT))
CONS['canons'] = {'sonde_v2': cs, 'banc_v2': cb, 'lecture_v1': cl}
brutes = [lire(SONDE), lire(BANC)]
chk('C02 les bases v1 du lot sont MES exemplaires certifies (sonde 214ea376cbf540a4, banc 666e69f11bc1f72c) ; '
    'la feuille de lecture est INCHANGEE (b3ac958a1a2b915b) ; les deux v2 sont ASCII, LF seul, et citent le gel v2',
    eb(lire(os.path.join(LOT2, 'sonde_qualification_EB_machine1_v1.py'))) == eb(lire(v1s)) == '214ea376cbf540a4' and
    eb(lire(os.path.join(LOT2, 'banc_qui_tue_qualification_EB_machine1_v1.py'))) == eb(lire(v1b)) == '666e69f11bc1f72c'
    and cl == 'b3ac958a1a2b915b' and all(all(b < 128 for b in r) and b'\r' not in r and b'cde0cd11a763f26d' in r
                                         for r in brutes),
    'sonde v2 %s, banc v2 %s' % (cs, cb))
neutre = os.path.join(OUT, 'reconstruction')
os.makedirs(neutre)
rs = os.path.join(neutre, 'sonde_v2.py')
rb = os.path.join(neutre, 'banc_v2.py')
r = subprocess.run(PY + [os.path.join(LOT2, 'construction_sonde_banc_v2_machine1_v1.py'), v1s, rs, v1b, rb],
                   cwd=neutre, capture_output=True, text=True, timeout=120)
with open(os.path.join(OUT, 'm2_reconstruction.log'), 'w', encoding='ascii', errors='replace', newline='\n') as fh:
    fh.write(r.stdout + r.stderr)
chk('C03 la construction de machine 1, lue puis rejouee depuis MES v1, rend une sonde v2 et un banc v2 '
    'IDENTIQUES AU BIT a ceux livres', r.returncode == 0 and os.path.isfile(rs) and os.path.isfile(rb) and
    lire(rs) == lire(SONDE) and lire(rb) == lire(BANC), 'sonde %s, banc %s ; %d remplacements annonces' % (
        'identique' if os.path.isfile(rs) and lire(rs) == lire(SONDE) else 'DIFFERENTE',
        'identique' if os.path.isfile(rb) and lire(rb) == lire(BANC) else 'DIFFERENT', r.stdout.count('applique')))


def lignes_changees(a, b):
    """Lignes ajoutees/retirees de MON diff, sans les lignes vides (difflib et diff -u n'alignent pas les
    lignes vides de la meme facon : un artefact d'alignement, pas un ecart)."""
    return [l for l in difflib.unified_diff(a.decode().splitlines(), b.decode().splitlines(), lineterm='', n=0)
            if l[:1] in '+-' and l[:3] not in ('+++', '---') and l[1:].strip()]


def lignes_diff(p):
    return [l for l in lire(p).decode().splitlines()
            if l[:1] in '+-' and l[:3] not in ('+++', '---') and l[1:].strip()]


def reconstruit(v1, v2, lignes):
    """Critere decisif : v1 - lignes retirees + lignes ajoutees == v2, en multi-ensemble de lignes non vides."""
    c = collections.Counter(l for l in v1.decode().splitlines() if l.strip())
    for l in lignes:
        c[l[1:]] += -1 if l[0] == '-' else 1
    return +c == collections.Counter(l for l in v2.decode().splitlines() if l.strip()) and min(c.values()) >= 0


ds = collections.Counter(lignes_changees(lire(v1s), lire(SONDE))) == collections.Counter(
    lignes_diff(os.path.join(LOT2, 'diff_sonde_EB_v1_v2.txt')))
db = collections.Counter(lignes_changees(lire(v1b), lire(BANC))) == collections.Counter(
    lignes_diff(os.path.join(LOT2, 'diff_banc_EB_v1_v2.txt')))
rs_ = reconstruit(lire(v1s), lire(SONDE), lignes_diff(os.path.join(LOT2, 'diff_sonde_EB_v1_v2.txt')))
rb_ = reconstruit(lire(v1b), lire(BANC), lignes_diff(os.path.join(LOT2, 'diff_banc_EB_v1_v2.txt')))
chk('C04 les diffs joints sont exacts : memes lignes ajoutees et retirees que les miennes (hors lignes vides, que '
    'difflib et diff -u n alignent pas pareil), et chacun reconstruit son v2 depuis son v1', ds and db and rs_ and rb_,
    'sonde : memes lignes %s, reconstruit %s ; banc : memes lignes %s, reconstruit %s ; sonde +%d -%d' % (
        ds, rs_, db, rb_, sum(1 for l in lignes_changees(lire(v1s), lire(SONDE)) if l[0] == '+'),
        sum(1 for l in lignes_changees(lire(v1s), lire(SONDE)) if l[0] == '-')))

# ---------------------------------------------------------------- 2. selftest, etage 1 en deux passages
say('=== 2. SELFTEST ET PRE-VOL DE L ETAGE 1 SOUS LA SONDE v2 (NON OPPOSABLE) ===')
rc, so = courir([LECT, '--selftest'], 'm2_selftest_v2.log')
chk('C05 selftest G-Q7 : 13 tenus sur 13', rc == 0 and '13 tenus sur 13' in so)
PV = os.path.join(OUT, 'pv2')
RET = os.path.join(LOT2, 'prevol_v2', 'tp_retenus_prevol.json')
REFP = os.path.join(LOT2, 'prevol_v2', 'tp_reference_prevol.json')
rc, so = courir(sonde_args(PV, 1, ['--retenus', RET, '--prevol']), 'm2_v2_prevol_etage1_passage1.log')
s1a = json.load(open(os.path.join(PV, 'sonde_etage1.json')))
shutil.copy(os.path.join(PV, 'sonde_etage1.json'), os.path.join(OUT, 'sonde_etage1_passage1.json'))
nj = nid = 0
for d, _, fs in os.walk(os.path.join(PV, 'reprise')):
    for f in fs:
        if f.endswith('.json'):
            nj += 1
            nid += 1 if 'identite_reprise' in json.load(open(os.path.join(d, f))) else 0
c = s1a['comptes']
chk('C06 pre-vol etage 1, premier passage : G-Q3 six sur six ; TN 15, TP 30, plancher 30 TOUS JOUES ; G-Q10 ; '
    '%d fichiers de reprise, %d portent une identite' % (nj, nid),
    rc == 0 and all(s1a['GQ3'].values()) and c['TN']['joues'] == 15 and c['TP']['joues'] == 30 and
    c['plancher']['joues'] == 30 and s1a['GQ10'] and nj == 75 and nid == nj, 'comptes %s' % c)
rc, so = courir(sonde_args(PV, 1, ['--retenus', RET, '--prevol']), 'm2_v2_prevol_etage1_passage2.log')
s1b = json.load(open(os.path.join(PV, 'sonde_etage1.json')))
cb2 = s1b['comptes']
mem = all(json.dumps(s1a[k], sort_keys=True) == json.dumps(s1b[k], sort_keys=True) for k in ('TP', 'TN', 'GQ5', 'GQ3'))
chk('C07 second passage dans le MEME dossier : 0 joue + 75 repris == 75 (la reprise sous identite laisse passer le '
    'meme calcul), et ses trajectoires sont celles du premier passage', rc == 0 and
    sum(v['joues'] for v in cb2.values()) == 0 and sum(v['repris'] for v in cb2.values()) == 75 and s1b['GQ10'] and mem,
    'comptes %s ; trajectoires identiques : %s' % (cb2, mem))
rc, so = courir([LECT, '--etage', '1', '--sortie', PV, '--reference', REFP], 'm2_v2_prevol_etage1_lecture.log')
mien = [arrondi(l) for l in lire(os.path.join(PV, 'lecture_etage1.log')).decode().splitlines() if 'canon' not in l]
sien = [arrondi(l) for l in lire(os.path.join(LOT2, 'prevol_v2', 'lecture_etage1.log')).decode().splitlines()
        if 'canon' not in l]
chk('C08 lecture de l etage 1 sur la sortie v2 == celle de machine 1 (hors canon ; nombres a 3 chiffres)',
    rc == 0 and mien == sien, '%d lignes' % len(mien))
shutil.copy(os.path.join(PV, 'verdict_etage1.json'), os.path.join(PV, 'verdict_etage1_reel.json'))

# ---------------------------------------------------------------- 3. etage 2 en pre-vol
say('=== 3. PRE-VOL DE L ETAGE 2 SOUS VERDICT FACTICE DE MON CANON (NON OPPOSABLE) ===')
json.dump({'canon_sonde_etage1': eb(lire(os.path.join(PV, 'sonde_etage1.json'))), 'etage1': 'TIENT',
           'factice': True, 'note': 'verdict FACTICE (m2)', 'prevol': True},
          open(os.path.join(PV, 'verdict_etage1.json'), 'w'), sort_keys=True)
rc, so = courir(sonde_args(PV, 2, ['--verdict1', os.path.join(PV, 'verdict_etage1.json'), '--prevol']),
                'm2_v2_prevol_etage2_sonde.log')
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
chk('C09 pre-vol etage 2 : F1 174 + 6 repris == 180, formes 180, translation 90, ouverture 6 ; %d etats-pas, %d '
    'perdus ; identite min %.4f (la reprise ouverture -> F1 passe sous identite)' % (tot, perdus, idmin),
    rc == 0 and c['F1'] == {'joues': 174, 'repris': 6, 'sautes': 0} and sum(c['formes'].values()) == 180 and
    sum(c['translation'].values()) == 90 and c['ouverture']['joues'] == 6 and tot == 1260 and perdus == 0 and
    idmin > 0.999 and s2['GQ10'], 'comptes %s' % c)
rc, so = courir([LECT, '--etage', '2', '--sortie', PV], 'm2_v2_prevol_etage2_lecture.log')
mien = [l for l in lire(os.path.join(PV, 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
sien = [l for l in lire(os.path.join(LOT2, 'prevol_v2', 'lecture_etage2.log')).decode().splitlines()
        if 'canon' not in l]
sien1 = [l for l in lire(os.path.join(LOT1, 'prevol', 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
chk('C10 lecture de l etage 2 sur la sortie v2 IDENTIQUE a celle de machine 1 sous v2, ET a celle du v1',
    rc == 0 and mien == sien == sien1, '%d lignes' % len(mien))

# ---------------------------------------------------------------- 4. le banc v2
say('=== 4. LE BANC QUI TUE v2, TEL QUE LIVRE ===')
rc, so = courir([BANC, '--lecture', LECT, '--sonde', SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF,
                 '--prevol', PV, '--retenus', RET, '--sortie', os.path.join(OUT, 'banc_v2')], 'm2_v2_banc.log')
dern = so.strip().splitlines()[-1] if so.strip() else ''
chk('C11 D-3 levee : le banc v2 TEL QUE LIVRE rend 6 mordues sur 6, base saine, 4 refus sur 4 sur ce poste',
    rc == 0 and '6 mordues == 6 attendues' in dern and '4 refus == 4' in dern and 'PASSE' in dern, dern)

# ---------------------------------------------------------------- 5. D-1 : l'identite de reprise, attaquee
say('=== 5. D-1 : L IDENTITE DE REPRISE, ATTAQUEE (CAS QUE LE BANC NE JOUE PAS) ===')


def attaque(nom, modif):
    d = os.path.join(OUT, 'attaque_' + nom)
    os.makedirs(os.path.join(d, 'reprise'))
    shutil.copytree(os.path.join(PV, 'reprise', 'TP_j08_F1G20'), os.path.join(d, 'reprise', 'TP_j08_F1G20'))
    fj = os.path.join(d, 'reprise', 'TP_j08_F1G20', 'k_+03.json')
    j = json.load(open(fj))
    modif(j)
    json.dump(j, open(fj, 'w'), sort_keys=True)
    rc_, so_ = courir(sonde_args(d, 1, ['--retenus', RET, '--prevol']), 'm2_v2_attaque_%s.log' % nom)
    arr = [l for l in so_.splitlines() if l.startswith('ARRET')]
    return rc_, (arr[0] if arr else ''), 'G-Q10' in so_


rc_a, arr_a, gq_a = attaque('legacy', lambda j: j.pop('identite_reprise'))
rc_b, arr_b, gq_b = attaque('g', lambda j: j['identite_reprise'].__setitem__('g', j['identite_reprise']['g'] * 1.001))
rc_c, arr_c, gq_c = attaque('sonde', lambda j: j['identite_reprise'].__setitem__('sonde', '0123456789abcdef'))
rc_d, arr_d, gq_d = attaque('eta0', lambda j: j['identite_reprise'].__setitem__('eta0', j['identite_reprise']['eta0'] * 2.0))
CONS['D1_attaques'] = {'legacy': arr_a[:200], 'g': arr_b[-60:], 'sonde': arr_c[-60:], 'eta0': arr_d[-60:]}
chk('C12 D-1 levee : une reprise AU FORMAT v1 (sans identite) est REFUSEE (code 2), sans decomposer',
    rc_a == 2 and 'reprise refusee (D-1)' in arr_a and not gq_a, arr_a[-120:])
chk('C13 D-1 levee : une reprise dont l identite porte un g, un canon de sonde ou un eta0 DIFFERENT est refusee '
    'en nommant la cle en ecart', rc_b == 2 and "['g']" in arr_b and rc_c == 2 and "['sonde']" in arr_c and
    rc_d == 2 and "['eta0']" in arr_d, "g : ...%s ; sonde : ...%s ; eta0 : ...%s" % (arr_b[-14:], arr_c[-14:], arr_d[-14:]))
CT = os.path.join(OUT, 'pv_contamine')
os.makedirs(CT)
shutil.copytree(os.path.join(PV, 'reprise'), os.path.join(CT, 'reprise'))
rc, so = courir(sonde_args(CT, 1, ['--retenus', RET]), 'm2_v2_D1_etage1_reel_dans_reprise_prevol.log')
gq3 = re.findall(r'G-Q3 (\S+)\s+N = (\d+) : (\w+)', so)
arr = [l for l in so.splitlines() if l.startswith('ARRET')]
chk('C14 D-1 levee, ma demonstration du v1 REJOUEE : un etage 1 REEL dans une reprise de pre-vol s arrete au '
    'premier fichier (code 2), apres G-Q3 a taille reelle six sur six (N = 60, 60, 60, 61, 61, 61, matrices seulement), '
    'sans aucun G-Q10 ni sonde_etage1.json ecrit',
    rc == 2 and [(a, int(b), c3) for a, b, c3 in gq3] == [('39_20', 60, 'OK'), ('197_100', 60, 'OK'),
                                                          ('99_50', 60, 'OK'), ('101_50', 61, 'OK'),
                                                          ('203_100', 61, 'OK'), ('41_20', 61, 'OK')] and
    len(arr) == 1 and 'reprise refusee (D-1)' in arr[0] and 'G-Q10' not in so and
    not os.path.exists(os.path.join(CT, 'sonde_etage1.json')), arr[0][-80:] if arr else so[-200:])

# ---------------------------------------------------------------- 6. D-2 : la porte, sept cas
say('=== 6. D-2 : LA PORTE DE L ETAGE 2, SEPT CAS, PAR SENTINELLE (AUCUN CALCUL) ===')
with open(os.path.join(OUT, 'd2_portes_v2.py'), 'w', encoding='ascii', newline='\n') as fh:
    fh.write('''# Portes de l'etage 2 SANS calcul : etage2 est remplace par une sentinelle. Sept cas.
import sys, os, json, shutil, hashlib, unicodedata, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN, MANIF, SRC, BASE = sys.argv[1:7]
def canon(raw):
    return hashlib.sha256(unicodedata.normalize("NFC", raw.decode()).replace("\\r\\n", "\\n").encode()).hexdigest()[:16]
# (nom, commande pre-vol, verdict pre-vol, sonde_etage1 pre-vol, mutation etage 1, factice, sonde_etage1 absent, attendu)
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
rc, so = courir([os.path.join(OUT, 'd2_portes_v2.py'), SONDE, MOTEUR, RUN, MANIF,
                 os.path.join(PV, 'sonde_etage1.json'), OUT], 'm2_v2_D2_portes.log')
lp = [l for l in so.splitlines() if l.startswith('PORTE ')]
chk('C15 D-2 levee : sur sept cas, la porte se FERME aux cinq cas interdits (original, croise, inverse, etage 1 '
    'mute, sonde_etage1.json absent -- sans exception) et reste OUVERTE aux deux chemins legitimes (tout reel, tout '
    'pre-vol)', rc == 0 and len(lp) == 7 and all(l.endswith(': OK') for l in lp), '%d cas, %d OK' % (
        len(lp), sum(1 for l in lp if l.endswith(': OK'))))

# ---------------------------------------------------------------- 7. l'ancrage a taille reelle sous la v2
say('=== 7. L ANCRAGE A TAILLE REELLE SOUS LA v2 : UNE DECOMPOSITION, (F1, G20, k = 3), POINT 1.95 ===')
with open(os.path.join(OUT, 'fumee_ancrage_m2_v2.py'), 'w', encoding='ascii', newline='\n') as fh:
    fh.write('''# UNE decomposition a taille reelle ; N'IMPRIME QUE gamma de l'etat d'ancrage et son rapport a G_run.
import sys, os, time, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN = sys.argv[1:4]
spec = importlib.util.spec_from_file_location("sonde_qeb", SONDE)
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
M = S.charger_moteur(MOTEUR)
p = S.parametres(RUN, False)["39_20"]
forme, r_c, N, L = S.geometrie("F1G20", p["r0"], False)
s = S.Systeme(M, N, p["w2"], p["g"], -1)
psi = S.cible(M, ("graine",), N, p["s"], p["w2"])
t0 = time.time()
vals, vecs = s.decomposer(p["eta0"] * 2.0 ** (-3), S.absorbeur(forme, r_c, N, L))
idx, x = S.choisir_graine(psi, 1)(vals, vecs)
g3 = float(-2.0 * vals[idx[0]].imag)
print("ANCRAGE point 39_20 N = %d : %.1f s ; gamma = %.10e ; G_run = %.10e ; rapport - 1 = %.3e ; au bit %s" % (
    N, time.time() - t0, g3, p["G_run"], g3 / p["G_run"] - 1.0, g3 == p["G_run"]))
''')
rc, so = courir([os.path.join(OUT, 'fumee_ancrage_m2_v2.py'), SONDE, MOTEUR, RUN], 'm2_v2_ancrage_reel_39_20.log')
m = re.search(r'ANCRAGE .* rapport - 1 = (\S+) ; au bit (\w+)', so)
CONS['ancrage_reel_v2'] = so.strip().splitlines()[-1] if so.strip() else ''
chk('C16 ancrage a taille reelle sous la SONDE v2 (machine 1 ne l a pas rejoue sous v2) : gamma(F1, G20, k = 3) au '
    'point 1.95 retombe AU BIT sur G_run', rc == 0 and m is not None and m.group(2) == 'True',
    '%s' % (m.group(0)[-70:] if m else so[-200:]))

# ---------------------------------------------------------------- bilan
nchk = len(CHK)
noms = [n for n, ok, _ in CHK if not ok]
say('=== BILAN : %d controles, %d mordent ===' % (nchk, len(noms)))
for n in noms:
    say('  MORD : ' + n)
with open(os.path.join(OUT, 'audit_sonde_EB_v2_machine2_v1.log'), 'w', encoding='ascii', errors='replace',
          newline='\n') as fh:
    fh.write('\n'.join(LOG) + '\n')
with open(os.path.join(OUT, 'audit_sonde_EB_v2_machine2_v1.json'), 'w', encoding='ascii', newline='\n') as fh:
    json.dump({'bilan': {'chk': nchk, 'mord': len(noms), 'noms': noms},
               'controles': [{'nom': n, 'ok': ok, 'detail': d} for n, ok, d in CHK],
               'consignes': CONS}, fh, indent=1, ensure_ascii=True)
