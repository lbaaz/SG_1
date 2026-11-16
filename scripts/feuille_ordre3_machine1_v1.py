# -*- coding: ascii -*-
"""FEUILLE D'ORDRE 3 du gel "loi de la largeur, ordre 3" -- machine 1, v1, 2026-11-15. Elle JUGE et ne mesure rien en 2D.
Elle lit : la table gelee des points ; la sortie de la sonde dense a ces points (etiquettes lues, J) ; le verdict du lecteur
(largeurs de plateau des etats QUALIFIES). Elle calcule, a l'etiquette LUE de chaque etat, des chaines a une dimension :
moteur, ordre 2 (bloc depose), ordre 3 (bloc du gel). Puis elle juge, la CELLULE pour unite :
  E1  (cellules des lignes N et P) : chaque etat juge DANS LE DOMAINE a |ln(G3 / Gamma_pl)| <= T, T = 0.05 si e_bord < 0.3,
      0.10 sinon.
  E2  (cellules de la ligne N) : pour au moins les trois quarts des etats juges du domaine, l'ordre 3 est plus pres de la
      largeur de plateau que l'ordre 2.
  E1B (cellules de bord BN, BP) : comme E1, sur leurs etats juges du domaine.
  E3  (les douze cellules) : chaque etat juge, dans le domaine ou non, a sa largeur d'ordre 2 dans la bande du delta 98
      (1.25 pour |delta| <= 0.06, 1.6 jusqu'a 0.10, 2 jusqu'a 0.12).
ETAT JUGE : QUALIFIE par le lecteur ; J net (ecart-type < 0.2) ; etiquette unique parmi les 14 etats lus du point ; barriere
non vide ; chaine du moteur et chaine d'ordre 2 stables (quatre eta de chaine, toutes > 0, max / min <= 2).
DANS LE DOMAINE : e_bord < 0.7 et stabilite de la chaine d'ordre 3 definie et <= 0.05 (definitions de la premiere partie, 4.3, 4.4).
CELLULE EXPLOITABLE : ligne, au moins 5 etats juges dans le domaine ; bord, au moins 2 dans le domaine et 2 hors du domaine.
ISSUES. E1 (dix cellules de ligne) et E2 (cinq cellules N) : TOMBE si deux cellules exploitables ou plus tombent ; sinon NON
CONCLUANT si plus de deux (E1), plus d'une (E2) cellules sont inexploitables ; sinon TENU, ou TENU SAUF UNE CELLULE.
E1B : TOMBE si une cellule de bord exploitable tombe ; sinon NON CONCLUANT si l'une est inexploitable ; sinon TENU.
E3 : TENU si aucune cellule ne tombe (une cellule sans etat juge est VIDE et ne tombe pas).
Les fonctions de chaine sont celles de carte_chaine_machine1_v1.py (f0f6581d87176752), fonction etat, recopiee.
Une cellule ou moins des deux tiers des etats lus par le lecteur sont juges est INEXPLOITABLE elle aussi.
AVANT TOUT JUGEMENT : canons (moteur, blocs, depot en dur ; sortie dense et verdict du lecteur passes par le pilote) ;
provenance (la sortie dense et le verdict portent le canon de la table, de la sonde dense, de la feuille du lecteur) ;
forme de la sortie dense (w2, facteur, couplage, 14 etats par point) ; ANCRES : les deux ancres rejouees par la sonde
dense redonnent celles du depot (memes etiquettes, Gamma_2D(3) a 1e-3 en relatif plus 1e-12, energie a 1e-9).
Usage : python3 -I feuille_ordre3_machine1_v1.py <moteur_v17.py> <bloc ordre 2> <bloc ordre 3> <table des points.json>
        <sonde_ordre2.json (depot)> <sortie dense.json> <canon de la sortie dense> <verdict du lecteur.json>
        <canon du verdict> <sortie.json> [--prevol]
        --prevol : la table n'est PAS celle du gel (points deja joues) ; la sortie porte "prevol" et ne juge rien."""
import sys, os, math, json, hashlib, unicodedata, importlib.util
from fractions import Fraction as F
import numpy as np
args = [a for a in sys.argv[1:] if a != "--prevol"]; PREVOL = "--prevol" in sys.argv[1:]
MOTEUR, BLOC2, BLOC3, TABLE, DEPOT, DENSE, CANON_DENSE_RECU, LECTEUR, CANON_LECTEUR_RECU, SORTIE = args[0:10]
CANON_MOTEUR, CANON_BLOC2, CANON_BLOC3, CANON_DEPOT = "82a0be882568fe0c", "7cd5977bc27bebc1", "534ba246aa3b8973", "10887c60d5f55bcf"
CANON_TABLE, CANON_SONDE_DENSE, CANON_FEUILLE_LECTEUR = "35fa7b73f2b7f8eb", "68baf04c73ed5d44", "83701094e6a2b965"
CANON_SONDE_DEPOT = "24315c52b234319c"
TOL_ANCRE_REL, TOL_ANCRE_ABS, TOL_ANCRE_E = 1e-3, 1e-12, 1e-9
EF = 0.0625; ETAS = (0.25, 0.125, 0.0625, 0.03125)
E_MAX = 0.7; STAB_MAX = 0.05; J_NET = 0.2; E_BAS = 0.3; T_BAS = 0.05; T_HAUT = 0.10
DOM_MIN = 5; BORD_MIN = 2; PART_JUGES = F(2, 3); PART_E2 = F(3, 4); INEXPLOITABLES_E1 = 2; INEXPLOITABLES_E2 = 1; N_ETATS = 14
BANDES = ((0.06, 1.25), (0.10, 1.6), (0.12, 2.0))
LIGNES = ("N", "P"); BORDS = ("BN", "BP")

def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]

def arret(msg):
    print("ARRET : " + msg); sys.exit(2)

for chemin, attendu, quoi in ((MOTEUR, CANON_MOTEUR, "moteur"), (BLOC2, CANON_BLOC2, "bloc d'ordre 2"), (BLOC3, CANON_BLOC3, "bloc d'ordre 3"), (DEPOT, CANON_DEPOT, "depot du delta 98"),
                              (DENSE, CANON_DENSE_RECU, "sortie dense"), (LECTEUR, CANON_LECTEUR_RECU, "verdict du lecteur")):
    if canon_B(chemin) != attendu:
        arret("%s : canon %s, attendu %s" % (quoi, canon_B(chemin), attendu))
if (canon_B(TABLE) == CANON_TABLE) == PREVOL:
    arret("sans --prevol la table doit etre au canon %s ; avec --prevol elle ne doit pas l'etre" % CANON_TABLE)
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
_brut = M.X_saut_reel; _cache = {}
def _X(p, k, l, n1, n2, w2):                      # memoire des elements de x^5 : memes valeurs, moins d'appels
    c = (k, l, n1, n2, w2)
    if c not in _cache:
        _cache[c] = _brut(p, k, l, n1, n2, w2)
    return _cache[c]
M.X_saut_reel = _X
exec(compile(open(BLOC2, encoding="ascii").read(), BLOC2, "exec")); exec(compile(open(BLOC3, encoding="ascii").read(), BLOC3, "exec"))

def stable(v):
    return bool(all(x > 0.0 for x in v) and max(v) / min(v) <= 2.0)

def etat(w2, g, a, b):
    d = float(w2) - 2.0
    sites = M.barriere(float(a), float(b), w2, g, True)
    if not sites:
        return {"n1": a, "n2": b, "vide": True}
    g1 = [float(M.gamma_chaine(float(a), float(b), w2, g, sites, eta_facteur=x, M_facteur=4)["Gamma_c"]) for x in ETAS]
    tb = tables_ordre2(float(a), float(b), w2, g, sites, M_facteur=4)
    r2 = [gamma_chaine_ordre2(tb, x) for x in ETAS]; g2 = [r["Gamma_flux"] for r in r2]
    t3 = tables_ordre3(float(a), float(b), w2, g, tb)
    r3 = gamma_chaine_ordre3(tb, t3, EF); G3 = r3["Gamma_flux"]
    var = [gamma_chaine_ordre3(tb, t3, 2 * EF)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF / 2)["Gamma_flux"], gamma_chaine_ordre3(tb, t3, EF, recul=4)["Gamma_flux"]]
    mb = tb["m2_bord"]
    return {"n1": a, "n2": b, "vide": False, "card": len(sites), "m_bord": mb, "e_bord": abs(mb * d + tb["S"][mb] - tb["S"][0]), "t_bord": abs(tb["t"][mb]),
            "kappa": abs(tb["t"][0]) / abs(d), "G1": g1, "stable1": stable(g1), "G2": g2, "stable2": stable(g2), "dE2": r2[2]["dE"],
            "G3": G3, "dE3": r3["dE"], "stab3": (max(abs(math.log(x / G3)) for x in var) if G3 > 0.0 and all(x > 0.0 for x in var) else None),
            "E_libre": float(M.energie_libre(a, b, w2))}

def bande(d):
    for lim, b in BANDES:
        if abs(d) <= lim + 1e-12:
            return b
    return None

T = json.load(open(TABLE)); D = json.load(open(DENSE)); V = json.load(open(LECTEUR)); DEP = {p["id"]: p for p in json.load(open(DEPOT))["points"]}
dense = {p["id"]: p for p in D["points"]}
if D.get("moteur_canon") != CANON_MOTEUR or D.get("sonde_canon") not in ((CANON_SONDE_DENSE, CANON_SONDE_DEPOT) if PREVOL else (CANON_SONDE_DENSE,)):
    arret("la sortie dense ne porte pas les canons du moteur et de la sonde dense")
if not PREVOL:
    if D.get("table_canon") != CANON_TABLE or D.get("prevol") is not False or sorted(dense) != sorted(p["id"] for p in T["points"]):
        arret("la sortie dense n'a pas ete produite sur la table du gel, ou n'en porte pas tous les points et eux seuls")
    if V.get("feuille_canon") != CANON_FEUILLE_LECTEUR or V.get("table_canon") != CANON_TABLE or V.get("dense_canon") != CANON_DENSE_RECU or V.get("prevol") is not False:
        arret("le verdict du lecteur ne porte pas les canons de la feuille du lecteur, de la table et de cette sortie dense")
ENTETE = {"prevol": PREVOL, "feuille": "feuille_ordre3_machine1_v1", "canons": {"moteur": CANON_MOTEUR, "bloc2": CANON_BLOC2, "bloc3": CANON_BLOC3, "table": canon_B(TABLE),
          "depot": CANON_DEPOT, "dense": CANON_DENSE_RECU, "lecteur": CANON_LECTEUR_RECU}}
print("%sFEUILLE D'ORDRE 3 -- table %s, sortie dense %s, verdict du lecteur %s" % ("PRE-VOL (ne juge rien) -- " if PREVOL else "", canon_B(TABLE), CANON_DENSE_RECU, CANON_LECTEUR_RECU))
motifs = []                                            # les ancres rejouees par la sonde dense contre le depot
for pt in T["points"]:
    if pt["role"] != "ancre":
        continue
    pid = pt["id"]
    if pid not in dense or pid not in DEP or len(dense[pid]["etats"]) != N_ETATS:
        motifs.append("ancre %s absente ou incomplete" % pid); continue
    for a, b in zip(sorted(dense[pid]["etats"], key=lambda e: e["rang"]), sorted(DEP[pid]["etats"], key=lambda e: e["rang"])):
        ga, gb = a["Gamma_2D"]["3"], b["Gamma_2D"]["3"]
        if (a["n1"], a["n2"]) != (b["n1"], b["n2"]) or abs(ga - gb) > TOL_ANCRE_ABS + TOL_ANCRE_REL * abs(gb) or abs(a["E_re"] - b["E_re"]) > TOL_ANCRE_E:
            motifs.append("ancre %s rang %d : etiquette, largeur ou energie differente du depot" % (pid, a["rang"]))
n_ancres = sum(1 for pt in T["points"] if pt["role"] == "ancre")
print("ANCRES de la sonde dense contre le depot : %d ancres, %d ecarts : %s" % (n_ancres, len(motifs), "TIENNENT" if not motifs and n_ancres == 2 else "NE TIENNENT PAS"))
for m_ in motifs[:8]:
    print("     " + m_)
if V.get("instrument") != "TIENT" or motifs or n_ancres != 2:
    print("L'INSTRUMENT NE TIENT PAS (%s) : RIEN N'EST JUGE" % ("verdict du lecteur" if V.get("instrument") != "TIENT" else "ancres de la sonde dense"))
    ENTETE.update({"instrument": "NE TIENT PAS", "motifs_ancres": motifs, "instrument_lecteur": V.get("instrument"), "verdict": "RIEN N'EST JUGE"})
    json.dump(ENTETE, open(SORTIE, "w"), indent=1, sort_keys=True); sys.exit(0)
out = dict(ENTETE); out.update({"instrument": "TIENT", "cellules": []})
for pt in T["points"]:
    if pt["role"] != "juge":
        continue
    pid, w2, fac, cr = pt["id"], F(pt["w2"]), F(pt["facteur"]), pt["creneau"]; d = float(w2) - 2.0; _cache.clear()
    if cr not in LIGNES + BORDS:
        arret("creneau inconnu a %s" % pid)
    if pid not in dense or pid not in V["points"]:
        arret("le point %s manque a la sortie dense ou au verdict du lecteur" % pid)
    dp = dense[pid]; g = dp["g"]; g_att = float(M.g_du_point(w2)) * float(fac)
    if F(dp["w2"]) != w2 or F(dp["facteur"]) != fac or abs(g / g_att - 1.0) > 1e-12 or len(dp["etats"]) != N_ETATS or not dp.get("faisable"):
        arret("forme de la sortie dense a %s : w2, facteur, couplage ou nombre d'etats differents de la table" % pid)
    de = {e["rang"]: e for e in dp["etats"]}; labels = [(e["n1"], e["n2"]) for e in dp["etats"]]; etats = []; B = bande(d)
    if B is None:
        arret("pas de bande pour delta = %+.3f" % d)
    for ev in sorted(V["points"][pid]["etats"], key=lambda x: x["rang"]):
        e = de[ev["rang"]]
        if (e["n1"], e["n2"]) != (ev["n1"], ev["n2"]):
            arret("etiquettes differentes entre la sortie dense et le lecteur a %s rang %d" % (pid, ev["rang"]))
        r = {"rang": ev["rang"], "n1": e["n1"], "n2": e["n2"], "statut_lecteur": ev["statut"], "exclu": None}
        if ev["statut"] != "QUALIFIE":
            r["exclu"] = "non qualifie"
        elif not (e["J_ecart_type"] < J_NET):
            r["exclu"] = "J flou"
        elif labels.count((e["n1"], e["n2"])) != 1:
            r["exclu"] = "etiquette double"
        else:
            c = etat(w2, g, e["n1"], e["n2"])
            if c["vide"]:
                r["exclu"] = "barriere vide"
            elif not c["stable1"]:
                r["exclu"] = "chaine du moteur instable"
            elif not c["stable2"]:
                r["exclu"] = "chaine d'ordre 2 instable"
            else:
                Gpl = ev["plateaux"]["A"]["Gamma_pl"]; dans = bool(c["G3"] > 0.0 and c["e_bord"] < E_MAX and c["stab3"] is not None and c["stab3"] <= STAB_MAX)
                tol = T_BAS if c["e_bord"] < E_BAS else T_HAUT; q2 = c["G2"][2] / Gpl; q3 = (c["G3"] / Gpl) if c["G3"] > 0.0 else None
                r.update({"Gamma_pl": Gpl, "G1": c["G1"][2], "G2": c["G2"][2], "G3": c["G3"], "e_bord": c["e_bord"], "m_bord": c["m_bord"], "stab3": c["stab3"], "kappa": c["kappa"],
                          "dans_le_domaine": dans, "tolerance": tol, "q2": q2, "q3": q3, "ln_q2": math.log(q2), "ln_q3": (math.log(q3) if q3 else None),
                          "dans_la_tolerance": bool(dans and abs(math.log(q3)) <= tol), "ordre3_plus_pres": bool(q3 is not None and abs(math.log(q3)) < abs(math.log(q2))),
                          "dans_la_bande": bool(1.0 / B <= q2 <= B)})
        etats.append(r)
    jug = [r for r in etats if r["exclu"] is None]; dom = [r for r in jug if r["dans_le_domaine"]]; hors = [r for r in jug if not r["dans_le_domaine"]]
    role = "ligne" if cr in LIGNES else "bord"
    assez = bool(etats and F(len(jug)) >= PART_JUGES * len(etats))
    expl = bool(assez and len(dom) >= DOM_MIN) if role == "ligne" else bool(assez and len(dom) >= BORD_MIN and len(hors) >= BORD_MIN)
    e1 = "INEXPLOITABLE" if not expl else ("TIENT" if all(r["dans_la_tolerance"] for r in dom) else "TOMBE")
    n_pres = sum(r["ordre3_plus_pres"] for r in dom); seuil = -(-PART_E2.numerator * len(dom) // PART_E2.denominator)
    e2 = None if cr != "N" else ("INEXPLOITABLE" if not expl else ("TIENT" if n_pres >= seuil else "TOMBE"))
    e3 = "VIDE" if not jug else ("TIENT" if all(r["dans_la_bande"] for r in jug) else "TOMBE")
    cel = {"id": pid, "creneau": cr, "role": role, "w2": str(w2), "facteur": str(fac), "delta": d, "g": g, "bande": B, "etats": etats, "n_lus": len(etats), "n_juges": len(jug),
           "n_domaine": len(dom), "n_hors": len(hors), "exploitable": expl, "E1": e1, "E2": e2, "E3": e3, "n_ordre3_plus_pres": n_pres, "seuil_E2": seuil,
           "pire_ln_q3_domaine": max([abs(r["ln_q3"]) for r in dom]) if dom else None, "pire_ln_q2": max([abs(r["ln_q2"]) for r in jug]) if jug else None,
           "exclus": sorted([[r["rang"], r["exclu"]] for r in etats if r["exclu"]]), "assez_de_juges": assez,
           "hors_ordre3_pire_que_ordre2": [sum((r["ln_q3"] is None) or abs(r["ln_q3"]) > abs(r["ln_q2"]) for r in hors), len(hors)],
           "signe_ln_q3_domaine": [sum(r["ln_q3"] < 0 for r in dom), sum(r["ln_q3"] > 0 for r in dom)]}
    out["cellules"].append(cel)
    print("  %-3s w2 = %-9s x%-4s : lus %2d, juges %2d, domaine %2d, hors %2d ; %s ; E1 %-13s E2 %-13s E3 %-5s ; pire |ln q3| du domaine %s ; pire |ln q2| %s" % (
        pid, w2, fac, len(etats), len(jug), len(dom), len(hors), "exploitable" if expl else "INEXPLOITABLE", e1, e2 if e2 else "-", e3,
        ("%.4f" % cel["pire_ln_q3_domaine"]) if dom else "-", ("%.4f" % cel["pire_ln_q2"]) if jug else "-"), flush=True)

def issue(cells, cle, max_inexpl, chutes_admises):
    """D'abord les chutes (ce sont des faits), ensuite les cellules inexploitables."""
    if not cells:
        return "SANS OBJET", [], 0
    ex = [c for c in cells if c[cle] != "INEXPLOITABLE"]; tombees = [c["id"] for c in ex if c[cle] == "TOMBE"]
    if len(tombees) > chutes_admises:
        return "TOMBE", tombees, len(ex)
    if len(cells) - len(ex) > max_inexpl:
        return "NON CONCLUANT", tombees, len(ex)
    return ("TENU" if not tombees else "TENU SAUF UNE CELLULE"), tombees, len(ex)
C = out["cellules"]; lig = [c for c in C if c["role"] == "ligne"]; ligN = [c for c in C if c["creneau"] == "N"]; brd = [c for c in C if c["role"] == "bord"]
out["E1"] = dict(zip(("issue", "tombees", "exploitables"), issue(lig, "E1", INEXPLOITABLES_E1, 1))); out["E1"]["cellules"] = len(lig)
out["E2"] = dict(zip(("issue", "tombees", "exploitables"), issue(ligN, "E2", INEXPLOITABLES_E2, 1))); out["E2"]["cellules"] = len(ligN)
out["E1B"] = dict(zip(("issue", "tombees", "exploitables"), issue(brd, "E1", 0, 0))); out["E1B"]["cellules"] = len(brd)
t3 = [c["id"] for c in C if c["E3"] == "TOMBE"]; out["E3"] = {"issue": "TENU" if not t3 else "TOMBE", "tombees": t3, "cellules": len(C), "vides": [c["id"] for c in C if c["E3"] == "VIDE"]}
out["comptes"] = {"lus": sum(c["n_lus"] for c in C), "juges": sum(c["n_juges"] for c in C), "domaine": sum(c["n_domaine"] for c in C), "hors": sum(c["n_hors"] for c in C)}
for k in ("E1", "E2", "E1B", "E3"):
    o = out[k]
    print("%-3s : %-22s (%d cellules%s ; tombees : %s)" % (k, o["issue"], o["cellules"], (", %d exploitables" % o["exploitables"]) if "exploitables" in o else "", ", ".join(o["tombees"]) or "aucune"))
print("etats : %d lus par le lecteur, %d juges, %d dans le domaine, %d hors" % (out["comptes"]["lus"], out["comptes"]["juges"], out["comptes"]["domaine"], out["comptes"]["hors"]))
if PREVOL:
    print("PRE-VOL : cette sortie ne juge rien")
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
