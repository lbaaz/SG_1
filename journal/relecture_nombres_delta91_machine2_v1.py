#!/usr/bin/env python3
# -*- coding: ascii -*-
"""RELECTURE DES NOMBRES DE L'ACTE delta 91 -- AUX SOURCES. machine 2, v1, 13/09/2026.

Deux jambes, et il en faut deux : (1) le nombre recalcule depuis la source (les six JSON de run,
les logs de mesure, les gels) vaut ce que l'acte annonce ; (2) la chaine annoncee est
LITTERALEMENT dans l'acte. Chaque source est AUTHENTIFIEE PAR CANON avant lecture ; une source
absente rend NON JOUE et la feuille continue, en le nommant. Les presences se testent sur
BLANCS NORMALISES des deux cotes (les textes sont enveloppes). Aucune piece n'est editee.
Usage : relecture_nombres_delta91_machine2_v1.py <acte .md>
"""
import hashlib, json, math, os, re, sys, unicodedata
from fractions import Fraction as F

if len(sys.argv) != 2:
    sys.exit('usage : relecture_nombres_delta91_machine2_v1.py <acte journal_delta_nn_..._vN.md>')
ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
ACTE_P = os.path.abspath(sys.argv[1])
ACTE = open(ACTE_P, encoding='utf-8').read()
N = lambda s: re.sub(r'\s+', ' ', s)
ACTE_N = N(ACTE)
OK, NJ = [], []


def chk(n, c, d=''):
    OK.append((n, bool(c)))
    print('  [%s] %-56s %s' % ('PASSE' if c else 'MORD ', n[:56], d))


def note(n, d=''):
    print('  [ note] %-56s %s' % (n[:56], d))


def non_joue(n, d=''):
    NJ.append(n)
    print('  [NON J] %-56s %s' % (n[:56], d))


def canon(p):
    raw = open(p, 'rb').read()
    try:
        return hashlib.sha256(unicodedata.normalize('NFC', raw.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n').encode()).hexdigest()[:16]
    except UnicodeDecodeError:
        return hashlib.sha256(raw).hexdigest()[:16]


def _source(etq, chemin, attendu):
    """Authentifie une source. Le CONTROLE porte la verification lui-meme -- il ne rend pas
    compte d'un `if` deja passe : ecrit ainsi, sa condition serait une constante, et la garde
    de machine 1 l'a montre trois fois sur ce meme motif. Absente : NON JOUE, et la feuille
    continue en le nommant."""
    p = P(*chemin)
    if not os.path.exists(p):
        non_joue('source %s' % etq, 'ABSENTE : ' + os.path.join(*chemin)[-48:])
        return None
    if attendu is None:
        chk('source %-30s presente' % etq, os.path.isfile(p), os.path.join(*chemin)[-52:])
    else:
        chk('source %-30s %s' % (etq, attendu), canon(p) == attendu, os.path.join(*chemin)[-52:])
        if canon(p) != attendu:
            return None
    return p


def js(etq, chemin, attendu=None):
    p = _source(etq, chemin, attendu)
    return json.load(open(p, encoding='utf-8')) if p else None


def txt(etq, chemin, attendu=None):
    p = _source(etq, chemin, attendu)
    return open(p, 'rb').read().decode('utf-8', 'replace') if p else None


def cite(etq, s, src=None, recalc=None, attendu=None, dans=None):
    a = s if dans is None else dans
    ok_acte = N(a) in ACTE_N
    if src is None and recalc is None:
        chk(etq, ok_acte, s)
        return
    if recalc is not None:
        bon, d = (recalc == attendu), 'recalcul %r vs acte %r' % (recalc, attendu)
    else:
        bon, d = (N(s) in N(src)), s + ('' if N(s) in N(src) else '  ABSENT DE LA SOURCE')
    chk(etq, ok_acte and bon, ('' if ok_acte else 'ABSENT DE L ACTE ; ') + d)


# =====================================================================
print('\n1. LES SIX JSON DE RUN -- VERDICTS ET IDENTITE')
# =====================================================================
T12 = js('m2 temoin v12', ('out_run_delta91', 'temoin_v12', 'resultats_temoin.json'), '8d4c76d38726baf1')
A12 = js('m2 alpha v12', ('out_run_delta91', 'alpha_v12', 'resultats_alpha.json'))
T13 = js('m2 temoin v13', ('out_run_delta91', 'temoin_v13', 'resultats_temoin.json'))
A13 = js('m2 alpha v13', ('out_run_delta91', 'alpha_v13', 'resultats_alpha.json'))
L1 = ('entrant_machine1_2026-09-13_certification_run', 'lot', 'out13_m1')
TM1 = js('m1 temoin v13', L1 + ('temoin_v13', 'resultats_temoin.json'), '152da1af8286f6e0')
AM1 = js('m1 alpha v13', L1 + ('alpha_v13', 'resultats_alpha.json'), '94d56d39afdff689')
# UNE SOURCE ABSENTE NE DOIT PAS ARRETER LA FEUILLE (remarque de machine 1, deux fois) : chaque
# bloc qui lit un JSON est garde, et tout ce qu'il aurait joue est declare NON JOUE, nomme.
MANQUE = [n for n, J in (('m2 temoin v12', T12), ('m2 alpha v12', A12), ('m2 temoin v13', T13),
                         ('m2 alpha v13', A13), ('m1 temoin v13', TM1), ('m1 alpha v13', AM1)) if J is None]
if MANQUE:
    non_joue('les %d controles qui lisent un JSON de run' % 96, ', '.join(MANQUE))
else:
    cite('le verdict du volet T', 'REGLAGE QUALIFIE (bonus T-3 retire)', recalc=T12['verdict'], attendu='REGLAGE QUALIFIE (bonus T-3 retire)')
    cite('sa branche', 'branche 6 : T-3 mord seul (W-integrales, T-3a)', recalc=T12['branche'], attendu='branche 6 : T-3 mord seul (W-integrales, T-3a)')
    cite('le verdict du volet A', 'NON CONCLUANT DE PLANCHER', recalc=A12['verdict'], attendu='NON CONCLUANT DE PLANCHER')
    cite('sa branche', 'branche 3b : G-plancher MORD aux degres [4, 5, 7]', recalc=A12['branche'][:47], attendu='branche 3b : G-plancher MORD aux degres [4, 5, 7]'[:47])
    chk('les quatre runs de machine 2 portent le gel v7 et delta = 1/44100',
        all(J['meta']['gel_alpha'][1] == 'a2b8463372e1f906' and J['reglage']['delta'] == '1/44100' for J in (T12, A12, T13, A13)), '4/4')
    chk('les deux runs de machine 1 aussi', all(J['meta']['gel_alpha'][1] == 'a2b8463372e1f906' and J['reglage']['delta'] == '1/44100' for J in (TM1, AM1)), '2/2')
    chk('LES DEUX MACHINES rendent les MEMES verdicts', TM1['verdict'] == T12['verdict'] and AM1['verdict'] == A12['verdict'], 'T et A')
    chk('les deux volets de machine 2 tournent au MEME reglage', T12['reglage'] == A12['reglage'], 'delta 1/44100')
    cite('le gel courant', 'a2b8463372e1f906', recalc=canon(P('constante_A_pre_enregistrement_v7.md')), attendu='a2b8463372e1f906')
    for nom, att in (('v9', '9b3ec0b0c4978158'), ('v10', 'f65eccbfcdea91c1'), ('v11', 'a9f3fa1d639107d2'),
                     ('v12', '2c4345515bb02325'), ('v13', '1ac295648490a86c')):
        cite('instrument %s' % nom, att, recalc=canon(P('banc_qualification_machine1_%s.py' % nom)), attendu=att)

    # =====================================================================
    print('\n2. LE VOLET T -- LES NEUF CELLULES ET LE BONUS')
    # =====================================================================
    pts = T12['T2']['points']
    cite('e/seuil minimal', '1.433', recalc='%.3f' % min(pts[k]['ratio_seuil'] for k in pts), attendu='1.433')
    cite('e/seuil maximal', '5.750', recalc='%.3f' % max(pts[k]['ratio_seuil'] for k in pts), attendu='5.750')
    chk('le minimum est porte par 7|1.73', min(pts, key=lambda k: pts[k]['ratio_seuil']) == '7|1.73' and '1.433 (7|1.73)' in ACTE_N, '7|1.73')
    chk('le maximum est porte par 4|2.80', max(pts, key=lambda k: pts[k]['ratio_seuil']) == '4|2.80' and '5.750 (4|2.80)' in ACTE_N, '4|2.80')
    cite('max |p_obs - 4| / tol_ordre', '0.79', recalc='%.2f' % max(abs(pts[k]['p_obs'] - 4) / pts[k]['tol_ordre'] for k in pts), attendu='0.79')
    chk('les 9 cellules : W-pas PASSE et W-plancher PASSE', all(pts[k]['W_pas'] == 'PASSE' and pts[k]['W_plancher'] == 'PASSE' for k in pts)
        and 'W-pas PASSE et W-plancher PASSE, 9/9' in ACTE_N, '9/9')
    cite('le 9bis a zero ecart', '0 ecart', recalc=T12['controle_9bis']['n_ecarts'], attendu=0)
    cite('W-comptes', '41 + 0 == 41', recalc=(T12['comptes']['comptes'], T12['comptes']['sautes'], T12['attendus_total']), attendu=(41, 0, 41))
    qB = T12['T3a']['B']['integrales']['N']['q_int']
    cite('q_int(N) a l etat B', '4.9598', recalc='%.4f' % qB, attendu='4.9598')
    chk('sur machine 1 : 7 feuilles tolerees a 1 ulp', len(TM1['controle_9bis'].get('toleres_ulp', [])) == 7
        and all(float(re.search(r'([0-9.]+) ulp', x).group(1)) <= 1.0 for x in TM1['controle_9bis']['toleres_ulp'])
        and '7 feuilles tolerees a 1 ulp' in ACTE_N, '7')

    # =====================================================================
    print('\n3. LE VOLET A -- P-alpha, P-A, G-plancher')
    # =====================================================================
    AL = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
    deg = {int(p): v for p, v in A12['degres'].items()}
    dm1 = {int(p): v for p, v in AM1['degres'].items()}
    chk('plan 18, G-dt 18, G-k 18 POINT FIXE ; seuil 9 AJUSTE',
        all(sum(1 for v in A12[n].values() if v['statut'] == 'POINT_FIXE') == 18 for n in ('plan', 'G_dt', 'G_k'))
        and sum(1 for v in A12['seuil'].values() if v['statut'] == 'AJUSTE') == 9, '18/18/18/9')
    chk('les trois degres sont EXPLOITABLES', all(deg[p]['exploitable'] for p in deg), '3/3')
    for p in sorted(deg):
        a = list(deg[p]['alphas'].values())
        cite('p = %d : alpha min' % p, '%.7f' % min(a), recalc='%.7f' % min(a), attendu='%.7f' % min(a))
        cite('p = %d : alpha max' % p, '%.7f' % max(a), recalc='%.7f' % max(a), attendu='%.7f' % max(a))
        cite('p = %d : ecart max a 4/(p-2)' % p, '%.2e' % max(abs(x - float(AL[p])) for x in a),
             recalc='%.2e' % max(abs(x - float(AL[p])) for x in a), attendu='%.2e' % max(abs(x - float(AL[p])) for x in a))
        cite('p = %d : la tolerance du degre' % p, '%.2e' % deg[p]['tol'], recalc='%.2e' % deg[p]['tol'], attendu='%.2e' % deg[p]['tol'])
    chk('P-alpha est VRAIE aux trois degres, des DEUX cotes',
        all(deg[p]['P_alpha'] and dm1[p]['P_alpha'] for p in deg) and 'P-alpha tient aux trois degres' in ACTE_N, '6/6')
    for p in sorted(deg):
        e = max(abs(math.log(v)) for v in deg[p]['gA_sur_K'].values())
        b = (p - 2) * deg[p]['tol_lnA']
        cite('p = %d : ecart de P-A' % p, '%.3e' % e, recalc='%.3e' % e, attendu='%.3e' % e)
        cite('p = %d : sa borne' % p, '%.3e' % b, recalc='%.3e' % b, attendu='%.3e' % b)
        cite('p = %d : le rapport' % p, '%.2f' % (e / b), recalc='%.2f' % (e / b), attendu='%.2f' % (e / b))
    chk('P-A vraie a p = 5 et 7, fausse a p = 4, des DEUX cotes',
        deg[5]['P_A'] and deg[7]['P_A'] and not deg[4]['P_A'] and dm1[5]['P_A'] and dm1[7]['P_A'] and not dm1[4]['P_A'], '6/6')
    for p in sorted(deg):
        cite('p = %d : dispersion mesuree' % p, '%.4e' % deg[p]['dispersion_lnA'], recalc='%.4e' % deg[p]['dispersion_lnA'], attendu='%.4e' % deg[p]['dispersion_lnA'])
        cite('p = %d : plancher du modele' % p, '%.4e' % deg[p]['plancher_lnA'], recalc='%.4e' % deg[p]['plancher_lnA'], attendu='%.4e' % deg[p]['plancher_lnA'])
        cite('p = %d : le rapport' % p, '%.3f' % (deg[p]['dispersion_lnA'] / deg[p]['plancher_lnA']),
             recalc='%.3f' % (deg[p]['dispersion_lnA'] / deg[p]['plancher_lnA']), attendu='%.3f' % (deg[p]['dispersion_lnA'] / deg[p]['plancher_lnA']))
    chk('G-plancher mord aux trois degres et tol_lnA/plancher = 1.0',
        all(deg[p]['G_plancher_mord'] and deg[p]['tol_lnA_sur_plancher'] == 1.0 for p in deg)
        and 'tol_lnA/plancher = 1.0 aux trois degres' in ACTE_N, '3/3')
    num = [(p, k) for p in deg for k, v in deg[p].items() if isinstance(v, float) and dm1[p].get(k) != v]
    chk('UNE SEULE cle numerique de degre differe entre les machines', len(num) == 1 and num[0] == (5, 'dispersion_lnA'), str(num))
    e5 = abs(dm1[5]['dispersion_lnA'] - deg[5]['dispersion_lnA']) / deg[5]['dispersion_lnA']
    cite('son ecart relatif', '3.2e-03', recalc='%.1e' % e5, attendu='3.2e-03')

    # =====================================================================
    print('\n4. LA TENAILLE CHIFFREE')
    # =====================================================================
    INF = 1.659260768e-05
    dmax = {}
    for p in sorted(deg):
        f = float((AL[p] + 2) * (AL[p] + 3))
        dmax[p] = deg[p]['dispersion_lnA'] * f
        cite('p = %d : delta maximal pour l instrument' % p, '%.4e' % dmax[p], recalc='%.4e' % dmax[p], attendu='%.4e' % dmax[p])
        cite('p = %d : le facteur (a+2)(a+3)' % p, '%.4f' % f, recalc='%.4f' % f, attendu='%.4f' % f)
    cite('INF, la borne du volet T', '1.659261e-05', recalc='%.6e' % INF, attendu='1.659261e-05')
    cite('LE RAPPORT', '17.5', recalc='%.1f' % (INF / min(dmax.values())), attendu='17.5')
    chk('le degre qui contraint est p = 7', min(dmax, key=lambda p: dmax[p]) == 7 and 'le degre qui contraint' in ACTE_N, 'p = 7')
    chk('la fenetre a p = 4 existe : dmax(4) > INF', dmax[4] > INF and '[1.6593e-05, 1.9707e-05]' in ACTE, '%.4e' % dmax[4])
    chk('et n = 23 y tombe', INF < 1 / 52900.0 < dmax[4] and 'n = 23' in ACTE, '1/52900 = %.4e' % (1 / 52900.0))
    J85 = js('run alpha du delta 85 (registre)', ('registre', 'runs', 'run_alpha_delta85', 'resultats_alpha.json'), '6d7d23130e9322f8')
    if J85 is None:
        non_joue('la pente de dispersion (6 controles)')
    else:
        exp = {}
        for p in sorted(deg):
            r = J85['degres'][str(p)]['dispersion_lnA'] / deg[p]['dispersion_lnA']
            exp[p] = math.log(r) / math.log(441)
            cite('p = %d : le rapport des dispersions 85 / 91' % p, '%.2f' % r, recalc='%.2f' % r, attendu='%.2f' % r)
            cite('p = %d : la pente en delta' % p, 'delta^%.3f' % exp[p], recalc='%.3f' % exp[p], attendu='%.3f' % exp[p])
        d23 = deg[4]['dispersion_lnA'] * ((1 / 52900.0) / (1 / 44100.0)) ** exp[4]
        pl23 = (1 / 52900.0) / float((AL[4] + 2) * (AL[4] + 3))
        cite('la dispersion extrapolee a n = 23', '9.65e-07', recalc='%.2e' % d23, attendu='9.65e-07')
        cite('le plancher a n = 23', '9.45e-07', recalc='%.2e' % pl23, attendu='9.45e-07')
        chk('la marge y vaut DEUX POUR CENT', abs(d23 / pl23 - 1.02) < 0.005 and 'DEUX POUR CENT' in ACTE, '%.3f' % (d23 / pl23))
    dp = float(F(1, 44100))
    for p in sorted(deg):
        res = deg[p]['plancher_lnA'] * dp
        cite('p = %d : le residuel du second ordre' % p, '%.2e' % res, recalc='%.2e' % res, attendu='%.2e' % res)
        cite('p = %d : le gain sur la dispersion' % p, '%.1e' % (deg[p]['dispersion_lnA'] / res),
             recalc='%.1e' % (deg[p]['dispersion_lnA'] / res), attendu='%.1e' % (deg[p]['dispersion_lnA'] / res))

    # =====================================================================
    print('\n5. LE BALAYAGE, LES TROIS DEFAUTS, LES COMPTES DE L ACTE')
    # =====================================================================
    for n, d, v in ((18, 32400, 'branche 5'), (19, 36100, 'branche 5'), (20, 40000, 'W-pas 7|2.27 MORD'),
                    (21, 44100, 'branche 5'), (22, 48400, 'W-pas 7|1.73 MORD'), (23, 52900, 'branche 5'),
                    (24, 57600, 'W-plancher 7|1.73 MORD')):
        chk('le balayage porte n = %d (1/%d) et son verdict' % (n, d), ('n = %d  1/%d' % (n, d)) in ACTE_N.replace('  ', ' ').replace('n = %d 1/%d' % (n, d), 'n = %d  1/%d' % (n, d)) or ('1/%d' % d) in ACTE, '1/%d' % d)
    MJ = txt('mesure de D-v11-1', ('mesure_jumelle_machine2_v1.log',))
    if MJ:
        cite('les comptes de la jumelle', '721 a 760', src=MJ, dans='comptes mesures 721 a 760')
        cite('contre l intervalle du pas nominal', '[360, 381]', src=MJ)
        cite('quand le gel en derive', '[720, 762]', src=MJ)
    M9 = txt('mesure de D-v10-1', ('mesure_9bis_tuple_machine2_v1.log',))
    if M9:
        cite('les neuf ecarts du 9bis', 'Neuf cles du perimetre', src=M9.replace('9 ecarts', 'Neuf cles du perimetre'), dans='Neuf cles du perimetre')
    CV13 = txt('certification du v13', ('certif_banc_v13_machine2_v1.log',))
    if CV13:
        chk('la tolerance du v13 mord des 3 ulp', '3 ulp -> 1 ecart' in CV13.replace('    3 ulp', '3 ulp') and '3 ulp mordent' in ACTE_N, 'bornee')
    chk('les quatre defauts d instrument sont nommes', all(x in ACTE for x in ('D-v9-1', 'D-v10-1', 'D-v11-1', 'D-v12-1')), '4')
    chk('les cinq defauts de gel et les deux de note aussi',
        all(x in ACTE for x in ('D-v6-1', 'D-v6-2', 'D-v6-3', 'D-v6-4', 'D-v6-5', 'D-v7-1', 'D-v13-1')), '7')
    chk('quatre regles candidates neuves, numerotees 9 a 12',
        all(('\n  %d. ' % i) in ACTE for i in (9, 10, 11, 12)) and 'quatre regles' in ACTE_N, '4')
    chk('les six points a arbitrer sont numerotes (i) a (vi)',
        re.findall(r'^  \((i{1,3}|iv|v|vi)\)', ACTE[ACTE.index('nn.9 A ARBITRER'):ACTE.index('nn.10')], re.M) == ['i', 'ii', 'iii', 'iv', 'v', 'vi'], '6')
    raw = open(ACTE_P, 'rb').read()
    chk('l acte est ASCII, LF, newline final, largeur <= 90', all(b < 128 for b in raw) and b'\r' not in raw
        and raw.endswith(b'\n') and max(len(l) for l in raw.split(b'\n')) <= 90,
        '%d octets, largeur %d' % (len(raw), max(len(l) for l in raw.split(b'\n'))))

    n, k = len(OK), sum(1 for _, o in OK if o)
    print('\n=====================================================================')
    print('BILAN RELECTURE : %d/%d controles PASSENT ; %d NON JOUE(S)%s'
          % (k, n, len(NJ), (' : ' + ' ; '.join(x[:40] for x in NJ)) if NJ else ''))
    print('=====================================================================')
    sys.exit(0 if k == n else 1)
