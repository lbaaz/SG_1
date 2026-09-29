"""certif_run_delta92_machine2_v1.py -- machine 2, 2026-09-29.

CERTIFICATION DU RUN delta 92, joue sur BOCAL4 sous l'instrument v15 (a1553f6eb5cc74b8) et le
gel v9 (b515abc5a6da73c5), tous deux certifies des deux cotes ; E19 levee ; declenchement
operateur du 29/09.

C'est LE PREMIER RUN OU LA P-A CORRIGEE EXISTE. Cette piece etablit, dans cet ordre :
  1. le run porte les TROIS niveaux de pas -- sans G_dt4, q ne se mesure pas et toute la lecture
     corrigee tombe en NON JOUEE par consigne (D-essai-1) : la P-A corrigee n'existerait pas ;
  2. les comptes du run egalent les 108 que le gel ecrit et que l'instrument derive ;
  3. la lecture corrigee est JOUEE : q mesure dans [3, 5] aux points lus, lnA_R present, S(p) et
     plancher_corr calcules, et les points NON LUS enumeres avec leur motif ;
  4. G-plancher sur le COUPLE CORRIGE ne mord pas -- et le rapport tol_lnA/plancher_corr est
     confronte aux 1.7e+04 a 2.1e+05 que ma certification du v9/v15 avait PREDITS ;
  5. les grandeurs du v14 sont conservees sous v14_* et lisibles a cote ;
  6. le plancher corrige du run est RE-DERIVE ici par ma forme close, jamais lu du run.
Elle ne lit PAS les deux predictions : c'est lecture_v9 --predictions qui les joue, et sa sortie
est certifiee a part. Deux verbes : chk (peut mordre), note (ne peut pas).
Usage : certif_run_delta92_machine2_v1.py <repertoire du volet alpha> [<repertoire du volet temoin>]
"""
import hashlib
import json
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

ALPHA = sys.argv[1] if len(sys.argv) > 1 else 'out_run_delta92/alpha_v15'
TEMOIN = sys.argv[2] if len(sys.argv) > 2 else 'out_run_delta92/temoin_v15'
V9, B15 = 'constante_A_pre_enregistrement_v9.md', 'banc_qualification_machine1_v15.py'
DERJ = 'derivation_second_ordre_machine2_v1.json'
CANON = {V9: 'b515abc5a6da73c5', B15: 'a1553f6eb5cc74b8', DERJ: 'b70fca94d72822ad'}
W2S = ('1.73', '2.27', '2.80')
C_PLAN = ('1.05', '1.20')
DEGRES = (4, 5, 7)
PROJ4 = 0.2238
DP = F(1, 32400)
lignes, bilan = [], {'chk': 0, 'mord': []}


def out(s=''):
    print(s)
    lignes.append(s)


def chk(nom, cond, detail=''):
    bilan['chk'] += 1
    if not cond:
        bilan['mord'].append(nom)
    out('  [chk %s] %s%s' % ('PASSE' if cond else 'MORD ', nom, (' -- ' + detail) if detail else ''))
    return cond


def note(nom, detail):
    out('  [note] %s -- %s' % (nom, detail))


def B(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


def coeffs(p, w2):
    """MA forme close de c1 et c2 -- retapee, jamais lue du run ni de machine 1"""
    a = F(4, p - 2)
    w = F(w2)
    K = a * (a + 1) * (a + 2) * (a + 3)
    P2 = a * (a + 1) * (a - 1) * (a - 2)
    P4 = (4 - a) * (3 - a) * (2 - a) * (1 - a)
    c1 = (1 + w * w) * a * (a + 1) / ((p - 1) * K - P2)
    c2 = (K * F((p - 1) * (p - 2), 2) * c1 * c1 - (1 + w * w) * c1 * (2 - a) * (1 - a) - w * w) / (P4 - (p - 1) * K)
    return c1, c2


def plancher_corr(p):
    return PROJ4 * max(abs(float(coeffs(p, w2)[1])) * (float(DP) / (1 + float(w2) ** 2)) ** 2 for w2 in W2S)


out('CERTIFICATION MACHINE 2 DU RUN delta 92 (instrument v15, gel v9)')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out('volet alpha : %s' % ALPHA)
out('volet temoin : %s' % TEMOIN)
out()
out('0. ANCRES, PROVENANCE, INTEGRITE DU DEPOT DU RUN')
for f in sorted(CANON):
    chk('canon %s' % f, os.path.isfile(f) and B(f) == CANON[f], B(f) if os.path.isfile(f) else 'absent')
JA = os.path.join(ALPHA, 'resultats_alpha.json')
if not chk('0.1 : le volet alpha a depose son JSON', os.path.isfile(JA), JA):
    out()
    out('ARRET : sans le JSON du volet alpha il n y a rien a certifier.')
    sys.exit(1)
ra = json.load(open(JA, encoding='utf-8'))
note('0.2 empreinte B du JSON alpha', B(JA))
for nom, f in (('journal alpha', os.path.join(ALPHA, 'journal_alpha.txt')),
               ('MANIFEST du volet alpha', os.path.join(ALPHA, 'MANIFEST.sha256'))):
    chk('0.3 %s present' % nom, os.path.isfile(f), B(f) if os.path.isfile(f) else 'absent')
man = os.path.join(ALPHA, 'MANIFEST.sha256')
if os.path.isfile(man):
    faux, compte = [], 0
    for l in open(man, encoding='utf-8'):
        if not l.strip():
            continue
        h, n = l.split()
        n = n.lstrip('*')
        q = os.path.join(ALPHA, n)
        compte += 1
        if not os.path.isfile(q) or hashlib.sha256(open(q, 'rb').read()).hexdigest() != h:
            faux.append(n)
    chk('0.4 : les %d series du volet alpha sont au sha256 de son propre MANIFEST' % compte,
        not faux, 'en ecart ou absentes : %s' % (faux[:4] or 'aucune'))
# le canon de l instrument et le pin du gel se lisent au JOURNAL, aux lignes qui les portent
# (N-59 pour le script, E19 pour les gels) -- pas dans meta, dont la composition varie.
tj = open(os.path.join(ALPHA, 'journal_alpha.txt'), encoding='utf-8', errors='replace').read()     if os.path.isfile(os.path.join(ALPHA, 'journal_alpha.txt')) else ''
mN59 = re.search(r'N-59\s+(\S+)\s+\d+ o\s+sha256 brut ([0-9a-f]{16})', tj)
chk('0.5 : le journal du run declare l instrument v15 a son canon',
    mN59 is not None and mN59.group(2) == CANON[B15] and mN59.group(1).endswith(B15),
    mN59.group(0)[:90] if mN59 else 'ligne N-59 introuvable')
mE19 = re.search(r'E19\s+gels/%s\s+([0-9a-f]{16})' % re.escape(V9), tj)
chk('0.6 : et le gel v9 est CONCORDANT au pin',
    mE19 is not None and mE19.group(1) == CANON[V9] and 'CONCORDANT' in tj[mE19.start():mE19.start() + 200],
    mE19.group(0)[:90] if mE19 else 'ligne E19 du gel v9 introuvable')

# ---------------------------------------------------------------- 1. LES TROIS NIVEAUX
out()
out('1. LES TROIS NIVEAUX DE PAS -- LA CONDITION D EXISTENCE DE LA P-A CORRIGEE')
etages = {k: len(ra.get(k, {})) for k in ('plan', 'G_dt', 'G_dt4', 'G_k')}
note('1.1 etages deposes', str(etages))
for k in ('plan', 'G_dt', 'G_dt4'):
    chk('1.1 %s : 18 cellules' % k, etages.get(k) == 18, str(etages.get(k)))
chk('1.2 : G_dt4 est PRESENT -- sans lui la lecture corrigee tombe en NON JOUEE',
    etages.get('G_dt4') == 18, '%s cellule(s)' % etages.get('G_dt4'))
chk('1.3 : les cellules du plan portent l ajustement corrige (lnA_M)',
    all(((ra['plan'].get(c) or {}).get('ajustement_corrige') or {}).get('lnA_M') is not None
        for c in ra.get('plan', {})),
    '%d/%d cellules du plan avec lnA_M'
    % (sum(1 for c in ra.get('plan', {}) if ((ra['plan'][c] or {}).get('ajustement_corrige') or {}).get('lnA_M') is not None),
       len(ra.get('plan', {}))))

# ---------------------------------------------------------------- 2. LES COMPTES
out()
out('2. LES COMPTES DU RUN CONTRE LES 108 DU GEL')
n_att = 18 * 4 + 9 + 27
chk('2.1 : le run derive bien 108 attendus (18x4 + 9 + 27), le compte que le gel ECRIT',
    ra.get('attendus_total') == n_att == 108,
    'attendus_total du run %s | je derive %d' % (ra.get('attendus_total'), n_att))
note('2.2 comptes du run', str(ra.get('comptes'))[:200])
note('2.3 G_comptes', str(ra.get('G_comptes'))[:200])
chk('2.4 : la garde de comptes du run ne mord pas',
    ra.get('G_comptes') in (True, 'PASSE', None) or not re.search(r'MORD', str(ra.get('G_comptes'))),
    str(ra.get('G_comptes'))[:120])

# ---------------------------------------------------------------- 3. LA LECTURE CORRIGEE
out()
out('3. LA LECTURE CORRIGEE EST-ELLE JOUEE ?')
deg = ra.get('degres', {})
chk('3.0 : les trois degres sont depouilles', sorted(int(p) for p in deg) == list(DEGRES), str(sorted(deg)))
jouee = {}
for p in DEGRES:
    D = deg.get(str(p), {})
    nonjouee = D.get('lecture_corrigee')
    S_p = D.get('S_p')
    jouee[p] = S_p is not None
    if nonjouee:
        note('3.1 p=%d LECTURE CORRIGEE NON JOUEE' % p, str(nonjouee)[:200])
    chk('3.1 p=%d : la lecture corrigee est JOUEE (S(p) existe)' % p, S_p is not None,
        'S_p = %s' % ('%.4e' % S_p if isinstance(S_p, (int, float)) else S_p))
    q = D.get('q_mesure', {}) or {}
    nl = D.get('points_non_lus', []) or []
    note('3.2 p=%d q mesure' % p, '%d point(s) ; %s' % (len(q), sorted('%.3f' % v for v in q.values())))
    chk('3.2 p=%d : tout q mesure est dans [3, 5]' % p,
        all(3.0 <= v <= 5.0 for v in q.values()) if q else False,
        'hors bornes : %s' % [k for k, v in q.items() if not 3.0 <= v <= 5.0])
    chk('3.3 p=%d : les six points sont LUS (aucun non lu)' % p, len(nl) == 0,
        '%d non lu(s) : %s' % (len(nl), nl[:3]))
    chk('3.4 p=%d : lnA_R present aux six points' % p, len(D.get('lnA_R', {}) or {}) == 6,
        '%d point(s)' % len(D.get('lnA_R', {}) or {}))
    chk('3.5 p=%d : le modele est celui que le gel ecrit (M1 aux degres 4 et 5, M2 au 7)' % p,
        str(D.get('modele')) == ('M2' if p == 7 else 'M1'), str(D.get('modele')))

# ---------------------------------------------------------------- 4. G-PLANCHER, LE POINT DE FOND
out()
out('4. G-PLANCHER SUR LE COUPLE CORRIGE -- CE QUE MA CERTIFICATION AVAIT PREDIT')
PRED = {4: (1.2e5, 2.1e5), 5: (3.4e4, 5.7e4), 7: (1.7e4, 2.5e4)}
for p in DEGRES:
    D = deg.get(str(p), {})
    mien = plancher_corr(p)
    sien = D.get('plancher_corrige')
    chk('4.1 p=%d : le plancher corrige du run == celui que JE re-derive' % p,
        isinstance(sien, (int, float)) and abs(sien / mien - 1) < 1e-12,
        'run %s | moi %.6e' % (('%.6e' % sien) if isinstance(sien, (int, float)) else sien, mien))
    if not jouee[p]:
        note('4.2 p=%d' % p, 'lecture corrigee NON JOUEE : G-plancher corrige ne se lit pas')
        continue
    S_p, tol = D.get('S_p'), D.get('tol_lnA')
    rap = (tol / sien) if (isinstance(tol, (int, float)) and sien) else float('nan')
    note('4.2 p=%d' % p, 'S(p) %.4e ; plancher_corr %.4e ; tol_lnA %.4e ; tol/plancher %.2e'
         % (S_p, sien, tol, rap))
    chk('4.3 p=%d : G-plancher sur le couple corrige NE MORD PAS' % p,
        D.get('G_plancher_mord') is False, 'G_plancher_mord = %s' % D.get('G_plancher_mord'))
    lo, hi = PRED[p]
    chk('4.4 p=%d : le rapport tol/plancher tombe dans ce que ma certification PREDISAIT (%.1e a %.1e)'
        % (p, lo, hi), lo / 3 <= rap <= hi * 3, 'mesure %.2e' % rap)
    note('4.5 p=%d contraste v14' % p, 'v14 : tol %s, G-plancher mord %s, P-A %s'
         % (('%.4e' % D['v14_tol_lnA']) if isinstance(D.get('v14_tol_lnA'), (int, float)) else D.get('v14_tol_lnA'),
            D.get('v14_G_plancher_mord'), D.get('v14_P_A')))
    chk('4.6 p=%d : les grandeurs du v14 sont CONSERVEES a cote (R-v8-1)' % p,
        'v14_tol_lnA' in D and 'v14_P_A' in D and 'v14_G_plancher_mord' in D)

# ---------------------------------------------------------------- 5. LA P-A ET LE VERDICT
out()
out('5. LA P-A CORRIGEE ET LE VERDICT DU RUN')
for p in DEGRES:
    D = deg.get(str(p), {})
    note('5.1 p=%d' % p, 'P-A corrigee %s | P-A du v14 %s' % (D.get('P_A'), D.get('v14_P_A')))
note('5.2 verdict du volet alpha', str(ra.get('verdict', ra.get('branche'))))
note('5.3 branche', str(ra.get('branche')))
note('5.4 porte du temoin', str(ra.get('porte'))[:200])
note('5.5 lectures non lues (global)', str(ra.get('lectures_non_lues'))[:200])
jt = os.path.join(TEMOIN, 'resultats_temoin.json')
if os.path.isfile(jt):
    rt = json.load(open(jt, encoding='utf-8'))
    note('5.6 verdict du volet temoin', str(rt.get('verdict', rt.get('branche'))))
    chk('5.7 : le volet alpha a bien lu la porte du temoin REEL',
        bool(ra.get('porte')), str(ra.get('porte'))[:100])
else:
    note('5.6 volet temoin', 'JSON absent : %s' % jt)

# ---------------------------------------------------------------- BILAN
out()
sortie = {'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']},
          'etages': etages,
          'planchers_re_derives': {str(p): plancher_corr(p) for p in DEGRES},
          'par_degre': {str(p): {'S_p': deg.get(str(p), {}).get('S_p'),
                                 'tol_lnA': deg.get(str(p), {}).get('tol_lnA'),
                                 'plancher_corrige': deg.get(str(p), {}).get('plancher_corrige'),
                                 'G_plancher_mord': deg.get(str(p), {}).get('G_plancher_mord'),
                                 'P_A': deg.get(str(p), {}).get('P_A'),
                                 'v14_P_A': deg.get(str(p), {}).get('v14_P_A'),
                                 'points_non_lus': deg.get(str(p), {}).get('points_non_lus')}
                        for p in DEGRES},
          'verdict_alpha': ra.get('verdict', ra.get('branche')),
          'portee': 'certification m2 du run delta 92 ; les deux predictions se lisent a part '
                    '(lecture_v9 --predictions)'}
with open('certif_run_delta92_machine2_v1.json', 'w', encoding='utf-8', newline='\n') as fh:
    json.dump(sortie, fh, sort_keys=True, ensure_ascii=True, indent=1, default=str)
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for nm in bilan['mord']:
    out('   MORD : %s' % nm)
with open('certif_run_delta92_machine2_v1.log', 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(lignes) + '\n')
print()
print('log convention B %s' % B('certif_run_delta92_machine2_v1.log'))
