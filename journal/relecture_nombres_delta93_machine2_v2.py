"""relecture_nombres_delta93_machine2_v2.py -- machine 2, 2026-09-29.

v2 DE LA FEUILLE (la v1 est scellee dans mon lot 549d06cc0e1567f0 : une piece emise ne s'edite
pas, elle se versionne). UN CORRECTIF DE FOND, et le report sur le v2 de l'acte.

LE CORRECTIF : la v1 RECOPIAIT a la main, dans des tables ATT_*, les nombres que l'acte ecrit,
pour les confronter aux miens. Deux vices : une recopie peut se tromper de recopie (le controle
n'aurait alors mordu que sur ma faute), et surtout il faut RE-EDITER la feuille a chaque version
de l'acte -- ce que la regle 17 interdit justement. La v2 EXTRAIT de l'acte la table de nn.4 et
la borne du titre, ligne a ligne, et confronte l'extrait a ce que je recalcule. La feuille se
rejoue donc sur n'importe quelle version de l'acte sans etre touchee.

Les sorties portent la VERSION DE L'ACTE relu, jamais un nom fixe : un rejeu sur un v3
n'ecrasera pas le journal du v2. C'est la convention que ma feuille de perimetre appliquait deja
a son manifeste.

RELECTURE DES NOMBRES DE L'ACTE DELTA 93 AUX SOURCES, DEUX JAMBES (forme du 91 et du 92).
Entrant : l'acte journal_delta_nn_constante_A_mesure_v1.md, plume machine 1, projet v1.

  JAMBE 1 -- LES CANONS. Chaque empreinte de 16 hex citee par l'acte est cherchee dans ce que
     je detiens. Une empreinte RESOLUE nomme le fichier qui la porte ; une empreinte NON
     RESOLUE est nommee et comptee -- elle n'est pas une faute en soi (l'acte declare des
     pieces a detention unique), mais elle ne peut pas etre relue par moi, et cela se dit.
  JAMBE 2 -- LES NOMBRES. Chaque nombre que l'acte ecrit et que je peux recalculer ou relire
     dans MA source est confronte a elle. Jamais depuis l'acte, jamais depuis machine 1, sauf
     la ou l'acte cite EXPLICITEMENT un nombre de machine 1 : il est alors relu dans la piece
     de machine 1 que le lot m'a livree, et le controle le dit.

Versionnee depuis la v1 du 92 (nom fixe -> nom versionne, regle candidate 17) : sources du 93
(out_run_delta93, lecture v10, ce_qui_borne v2, test de (d)), et la table A(p) de nn.4, qui
n'existait pas au 92, est relue colonne par colonne -- y compris la colonne du 92, recalculee
sous la convention meme de l'acte (lnA_R sur M1 a p = 4, 5 ; M2 a p = 7).

Deux verbes : chk (peut mordre), note (ne peut pas). Rien n'est edite.
Usage : python DEPOT_delta93/relecture_nombres_delta93_machine2_v2.py <acte.md>   (depuis BOCAL4)
"""
import hashlib
import json
import math
import os
import re
import sys
import unicodedata
from fractions import Fraction as F

ACTE = sys.argv[1] if len(sys.argv) > 1 else 'm2_rec_acte93_v2/lot_interne/journal_delta_nn_constante_A_mesure_v2.md'
V_ACTE = re.search(r'_v(\d+)\.md$', os.path.basename(ACTE)).group(1)
RUNA = 'out_run_delta93/alpha_v16/resultats_alpha.json'
RUNT = 'out_run_delta93/temoin_v16/resultats_temoin.json'
PRED93 = 'm2_lecture_v10_predictions_delta93.json'
PRED92 = 'm2_lecture_v9_predictions_delta92.json'
M1_93 = 'm1_lecture_v10_predictions_delta93.json'
M1_92 = 'm1_lecture_v9_predictions_delta92.json'
BORNE = 'ce_qui_borne_A_machine2_v2.json'
GEL = 'constante_A_pre_enregistrement_v10.md'
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


T = open(ACTE, encoding='utf-8').read()
PLAT = ' '.join(T.split())

out('RELECTURE MACHINE 2 DES NOMBRES DE L ACTE DELTA 93, AUX SOURCES')
out('python %s ; %s' % (sys.version.split()[0], os.path.basename(__file__)))
out('acte : %s  (convention B %s, %d octets)' % (os.path.basename(ACTE), B(ACTE), os.path.getsize(ACTE)))

# ================================================================= JAMBE 1
out()
out('JAMBE 1 -- LES CANONS CITES, RESOLUS DANS CE QUE JE DETIENS')
cites = sorted(set(re.findall(r'\b[0-9a-f]{16}\b', T)))
note('1.0 empreintes distinctes citees par l acte', str(len(cites)))
index = {}
for rac, dn, fs in os.walk('.'):
    dn[:] = [x for x in dn if x not in ('.git', '__pycache__')]
    for f in fs:
        q = os.path.join(rac, f)
        try:
            if os.path.getsize(q) > 40_000_000:
                continue
            index.setdefault(B(q), []).append(q.replace('\\', '/').lstrip('./'))
        except Exception:
            continue
resolues = [c for c in cites if c in index]
non = [c for c in cites if c not in index]
note('1.1 resolues chez moi', '%d / %d' % (len(resolues), len(cites)))
for c in non:
    ctx = re.search(r'([^\n]*\b%s\b[^\n]*)' % c, T)
    out('  [NON RESOLUE] %s -- %s' % (c, (ctx.group(1).strip()[:110]) if ctx else ''))
note('1.2 non resolues', '%d -- l acte ne doit citer que ce qui existe ; ce qui ne resout pas '
     'chez moi est enumere ci-dessus' % len(non))
chk('1.3 : TOUTE empreinte citee par l acte resout dans ce que je detiens', not non,
    ','.join(non) or '%d / %d' % (len(resolues), len(cites)))
chk('1.4 : le gel v10 et l instrument v16 cites sont ceux que J AI CERTIFIES',
    '130ba949482129a7' in index and '634c4aaa2aad7598' in index
    and '130ba949482129a7' in PLAT and '634c4aaa2aad7598' in PLAT)
chk('1.5 : les pieces de MON lot du run 93 se resolvent toutes chez moi',
    all(c in index for c in ('90a0b0ca445989ef', '0c90082db29ee718', '3035b9a733853bf6',
                             '7b8cd71029a65c22', 'ea98455afc1169e5', '5100bde802a588bf',
                             '32fcdc2013702093', '66547ce46ca6d821', 'ba03f8023318c30d',
                             '37eb4a976ce09e26', '6df42b6aeba84547', '7a7cfbe3c8236b91',
                             '3e7d344106027a1d')))
chk('1.6 : les pieces du lot de machine 1 sur le run 93 se resolvent chez moi (lot recu)',
    all(c in index for c in ('c40bc1962170ca87', 'e06cdb73aabc231a', '054a1a3b07892ac7',
                             'e5757a6872866ea7', 'c718fec4a2d3ae66', '0a8fadb16d6981fa',
                             '880f22789d8bd10c', '91fc85380bb6dd77', '3adb387f841ac60a',
                             '7376a0bc05151320')))
chk('1.7 : le v11 et le v17, declares RETIRES, sont quand meme cites et detenus',
    all(c in index for c in ('ac398dc92badbdc5', 'f914156a2c341f4b', 'e28749e8c84207f3',
                             '33d19b7ecb54c9ca', 'c446e2b99e53d2a3'))
    and 'RETIRE' in T)
chk('1.8 : PB-1, l acte n edite rien -- les pieces citees que je detiens portent leur canon',
    all(any(os.path.isfile(p) for p in index[c]) for c in resolues))

# ================================================================= JAMBE 2
out()
out('JAMBE 2 -- LES NOMBRES, RELUS DANS MES SOURCES')
ra = json.load(open(RUNA, encoding='utf-8'))
rt = json.load(open(RUNT, encoding='utf-8'))
p93 = json.load(open(PRED93, encoding='utf-8'))
p92 = json.load(open(PRED92, encoding='utf-8'))
m193 = json.load(open(M1_93, encoding='utf-8'))
m192 = json.load(open(M1_92, encoding='utf-8'))
bo = json.load(open(BORNE, encoding='utf-8'))
deg = ra['degres']
DEGRES = (4, 5, 7)
EST = {4: 'M1', 5: 'M1', 7: 'M2'}      # nn.4 : lnA_R sur M1 a p = 4, 5 ; M2 a p = 7


def A_de(src, p):
    """A(p) sous la convention ECRITE PAR L ACTE : exp de la moyenne des six lnA_R du degre."""
    v = [x for k, x in src['lnA_R'][EST[p]].items() if k.startswith('%d|' % p)]
    return math.exp(sum(v) / len(v)), len(v)


out()
out('2.1 LE RUN 93 (nn.3) : comptes, etages, durees, verdicts, series')
chk('2.1a : comptes 108', ra['attendus_total'] == 108 and 'comptes 108' in PLAT,
    str(ra['attendus_total']))
for k in ('plan', 'G_dt', 'G_dt4'):
    chk('2.1b : %s 18 cellules -- les TROIS niveaux de pas sont la' % k, len(ra[k]) == 18,
        str(len(ra[k])))
chk('2.1c : l acte ecrit "trois niveaux", et je les ai', 'trois niveaux' in PLAT)
for f, att, quoi in (('m2_run_delta93_temoin.log', '54.8', 'volet temoin'),
                     ('m2_run_delta93_alpha.log', '161.8', 'volet alpha')):
    t = open(f, encoding='utf-8', errors='replace').read()
    m = re.search(r'FIN\s+\w+ : .*? -- ([\d.]+) s', t)
    chk('2.1d : duree BOCAL4 du %s = %s s' % (quoi, att),
        m is not None and m.group(1) == att and ('%s s' % att) in PLAT,
        'mon journal rend %s s' % (m.group(1) if m else '?'))
vt = re.findall(r'VERDICT\s+(.+)', open('m2_run_delta93_temoin.log', encoding='utf-8',
                                        errors='replace').read())[-1].strip()
va = re.findall(r'VERDICT\s+(.+)', open('m2_run_delta93_alpha.log', encoding='utf-8',
                                        errors='replace').read())[-1].strip()
chk('2.1e : le verdict temoin de l acte est le mien, mot pour mot',
    'REGLAGE QUALIFIE (bonus T-3 retire)' in PLAT and 'T-3 mord seul' in PLAT
    and vt.startswith('REGLAGE QUALIFIE (bonus T-3 retire)') and 'T-3 mord seul' in vt, vt[:70])
chk('2.1f : le verdict alpha de l acte est le mien, mot pour mot',
    'VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres' in PLAT
    and va == 'VERIFIE -- branche 5 : P-alpha les six par degre ET P-A aux trois degres', va[:70])
chk('2.1g : branche 6 au temoin, branche 5 a l alpha, comme l acte l ecrit',
    str(rt.get('branche', '')).startswith('branche 6')
    and str(ra.get('branche', '')).startswith('branche 5')
    and 'branche 6' in PLAT and 'branche 5' in PLAT,
    'temoin "%s", alpha "%s"' % (str(rt.get('branche'))[:20], str(ra.get('branche'))[:20]))
nser = sum(1 for l in open('out_run_delta93/alpha_v16/MANIFEST.sha256', encoding='utf-8') if l.strip())
chk('2.1h : 83 series au volet alpha, au sha256 de leur manifeste', nser == 83 and '83 series' in PLAT,
    '%d lignes de manifeste' % nser)
faux = []
for l in open('out_run_delta93/alpha_v16/MANIFEST.sha256', encoding='utf-8'):
    if not l.strip():
        continue
    h, nom = l.split()
    q = os.path.join('out_run_delta93/alpha_v16', nom.lstrip('*'))
    if not os.path.isfile(q) or hashlib.sha256(open(q, 'rb').read()).hexdigest() != h:
        faux.append(nom)
chk('2.1i : chacune des 83 series est au sha256 ecrit', not faux, ','.join(faux[:3]) or '0 ecart')
chk('2.1j : G-plancher corrige silencieux aux trois degres, P-A vraie aux trois',
    all(deg[str(p)]['G_plancher_mord'] is False and deg[str(p)]['P_A'] is True for p in DEGRES)
    and 'G-plancher corrige silencieux' in PLAT)
q = p93['q']
chk('2.1k : lecture corrigee jouee 18/18, q dans [3, 5] partout',
    len(q) == 18 and all(3.0 <= v <= 5.0 for v in q.values()) and '18/18' in PLAT
    and 'q dans [3, 5]' in PLAT, 'q de %.3f a %.3f' % (min(q.values()), max(q.values())))

out()
out('2.2 LE REGLAGE (nn.2) : n = 21, delta\', planchers, planchers corriges')
chk('2.2a : delta\' = 1/44100 et b = 21 dans MON run',
    ra['reglage']['delta'] == '1/44100' and ra['reglage']['b'] == 21
    and "1/44100" in PLAT and 'n = 21' in PLAT, str(ra['reglage']['delta']))
gel = open(GEL, encoding='utf-8').read() if os.path.isfile(GEL) else ''
chk('2.2b : kT = 1.3666 et m = 1.5247 sont DANS LE GEL v10 que j ai certifie',
    'kT = 1.3666' in gel.replace('\n', ' ') and 'm = 1.5247' in gel.replace('\n', ' ')
    and '1.3666' in PLAT and '1.5247' in PLAT)
for p, pl in ((4, '1/882000'), (5, '1/637000'), (7, '1/469224')):
    chk('2.2c p=%d : le plancher %s est celui du gel v10' % (p, pl), pl in gel and pl in PLAT)
ATT_PC = {4: '2.804073e-14', 5: '6.604951e-14', 7: '1.717439e-13'}
for p in DEGRES:
    chk('2.2d p=%d : plancher corrige %s == celui de MON run' % (p, ATT_PC[p]),
        '%.6e' % deg[str(p)]['plancher_corrige'] == ATT_PC[p] and ATT_PC[p] in PLAT,
        '%.6e' % deg[str(p)]['plancher_corrige'])
tl = open('derivation_plancher_corrige_machine2_v3.log', encoding='utf-8', errors='replace').read()
chk('2.2e : proj4 = 0.2238, comme l acte l ecrit', '0.223764' in tl and '0.2238' in PLAT)

out()
out('2.3 LA LECTURE v10 (nn.4) : bilan, (a), (b), (c)')
chk('2.3a : lecture v10 = 139 controles, 1 morsure', p93['bilan']['chk'] == 139
    and p93['bilan']['mord'] == 1 and '139 controles, 1 morsure' in PLAT,
    '%d controles, %d morsure' % (p93['bilan']['chk'], p93['bilan']['mord']))
chk('2.3b : la morsure unique est bien (a) a p = 7', '(a) p = 7' in p93['bilan']['noms_mord'][0],
    p93['bilan']['noms_mord'][0][:60])
chk('2.3c : la meme morsure chez machine 1 (sa piece, livree)',
    m193['bilan']['mord'] == 1 and '(a) p = 7' in m193['bilan']['noms_mord'][0]
    and 'la meme sur les deux machines' in PLAT,
    '%d morsure(s) chez elle' % m193['bilan']['mord'])
chk('2.3d : (a) p = 4 TIENT, p = 5 TIENT, p = 7 NON',
    p93['prediction_a'] == {'4': 'TIENT', '5': 'TIENT', '7': 'NON'}, str(p93['prediction_a']))
chk('2.3e : (b) 6/6', p93['prediction_b']['tenus'] == 6 and '6/6' in PLAT,
    str(p93['prediction_b']['tenus']))
chk('2.3f : (c) 18/18 lus', p93['prediction_c']['lus'] == 18 and '(c) 18/18' in PLAT
    or p93['prediction_c']['lus'] == 18 and '18/18' in PLAT, str(p93['prediction_c']['lus']))
rap = [v['rapport'] for v in p93['prediction_c']['points'].values()]
chk('2.3g : (c) -- les 18 rapports c1_R/c1_derive tiennent dans la tolerance de 10 pour cent',
    all(0.9 <= r <= 1.1 for r in rap) and '10 pour cent' in PLAT,
    '%.4f a %.4f' % (min(rap), max(rap)))
MIENS = ['1.0013', '1.0072', '0.9988', '0.9884']
prem = ['%.4f' % p93['prediction_c']['points'][k]['rapport']
        for k in ('4|1.73|1.05', '4|1.73|1.20', '4|2.27|1.05', '4|2.27|1.20')]
chk('2.3h : les quatre premiers rapports que l acte m attribue sont les miens',
    prem == MIENS and all(x in PLAT for x in MIENS), ' '.join(prem))
rm1 = [v['rapport'] for v in m193['prediction_c']['points'].values()]
chk('2.3i : "entre 0.961 et 1.037 chez machine 1" se relit dans SA piece',
    '%.3f' % min(rm1) == '0.961' and '%.3f' % max(rm1) == '1.037'
    and '0.961' in PLAT and '1.037' in PLAT, '%.4f a %.4f' % (min(rm1), max(rm1)))
chk('2.3j : (c) tient aux 18 points des DEUX cotes',
    all(v['etat'] == 'TIENT' for v in p93['prediction_c']['points'].values())
    and all(v['etat'] == 'TIENT' for v in m193['prediction_c']['points'].values()))
chk('2.3k : le facteur d amplitude et le decalage de phase du transport (b)',
    '%.4f' % p93['prediction_b']['facteur_amplitude'] == '0.7015'
    and '%.4f' % p93['prediction_b']['decalage_phase'] == '0.4465'
    and '0.7015' in PLAT and '0.4465' in PLAT,
    '%.4f, %+.4f rad' % (p93['prediction_b']['facteur_amplitude'], p93['prediction_b']['decalage_phase']))

out()
out('2.4 LA TABLE A(p) DE nn.4 -- COLONNE PAR COLONNE, EXTRAITE DE L ACTE ET RECALCULEE CHEZ MOI')
# La table est LUE dans l'acte, pas recopiee ici : six colonnes, trois lignes. Si sa forme
# change, l'extraction mord au lieu de comparer a des nombres perimes.
LIGNE = re.compile(r'^\s+(4|5|7)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.e+-]+)\s*/\s*([\d.e+-]+)\s*$', re.M)
ATT_92, ATT_93, ATT_M1, ATT_TH, ATT_S, ATT_SM1 = {}, {}, {}, {}, {}, {}
for _m in LIGNE.finditer(T):
    _p = int(_m.group(1))
    ATT_92[_p], ATT_93[_p], ATT_M1[_p] = _m.group(2), _m.group(3), _m.group(4)
    ATT_TH[_p], ATT_S[_p], ATT_SM1[_p] = _m.group(5), _m.group(6), _m.group(7)
chk('2.4- : la table A(p) de nn.4 s extrait de l acte, trois lignes, six colonnes',
    sorted(ATT_92) == [4, 5, 7] and all(len(d) == 3 for d in (ATT_93, ATT_M1, ATT_TH, ATT_S, ATT_SM1)),
    '%d ligne(s) extraite(s)' % len(ATT_92))
# La borne se lit partout ou l'acte l'ecrit (titre en capitales, nn.0, nn.4, nn.6) ; elles
# doivent toutes porter le MEME nombre, sinon l'acte se contredit et cela mord.
_bos = sorted(set(re.findall(r'([0-9]+)e-10 (?:relatif|de la forme)', PLAT, re.I)))
BORNE = int(_bos[0]) if len(_bos) == 1 else None
chk('2.4= : la borne relative est ecrite dans l acte, et la MEME a chaque emplacement',
    BORNE is not None, ('%se-10' % BORNE) if BORNE else
    ('bornes divergentes : %s' % _bos if _bos else 'introuvable'))
for p in DEGRES:
    a92, n92 = A_de(p92, p)
    a93, n93 = A_de(p93, p)
    am1, nm1 = A_de(m193, p)
    note('p=%d' % p, 'MES sources : A(92) %.9f (%d pts) ; A(93) %.9f (%d pts) ; machine 1 '
         'A(93) %.9f (%d pts)' % (a92, n92, a93, n93, am1, nm1))
    chk('2.4a p=%d : la colonne "A au 92" de l acte == MA valeur du 92, sous SA convention' % p,
        '%.9f' % a92 == ATT_92[p] and ATT_92[p] in PLAT,
        'acte %s, je relis %.9f' % (ATT_92[p], a92))
    chk('2.4b p=%d : la colonne "A au 93, BOCAL4" == ma valeur du 93' % p,
        '%.9f' % a93 == ATT_93[p] and ATT_93[p] in PLAT,
        'acte %s, je relis %.9f' % (ATT_93[p], a93))
    chk('2.4c p=%d : la colonne "A au 93, machine 1" == la valeur de SA piece' % p,
        '%.9f' % am1 == ATT_M1[p] and ATT_M1[p] in PLAT,
        'acte %s, sa piece rend %.9f' % (ATT_M1[p], am1))
    chk('2.4d p=%d : la colonne theorique == (K/g)^(1/(p-2)) de MA lecture' % p,
        '%.9f' % p93['mesure_A'][str(p)]['A_theorique'] == ATT_TH[p] and ATT_TH[p] in PLAT,
        '%.9f' % p93['mesure_A'][str(p)]['A_theorique'])
    chk('2.4e p=%d : S(93) BOCAL4 == le mien' % p,
        '%.3e' % deg[str(p)]['S_p'] == ATT_S[p] and ATT_S[p] in PLAT, '%.4e' % deg[str(p)]['S_p'])
    chk('2.4f p=%d : S(93) machine 1 == celui de SA piece' % p,
        '%.3e' % m193['S'][str(p)][EST[p]] == ATT_SM1[p] and ATT_SM1[p] in PLAT,
        '%.4e' % m193['S'][str(p)][EST[p]])
    note('2.4g p=%d' % p, 'ecart relatif a la forme auto-semblable : BOCAL4 %+.3e, machine 1 '
         '%+.3e' % (p93['mesure_A'][str(p)]['delta_p'], m193['mesure_A'][str(p)]['delta_p']))
ecarts_tous = [abs(src['mesure_A'][str(p)]['delta_p']) for src in (p93, m193) for p in DEGRES]
chk('2.4h : la borne que l acte ecrit (%se-10) couvre le plus grand ecart des deux machines'
    % BORNE, BORNE is not None and max(ecarts_tous) <= BORNE * 1e-10,
    'l acte ecrit %se-10 ; je mesure au plus %.2e (p = 5), BOCAL4 %.2e et machine 1 %.2e'
    % (BORNE, max(ecarts_tous), abs(p93['mesure_A']['5']['delta_p']),
       abs(m193['mesure_A']['5']['delta_p'])))
chk('2.4j : la borne n est pas non plus trop LACHE (elle serre au 1e-10 pres)',
    BORNE is not None and max(ecarts_tous) > (BORNE - 1) * 1e-10,
    'max %.2e contre une borne de %se-10' % (max(ecarts_tous), BORNE))
chk('2.4i : l accord a la forme auto-semblable tient, lui, a mieux que 1e-09 partout',
    max(ecarts_tous) < 1e-9, 'au plus %.2e' % max(ecarts_tous))
note('2.4 convention', 'A(p) = exp de la moyenne des six lnA_R du degre, estimateur M1 a p = 4 '
     'et 5, M2 a p = 7 -- la convention que l acte ecrit lui-meme en nn.4')

out()
out('2.5 LES ECARTS ENTRE MACHINES (nn.4)')
def confronte(est):
    id_, ec = 0, []
    for p in DEGRES:
        e = est if est != 'mixte' else EST[p]
        for k, v in p93['lnA_R'][e].items():
            if not k.startswith('%d|' % p):
                continue
            w = m193['lnA_R'][e][k]
            if v == w:
                id_ += 1
            else:
                ec.append((abs(v - w), k))
    return id_, ec


for e in ('II', 'M1', 'M2', 'mixte'):
    i_, c_ = confronte(e)
    note('2.5 estimateur %-5s' % e, '%d identiques au bit / 18, ecart max %.4e'
         % (i_, max(c_)[0] if c_ else 0.0))
note('2.5 convention', "l acte ne nomme pas l estimateur sous lequel il compte : 15 sur 18 et "
     "4.2e-10 sont les nombres de l ajustement II. Sous l estimateur de la MESURE (M1 a p = 4 "
     "et 5, M2 a p = 7) ce serait 14 sur 18 et 3.8e-10. Les deux sont vrais ; c est le meme "
     "defaut instrumental. Candidate : une comparaison entre machines se cite avec l estimateur.")
ident, ecarts = confronte('II')
chk('2.5a : 15 des 18 lnA_R sont identiques AU BIT entre les deux machines (sous II)',
    ident == 15 and '15 des 18' in PLAT, '%d identiques, %d en ecart' % (ident, len(ecarts)))
mx = max(ecarts) if ecarts else (0, '-')
chk('2.5b : l ecart maximal vaut 4.2e-10 et il est a p = 4',
    '%.1e' % mx[0] == '4.2e-10' and mx[1].startswith('4|') and '4.2e-10' in PLAT,
    '%.4e a %s' % (mx[0], mx[1]))
chk('2.5c : la cellule exposee est 4|2.27|1.20, le defaut instrumental deja releve au 92',
    mx[1] == '4|2.27|1.20', mx[1])
chk('2.5d : c est cet ecart qui fait differer S(4) entre machines, et S(4) seul',
    '%.3e' % deg['4']['S_p'] != '%.3e' % m193['S']['4']['M1']
    and all('%.3e' % deg[str(p)]['S_p'] == '%.3e' % m193['S'][str(p)][EST[p]] for p in (5,))
    and 'ne se cite pas comme un nombre a deux machines' in PLAT)

out()
out('2.6 LE 92 VERS LE 93 : CE QUE LE PLUS GRAND n A ACHETE (nn.4)')
ATT_R = {4: '0.471', 5: '0.652', 7: '1.396'}
for p in DEGRES:
    r = bo['rapport_S_93_sur_92'][str(p)]
    chk('2.6a p=%d : S(93)/S(92) = %s, comme l acte l ecrit' % (p, ATT_R[p]),
        '%.3f' % r == ATT_R[p] and ATT_R[p] in PLAT, '%.4f' % r)
chk('2.6b : delta\' x 0.735 du 92 au 93 (324/441)',
    '%.3f' % (324 / 441) == '0.735' and '0.735' in PLAT, '%.4f' % (324 / 441))
chk('2.6c : le residu vaut 3e+04 a 8e+04 fois le plancher analytique',
    all(2e4 <= deg[str(p)]['S_p'] / deg[str(p)]['plancher_corrige'] <= 1e5 for p in DEGRES)
    and '3e+04 a 8e+04' in PLAT,
    ' '.join('%.2e' % (deg[str(p)]['S_p'] / deg[str(p)]['plancher_corrige']) for p in DEGRES))
chk('2.6d : le residu est de 2 a 5e-09 en lnA',
    all(2e-9 <= deg[str(p)]['S_p'] <= 5e-9 for p in DEGRES) and '2 a 5e-09' in PLAT,
    ' '.join('%.3e' % deg[str(p)]['S_p'] for p in DEGRES))

out()
out('2.7 LES DEUX REFUTATIONS (nn.5)')
MIENS_45 = ['+0.78', '-2.11', '+1.21']
sig = open('ce_qui_borne_A_machine2_v2.log', encoding='utf-8').read()
chk('2.7a : mes trois ecarts en c a p = 4 sont ceux que l acte m attribue',
    all(x in sig.replace('+0.780', '+0.78').replace('-2.107', '-2.11').replace('+1.205', '+1.21')
        for x in MIENS_45) and all(x in PLAT for x in MIENS_45),
    '+0.780 -2.107 +1.205 dans mon journal')
chk('2.7b : signes MELES a p = 4, UNIQUE a p = 5, chez moi',
    bo['signes_93']['4'] == 'meles' and bo['signes_93']['5'] == 'tous positifs'
    and 'MELE' in T and 'unique a p = 5' in PLAT,
    '%s / %s' % (bo['signes_93']['4'], bo['signes_93']['5']))
chk('2.7c : au 92 le signe etait UNIQUE a p = 4 et 5 -- ce que la v1 avait mesure',
    bo['signes_92']['4'] == 'tous positifs' and bo['signes_92']['5'] == 'tous positifs')
chk('2.7d : ce que je retire est ce que l acte dit que je retire',
    len(bo['retire']) == 2 and 'Q4' in ' '.join(bo['retire'])
    and 'machine 2 le retire' in PLAT and 'Q4' in PLAT, ' ; '.join(bo['retire']))
chk('2.7e : ce_qui_borne_A v2 = 6 controles, 0 morsure', bo['bilan']['chk'] == 6
    and bo['bilan']['mord'] == 0 and '6 controles' in PLAT,
    '%d controles, %d morsure' % (bo['bilan']['chk'], bo['bilan']['mord']))
lnm1 = m193['lnA_R']['M1']
e_m1 = {w: (lnm1['4|%s|1.20' % w] - lnm1['4|%s|1.05' % w]) for w in ('1.73', '2.27', '2.80')}
note('2.7 (d) chez elle', 'ecarts en c a p = 4, relus dans SA piece : '
     + ' '.join('%s %+.3e' % (w, v) for w, v in e_m1.items()))
chk('2.7f : (d) exigeait les SIX positifs a p = 4 et 5 ; a p = 4 elle ne les a pas',
    any(v < 0 for v in e_m1.values()) and 'FAUSSE a p = 4' in T,
    '%d negatif(s) sur 3 chez elle' % sum(1 for v in e_m1.values() if v < 0))
d93 = {w: (p93['lnA_R']['M1']['4|%s|1.20' % w] - p93['lnA_R']['M1']['4|%s|1.05' % w])
       for w in ('1.73', '2.27', '2.80')}
chk('2.7g : le point qui tombe est 4|2.27, et il est NEGATIF SUR LES DEUX MACHINES',
    d93['2.27'] < 0 and e_m1['2.27'] < 0,
    'BOCAL4 %+.3e ; machine 1 %+.3e' % (d93['2.27'], e_m1['2.27']))
chk('2.7h : le v11 et le v17 sont declares RETIRES, et le gel courant reste le v10',
    'RETIRES' in T and 'le gel courant reste le v10' in PLAT
    and "l'instrument le v16" in T.replace('\n', ' '))

out()
out('2.8 CE QUE L ACTE DIT DE MES PROPRES PIECES')
chk('2.8a : ma certification du v10/v16 -- 39 controles, 0 morsure',
    '39 controles, 0 morsure' in PLAT
    and re.search(r'^BILAN : 39 controles, 0 mordent',
                  open('certif_v10_v16_machine2_v1.log', encoding='utf-8').read(), re.M) is not None)
chk('2.8b : selftest 103/103 et banc 58/58 sur BOCAL4',
    '103/103' in PLAT and '58/58' in PLAT
    and re.search(r'^\s*bilan .*58/58|58/58',
                  open('m2_v16_banc.log', encoding='utf-8', errors='replace').read(), re.M) is not None
    and '103/103' in open('m2_v16_selftest.log', encoding='utf-8', errors='replace').read())
chk('2.8c : E18 -- aucun numero pris, aucune regle adoptee, aucun delta recommande',
    'Aucun numero pris (E18)' in T.replace('\n', ' ') or 'aucune regle' in PLAT)
chk('2.8d : l acte ecrit que le residu N EST PAS NOMME',
    "L'ACTE NE LE NOMME PAS" in T or 'SANS NOM' in T.upper())
chk('2.8e : l acte consigne le run 93 comme run d OBSERVATION, E19 levee d un seul cote',
    "run d'OBSERVATION" in T and 'E19' in T and "levee d'un seul cote" in T.replace('\n', ' '))
chk('2.8f : l acte ne recommande PAS de rejouer le run',
    'aucune ne recommande de le rejouer' in PLAT)

# ================================================================= BILAN
out()
out('BILAN : %d controles, %d mordent' % (bilan['chk'], len(bilan['mord'])))
for m in bilan['mord']:
    out('  MORD : %s' % m)
json.dump({'acte': os.path.basename(ACTE), 'canon_acte': B(ACTE),
           'bilan': {'chk': bilan['chk'], 'mord': len(bilan['mord']), 'noms': bilan['mord']}},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'relecture_nombres_delta93_sur_acte_v%s_machine2.json' % V_ACTE), 'w',
               encoding='utf-8', newline='\n'), indent=1, sort_keys=True)
sys.exit(0)
