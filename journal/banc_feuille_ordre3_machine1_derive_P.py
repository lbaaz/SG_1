# -*- coding: ascii -*-
"""BANC A MUTATIONS DE LA FEUILLE D'ORDRE 3 -- machine 1, v1, 2026-11-15. Aucun calcul 2D : la feuille est lancee sur des
entrees DEJA JOUEES (trois points du delta 98 : C1, C2, L4 ; sortie dense du depot ; verdict du lecteur du run ter), en mode
--prevol, d'abord telles quelles, puis sur des copies ou UNE chose est changee. Chaque mutation a un effet ATTENDU, ecrit ici
avant de lancer ; le banc tient si chaque effet attendu est observe, et seulement celui-la pour les verdicts suivis.
Usage : python3 -I banc_feuille_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <feuille> <sortie dense du depot>
        <verdict du lecteur du run ter> <dossier de travail (neuf)> <sortie.json>"""
import sys, os, json, copy, hashlib, unicodedata, subprocess, math
MOTEUR, BLOC2, BLOC3, FEUILLE, DENSE, LECTEUR, TRAVAIL, SORTIE = sys.argv[1:9]
os.makedirs(TRAVAIL, exist_ok=False)
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
D0 = json.load(open(DENSE)); V0 = json.load(open(LECTEUR))
T0 = {"table": "banc : trois points deja joues et les deux ancres", "prevol": True,
      "points": [{"id": p["id"], "role": "juge", "creneau": "N" if p["id"] != "L4" else "BP", "w2": p["w2"], "facteur": p["facteur"]} for p in D0["points"] if p["id"] in ("C1", "C2", "L4")]
                + [{"id": p["id"], "role": "ancre", "creneau": None, "w2": p["w2"], "facteur": p["facteur"]} for p in D0["points"] if p["id"] in ("A1", "A2")]}
def ecrire(nom, obj):
    ch = os.path.join(TRAVAIL, nom); json.dump(obj, open(ch, "w"), indent=1, sort_keys=True); return ch
def lancer(nom, T, D, V, canon_dense=None, canon_lecteur=None):
    t, d, v = ecrire(nom + "_table.json", T), ecrire(nom + "_dense.json", D), ecrire(nom + "_lecteur.json", V); s = os.path.join(TRAVAIL, nom + "_sortie.json")
    r = subprocess.run([sys.executable, "-P", "-B", FEUILLE, MOTEUR, BLOC2, BLOC3, t, DENSE, d, canon_dense or canon_B(d), v, canon_lecteur or canon_B(v), s, "--prevol"], capture_output=True, text=True)
    out = json.load(open(s)) if (r.returncode == 0 and os.path.exists(s)) else None
    return {"code": r.returncode, "arret": [l for l in r.stdout.split("\n") if l.startswith("ARRET")], "sortie": out}
def cel(res, pid):
    return [c for c in res["sortie"]["cellules"] if c["id"] == pid][0]
def etat_v(V, pid, rang):
    return [e for e in V["points"][pid]["etats"] if e["rang"] == rang][0]
def etat_d(D, pid, rang):
    return [e for p in D["points"] if p["id"] == pid for e in p["etats"] if e["rang"] == rang][0]

base = lancer("m00_temoin", T0, D0, V0); assert base["code"] == 0, base
b1, b2, b4 = cel(base, "C1"), cel(base, "C2"), cel(base, "L4")
r_c1 = [e["rang"] for e in b1["etats"] if e["exclu"] is None][0]; r_l4 = [e["rang"] for e in b4["etats"] if e["exclu"] is None][0]
print("TEMOIN : C1 juges %d domaine %d E1 %s E2 %s E3 %s ; C2 juges %d domaine %d E1 %s E2 %s E3 %s ; L4 juges %d domaine %d E1 %s E3 %s" % (
    b1["n_juges"], b1["n_domaine"], b1["E1"], b1["E2"], b1["E3"], b2["n_juges"], b2["n_domaine"], b2["E1"], b2["E2"], b2["E3"], b4["n_juges"], b4["n_domaine"], b4["E1"], b4["E3"]))
assert (b1["E1"], b1["E2"], b1["E3"], b2["E1"], b2["E2"], b2["E3"], b4["E1"], b4["E3"]) == ("TIENT", "TIENT", "TIENT", "TIENT", "TIENT", "TIENT", "INEXPLOITABLE", "TIENT")
res = []
def epreuve(nom, quoi, attendu, obtenu):
    ok = bool(obtenu); res.append({"mutation": nom, "quoi": quoi, "attendu": attendu, "tient": ok})
    print("%-4s %-5s %s -> attendu : %s" % (nom, "MORD" if ok else "MUET", quoi, attendu), flush=True)

# m01 : une largeur de plateau du domaine de C1 multipliee par 1.2 -> E1 tombe a C1, C2 inchange
V = copy.deepcopy(V0); etat_v(V, "C1", r_c1)["plateaux"]["A"]["Gamma_pl"] *= 1.2; r = lancer("m01", T0, D0, V)
epreuve("m01", "Gamma_pl(A) d'un etat du domaine de C1 x 1.2", "E1 TOMBE a C1 ; C2 et L4 inchanges",
        r["code"] == 0 and cel(r, "C1")["E1"] == "TOMBE" and cel(r, "C2")["E1"] == "TIENT" and cel(r, "L4")["E3"] == "TIENT" and cel(r, "C1")["n_juges"] == b1["n_juges"])
# m02 : toutes les largeurs de plateau de C2 x 1.15 -> l'ordre 2 devient le plus pres : E2 tombe a C2
V = copy.deepcopy(V0)
for e in V["points"]["C2"]["etats"]:
    e["plateaux"]["A"]["Gamma_pl"] *= 1.15
r = lancer("m02", T0, D0, V)
epreuve("m02", "toutes les Gamma_pl(A) de C2 x 1.15", "E2 TOMBE a C2 (l'ordre 2 est alors le plus pres) ; C1 inchange", r["code"] == 0 and cel(r, "C2")["E2"] == "TOMBE" and cel(r, "C1")["E2"] == "TIENT")
# m03 : un etat de C1 passe NON QUALIFIE -> un juge de moins, verdicts inchanges
V = copy.deepcopy(V0); etat_v(V, "C1", r_c1)["statut"] = "NON QUALIFIE"; r = lancer("m03", T0, D0, V)
epreuve("m03", "un etat de C1 declare NON QUALIFIE", "un etat juge de moins a C1, exclu \"non qualifie\" ; verdicts inchanges",
        r["code"] == 0 and cel(r, "C1")["n_juges"] == b1["n_juges"] - 1 and [r_c1, "non qualifie"] in cel(r, "C1")["exclus"] and cel(r, "C1")["E1"] == "TIENT")
# m04 : l'instrument ne tient pas -> rien n'est juge
V = copy.deepcopy(V0); V["instrument"] = "NE TIENT PAS"; r = lancer("m04", T0, D0, V)
epreuve("m04", "verdict du lecteur : instrument NE TIENT PAS", "rien n'est juge", r["code"] == 0 and r["sortie"].get("verdict") == "RIEN N'EST JUGE" and "cellules" not in r["sortie"])
# m05 : une etiquette changee dans la sortie dense -> arret
D = copy.deepcopy(D0); etat_d(D, "C1", r_c1)["n1"] += 1; r = lancer("m05", T0, D, V0)
epreuve("m05", "une etiquette de la sortie dense changee (n1 + 1)", "ARRET : etiquettes differentes", r["code"] == 2 and any("etiquettes differentes" in a for a in r["arret"]))
# m06 : le couplage de la sortie dense change de 1e-6 -> arret de forme
D = copy.deepcopy(D0)
for p in D["points"]:
    if p["id"] == "C2":
        p["g"] *= 1.000001
r = lancer("m06", T0, D, V0)
epreuve("m06", "couplage de C2 dans la sortie dense x (1 + 1e-6)", "ARRET : forme de la sortie dense", r["code"] == 2 and any("forme de la sortie dense" in a for a in r["arret"]))
# m07 : un etat retire d'un point de la sortie dense -> arret de forme
D = copy.deepcopy(D0)
for p in D["points"]:
    if p["id"] == "L4":
        p["etats"] = p["etats"][:-1]
r = lancer("m07", T0, D, V0)
epreuve("m07", "un etat retire de L4 dans la sortie dense (13 etats)", "ARRET : forme de la sortie dense", r["code"] == 2 and any("forme de la sortie dense" in a for a in r["arret"]))
# m08 : le facteur d'un point change dans la table -> arret de forme
T = copy.deepcopy(T0); T["points"][0]["facteur"] = "3/4" if T["points"][0]["facteur"] != "3/4" else "5/6"; r = lancer("m08", T, D0, V0)
epreuve("m08", "facteur d'un point change dans la table", "ARRET : forme de la sortie dense", r["code"] == 2 and any("forme de la sortie dense" in a for a in r["arret"]))
# m09 : une largeur de plateau de L4 x 0.4 -> l'ordre 2 sort de la bande : E3 tombe a L4
V = copy.deepcopy(V0); etat_v(V, "L4", r_l4)["plateaux"]["A"]["Gamma_pl"] *= 0.4; r = lancer("m09", T0, D0, V)
epreuve("m09", "Gamma_pl(A) d'un etat de L4 x 0.4", "E3 TOMBE a L4 ; C1 et C2 inchanges", r["code"] == 0 and cel(r, "L4")["E3"] == "TOMBE" and cel(r, "C1")["E3"] == "TIENT" and cel(r, "C2")["E3"] == "TIENT")
# m10 : J flou a un etat -> exclu
D = copy.deepcopy(D0); etat_d(D, "C1", r_c1)["J_ecart_type"] = 0.5; r = lancer("m10", T0, D, V0)
epreuve("m10", "ecart-type de J d'un etat de C1 mis a 0.5", "un juge de moins a C1, exclu \"J flou\"", r["code"] == 0 and cel(r, "C1")["n_juges"] == b1["n_juges"] - 1 and [r_c1, "J flou"] in cel(r, "C1")["exclus"])
# m11 : mauvais canon passe pour la sortie dense -> arret
r = lancer("m11", T0, D0, V0, canon_dense="0" * 16)
epreuve("m11", "canon de la sortie dense passe faux", "ARRET : sortie dense : canon", r["code"] == 2 and any("sortie dense : canon" in a for a in r["arret"]))
# m12 : C1 rendue inexploitable (il ne reste que 4 etats QUALIFIES)
V = copy.deepcopy(V0); gardes = [e["rang"] for e in b1["etats"] if e["exclu"] is None][:4]
for e in V["points"]["C1"]["etats"]:
    if e["rang"] not in gardes:
        e["statut"] = "NON QUALIFIE"
r = lancer("m12", T0, D0, V)
epreuve("m12", "C1 : tous les etats sauf 4 declares NON QUALIFIES", "C1 INEXPLOITABLE pour E1 et E2 ; E3 tient encore", r["code"] == 0 and cel(r, "C1")["E1"] == "INEXPLOITABLE" and cel(r, "C1")["E2"] == "INEXPLOITABLE" and cel(r, "C1")["E3"] == "TIENT")
# m13 : etiquette double a C2 (deux etats de la sortie dense portent la meme etiquette) -> exclus tous les deux s'ils sont lus
D = copy.deepcopy(D0); V = copy.deepcopy(V0); js = [e["rang"] for e in b2["etats"] if e["exclu"] is None][:2]
a, b = etat_d(D, "C2", js[0]), etat_d(D, "C2", js[1]); b["n1"], b["n2"] = a["n1"], a["n2"]; vb = etat_v(V, "C2", js[1]); vb["n1"], vb["n2"] = a["n1"], a["n2"]; r = lancer("m13", T0, D, V)
epreuve("m13", "deux etats de C2 portent la meme etiquette (sortie dense et lecteur)", "les deux sont exclus \"etiquette double\"",
        r["code"] == 0 and [js[0], "etiquette double"] in cel(r, "C2")["exclus"] and [js[1], "etiquette double"] in cel(r, "C2")["exclus"] and cel(r, "C2")["n_juges"] == b2["n_juges"] - 2)
# m14 : une largeur d'ancre changee dans la sortie dense -> l'instrument ne tient pas, rien n'est juge
D = copy.deepcopy(D0); etat_d(D, "A1", 0)["Gamma_2D"]["3"] *= 1.01; r = lancer("m14", T0, D, V0)
epreuve("m14", "Gamma_2D(3) de l'etat de rang 0 de l'ancre A1 x 1.01 dans la sortie dense", "l'instrument ne tient pas : rien n'est juge",
        r["code"] == 0 and r["sortie"].get("verdict") == "RIEN N'EST JUGE" and r["sortie"].get("instrument") == "NE TIENT PAS" and "cellules" not in r["sortie"])
# m15 : C2, quatre etats declares NON QUALIFIES : 7 juges sur 11 lus, moins des deux tiers -> INEXPLOITABLE bien que 7 >= 5 dans le domaine
V = copy.deepcopy(V0); retires = [e["rang"] for e in b2["etats"] if e["exclu"] is None][:4]
for e in V["points"]["C2"]["etats"]:
    if e["rang"] in retires:
        e["statut"] = "NON QUALIFIE"
r = lancer("m15", T0, D0, V)
epreuve("m15", "C2 : quatre etats sur onze declares NON QUALIFIES", "C2 INEXPLOITABLE (7 juges sur 11 lus, moins des deux tiers) alors que 7 sont dans le domaine",
        r["code"] == 0 and cel(r, "C2")["n_domaine"] == 7 and cel(r, "C2")["E1"] == "INEXPLOITABLE" and cel(r, "C2")["assez_de_juges"] is False and cel(r, "C1")["E1"] == "TIENT")
# m16 : une ancre retiree de la table -> l'instrument ne tient pas
T = copy.deepcopy(T0); T["points"] = [p for p in T["points"] if p["id"] != "A2"]; r = lancer("m16", T, D0, V0)
epreuve("m16", "l'ancre A2 retiree de la table", "l'instrument ne tient pas : rien n'est juge", r["code"] == 0 and r["sortie"].get("verdict") == "RIEN N'EST JUGE")
# m17 : la table du banc presentee SANS --prevol -> arret (elle n'est pas au canon du gel)
t_, d_, v_ = ecrire("m17_table.json", T0), ecrire("m17_dense.json", D0), ecrire("m17_lecteur.json", V0)
r17 = subprocess.run([sys.executable, "-P", "-B", FEUILLE, MOTEUR, BLOC2, BLOC3, t_, DENSE, d_, canon_B(d_), v_, canon_B(v_), os.path.join(TRAVAIL, "m17_sortie.json")], capture_output=True, text=True)
epreuve("m17", "une table qui n'est pas celle du gel, sans --prevol", "ARRET : sans --prevol la table doit etre au canon", r17.returncode == 2 and "sans --prevol la table doit etre au canon" in r17.stdout
        and not os.path.exists(os.path.join(TRAVAIL, "m17_sortie.json")))
n_ok = sum(x["tient"] for x in res)
print("BANC DE LA FEUILLE D'ORDRE 3 : %d mutations, %d mordent comme attendu : %s" % (len(res), n_ok, "TIENT" if n_ok == len(res) else "NE TIENT PAS"))
json.dump({"temoin": {"C1": [b1["n_juges"], b1["n_domaine"]], "C2": [b2["n_juges"], b2["n_domaine"]], "L4": [b4["n_juges"], b4["n_domaine"]]}, "mutations": res, "tient": n_ok == len(res)}, open(SORTIE, "w"), indent=1, sort_keys=True)
sys.exit(0 if n_ok == len(res) else 1)
