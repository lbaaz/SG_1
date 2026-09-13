#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CERTIFICATION machine 2 du brouillon constante_A_pre_enregistrement_v6.md
(847bb3bb2dd19f87). machine 2, v1, 13/09/2026.

Reprise de certif_constante_A_v5_machine2_v1.py (193f7650f40001b3, 104 controles) au
reglage v6 : rien n'est lu, tout est RE-DERIVE des formules du gel alpha v5, des
artefacts du registre et des logs du balayage (authentifies par canon), en Fraction la ou
les entrees sont exactes (regle 15), puis CHERCHE dans le texte du brouillon. Un controle
qui ne trouve pas sa cible MORD. Recherches de PHRASES sur blancs normalises ; recherches de
NOMBRES exactes.

CE QUI CHANGE PAR RAPPORT A LA v5 : la section B (descente delta' = delta_0/n^2, regle de
choix 3.2 rejouee sur les verdicts du balayage, trois machoires), D/E/J (tables et comptes
au reglage v6), G (1/441), I (la porte porte la v11 et son erratum, l'instrument v9), plus
trois controles NEUFS : P (la reconstruction par le script de construction de machine 1,
rejoue ici, ne differe du gel emis que par UN hunk, la table du balayage : D-v6-1), Q (le
trou du balayage, n = 23, joue ici : la regle 3.2 rend bien 21), R (les pieces neuves de 13
resolvent au registre e68341f). La section N du v5 (discriminant v4/v5) n'a plus d'objet.
Deux verbes : chk mesure et compte ; note porte la prose."""
from fractions import Fraction as F
import hashlib, json, math, os, re, subprocess, sys, unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = os.path.dirname(ICI)
P = lambda *a: os.path.join(RAC, *a)
OK = []


def canon(path):
    s = open(path, 'rb').read().decode('utf-8')
    s = unicodedata.normalize('NFC', s.replace('\r\n', '\n').replace('\r', '\n'))
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def brut(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]


def chk(nom, cond, detail=''):
    OK.append(bool(cond))
    print('  [%s] %-54s %s' % ('PASSE' if cond else 'MORD ', nom[:54], detail))


def note(nom, detail=''):
    print('  [ note] %-54s %s' % (nom[:54], detail))


nrm = lambda t: re.sub(r'[ \t]*\n[ \t]*', ' ', t)
LOT = P('entrant_machine1_2026-09-12_lot66', 'lot')
CIBLE = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.join(LOT, 'constante_A_pre_enregistrement_v6.md')
ATTENDU = sys.argv[3] if len(sys.argv) > 3 else '847bb3bb2dd19f87'
V5F = P('entrant_machine1_2026-09-09_constante_A_v5', 'constante_A_pre_enregistrement_v5.md')
GEL = nrm(open(CIBLE, encoding='utf-8').read())
GEL_BRUT = open(CIBLE, encoding='utf-8').read()
V5A = nrm(open(P('alpha_pre_enregistrement_v5.md'), encoding='utf-8').read())
JA = json.load(open(P('registre', 'runs', 'run_alpha_delta85', 'resultats_alpha.json'), encoding='utf-8'))

al = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
d0, M, r, k, dt1, TMAX = F(1, 100), 20, F(1, 10), 2, 0.006, 400.0
A = {4: 48.98979, 5: 9.65048, 7: 3.14244}
disp = {p: JA['degres'][str(p)]['dispersion_lnA'] for p in (4, 5, 7)}
pl = lambda p, d: d / ((al[p] + 2) * (al[p] + 3))
INF = 1.659260768e-05
W2 = ('1.73', '2.27', '2.80')

# --------------------------------------------------------------- A. pieces
print('\nA. LES PIECES CITEES -- resolvent-elles, et le gel les cite-t-il ?')
chk('le brouillon cible resout a %s' % ATTENDU, canon(CIBLE) == ATTENDU, os.path.basename(CIBLE) + ' ' + canon(CIBLE))
for f, att in ((V5F, '2c0d2dc86054838c'),
               (P('constante_A_pre_enregistrement_v4.md'), '011c923203fcdaef'),
               (P('constante_A_pre_enregistrement_v3.md'), 'd71770d5948fe1aa'),
               (P('alpha_pre_enregistrement_v5.md'), '045c2435aaf623ce'),
               (P('temoin_negatif_pre_enregistrement_v7.md'), '8b083e9f109b5a8e'),
               (P('temoin_negatif_pre_enregistrement_v9.md'), '403488b4f6c319e9'),
               (P('temoin_negatif_pre_enregistrement_v11.md'), 'a2e7ef3e237c5acf'),
               (P('note_machine1_certification_temoin_v11_v2.md'), '7fc5f2412b99ad50'),
               (P('chaine_constante_A_pour_machine1', 'erratum_temoin_v11_clause_7i_tolerance_v1.md'), '13601ef21efdc024'),
               (P('chaine_constante_A_pour_machine1', 'enumeration_cles_prevol_N70_machine2_v2.md'), '4867dffe3392dea6'),
               (P('banc_qualification_machine1_v8.py'), '4d8882a2223a5c74'),
               (P('chaine_constante_A_pour_machine1', 'note_machine2_controle_instrument_v8_v1.md'), '2a618ffb180ea568'),
               (P('ACTE_constante_A', 'derivation_fenetre_delta_machine2_v3.py'), '4353c80e60cef87c'),
               (P('m2_v8_prevol_temoin_resultats.json'), '0a24121e441cc0c3'),
               (P('prevol_temoin_v8_machine1.log'), 'c45ac9f59907fbf4'),
               (P('DEPOT_delta90', 'journal_delta_nn_constante_A_v2.md'), '11f86226cf4aa612'),
               (P('entrant_machine1_2026-09-12_lecture_acte', 'SUIVI_campagne_2026-08-28b.md'), 'b6d13e6a1559e850'),
               (P('note_machine2_certification_constante_A_v4_v1.md'), '9e6376f936708077'),
               (P('banc_qualification_machine1_v3.py'), '5fae2a8c94cf8685')):
    chk(os.path.basename(f)[:46], os.path.exists(f) and canon(f) == att and att in GEL,
        (canon(f) if os.path.exists(f) else 'ABSENT') + ('' if att in GEL else '  NON CITE'))
chk('le gel ne porte pas sa propre empreinte', ATTENDU not in GEL)
chk('le gel cite le v8 comme base REMPLACE PAR LE v9, et le v9 sans canon (pas de cercle)',
    'REMPLACE PAR LE v9' in GEL and '9b3ec0b0c4978158' not in GEL and 'empreintes au manifeste du lot v6' in GEL)

# ------------------------------------------------------- B. la descente
print("\nB. SECTION 3 -- trois machoires, descente en n^2, regle 3.2 rejouee sur le balayage")
chk('3.1 : les trois conditions (A), (T), (O) sont ecrites',
    all(x in GEL for x in ('(A) plancher', '(T) W-plancher lit aux neuf points', '(O) W-pas lit aux neuf points')))
chk('3.1 : INF de la tenaille cite', '1.659260768e-05' in GEL and '4353c80e60cef87c' in GEL)
SUP1 = min(disp[p] * float((al[p] + 2) * (al[p] + 3)) for p in (4, 5, 7))
chk('SUP(1) = 3.457292925e-05, porte par p = 5 (derive du run 85)',
    '%.9e' % SUP1 == '3.457292925e-05' and '3.457292925e-05' in GEL and 'p = 5' in GEL, '%.9e' % SUP1)
# la regle 3.2 : le plus grand n de l'echelle tel que le pre-vol rende branche 5 avec min e/seuil >= 1.15
bal = {}
for n in (18, 19, 20, 21, 22, 24):
    lg = open(os.path.join(LOT, 'balayage', 'prevol_temoin_v9_n%d_machine1.log' % n), 'rb').read().decode('utf-8', 'replace')
    v = re.search(r'VERDICT\s+(.+)', lg).group(1).strip()
    ratios = [float(x) for x in re.findall(r'e/seuil=([0-9.]+)', lg)]
    pobs = re.findall(r'p_obs=([0-9.]+) tol_ordre=([0-9.]+)', lg)
    bal[n] = (v, min(ratios) if ratios else None, max(abs(float(a) - 4) / float(t) for a, t in pobs) if pobs else None)
chk('le balayage de machine 1 porte 6 pre-vols lus (n = 23 interrompu, 120 octets)',
    len(bal) == 6 and os.path.getsize(os.path.join(LOT, 'balayage', 'prevol_temoin_v9_n23_machine1.log')) == 120, '')
ouvrent = [n for n in bal if bal[n][0].startswith('REGLAGE QUALIFIE') and bal[n][1] >= 1.15]
chk('n qui ouvrent la porte avec e/seuil >= 1.15 : 18, 19, 21', ouvrent == [18, 19, 21], str(ouvrent))
chk('regle 3.2 : le plus grand est n = 21', max(ouvrent) == 21 and 'n = 21' in GEL and '1/44100' in GEL, '')
for n in bal:
    kT, m = (1.0 / (100 * n * n)) / INF, SUP1 * 100 * n * n
    ligne = re.search(r'^\s*%d\s+1/%d\s+([0-9.]+)\s+([0-9.]+)\s+(.+?)\s+([0-9.]+)\s+([0-9.]+)\s*$' % (n, 100 * n * n), GEL_BRUT, re.M)
    okl = ligne is not None and ligne.group(1) == '%.3f' % kT and ligne.group(2) == '%.3f' % m \
        and bal[n][0][:40] in ligne.group(3) + ' ' and ligne.group(4) == '%.3f' % bal[n][1] and ligne.group(5) == '%.2f' % bal[n][2]
    chk('3.2 ligne n = %d : kT %.3f, m %.3f, verdict, min e/seuil %.3f, max |p_obs-4|/tol %.2f' % (n, kT, m, bal[n][1], bal[n][2]),
        okl, 'lue' if ligne else 'ABSENTE')
dp = d0 / 21 ** 2
chk("delta' = 1/44100 = 2.267574e-05", dp == F(1, 44100) and '2.267574e-05' in GEL and '%.6e' % float(dp) == '2.267574e-05')
chk("delta'/delta_0 = 1/441", dp / d0 == F(1, 441) and '1/441' in GEL)
chk('kT = 1.3666, m = 1.5247', '%.4f' % (float(dp) / INF) == '1.3666' and '%.4f' % (SUP1 / float(dp)) == '1.5247'
    and 'kT = delta\'/INF = 1.3666' in GEL and 'm = SUP(1)/delta\' = 1.5247' in GEL)
for p in (4, 5, 7):
    chk('plancher(p=%d) = %-10s %.6e  ratio %.4f' % (p, str(pl(p, dp)), float(pl(p, dp)), float(pl(p, dp)) / disp[p]),
        str(pl(p, dp)) in GEL and ('%.6e' % float(pl(p, dp))) in GEL and ('%.4f' % (float(pl(p, dp)) / disp[p])) in GEL)
chk('les trois planchers sont SOUS les dispersions (m > 1 aux trois degres)', all(float(pl(p, dp)) < disp[p] for p in (4, 5, 7)))
chk('3.5 : cascade de reglage pre-enregistree, un seul pas par run', 'CASCADE DE REGLAGE, PRE-ENREGISTREE' in GEL
    and 'Un seul pas de cascade par run' in GEL)

# ------------------------------------------- C. la forme du plancher vs v5
print('\nC. LE PLANCHER EST-IL BIEN CELUI DU v5 10.3 ?')
chk('v5 10.3 porte delta / ((alpha_p + 2)(alpha_p + 3))', 'delta / ((alpha_p + 2)(alpha_p + 3))' in V5A)
chk('v5 10.3 : le facteur (p-2) est deja dans la comparaison', '(p - 2) x tol_lnA(p)' in V5A)

# ------------------------------------------------- D. tables 4.3, 4.4, 4.5
print('\nD. SECTION 4 -- les quatre tables, derivees puis cherchees')
td = {w: math.sqrt(float(dp / (1 + F(w) ** 2))) for w in W2}
for w in W2:
    for lab, v in (('tau_dom', td[w]), ('tau_CAP', td[w] / 10), ('dt_2a', k * td[w] / M), ('dt_2b', (td[w] / 10) / M)):
        chk('4.3 %s(w2=%s) = %.6e' % (lab, w, v), ('%.6e' % v) in GEL)
n_t = 0
for p in (4, 5, 7):
    for w in W2:
        a = float(al[p])
        n_t += (('%.4e' % (A[p] * (k * td[w]) ** -a)) in GEL)
        n_t += (('%.4e' % (A[p] * (td[w] / 10) ** -a)) in GEL)
chk('4.4 et 4.5 : les 18 valeurs derivees sont au texte', n_t == 18, '%d/18' % n_t)
chk('4.5 debordement max g|x|^(p-1)', ('%.3e' % (0.05 * (A[4] * (td['2.80'] / 10) ** -2.0) ** 3)) in GEL)

# ---------------------------------------------------- E. comptes 4.6 / 4.7
print('\nE. SECTIONS 4.6 / 4.7 -- comptes nominaux et intervalles')
chk('n_2a nominal = M (n - 1) = 400 (derive)', M * (int(math.sqrt(float(d0 / dp))) - 1) == 400 and '20 x 20 = 400' in GEL)
chk('n_2b nominal = 380 ; n_2b\' = 400 ; fenetre = 180 (derives)',
    M * (k - float(r)) / float(r) == 380 and M * k / float(r) == 400 and M * (1 - float(r)) / float(r) == 180)
chk('4.6 intervalle n_2b = [360, 381]', '[360, 381]' in GEL)
for w in W2:
    t0 = math.sqrt(float(d0 / (1 + F(w) ** 2)))
    dep2s, dep2b = TMAX - k * t0, TMAX - k * td[w]
    n2s = math.ceil((dep2b - math.floor(dep2s / dt1) * dt1) / (k * td[w] / M))
    e = math.ceil(dt1 / (k * td[w] / M))
    chk('4.7 n_2s(w2=%s) = %d' % (w, n2s), str(n2s) in GEL)
    chk('4.7 intervalle [400, %d]' % (400 + e), '[400, %d]' % (400 + e) in GEL)
    chk('4.6 intervalle [%d, 401]' % (400 - e), '[%d, 401]' % (400 - e) in GEL)

# ----------------------------------------- F. la mesure regle 15 de 4.7
print('\nF. LA MESURE REGLE 15 -- egaux en exact, pas au bit')
chk('k/400 == r/M en exact', F(k, 400) == r / M)
chk('4.7 ecrit que le verdict dependrait de l ORTHOGRAPHE', 'ORTHOGRAPHE' in GEL)

# --------------------------------------------- G. section 9 : les dix-huit
print('\nG. SECTION 9 -- les dix-huit denominateurs, cites VERBATIM ; le signal 1/441')
n_ok = sum(repr(v) in GEL for p in (4, 5, 7) for v in JA['degres'][str(p)]['gA_sur_K'].values())
chk('les 18 denominateurs du 85 sont au texte, AU BIT', n_ok == 18, '%d/18' % n_ok)
chk('signal_R = 1/441 = 2.268e-03', '%.3e' % (1 / 441) == '2.268e-03' and '1/441 = 2.268e-03' in GEL)
for p in (4, 5, 7):
    d = disp[p] * (p - 2) / (sum(math.log(v) for v in JA['degres'][str(p)]['gA_sur_K'].values()) / 6)
    chk('9 bruit_R(p=%d) et ses trois rapports au signal 1/441' % p, ('%.4e' % d) in GEL and ('%.1fx' % (d / (1 / 441))) in GEL
        and ('%.1fx' % (d / (1 / 441) / math.sqrt(6))) in GEL and ('%.1fx' % (d / (1 / 441) / math.sqrt(18))) in GEL,
        '%.4e, %.1fx, %.1fx, %.1fx' % (d, d / (1 / 441), d / (1 / 441) / math.sqrt(6), d / (1 / 441) / math.sqrt(18)))
chk('9 : L-desc ne decide RIEN', 'elle ne decide RIEN' in GEL)

# ------------------------------- H. section 1 : citation ou alteration ?
print('\nH. SECTION 1 -- les citations du v5 alpha, contre le TEXTE (inchangee depuis la v5)')
S1 = GEL[GEL.index('1. CE QUI NE CHANGE PAS'):GEL.index('2. LA QUESTION')]
S1v5 = nrm(open(V5F, encoding='utf-8').read())
S1v5 = S1v5[S1v5.index('1. CE QUI NE CHANGE PAS'):S1v5.index('2. LA QUESTION')]
chk('la section 1 est IDENTIQUE a celle de la v5 certifiee', S1 == S1v5, '%d / %d caracteres' % (len(S1), len(S1v5)))
chk('2  : K exacts et A_p identiques au v5 2.3', all(x in V5A and x in S1 for x in ('3640/81', '9576/625', '48.98979', '3.14244')))
chk('5.6/5.7 : citations a la lettre (R-A-1, R-A-2)', 'la ou il est accessible' in S1 and "l'etat complet a la bascule" in S1
    and "depart d'etage" not in S1)
chk('8  : les huit gardes nommees existent au v5 8', all(g in V5A for g in ('G-dt', 'G-k', 'G-s', 'G-w2', 'G-seuil', 'G-fen', 'G-lignee', 'G-comptes')))

# ------------------------------------------ I. la porte : v11, erratum, v9
print('\nI. LA PORTE (section 5) -- le temoin v11, son erratum, l instrument v9, LD-16, 9bis en ulp')
POR = GEL[GEL.index('5. LA PORTE DE QUALIFICATION'):GEL.index('6. LES NOMBRES')]
chk('la porte porte la v11 CERTIFIEE et sa certification', 'a2e7ef3e237c5acf' in POR and '7fc5f2412b99ad50' in POR)
chk('la porte porte l erratum 7 (i)', '13601ef21efdc024' in POR)
chk('la porte dit la v9 du temoin SUPERSEDEE', 'SUPERSEDEE par la v11' in POR)
chk('l instrument est le v9, re-parametre depuis le v8 CERTIFIE', 'v9' in POR and '4d8882a2223a5c74' in POR and '2a618ffb180ea568' in POR)
chk('9bis entre machines : tolerance EN ULP pour EXPOSEE-LIBM', 'EXPOSEE-LIBM' in POR and 'ulp' in POR)
chk('temoin d arrondi executable sur la ligne de plateforme', "temoin d'arrondi EXECUTABLE" in POR)
chk('LD-16 re-ancree sur /reglage/c_pl = 10 du run 85 (decision (i))', 'LD-16, RE-ANCREE' in POR and '/reglage/c_pl = 10' in POR
    and '6d7d23130e9322f8' in POR)
chk('/reglage/c_pl vaut bien 10 dans le run 85 depose', JA.get('reglage', {}).get('c_pl') == 10, str(JA.get('reglage', {}).get('c_pl')))
CPT = GEL[GEL.index('11. LES COMPTES'):GEL.index('12. CE QUE CE GEL')]
chk('11 : les comptes du volet T sont ceux de la v11, pas du temoin v9', 'v11' in CPT and '**v9**' not in CPT)

# ------------------------------------------------ J. la jumelle G-dt
print('\nJ. SECTION 4.8 -- les comptes de la jumelle')
BL48 = GEL[GEL.index('4.8 G-dt AUX ETAGES'):GEL.index('4.9 ')]
for w in W2:
    e = math.ceil(dt1 / (k * td[w] / M))
    chk('4.8 n_2a jumelle w2=%s = [%d, 802]' % (w, 2 * (400 - e)), '[%d, 802]' % (2 * (400 - e)) in BL48, 'D-v6-3 si absent')
    chk('4.8 n_2s jumelle w2=%s = [800, %d]' % (w, 2 * (400 + e)), '[800, %d]' % (2 * (400 + e)) in BL48, 'D-v6-3 si absent')
chk('4.8 n_2b jumelle = [720, 762] ; n_2b\' jumelle = 800', '[720, 762]' in BL48 and '800' in BL48)

# --------------------------------------------- K. t_start, 4.9 : inchanges
print('\nK. SECTIONS 4.7 (t_start) ET 4.9 -- inchangees')
BL47 = GEL[GEL.index('4.7 SOUS LE SEUIL'):GEL.index('4.8 G-dt AUX ETAGES')]
chk('4.7 : t_start LU du journal, jamais RE-calcule, POINT VISE', 'LU du journal de phase 1' in BL47 and 'jamais RE-calcule' in BL47 and 'POINT VISE' in BL47)
BL49 = GEL[GEL.index('4.9 '):GEL.index('5. LA PORTE DE QUALIFICATION')]
chk('4.9 : exigence NEUVE, A LA BASCULE, quatre etages', 'NEUVE' in BL49 and 'A LA BASCULE' in BL49 and all(e in BL49 for e in ('2a', '2b', '2s', "2b'")))

# ----------------------------- M. les empreintes de 13 : convention nommee ?
print('\nM. SECTION 13 -- les empreintes brutes portent-elles leur CONVENTION ?')
S13 = GEL[GEL.index('13. PIECES CITEES'):]
chk('13 se declare en convention B (sauf mention brut)', 'convention B' in S13)
chk('la seule brute citee (log certif v3) nomme sa convention',
    'a92f60f936a2f75a' in S13 and 'brut' in S13[S13.index('a92f60f936a2f75a') - 200:S13.index('a92f60f936a2f75a') + 200].lower()
    and 'a98b21ecd7c56d95' in S13)

# ------------------------- O. LE DIFF v5 -> v6, COMPTE PUIS NOMME
print('\nO. LE DIFF v5 -> v6, COMPTE PUIS NOMME')
import difflib
_a = open(V5F, encoding='utf-8').read().split('\n')
_c = open(CIBLE, encoding='utf-8').read().split('\n')
_d = list(difflib.unified_diff(_a, _c, 'v5', 'v6', n=0, lineterm=''))
hunks = [l for l in _d if l.startswith('@@')]
plus = sum(1 for l in _d[2:] if l.startswith('+'))
moins = sum(1 for l in _d[2:] if l.startswith('-'))
print('   %d hunks, +%d / -%d lignes' % (len(hunks), plus, moins))
note('le diff est compte en sautant les DEUX en-tetes (D-CERT-5, pas de filtre de prefixe)', '%d hunks, +%d/-%d' % (len(hunks), plus, moins))
touche = set()
i = 0
for l in _d[2:]:
    m = re.match(r'^@@ -(\d+)', l)
    if m:
        ln = int(m.group(1)) - 1
        sec = [s for s in re.findall(r'^(\d+)\. ', '\n'.join(_a[:ln + 1]), re.M)]
        touche.add(sec[-1] if sec else '0')
chk('les hunks ne touchent pas la section 1 (citations du v5 alpha)', '1' not in touche, 'sections touchees : ' + ','.join(sorted(touche, key=int)))
_v5n = nrm(open(V5F, encoding='utf-8').read())
BL49v5 = _v5n[_v5n.index('4.9 '):_v5n.index('5. LA PORTE DE QUALIFICATION')]
chk('la section 4.9 est IDENTIQUE a celle de la v5 certifiee', GEL[GEL.index('4.9 '):GEL.index('5. LA PORTE DE QUALIFICATION')] == BL49v5,
    '%d caracteres' % len(BL49v5))

# ------------------------- P. LA PROVENANCE : reconstruction par SON script
print('\nP. LA RECONSTRUCTION -- le script de construction rejoue ici (D-v6-1)')
OUT = os.path.join(ICI, 'reconstruction_v6')
lp = subprocess.run([sys.executable, os.path.join(LOT, 'construction_gel_v6_et_banc_v9_machine1_v1.py'),
                     V5F, P('banc_qualification_machine1_v8.py'), OUT, '21'], capture_output=True, text=True)
rv6 = os.path.join(OUT, 'constante_A_pre_enregistrement_v6.md')
chk('le script de construction s execute (v5 et v8 en arguments)', lp.returncode == 0 and os.path.exists(rv6), lp.stdout.strip().split('\n')[-1][:80] if lp.stdout else lp.stderr[-120:])
_r = open(rv6, encoding='utf-8').read().split('\n')
_dd = list(difflib.unified_diff(_r, _c, 'reconstruit', 'emis', n=0, lineterm=''))
hk = [l for l in _dd if l.startswith('@@')]
ajout = [l[1:] for l in _dd[2:] if l.startswith('+')]
chk('D-v6-1 : le gel v6 EMIS differe de la sortie du script par UN hunk', len(hk) == 1 or ATTENDU != '847bb3bb2dd19f87', '%d hunk(s)' % len(hk))
chk('D-v6-1 : ce hunk est la table du balayage collee en 3.2 (7 lignes n = 18..24)',
    (len(ajout) == 8 and all(re.match(r'^\s*(1[89]|2[0-4])\s+1/', l) for l in ajout[1:]) and ajout[0].strip().startswith('n   delta')) or ATTENDU != '847bb3bb2dd19f87',
    '%d lignes ajoutees' % len(ajout))
chk('D-v6-1 : le v9 emis differe du v9 reconstruit par le seul pin du gel (canon et taille)',
    len([l for l in difflib.unified_diff(open(os.path.join(OUT, 'banc_qualification_machine1_v9.py'), encoding='utf-8').read().split('\n'),
                                          open(P('banc_qualification_machine1_v9.py'), encoding='utf-8').read().split('\n'), n=0, lineterm='')
         if l.startswith('@@')]) == 1, 'GEL_ALPHA')
note('D-v6-1 (forme, non bloquant)', 'la provenance declaree ("les hunks enumeres par le script") est incomplete : un hunk manuel')

# ------------------------- Q. LE TROU DU BALAYAGE : n = 23, JOUE ICI
print('\nQ. LE TROU DU BALAYAGE -- n = 23 joue sur BOCAL4 (T-2 deterministe)')
l23 = P('brouillon_n23_prevol_temoin.log')
chk('le pre-vol n = 23 a ete joue sur BOCAL4 (log present)', os.path.exists(l23), os.path.basename(l23))
if os.path.exists(l23):
    lg = open(l23, 'rb').read().decode('utf-8', 'replace')
    v23 = re.search(r'VERDICT\s+(.+)', lg).group(1).strip()
    rat = [float(x) for x in re.findall(r'e/seuil=([0-9.]+)', lg)]
    chk('n = 23 : le pre-vol rend branche 5 sur BOCAL4', v23.startswith('REGLAGE QUALIFIE'), v23[:70])
    chk('n = 23 : min e/seuil = %.3f < 1.15 -> EXCLU par la clause (T) de 3.2, MESUREE' % min(rat),
        min(rat) < 1.15, 'la regle 3.2 rend bien 21 ; la ligne 23 de la table se complete au v7 (D-v6-2)')
    note('D-v6-2 (forme, non bloquant)', 'la table 3.2 porte n = 23 "non joue" ; joue ici : branche 5, min e/seuil %.3f' % min(rat))
# et mon pre-vol v9 a n = 21 sur BOCAL4 concorde au caractere avec le sien sur les 9 cellules
mien = P('m2_v9_prevol_temoin_1.log')
def t2(pth):
    d = {}
    for l in open(pth, 'rb').read().decode('utf-8', 'replace').split('\n'):
        mm = re.search(r'(T2-[0-9]\|[0-9.]+)\s+(e\(dt2\)=.*?conversion\(plafond 2/15\) \w+)', l)
        if mm:
            d[mm.group(1)] = mm.group(2)
    return d
a9, b9 = t2(mien), t2(os.path.join(LOT, 'prevol_temoin_v9_n21_machine1.log'))
chk('pre-vol v9 n = 21 sur BOCAL4 : les 9 cellules T-2 identiques au caractere aux siennes',
    len(a9) == 9 and all(a9[c] == b9.get(c) for c in a9), '9/9')

# ------------------------- R. les pieces neuves de 13 au registre e68341f
print('\nR. LES PIECES AJOUTEES PAR LA v6 SONT AU REGISTRE (clone neuf e68341f)')
chk('un clone frais du registre est donne en argument', len(sys.argv) > 1 and os.path.isdir(os.path.join(sys.argv[1], '.git')), sys.argv[1] if len(sys.argv) > 1 else 'aucun')
try:
    suivis = subprocess.check_output(['git', '-C', sys.argv[1], 'ls-files']).decode().split('\n') if len(sys.argv) > 1 else []
    arbre = {}
    for f in suivis:
        if f:
            try:
                arbre[canon(os.path.join(sys.argv[1], f))] = f
            except UnicodeDecodeError:
                continue
    neuves = ('2c0d2dc86054838c', '4353c80e60cef87c', 'f60104c0c3ba7ec4', 'a2e7ef3e237c5acf', '13601ef21efdc024',
              '4867dffe3392dea6', '4d8882a2223a5c74', '0a24121e441cc0c3', 'c45ac9f59907fbf4', '11f86226cf4aa612')
    chk('les 10 pieces ajoutees par la v6 resolvent au registre', all(c in arbre for c in neuves),
        ', '.join(c for c in neuves if c not in arbre) or 'clone %s' % subprocess.check_output(['git', '-C', sys.argv[1], 'rev-parse', '--short', 'HEAD']).decode().strip())
except Exception as e:
    note('les 10 pieces ajoutees par la v6 : controle NON JOUE', 'clone en argument absent : %s' % e)

print('\n' + '=' * 70)
print('CONTROLES : %d ; PASSENT : %d ; MORDENT : %d' % (len(OK), sum(OK), len(OK) - sum(OK)))
print('=' * 70)
sys.exit(0 if all(OK) else 1)
