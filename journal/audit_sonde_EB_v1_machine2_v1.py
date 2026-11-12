# -*- coding: ascii -*-
"""AUDIT machine 2 de la SONDE, de la FEUILLE DE LECTURE et du BANC QUI TUE de qualification E-B v1
(machine 1, 2026-11-11, ecrits contre le gel v2 cde0cd11a763f26d). Classe B.

E19 : AUCUN RUN DE L'ETAGE 1 NI 2 JOUE. Ce qui est calcule ici est declare : les pre-vols (geometrie
reduite, NON OPPOSABLES), le banc, la porte de l'etage 2 (sentinelle, sans calcul), UN calcul de
G-Q3 a taille reelle (matrices seulement) et UNE decomposition (F1, G20, k = 3) au point 1.95 pour
l'ancrage, dont SEUL gamma de l'etat d'ancrage est imprime (aucun T-etat : cf. D-QEB-1).

Usage : python audit_sonde_EB_v1_machine2_v1.py LOT_EXTRAIT MOTEUR DOSSIER_RUN MANIFESTE_RUN SORTIE_DIR
  LOT_EXTRAIT = le lot de machine 1 extrait dans un dossier neuf ; SORTIE_DIR = dossier NEUF.
  Tous les chemins sont des ARGUMENTS. Les scripts de machine 1 sont lances avec 'python -P'
  (et non -I : voir D-3) depuis SORTIE_DIR.
Sorties : SORTIE_DIR/audit_sonde_EB_v1_machine2_v1.log et .json, plus les journaux des rejeux."""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import unicodedata

sys.dont_write_bytecode = True
if len(sys.argv) != 6:
    print(__doc__)
    sys.exit(2)
LOT, MOTEUR, RUN, MANIF, OUT = [os.path.abspath(x) for x in sys.argv[1:6]]
if os.path.exists(OUT) and os.listdir(OUT):
    sys.exit('SORTIE_DIR doit etre un dossier neuf et vide : %s' % OUT)
os.makedirs(OUT, exist_ok=True)
PY = [sys.executable, '-P']
SONDE = os.path.join(LOT, 'sonde_qualification_EB_machine1_v1.py')
LECT = os.path.join(LOT, 'lecture_qualification_EB_machine1_v1.py')
BANC = os.path.join(LOT, 'banc_qui_tue_qualification_EB_machine1_v1.py')
PV = os.path.join(LOT, 'prevol')
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


def courir(args, nom_log, cwd=OUT, timeout=900):
    r = subprocess.run(PY + args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    txt = r.stdout + (('\n[stderr]\n' + r.stderr) if r.stderr.strip() else '')
    with open(os.path.join(OUT, nom_log), 'w', encoding='ascii', errors='replace', newline='\n') as fh:
        fh.write(txt)
    return r.returncode, r.stdout


def arrondi(ligne):
    return re.sub(r'[-+]?\d+\.\d+(?:[eE][-+]?\d+)?', lambda m: '%.3g' % float(m.group(0)), ligne)


# ---------------------------------------------------------------- 1. le lot
say('=== 1. LE LOT ENTRANT ===')
man = lire(os.path.join(LOT, 'MANIFEST_lot_machine1_sonde_EB_v1_v1.txt'))
CONS['canon_lot'] = eb(man)
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
chk('C01 lot : %d pieces au canon, a l empreinte brute et a la taille (canon du lot %s)' % (len(pieces), CONS['canon_lot']),
    len(pieces) == 39 and not mal, 'ecarts : %s' % (mal or 'aucun'))
canons = {n: eb(lire(p)) for n, p in (('sonde', SONDE), ('lecture', LECT), ('banc', BANC))}
CONS['canons_scripts'] = canons
brutes = [lire(p) for p in (SONDE, LECT, BANC)]
chk('C02 les trois scripts : ASCII pur, LF seul, et chacun cite le gel v2 cde0cd11a763f26d ; le gel v2 du lot '
    'est au canon cde0cd11a763f26d',
    all(all(b < 128 for b in r) and b'\r' not in r and b'cde0cd11a763f26d' in r for r in brutes) and
    eb(lire(os.path.join(LOT, 'qualification_EB_pre_enregistrement_v2.md'))) == 'cde0cd11a763f26d',
    'sonde %s lecture %s banc %s' % (canons['sonde'], canons['lecture'], canons['banc']))

# ---------------------------------------------------------------- 2. selftest et pre-vol de l'etage 1
say('=== 2. SELFTEST ET PRE-VOL DE L ETAGE 1 (NON OPPOSABLE) ===')
rc, so = courir([LECT, '--selftest'], 'm2_selftest.log')
chk('C03 selftest G-Q7 de la feuille de lecture : 13 tenus sur 13', rc == 0 and '13 tenus sur 13' in so, so.strip().splitlines()[-1])
PVS = os.path.join(OUT, 'pv')
rc, so = courir([SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF, '--sortie', PVS, '--etage', '1',
                 '--retenus', os.path.join(PV, 'tp_retenus_prevol.json'), '--prevol'], 'm2_prevol_etage1_sonde.log')
s1 = json.load(open(os.path.join(PVS, 'sonde_etage1.json')))
CONS['plateforme_m2'] = s1['plateforme']
c = s1['comptes']
chk('C04 pre-vol etage 1 : G-Q3 six sur six ; TN 15, TP 30, plancher 30 ; G-Q10 ; temoin d arrondi lu CR',
    rc == 0 and all(s1['GQ3'].values()) and len(s1['GQ3']) == 6 and
    sum(c['TN'].values()) == 15 and sum(c['TP'].values()) == 30 and sum(c['plancher'].values()) == 30 and
    s1['GQ10'] and s1['plateforme']['temoin_lecture'] == 'CR', 'comptes %s' % c)
rc, so = courir([LECT, '--etage', '1', '--sortie', PVS, '--reference', os.path.join(PV, 'tp_reference_prevol.json')],
                'm2_prevol_etage1_lecture.log')
mien = [arrondi(l) for l in lire(os.path.join(PVS, 'lecture_etage1.log')).decode().splitlines() if 'canon' not in l]
sien = [arrondi(l) for l in lire(os.path.join(PV, 'lecture_etage1.log')).decode().splitlines() if 'canon' not in l]
chk('C05 lecture de l etage 1 rejouee == celle de machine 1 (hors canon ; nombres a 3 chiffres significatifs : '
    'un affichage de la 5e decimale differe, 1.7179 / 1.7178, par plateforme)', rc == 0 and mien == sien,
    '%d lignes' % len(mien))
shutil.copy(os.path.join(PVS, 'verdict_etage1.json'), os.path.join(PVS, 'verdict_etage1_reel.json'))

# ---------------------------------------------------------------- 3. pre-vol de l'etage 2
say('=== 3. PRE-VOL DE L ETAGE 2 SOUS VERDICT FACTICE DE MON CANON (NON OPPOSABLE) ===')
json.dump({'canon_sonde_etage1': eb(lire(os.path.join(PVS, 'sonde_etage1.json'))), 'etage1': 'TIENT', 'factice': True,
           'note': 'verdict FACTICE (m2) : teste le chemin de l etage 2 en pre-vol, pas le jugement', 'prevol': True},
          open(os.path.join(PVS, 'verdict_etage1.json'), 'w'), sort_keys=True)
rc, so = courir([SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF, '--sortie', PVS, '--etage', '2',
                 '--verdict1', os.path.join(PVS, 'verdict_etage1.json'), '--prevol'], 'm2_prevol_etage2_sonde.log')
s2 = json.load(open(os.path.join(PVS, 'sonde_etage2.json')))
c = s2['comptes']
perdus = tot = 0
idmin, sc_max = 9.0, 0.0
for n, p in s2['points'].items():
    for cfg, cc in p['cfg'].items():
        idmin = min(idmin, cc['identite'])
        for rec in cc['traj'].values():
            for e in rec['etats']:
                tot += 1
                perdus += 0 if e['suivi'] else 1
        if cfg == 'F1G20':
            r3 = cc['traj']['3']
            sc_max = max(sc_max, abs(complex(r3['somme_c_re'], r3['somme_c_im']) - 1.0))
CONS['etage2_prevol'] = {'etats_suivis_comptes': tot, 'perdus': perdus, 'identite_min': idmin, 'ecart_somme_c_max': sc_max}
chk('C06 pre-vol etage 2 : F1 174 joues + 6 repris == 180, formes 180, translation 90, ouverture 6 ; %d etats-pas, '
    '%d perdus ; identite min %.4f ; |somme des c - 1| max %.1e' % (tot, perdus, idmin, sc_max),
    rc == 0 and c['F1'] == {'joues': 174, 'repris': 6, 'sautes': 0} and sum(c['formes'].values()) == 180 and
    sum(c['translation'].values()) == 90 and c['ouverture']['joues'] == 6 and tot == 1260 and perdus == 0 and
    idmin > 0.999 and sc_max < 1e-12 and s2['GQ10'], 'comptes %s' % c)
rc, so = courir([LECT, '--etage', '2', '--sortie', PVS], 'm2_prevol_etage2_lecture.log')
mien = [l for l in lire(os.path.join(PVS, 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
sien = [l for l in lire(os.path.join(PV, 'lecture_etage2.log')).decode().splitlines() if 'canon' not in l]
chk('C07 lecture de l etage 2 rejouee IDENTIQUE a celle de machine 1 (hors canon)', rc == 0 and mien == sien,
    '%d lignes ; verdict "%s"' % (len(mien), [l for l in mien if l.startswith('VERDICT')]))

# ---------------------------------------------------------------- 4. le banc qui tue
say('=== 4. LE BANC QUI TUE ===')
BP = os.path.join(OUT, 'pv_banc')
os.makedirs(BP)
for f in ('sonde_etage1.json', 'verdict_etage1.json', 'verdict_etage1_reel.json', 'ancrage_prevol.json'):
    shutil.copy(os.path.join(PVS, f), BP)
argsb = ['--lecture', LECT, '--sonde', SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF, '--prevol', BP,
         '--retenus', os.path.join(PV, 'tp_retenus_prevol.json')]
rc, so = courir([BANC] + argsb + ['--sortie', os.path.join(OUT, 'banc_tel_que_livre')], 'm2_banc_tel_que_livre.log')
dern = so.strip().splitlines()[-1]
chk('C08 D-3 : le banc TEL QUE LIVRE rend 6 mordues sur 6 sur ce poste (il lance la sonde par python -I, qui '
    'ecarte les paquets utilisateur, donc numpy ici)', rc == 0 and '6 mordues == 6 attendues' in dern, dern)
copie = os.path.join(OUT, 'banc_copie_m2_P.py')
src = lire(BANC).decode('ascii')
assert src.count('sys.executable, "-I", a.sonde') == 1
open(copie, 'w', encoding='ascii', newline='\n').write(src.replace('sys.executable, "-I", a.sonde',
                                                                      'sys.executable, "-P", a.sonde'))
rc, so = courir([copie] + argsb + ['--sortie', os.path.join(OUT, 'banc_copie_P')], 'm2_banc_copie_P.log')
dern = so.strip().splitlines()[-1]
chk('C09 le MEME banc avec une seule modification, -I -> -P (copie de mon cru), rend 6 mordues sur 6, base saine, '
    'porte tenue', rc == 0 and '6 mordues == 6 attendues' in dern and 'PASSE' in dern, dern)

# ---------------------------------------------------------------- 5. D-1 et D-2
say('=== 5. D-1 (REPRISE) ET D-2 (PORTE), SANS DECOMPOSITION ===')
CT = os.path.join(OUT, 'pv_contamine')
os.makedirs(CT)
shutil.copytree(os.path.join(PVS, 'reprise'), os.path.join(CT, 'reprise'))
rc, so = courir([SONDE, '--moteur', MOTEUR, '--run', RUN, '--manifeste', MANIF, '--sortie', CT, '--etage', '1',
                 '--retenus', os.path.join(PV, 'tp_retenus_prevol.json')], 'm2_D1_contamination_etage1_reel.log')
sc = json.load(open(os.path.join(CT, 'sonde_etage1.json')))
cc = sc['comptes']
CONS['D1'] = {'prevol_ecrit': sc['prevol'], 'comptes': cc, 'GQ10': sc['GQ10']}
chk('C10 D-1 : un etage 1 REEL lance dans un dossier qui ne contient que la reprise d un PRE-VOL doit REFUSER '
    '(la reprise ne controle ni la geometrie, ni le canon de la sonde, ni prevol)',
    rc != 0,
    'il a rendu code %d : joues %d, repris %d, sonde_etage1.json ecrit avec prevol = %s et GQ10 = %s' %
    (rc, sum(v['joues'] for v in cc.values()), sum(v['repris'] for v in cc.values()), sc['prevol'], sc['GQ10']))
gq3 = re.findall(r'G-Q3 (\S+)\s+N = (\d+) : (\w+)', so)
chk('C11 G-Q3 A TAILLE REELLE : la forme native est celle du moteur element par element aux six points '
    '(N = 60, 60, 60, 61, 61, 61), matrices seulement, aucune decomposition',
    [(a, int(b), c3) for a, b, c3 in gq3] == [('39_20', 60, 'OK'), ('197_100', 60, 'OK'), ('99_50', 60, 'OK'),
                                              ('101_50', 61, 'OK'), ('203_100', 61, 'OK'), ('41_20', 61, 'OK')],
    '%s' % gq3)
with open(os.path.join(OUT, 'd2_porte.py'), 'w', encoding='ascii', newline='\n') as fh:
    fh.write('''# Porte de l'etage 2 SANS calcul : etage2 est remplace par une sentinelle.
import sys, os, json, shutil, hashlib, unicodedata, importlib.util
sys.dont_write_bytecode = True
SONDE, MOTEUR, RUN, MANIF, SRC, D = sys.argv[1:7]
spec = importlib.util.spec_from_file_location("sonde_qeb", SONDE)
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
def sentinelle(*a, **k): raise RuntimeError("PORTE FRANCHIE")
S.etage2 = sentinelle
shutil.rmtree(D, ignore_errors=True); os.makedirs(D)
shutil.copy(SRC, os.path.join(D, "sonde_etage1.json"))
raw = open(os.path.join(D, "sonde_etage1.json"), "rb").read()
c = hashlib.sha256(unicodedata.normalize("NFC", raw.decode()).replace("\\r\\n", "\\n").encode()).hexdigest()[:16]
print("sonde_etage1.json : prevol = %s" % json.loads(raw)["prevol"])
json.dump({"canon_sonde_etage1": c, "etage1": "TIENT", "prevol": True}, open(os.path.join(D, "v.json"), "w"))
sys.argv = ["sonde", "--moteur", MOTEUR, "--run", RUN, "--manifeste", MANIF, "--sortie", D, "--etage", "2",
            "--verdict1", os.path.join(D, "v.json")]
try:
    S.main()
except RuntimeError as e:
    print(e)
except SystemExit as e:
    print("PORTE FERMEE (SystemExit %s)" % e.code)
''')
rc, so = courir([os.path.join(OUT, 'd2_porte.py'), SONDE, MOTEUR, RUN, MANIF, os.path.join(PVS, 'sonde_etage1.json'),
                 os.path.join(OUT, 'pv_d2')], 'm2_D2_porte.log')
chk('C12 D-2 : un etage 2 REEL (sans --prevol) doit REFUSER un verdict d etage 1 marque prevol, sur un '
    'sonde_etage1.json de pre-vol', 'PORTE FERMEE' in so, 'rendu : %s' % ([l for l in so.splitlines() if 'PORTE' in l] or so[-120:]))

# ---------------------------------------------------------------- 6. l'ancrage a taille reelle
say('=== 6. L ANCRAGE A TAILLE REELLE : UNE DECOMPOSITION, (F1, G20, k = 3), POINT 1.95 ===')
with open(os.path.join(OUT, 'fumee_ancrage_m2.py'), 'w', encoding='ascii', newline='\n') as fh:
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
rc, so = courir([os.path.join(OUT, 'fumee_ancrage_m2.py'), SONDE, MOTEUR, RUN], 'm2_ancrage_reel_39_20.log')
m = re.search(r'ANCRAGE .* rapport - 1 = (\S+) ; au bit (\w+)', so)
CONS['ancrage_reel'] = so.strip().splitlines()[-1] if so.strip() else ''
chk('C13 ancrage a taille reelle sur BOCAL4 : gamma(F1, G20, k = 3) au point 1.95 retombe sur G_run a 1e-3 '
    '(le gel attend le bit sur BOCAL4)', rc == 0 and m is not None and abs(float(m.group(1))) <= 1e-3,
    '%s' % (m.group(0)[-60:] if m else so[-200:]))

# ---------------------------------------------------------------- bilan
nchk = len(CHK)
noms = [n for n, ok, _ in CHK if not ok]
say('=== BILAN : %d controles, %d mordent ===' % (nchk, len(noms)))
for n in noms:
    say('  MORD : ' + n)
with open(os.path.join(OUT, 'audit_sonde_EB_v1_machine2_v1.log'), 'w', encoding='ascii', errors='replace',
          newline='\n') as fh:
    fh.write('\n'.join(LOG) + '\n')
with open(os.path.join(OUT, 'audit_sonde_EB_v1_machine2_v1.json'), 'w', encoding='ascii', newline='\n') as fh:
    json.dump({'bilan': {'chk': nchk, 'mord': len(noms), 'noms': noms},
               'controles': [{'nom': n, 'ok': ok, 'detail': d} for n, ok, d in CHK],
               'consignes': CONS}, fh, indent=1, ensure_ascii=True)
