# -*- coding: ascii -*-
"""RELEVE DE SORTIE de l'acte du run du gel "la garde G-1 du moteur et la chaine E-A par etat" -- machine 1, v1.
Il ne reprend pas le script qui a ecrit l'acte : il relit le JSON de la sonde par un code a lui, ecrit du texte du
gel (sections 5 a 8), et cherche chaque nombre dans le texte de l'acte.
Arguments : <acte> <recu> <dossier du gel> <clone du registre> <verdict du run precedent (json)>."""
import sys, os, re, json, math, hashlib, unicodedata, subprocess
ACTE, RECU, GEL, CLONE, PREC = sys.argv[1:6]
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
acte = open(ACTE, encoding="ascii").read()
plat = " ".join(acte.split())
SO = RECU + "/lots/resultat_domaine_G1_chaine_EA/domaine_G1/sortie/"
LC = RECU + "/lots/certification_gel_domaine_G1_chaine_EA/"
mord = []
def C(nom, ok, detail=""):
    print("  %s  %s%s" % ("TIENT" if ok else "MORD ", nom, (" : " + detail) if detail else ""))
    if not ok:
        mord.append(nom)

# --- R1 : relecture independante du JSON de la sonde, du texte du gel
S = json.load(open(SO + "sonde_domaine_G1.json"))
TABLE = {"E1": ("EN", "2.08", "1"), "E2": ("EN", "2.09", "1"), "E3": ("EN", "2.10", "3/2"), "E4": ("EN", "2.12", "3/2"),
         "E5": ("EN", "1.91", "1"), "E6": ("EN", "1.90", "3/2"), "H1": ("HORS", "2.08", "2/3"), "H2": ("HORS", "2.10", "2/3"),
         "H3": ("HORS", "2.12", "1"), "H4": ("HORS", "1.91", "2/3"), "H5": ("HORS", "1.90", "2/3"), "H6": ("HORS", "1.89", "1"),
         "A1": ("EN", "1.95", "1"), "A2": ("EN", "2.05", "1")}
def juge(e):                       # gel, section 5, criteres (1) a (8)
    g2 = [e["Gamma_2D"][k] for k in "234"]; ch = e["chaine"]
    if not e["J_ecart_type"] < 0.2: return False
    if e["n1"] < 0 or e["n2"] < 0: return False
    if e["poids_site"] < 0.5: return False
    if not e["Gamma_2D"]["3"] > 1.33e-12: return False
    if e["suivi"]["2"] < 0.9 or e["suivi"]["4"] < 0.9: return False
    if min(g2) <= 0 or max(g2) > 2 * min(g2): return False
    if ch.get("erreur") or ch.get("vide") or not ch.get("definie"): return False
    cg = ch["gammas"]
    if min(cg) <= 0 or max(cg) > 2 * min(cg): return False
    return True
L = {}
for p in S["points"]:
    lab = [(e["n1"], e["n2"]) for e in p["etats"]]
    js = [e for e in p["etats"] if juge(e) and lab.count((e["n1"], e["n2"])) == 1]      # critere (9)
    q = [e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"] for e in js]
    if len(q) < 6:
        L[p["id"]] = {"statut": "NON LISIBLE"}; continue
    st = "FACTEUR 2" if all(0.5 <= x <= 2 for x in q) else ("DECADE" if all(0.1 <= x * x <= 10 for x in q) else "HORS DECADE")
    t = sorted(q)
    L[p["id"]] = {"statut": st, "classe": "TOMBE" if st == "HORS DECADE" else "TENU", "n": len(q), "min": t[0], "max": t[-1],
                  "med": 0.5 * (t[(len(t) - 1) // 2] + t[len(t) // 2]), "q": t, "premier": (js[0]["n1"], js[0]["n2"], q[0]), "etats": js}
ok = True
for pid in TABLE:
    x = L[pid]; g, w2, f = TABLE[pid]
    ligne = "  %-3s %-5s  %s  x%-3s  %-11s  %-7s  %2d     %.3f  %.3f  %.3f  (%d,%d) q = %.3f" % (
        pid, g, w2, f, x["statut"], x["classe"] if pid[0] != "A" else "(ancre)", x["n"], x["min"], x["max"], x["med"], *x["premier"])
    if ligne not in acte:
        ok = False; print("      ligne absente : " + ligne)
    ok = ok and S["points"][list(TABLE).index(pid)]["garde_moteur"]["statut"] == {"EN": "EN DOMAINE", "HORS": "HORS DOMAINE"}[g]
C("R1 les quatorze lignes de nn.4, relues du JSON par un code independant", ok)
a = [k for k in TABLE if k[0] == "E" and L[k]["classe"] == "TOMBE"]; b = [k for k in TABLE if k[0] == "H" and L[k]["classe"] == "TENU"]
C("R1 a = 3 (E2, E3, E4), b = 3 (H4, H5, H6), verdict", (a, b) == (["E2", "E3", "E4"], ["H4", "H5", "H6"]) and
  "a = 3 : E2, E3 et E4, EN DOMAINE, sont TOMBES. b = 3 : H4, H5 et H6, HORS DOMAINE, sont TENUS" in plat and
  "VERDICT : LA GARDE NE TIENT PAS (a = 3, b = 3). RIVALE : NON TENUE, A UN ETAT PRES." in acte)
PA = {"P1": ("E1", "H1"), "P2": ("E3", "H2"), "P3": ("E4", "H3"), "P4": ("E5", "H4"), "P5": ("E6", "H5")}
okp = True
for nom, (x, y) in PA.items():
    lec = "HOMOGENE" if L[x]["classe"] == L[y]["classe"] else "HETEROGENE"
    ligne = "    %s     %s  %s facteur %-3s  %.3f    %s facteur %-3s  %.3f    %s" % (nom, TABLE[x][1], x, TABLE[x][2], L[x]["med"], y, TABLE[y][2], L[y]["med"], lec)
    if ligne not in acte:
        okp = False; print("      ligne absente : " + ligne)
riv = "TENUE" if all(L[x]["classe"] == L[y]["classe"] for x, y in list(PA.values())[:3]) else "NON TENUE"
C("R1 les cinq paires et la rivale", okp and riv == "NON TENUE" and "La feuille rend RIVALE NON TENUE" in plat)
C("R1 154 etats juges sur 196", sum(L[k]["n"] for k in TABLE) == 154 and sum(len(p["etats"]) for p in S["points"]) == 196 and
  "154 etats juges sur 196" in plat)
# --- R2 : les comptes et les marges de nn.5
R10 = math.sqrt(10.0)
hd = lambda k: sum(x * x > 10 or x * x < 0.1 for x in L[k]["q"])
ph = ("sur ses 13 etats juges, dont %d hors de la demi-decade ; le plus grand q depasse la borne de %.1f pour cent" % (hd("E2"), 100 * (L["E2"]["max"] / R10 - 1)),
      "%d etats sur 13 hors de la demi-decade, le plus grand la depassant de %.1f pour cent" % (hd("E3"), 100 * (L["E3"]["max"] / R10 - 1)),
      "les %d etats juges hors de la demi-decade, le plus petit la depassant de %.1f pour cent" % (hd("E4"), 100 * (L["E4"]["min"] / R10 - 1)),
      "%d etats juges sur 13 au-dessus de 2" % sum(x > 2 for x in L["E1"]["q"]), "%d etats juges sur 7 sous 1/2" % sum(x < 0.5 for x in L["H4"]["q"]),
      "FACTEUR 2 avec %d etats juges, le minimum du gel" % L["H5"]["n"],
      "tous leurs etats juges sont hors de la demi-decade (%d et %d)" % (hd("H2"), hd("H3")))
C("R2 comptes et marges de nn.5", all(x in plat for x in ph) and hd("E4") == L["E4"]["n"] and hd("H2") == L["H2"]["n"] and hd("H3") == L["H3"]["n"],
  " ; ".join(x for x in ph if x not in plat))
# --- R3 : l'etat de H1
e1 = [e for e in L["H1"]["etats"] if (e["chaine"]["gammas"][2] / e["Gamma_2D"]["3"]) ** 2 > 10]
q1 = e1[0]["chaine"]["gammas"][2] / e1[0]["Gamma_2D"]["3"]
ph = "H1 tombe par un seul de ses %d etats juges : rang %d, etiquette (%d,%d), Gamma_2D(3) = %.2e, q = %.4f, a %.2f pour cent au-dessus de la borne de la demi-decade (%.4f). Le bruit des fils sur la cible, 7.32e-14 en absolu, vaut %.1f pour cent de cette lecture" % (
    L["H1"]["n"], e1[0]["rang"], e1[0]["n1"], e1[0]["n2"], e1[0]["Gamma_2D"]["3"], q1, 100 * (q1 / R10 - 1), R10, 100 * 7.32e-14 / e1[0]["Gamma_2D"]["3"])
C("R3 l'etat de H1 qui tient la rivale", len(e1) == 1 and ph in plat and "7.32e-14" in open(RECU + "/lots/resultat_domaine_G1_chaine_EA/POUR_MACHINE1_resultat_domaine_G1_machine2_v1.md").read()
  and S["points"][6]["id"] == "H1" and S["points"][6]["N"] == 74 and {S["points"][12]["N"], S["points"][13]["N"]} == {60, 61})
# --- R4 : les annonces
med = {k: L[k]["med"] for k in TABLE}
A = [True, L["E3"]["statut"] == "HORS DECADE", L["E4"]["statut"] == "HORS DECADE", L["E2"]["statut"] == "HORS DECADE", L["E1"]["statut"] == "DECADE",
     L["H1"]["classe"] == "TENU", L["H6"]["classe"] == "TENU", riv == "TENUE", 3.0 <= med["E3"] <= 4.5,
     L["E5"]["classe"] == "TENU" and L["E6"]["classe"] == "TENU", "HORS DECADE" in (L["H4"]["statut"], L["H5"]["statut"]),
     all((med[k] < 1) == (float(TABLE[k][1]) < 2) for k in TABLE if k[0] != "A"), True]
faux = ["A-%d" % (i + 1) for i, v in enumerate(A) if not v]
lus = re.findall(r"^  (A-\d+) +\(0\.\d+\)  .*? (REALISEE|VRAIES?|FAUSSE)", acte, re.M)
C("R4 annonces : neuf sur treize, fausses A-6, A-8, A-9, A-11", faux == ["A-6", "A-8", "A-9", "A-11"] and len(lus) == 13 and
  [n for n, r in lus if r == "FAUSSE"] == faux and "Neuf sur treize" in plat and "FAUSSE (%.3f)" % med["E3"] in acte)
# --- R5 : le run precedent et les rapports
prec = {x["id"]: x["q_median"] for x in json.load(open(PREC))["points"]}
ph = "%.3f (3/2), %.3f (1) et %.3f (2/3). A 2.05 il avait lu %.3f (3/2), %.3f (1) et %.3f (2/3). Entre les facteurs 2/3 et 3/2, le rapport des q medians vaut %.2f a 2.05 et %.2f a 2.10" % (
    med["E3"], prec["J2"], med["H2"], prec["J4"], prec["A2"], prec["J6"], prec["J6"] / prec["J4"], med["H2"] / med["E3"])
C("R5 lectures du run precedent et rapports entre facteurs", B(PREC) == "4fbc5f7115002054" and ph in plat and
  all(abs(math.log(med[y])) > abs(math.log(med[x])) for x, y in PA.values()), ph if ph not in plat else "")
# --- R6 : les ancres, les gardes
ref = {"A1": ((7, 2), 2.1623273017950654e-10), "A2": ((8, 2), 2.6613925716641374e-09)}
ec = max(abs([e for e in S["points"][i]["etats"] if (e["n1"], e["n2"]) == ref[k][0]][0]["Gamma_2D"]["3"] / ref[k][1] - 1) for i, k in ((12, "A1"), (13, "A2")))
gel = open(GEL + "/gel_domaine_G1_chaine_EA_pre_enregistrement_v1.md", encoding="ascii").read()
tab = {m.group(1): (float(m.group(2)), float(m.group(3))) for m in re.finditer(r"^    (\w\d)  w2 = \S+ +facteur \S+ +D1 (\S+)  c_max (\S+)  N \d+$", gel, re.M)}
eg = max(max(abs(p["garde_moteur"]["D1"] - tab[p["id"]][0]), abs(p["garde_moteur"]["c_max"] - tab[p["id"]][1])) for p in S["points"])
C("R6 ancres a ecart nul ; garde consignee egale a la table du gel", ec == 0.0 and len(tab) == 14 and eg < 5e-7 and "ecart relatif NUL" in plat and "a moins de 5e-7 pres" in plat,
  "ancres %.1e, garde %.1e" % (ec, eg))
# --- R7 : les canons de nn.1
cites = re.findall(r"^ +(\S+\.(?:py|md|json|log))  ([0-9a-f]{16})$", acte, re.M)
ou = {"scripts/": CLONE + "/", "gels/": CLONE + "/", "journal/": CLONE + "/", "domaine_G1/sortie/": RECU + "/lots/resultat_domaine_G1_chaine_EA/",
      "domaine_G1/": LC}
def chemin(n):
    for pre, base in ou.items():
        if n.startswith(pre):
            return base + n
    if n.startswith("POUR_MACHINE1_certification"): return LC + n
    if n.startswith("POUR_MACHINE1_resultat"): return RECU + "/lots/resultat_domaine_G1_chaine_EA/" + n
    if n in ("verdict_rejoue_machine1.json", "lecture_rejouee_machine1.log"): return os.path.dirname(os.path.abspath(ACTE)) + "/" + n
    return GEL + "/" + n
mauvais = [n for n, c in cites if B(chemin(n)) != c]
lots = {"d92a200ac348f0a3": RECU + "/enveloppe/MANIFEST_lot_machine2_certification_gel_domaine_G1_chaine_EA_v1.txt",
        "86a677dc0ff8ba9d": RECU + "/enveloppe/MANIFEST_lot_machine2_resultat_domaine_G1_chaine_EA_v1.txt",
        "1aafb301d7d0ebb3": GEL + "/MANIFEST_lot_machine1_gel_domaine_G1_chaine_EA_v1.txt"}
connus = set(c for n, c in cites) | set(lots)
etrangers = sorted(set(re.findall(r"\b[0-9a-f]{16}\b", acte)) - connus)       # toute empreinte de l'acte est une empreinte relue
C("R7 les %d canons de pieces et les trois canons de lots ; aucune autre empreinte dans l'acte" % len(cites), len(cites) == 19 and not mauvais
  and all(B(p) == c and c in acte for c, p in lots.items()) and not etrangers, " ".join(mauvais + etrangers))
# --- R8 : le registre et le run
def git(*a):
    return subprocess.run(["git", "-C", CLONE] + list(a), check=True, capture_output=True, text=True).stdout.strip()
con = open(SO + "console_domaine_G1.log").read()
C("R8 registre 04053e0, deltas 95 et 96 a 14 h 12 et 14 h 13 ; run de 18:59:46 a 19:50:14, 3028 s",
  git("rev-parse", "--short", "HEAD") == "04053e0" and git("log", "-1", "--format=%ad", "--date=format:%H:%M", "3c26420") == "14:12"
  and git("log", "-1", "--format=%ad", "--date=format:%H:%M", "04053e0") == "14:13" and plat.count("a 14 h 12 et 14 h 13") == 2
  and sorted(re.findall(r"\b\d\d h \d\d\b", plat)) == ["14 h 12", "14 h 12", "14 h 13", "14 h 13", "14 h 57", "14 h 57"]
  and "18:59:46 LANCEMENT DE LA SONDE" in con and "19:50:14 FIN DE LA SONDE code=0 duree=3028 s" in con
  and "de 18:59:46 a 19:50:14 ; sonde code 0 en 3028 s" in plat)
# --- R9 : la forme
lg = acte.split("\n")
C("R9 ASCII, sans pour cent, 100 colonnes au plus, aucune ligne ne commence par un signe double",
  all(ord(ch) < 128 for ch in acte) and "%" not in acte and max(len(l) for l in lg) <= 100 and not [l for l in lg if re.match(r"\s*[;:?]", l)]
  and acte.endswith("-- FIN journal_delta_nn_domaine_G1_chaine_EA_v1 --\n"))
print("RELEVE : %d controle(s) mordent%s" % (len(mord), (" : " + " ; ".join(mord)) if mord else ""))
