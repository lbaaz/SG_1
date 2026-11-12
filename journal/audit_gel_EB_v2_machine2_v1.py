# -*- coding: ascii -*-
"""AUDIT machine 2 du gel 'qualification de l'estimateur E-B (Gamma_LS) v2' de machine 1.
2026-11-11. Classe B. AUCUN RUN JOUE (E19) : controles de LECTURE du v2 contre le v1 que j'ai
audite, contre le lot entrant et contre les pieces deja deposees. La sonde n'est pas livree : rien
n'en est certifie ici.

Usage : python audit_gel_EB_v2_machine2_v1.py V1 DOSSIER_LOT_ENTRANT DOSSIER_RUN MANIFESTE_RUN SORTIE_BASE
  V1 = qualification_EB_pre_enregistrement_v1.md ; DOSSIER_LOT_ENTRANT = le lot de machine 1
  EXTRAIT dans un dossier neuf. Tous les chemins sont des ARGUMENTS. La construction de machine 1
  est executee dans un dossier neutre, sortie hors du lot.
Sorties : SORTIE_BASE.log et SORTIE_BASE.json (le bilan est LU par la fabrique du lot)."""
import difflib
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
import zipfile
from fractions import Fraction

sys.dont_write_bytecode = True

if len(sys.argv) != 6:
    print(__doc__)
    sys.exit(2)
V1, LOT, DOSSIER, MANIF, SORTIE = sys.argv[1:6]

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


def lignes_manifeste(p, colonnes):
    out = []
    for l in lire(p).decode('utf-8').splitlines():
        t = l.split()
        if l.startswith('#') or len(t) != colonnes or len(t[0]) != 16:
            continue
        out.append(t)
    return out


# ---------------------------------------------------------------- 1. le lot entrant
say('=== 1. LE LOT ENTRANT DE MACHINE 1 ===')
man_lot = os.path.join(LOT, 'MANIFEST_lot_machine1_gel_EB_v2_v1.txt')
CONS['canon_lot_entrant'] = eb(lire(man_lot))
mal = []
pieces = lignes_manifeste(man_lot, 5)
for e, br, ob, obr, nom in pieces:
    r = lire(os.path.join(LOT, nom))
    if eb(r) != e or hashlib.sha256(r).hexdigest()[:16] != br or len(r) != int(obr):
        mal.append(nom)
chk('C01 lot entrant : %d pieces au canon B, a l empreinte brute et a la taille (canon du lot %s)'
    % (len(pieces), CONS['canon_lot_entrant']), len(pieces) == 18 and not mal, 'ecarts : %s' % (mal or 'aucun'))

# ---------------------------------------------------------------- 2. l'etape 0, enfin livree
say('=== 2. L ETAPE 0 (M-3), JOINTE AU LOT ===')
man0 = os.path.join(LOT, 'etape0', 'MANIFEST_lot_machine1_piste0_etape0_v1.txt')
p0 = lignes_manifeste(man0, 3)
mal0 = [n for e, n, t in p0 if eb(lire(os.path.join(LOT, 'etape0', n))) != e or
        len(lire(os.path.join(LOT, 'etape0', n))) != int(t)]
CITES = {'20cbc762d58ce1ca', '2d246b2a5c60c244', '37169cd7d595c575'}
chk('C02 etape 0 : manifeste au canon 94c3749c83d4b044, %d pieces au canon, et les trois pieces citees '
    'par le gel v1 (section 2) y figurent' % len(p0),
    eb(lire(man0)) == '94c3749c83d4b044' and len(p0) == 10 and not mal0 and CITES <= {e for e, _, _ in p0},
    'ecarts : %s' % (mal0 or 'aucun'))

# ---------------------------------------------------------------- 3. v2 = v1 + construction
say('=== 3. LE v2 SE RECONSTRUIT DEPUIS LE v1 ===')
v1 = lire(V1)
v2 = lire(os.path.join(LOT, 'qualification_EB_pre_enregistrement_v2.md'))
chk('C03 v1 au canon 8603af9d4f63e9dc ; v2 au canon cde0cd11a763f26d',
    eb(v1) == '8603af9d4f63e9dc' and eb(v2) == 'cde0cd11a763f26d', 'lus %s %s' % (eb(v1), eb(v2)))
neutre = tempfile.mkdtemp(prefix='reconstruction_v2_')
sortie = os.path.join(neutre, 'v2_reconstruit.md')
r = subprocess.run([sys.executable, '-P', os.path.abspath(os.path.join(LOT, 'construction_gel_EB_v2_machine1_v1.py')),
                    os.path.abspath(V1), sortie], cwd=neutre, capture_output=True, text=True, timeout=120)
rec = lire(sortie) if os.path.isfile(sortie) else b''
chk('C04 la construction de machine 1 rejouee chez moi depuis le v1 rend un v2 IDENTIQUE AU BIT '
    'au v2 livre, par 18 remplacements', r.returncode == 0 and rec == v2 and r.stdout.count('applique :') == 18,
    'sortie %s ; %d remplacements ; code %d %s' % ('identique' if rec == v2 else 'DIFFERENTE',
                                                  r.stdout.count('applique :'), r.returncode,
                                                  r.stderr.strip()[-200:]))

# ---------------------------------------------------------------- 4. le diff
say('=== 4. LE DIFF ===')
a, b = v1.decode('ascii').splitlines(), v2.decode('ascii').splitlines()
mien = [l for l in difflib.unified_diff(a, b, lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
sien = [l for l in lire(os.path.join(LOT, 'diff_gel_EB_v1_v2.txt')).decode('ascii').splitlines()
        if l[:1] in '+-' and l[:3] not in ('+++', '---')]
chk('C05 le diff joint == mon diff : memes lignes ajoutees et retirees, dans le meme ordre',
    mien == sien, '%d lignes de changement chez moi, %d dans le diff joint ; ajoutees %d, retirees %d' %
    (len(mien), len(sien), sum(1 for l in mien if l[0] == '+'), sum(1 for l in mien if l[0] == '-')))


def bloc(txt, debut, fin):
    return re.search(re.escape(debut) + r'(.*?)' + re.escape(fin), txt, re.S).group(1)


t1, t2 = v1.decode('ascii'), v2.decode('ascii')
tol1 = bloc(t1, '## 4. Tolerances (aucune n\'est fixee apres lecture)', 'Ce que la plume a vu')
tol2 = bloc(t2, '## 4. Tolerances (aucune n\'est fixee apres lecture)', 'Ce que la plume a vu')
chk('C06 section 4 : le bloc des tolerances (tau, 0.90, 1e-12, tau_TP) est identique au v1 octet pour octet',
    tol1 == tol2 and 'tau = 0.05' in tol2, '%d caracteres' % len(tol2))
chk('C07 les nombres mesures cites sont intacts dans le v2 : 3.7027 ; 2.6614e-09 / 6.5625e-11 ; 7.550e-14 ; '
    '"5e+03 a 5e+06"', all(s in t2 for s in ('3.7027', '2.6614e-09 / 6.5625e-11', '7.550e-14', '5e+03 a 5e+06')))

# ---------------------------------------------------------------- 5. E-EB-2 : le compte
say('=== 5. E-EB-2 : LE DECOMPTE ===')
par = re.search(r'Decompositions attendues(.*?)## 9', t2, re.S).group(1)
nb = [int(x) for x in re.findall(r'(?:F1|formes|translation|plancher|TP au plus|TN)\s+(\d+)', par)]
chk('C08 le decompte du v2 nomme le TN et somme 180 + 180 + 90 + 30 + 60 + 15 = 555 ("au plus 555")',
    re.search(r'\bTN 15\b', par) is not None and nb == [180, 180, 90, 30, 60, 15] and sum(nb) == 555 and
    'au\nplus 555' in par, 'lus %s, somme %d' % (nb, sum(nb)))

# ---------------------------------------------------------------- 6. E-EB-1 : la borne exacte
say('=== 6. E-EB-1 : LA REGLE DU v2, JOUEE ===')


def plateau_exact(serie):
    """Regle du v2 (3.11) : cinq valeurs a k consecutifs, Fraction(max) <= (1 + 1/20) * Fraction(min)."""
    for d in range(len(serie) - 4):
        f = serie[d:d + 5]
        if Fraction(max(f)) <= (1 + Fraction(1, 20)) * Fraction(min(f)):
            return True
    return False


lim = [20.0, 20.25, 20.5, 20.75, 21.0]
lim_plus = [20.0, 20.25, 20.5, 20.75, math.nextafter(21.0, math.inf)]
trap_v1 = [1.0, 1.0125, 1.025, 1.0375, 1.05]
CONS['G_Q7_v2'] = {'borne_exacte_(20..21)': plateau_exact(lim), 'borne_plus_un_ulp': plateau_exact(lim_plus),
                   'serie_du_piege_v1_(1.0..1.05)_en_rationnels': plateau_exact(trap_v1)}
chk('C09 G-Q7 du v2 est SATISFAISABLE : (20.0 ... 21.0) -> PLATEAU, la meme avec nextafter(21.0, +inf) '
    '-> PAS DE PLATEAU, en rationnels exacts', plateau_exact(lim) and not plateau_exact(lim_plus),
    '%s' % CONS['G_Q7_v2'])
tau = 0.05
say('  consigne (pas un controle) : G-Q7 ACCORD ecrit "|ln| = tau - 1e-6 -> ACCORD ; tau + 1e-6 -> PAS" et '
    'vaut aussi pour "l accord au TP" dont la borne est tau_TP = tau + u_ref (section 4) : le second '
    'cas rend ACCORD des que u_ref > 1e-6 -> reserve R-2 de la note (le selftest doit dire u_ref = 0)')
CONS['reserve_R2'] = 'G-Q7 : accord au TP a tau_TP = tau + u_ref ; le test a tau + 1e-6 suppose u_ref = 0'

# ---------------------------------------------------------------- 7. M-2 : le 37e fichier
say('=== 7. M-2 : LE 37e FICHIER DU DOSSIER DU RUN ===')
p37 = os.path.join(DOSSIER, 'pt_39_20_f100.zip')
raw37 = lire(p37)
z = zipfile.ZipFile(p37)
noms_man = sorted(t[1] for t in lignes_manifeste(MANIF, 3))
membres_ok = all(eb(z.read(n)) == e for e, n, _ in lignes_manifeste(MANIF, 3))
chk('C10 le 37e fichier est l archive de transport : 48748 o, sha256 79c57b2bccfa43bb89df60ab088fc9d0f1df2a92'
    'd818aa7a1d07f5596796a28c (celui que machine 1 donne), 36 membres == les 36 lignes du manifeste, '
    'au canon, aucun zip interne',
    len(raw37) == 48748 and hashlib.sha256(raw37).hexdigest() ==
    '79c57b2bccfa43bb89df60ab088fc9d0f1df2a92d818aa7a1d07f5596796a28c' and
    sorted(z.namelist()) == noms_man and membres_ok and not [n for n in z.namelist() if n.endswith('.zip')],
    '%d o, %d membres' % (len(raw37), len(z.namelist())))

# ---------------------------------------------------------------- 8. une phrase de l'etape 0, relue dans les pieces
say('=== 8. UNE PHRASE DE L ETAPE 0 QUE LES PIECES PERMETTENT DE RELIRE ===')
rap = []
for stem in ('39_20', '197_100', '99_50', '101_50', '203_100', '41_20'):
    h = json.load(open(os.path.join(DOSSIER, 'pt_%s_f070.json' % stem), encoding='utf-8'))['EB']['Gamma_LS']['H']
    rap.append(h['Gamma_pondere'] / h['Gamma_LS'])
chk('C11 la largeur ponderee du gel M17 vaut 5e+03 a 5e+06 fois Gamma_LS aux six points (gel 7, repris au v2)',
    min(rap) >= 5e3 and max(rap) <= 5e6, 'rapports %s' % ['%.2e' % x for x in rap])

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
