# -*- coding: ascii -*-
"""RELEVE de l'acte du run du gel "pont" contre les pieces -- machine 1, v1, 2026-11-18. Dix controles ; aucune 2D.
Les tables de l'acte sont recalculees depuis les fichiers RENDUS PAR MACHINE 2 (et non depuis le rejeu de machine 1).
Code de sortie 0 si aucun controle ne mord.
Usage : python3 -I -B ce_script <acte.md> <dossier du run de machine 2> <gel partie 2.md> <liste des manifestes.json>
                                <liste des pieces.json>"""
import sys, os, re, json, math, hashlib, unicodedata
ACTE, RUN, GEL, MANIFS, LISTE = [a.rstrip("/") for a in sys.argv[1:6]]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
brut = open(ACTE, "rb").read(); T = brut.decode("utf-8"); LG = T.split("\n"); TN = " ".join(T.split()); mord = []
def controle(nom, fautes):
    print("%s : %s" % (nom, "OK" if not fautes else "MORD -- " + " | ".join(str(f)[:90] for f in fautes[:3])))
    if fautes: mord.append(nom.split()[0])
def absents(att): return [a for a in att if a not in T]
def section(n):
    i = [k for k, l in enumerate(LG) if l.startswith("nn.%d " % n)][0]
    j = [k for k, l in enumerate(LG) if k > i and (re.match(r"^nn\.\d+ ", l) or l.startswith("-- FIN"))][0]
    return "\n".join(LG[i:j])
NOMS = ("MG3", "MG4", "MG5", "PG3", "PG4", "PG5")
V = json.load(open(RUN + "/verdict.json")); C = V["cellules"]; F = V["familles"]; Q = V["questions"]
LD = {n: json.load(open("%s/lecture_densite_2d_%s.json" % (RUN, n))) for n in NOMS}; X = LD["MG3"]["X"]
f = []
try: brut.decode("ascii")
except UnicodeDecodeError: f.append("non ASCII")
f += ["ligne trop longue"] * any(len(l) > 100 for l in LG) + ["signe pour cent"] * ("%" in T) + ["espace en fin de ligne"] * any(l != l.rstrip() for l in LG)
f += ["fin absente"] * (not T.endswith("-- FIN journal_delta_nn_pont_v1 --\n"))
controle("A01 forme", f)
pcs = re.findall(r"^    ([0-9a-f]{16})  (\S+)$", section(12), re.M); liste = json.load(open(LISTE))
f = ["compte %d contre %d" % (len(pcs), len(liste))] * (len(pcs) != len(liste))
f += ["%s" % os.path.basename(p) for (c, n), (p, q) in zip(pcs, liste) if n != os.path.basename(p) or c != canon(p)]
controle("A02 les %d pieces de nn.12, canons recalcules" % len(pcs), f)
controle("A03 la ligne de verdict", absents(["VERDICT : (S) %s, (C) %s, (L) %s, (L2) %s." % (F["S"]["verdict"], F["C"]["verdict"], F["L"]["verdict"], F["L2"]["verdict"])]))
att = []
for n in NOMS:
    c = C[n]
    att.append("    %-7s  %-6s  %+.4f a x = %-12s %.2f                   %s" % (n, c["L"]["verdict"], c["L"]["pire_ln_R3"], "%g" % c["L"]["pire_ecart"], c["L"]["pire_part_de_tolerance"], c["L2"]["verdict"]))
    att.append("    %-7s  %-6s  %.4f +- %.4f   %-6s  %.3f               %.3f   %.3f" % (n, c["S"]["verdict"], c["S"]["moyenne"], c["S"]["erreur"], c["C"]["verdict"],
               c["C"]["compte_reduit"]["UN"], c["C"]["compte_reduit"]["DEUX"], c["C"]["rapport"]))
for fam in ("L", "L2", "S", "C"):
    att.append("(%s), " % fam); att.append(": %s ; cellules lisibles %d sur 6%s" % (F[fam]["verdict"], len(F[fam]["lisibles"]), "" if not F[fam]["tombees"] else " ; tombees : " + " ".join(F[fam]["tombees"])))
controle("A04 nn.3 : les tables de verdict, depuis le verdict rendu par machine 2", absents(att))
att = []
for i, x in enumerate(X):
    att.append("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % LD[n]["par_x"][i]["ln_R3"] for n in NOMS))
    att.append("    %-5s  " % ("%g" % x) + "  ".join("%+7.4f" % LD[n]["par_x"][i]["ln_R2"] for n in NOMS))
for n in NOMS:
    c = C[n]
    att.append("    %-7s  %.4f +- %.4f   %.4f   %.4f    %.3f / %.3f          %.2f   %.2f" % (n, c["S"]["moyenne"], c["S"]["erreur"], c["S"]["moyenne_par_groupe"]["UN"],
               c["S"]["moyenne_par_groupe"]["DEUX"], c["S"]["ecart_type_par_groupe"]["UN"], c["S"]["ecart_type_par_groupe"]["DEUX"], c["C"]["moyenne_par_groupe"]["UN"],
               c["C"]["moyenne_par_groupe"]["DEUX"]))
controle("A05 nn.5 : ln R3, ln R2, sommes et comptes (%d lignes)" % len(att), absents(att))
att = ["S = %.4f +- %.4f sur %d boites, soit %+.2f erreur" % (Q["Q1"]["moyenne"], Q["Q1"]["erreur"], Q["Q1"]["boites"], Q["Q1"]["exces_en_erreurs"]),
       "%.3f au groupe UN, %.3f au groupe DEUX" % (Q["Q2_UN"]["rapport"], Q["Q2_DEUX"]["rapport"])]
attb = []
for n in NOMS:
    q4 = C[n]["Q4_vide_ln_chaine3_sur_2d"]; abd = [q4[a] for a in "ABD"]
    attb.append("    %-7s  %.4f              %.4f                 %+.5f a %+.5f       %+.5f" % (n, C[n]["Q3_somme_avec_la_densite_2d"]["moyenne"], C[n]["S"]["moyenne"], min(abd), max(abd), q4["C"]))
controle("A06 nn.6 : les quatre questions", [a for a in att if a not in TN] + absents(attb))
gel = open(GEL, encoding="ascii").read(); f = []
for fam in ("L", "L2", "S", "C"):
    m = re.search(r"^    \(%s\)\s+((?:\d\.\d\d\s+){6})(\d\.\d\d)$" % fam, gel, re.M); pr = [float(v) for v in m.group(1).split()]
    ligne = "    %-7s  " % ("(%s)" % fam) + "  ".join("%.2f %-5s" % (p, "tient" if C[n][fam]["verdict"] == "TIENT" else "TOMBE") for p, n in zip(pr, NOMS)) + " %.2f %s" % (float(m.group(2)), F[fam]["verdict"])
    if ligne not in T: f.append("annonces (%s)" % fam)
controle("A07 nn.7 : les annonces du gel et les issues", f)
M = json.load(open(MANIFS)); s1 = section(1)
controle("A08 nn.1 : les canons des sept lots, relus sur leurs manifestes", [k for k, p in M.items() if canon(p) not in s1])
ET = json.load(open(RUN + "/etat_run.json")); jr = open(RUN + "/run_pont_machine2.log", encoding="utf-8").read(); f = []
duree = re.search(r"\[\s*(\d+) s\] RUN TERMINE", jr).group(1); heure = re.search(r"feu vert ecrit : \S+ (\d\d):(\d\d)", jr).groups()
f += ["calculs"] * (("%d calculs" % len(ET)) not in TN or any(v["relances"] != 0 or v["etat"] != "fait" for v in ET.values()))
f += ["duree"] * ((duree + " s. Aucun calcul relance") not in TN) + ["heure"] * (("a %s h %s a son horloge" % heure) not in TN)
f += ["completude"] * (jr.count("complete (12 barreaux)") != 24 or "24 sorties de densite completes sur 24" not in TN)
controle("A09 nn.1 : les faits du run, depuis l'etat et le journal de machine 2", f)
gn = " ".join(gel.split()); cit = re.findall(r'"(\(L2?\) TOMBEE[^"]+)"', " ".join(section(8).split()))
controle("A10 nn.8 : les %d citations du gel sont mot pour mot" % len(cit), ["aucune citation"] * (len(cit) != 2) + [c[:40] for c in cit if c.rstrip(".") not in gn])
print("RELEVE DE L'ACTE : 10 controles ; %s" % ("0 morsure" if not mord else "%d MORSURE(S) : %s" % (len(mord), ", ".join(mord))))
sys.exit(1 if mord else 0)
