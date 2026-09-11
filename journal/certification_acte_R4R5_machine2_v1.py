#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CERTIFICATION DE L'ACTE DELTA nn (R4/R5) -- machine 2, v1, 11/09/2026.

Machine 1 ecrit en tete de son acte : « chaque nombre de cet acte est RE-DERIVE des
pieces de la section nn.1 [...] ; aucune valeur de lecture n'est crue », et au manifeste :
« m2 re-derive avec ses feuilles, comme au 88 ».

C'est ce que fait cette feuille. Chaque nombre de l'acte qui porte sur une mesure de
machine 2 est repris de MES .json et confronte au texte de l'acte. Je ne relis pas son
log : je recalcule.

CE QUE CETTE FEUILLE NE PEUT PAS FAIRE, ET QUI EST DECLARE :
  - les nombres de la confrontation post hoc de A-1 (31 cellules archivees, A(2.00),
    7|1.45, 7|1.55, 7|2.50) viennent des archives G6, que je detiens mais qui n'ont pas
    ete versees en .json structure : ils sont controles sur ce que mes lots portent, et
    ce qui n'y est pas est DIT non controle, jamais tenu pour vrai.
  - les coefficients derives de machine 1 (a', b, r1, p_c, s_open, C_P derive) ne sont
    pas re-derives : la machinerie D1 n'est pas detenue ici. Je verifie leur COHERENCE
    ARITHMETIQUE avec les nombres qu'ils produisent, pas leur derivation.

Une ligne qui MORD est un defaut de l'acte, a corriger avant depot.
"""
import hashlib, json, math, os, re, sys, unicodedata
import numpy as np

RAC = r"D:\devs\bocal\BOCAL4"
ACTE = os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5", "lot",
                    "journal_delta_nn_R4R5_v1.md")
T = open(ACTE, encoding="utf-8").read()
J = lambda p: json.load(open(os.path.join(RAC, p), encoding="utf-8"))
OK, MORD = [], []


def chk(sec, quoi, cond, detail=''):
    OK.append((sec, quoi, bool(cond)))
    if not cond:
        MORD.append((sec, quoi, detail))
    print('  [%s] %-6s %-46s %s' % ('OK  ' if cond else 'MORD', sec, quoi[:46], detail))


TPLAT = re.sub(r"\s+", " ", T)          # l'acte est formate a ~72 colonnes : une
                                        # citation peut etre coupee en fin de ligne.


def sect(nom):
    """Debut de la SECTION <nom>, ancre en debut de ligne. T.index(nom) prenait la
    PREMIERE occurrence -- un simple renvoi en prose (nn.6 est annonce des la ligne
    1513) -- et rendait un intervalle vide. Un perimetre s'extrait d'une STRUCTURE,
    jamais d'une PROSE : trois controles sont tombes la-dessus."""
    m = re.search(r"^%s" % re.escape(nom), T, re.M)
    if m is None:
        raise SystemExit("section %s introuvable" % nom)
    return m.start()


def cite(s):
    """Cherche dans l'acte APLATI. Sans cela, quatre controles mordaient sur un
    simple retour a la ligne -- un faux echec vaut un controle vide."""
    return re.sub(r"\s+", " ", s) in TPLAT


print("=" * 84)
print("CERTIFICATION DE L'ACTE DELTA nn (R4/R5) -- re-derivation par les feuilles de m2")
print("=" * 84)

# ----------------------------------------------------------------- nn.1 custody
print("\n[nn.1] LES EMPREINTES DE MES PIECES, CITEES PAR L'ACTE")


def emp(p, texte=True):
    raw = open(os.path.join(RAC, p), 'rb').read()
    br = hashlib.sha256(raw).hexdigest()[:16]
    if not texte:
        return br
    can = unicodedata.normalize('NFC', raw.decode('utf-8')) \
        .replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')
    return hashlib.sha256(can).hexdigest()[:16]


for nom, p, att, txt in [
    ("run volet B", r"R4_voletB_D2\run_R4_voletB_machine2_v1.json", "90d4675bebb23f0e", True),
    ("canon volet B", r"R4_voletB_D2\MANIFEST_lot_machine2_voletB_v1.txt", "579cf0a6bed9ac76", True),
    ("ZIP volet B", r"lot_machine2_2026-09-11_voletB_v1.zip", "575f0d8f99b64cb3", False),
    ("run p=8", r"R4_voletB_D2\run_P2_p8_machine2_v1.json", "9a201423743cfde6", True),
    ("controle maxima", r"R4_voletB_D2\controle_maxima_p8_machine2_v1.json", "0787e737e657e705", True),
    ("canon p=8", r"R4_voletB_D2\MANIFEST_lot_machine2_P2_p8_v1.txt", "19edb2ba80f357f1", True),
    ("ZIP p=8", r"lot_machine2_2026-09-11_P2_p8_v1.zip", "752be8b86d1a1d7b", False),
    ("canon erratum", r"R4_voletB_D2\MANIFEST_lot_machine2_accuse_p8_v1.txt", "0040a285bbbbcd10", True),
]:
    chk("nn.1", "%s au bit et cite" % nom, emp(p, txt) == att and cite(att), att)

# ------------------------------------------------------------------------ A-1
print("\n[A-1] LE TEST AVEUGLE DU VOLET E -- six paires")
E = J(r"R4_tests_D1\run_R4_voletE_machine2_v1.json")
att_E = {(7, 3.90): (-0.129976, -0.129976), (7, 4.10): (+0.289269, +0.303414),
         (9, 1.45): (+0.135987, +0.135987), (9, 1.55): (-0.224387, -0.210242),
         (13, 1.90): (-0.110726, -0.110726), (13, 2.10): (+0.111924, +0.111924)}
lig = {(r["p"], round(r["w2"], 2)): r for r in E["resultats"]}
chk("A-1", "les 6 paires du gel sont dans mon run", len(att_E) == 6 and
    all(k in lig for k in att_E), "%d lignes" % len(E["resultats"]))
for (p, w2), (a4, a16) in sorted(att_E.items()):
    r = lig.get((p, w2))
    if r is None:
        chk("A-1", "%d|%.2f present" % (p, w2), False); continue
    chk("A-1", "%d|%.2f : A400 %+.6f et A1600 %+.6f" % (p, w2, a4, a16),
        abs(r["A_400"] - a4) < 5e-7 and abs(r["A_1600"] - a16) < 5e-7
        and cite("%.6f" % abs(a4)) and cite("%.6f" % abs(a16)),
        "mesure %+.6f / %+.6f" % (r["A_400"], r["A_1600"]))
chk("A-1", "6 tenues, 0 falsifiee, 0 muette",
    (E["tenues"], E["falsifiees"], E["muettes"]) == (6, 0, 0)
    and cite("6 tenues, 0 falsifiee, 0 muette"),
    "%s/%s/%s" % (E["tenues"], E["falsifiees"], E["muettes"]))
chk("A-1", "porte ln 1.02 == celle du run",
    abs(E["porte"] - math.log(1.02)) < 1e-12 and cite("porte ln 1.02"))
chk("A-1", "la marche de 3:2 est INVERSEE par rapport a 2:1",
    (lig[(9, 1.45)]["A_400"] > 0 > lig[(9, 1.55)]["A_400"]) and
    (lig[(13, 1.90)]["A_400"] < 0 < lig[(13, 2.10)]["A_400"]))
chk("A-1", "la bande 13 [0.095, 0.125] contient les DEUX mesures de p=13",
    all(0.095 <= abs(lig[(13, w)][k]) <= 0.125 for w in (1.90, 2.10)
        for k in ("A_400", "A_1600")))

# ------------------------------------------------------------------------ A-2
print("\n[A-2] VOLET D -- les trois seuils a T = 6400")
D = J(r"R4_tests_D1\run_R4_voletD_machine2_v2.json")
attD = {"7|2.42": (70, 69, 69, 27), "5|1.50": (63, 62, 62, 34), "7|1.50": (62, 61, 61, 35)}
for r in D["resultats"]:
    g = np.array([float(x) for x in r["grille_repr"]])
    tex = np.array(r["t_exp"])
    idx = {}
    for Tq in (400., 1600., 6400.):
        m = (tex > 0) & (tex <= Tq)
        idx[Tq] = int(np.argmax(m)) if m.any() else None
    cle = "%d|%.2f" % (r["p"], r["w2"])
    if cle not in attD:
        continue
    i4, i16, i64, nex = attD[cle]
    chk("A-2", "%s indices %d / %d / %d" % (cle, i4, i16, i64),
        (idx[400.], idx[1600.], idx[6400.]) == (i4, i16, i64)
        and cite("%d / %d / %d" % (i4, i16, i64)),
        "mesure %s" % [idx[400.], idx[1600.], idx[6400.]])
    n16 = int(((tex > 0) & (tex <= 1600.)).sum())
    n64 = int(((tex > 0) & (tex <= 6400.)).sum())
    chk("A-2", "%s : %d explosifs, identiques a 1600 et 6400" % (cle, nex),
        n16 == n64 == nex, "1600:%d 6400:%d" % (n16, n64))
    chk("A-2", "%s : 0 noeud entre 1600 et 6400" % cle,
        int((((tex > 0) & (tex <= 6400.)) & ~((tex > 0) & (tex <= 1600.))).sum()) == 0)
chk("A-2", "l'acte cite 'aucune explosion nouvelle' et les trois comptes",
    cite("27, 34, 35 explosifs sur 96"))

# ------------------------------------------------------------------------ A-3
print("\n[A-3] VOLET C -- 11|6.00 piegee, 11|2.50 non concluante")
C = J(r"R4_tests_D1\run_R4_voletC_machine2_v1.json")
for r in C["resultats"]:
    g = np.array([float(x) for x in r["grille_repr"]])
    tex = np.array(r["t_exp"])
    n4 = np.where((tex > 0) & (tex <= 400.))[0].tolist()
    n16 = np.where((tex > 0) & (tex <= 1600.))[0].tolist()
    cle = "%d|%.2f" % (r["p"], r["w2"])
    if abs(r["w2"] - 6.00) < 1e-9:
        chk("A-3", "11|6.00 : s0 = 1.873518", abs(r["s0"] - 1.873518) < 5e-7
            and cite("1.873518"), "%.6f" % r["s0"])
        chk("A-3", "11|6.00 : explosifs = noeuds 85 a 95 AUX DEUX fenetres",
            n4 == n16 == list(range(85, 96)) and cite("85 a 95"),
            "400:%s..%s 1600:%s..%s" % (n4[0], n4[-1], n16[0], n16[-1]))
        chk("A-3", "11|6.00 : dln = 0", abs(r.get("dln") or 0.0) < 1e-12)
    if abs(r["w2"] - 2.50) < 1e-9:
        chk("A-3", "11|2.50 : s0 = 0.979962", abs(r["s0"] - 0.979962) < 5e-7
            and cite("0.979962"), "%.6f" % r["s0"])
        chk("A-3", "11|2.50 : a T=400 explosifs = 86 a 95",
            n4 == list(range(86, 96)) and cite("86 a 95"), str(n4))
        ilots = [i for i in n16 if i < 86]
        chk("A-3", "11|2.50 : ilots {47, 48, 50, 53, 56} a T=1600",
            ilots == [47, 48, 50, 53, 56] and cite("{47, 48, 50, 53, 56}"), str(ilots))
        chk("A-3", "11|2.50 : le bloc du haut ne bouge pas",
            [i for i in n16 if i >= 86] == list(range(86, 96)))
        chk("A-3", "11|2.50 : dln = -0.55164", abs(r["dln"] + 0.55164) < 5e-6
            and cite("-0.55164"), "%.5f" % r["dln"])
chk("A-3", "loi directe citee a -0.15403", cite("-0.15403"))

# ------------------------------------------------------------------------ A-4
print("\n[A-4] VOLET A -- GEL 5/5, excursion falsifiee")
A = J(r"R4_tests_D1\run_R4_voletA_machine2_v1.json")
gel = [r for r in A["resultats"] if "GEL" in str(r["attendu"])]
exc = [r for r in A["resultats"] if "GEL" not in str(r["attendu"])]
chk("A-4", "5 cellules GEL et 6 d'excursion", (len(gel), len(exc)) == (5, 6),
    "%d / %d" % (len(gel), len(exc)))
chk("A-4", "T du volet A = 3000 (l'hypothese falsifiee)", float(A["T"]) == 3000.0
    and cite("T = 3000"))
libre = lambda r: r["s0"] * (3.0 + r["w2"] ** 2) / (r["w2"] ** 2 - 1.0)
ecg = max(abs(r["apex"] / libre(r) - 1.0) for r in gel)
chk("A-4", "GEL : apex = excursion libre, 5/5 (l'acte annonce 'a 1e-6 pres')",
    ecg < 1e-6, "max ecart RELATIF %.2e ; absolu %.2e -- la borne juste est 1e-5"
    % (ecg, max(abs(r["apex"] - libre(r)) for r in gel)))
chk("A-4", "excursion : rapport 1.0000 aux 6 cellules",
    all(abs(r["apex"] / libre(r) - 1.0) < 1e-4 for r in exc),
    "max ecart %.2e" % max(abs(r["apex"] / libre(r) - 1.0) for r in exc))
chk("A-4", "zero explosion au volet A",
    not any(r["explose"] for r in A["resultats"]))

# ------------------------------------------------------------------------ A-5
print("\n[A-5] VOLET B -- l'ile a 6|2.00")
B = J(r"R4_voletB_D2\run_R4_voletB_machine2_v1.json")
cp = B["P1"]["colonnes"]["1"]
chk("A-5", "s*(400) = s*(1600) = 1.012586, les deux signes",
    all(abs(B["P1"]["colonnes"][s][k] - 1.012586) < 5e-7
        for s in ("1", "-1") for k in ("s400", "s1600")) and cite("1.012586"))
tex = np.array(cp["t_exp"])
nex = int(((tex > 0) & (tex <= 1600.)).sum())
chk("A-5", "11 explosifs sur 96 en un intervalle, 0 ilot",
    nex == 11 and cp["ilots_1600"] == 0 and cp["explosifs_forment_un_intervalle"]
    and cite("11 explosifs sur 96"), "%d" % nex)
chk("A-5", "noeud 85", int(np.argmax((tex > 0) & (tex <= 1600.))) == 85
    and cite("noeud 85"))
chk("A-5", "ratio 1.0", B["P1"]["ratios"]["1"] == 1.0)
K6 = B["g"] * cp["s1600"] ** 4
chk("A-5", "K*(6|2.00) = 0.052565", abs(K6 - 0.052565) < 5e-7 and cite("0.052565"),
    "%.6f" % K6)
chk("A-5", "r1 cite : 0, 0.094, 0.219, 0.346, 0.465, 0.572 et p_c = 26",
    cite("0, 0.094, 0.219, 0.346, 0.465, 0.572") and cite("p = 26"))

# ------------------------------------------------------------------------ A-6
print("\n[A-6] LA PERIODE D'ENVELOPPE -- p = 6 puis p = 8")
P2 = B["P2"]["colonnes"]
pred6 = [503.4, 206.2, 99.4]
mes6 = [477.5, 195.0, 95.0]
for c, pp, mm in zip(P2, pred6, mes6):
    chk("A-6", "p=6 s=%.2f : predit %.1f, mesure %.1f" % (c["s"], pp, mm),
        abs(c["periode_predite"] - pp) < 0.06 and abs(c["periode_mesuree"] - mm) < 5e-2
        and cite("%.1f" % mm))
ap_eff = [math.pi * 6 * 3 / (c["periode_mesuree"] * c["K"]) for c in P2]
chk("A-6", "a' effectif 92.52, 92.80, 91.86",
    all(abs(a - b) < 0.005 for a, b in zip(ap_eff, [92.52, 92.80, 91.86]))
    and cite("92.52, 92.80, 91.86"),
    " ".join("%.2f" % a for a in ap_eff))
# LE POINT LITIGIEUX : la fourchette de l'ecart a p = 6
ec6 = [100 * (c["periode_predite"] / c["periode_mesuree"] - 1) for c in P2]
chk("A-6", "l'acte ecrit 'BAS de 5.4 a 5.7 pour cent'",
    min(ec6) >= 5.35 and max(ec6) <= 5.75,
    "ecarts mesures : %s" % " ".join("%.2f" % e for e in ec6))
prof6 = [c["profondeur_mesuree"] for c in P2]
chk("A-6", "profondeur p=6 : 0.897 a 0.905 pour 0.868",
    abs(min(prof6) - 0.897) < 5e-4 and abs(max(prof6) - 0.905) < 5e-4
    and abs(2.024 / 2.333 - 0.868) < 5e-4 and cite("0.897 a 0.905"))
chk("A-6", "b/a' = 0.01832 coherent avec r1(6) = 0.0940 et J2_0",
    abs(0.01832 / 0.44444 - 0.0412) < 5e-4 and cite("0.01832"),
    "b/a' / J2_0 = %.4f (l'acte dit 4.1 pc)" % (0.01832 / 0.44444))
# p = 8
p8 = J(r"R4_voletB_D2\run_P2_p8_machine2_v1.json")["colonnes"]
for c, co, na, me in zip(p8, [1464.5, 324.2, 97.3], [1683.9, 372.8, 111.8],
                         [1466.67, 323.33, 100.00]):
    chk("A-6", "p=8 s=%.2f : corrigee %.1f, naive %.1f, mesure %.2f"
        % (c["s"], co, na, me),
        abs(c["periode_corrigee"] - co) < 0.06 and abs(c["periode_naive"] - na) < 0.06
        and abs(c["periode_mesuree"] - me) < 5e-3 and cite("%.2f" % me))
    chk("A-6", "p=8 s=%.2f : corrigee DANS, naive HORS" % c["s"],
        c["bande"][0] <= c["periode_mesuree"] <= c["bande"][1]
        and not (c["bande"][0] <= c["periode_naive"] <= c["bande"][1]))
ctl = J(r"R4_voletB_D2\controle_maxima_p8_machine2_v1.json")["colonnes"]
ctl = [x for x in ctl if x.get("periode_regressee")]
for c, aff, res in zip(ctl, [1464.19, 324.70, 97.83], [-0.02, 0.15, 0.59]):
    chk("A-6", "p=8 affinee s=%.2f : %.2f, residu %+.2f" % (c["s"], aff, res),
        abs(c["periode_regressee"] - aff) < 5e-3
        and abs(100 * (c["periode_regressee"] / c["periode_corrigee"] - 1) - res) < 5e-3
        and cite("%.2f" % aff))
# le 2.82 a le droit d'exister -- mais SEULEMENT dans nn.5, comme defaut retire.
occ = [m.start() for m in re.finditer(r"2\.82", T)]
deb5, fin5 = sect("nn.5"), sect("nn.6")
chk("A-6", "residus de l'erratum ; 2.82 cite QUE dans nn.5 (retire)",
    cite("-0.02, +0.15, +0.59") and all(deb5 < o < fin5 for o in occ),
    "%d occurrence(s) de 2.82, toutes dans nn.5 : %s"
    % (len(occ), all(deb5 < o < fin5 for o in occ)))
chk("A-6", "l'erratum est pris : pas de lecture 10.2 pc a s = 0.55",
    cite("10.2 pour cent de la periode") and cite("erratum m2, pris"))
prof8 = [c["profondeur_mesuree"] for c in p8]
chk("A-6", "profondeur p=8 : 0.917 a 0.930 pour 0.913",
    abs(min(prof8) - 0.917) < 1e-3 and abs(max(prof8) - 0.930) < 1e-3
    and cite("0.917 a 0.930"))
chk("A-6", "a'(8) = 487.1433 coherent avec la corrigee/naive",
    abs(math.pi * 8 * 3 / (0.05 * 487.1433470507544 * 0.35 ** 6) - 1683.9) < 0.6,
    "naive recalculee %.1f" % (math.pi * 8 * 3 / (0.05 * 487.1433470507544 * 0.35 ** 6)))

# ------------------------------------------------------------------------ A-7
print("\n[A-7] LA PERIODE DE LIBRATION")
L = J(r"R6_periode_libration\run_periode_libration_machine2_v1.json")
R = J(r"R6_periode_libration\resolution_periodes_machine2_v1.json")
lib = {round(r["s0"], 2): r for r in L["resultats"]}
chk("A-7", "run : 2450 (s0=0.15) et 500 (s0=0.25)",
    abs(lib[0.15]["periode"] - 2450) < 0.5 and abs(lib[0.25]["periode"] - 500) < 0.5
    and cite("2450") and cite("500"),
    "%.0f / %.0f" % (lib[0.15]["periode"], lib[0.25]["periode"]))
chk("A-7", "bandes [1926, 2519] et [416, 544]",
    abs(lib[0.15]["bande"][0] - 1926) < 1 and abs(lib[0.15]["bande"][1] - 2519) < 1
    and abs(lib[0.25]["bande"][0] - 416) < 1 and abs(lib[0.25]["bande"][1] - 544) < 1
    and cite("[1926, 2519]") and cite("[416, 544]"))
run_l = {round(r["s0"], 2): r for r in L["resultats"]}
res = {round(r["s0"], 2): r for r in R["resultats"]}
chk("A-7", "resolution : 2417 et 483 a plus ou moins 17",
    abs(res[0.15]["periode"] - 2417) < 1 and abs(res[0.25]["periode"] - 483) < 1
    and cite("2417 et 483"),
    "%.0f / %.0f" % (res[0.15]["periode"], res[0.25]["periode"]))
acteCP = {0.15: 0.3262, 0.20: 0.320, 0.25: 0.3021, 0.30: 0.2808}
chk("A-7", "les deux s0 RESOLUS de l'acte sont les miens au chiffre",
    all(abs(res[s]["C_P"] - acteCP[s]) < 5e-4 for s in (0.15, 0.25))
    and cite("0.3262") and cite("0.3021"))
chk("A-7", "les quatre C_P sont dans la bande gelee [0.26, 0.34]",
    all(0.26 <= v <= 0.34 for v in acteCP.values()) and cite("[0.26, 0.34]"))
chk("A-7", "la pente -1.071 se reproduit des quatre valeurs de l'acte",
    abs(np.polyfit(np.log([0.05 * s ** 3 / 1.25 for s in sorted(acteCP)]),
                   np.log([acteCP[s] / (0.05 * s ** 3 / 1.25) for s in sorted(acteCP)]),
                   1)[0] + 1.071) < 5e-4 and cite("-1.071"))
# LE POINT : la serie est-elle HOMOGENE en resolution ?
chk("A-7", "les QUATRE s0 de la serie C_P sont a la meme resolution",
    all(s in res for s in acteCP),
    "s0 = 0.20 et 0.30 ne sont dans AUCUNE de mes pieces ; "
    "la resolution deplace C_P de %.2f %% et %.2f %% aux deux que je detiens"
    % tuple(100 * (res[s]["C_P"] / run_l[s]["C_P_mesure"] - 1) for s in (0.15, 0.25)))

# ------------------------------------------------------------------------ A-9
print("\n[A-9] LES DEUX PREDICTIONS QUI TOMBENT")
R5 = J(r"R5_p5\lecture_R5_PD2_machine2_v1.json")
txt5 = json.dumps(R5, ensure_ascii=False)
chk("A-9", "n = 6 (le site exact ne porte pas l'observable)",
    R5.get("n") == 6 and cite("n = 6"), "n=%s" % R5.get("n"))
chk("A-9", "rho 13/35 et -19/35 presents dans ma lecture R5",
    ("13/35" in txt5 or "0.3714" in txt5) and ("-19/35" in txt5 or "-0.5428" in txt5)
    and cite("13/35") and cite("-19/35"))
chk("A-9", "p = 179/720 et 211/240 cites", cite("179/720") and cite("211/240"))
chk("A-9", "la moitie parite de P1 est declaree tautologie",
    cite("tautologie") and cite("identite de l'integrateur"))
chk("A-9", "mes 96/96 au bit soutiennent cette declaration",
    B["P1"]["colonnes"]["1"]["t_exp"] == B["P1"]["colonnes"]["-1"]["t_exp"])

# --------------------------------------------------------------- nn.3 / nn.5
print("\n[nn.3/nn.5] LA TABLE ET LES DEFAUTS")
bloc3 = T[sect("nn.3"):sect("nn.4")]
lig3 = [L for L in bloc3.splitlines() if re.match(r"^    \S.*\s(m1|m2)\s+[0-9a-f]{16}", L)]
chk("nn.3", "la table porte 10 lignes de prediction", len(lig3) == 10, "%d" % len(lig3))
chk("nn.3", "P2 periode : 'coefficient bas de 5.5 pour cent' coherent avec C",
    abs(100 * (0.64431 / (sum(c["periode_mesuree"] * c["K"] for c in P2) / 3) - 1) - 5.5)
    < 0.25 and cite("5.5 pour cent"),
    "mesure %.2f pc" % (100 * (0.64431 / (sum(c["periode_mesuree"] * c["K"]
                                              for c in P2) / 3) - 1)))
chk("nn.5", "D-R4-6 : le facteur 20.70 de la prose D2",
    cite("20.70") and cite("0.6224"))
chk("nn.5", "D-R4-7 : le +2.82 est retire comme mesure", cite("retire"))
chk("nn.5", "E-m2-5 : mon ecart de custody est repris",
    cite("edite d'un hunk sans renommage"))
chk("nn.5", "D-R4-5 : la tautologie est portee au compte de m1",
    cite("D-R4-5") and cite("tautologie gelee comme prediction"))
chk("nn.9", "l'acte declare ne prendre aucun numero",
    cite("Il ne prend aucun numero") and cite('le corps garde "nn"'))

# ------------------------------------------------------------------- verdict
n = len(MORD)
print("\n" + "=" * 84)
print("re-derivations : %d ; MORDENT : %d" % (len(OK), n))
if n:
    print("\nCE QUI MORD -- a corriger avant depot :")
    for sec, quoi, det in MORD:
        print("  %-6s %s\n         %s" % (sec, quoi, det))
    print("\nVERDICT : CERTIFIE SOUS RESERVE -- les %d point(s) ci-dessus." % n)
else:
    print("VERDICT : CERTIFIE -- les %d nombres re-derives concordent." % len(OK))
print("=" * 84)
