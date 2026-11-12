# -*- coding: ascii -*-
"""AUDIT machine 2 du gel 'qualification de l'estimateur E-B (Gamma_LS) v1' de machine 1.
2026-11-11. Classe B. AUCUN RUN DE L'ETAGE 1 NI 2 JOUE (E19) : ce sont des controles de LECTURE du
gel contre les pieces deja deposees, plus un ESSAI DE FORMULE de la rotation complexe du temoin
positif. DECLARE : cet essai calcule UN SEUL point de l'echelle du TP, g_8 = 0.10 (N <= 50, trois
theta), pour valider la formule de 5.1 ; il ne selectionne rien, la reference de l'etage 1 (17 g_j,
N jusqu'a 70) reste a jouer apres certification du gel ET de la sonde.

Usage : python audit_gel_EB_v1_machine2_v1.py GEL.md WKB.py MOTEUR.py GEL_M17.md DOSSIER_RUN MANIFESTE_RUN SORTIE_BASE
  (tous les chemins sont des ARGUMENTS ; rien n'est lu en dur ; le moteur est charge en LECTURE
   SEULE, sans ecrire de bytecode ; le script WKB de machine 1 est execute dans un dossier neutre).
Sorties : SORTIE_BASE.log et SORTIE_BASE.json (le bilan est LU par la fabrique du lot, jamais tape).
"""
import hashlib
import importlib.util
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import time
import unicodedata
from fractions import Fraction

sys.dont_write_bytecode = True
import numpy as np  # noqa: E402

if len(sys.argv) != 8:
    print(__doc__)
    sys.exit(2)
GEL, WKB, MOTEUR, GEL_M17, DOSSIER, MANIF, SORTIE = sys.argv[1:8]

CANON = {'moteur': ('82a0be882568fe0c', 103150),
         'gel_m17_v12_b2': ('20950e52e7d63225', 58507),
         'manifeste_run': ('4aecd0e2b23bc818', None)}

LOG = []
CHK = []          # (nom, ok, detail)
CONS = {}         # consignes (faits, pas des controles)


def emp(raw):
    t = unicodedata.normalize('NFC', raw.decode('utf-8').replace('\r\n', '\n')).encode('utf-8')
    return hashlib.sha256(t).hexdigest()[:16]


def say(s):
    LOG.append(s)
    print(s, flush=True)


def chk(nom, ok, detail=''):
    CHK.append((nom, bool(ok), detail))
    say('%-5s %s%s' % ('OK' if ok else 'MORD', nom, (' : ' + detail) if detail else ''))


def lire(p):
    return open(p, 'rb').read()


# ---------------------------------------------------------------- 1. les deux pieces livrees
say('=== 1. LES DEUX PIECES LIVREES ===')
brut_gel, brut_wkb = lire(GEL), lire(WKB)
for nom, brut in (('gel', brut_gel), ('wkb', brut_wkb)):
    CONS['empreinte_B_' + nom] = emp(brut)
    CONS['octets_' + nom] = len(brut)
    say('  %s : B %s  %d o  CR=%d  non-ASCII=%d' % (nom, emp(brut), len(brut), brut.count(b'\r'),
                                                  sum(1 for b in brut if b > 127)))
chk('C01 gel : ASCII pur, LF seul, termine par -- FIN --',
    all(b < 128 for b in brut_gel) and b'\r' not in brut_gel and brut_gel.rstrip().endswith(b'-- FIN --'))
chk('C02 script WKB : ASCII pur, LF seul',
    all(b < 128 for b in brut_wkb) and b'\r' not in brut_wkb)
TXT = brut_gel.decode('ascii')

# ---------------------------------------------------------------- 2. les sources citees
say('=== 2. LES SOURCES CITEES PAR LE GEL (section 2) ===')
brut_mot = lire(MOTEUR)
chk('C03 moteur au canon %s et a la taille %d' % CANON['moteur'],
    emp(brut_mot) == CANON['moteur'][0] and len(brut_mot) == CANON['moteur'][1],
    'lu %s %d o' % (emp(brut_mot), len(brut_mot)))
brut_g17 = lire(GEL_M17)
chk('C04 gel M17 v12_b2 au canon %s et a la taille %d' % CANON['gel_m17_v12_b2'],
    emp(brut_g17) == CANON['gel_m17_v12_b2'][0] and len(brut_g17) == CANON['gel_m17_v12_b2'][1],
    'lu %s %d o' % (emp(brut_g17), len(brut_g17)))
brut_man = lire(MANIF)
chk('C05 manifeste du run au canon %s' % CANON['manifeste_run'][0],
    emp(brut_man) == CANON['manifeste_run'][0], 'lu %s' % emp(brut_man))
lignes = [l.split() for l in brut_man.decode('utf-8').splitlines() if len(l.split()) >= 3]
mauvais = []
for emp_att, nom, taille in lignes:
    p = os.path.join(DOSSIER, nom)
    if not os.path.isfile(p):
        mauvais.append(nom + ' absente')
        continue
    r = lire(p)
    if emp(r) != emp_att or len(r) != int(taille):
        mauvais.append(nom + ' ecart')
chk('C06 dossier du run : %d pieces au canon et a la taille, comptees par le MANIFESTE' % len(lignes),
    len(lignes) == 36 and not mauvais, 'ecarts : %s' % (mauvais or 'aucun'))
noms_man = {l[1] for l in lignes}
hors = sorted(f for f in os.listdir(DOSSIER) if f not in noms_man)
CONS['fichiers_hors_manifeste'] = hors
say('  consigne : le dossier contient %d fichiers, dont %d hors manifeste : %s' %
    (len(os.listdir(DOSSIER)), len(hors), hors))

# ---------------------------------------------------------------- 3. les nombres du gel dans les pieces
say('=== 3. LES NOMBRES DU GEL, RELUS DANS LES SIX PIECES f070 ===')
PTS = [('39_20', 1.95), ('197_100', 1.97), ('99_50', 1.98), ('101_50', 2.02), ('203_100', 2.03),
       ('41_20', 2.05)]
G_run, hplus, rcs, etas, efac = [], [], [], [], []
for stem, w2 in PTS:
    d = json.load(open(os.path.join(DOSSIER, 'pt_%s_f070.json' % stem), encoding='utf-8'))
    e = d['EB']
    G_run.append(e['Gamma_LS']['H']['Gamma_LS'])
    hplus.append(abs(e['Gamma_LS']['Hplus']['Gamma_LS']))
    rcs.append(e['r_c'])
    etas.append(e['eta'])
    efac.append(e['operatif_4_6']['eta_final_facteur'])
    assert abs(float(Fraction(d['w2'])) - w2) < 1e-12
chk('C07 r0 = 40 a gauche (1.95 1.97 1.98), 41 a droite (2.02 2.03 2.05) ; N = r0 + 20',
    rcs == [40, 40, 40, 41, 41, 41], 'r_c lus %s' % rcs)
chk('C08 eta0 = |w2 - 2| (EB.eta) a 1e-12 aux six points',
    all(abs(et - abs(w - 2.0)) < 1e-12 for et, (_, w) in zip(etas, PTS)),
    'eta lus %s' % ['%.17g' % x for x in etas])
chk('C09 la valeur du run G_run est a k = 3 (eta_final_facteur = 0.125 = 2^-3) aux six points',
    all(f == 0.125 for f in efac), 'facteurs lus %s' % efac)
E_run = math.log(max(G_run) / min(G_run))
CONS['E_run'] = E_run
chk('C10 etendue E_run = ln(2.6614e-09 / 6.5625e-11) = 3.7027',
    '%.4e' % max(G_run) == '2.6614e-09' and '%.4e' % min(G_run) == '6.5625e-11' and
    '%.4f' % E_run == '3.7027', 'max %.4e  min %.4e  E_run %.6f' % (max(G_run), min(G_run), E_run))
chk('C11 plancher : max |Gamma(H+)| = 7.550e-14 aux six points, dix fois = 7.55e-13 -> decade 1e-12',
    '%.3e' % max(hplus) == '7.550e-14' and 10 * max(hplus) < 1e-12 <= 10 * 10 * max(hplus),
    'max %.4e' % max(hplus))

# ---------------------------------------------------------------- 4. les decomptes et le script WKB
say('=== 4. LES DECOMPTES ET LE SCRIPT WKB ===')
n_k = len(range(-2, 13))
decomp = {'F1': 6 * 2 * n_k, 'formes': 6 * 2 * n_k, 'translation': 6 * n_k, 'plancher': 6 * 5,
          'TP': 2 * 2 * n_k}
chk('C12 echelle k = -2..12 : 15 valeurs ; sommes 180 + 180 + 90 + 30 + 60 = 540',
    n_k == 15 and sum(decomp.values()) == 540, '%s total %d' % (decomp, sum(decomp.values())))
par = re.search(r'Decompositions attendues(.*?)## 9', TXT, re.S).group(1)
chk('C13 la liste "Decompositions attendues" couvre le TEMOIN NEGATIF (5.2)',
    re.search(r'\bTN\b|temoin negatif', par, re.I) is not None,
    'le texte declare "%s" ; le TN (15 decompositions, jusqu a 45 avec les replis a +5 puis -5) '
    'n y figure pas' % ' '.join(par.split())[:120])
neutre = tempfile.mkdtemp(prefix='wkb_neutre_')
r = subprocess.run([sys.executable, '-P', os.path.abspath(WKB)], cwd=neutre, capture_output=True,
                   text=True, timeout=120)
m = re.search(r'fenetre \[1e-11, 1e-7\] : \[([0-9, ]+)\] \((\d+) sur 17\)', r.stdout)
js = [int(x) for x in m.group(1).split(',')] if m else []
chk('C14 le script WKB de machine 1 tourne et rend j = 5..11 (7 sur 17) comme le gel l ecrit',
    r.returncode == 0 and js == list(range(5, 12)), 'rendu %s' % js)

# ---------------------------------------------------------------- 5. la comparaison de G-Q7 en flottants
say('=== 5. G-Q7 : "etalement 0.05 exactement -> PLATEAU" EN FLOTTANTS ===')
tau = 0.05
e_lit = 1.05 / 1.0 - 1.0
forme_b = 1.05 <= (1.0 + tau) * 1.0
CONS['G_Q7_etalement_litteral'] = repr(e_lit)
# serie a valeurs EXACTEMENT representables (20, 21) : etalement 21/20 - 1 = 1/20 exactement
e20 = 21.0 / 20.0 - 1.0
CONS['G_Q7_serie_20_21'] = {
    'etalement_litteral_flottant': repr(e20), 'litteral_<=_tau': e20 <= tau,
    'forme_max<=(1+tau)*min_flottant': 21.0 <= (1.0 + tau) * 20.0,
    'forme_exacte_Fraction': Fraction(21) <= (1 + Fraction(1, 20)) * Fraction(20)}
say('  consigne : serie (20.0, 21.0) -> %s' % CONS['G_Q7_serie_20_21'])
chk('C15 etalement litteral e = max/min - 1 sur la serie (1.0 ... 1.05) rend <= tau = 0.05',
    e_lit <= tau, 'e = %s ; e <= 0.05 : %s ; forme max <= (1+tau)*min : %s' % (repr(e_lit), e_lit <= tau, forme_b))

# ---------------------------------------------------------------- 6. la rotation complexe du TP (5.1)
say('=== 6. LA ROTATION COMPLEXE DU TEMOIN POSITIF (5.1) -- ESSAI, NON OPPOSABLE ===')
spec = importlib.util.spec_from_file_location('moteur_ro', MOTEUR)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)


def oscillateurs(N, w, theta):
    """w [cos2t n + (i/2) sin2t (a^2 + a+^2)] sur le bloc N x N, et le meme par x, p tournes."""
    a = np.diag(np.sqrt(np.arange(1, N + 2)), 1)           # taille N + 2 : le bloc N x N est exact
    ad = a.T
    n = ad @ a
    form = w * (math.cos(2 * theta) * n + 0.5j * math.sin(2 * theta) * (a @ a + ad @ ad))
    x = (a + ad) / math.sqrt(2.0 * w)
    p = 1j * math.sqrt(w / 2.0) * (ad - a)
    direct = 0.5 * np.exp(-2j * theta) * (p @ p) + 0.5 * w * w * np.exp(2j * theta) * (x @ x)
    # le point zero : direct contient w (n + 1/2) cos2t ; la formule du gel l'ajoute via (1/2) sum w cos2t
    return form[:N, :N], direct[:N, :N]


err_osc = 0.0
for w in (1.0, 1.95):
    for th in (0.0, 0.15, 0.30):
        f, d = oscillateurs(12, w, th)
        f = f + 0.5 * w * math.cos(2 * th) * np.eye(12)
        err_osc = max(err_osc, float(np.max(np.abs(f[:10, :10] - d[:10, :10]))))
chk('C16 partie oscillateur du gel (cos2t n + (i/2) sin2t (a^2 + a+^2) + point zero) == 1/2 e^-2it p^2 '
    '+ 1/2 w^2 e^2it x^2, matrices, bloc interieur', err_osc < 1e-12, 'ecart max %.2e' % err_osc)

W1_, W2_ = 1.0, 1.95
Dn = W2_ ** 2 - W1_ ** 2
_, l1m, l2m = M.lambdas(Fraction(39, 20))
chk('C17 x du moteur = (q1 + q2) / sqrt(Delta) : l_i = 1 / sqrt(2 Delta w_i), donc lineaire en q_i '
    '-> e^{i t} x et e^{5 i t} x^5 sous la rotation',
    abs(l1m - 1 / math.sqrt(2 * Dn * W1_)) < 1e-15 and abs(l2m - 1 / math.sqrt(2 * Dn * W2_)) < 1e-15,
    'l1 %.12g  l2 %.12g' % (l1m, l2m))


def H_rot(N, g, theta):
    """H(theta) du gel 5.1 ; x^5 EXACT sur le bloc (produit dans une base elargie, puis coupe)."""
    Mx = N + 5
    a = np.diag(np.sqrt(np.arange(1, Mx)), 1)
    xt = a + a.T
    Xj = [np.linalg.matrix_power(xt, j)[:N, :N] for j in range(6)]
    x5 = np.zeros((N * N, N * N))
    for j in range(6):
        x5 += math.comb(5, j) * l1m ** j * l2m ** (5 - j) * np.kron(Xj[j], Xj[5 - j])
    n = np.diag(np.arange(N, dtype=float))
    aN = np.diag(np.sqrt(np.arange(1, N)), 1)
    sq = aN @ aN + aN.T @ aN.T
    I = np.eye(N)
    c2, s2 = math.cos(2 * theta), math.sin(2 * theta)
    H = np.zeros((N * N, N * N), dtype=complex)
    H += W1_ * (c2 * np.kron(n, I) + 0.5j * s2 * np.kron(sq, I))
    H += W2_ * (c2 * np.kron(I, n) + 0.5j * s2 * np.kron(I, sq))
    H += 0.5 * (W1_ + W2_) * (c2 - 1.0) * np.eye(N * N)
    H += np.exp(5j * theta) * (g / 5.0) * x5
    return H


N0, g0 = 14, 0.10
Hm, _ = M.H_2D(N0, Fraction(39, 20), g0, +1, 'x5', 0.0, None)
ecart0 = float(np.max(np.abs(H_rot(N0, g0, 0.0) - Hm)))
chk('C18 theta = 0 : H_rot == H_2D(N, w2, g, +1, "x5") du moteur, element par element',
    ecart0 < 1e-12 * float(np.max(np.abs(Hm))), 'ecart max %.2e (max|H| %.3f)' % (ecart0, np.max(np.abs(Hm))))

GRID_N, GRID_T, G_TEST = (30, 40, 50), (0.15, 0.20, 0.25), 0.10
essai = []
for N in GRID_N:
    psi = np.zeros(N * N)
    psi[0] = 1.0
    for th in GRID_T:
        t0 = time.time()
        v, V = np.linalg.eig(H_rot(N, G_TEST, th))
        rec = np.abs(V.conj().T @ psi) ** 2
        nu = int(np.lexsort((v.real, -rec))[0])
        essai.append({'N': N, 'theta': th, 'E_re': float(v[nu].real), 'Gamma': float(-2 * v[nu].imag),
                      'rec': float(rec[nu]), 'secondes': round(time.time() - t0, 1)})
        say('  N=%d theta=%.2f  E=%.10f  Gamma=-2 Im E = %.4e  recouvrement %.4f  (%.1f s)' %
            (N, th, v[nu].real, -2 * v[nu].imag, rec[nu], time.time() - t0))
CONS['essai_rotation_g'] = G_TEST
CONS['essai_rotation'] = essai
gam = [e['Gamma'] for e in essai]
spread_theta = max(max(e['Gamma'] for e in essai if e['N'] == N) / min(e['Gamma'] for e in essai if e['N'] == N)
                   for N in GRID_N)
chk('C19 la resonance fondamentale du jumeau H+ a g = %.2f a une largeur POSITIVE, STABLE en theta '
    '(etalement max/min sur trois theta, a chaque N) -- une formule fausse ne rendrait pas de plateau en theta'
    % G_TEST, all(x > 0 for x in gam) and spread_theta < 1.5,
    'etalements par N : %s' % ['%.3f' % (max(e['Gamma'] for e in essai if e['N'] == N) /
                                         min(e['Gamma'] for e in essai if e['N'] == N)) for N in GRID_N])

# ---------------------------------------------------------------- 7. ce que le gel prend de l'etape 0
say('=== 7. CE QUE LE GEL PREND DE L ETAPE 0 : CE QUE LES SIX PIECES PERMETTENT DE RELIRE ===')
portes, derniers, dernier_gt_prec = [], [], []
for stem, w2 in PTS:
    e = json.load(open(os.path.join(DOSSIER, 'pt_%s_f070.json' % stem), encoding='utf-8'))['EB']
    acc = [x for x in e['critere_absorbeur']['essais'] if x.get('accepte')][-1]
    portes.append((e['stationnarites']['N_plus_p'], e['stationnarites']['translation_p']))
    derniers.append(list(acc['pas'][-2:]))
    dernier_gt_prec.append(acc['pas'][-1] > acc['pas'][-2])
chk('C20 aux six points, les portes (N + p, translation de p couches) et les deux derniers pas de '
    'descente sont sous tau_LS = 0.05 (gel, section 2, derniere phrase)',
    all(a < 0.05 and b < 0.05 for a, b in portes) and all(q < 0.05 for pr in derniers for q in pr),
    'portes max %.4f ; derniers pas max %.4f' % (max(max(p) for p in portes),
                                                 max(max(pr) for pr in derniers)))
chk('C21 la premisse de l annonce A-2 est exacte : le dernier pas du run est plus grand que le '
    'precedent a 2.02 (et a lui seul)', dernier_gt_prec == [False, False, False, True, False, False],
    'dernier > precedent aux six points : %s' % dernier_gt_prec)
CONS['etape0'] = ('non retrouvee sur ce poste : voir cherche_etape0_machine2_v1.log ; les quatre canons '
                  '20cbc762d58ce1ca 2d246b2a5c60c244 37169cd7d595c575 94c3749c83d4b044 ne sont lus '
                  'dans aucun fichier ni membre de zip')

# ---------------------------------------------------------------- bilan
nchk = len(CHK)
noms = [n for n, ok, _ in CHK if not ok]
say('=== BILAN : %d controles, %d mordent ===' % (nchk, len(noms)))
for n in noms:
    say('  MORD : ' + n)

with open(SORTIE + '.log', 'w', encoding='ascii', newline='\n') as fh:
    fh.write('\n'.join(LOG) + '\n')
with open(SORTIE + '.json', 'w', encoding='ascii', newline='\n') as fh:
    json.dump({'bilan': {'chk': nchk, 'mord': len(noms), 'noms': noms},
               'controles': [{'nom': n, 'ok': ok, 'detail': d} for n, ok, d in CHK],
               'consignes': CONS}, fh, indent=1, ensure_ascii=True)
