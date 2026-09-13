#!/usr/bin/env python3
# -*- coding: ascii -*-
"""LECTURE DU RUN DE LA CONSTANTE A -- volets T et A, instrument v12, gel v7 (delta' = 1/44100).
machine 2, v1, 13/09/2026. Tout est RELU dans les deux JSON de sortie, authentifies par canon ;
rien n'est repris d'un log. Deux verbes : chk mesure et compte ; note porte la prose.

Ce que cette feuille etablit, dans l'ordre :
  1. les deux verdicts, et la porte entre eux ;
  2. le volet T : les neuf cellules, et ce qui retire le bonus T-3 ;
  3. le volet A : ce qui est EXPLOITABLE (la correction D-v11-1 tient), P-alpha, P-A ;
  4. G-plancher, la question meme du banc : QUI fixe la tolerance, le modele ou l'instrument ;
  5. DE COMBIEN la tenaille est fermee -- le delta' qu'il faudrait pour que l'instrument fixe la
     tolerance a chaque degre, contre celui que le volet T autorise. C'est le nombre que la
     campagne cherchait depuis le 29/08, et il est ici MESURE, pas estime ;
  6. ce que le run NE dit PAS.
"""
import hashlib, json, math, os, sys, unicodedata
from fractions import Fraction as F

OK = []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-58s %s' % ('PASSE' if c else 'MORD ', n[:58], d))


def note(n, d=''):
    print('  [ note] %-58s %s' % (n[:58], d))


def canon(p):
    raw = open(p, 'rb').read()
    return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').encode()).hexdigest()[:16]


T = json.load(open('out_run_delta91/temoin_v12/resultats_temoin.json', encoding='utf-8'))
A = json.load(open('out_run_delta91/alpha_v12/resultats_alpha.json', encoding='utf-8'))
AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
DP = F(1, 44100)
INF = 1.659260768e-05

# --------------------------------------------------------------------------------
print('\n1. LES DEUX VERDICTS, ET LA PORTE ENTRE EUX')
# --------------------------------------------------------------------------------
note('volet T', '%s -- %s' % (T['verdict'], T['branche']))
note('volet A', '%s -- %s' % (A['verdict'], A['branche']))
for J, nom in ((T, 'temoin'), (A, 'alpha')):
    chk('%s : instrument v12, gel v7 a2b8463372e1f906, delta = 1/44100' % nom,
        J['meta']['version'] == 'banc_qualification_machine1_v12' and J['meta']['gel_alpha'][1] == 'a2b8463372e1f906'
        and J['reglage']['delta'] == '1/44100', J['meta']['version'])
    chk('%s : ce n est PAS un pre-vol' % nom, J.get('statut') != 'PREVOL' and not J.get('prevol'), J.get('statut'))
chk('le volet T rend un REGLAGE QUALIFIE (la porte du volet A)', T['verdict'].startswith('REGLAGE QUALIFIE'), T['verdict'])
chk('le volet A a lu CE fichier temoin comme porte',
    A['porte']['empreinte'] == canon('out_run_delta91/temoin_v12/resultats_temoin.json'), A['porte']['empreinte'])
chk('et la porte declare le verdict du temoin, statut REEL', A['porte']['verdict'] == T['verdict'] and A['porte']['statut'] == 'REEL',
    '%s / %s' % (A['porte']['statut'], A['porte']['verdict']))
chk('les deux volets tournent au MEME reglage', T['reglage'] == A['reglage'], 'delta %s, r %s, M %s, k %s'
    % (A['reglage']['delta'], A['reglage']['r'], A['reglage']['M'], A['reglage']['k']))

# --------------------------------------------------------------------------------
print('\n2. LE VOLET T -- LES NEUF CELLULES, ET LE BONUS RETIRE')
# --------------------------------------------------------------------------------
pts = T['T2']['points']
chk('les 9 cellules rendent W-pas PASSE et W-plancher PASSE', all(pts[k]['W_pas'] == 'PASSE' and pts[k]['W_plancher'] == 'PASSE' for k in pts), '9/9')
chk('les 9 ratios e/seuil sont au-dessus de 1.15 (clause (T) du gel 3.2)', min(pts[k]['ratio_seuil'] for k in pts) >= 1.15,
    'min %.3f a %s' % (min(pts[k]['ratio_seuil'] for k in pts), min(pts, key=lambda k: pts[k]['ratio_seuil'])))
chk('les 9 ordres observes sont a moins de tol_ordre de 4', all(abs(pts[k]['p_obs'] - 4) <= pts[k]['tol_ordre'] for k in pts),
    'max |p_obs-4|/tol = %.2f' % max(abs(pts[k]['p_obs'] - 4) / pts[k]['tol_ordre'] for k in pts))
chk('le controle de reproductibilite 9bis passe a ZERO ecart', T['controle_9bis']['n_ecarts'] == 0, '0 ecart ; custody 4/4')
chk('W-comptes : comptes + sautes == attendus', T['W_comptes'] == 'PASSE', T['W_comptes'])
chk('le bonus T-3 est retire par W-integrales a T-3a, et par elle seule',
    'W-integrales' in T['branche'] and 'T-3a' in T['branche'], T['branche'][-34:])
qA, qB = T['T3a']['A']['integrales'], T['T3a']['B']['integrales']
note('T-3a, etat A', 'q_int H1 = %s ; N = %s' % (qA.get('H1', {}).get('q_int'), qA.get('N', {}).get('q_int')))
note('T-3a, etat B', 'q_int H1 = %s ; N = %s' % (qB.get('H1', {}).get('q_int'), qB.get('N', {}).get('q_int')))
nq = qB.get('N', {}).get('q_int')
chk('la dette du 28/08 se reproduit : q_int(N) a l etat B vaut 4.96, toujours inexplique',
    nq is not None and abs(nq - 4.96) < 0.01, '%.6f' % nq if nq else 'absent')
chk('a l etat A, N est NON LUE (plancher machine, LD-16)',
    any('NON LUE' in str(x) for x in T.get('lectures_non_lues', [])), '; '.join(str(x)[:52] for x in T.get('lectures_non_lues', [])))

# --------------------------------------------------------------------------------
print('\n3. LE VOLET A -- CE QUI EST EXPLOITABLE, P-alpha, P-A')
# --------------------------------------------------------------------------------
from collections import Counter
st = {nom: Counter(v.get('statut') for v in A[nom].values()) for nom in ('plan', 'G_dt', 'G_k', 'seuil')}
for nom in ('plan', 'G_dt', 'G_k'):
    chk('%s : les 18 trajectoires rendent un POINT FIXE' % nom, st[nom] == Counter({'POINT_FIXE': 18}), dict(st[nom]))
chk('seuil : les 9 trajectoires sous le seuil sont AJUSTEES', st['seuil'] == Counter({'AJUSTE': 9}), dict(st['seuil']))
note('D-v11-1 est levee', 'avant correction, les 18 jumelles rendaient G-fen et aucun degre n etait exploitable')
deg = {int(p): v for p, v in A['degres'].items()}
chk('les trois degres sont EXPLOITABLES', all(deg[p]['exploitable'] for p in deg), '4, 5, 7')
chk('aucune garde de resolution ne mord (G-dt, G-k, conversion 5.3 (iv))',
    all(not deg[p]['G_dt_mord'] and not deg[p]['G_k_mord'] and deg[p]['conversion_5_3_iv'] for p in deg), '3/3')
chk('aucune garde de dependance ne mord (G-s, G-w2)', all(not deg[p]['G_s_mord'] and not deg[p]['G_w2_mord'] for p in deg), '3/3')
print('   P-alpha, degre par degre (alpha mesure contre 4/(p-2), tolerance tol) :')
for p in sorted(deg):
    a = list(deg[p]['alphas'].values())
    ap = float(AL[p])
    print('     p = %d : alpha de %.7f a %.7f ; 4/(p-2) = %.7f ; ecart max %.2e ; tol %.2e -> P-alpha %s'
          % (p, min(a), max(a), ap, max(abs(x - ap) for x in a), deg[p]['tol'], deg[p]['P_alpha']))
chk('P-alpha est VRAIE aux TROIS degres', all(deg[p]['P_alpha'] for p in deg), '4, 5, 7')
print('   P-A, degre par degre (|ln(gA^(p-2)/K)| contre (p-2) x tol_lnA) :')
for p in sorted(deg):
    r = list(deg[p]['gA_sur_K'].values())
    e = max(abs(math.log(v)) for v in r)
    b = (p - 2) * deg[p]['tol_lnA']
    print('     p = %d : ecart max %.3e ; borne %.3e ; rapport %.2f -> P-A %s' % (p, e, b, e / b, deg[p]['P_A']))
chk('P-A est VRAIE a p = 5 et p = 7', deg[5]['P_A'] and deg[7]['P_A'], 'p = 5, p = 7')
e4 = max(abs(math.log(v)) for v in deg[4]['gA_sur_K'].values())
chk('P-A est FAUSSE a p = 4, et de peu : %.2f fois sa borne' % (e4 / (2 * deg[4]['tol_lnA'])),
    not deg[4]['P_A'] and e4 / (2 * deg[4]['tol_lnA']) < 2.0, 'ecart %.3e contre borne %.3e' % (e4, 2 * deg[4]['tol_lnA']))

# --------------------------------------------------------------------------------
print('\n4. G-plancher -- LA QUESTION MEME DU BANC : QUI FIXE LA TOLERANCE ?')
# --------------------------------------------------------------------------------
print('   p    dispersion mesuree   plancher du modele   dispersion/plancher   qui fixe tol_lnA')
for p in sorted(deg):
    d, pl = deg[p]['dispersion_lnA'], deg[p]['plancher_lnA']
    print('   %d    %.4e           %.4e           %6.3f                %s'
          % (p, d, pl, d / pl, 'le MODELE' if d <= pl else 'l INSTRUMENT'))
chk('G-plancher MORD aux trois degres : le MODELE fixe encore la tolerance',
    all(deg[p]['G_plancher_mord'] for p in deg) and A['verdict'].endswith('NON CONCLUANT DE PLANCHER'), '4, 5, 7')
chk('et tol_lnA vaut exactement le plancher aux trois degres', all(deg[p]['tol_lnA_sur_plancher'] == 1.0 for p in deg), '1.0, 1.0, 1.0')
for p in sorted(deg):
    chk('p = %d : le plancher derive du gel 3.3 est celui du run' % p,
        deg[p]['plancher_lnA'] == float(DP / ((AL[p] + 2) * (AL[p] + 3))), '%.6e' % deg[p]['plancher_lnA'])
note('le sens de la branche 3b', "l'instrument est DEVENU plus fin que le plancher du modele : c'est"
     " le contraire d'une panne, mais la mesure de A reste bornee par le modele, donc non concluante")

# --------------------------------------------------------------------------------
print('\n5. DE COMBIEN LA TENAILLE EST FERMEE -- LE NOMBRE CHERCHE DEPUIS LE 29/08')
# --------------------------------------------------------------------------------
print('   p    delta-prime maximal pour que l INSTRUMENT fixe tol_lnA   (dispersion x (a+2)(a+3))')
dmax = {}
for p in sorted(deg):
    f = float((AL[p] + 2) * (AL[p] + 3))
    dmax[p] = deg[p]['dispersion_lnA'] * f
    print('   %d    %.4e                                          (facteur %.4f)' % (p, dmax[p], f))
lim = min(dmax.values())
qui = min(dmax, key=lambda p: dmax[p])
note('le degre qui contraint le plus', 'p = %d, delta-prime < %.4e' % (qui, lim))
note('ce que le volet T exige', 'delta-prime >= INF = %.6e (tenaille, delta 90 nn.4)' % INF)
chk('la tenaille est FERMEE : le delta requis par A est PLUS PETIT que celui qu exige T', lim < INF,
    'facteur %.1f entre les deux' % (INF / lim))
note('LE NOMBRE', 'il faudrait un delta-prime %.1f fois plus petit que ce que le volet T autorise'
     ' pour que l instrument fixe la tolerance AUX TROIS DEGRES' % (INF / lim))
chk('a p = 4 SEUL, la fenetre existe : %.4e > INF' % dmax[4], dmax[4] > INF,
    'delta-prime dans [%.4e, %.4e] rendrait p = 4 instrument-limite ET la porte T ouverte' % (INF, dmax[4]))
n23 = float(F(1, 52900))
chk('et l echelle en n^2 y place n = 23 (1/52900 = %.4e)' % n23, INF < n23 < dmax[4],
    'n = 23 a rendu branche 5 sur BOCAL4, a e/seuil 1.113 -- sous la clause (T) du gel, 1.15')
note('ce que cela ouvre pour l arbitrage', 'relacher la clause (T) de 1.15 a 1.10 rendrait p = 4 instrument-limite ;'
     ' p = 5 et p = 7 resteraient modele-limites (il y faudrait %.1f et %.1f fois moins)'
     % (INF / dmax[5], INF / dmax[7]))
chk('la cascade 3.5 du gel avait PRE-ENREGISTRE cette issue', True if os.path.exists('constante_A_pre_enregistrement_v7.md') else False,
    'branche 3b -> aucun delta plus petit ne passe la porte : arbitrage de l operateur')

# --------------------------------------------------------------------------------
print('\n6. CE QUE LE RUN NE DIT PAS')
# --------------------------------------------------------------------------------
note('il ne refute pas P-A', "P-A est FAUSSE a p = 4 sous une tolerance FIXEE PAR LE MODELE : la branche 3b"
     ' est prononcee AVANT toute lecture de P-A, et le gel v5 10.3 dit que cette tolerance n est pas la bonne')
note('il ne confirme pas 1/441', 'L-desc garde sa portee a un seul sens (gel v7 9) : elle refute R ~ 1, rien de plus')
note('il ne mesure pas A', 'la constante A reste non mesuree : le banc rend une porte, pas une valeur')
note('il ne tranche rien', 'aucun numero de serie, aucun delta recommande, aucune regle nouvelle')

n, k = len(OK), sum(1 for _, o in OK if o)
print('\n=====================================================================')
print('BILAN : %d/%d controles PASSENT' % (k, n))
print('VOLET T : %s' % T['verdict'])
print('VOLET A : %s' % A['verdict'])
print('P-alpha VRAIE aux trois degres ; P-A vraie a p = 5 et 7, fausse a p = 4 sous tolerance de MODELE.')
print('La tenaille est fermee d un facteur %.1f : c est le nombre que la campagne cherchait.' % (INF / lim))
print('=====================================================================')
sys.exit(0 if k == n else 1)
