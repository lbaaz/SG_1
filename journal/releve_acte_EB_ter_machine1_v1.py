# -*- coding: ascii -*-
"""RELEVE DE SORTIE DE L'ACTE DU GEL E-B TER -- machine 1, v1, 2026-11-15. Ce n'est PAS une certification.
Il relit le texte de l'acte et le confronte aux pieces par une AUTRE route que le script d'ecriture : les comptes, les
fenetres et les ecarts sont pris au verdict rendu sur BOCAL4 (verdict_ter.json) et non recalcules des sorties de la
sonde ; ce que ce verdict ne porte pas (lectures, fenetres de L3 rang 5, rejeu) est relu des sorties brutes, en
flottants. Chaque controle cherche dans l'acte les phrases et les lignes de tableau qu'il recalcule.
Usage : python3 -I releve_acte_EB_ter_machine1_v1.py <acte.md> <recu> <dossier du gel> <manifeste du lot du gel>
        <note hors chaine> <manifeste du lot de la note> <clone du registre> <dossier du lot de l'acte>"""
import sys, os, re, json, math, hashlib, unicodedata, subprocess, statistics, glob
ACTE, RECU, GEL, MANIF_GEL, NOTE, MANIF_NOTE, CLONE, LOT = sys.argv[1:9]
NOM = "journal_delta_nn_qualification_EB_ter_v1"

def canon(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def lire(p): return open(p, encoding="utf-8").read().replace("\r\n", "\n")
def plat(t): return " ".join(t.split())
T = lire(ACTE); U = plat(T); LIG = T.split("\n")
RES = []
def ctl(nom, ok, detail):
    RES.append((nom, bool(ok), detail)); print("%s  %s  %s" % (nom, "TIENT" if ok else "MORD ", detail))
def manquent(phrases):
    return [p for p in phrases if plat(p) not in U]
def lignes_manquent(ls):
    return [l for l in ls if l not in LIG]
med = statistics.median
f4 = lambda x: "%.4f" % x
sg4 = lambda x: "%+.4f" % x
def sup(x):
    e = math.floor(math.log10(x)); m = math.ceil(x / 10.0 ** e * 10 - 1e-9) / 10.0
    if m >= 10: m, e = 1.0, e + 1
    return "%.1fe%+03d" % (m, e)

ENV = RECU + "/env/"; LR = RECU + "/lot_resultat_EB_ter/"; LC = RECU + "/lot_certification_gel_EB_ter/"
LL = RECU + "/lot_lecteur_creux_hors_chaine/"; LJ = RECU + "/lot_rejeu_absorbeurs_longs_hors_chaine/"; RUN = LR + "run_EB_ter/"
JUGES = ["C1", "C2", "C3", "C4", "M1", "M2", "M3", "M4", "L1", "L2", "L3", "L4"]

# R01 forme
try:
    T.encode("ascii"); asc = True
except UnicodeEncodeError:
    asc = False
plus_longue = max(len(l) for l in LIG)
ctl("R01", asc and "%" not in T and plus_longue <= 100 and not any(l != l.rstrip() for l in LIG) and T.endswith("-- FIN %s --\n" % NOM)
    and LIG[0].startswith("DELTA nn -- ") and "VERDICT : ESTIMATEUR QUALIFIE." in LIG[1] and "-- PROJET, VERSION 1" in LIG[2]
    and [l[:5] for l in LIG if re.match(r"nn\.\d+ ", l)] == ["nn.%d " % k for k in range(10)] + ["nn.1%d" % k for k in range(6)],
    "ASCII %s ; plus longue ligne %d ; ligne de FIN ; seize sections nn.0 a nn.15" % (asc, plus_longue))

# R02 toute empreinte de 16 chiffres citee est celle d'une piece
connus = {}
def ajouter(racine, etiquette):
    for d, _, fs in os.walk(racine):
        if ".git" in d.split(os.sep) or "__pycache__" in d: continue
        for f in fs:
            p = os.path.join(d, f)
            try: connus.setdefault(canon(p), []).append(etiquette + ":" + os.path.relpath(p, racine).replace(os.sep, "/"))
            except Exception: pass
ajouter(CLONE, "registre"); ajouter(RECU, "recu"); ajouter(LOT, "lot")
for p, e in ((MANIF_GEL, "manifeste du lot du gel"), (MANIF_NOTE, "manifeste du lot de la note"), (NOTE, "note")):
    connus.setdefault(canon(p), []).append(e)
for f in os.listdir(GEL):
    p = os.path.join(GEL, f)
    if os.path.isfile(p):
        try: connus.setdefault(canon(p), []).append("gel:" + f)
        except Exception: pass
hexs = sorted(set(re.findall(r"(?<![0-9a-f.])[0-9a-f]{16}(?![0-9a-f])", T)))
non = [h for h in hexs if h not in connus]
ctl("R02", not non and len(hexs) >= 50, "%d empreintes citees, non resolues : %s" % (len(hexs), non))

# R03 chaque piece nommee de nn.1 porte l'empreinte dite
faux = []; n_nom = 0
sec1 = T[T.index("nn.1 PIECES"):T.index("nn.2 CE QUI")]
for m in re.finditer(r"^ +(\S+\.(?:py|md|json|log))  ([0-9a-f]{16})$", sec1, re.M):
    nom, h = m.group(1), m.group(2); n_nom += 1
    if not any(x.split(":", 1)[1].endswith(nom) or x.split(":", 1)[-1] == nom for x in connus.get(h, []) if ":" in x) and not (
            nom.startswith("note_machine1_piste0") and "note" in connus.get(h, [])):
        faux.append(nom)
for i in JUGES:
    m = re.search(r"\b%s ([0-9a-f]{16})\b" % i, sec1); n_nom += 1
    if not m or m.group(1) != canon(RUN + "sonde_ter_point_%s.json" % i): faux.append("point " + i)
for etiq, p in (("lot du gel", MANIF_GEL), ("lot de la note hors chaine", MANIF_NOTE), ("lot de certification", ENV + "MANIFEST_lot_machine2_certification_gel_EB_ter_v1.txt"),
                ("lot de resultat", ENV + "MANIFEST_lot_machine2_resultat_EB_ter_v1.txt"),
                ('lot "lecteur creux", hors chaine', ENV + "MANIFEST_lot_machine2_lecteur_creux_hors_chaine_v1.txt"),
                ('lot "rejeu sous absorbeurs longs", hors chaine', ENV + "MANIFEST_lot_machine2_rejeu_absorbeurs_longs_hors_chaine_v1.txt")):
    n_nom += 1
    if "    %s  %s" % (etiq, canon(p)) not in LIG: faux.append(etiq)
ctl("R03", not faux and n_nom >= 50, "%d pieces nommees ; empreintes fausses : %s" % (n_nom, faux))

# R04 citations, mot pour mot
src = {"gel": plat(lire(GEL + "/qualification_EB_ter_pre_enregistrement_v1.md")), "gel bis": plat(lire(CLONE + "/gels/qualification_EB_bis_pre_enregistrement_v1.md")),
       "acte 98": plat(lire(CLONE + "/journal/journal_delta_98_ordre2_chaine_EA_v1.md")), "acte 95": plat(lire(CLONE + "/journal/journal_delta_95_qualification_EB_bis_v2.md")),
       "certification": plat(lire(LC + "POUR_MACHINE1_certification_gel_EB_ter_machine2_v1.md")), "resultat": plat(lire(LR + "POUR_MACHINE1_resultat_EB_ter_machine2_v1.md")),
       "envoi": plat(lire(ENV + "ENVOI_machine2_2026-11-15d.txt"))}
tout = " ## ".join(src.values())
gui = [k for k, ch in enumerate(U) if ch == '"']          # guillemets apparies dans l'ordre : l'acte n'en emboite pas
tous_cit = [U[gui[k] + 1:gui[k + 1]] for k in range(0, len(gui) - 1, 2)]
cit = [c_ for c_ in tous_cit if len(c_) >= 30]
absentes = (["guillemets en nombre impair"] if len(gui) % 2 else []) + [c_[:40] for c_ in cit if c_ not in tout]
courtes = [("DERNIER ESSAI", "gel bis"), ("L'operateur peut lever ce garde-fou ; les machines, non", "gel bis"), ("tu peux certifier et jouer si c'est ok ?", "certification"),
           ("tu peux certifier et jouer si c'est ok ?", "envoi"), ("largeur sortante stable sous les variations jouees", "gel"),
           ("toute phrase portant un Gamma depuis juillet est reclassee", "gel bis"), ("La lecture de E-B garde son statut : elle n'est pas qualifiee.", "acte 98")]
absentes += [c_ for c_, s in courtes if ('"%s"' % c_) not in U or c_ not in src[s]]
ouv = {"ouvre": "15/11/2026, 08 h 38", "go": "15/11/2026, 10 h 28"}          # chaque mention datee d'une ouverture, pas la premiere seulement
dites = re.findall(r'"(ouvre|go)" \(([^)]*)\)', U)
absentes += ['ouverture "%s" (%s)' % d for d in dites if ouv[d[0]] != d[1]]
absentes += ["ouverture %s dite %d fois" % (k, sum(d[0] == k for d in dites)) for k in ouv if sum(d[0] == k for d in dites) < 2 or ('"%s" (%s)' % (k, ouv[k])) not in src["gel"]]
ctl("R04", not absentes and len(cit) >= 9, "%d citations longues ; absentes de leur source ou de l'acte : %s" % (len(cit), absentes))

# ---- sources de la seconde route
V2 = json.load(open(RUN + "verdict_ter.json")); DEP = json.load(open(CLONE + "/journal/sonde_ordre2.json")); PD = {p["id"]: p for p in DEP["points"]}
E = [(i, e) for i in JUGES for e in V2["points"][i]["etats"]]
def frac(s):
    a, b = s.split("/"); return int(a) / int(b)

# R05 premier tableau de nn.4 et comptes
l1 = []
for i in JUGES:
    p = V2["points"][i]; e0 = [e for e in p["etats"] if e["rang"] == 0][0]; d = PD[i]
    l1.append("    %-2s  %-7s  %-4s  %s  %s  %3d  %5d  %4d  %3d  %-8s  %s    %s" % (i, d["w2"], "1" if d["facteur"] == "1/1" else d["facteur"], "%+.2f" % (frac(d["w2"]) - 2),
              "%.2e" % d["g"], d["r_c"], p["n_juges"], p["n_qualifies"], p["n_lus_sur_le_plateau"], e0["statut"], "%.3e" % e0["plateaux"]["A"]["Gamma_pl"],
              sg4(math.log(e0["G_dep"] / e0["plateaux"]["A"]["Gamma_pl"]))))
nj = sum(V2["points"][i]["n_juges"] for i in JUGES); nq = sum(V2["points"][i]["n_qualifies"] for i in JUGES); ns = sum(V2["points"][i]["n_lus_sur_le_plateau"] for i in JUGES)
ndep = sum(len(PD[i]["etats"]) for i in JUGES); seuil = math.ceil(9 * nj / 10)
ph = ["%d etats juges sur %d le sont, pour un seuil de %d" % (nq, nj, seuil), "NEUF ETATS SUR DIX AU MOINS (%d sur %d)" % (ns, nj),
      "Aux douze points : %d etats au depot, %d juges, %d sous dix planchers." % (ndep, nj, ndep - nj),
      "%d etats juges sur %d sont QUALIFIES, soit plus des neuf dixiemes (seuil %d) : ESTIMATEUR QUALIFIE. Aucun etat n'est NON LISIBLE." % (nq, nj, seuil),
      "PLATEAU a %d etats sur %d sous A, sous B, sous C et sous D ; accord a A manque a %d etat pour B, %d pour C, %d pour D." % (
          (V2["n_plateau_A"], nj) + tuple(sum(e["plateaux"][x]["statut"] == "PLATEAU" and e["plateaux"][x]["ecart_ln_A"] > 0.05 for _, e in E) for x in "BCD"))]
ok5 = (V2["verdict"] == "ESTIMATEUR QUALIFIE" and V2["issue_depot"] == "LA LECTURE DEPOSEE EST SUR LE PLATEAU A NEUF ETATS SUR DIX AU MOINS" and V2["instrument"] == "TIENT"
       and all(e["plateaux"][x]["statut"] == "PLATEAU" for _, e in E for x in "ABCD") and all(V2["points"][i]["etat_lu"] == "QUALIFIE" for i in JUGES)
       and sum(V2["points"][i]["n_non_lisibles"] for i in JUGES) == 0 and (nj, nq, ns) == (V2["n_juges"], V2["n_qualifies"], V2["n_lus_sur_le_plateau"]))
m5 = lignes_manquent(l1) + manquent(ph)
ctl("R05", ok5 and not m5, "douze lignes et cinq phrases ; %d juges, %d QUALIFIES, %d sur le plateau ; manquent : %s" % (nj, nq, ns, [x[:30] for x in m5]))

# R06 second tableau de nn.4, medianes et plus grands de nn.5
l2 = []
for i in JUGES:
    es = V2["points"][i]["etats"]
    l2.append("    %-2s   %s  %s  %s  %s   %s  %s  %s    %s   %s" % ((i,) + tuple(f4(max(e["plateaux"][x]["etalement"] for e in es)) for x in "ABCD")
              + tuple(f4(max(e["plateaux"][x]["ecart_ln_A"] for e in es)) for x in "BCD") + (f4(med([e["ecart_ln_depot"] for e in es])), f4(max(e["ecart_ln_depot"] for e in es)))))
ET = {x: [e["plateaux"][x]["etalement"] for _, e in E] for x in "ABCD"}; AC = {x: [e["plateaux"][x]["ecart_ln_A"] for _, e in E] for x in "BCD"}
gel = src["gel"]
m = re.search(r"sous A : mediane [0-9.]+, plus grand ([0-9.]+) ; etalement de la meilleure fenetre sous B : mediane [0-9.]+, plus grand ([0-9.]+) ; etalement de la meilleure "
              r"fenetre sous C : mediane [0-9.]+, plus grand ([0-9.]+) ; etalement de la meilleure fenetre sous D : mediane [0-9.]+, plus grand ([0-9.]+) ;", gel)
ph = ["sur les %d etats : %s et %s sous A, %s et %s sous B, %s et %s sous C, %s et %s sous D, pour un seuil de 0.05." % ((nj,) + tuple(v for x in "ABCD" for v in (f4(med(ET[x])), f4(max(ET[x]))))),
      "mediane et plus grand : %s et %s pour B, %s et %s pour C, %s et %s pour D." % tuple(v for x in "BCD" for v in (f4(med(AC[x])), f4(max(AC[x])))),
      "dont les plus grands etalements etaient %s, %s, %s et %s." % m.groups()]
m6 = lignes_manquent(l2) + manquent(ph)
ctl("R06", not m6, "douze lignes et trois phrases ; manquent : %s" % [x[:30] for x in m6])

# R07 la consigne (e), le reclassement, le signe
hors = [(i, e) for i, e in E if not e["lu_sur_le_plateau"]]; ec = [e["ecart_ln_depot"] for _, e in E]
sgn = [math.log(e["G_dep"] / e["plateaux"]["A"]["Gamma_pl"]) for _, e in E]
n_dep = sum(e["statut"] == "QUALIFIE" and e["lu_sur_le_plateau"] for _, e in E); gq = [e["plateaux"]["A"]["Gamma_pl"] for _, e in E if e["statut"] == "QUALIFIE"]
lus = {i: [e for e in V2["points"][i]["etats"] if e["rang"] == 0][0] for i in JUGES}
ph = ["mediane %s et pour plus grande valeur %s. Elle depasse tau a %d etats : %s. Tous les %d sont QUALIFIES" % (f4(med(ec)), f4(max(ec)), len(hors),
          ", ".join("%s rang %d (%s)" % (i, e["rang"], f4(e["ecart_ln_depot"])) for i, e in hors), len(hors)),
      "vaut : %s. La lecture deposee de l'etat lu est sur le plateau a onze points ; a L4 elle est au-dessus de son plateau de %d pour cent." % (
          ", ".join("%s %s" % (i, sg4(math.log(lus[i]["G_dep"] / lus[i]["plateaux"]["A"]["Gamma_pl"]))) for i in JUGES),
          round((lus["L4"]["G_dep"] / lus["L4"]["plateaux"]["A"]["Gamma_pl"] - 1) * 100)),
      "au-dessus du plateau a %d etats, au-dessous a %d ; la mediane de ln(G_dep / Gamma_pl(A)) est %s." % (sum(x > 0 for x in sgn), sum(x < 0 for x in sgn), sg4(med(sgn))),
      "a %d etats sur %d, et a un facteur %.2f pres partout." % (ns, nj, math.ceil(math.exp(max(ec)) * 100) / 100.0),
      "est leve pour ces %d etats, et seulement pour eux, avec pour valeur Gamma_pl(A) : ces valeurs, de %.1e a %.1e, sont au verdict" % (nq, min(gq), max(gq)),
      "consigne (e) tient a cet etat : %d etats (nn.7)." % n_dep,
      "est leve pour %d etats de douze points du delta 98, a la valeur Gamma_pl(A), et pour leur largeur deposee a %d d'entre eux." % (nq, n_dep),
      "a l'etat lu elle l'est a onze points sur douze"]
ok7 = all(e["statut"] == "QUALIFIE" for _, e in hors) and sum(lus[i]["lu_sur_le_plateau"] for i in JUGES) == 11 and not lus["L4"]["lu_sur_le_plateau"]
m7 = manquent(ph)
ctl("R07", ok7 and not m7, "consigne (e) : %d etats hors de tau, mediane %s ; reclassement leve a %d et %d ; manquent : %s" % (len(hors), f4(med(ec)), nq, n_dep, [x[:30] for x in m7]))

# R08 l'etat non QUALIFIE et L3, relus des sorties brutes en flottants
S = {i: json.load(open(RUN + "sonde_ter_point_%s.json" % i)) for i in JUGES}
nqs = [(i, e) for i, e in E if e["statut"] != "QUALIFIE"]
i0, e0 = nqs[0]; brut = [x for x in S[i0]["points"][0]["etats"] if x["rang"] == e0["rang"]][0]
fen = []; marge = 1.0
for k0 in range(-3, 5):
    v = [brut["traj"]["C"][str(k)]["gamma"] for k in range(k0, k0 + 5)]; r = max(v) / min(v)
    fen.append((k0, r - 1.0, math.exp(sum(math.log(x) for x in v) / 5.0))); marge = min(marge, abs(r - 1.05))
pl = sorted([f for f in fen if f[1] <= 0.05], key=lambda f: f[1])
L3 = V2["points"]["L3"]["etats"]; aut = [e for i, e in E if i != "L3"]
pm = max(((e["plateaux"][x]["etalement"], i, e["rang"], x) for i, e in E for x in "ABCD"))
ph = []
if len(nqs) == 1 and len(pl) == 2:
    ph = ["Un seul etat n'est pas QUALIFIE : L3, rang %d, etiquette (%d, %d), G_dep %.2e." % (e0["rang"], e0["n1"], e0["n2"], e0["G_dep"]),
          "|ln(Gamma_pl(C) / Gamma_pl(A))| = %s pour tau = 0.05. B et D s'accordent a A a %s et %s." % (f4(e0["plateaux"]["C"]["ecart_ln_A"]), f4(e0["plateaux"]["B"]["ecart_ln_A"]), f4(e0["plateaux"]["D"]["ecart_ln_A"])),
          "(k0 = %d, etalement %s, valeur %.3e) ; l'autre (k0 = %d, etalement %s, valeur %.3e) est a %s de A." % (pl[0][0], f4(pl[0][1]), pl[0][2], pl[1][0], f4(pl[1][1]), pl[1][2],
              f4(abs(math.log(pl[1][2] / e0["plateaux"]["A"]["Gamma_pl"])))),
          "L3 (w2 = %s, facteur %s, g = %.2e) est le point juge de plus fort couplage" % (PD["L3"]["w2"], PD["L3"]["facteur"], PD["L3"]["g"]),
          "sous les quatre absorbeurs : %s, %s, %s et %s ; aux onze autres points, sur %d etats, ils sont %s, %s, %s et %s (tous a L4)." % (
              tuple(f4(max(e["plateaux"][x]["etalement"] for e in L3)) for x in "ABCD") + (len(aut),) + tuple(f4(max(e["plateaux"][x]["etalement"] for e in aut)) for x in "ABCD")),
          "La plus petite marge du run est a %s, rang %d, sous %s : etalement %s pour un seuil de 0.05." % (pm[1], pm[2], pm[3], f4(pm[0])),
          "Apres le %s de L3 rang 5, le plus grand ecart de C a A est %s." % (f4(e0["plateaux"]["C"]["ecart_ln_A"]), f4(sorted(e["plateaux"]["C"]["ecart_ln_A"] for _, e in E)[-2])),
          "Les treize autres etats de L3 sont QUALIFIES, son etat lu compris."]
ok8 = (len(nqs) == 1 and (i0, e0["rang"]) == ("L3", 5) and e0["echecs"] == ["(c) accord C / A : |ln| = 0.0659"] and len(pl) == 2 and pl[0][0] == e0["plateaux"]["C"]["k0"]
       and abs(pl[0][2] / e0["plateaux"]["C"]["Gamma_pl"] - 1) < 1e-12 and marge > 1e-3 and PD["L3"]["g"] == max(PD[i]["g"] for i in JUGES)
       and all(max((e["plateaux"][x]["etalement"], i) for i, e in E if i != "L3")[1] == "L4" for x in "ABCD") and sum(e["statut"] == "QUALIFIE" for e in L3) == 13)
m8 = manquent(ph) if ph else ["pas un seul etat non QUALIFIE a deux fenetres"]
ctl("R08", ok8 and not m8, "L3 rang 5 sous C : fenetres a PLATEAU %s ; plus petite distance d'une fenetre a la borne %.4f ; manquent : %s" % (
    [(f[0], f4(f[1])) for f in pl], marge, [x[:30] for x in m8]))

# R09 les lectures, relues des sorties brutes
n = 0; suiv = 0; it = {}; poids = 1.0; res = 0.0; rep = 0
for i in JUGES:
    for e in S[i]["points"][0]["etats"]:
        for x in "ABCD":
            for r in e["traj"][x].values():
                n += 1; suiv += bool(r["suivi"]); it[r["iterations"]] = it.get(r["iterations"], 0) + 1; poids = min(poids, r["poids_site"]); rep += bool(r["decalage_repris"])
                res = max(res, r["residu"] / max(1.0, math.hypot(r["E_re"], r["gamma_im"] / 2.0)))
J0 = json.load(open(RUN + "sonde_ter_etage0.json")); JA = json.load(open(RUN + "sonde_ter_ancres.json")); J1 = json.load(open(RUN + "sonde_ter_etage1.json"))
ni = 0
for q in (J0, JA):
    for p in q["points"]:
        for e in p["etats"]:
            for tr in e["traj"].values():
                for r in tr.values(): ni += 1; rep += bool(r["decalage_repris"])
for g in ("temoin", "temoin_negatif"):
    for t in J1[g]:
        for tr in t["traj"].values():
            for r in tr.values(): ni += 1; rep += bool(r["decalage_repris"])
ph = ["Les %d lectures de l'etage 2 sont toutes suivies : %d en deux iterations, %d en trois, %d en quatre ; poids au site au moins %.3f pour un seuil de 0.5 ; residu rapporte a "
      "max(1, |lambda|) au plus %s pour un critere de 1e-11. La garde de singularite du bloc ne s'est declenchee a aucune des %d lectures du run." % (
          n, it.get(2, 0), it.get(3, 0), it.get(4, 0), math.floor(poids * 1000) / 1000.0, sup(res), n + ni),
      "G-T5 : 84, 192, 96 et 96 lectures a l'instrument, %d a l'etage 2." % n]
m9 = manquent(ph)
ctl("R09", n == suiv == 6576 and rep == 0 and ni == 468 and sorted(it) == [2, 3, 4] and res < 1e-11 and not m9,
    "%d lectures, %d suivies, iterations %s, poids %.4f, residu %.2e, reprises %d ; manquent : %s" % (n, suiv, sorted(it.items()), poids, res, rep, [x[:30] for x in m9]))

# R10 l'instrument
VI = json.load(open(RUN + "verdict_ter_instrument.json")); TP = VI["etage1"]["detail"]["TP"]; TN = VI["etage1"]["detail"]["TN"]
logi = lire(RUN + "lecture_ter_instrument.log"); bo = dict(re.findall(r"TP (j0[68]) g = \S+ A : .*contre ([0-9.]+) : TIENT", logi))
tn3 = [t["traj"][x]["3"]["gamma"] for t in J1["temoin_negatif"] for x in "ABCD"]; tne = [TN[a][x]["etalement"] for a in TN for x in "ABCD"]
tnr = max(abs(t["traj"][x][str(k)]["gamma"] / t["traj"][x][str(k + 1)]["gamma"] - 2.0) for t in J1["temoin_negatif"] for x in "ABCD" for k in range(-3, 8))
ph = ["84 lectures sur 84 dans la tolerance ; plus grand ecart absolu %.2e, plus grand ecart relatif au-dessus de mille planchers %.1e." % (
          VI["etage0"]["pire_ecart_absolu"], VI["etage0"]["pire_ecart_relatif_au_dessus_de_mille_planchers"]),
      "192 lectures sur 192, memes statuts de suivi ; plus grand |ln| a la reference de machine 1 : %.1e, pour une tolerance de 1e-6." % VI["ancres"]["pire_ecart_ln"],
      "vaut au plus %s a j = 6 et %s a j = 8, pour des bornes de %s et %s." % (f4(max(TP["j06"][x]["ecart_ln"] for x in "ABCD")), f4(max(TP["j08"][x]["ecart_ln"] for x in "ABCD")),
                                                                              f4(float(bo["j06"])), f4(float(bo["j08"]))),
      "va de %.2f a %.2f, la ou une largeur proportionnelle a eta donne 15 ; ses largeurs vont de %.1e a %.1e a k = 3." % (min(tne), max(tne), min(tn3), max(tn3)),
      "L'ecart du rapport a 2 est de %s au plus dans le run, soit %s en relatif" % (f4(tnr), f4(tnr / 2)),
      "les ancres du run sont a %.1e de la reference de machine 1." % VI["ancres"]["pire_ecart_ln"],
      "Selftest de la feuille : 68 sur 68, sur BOCAL4 et chez machine 1."]
ok10 = (VI["instrument"] == "TIENT" and VI["etage0"]["lectures"] == 84 and VI["ancres"]["lectures"] == 192 and not VI["etage0"]["hors"] and not VI["ancres"]["hors"]
        and all(TP[j][x]["statut"] == "PLATEAU" for j in TP for x in "ABCD") and all(TN[a][x]["statut"] == "PAS DE PLATEAU" for a in TN for x in "ABCD")
        and "selftest : 68 tenus sur 68" in logi and "selftest : 68 tenus sur 68" in lire(RUN + "lecture_ter.log")
        and "selftest : 68 tenus sur 68" in lire(LOT + "/lecture_ter_rejouee_machine1.log"))
m10 = manquent(ph)
ctl("R10", ok10 and not m10, "instrument %s ; temoin negatif : ecart a 2 de %s ; manquent : %s" % (VI["instrument"], f4(tnr), [x[:30] for x in m10]))

# R11 le pilote et les couts
pil = lire(RUN + "pilote_EB_ter.log"); hh = re.findall(r"^2026-11-15 (\d\d):(\d\d):(\d\d) (.*)$", pil, re.M)
def quand(motif):
    x = [h for h in hh if motif in h[3]]; assert len(x) == 1, motif
    return int(x[0][0]), int(x[0][1]), int(x[0][2])
deb, ins, fin = quand("DEBUT DU PILOTE"), quand("VERDICT DE L INSTRUMENT"), quand("FIN DU PILOTE")
app = re.findall(r"FIN  (.+?)\s+code=(\d+)(?: duree=(\d+) s)?", pil); du = {a[0]: int(a[2]) for a in app if a[2]}
dp = {i: du["point_" + i] for i in JUGES}; cum = sum(S[i]["duree_s"] for i in JUGES)
sec = lambda t: t[0] * 3600 + t[1] * 60 + t[2]
ph = ["debut a %d h %02d min %02d s, fin a %d h %02d min %02d s, %d secondes ; les dix-sept appels a code 0" % (deb + fin + (sec(fin) - sec(deb),)),
      "etage0 (%d s), ancres (%d s), etage1 (%d s), trois processus" % (du["etage0"], du["ancres"], du["etage1"]),
      "un processus par point, de %d s (%s) a %d s" % (min(dp.values()), min(dp, key=dp.get), max(dp.values())),
      "un pilote qui verifie %d canons" % len(re.findall(r"^\S+ \S+ canon .* OK$", pil, re.M)),
      "en ont pris %.1f (%d s), pour %d minutes d'horloge." % (cum / 3600.0, round(cum), round((sec(fin) - sec(ins)) / 60.0)),
      "Windows AMD64, 16 coeurs, python 3.11.9, numpy 2.2.6, scipy 1.15.3, un fil par processus, sur secteur.", "lot scelle a 13 h 42 min 03 s",
      "Le gel annoncait de l'ordre de 7.1 h de calcul cumule pour l'etage 2", "la note d'accompagnement du gel la disait grossiere."]
pf = S["L3"]["plateforme"]
ok11 = (len(app) == 17 and all(a[1] == "0" for a in app) and ("DUREE TOTALE DU RUN : %d s" % (sec(fin) - sec(deb))) in pil
        and (pf["systeme"], pf["machine"], pf["coeurs"], pf["python"], pf["numpy"], pf["scipy"]) == ("Windows", "AMD64", 16, "3.11.9", "2.2.6", "1.15.3")
        and "2 = secteur" in pil and ": '2'" in pil and "scelle a 13 h 42 min 03 s" in src["resultat"] and "de 7.1 h de calcul cumule" in gel
        and "l'estimation pour BOCAL4 est grossiere" in plat(lire(GEL + "/POUR_MACHINE2_gel_EB_ter_machine1_v1.md")))
m11 = manquent(ph)
ctl("R11", ok11 and not m11, "%d appels a code 0 ; %d s ; cumul %.0f s ; manquent : %s" % (len(app), sec(fin) - sec(deb), cum, [x[:30] for x in m11]))

# R12 les annonces
s11 = gel[gel.index("## 11."):gel.index("## 12.")]
pa = dict(re.findall(r"(A-\d+) [^:]*?(?:\([^)]*\))?[^:]*?: (0\.\d\d)\.", s11[s11.index("A-3 "):]))
neg = [i for i in JUGES if frac(PD[i]["w2"]) < 2]
nnq = {i: V2["points"][i]["n_juges"] - V2["points"][i]["n_qualifies"] for i in JUGES}
vr = {"A-3": all(V2["points"][i]["etat_lu"] == "QUALIFIE" for i in JUGES if i != "L3"), "A-4": nnq["L3"] == max(nnq.values()),
      "A-5": max(max(e["plateaux"]["A"]["etalement"], e["plateaux"]["B"]["etalement"]) for i, e in E if i in neg) <= 0.02, "A-6": max(AC["B"]) <= 0.02,
      "A-7": VI["instrument"] == "TIENT", "A-8": True, "A-9": 0.01 <= med(ec) <= 0.04, "A-10": sum(V2["points"][i]["n_non_lisibles"] for i in JUGES) <= 3}
lg = []
for k in ("A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10"):
    mm = [l for l in LIG if l.startswith("    %-4s (%s) " % (k, pa.get(k, "?")))]
    if len(mm) != 1 or (" VRAIE" in mm[0]) != vr[k] or (" FAUSSE" in mm[0]) == vr[k]: lg.append(k)
a5 = max(max(e["plateaux"]["A"]["etalement"], e["plateaux"]["B"]["etalement"]) for i, e in E if i in neg)
ph = ["(%s au plus)" % f4(a5), "(%s au plus)" % f4(max(AC["B"])), "VRAIE (%s)" % f4(med(ec)), "VRAIE (1 ; 0 ailleurs)",
      "Les huit annonces a deux issues sont vraies, pour une somme de probabilites de %.2f." % sum(float(v) for v in pa.values()),
      "A-1 : la plume donnait 0.46 a ESTIMATEUR QUALIFIE, 0.08 a QUALIFIE A L'ETAT LU, 0.40 a QUALIFIE PAR POINT, 0.01 a NON QUALIFIE, 0.01 a NON LISIBLE, 0.04 a NON CONCLUANT D'INSTRUMENT.",
      "A-2 : elle donnait 0.02 a SUR LE PLATEAU a tous les etats, 0.23 a A NEUF ETATS SUR DIX AU MOINS, 0.75 a PAS PARTOUT. L'issue sortie est celle a 0.23",
      "a L3, la lecture deposee est sur le plateau a %d etats sur %d." % (V2["points"]["L3"]["n_lus_sur_le_plateau"], V2["points"]["L3"]["n_juges"]),
      "E4 (g = 1.2e-2), ou trois etats sur quatorze echouaient ; aucun des douze points juges n'en perd plus d'un."]
ok12 = (len(pa) == 8 and all(vr.values()) and nnq == {i: (1 if i == "L3" else 0) for i in JUGES}
        and "ESTIMATEUR QUALIFIE : 0.46 ; QUALIFIE A L'ETAT LU : 0.08 ; QUALIFIE PAR POINT : 0.40 ; NON QUALIFIE : 0.01 ; NON LISIBLE : 0.01 ; NON CONCLUANT D'INSTRUMENT : 0.04." in gel
        and "SUR LE PLATEAU a tous les etats : 0.02 ; A NEUF ETATS SUR DIX AU MOINS : 0.23 ; PAS PARTOUT : 0.75." in gel and "E4, g = 1.2e-2" in gel
        and "E4 11/14" in gel and max(nnq.values()) == 1)
m12 = lg + manquent(ph)
ctl("R12", ok12 and not m12, "huit annonces, probabilites %s ; manquent ou fausses : %s" % (sorted(pa.values()), [x[:30] for x in m12]))

# R13 le rejeu de machine 1, recompare ici aux sorties du run
nl = 0; pire = 0.0; itd = 0; net = 0; mauvais = 0; pts = set(); n_part = 0; l_part = 0
def cmp_etats(pid, etats):
    global nl, pire, itd, net, mauvais
    run = {e["rang"]: e for e in S[pid]["points"][0]["etats"]}
    for e in etats:
        net += 1; pts.add(pid)
        for x in "ABCD":
            for k, a in e["traj"][x].items():
                b = run[e["rang"]]["traj"][x][k]; nl += 1
                if not (a["suivi"] and b["suivi"]): mauvais += 1; continue
                pire = max(pire, abs(a["gamma"] - b["gamma"]) / b["gamma"]); itd += (a["iterations"] != b["iterations"])
try:
    mL3 = json.load(open(LOT + "/sonde_ter_point_L3_rejeu_machine1.json")); cmp_etats("L3", mL3["points"][0]["etats"]); n_L3 = len(mL3["points"][0]["etats"])
    okL3 = mL3["sonde_canon"] == canon(GEL + "/sonde_qualification_EB_ter_machine1_v1.py") == S["L3"]["sonde_canon"] and mL3["mode"] == "point" and mL3["ids"] == ["L3"]
    pfm = mL3["plateforme"]
    for f in sorted(glob.glob(LOT + "/rejeu_partiel_*.json")):
        q = json.load(open(f)); cmp_etats(q["id"], q["point"]["etats"]); n_part += len(q["point"]["etats"]); l_part += 48 * len(q["point"]["etats"])
        okL3 = okL3 and q["sonde_canon"] == mL3["sonde_canon"]
    att = {i: sorted({0} | {e["rang"] for j, e in hors if j == i}) for i in JUGES if i != "L3"}
    vus = {os.path.basename(f)[len("rejeu_partiel_"):-5]: sorted(json.load(open(f))["rangs"]) for f in glob.glob(LOT + "/rejeu_partiel_*.json")}
    ph = ["au point L3 (%d etats, %d lectures)" % (n_L3, 48 * n_L3), "pour %d etats des onze autres points : l'etat lu de chacun, et les etats ou la consigne (e) ne tient pas (%d lectures)." % (n_part, l_part),
          "Sur les %d lectures, toutes suivies des deux cotes : memes statuts, plus grand ecart relatif de largeur %s, pour une tolerance de 1e-6 ; %s. "
          "Conteneur %s, python %s, numpy %s, scipy %s." % (nl, sup(pire) if pire > 0 else "0",
              "meme nombre d'iterations a chaque lecture" if itd == 0 else "%d lectures n'ont pas le meme nombre d'iterations" % itd, pfm["systeme"], pfm["python"], pfm["numpy"], pfm["scipy"])]
    m13 = manquent(ph); CJ = json.load(open(LOT + "/comparaison_rejeu_machine1_v1.json"))
    ok13 = (okL3 and mauvais == 0 and pire <= 1e-6 and n_L3 == 14 and vus == att and len(pts) == 12 and CJ["tient"] and CJ["lectures"] == nl and abs(CJ["pire"] - pire) < 1e-18
            and "COMPARAISON : TIENT" in lire(LOT + "/comparaison_rejeu_machine1_v1.log") and "elle peut ensuite rejouer, et compare alors a 1e-6 en relatif sur les lectures suivies" in gel)
    ctl("R13", ok13 and not m13, "%d etats de %d points, %d lectures, pire ecart %.2e, iterations differentes %d ; manquent : %s" % (net, len(pts), nl, pire, itd, [x[:30] for x in m13]))
except Exception as ex:
    ctl("R13", False, "rejeu illisible : %s" % repr(ex)[:80])

# R14 le delta 98
V98 = json.load(open(CLONE + "/journal/verdict_ordre2.json")); P98 = {p["id"]: p for p in V98["points"]}
Ed = {(i, e["rang"]): e for i, e in E}; j98 = [(i, e["rang"]) for i in JUGES for e in P98[i]["etats"] if e["exclu"] is None]
ph = ["De ses %d etats juges, %d sont QUALIFIES ici, et la lecture deposee est sur le plateau a %d d'entre eux." % (
    len(j98), sum(Ed[k]["statut"] == "QUALIFIE" for k in j98), sum(Ed[k]["statut"] == "QUALIFIE" and Ed[k]["lu_sur_le_plateau"] for k in j98)), "le verdict du delta 98 : ses %d etats juges" % len(j98)]
m14 = manquent(ph)
ctl("R14", all(k in Ed for k in j98) and not m14, "%d etats juges au delta 98 ; manquent : %s" % (len(j98), [x[:30] for x in m14]))

# R15 les faits de machine 2 et le rang 1
nc, nr, nlc, nrj = src["certification"], src["resultat"], plat(lire(LL + "POUR_MACHINE1_lecteur_creux_machine2_v1.md")), plat(lire(LJ + "POUR_MACHINE1_rejeu_absorbeurs_longs_machine2_v1.md"))
faits = [("0 morsure, six observations", "CERTIFIE, 0 morsure", nc), ("ses 13 controles de lecture du gel, dont 12 tiennent", "12 sur 13 tiennent", nc),
         ("le banc de sorties de machine 2 (38 cas sur 38", "38 cas sur 38", nc), ("(38 etats reels, 20000 synthetiques, 2657206 cas de cascade : 0 desaccord)", "2657206 cas de cascade", nc),
         ("ecart 0 sur 12 assemblages", "ecart 0 sur 12 assemblages", nc), ("(192 lectures, ecart relatif au pire 2.0e-10)", "ecart relatif au pire 2.0e-10", nc),
         ('"py -3.11 -P"', "py -3.11 -P", nc), ("un echec de factorisation simule", "un echec de factorisation SIMULE", nc),
         ("43 alterations mordues sur 43, rejoue a l'identique par machine 2", "banc 43 sur 43 rejoues chez moi", nc),
         ("deux de ses controles ont mordu a ses premiers jets", "Deux de mes controles ont mordu au premier jet par ma faute", nc),
         ("non recalcule", "c'est le rang du depot, non recalcule", nc), ("ecrite apres lecture de celle de machine 1", "je l'ai ecrite apres avoir lu la tienne", nc),
         ("n'a pas lu les douze points", "Mon lecteur n'a pas lu les douze points", nr), ("0 ecart sur le run", "0 ecart", nr),
         ("une marge de recouvrement de 0.3 a 9 pour cent", "0.3 % a 9 %", nlc), ("different d'un facteur 22 a 30", "leurs largeurs different d'un facteur 22 a 30", nlc),
         ("en retrouve les tableaux", "30 cellules sur 30 sont les tiennes", nrj), ("quatre lots, 43, 28, 11 et 14 pieces", "43 pieces", src["envoi"])]
mf = [a for a, b, s in faits if a not in U or b not in s]
rec = {}; lar = {}
for i in JUGES:
    d0 = [e for e in PD[i]["etats"] if e["rang"] == 0][0]; d1 = [e for e in PD[i]["etats"] if e["rang"] == 1][0]
    rec[i] = d0["recouvrement"] / d1["recouvrement"]; q = d1["Gamma_2D"]["3"] / d0["Gamma_2D"]["3"]; lar[i] = max(q, 1 / q)
r1 = [i for i in JUGES if any(e["rang"] == 1 for e in V2["points"][i]["etats"])]
ph = ["va de %.3f (%s) a %.3f (%s) aux douze points, pour des largeurs deposees qui different d'un facteur %.1f a %.0f." % (
          min(rec.values()), min(rec, key=rec.get), max(rec.values()), max(rec, key=rec.get), math.floor(min(lar.values()) * 10) / 10.0, math.ceil(max(lar.values()))),
      "L'etat de rang 1 est juge a dix points sur douze et y est QUALIFIE ; a M3 et M4 il est sous dix planchers.", "celui des %d etats sur %d" % (nq, nj)]
ok15 = len(r1) == 10 and [i for i in JUGES if i not in r1] == ["M3", "M4"] and all(Ed[(i, 1)]["statut"] == "QUALIFIE" for i in r1) and all(
    [e for e in PD[i]["etats"] if e["rang"] == 1][0]["Gamma_2D"]["3"] <= 1.33e-12 for i in ("M3", "M4"))
m15 = mf + manquent(ph)
ctl("R15", ok15 and not m15, "%d faits de machine 2 relus dans ses notes ; rang 1 juge a %d points ; manquent : %s" % (len(faits), len(r1), [x[:30] for x in m15]))

# R16 la feuille rejouee par machine 1
def feuilles(d, p=""):
    if isinstance(d, dict):
        for k, v in d.items(): yield from feuilles(v, p + "/" + str(k))
    elif isinstance(d, list):
        for k, v in enumerate(d): yield from feuilles(v, p + "/" + str(k))
    else: yield p, d
nd = 0; nf = 0; eg = 0.0; el = 0.0; autre = 0
for a, b in ((LOT + "/verdict_ter_rejoue_machine1.json", RUN + "verdict_ter.json"), (LOT + "/verdict_ter_instrument_rejoue_machine1.json", RUN + "verdict_ter_instrument.json")):
    A, Bq = dict(feuilles(json.load(open(a)))), dict(feuilles(json.load(open(b))))
    autre += (set(A) != set(Bq))
    for k in A:
        x, y = A[k], Bq.get(k)
        if isinstance(x, float):
            nf += 1
            if x != y:
                nd += 1
                if k.endswith("/Gamma_pl"): eg = max(eg, abs(x - y) / abs(y))
                elif k.split("/")[-1].startswith("ecart_ln"): el = max(el, abs(x - y))
                else: autre += 1
        elif x != y: autre += 1
ph = ["different de ceux de BOCAL4 par %d flottants sur %d : des Gamma_pl, de %s au plus en relatif, et des ecarts logarithmiques, de %s au plus en absolu" % (nd, nf, sup(eg), sup(el)),
      "(canons %s et %s)" % (canon(LOT + "/lecture_ter_rejouee_machine1.log"), canon(LOT + "/lecture_ter_instrument_rejouee_machine1.log"))]
ok16 = (autre == 0 and canon(LOT + "/lecture_ter_rejouee_machine1.log") == canon(RUN + "lecture_ter.log")
        and canon(LOT + "/lecture_ter_instrument_rejouee_machine1.log") == canon(RUN + "lecture_ter_instrument.log"))
m16 = manquent(ph)
ctl("R16", ok16 and not m16, "journaux aux canons de BOCAL4 ; %d flottants differents sur %d ; manquent : %s" % (nd, nf, [x[:30] for x in m16]))

# R17 le registre
def git(*a): return subprocess.run(["git", "-C", CLONE] + list(a), check=True, capture_output=True, text=True).stdout.strip()
tete = git("rev-parse", "--short", "HEAD"); suj = git("log", "-1", "--format=%s")
ph = ["Registre a l'ecriture : origin/main %s, plafond 98. Aucun numero n'est pris ici (E18)." % tete, "Au registre (%s)" % tete, "Aucune regle nouvelle ; trente-quatre attendent la revue."]
m17 = manquent(ph)
ctl("R17", tete == git("rev-parse", "--short", "origin/main") and suj.startswith("delta 98 --") and "thirty-four await review (X)" in suj and not m17,
    "tete %s, plafond 98, trente-quatre regles en attente ; manquent : %s" % (tete, m17))

# R18 les pieces du lot nommees en nn.15
s15 = T[T.index("nn.15 PIECES DU LOT"):]
attendus = set()
for l in s15.split("\n"):
    if l.startswith("  ") and not l.startswith("   ") and not l.strip().startswith("Perimetre"):
        prem = None
        for t in re.split(r", ", l.strip().rstrip(",")):
            parts = t.split(" / ")
            prem = parts[0].split(" (")[0].strip()
            if "<id>" in prem: continue
            attendus.add(prem)
            for ext in parts[1:]:
                attendus.add(os.path.splitext(prem)[0] + ext.strip())
soi = {"releve_acte_EB_ter_machine1_v1.log", "contre_epreuve_releve_acte_EB_ter_machine1_v1.log"}
absents = sorted(a for a in attendus if a not in soi and not os.path.exists(os.path.join(LOT, a)))
npart = len(glob.glob(LOT + "/rejeu_partiel_*.json"))
ctl("R18", not absents and npart == 11 and len(attendus) >= 18, "%d pieces nommees en nn.15, absentes du lot : %s ; rejeu_partiel_<id>.json : %d" % (len(attendus), absents, npart))

nb = sum(1 for r in RES if not r[1])
print("RELEVE : %d controles, %d tenus, %d mordent %s" % (len(RES), len(RES) - nb, nb, [r[0] for r in RES if not r[1]]))
sys.exit(0 if nb == 0 else 1)
