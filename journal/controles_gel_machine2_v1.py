# -*- coding: ascii -*-
"""CONTROLES DE MACHINE 2 sur le gel "LA CHAINE E-A PAR ETAT, HORS PLAGE" (9df2702af59adbbc) : ce qui se lit sans rien jouer.
Chaque controle dit TIENT ou MORD ; les nombres viennent des pieces, jamais tapes. Usage depuis BOCAL4 :
python -P chaine_EA_par_etat/controles_gel_machine2_v1.py  > chaine_EA_par_etat/controles_gel_machine2_v1.log"""
import hashlib
import importlib.util
import os
import re
import sys
import unicodedata
import zipfile
from fractions import Fraction as F

RAC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(RAC)
D = 'chaine_EA_par_etat'
LOT = 'lot_machine1_2026-11-14_gel_chaine_EA_par_etat_v1_recu.zip'
MAN = 'MANIFEST_lot_machine1_gel_chaine_EA_par_etat_v1.txt'
REG = os.environ.get('REGISTRE_CLONE', '')
CHK = []


def emp(raw):
    try:
        t = unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()
        return hashlib.sha256(t).hexdigest()[:16], hashlib.sha256(raw).hexdigest()[:16], len(t), len(raw)
    except UnicodeDecodeError:
        h = hashlib.sha256(raw).hexdigest()[:16]
        return h, h, len(raw), len(raw)


def chk(nom, ok, msg):
    CHK.append((nom, bool(ok)))
    print('%s %-6s %s' % (nom, 'TIENT' if ok else 'MORD', msg), flush=True)


def lit(p):
    return open(p, encoding='utf-8').read()


GEL = lit(os.path.join(D, 'gel_chaine_EA_par_etat_pre_enregistrement_v1.md'))
SONDE = lit(os.path.join(D, 'sonde_chaine_par_etat_machine1_v1.py'))
sp = importlib.util.spec_from_file_location('feuille', os.path.join(D, 'lecture_chaine_par_etat_machine1_v1.py'))
FE = importlib.util.module_from_spec(sp)
sp.loader.exec_module(FE)
FSRC = lit(os.path.join(D, 'lecture_chaine_par_etat_machine1_v1.py'))

# C01 : le lot
z = zipfile.ZipFile(LOT)
man_raw = open(MAN, 'rb').read()
canon_lot = emp(man_raw)[0]
att = {}
for l in man_raw.decode('utf-8').split('\n'):
    p = l.split()
    if len(p) == 5 and re.fullmatch(r'[0-9a-f]{16}', p[0]):
        att[p[4]] = (p[0], p[1], int(p[2]), int(p[3]))
ecarts = [n for n in att if emp(z.read(n)) != att[n]]
chk('C01', canon_lot == 'b3d3e23e98914a95' and not ecarts and sorted(att) == sorted(n for n in z.namelist() if not n.startswith('MANIFEST_')),
    'lot %s (annonce b3d3e23e98914a95) ; %d pieces sur %d au canon, a l empreinte brute et aux deux tailles ; ecarts %s' % (canon_lot, len(att) - len(ecarts), len(att), ecarts))

# C02 : reconstruction du gel
rl = lit(os.path.join(D, 'reconstruction_gel_machine2.log'))
chk('C02', 'canon 9df2702af59adbbc' in rl and 'OCTET POUR OCTET' in rl, 'gel reconstruit depuis le gabarit et les canons des pieces : identique a l octet')

# C03 : les canons cites par le gel se resolvent chez moi
cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', GEL)) - {'9df2702af59adbbc'})
idx = {}


def noter(raw, nom):
    idx.setdefault(emp(raw)[0], nom)


SP = os.environ.get('SCRATCH_LOTS', '')
for base, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git')]
    for f in files:
        p = os.path.join(base, f)
        try:
            if os.path.getsize(p) > 8 * 1024 * 1024:
                continue
            raw = open(p, 'rb').read()
        except OSError:
            continue
        noter(raw, p.replace('\\', '/'))
        if f.endswith('.zip'):
            try:
                zz = zipfile.ZipFile(p)
                for n in zz.namelist():
                    noter(zz.read(n), p.replace('\\', '/') + '::' + n)
            except Exception:
                pass
if REG:
    for base, dirs, files in os.walk(REG):
        dirs[:] = [d for d in dirs if d != '.git']
        for f in files:
            noter(open(os.path.join(base, f), 'rb').read(), 'REGISTRE/' + os.path.relpath(os.path.join(base, f), REG).replace('\\', '/'))
non = [c for c in cites if c not in idx]
chk('C03', not non, '%d canons cites par le gel (hors le sien), tous resolus chez moi vers une piece du meme contenu ; non resolus : %s' % (len(cites), non))
for c in cites:
    print('        %s  %s' % (c, idx.get(c)))

# C04 : les douze points : gel section 4 == sonde == feuille
tab = {}
for m in re.finditer(r'^\s+([JTA]\d)\s+w2 = (\d+)/(\d+)\s+facteur (\d+)(?:/(\d+))?', GEL, re.M):
    pid, a, b, fa, fb = m.groups()
    tab[pid] = (a + '/' + b, fa + '/' + (fb or '1'))
pts_sonde = {}
for m in re.finditer(r'\("([JTA]\d)", "(\w+)", F\((\d+), (\d+)\), F\((\d+)(?:, (\d+))?\)\)', SONDE):
    pid, role, a, b, fa, fb = m.groups()
    pts_sonde[pid] = (role, a + '/' + b, fa + '/' + (fb or '1'))
ok4 = (len(tab) == 12 and len(pts_sonde) == 12 and all(tab[p] == pts_sonde[p][1:] for p in tab) and
       all(FE.ATTENDUS[p][1:] == tab[p] for p in tab) and all(FE.ATTENDUS[p][0] == pts_sonde[p][0] for p in tab))
chk('C04', ok4, 'les douze points (w2, facteur) : gel section 4 (%d lus), POINTS de la sonde (%d), ATTENDUS de la feuille (%d) : identiques, roles compris'
    % (len(tab), len(pts_sonde), len(FE.ATTENDUS)))

# C05 : boites attendues, par ma propre mesure sans diagonalisation, contre le gel et le journal de conception de machine 1
bl = lit(os.path.join(D, 'boites_attendues_machine2_v1.log'))
N_m2 = {}
for m in re.finditer(r'^(\w\d) w2=(\S+)\s+x(\S+)\s+g_regle=\S+ g=\S+ s=\S+ graine=\([^)]*\) card_b=\d+ r_c=(\d+) N=(\d+) faisable=(\w+)', bl, re.M):
    N_m2[m.group(1)] = (int(m.group(5)), m.group(6) == 'True')
ch = lit(os.path.join(D, 'conception_points_chaine_seule_machine1_v1.log'))
N_m1 = {}
for m in re.finditer(r'^w2=(\S+)\s+x(\S+)\s+g=\S+ graine=\([^)]*\) card=\d+ Lambda=\S+ r_c=\d+ N=(\d+)', ch, re.M):
    N_m1[(m.group(1), m.group(2))] = int(m.group(3))
acc = True
for pid, (w, f) in tab.items():
    f1 = f.replace('/1', '') if f.endswith('/1') else f
    if N_m1.get((w, f1)) != N_m2[pid][0]:
        acc = False
juges = {p: N_m2[p][0] for p in ('J1', 'J2', 'J3', 'J4', 'J5', 'J6')}
chk('C05', acc and min(juges, key=juges.get) == 'J3' and max(juges, key=juges.get) == 'J6' and juges['J3'] == 54 and juges['J6'] == 74
    and all(v[1] for v in N_m2.values()) and 'N de 54 (J3) a 74 (J6)' in GEL.replace('\n', ' ').replace('  ', ' '),
    'boites N recalculees par moi (douze points, sans diagonalisation) = celles du journal de conception de machine 1 ; juges : %s ; gel : "N de 54 (J3) a 74 (J6)" ; tous faisables'
    % juges)

# C06 : les affirmations chiffrees de la section 4 du gel sur la chaine seule, lues dans le journal de conception
vide = {}
for m in re.finditer(r'^w2=(\S+)\s+x(\S+)\s+.*?modal \((\d+),(\d+)\) Gamma_chaine=(\S+) \| (\d+)/(\d+) etats .*?, (\d+) a barriere vide', ch, re.M):
    vide[(m.group(1), m.group(2))] = (m.group(5), int(m.group(8)), int(N_m1[(m.group(1), m.group(2))]))
v2 = [vide[('39/20', '2')][1], vide[('41/20', '2')][1]]
v3 = [vide[('39/20', '3')][1], vide[('41/20', '3')][1]]
mod_demi = vide[('39/20', '1/2')][0]
ok6 = (min(v2) == 10 and max(v2) == 14 and min(v3) == 15 and max(v3) == 18 and float(mod_demi) < 1.33e-12 and
       {vide[('39/20', '1/2')][2], vide[('41/20', '1/2')][2]} == {87, 88})
chk('C06', ok6, 'section 4 du gel sur la chaine seule : facteur 2, sites sans barriere %s (gel : de 10 a 14) ; facteur 3 : %s (de 15 a 18) ; facteur 1/2 a 1.95 : '
    'etat modal %s sous 1.33e-12, boites N 87 et 88' % (v2, v3, mod_demi))

# C07 : constantes de la feuille et de la sonde == nombres du gel
cst = [('SIGMA_J_MAX', FE.SIGMA_J_MAX, 0.2, 'ecart-type de J < 0.2'), ('POIDS_SITE_MIN', FE.POIDS_SITE_MIN, 0.5, 'poids sur le site (n1, n2) >= 0.5'),
       ('DIX_PLANCHERS', FE.DIX_PLANCHERS, 1.33e-12, 'Gamma_2D(3) > 1.33e-12'), ('SUIVI_MIN', FE.SUIVI_MIN, 0.9, 'recouvrements de suivi >= 0.9'),
       ('STABILITE_CIBLE', FE.STABILITE_CIBLE, 2.0, 'max / min de Gamma_2D sur k = 2, 3, 4 <= 2'),
       ('ETALEMENT_CHAINE', FE.ETALEMENT_CHAINE, 2.0, 'max / min de ses quatre valeurs <= 2'), ('MIN_JUGES', FE.MIN_JUGES, 6, 'moins de 6 etats juges'),
       ('MIN_POINTS_LISIBLES', FE.MIN_POINTS_LISIBLES, 4, 'moins de 4 des 6'), ('TOL_ANCRE', FE.TOL_ANCRE, 1e-2, 'a 1e-2 pres'),
       ('N_ETATS', FE.N_ETATS, 14, 'les 14 etats')]
mauv = [n for (n, v, att_, phrase) in cst if v != att_ or phrase not in re.sub(r'\s+', ' ', GEL)]
refA = (FE.ANCRES['A1'][1], FE.ANCRES['A2'][1])
chk('C07', not mauv and refA == (2.1623273017950654e-10, 2.6613925716641374e-09) and '2.1623273017950654e-10' in GEL and '2.6613925716641374e-09' in GEL,
    '%d constantes de la feuille (%s) egales aux nombres du gel, phrase par phrase ; les deux ancres du gel egales a celles de la feuille ; mauvaises : %s'
    % (len(cst), ', '.join(n for n, _, _, _ in cst), mauv))
ok7b = all(s in SONDE for s in ('FRACTION, L_BOITE, N_ETATS = 0.70, 20, 14', 'KS = (2, 3, 4)', 'EF_CHAINE = (0.25, 0.125, 0.0625, 0.03125)',
                                  'M_facteur=4', 'gammas'))
chk('C08', ok7b and 'q = e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]' in FSRC,
    'sonde : fraction 0.70, L = 20, 14 etats, k = 2, 3, 4, quatre eta de chaine 1/4..1/32, M_facteur 4 ; feuille : q = gammas[2] (facteur 1/16) / Gamma_2D(3)')

# C09 : ordre des criteres et paliers
ordre = ['SIGMA_J_MAX', 'POIDS_SITE_MIN', 'DIX_PLANCHERS', 'SUIVI_MIN', 'STABILITE_CIBLE']
pos = [FSRC.index(o, FSRC.index('def motif_exclusion')) for o in ordre]
chk('C09', pos == sorted(pos) and FE.palier(0.5) == 'FACTEUR 2' and FE.palier(2.0) == 'FACTEUR 2' and FE.palier(0.4999) == 'DECADE' and FE.palier(3.16) == 'DECADE'
    and FE.palier(3.17) == 'HORS DECADE' and FE.palier(0.3162) == 'HORS DECADE' and FE.palier(0.3163) == 'DECADE',
    'feuille : criteres (1) a (6) dans l ordre du gel ; paliers : [1/2, 2] ferme, demi-decade 0.3162 a 3.1623')

# C10 : texte du gel
lg = max(len(l) for l in GEL.split('\n'))
chk('C10', all(ord(c) < 128 for c in GEL) and '%' not in GEL and lg <= 100 and GEL.rstrip().endswith('-- FIN gel_chaine_EA_par_etat_pre_enregistrement_v1 --'),
    'gel ASCII, sans pour cent, plus longue ligne %d, ligne de FIN' % lg)

# C11 : annonces : somme des probabilites de A-1
pr = [float(x) for x in re.findall(r'(?:TENU EN PARTIE|ORDRE DE GRANDEUR TENU HORS PLAGE|NON CONCLUANT\s+D\'INSTRUMENT|NON LISIBLE|NON TENU)\s+(0\.\d\d)', GEL)]
chk('C11', len(pr) == 5 and abs(sum(pr) - 1.0) < 1e-9, 'annonce A-1 : cinq issues, probabilites %s, somme %.2f' % (pr, sum(pr)))

nm = sum(1 for _, ok in CHK if not ok)
print('BILAN : %d controles, %d mordent : %s' % (len(CHK), nm, [n for n, ok in CHK if not ok]))
