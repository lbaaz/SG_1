# -*- coding: utf-8 -*-
"""CERTIFICATION machine 2 du brouillon constante_A_pre_enregistrement_v5.md
(2c0d2dc86054838c). Rien n'est lu : tout est re-derive des FORMULES du gel
alpha v5 et des artefacts du registre, en Fraction la ou les entrees sont
exactes (regle 15), puis CHERCHE dans le texte du brouillon. Un controle qui
ne trouve pas sa cible MORD.

Reprise de certif_constante_A_v4_machine2_v1.py : UN SEUL controle change.

CE QUI CHANGE, ET POURQUOI CE N'EST PAS UN TAMPON. Le controle M du v4
s'appelait "aucune empreinte BRUTE non signalee dans un bloc convention B"
mais ne TESTAIT que la PRESENCE de l'empreinte brute, jamais son SIGNALEMENT.
Ainsi ecrit, AUCUN texte n'aurait pu le satisfaire : le v5 aurait mordu apres
avoir corrige exactement ce qu'on lui demandait. L'etiquette et le test ne
disaient pas la meme chose -- la famille de defaut que les deux machines
paient depuis une semaine. M est donc reecrit pour MESURER CE QU'IL ANNONCE :
une brute est acceptable si SA LIGNE nomme sa convention.
PREUVE QUE LE CORRECTIF N'EST PAS COMPLAISANT : le M reecrit est rejoue sur
le v4 ET sur le v5 (section N). Il MORD sur le v4 et PASSE sur le v5. Un
controle qui ne separerait plus les deux versions ne certifierait rien."""

from fractions import Fraction as F
import hashlib, json, math, os, re, unicodedata

OK = []


def canon(path):
    s = open(path, 'rb').read().decode('utf-8')
    s = unicodedata.normalize('NFC', s.replace('\r\n', '\n').replace('\r', '\n'))
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def brut(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16]


def chk(nom, cond, detail=''):
    OK.append(bool(cond))
    print('  [%s] %-54s %s' % ('PASSE' if cond else 'MORD ', nom, detail))


# LES TEXTES SONT ENVELOPPES A 72 COLONNES : une phrase cherchee telle
# quelle enjambe les lignes et la sonde rend un FAUX ECHEC. Toute recherche
# de phrase se fait donc sur le texte a BLANCS NORMALISES. (Trois faux
# echecs payes avant d'ecrire cette ligne.)
nrm = lambda t: re.sub(r'[ \t]*\n[ \t]*', ' ', t)
CIBLE = os.path.join('entrant_machine1_2026-09-09_constante_A_v5',
                     'constante_A_pre_enregistrement_v5.md')
V4F = 'constante_A_pre_enregistrement_v4.md'
GEL = nrm(open(CIBLE, encoding='utf-8').read())
V5 = nrm(open('alpha_pre_enregistrement_v5.md', encoding='utf-8').read())
JA = json.load(open('out_banc/alpha/resultats_alpha.json', encoding='utf-8'))

al = {4: F(2), 5: F(4, 3), 7: F(4, 5)}
d0, b, m, M, r, k, dt1, TMAX = F(1, 100), 4, 2, 20, F(1, 10), 2, 0.006, 400.0
A = {4: 48.98979, 5: 9.65048, 7: 3.14244}
disp = {p: JA['degres'][str(p)]['dispersion_lnA'] for p in (4, 5, 7)}
pl = lambda p, d: d / ((al[p] + 2) * (al[p] + 3))

# --------------------------------------------------------------- A. pieces
print('\nA. LES PIECES CITEES -- resolvent-elles ?')
for f, att in ((CIBLE, '2c0d2dc86054838c'),
               (V4F, '011c923203fcdaef'),
               ('note_machine2_certification_constante_A_v4_v1.md', '9e6376f936708077'),
               ('constante_A_pre_enregistrement_v3.md', 'd71770d5948fe1aa'),
               ('alpha_pre_enregistrement_v5.md', '045c2435aaf623ce'),
               ('temoin_negatif_pre_enregistrement_v7.md', '8b083e9f109b5a8e'),
               ('temoin_negatif_pre_enregistrement_v8.md', '7ba4af8140b7a385'),
               ('temoin_negatif_pre_enregistrement_v9.md', '403488b4f6c319e9'),
               ('note_machine1_certification_temoin_v9_v1.md', 'b5da74783e5f97c6'),
               ('note_machine1_certification_temoin_v8_v1.md', 'ded4a5721601bd1e'),
               ('note_machine2_certification_constante_A_v3_v1.md', '52f76b9b82e7c861'),
               ('certif_constante_A_v3_machine2_v1.py', '1fa0c0eb3a341e09'),
               ('banc_qualification_machine1_v3.py', '5fae2a8c94cf8685')):
    # un gel ne porte pas sa PROPRE empreinte : elle se prend a la certification
    soi = f == CIBLE
    chk('%s' % f[:44], canon(f) == att and (soi or att in GEL),
        canon(f) + ('  (empreinte du gel lui-meme, non citee en 13)' if soi else ''))

# ------------------------------------------------------- B. delta' et 3.3
print("\nB. SECTION 3 -- delta', J minimal, les trois planchers")
J = next(j for j in range(1, 12)
         if all(float(pl(p, d0 / F(b) ** j)) <= disp[p] / m for p in (4, 5, 7)))
dp = d0 / F(b) ** J
chk('J minimal = 5 (J = 4 echoue)', J == 5 and 'J = 5' in GEL, 'J=%d' % J)
chk("delta' = 1/102400 au texte", dp == F(1, 102400) and '1/102400' in GEL)
chk("delta'/delta_0 = 1/1024", dp / d0 == F(1, 1024) and '1/1024' in GEL)
chk('temoin de minimalite 9/3328000', '9/3328000' in GEL)
for p in (4, 5, 7):
    chk('plancher(p=%d) = %-12s' % (p, str(pl(p, dp))), str(pl(p, dp)) in GEL)

# ------------------------------------------- C. la forme du plancher vs v5
print('\nC. LE PLANCHER EST-IL BIEN CELUI DU v5 10.3 ?')
chk('v5 10.3 porte delta / ((alpha_p + 2)(alpha_p + 3))',
    'delta / ((alpha_p + 2)(alpha_p + 3))' in V5)
for p, q in ((4, '1/2000'), (5, '9/13000'), (7, '1/1064')):
    chk('v5 : plancher(p=%d) = %s a delta_0' % (p, q), str(pl(p, d0)) == q and q in V5)
chk('v5 10.3 : le facteur (p-2) est deja dans la comparaison',
    '(p - 2) x tol_lnA(p)' in V5)

# ------------------------------------------------- D. tables 4.3, 4.4, 4.5
print('\nD. SECTION 4 -- les quatre tables, derivees puis cherchees')
td = {w: math.sqrt(float(dp / (1 + F(w) ** 2))) for w in ('1.73', '2.27', '2.80')}
for w in sorted(td):
    for lab, v in (('tau_dom', td[w]), ('tau_CAP', td[w] / 10),
                   ('dt_2a', k * td[w] / M), ('dt_2b', (td[w] / 10) / M)):
        chk('4.3 %s(w2=%s) = %.6e' % (lab, w, v), ('%.6e' % v) in GEL)
n_t = 0
for p in (4, 5, 7):
    for w in sorted(td):
        a = float(al[p])
        n_t += (('%.4e' % (A[p] * (k * td[w]) ** -a)) in GEL)
        n_t += (('%.4e' % (A[p] * (td[w] / 10) ** -a)) in GEL)
chk('4.4 et 4.5 : les 18 valeurs derivees sont au texte', n_t == 18, '%d/18' % n_t)
chk('4.5 debordement max g|x|^(p-1)',
    ('%.3e' % (0.05 * (A[4] * (td['2.80'] / 10) ** -2.0) ** 3)) in GEL)

# ---------------------------------------------------- E. comptes 4.6 / 4.7
print('\nE. SECTIONS 4.6 / 4.7 -- comptes nominaux et intervalles')
chk('n_2a nominal = 620 (derive)', M * (int(math.sqrt(float(d0 / dp))) - 1) == 620)
chk('n_2b nominal = 380 (derive)', M * (k - float(r)) / float(r) == 380)
chk("n_2b' = M k / r = 400 (derive)", M * k / float(r) == 400)
chk('fenetre = M (1-r)/r = 180 (derive)', M * (1 - float(r)) / float(r) == 180)
chk('4.6 intervalle n_2b = [360, 381]', '[360, 381]' in GEL)
for w in sorted(td):
    t0 = math.sqrt(float(d0 / (1 + F(w) ** 2)))
    dep2s, dep2b = TMAX - k * t0, TMAX - k * td[w]
    n2s = math.ceil((dep2b - math.floor(dep2s / dt1) * dt1) / (k * td[w] / M))
    e = math.ceil(dt1 / (k * td[w] / M))
    chk('4.7 n_2s(w2=%s) = %d' % (w, n2s), str(n2s) in GEL)
    chk('4.7 intervalle [620, %d]' % (620 + e), '[620, %d]' % (620 + e) in GEL)
    chk('4.6 intervalle [%d, 621]' % (620 - e), '[%d, 621]' % (620 - e) in GEL)

# ----------------------------------------- F. la mesure regle 15 de 4.7
print('\nF. LA MESURE REGLE 15 -- egaux en exact, pas au bit')
chk('k/400 == r/M en exact', F(k, 400) == r / M, str(F(k, 400)))
d1 = [w for w in sorted(td) if (k * td[w] / 400) != ((td[w] / 10) / M)]
d2 = [w for w in sorted(td) if (k * td[w] / 400) != ((float(r) * td[w]) / M)]
chk('orthographe (tau/10)/20 : ecart a 2.27 et 2.80 seulement',
    d1 == ['2.27', '2.80'], 'ecart a ' + ', '.join(d1))
chk('orthographe (0.1 tau)/20 : ecart aux TROIS w2',
    d2 == ['1.73', '2.27', '2.80'], 'ecart a ' + ', '.join(d2))
chk('4.7 ecrit que le verdict dependrait de l ORTHOGRAPHE',
    'ORTHOGRAPHE' in GEL)

# --------------------------------------------- G. section 9 : les dix-huit
print('\nG. SECTION 9 -- les dix-huit denominateurs, cites VERBATIM')
n_ok = sum(repr(v) in GEL for p in (4, 5, 7)
           for v in JA['degres'][str(p)]['gA_sur_K'].values())
chk('les 18 denominateurs du 85 sont au texte, AU BIT', n_ok == 18, '%d/18' % n_ok)
for p in (4, 5, 7):
    d = disp[p] * (p - 2) / (sum(math.log(v) for v in
                                 JA['degres'][str(p)]['gA_sur_K'].values()) / 6)
    chk('9 bruit_R(p=%d) et son rapport' % p,
        ('%.4e' % d) in GEL and ('%.1fx' % (d / (1 / 1024))) in GEL)

# ------------------------------- H. section 1 : citation ou alteration ?
print('\nH. SECTION 1 -- les citations du v5, contre le TEXTE du v5')
S1 = GEL[GEL.index('1. CE QUI NE CHANGE PAS'):GEL.index('2. LA QUESTION')]
chk('2  : K exacts et A_p identiques au v5 2.3',
    all(x in V5 and x in S1 for x in ('3640/81', '9576/625', '48.98979', '3.14244')))
chk('4  : comptes + sautes == 90 identique au v5 4.5',
    'comptes + sautes == 90' in V5 and 'comptes + sautes == 90' in S1)
chk('5.2: dt_1 = 0.006 et T_MAX = 400 sont au v5 5.2',
    'dt_1 = 0.006' in V5 and 'T_MAX = 400' in V5)
chk('5.6: le v5 qualifie l indice ("la ou il est accessible")',
    'la ou il est accessible' in V5)
chk('5.6: la citation REPREND le qualificatif (R-A-2)',
    'la ou il est accessible' in S1, 'sinon la citation DURCIT la garde')
chk('5.7: le v5 dit "l etat complet a la bascule", au SINGULIER',
    "l'etat complet a la bascule" in V5)
chk('5.7: la citation revient a la lettre du v5 (R-A-1)',
    "l'etat complet a la bascule" in S1)
chk('5.7: la citation n AJOUTE plus rien (R-A-1)',
    "depart d'etage" not in S1, "AJOUTE 'et a chaque depart d etage'")
chk('8  : les huit gardes nommees existent au v5 8',
    all(g in V5 for g in ('G-dt', 'G-k', 'G-s', 'G-w2', 'G-seuil',
                          'G-fen', 'G-lignee', 'G-comptes')))
chk('9  : le v5 porte bien les branches 0 a 7',
    all(('branche %d' % i) in V5 for i in range(8)))
chk('10 : la forme de 10.3 est citee sans alteration',
    'tol_lnA = max(' in S1 and 'max( dispersion de lnA sur la grille' in V5)

# ------------------------------------------ I. le gel temoin cite (R-A-3)
print('\nI. LE GEL TEMOIN CITE PAR LA PORTE -- R-A-3')
chk('le gel temoin CERTIFIE est bien la v9',
    canon('temoin_negatif_pre_enregistrement_v9.md') == '403488b4f6c319e9')
chk('le gel cite la v9 avec son empreinte', '403488b4f6c319e9' in GEL)
chk('le v4 cite la certification croisee de la v9', 'b5da74783e5f97c6' in GEL)
POR = GEL[GEL.index('5. LA PORTE DE QUALIFICATION'):GEL.index('6. LES NOMBRES')]
chk('5 : la porte ne depend plus de la v8',
    'v8 CERTIFIEE' not in POR and 'sous la **v8' not in POR)
chk('5 : la porte porte la v9', 'v9' in POR)
CPT = GEL[GEL.index('11. LES COMPTES'):GEL.index('12. CE QUE CE GEL')]
chk('11 : les comptes du volet T sont ceux de la v9',
    'v9' in CPT and 'v8' not in CPT)
HIST = ('7ba4af8140b7a385', 'ded4a5721601bd1e', 'NON CERTIFIEE', 'remplacee',
        'PAS ete certifiee')
# Sur FENETRE, pas sur ligne : le texte est enveloppe a 72 colonnes et un
# qualificatif ("remplacee", "n'a PAS ete certifiee") tombe souvent a la
# ligne suivante. Une sonde qui coupe au retour chariot rend de faux echecs.
mauvaises = []
for mt in re.finditer(r'\bv8\b', GEL):
    fen = GEL[max(0, mt.start() - 320):mt.end() + 320]
    if not any(t in fen for t in HIST):
        mauvaises.append(GEL[max(0, mt.start() - 40):mt.end() + 40].replace('\n', ' '))
chk('les %d mentions de v8 restantes sont HISTORIQUES'
    % len(re.findall(r'\bv8\b', GEL)),
    not mauvaises, ' | '.join(x[:70] for x in mauvaises))

# ------------------------------------------------ J. la jumelle G-dt (R-A-4)
print('\nJ. SECTION 4.8 -- les comptes de la jumelle -- R-A-4')
BL48 = GEL[GEL.index('4.8 G-dt AUX ETAGES'):GEL.index('4.9 ')]
chk('4.8 porte desormais des intervalles de compte',
    bool(re.search(r'\[\d+, \d+\]', BL48)))
for w in sorted(td):
    e = math.ceil(dt1 / (k * td[w] / M))
    chk('4.8 n_2a jumelle w2=%s = [%d, 1242]' % (w, 2 * (620 - e)),
        '[%d, 1242]' % (2 * (620 - e)) in BL48)
    chk('4.8 n_2s jumelle w2=%s = [1240, %d]' % (w, 2 * (620 + e)),
        '[1240, %d]' % (2 * (620 + e)) in BL48)
chk('4.8 n_2b jumelle = [720, 762]', '[720, 762]' in BL48)
chk("4.8 n_2b' jumelle = 800 exact", '800' in BL48)

# --------------------------------------------- K. t_start : lu ou calcule ?
print('\nK. SECTION 4.7 -- t_start se LIT-il desormais ? -- R-A-5')
BL47 = GEL[GEL.index('4.7 SOUS LE SEUIL'):GEL.index('4.8 G-dt AUX ETAGES')]
chk('4.7 dit que t_start est LU du journal de phase 1',
    'LU du journal de phase 1' in BL47)
chk('4.7 dit qu il ne se RE-calcule jamais', 'jamais RE-calcule' in BL47)
chk('la formule reste, declaree comme le POINT VISE', 'POINT VISE' in BL47)
acc = 0.0
for _ in range(66649):
    acc += dt1
chk('la mesure citee est la mienne, et elle tient',
    ('%.12f' % acc) in BL47 and ('%.12f' % (66649 * dt1)) in BL47,
    'accumulee %.12f contre recalcul %.12f' % (acc, 66649 * dt1))

# ------------------------------------- L. section 4.9 : l exigence NEUVE
print("\nL. SECTION 4.9 -- l'exigence est-elle declaree NEUVE ? -- R-A-1")
chk('4.9 existe', '4.9 ' in GEL)
BL49 = GEL[GEL.index('4.9 '):GEL.index('5. LA PORTE DE QUALIFICATION')]
chk('4.9 se declare EXIGENCE NEUVE et PAS une citation',
    'NEUVE' in BL49 and 'PAS UNE' in BL49)
chk('4.9 rappelle ce que le v5 5.7 exige vraiment (A LA BASCULE)',
    'A LA BASCULE' in BL49)
chk('4.9 enumere les quatre etages', all(e in BL49 for e in ('2a', '2b', '2s', "2b'")))

# ----------------------------- M. les empreintes de 13 : convention nommee ?
print('\nM. SECTION 13 -- les empreintes portent-elles leur CONVENTION ?')
S13 = GEL[GEL.index('13. PIECES CITEES'):]
chk('13 se declare en convention B (sauf mention brut)', 'convention B' in S13)
melange = []
for f in sorted(os.listdir('.')):
    if not f.endswith(('.md', '.py', '.log', '.json')):
        continue
    try:
        cb, br = canon(f), brut(f)
    except Exception:
        continue
    if cb != br and br in S13:
        melange.append((f, br, cb, open(f, 'rb').read().count(13)))
def non_signalees(S):
    """Empreintes BRUTES citees dans S dont LA LIGNE ne nomme pas la convention.

    Le M du v4 rendait toute brute presente ; il ignorait le signalement, donc
    son etiquette mentait. Ici une brute est acceptee si sa propre ligne porte
    a la fois le mot 'brut' et sa convention B."""
    out = []
    for f in sorted(os.listdir('.')):
        if not f.endswith(('.md', '.py', '.log', '.json')):
            continue
        try:
            cb, br = canon(f), brut(f)
        except Exception:
            continue
        if cb == br or br not in S:
            continue
        ligne = next((l for l in S.split('\n') if br in l), '')
        signalee = ('brut' in ligne.lower()) and (cb in ligne)
        if not signalee:
            out.append((f, br, cb, open(f, 'rb').read().count(13)))
    return out


melange = non_signalees(S13)
chk('aucune empreinte BRUTE non signalee dans un bloc convention B',
    not melange,
    ' ; '.join('%s : cite %s (BRUT) ; convention B = %s ; %d CR'
               % (f, br, cb, cr) for f, br, cb, cr in melange))

# ------------------------- N. LE M REECRIT SEPARE-T-IL ENCORE v4 ET v5 ?
print('\nN. LE CONTROLE REECRIT EST-IL DISCRIMINANT ? (v4 contre v5)')
txt_v4 = nrm(open(V4F, encoding='utf-8').read())
S13_v4 = txt_v4[txt_v4.index('13. PIECES CITEES'):]
m4, m5 = non_signalees(S13_v4), non_signalees(S13)
chk('le M reecrit MORD encore sur le v4', bool(m4),
    ' ; '.join('%s cite %s sans nommer sa convention' % (f, br) for f, br, _, _ in m4))
chk('le M reecrit PASSE sur le v5', not m5,
    'le v5 nomme la convention de chaque brute citee')
chk('il SEPARE donc les deux versions', bool(m4) and not m5,
    'un controle qui ne les separerait plus ne certifierait rien')

# ------------------------- O. LE DIFF v4 -> v5 EST-IL CELUI QU'ELLE ANNONCE ?
print('\nO. LE DIFF v4 -> v5, COMPTE PUIS NOMME')
import difflib
_a = open(V4F, encoding='utf-8').read().split('\n')
_c = open(CIBLE, encoding='utf-8').read().split('\n')
_d = list(difflib.unified_diff(_a, _c, 'v4', 'v5', n=0, lineterm=''))
hunks = [l for l in _d if l.startswith('@@')]
plus = sum(1 for l in _d if l.startswith('+') and not l.startswith('+++'))
moins = sum(1 for l in _d if l.startswith('-') and not l.startswith('---'))
print('   %d hunks, +%d / -%d lignes' % (len(hunks), plus, moins))
for l in hunks:
    print('     ', l)
chk('elle annonce CINQ hunks, +12 / -3 : le diff les rend',
    len(hunks) == 5 and plus == 12 and moins == 3,
    '%d hunks, +%d/-%d' % (len(hunks), plus, moins))
fond = [l[1:] for l in _d if l.startswith('+') and not l.startswith('+++')
        and 'a92f60f936a2f75a' in l]
chk('un seul hunk touche le fond, et c est la ligne de la morsure', len(fond) == 1,
    fond[0].strip()[:66] if fond else 'AUCUNE ligne de fond trouvee')
chk('ce hunk ne change ni nombre ni tolerance ni perimetre',
    bool(fond) and all(x in fond[0] for x in ('a92f60f936a2f75a', 'a98b21ecd7c56d95', '119')),
    'il ne fait que nommer la convention d une empreinte deja juste')

# --------------------------------------------------------------- resultat
print('\n' + '=' * 70)
print('CONTROLES : %d ; PASSENT : %d ; MORDENT : %d'
      % (len(OK), sum(OK), len(OK) - sum(OK)))
print('=' * 70)
