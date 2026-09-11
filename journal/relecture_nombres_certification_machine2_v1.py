#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RELECTURE MECANIQUE DES NOMBRES DE MA CERTIFICATION -- machine 2, v1, 11/09/2026.

Feuille de LECTURE (separee des feuilles de MESURE, regle du 28/08). Elle a mordu deux
fois cette semaine sur ma propre prose -- « dix pas de grille » pour 24.50, « une
cinquantaine de fois » pour 43. Je certifie un acte en lui reprochant trois nombres :
rendre ma certification sans le meme controle serait intenable.
"""
import json, math, os, re, sys
import numpy as np

ICI = os.path.dirname(os.path.abspath(__file__))
RAC = r"D:\devs\bocal\BOCAL4"
T = open(os.path.join(ICI, "CERTIFICATION_acte_R4R5_machine2_v1.md"), encoding="utf-8").read()
TP = re.sub(r"\s+", " ", T)
CERT = open(os.path.join(ICI, "certification_acte_R4R5_machine2_v1.log"), encoding="utf-8").read()
J = lambda p: json.load(open(os.path.join(RAC, p), encoding="utf-8"))
OK = []


def chk(q, c, d=''):
    OK.append((q, bool(c)))
    print('  [%s] %-54s %s' % ('OK  ' if c else 'MORD', q[:54], d))


def cite(s):
    return re.sub(r"\s+", " ", s) in TP


print("=" * 78)
print("RELECTURE MECANIQUE DES NOMBRES DE MA CERTIFICATION")
print("=" * 78)

print("\n[A] LE COMPTE DE LA CERTIFICATION")
m = re.search(r"re-derivations : (\d+) ; MORDENT : (\d+)", CERT)
nre, nmo = int(m.group(1)), int(m.group(2))
chk("88 re-derivees, 3 mordent, 85 concordent",
    (nre, nmo) == (88, 3) and cite("88 nombres re-derives") and cite("85 concordent")
    and cite("3 mordent"), "%d / %d" % (nre, nmo))
chk("17/17 a la reception", cite("17/17 verifiees"))
chk("8/8 sur mes empreintes", cite("8/8"))
chk("brut du lot recu 90a3e5b058e7d478", cite("90a3e5b058e7d478"))

print("\n[B] D-CERT-1 : la serie C_P")
L = J(r"R6_periode_libration\run_periode_libration_machine2_v1.json")
R = J(r"R6_periode_libration\resolution_periodes_machine2_v1.json")
run = {round(r["s0"], 2): r for r in L["resultats"]}
res = {round(r["s0"], 2): r for r in R["resultats"]}
for s, av, ap, pc in ((0.15, 0.3307, 0.3262, -1.36), (0.25, 0.3125, 0.3021, -3.33)):
    chk("s0=%.2f : %.4f -> %.4f, soit %.2f %%" % (s, av, ap, pc),
        abs(run[s]["C_P_mesure"] - av) < 5e-5 and abs(res[s]["C_P"] - ap) < 5e-5
        and abs(100 * (res[s]["C_P"] / run[s]["C_P_mesure"] - 1) - pc) < 0.005
        and cite("%.4f" % av) and cite("%.4f" % ap) and cite("%.2f %%" % abs(pc)))
acte = {0.15: 0.3262, 0.20: 0.320, 0.25: 0.3021, 0.30: 0.2808}
eps = {s: 0.05 * s ** 3 / 1.25 for s in acte}
x = np.log([eps[s] for s in sorted(acte)])
y = np.log([acte[s] / eps[s] for s in sorted(acte)])
p4 = np.polyfit(x, y, 1)[0]
chk("pente des quatre valeurs de l'acte = -1.071",
    abs(p4 + 1.071) < 5e-4 and cite("-1.071"), "%.4f" % p4)
p2 = (y[2] - y[0]) / (x[2] - x[0])
chk("pente des deux points resolus = -1.050",
    abs(p2 + 1.050) < 5e-4 and cite("-1.050"), "%.4f" % p2)
ba = np.mean([res[s]["C_P"] / run[s]["C_P_mesure"] - 1 for s in (0.15, 0.25)])
a2 = dict(acte); a2[0.20] *= (1 + ba); a2[0.30] *= (1 + ba)
p3 = np.polyfit(x, np.log([a2[s] / eps[s] for s in sorted(a2)]), 1)[0]
chk("baisse moyenne -2.35 %% et pente corrigee -1.078",
    abs(100 * ba + 2.35) < 0.005 and abs(p3 + 1.078) < 5e-4
    and cite("-2.35 %") and cite("-1.078"), "%.2f %% / %.4f" % (100 * ba, p3))
chk("incertitude 0.007 et 9.8 %% de l'ecart a -1",
    abs(abs(p3 - p4) - 0.007) < 5e-4
    and abs(100 * abs(p3 - p4) / abs(p4 + 1) - 9.8) < 0.15
    and cite("0.007") and cite("9.8 %"),
    "%.4f / %.1f %%" % (abs(p3 - p4), 100 * abs(p3 - p4) / abs(p4 + 1)))
chk("s0 = 0.20 et 0.30 absents de mes pieces",
    0.20 not in run and 0.20 not in res and 0.30 not in run and 0.30 not in res)

print("\n[C] D-CERT-2 : la fourchette de A-6")
P2 = J(r"R4_voletB_D2\run_R4_voletB_machine2_v1.json")["P2"]["colonnes"]
ec = [100 * (c["periode_predite"] / c["periode_mesuree"] - 1) for c in P2]
chk("les trois ecarts 5.42 / 5.73 / 4.66",
    all(abs(a - b) < 0.005 for a, b in zip(ec, [5.42, 5.73, 4.66]))
    and all(cite("%.2f" % v) for v in (5.42, 5.73, 4.66)),
    " ".join("%.2f" % e for e in ec))
chk("le troisieme est HORS de la fourchette annoncee", not (5.4 <= ec[2] <= 5.7))
Cm = sum(c["periode_mesuree"] * c["K"] for c in P2) / 3
chk("5.27 %% sur le coefficient C = P.K",
    abs(100 * (0.64431 / Cm - 1) - 5.27) < 0.01 and cite("5.27 %"),
    "%.2f %%" % (100 * (0.64431 / Cm - 1)))
LOG = open(os.path.join(RAC, "entrant_machine1_2026-09-11_reponse_voletB", "lot",
                        "correction_action_P2_machine1_v1.log"), encoding="utf-8").read()
chk("son propre log porte bien +4.7 pc a s = 0.60",
    "+4.7 pc" in LOG and cite("+4.7 pc"))

print("\n[D] D-CERT-3 : la borne de A-4")
A = J(r"R4_tests_D1\run_R4_voletA_machine2_v1.json")
gel = [r for r in A["resultats"] if "GEL" in str(r["attendu"])]
lib = lambda r: r["s0"] * (3.0 + r["w2"] ** 2) / (r["w2"] ** 2 - 1.0)
rel = max(abs(r["apex"] / lib(r) - 1.0) for r in gel)
ab = max(abs(r["apex"] - lib(r)) for r in gel)
chk("ecart relatif max 9.49e-06 et absolu 5.28e-06",
    abs(rel - 9.49e-6) < 5e-9 and abs(ab - 5.28e-6) < 5e-9
    and cite("9.49e-06") and cite("5.28e-06"), "%.2e / %.2e" % (rel, ab))
chk("la cellule nommee est bien 7|6.00 a s0 = 0.5",
    max(gel, key=lambda r: abs(r["apex"] / lib(r) - 1.0))["p"] == 7
    and cite("7|6.00, s0 = 0.5"))

print("\n[E] LE REGISTRE")
REG = open(os.path.join(ICI, "controle_registre_local_machine2_v1.log"), encoding="utf-8").read()
chk("69 numeros distincts, de 19 a 88, un trou au 20",
    "69 numeros distincts" in REG and "[20]" in REG
    and cite("69 numeros distincts, de 19 a 88") and cite("un seul trou : le 20"))
chk("89 libre localement et delta 88 au bit",
    "89 present au poste                 : False" in REG and "AU BIT" in REG
    and cite("0f8e283fa9499f96"))
chk("je declare NE PAS pouvoir relever le registre ordonnant",
    cite("Je ne peux pas le") and cite("aucun depot git"))

print("\n[F] MES PROPRES FAUX ECHECS, DECLARES")
chk("7 mordants d'abord, 4 de mon fait", cite("7") and cite("quatre etaient de mon fait"))
chk("la ligne 1513 du renvoi nn.6 est citee juste",
    cite("1513") and re.search(r"^.{0,200}nn\.6",
                               open(os.path.join(RAC, "entrant_machine1_2026-09-11_acte_R4R5",
                                                 "lot", "journal_delta_nn_R4R5_v1.md"),
                                    encoding="utf-8").read()[1400:1600], re.S) is not None)

n = sum(1 for _, c in OK if not c)
print("\n" + "=" * 78)
if n:
    print("LA CERTIFICATION PORTE %d ASSERTION(S) FAUSSE(S) -- NE PAS DEPOSER." % n)
    for q, c in OK:
        if not c:
            print("   MORD : " + q)
    sys.exit(1)
print("Relecture : %d/%d assertions chiffrees confirmees a la source." % (len(OK), len(OK)))
print("=" * 78)
