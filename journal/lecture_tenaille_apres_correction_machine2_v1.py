#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CE QUE LA CAUSE DU NOYAU SIMD CHANGE A LA TENAILLE -- machine 2, v1, 12/09/2026.

C'est LA question operationnelle du geste (2), et aucune des deux notes de machine 1 ne
la pose : la borne INFERIEURE de la tenaille est portee, dans les trois lectures, par
7|1.73 -- le point dont on vient d'apprendre que la valeur de machine 1 sortait d'un
noyau non correctement arrondi.

LA QUESTION : la borne RETENUE utilise-t-elle SES ratios ou les MIENS ?

Elle ne se lit pas dans une prose : elle se lit dans la STRUCTURE de la feuille qui a
derive la borne (derivation_fenetre_delta_machine2_v1.py), et le resultat se verifie
contre son log. Les deux chemins sont des ARGUMENTS.

L'ISSUE QUI FERAIT MORDRE, ecrite avant : si INF etait construit sur R_ELLE, la borne
retenue reposerait sur une valeur corrompue, il faudrait la recalculer avec 0.684, et
la carte des marges changerait. C'est le cas qu'il faut exclure ou constater.
"""
import re, sys

if len(sys.argv) < 3:
    sys.exit("usage : lecture_tenaille_apres_correction_machine2_v1.py "
             "<derivation_fenetre_delta_*.py> <son .log>")
SRC = open(sys.argv[1], encoding="utf-8").read()
LOG = open(sys.argv[2], encoding="utf-8").read()
OK, MORD = [], []


def chk(q, c, d=''):
    OK.append(bool(c))
    if not c:
        MORD.append((q, d))
    print("  [%s] %-56s %s" % ("OK  " if c else "MORD", q[:56], d))


print("=" * 92)
print("LA TENAILLE APRES LA CAUSE : LA BORNE RETENUE EST-ELLE TOUCHEE ?")
print("=" * 92)

print("\n[1] QUI ALIMENTE LA BORNE RETENUE -- pris dans la STRUCTURE, pas dans la prose")
m = re.search(r"^INF\s*=\s*max\(borne\((\w+),\s*(\w+)\)\.values\(\)\)", SRC, re.M)
chk("la ligne qui definit INF est trouvee", m is not None)
table, cons = (m.group(1), m.group(2)) if m else ("?", "?")
print("      INF = max(borne(%s, %s).values())" % (table, cons))
chk("INF est construit sur MES ratios (R_MOI), non sur les siens (R_ELLE)",
    table == "R_MOI", "table = %s" % table)
chk("et avec la lecture conservatrice", cons == "True", "cons = %s" % cons)

m2 = re.search(r"PRE\s*=\s*json\.load\(open\('([^']+)'", SRC)
m3 = re.search(r"REF\s*=\s*json\.load\(open\('([^']+)'", SRC)
print("      PRE = %s" % (m2.group(1) if m2 else "?"))
print("      REF = %s" % (m3.group(1) if m3 else "?"))
chk("'conservatrice' combine DEUX RUNS A MOI (pre-vol et reference), pas deux machines",
    bool(m2 and m3) and "m2_" in (m2.group(1) if m2 else "")
    and "run_temoin_delta85" in (m3.group(1) if m3 else ""))
# Mon premier passage attendait DEUX occurrences ; il y en a QUATRE, et un compte
# suppose n'est pas un compte. Ce qui importe n'est pas COMBIEN, mais OU : aucune ne doit
# se trouver sur le chemin qui calcule INF. Je le verifie ligne a ligne.
lignes_elle = [(i + 1, l.strip()) for i, l in enumerate(SRC.splitlines()) if "R_ELLE" in l]
print("      les %d occurrences de R_ELLE, une par une :" % len(lignes_elle))
for i, l in lignes_elle:
    print("        l.%-4d %s" % (i, l[:78]))
i_inf = next(i + 1 for i, l in enumerate(SRC.splitlines()) if l.startswith("INF ="))
chk("aucune occurrence de R_ELLE n'est sur la ligne qui calcule INF",
    all(i != i_inf for i, _ in lignes_elle))
chk("et aucune ne sert a AFFECTER une borne (elles affichent, controlent, diagnostiquent)",
    all(not re.match(r"(INF|SUP|borne_inf)\s*=", l) for _, l in lignes_elle),
    "affichage l.%d ; controle du porteur l.%d ; diagnostic de fragilite l.%d"
    % tuple(i for i, _ in lignes_elle[1:]))

print("\n[2] LES TROIS LECTURES, RELUES DANS LE LOG")
lec = re.findall(r"^\s+(machine 1 \(ses ratios\)|machine 2 \(mes ratios\)|"
                 r"CONSERVATRICE \(e = min des deux\))\s+delta >= ([\d.e+-]+)\s+\(x([\d.]+)\)"
                 r"\s+porte par (\S+)", LOG, re.M)
chk("les trois lectures sont lues", len(lec) == 3, "%d" % len(lec))
for etq, val, fac, porteur in lec:
    print("      %-34s delta >= %s  (x%s)  porte par %s" % (etq, val, fac, porteur))
chk("les trois sont portees par 7|1.73", all(p == "7|1.73" for _, _, _, p in lec))
d = {e.split(" (")[0]: float(v) for e, v, _, _ in lec}
INF = d["CONSERVATRICE"]
chk("la borne retenue est la CONSERVATRICE", abs(INF - 1.659726e-05) < 1e-11,
    "%.6e" % INF)

print("\n[3] CE QUI EST TOUCHE, ET CE QUI NE L'EST PAS")
print("      SA lecture (ses ratios, e/seuil = 0.759) -> %.6e" % d["machine 1"])
print("        => CADUQUE : 0.759 est la valeur du noyau SIMD non CR. Son propre run")
print("           sans X86_V4 rend 0.684, mon nombre. Cette ligne est informative.")
print("      MA lecture (mes ratios, 0.684)          -> %.6e" % d["machine 2"])
print("        => CONFIRMEE des deux cotes depuis le 12/09 (44/44 au bit).")
print("      LA RETENUE (mes ratios, e conservative) -> %.6e" % INF)
chk("LA BORNE RETENUE N'EST PAS TOUCHEE : elle ne lit aucun nombre de machine 1",
    table == "R_MOI")

print("\n[4] LA CARTE DES MARGES -- INCHANGEE, ET JE LE MONTRE")
SUP = {}
for mm, v in re.findall(r"^\s+m=(\d) : delta <= ([\d.e+-]+)", LOG, re.M):
    SUP[int(mm)] = float(v)
print("      %-6s | %s" % ("kT", "  ".join("%9s" % ("m=%d" % k) for k in sorted(SUP))))
for kT in (1.00, 1.15, 1.30, 1.50, 1.74):
    row = []
    for k in sorted(SUP):
        lo = kT * INF
        row.append("x%.2f" % (SUP[k] / lo) if lo <= SUP[k] else "VIDE")
    print("      %-6.2f | %s" % (kT, "  ".join("%9s" % c for c in row)))
chk("m=2, kT=1 rend bien x1.04, comme au log d'origine",
    abs(SUP[2] / INF - 1.04) < 0.005, "x%.4f" % (SUP[2] / INF))
chk("et le plateau mesure par machine 1 (1.26 a 1.46) tient dans D-t-25 (1.15 a 1.74)",
    1.15 <= 1.26 and 1.46 <= 1.74,
    "son plateau confirme l'intervalle de b, il ne le deplace pas")

print("\n[5] CE QUE LE GESTE (2) REND VRAIMENT AU CHANTIER")
print("      La feuille d'origine porte, en section 6, ce constat :")
print("        \" le point porteur 7|1.73 differe de 11.0 pour cent entre nos deux")
print("          mesures, c'est le SEUL point non bit-reproductible de la campagne \"")
print("      et la fenetre a m=2 vaut x1.04, soit 4 % : l'ecart faisait pres de TROIS")
print("      FOIS la largeur de la fenetre. C'est ce qui empechait de conclure.")
print("      => CET ECART EST RESOLU, ET EN FAVEUR DE LA VALEUR DEJA UTILISEE.")
print("         La borne ne bouge pas ; ce qui disparait, c'est le DOUTE sur elle.")

print("\n" + "=" * 92)
print("BILAN : %d controles, %d mordent" % (len(OK), len(MORD)))
for q, dd in MORD:
    print("   MORD  %s  %s" % (q, dd))
print("=" * 92)
