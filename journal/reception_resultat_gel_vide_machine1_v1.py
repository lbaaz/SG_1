# -*- coding: ascii -*-
"""RECEPTION DU RESULTAT DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. ECRITE PENDANT LE RUN, AVANT TOUT RESULTAT.
Elle ne mesure rien et ne juge rien de plus que la feuille gelee : elle la REJOUE sur les fichiers de machine 2, compare les
deux verdicts, et lit les sept annonces de la plume (section 10 de la seconde partie) contre l'issue. Les probabilites des
annonces sont LUES dans le texte du gel (canon controle), pas recopiees.
  1. INVENTAIRE du dossier du run : les 28 fichiers de cellule, le verdict de l'instrument, le verdict de machine 2.
  2. REJEU de feuille_vide_machine1_v1.py (canon controle) sur ce dossier ; la sortie va dans le dossier de sortie, rien
     n'est ecrit dans le dossier du run.
  3. COMPARAISON des deux verdicts : tout champ discret doit etre egal ; les nombres sont compares et leur plus grand ecart
     est rendu. Si un champ discret differe : VERDICTS DIFFERENTS, et l'acte donnera les deux (section 11 du gel) ; les
     champs d'issue, de jugement et de statut qui different sont listes a part des champs consignes.
  4. ANNONCES, lues sur le verdict REJOUE. Conventions fixees ici, avant le resultat :
     A-1 l'instrument TIENT.
     A-2 le temoin tient aux 28 cellules. La feuille ne juge le temoin qu'aux cellules ou le lecteur est QUALIFIE (il lui
         faut le plateau). VRAIE si 28 temoins tenus ; FAUSSE si un temoin juge ne tient pas ; sinon INDETERMINEE. A titre
         d'indication, hors annonce, le rapport de la plus grande largeur du jumeau a la largeur PREDITE est rendu partout.
     A-3 nombre de cellules lisibles ou le lecteur est QUALIFIE : seize ; douze au moins.
     A-4 issue de V1 ; A-5 issue de VP. Si l'instrument ne tient pas ou si le run est incomplet : "instrument".
     A-6 aux cellules lisibles LUES (qui portent un ln q), le plus grand |ln q| est sous 0.01. Sans cellule lue : INDETERMINEE.
     A-7 aux cellules lisibles lues de MG : ln q negatif (comme delta) a trois cellules au moins ; positif a trois au moins ;
         sinon "ni l'un ni l'autre", dont la probabilite est le reste.
Usage : python3 -I -B reception_resultat_gel_vide_machine1_v1.py <feuille_vide.py> <lecture_lecteur_gel_loi (deposee)>
        <table gelee.json> <gel partie 2.md> <dossier du run recu> <dossier de sortie (neuf)>"""
import sys, os, re, json, math, hashlib, unicodedata, subprocess
FEUILLE, F_LECT, TABLE, GEL, RUN, SORTIE = sys.argv[1:7]
CANON_FEUILLE, CANON_TABLE, CANON_GEL = "ac39a24def6c7420", "b71206e5daf6c741", "eebd979f18d8db48"
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
assert canon_B(FEUILLE) == CANON_FEUILLE and canon_B(TABLE) == CANON_TABLE and canon_B(GEL) == CANON_GEL, "feuille, table ou gel hors canon"
os.makedirs(SORTIE, exist_ok=False)
T = json.load(open(TABLE)); CELLULES = T["cellules"]; assert len(CELLULES) == 28
out = {"piece": "reception_resultat_gel_vide_machine1_v1", "feuille_canon": CANON_FEUILLE, "table_canon": CANON_TABLE, "gel_canon": CANON_GEL}

# --- les probabilites des annonces, lues dans le gel
g = open(GEL, encoding="ascii").read(); s10 = g[g.index("\n10. ANNONCES DE LA PLUME"):g.index("\n11. DEROULEMENT")]
s10 = " ".join(s10.split())
def pr(motif):
    m = re.search(motif, s10); assert m, motif
    return [float(x) for x in m.groups()]
PA = {"A-1": pr(r"A-1 \(([0-9.]+)\) l'instrument du lecteur tient")[0], "A-2": pr(r"A-2 \(([0-9.]+)\) le temoin tient aux 28 cellules")[0]}
PA["A-3"] = dict(zip(("seize", "douze_au_moins"), pr(r"A-3 \(([0-9.]+)\) le lecteur qualifie les seize cellules lisibles ; \(([0-9.]+)\) au moins douze")))
PA["A-4"] = dict(zip(("TENU", "TENU SAUF UNE CELLULE", "TOMBE", "NON CONCLUANT", "instrument"),
                     pr(r"A-4 V1 : TENU ([0-9.]+) ; TENU SAUF UNE CELLULE ([0-9.]+) ; TOMBE ([0-9.]+) ; NON CONCLUANT ([0-9.]+) ; le reste \(([0-9.]+)\) est l'instrument")))
PA["A-5"] = dict(zip(("TENU", "TENU SAUF UNE CELLULE", "TOMBE", "NON LUE ou NON CONCLUANT", "instrument"),
                     pr(r"A-5 VP : TENU ([0-9.]+) ; TENU SAUF UNE CELLULE ([0-9.]+) ; TOMBE ([0-9.]+) ; NON LUE ou NON CONCLUANT ([0-9.]+) ; le reste \(([0-9.]+)\) est l'instrument")))
PA["A-6"] = dict(zip(("probabilite", "seuil"), pr(r"A-6 \(([0-9.]+)\) aux cellules lisibles lues, le plus grand \|ln q\| est sous ([0-9.]+)\.")))
PA["A-7"] = dict(zip(("negatif", "positif"), pr(r"negatif, comme delta, a trois cellules au moins : ([0-9.]+) ; positif, comme la lecture \(b\), a trois au moins : ([0-9.]+)\.")))
PA["A-7"]["ni l'un ni l'autre"] = round(1.0 - PA["A-7"]["negatif"] - PA["A-7"]["positif"], 10)
for k in ("A-4", "A-5"):
    assert abs(sum(PA[k].values()) - 1.0) < 1e-9, (k, PA[k])
out["annonces_gelees"] = PA

# --- 1. inventaire
attendus = ["sonde_vide_%s.json" % c["id"] for c in CELLULES] + ["verdict_ter_instrument.json", "verdict_vide.json"]
presents = sorted(os.listdir(RUN)); manquent = [f for f in attendus if f not in presents]
out["inventaire"] = {"fichiers": len(presents), "attendus": len(attendus), "manquent": manquent}
print("=" * 100); print("RECEPTION DU RESULTAT DU GEL LARGEUR DU VIDE -- machine 1"); print("=" * 100)
print("1. INVENTAIRE : %d fichiers dans le dossier du run ; %d attendus ; manquent : %s" % (len(presents), len(attendus), manquent or "aucun"))

# --- 2. rejeu de la feuille
mien = os.path.join(SORTIE, "verdict_vide_rejoue_machine1.json")
p = subprocess.run([sys.executable, "-I", "-B", FEUILLE, F_LECT, TABLE, RUN, mien], capture_output=True, text=True)
open(os.path.join(SORTIE, "feuille_vide_rejouee_machine1.console.log"), "w", encoding="utf-8", newline="\n").write(p.stdout + p.stderr)
out["rejeu"] = {"code": p.returncode, "verdict_ecrit": os.path.exists(mien)}
print("2. REJEU de la feuille : code %d ; verdict ecrit : %s" % (p.returncode, os.path.exists(mien)))
if not os.path.exists(mien):
    out["conclusion"] = "LA FEUILLE REFUSE LE DOSSIER : %s" % (p.stdout.strip().splitlines() or ["?"])[-1]
    print(out["conclusion"]); json.dump(out, open(os.path.join(SORTIE, "reception_resultat_vide_v1.json"), "w"), indent=1, sort_keys=True); sys.exit(3)
V = json.load(open(mien))

# --- 3. comparaison des deux verdicts
def aplatir(o, chemin=""):
    if isinstance(o, dict):
        for k in sorted(o):
            for x in aplatir(o[k], chemin + "/" + str(k)):
                yield x
    elif isinstance(o, list):
        if o and all(isinstance(x, dict) and "id" in x for x in o):
            for x in o:
                for y in aplatir(x, chemin + "/" + x["id"]):
                    yield y
        else:
            yield chemin, json.dumps(o, sort_keys=True)
    else:
        yield chemin, o
f2 = os.path.join(RUN, "verdict_vide.json")
if os.path.exists(f2):
    A, B = dict(aplatir(V)), dict(aplatir(json.load(open(f2))))
    discrets, nombres, pire = [], 0, (0.0, None)
    for k in sorted(set(A) | set(B)):
        a, b = A.get(k, "<absent>"), B.get(k, "<absent>")
        if isinstance(a, float) and isinstance(b, float):
            if math.isnan(a) or math.isnan(b):
                if not (math.isnan(a) and math.isnan(b)):
                    discrets.append({"champ": k, "machine1": repr(a), "machine2": repr(b)})
                continue
            nombres += 1; e = abs(a - b)
            if e > pire[0]:
                pire = (e, k)
        elif a != b:
            discrets.append({"champ": k, "machine1": a, "machine2": b})
    out["comparaison"] = {"champs": len(set(A) | set(B)), "nombres_compares": nombres, "plus_grand_ecart": pire[0], "plus_grand_ecart_champ": pire[1],
                          "champs_discrets_differents": discrets, "issue": "VERDICTS IDENTIQUES" if not discrets else "VERDICTS DIFFERENTS",
                          "dont_issues_jugements_statuts": [d["champ"] for d in discrets if d["champ"].endswith(("/issue", "/jugement", "/statut", "/verdict", "/instrument", "/tombees", "/motif"))
                                                            or "/comptes/" in d["champ"]]}
    print("3. COMPARAISON au verdict de machine 2 : %d champs, dont %d nombres ; plus grand ecart d'un nombre %.1e (%s) ; champs discrets differents : %d -> %s" % (
        len(set(A) | set(B)), nombres, pire[0], pire[1], len(discrets), out["comparaison"]["issue"]))
    print("     dont issues, jugements, statuts : %s" % (out["comparaison"]["dont_issues_jugements_statuts"] or "aucun"))
    for d in discrets[:40]:
        print("     %s : machine 1 %r ; machine 2 %r" % (d["champ"], d["machine1"], d["machine2"]))
else:
    out["comparaison"] = {"issue": "LE VERDICT DE MACHINE 2 MANQUE AU DOSSIER"}; print("3. COMPARAISON : %s" % out["comparaison"]["issue"])

# --- 4. annonces
juge = "V1" in V; cel = {r["id"]: r for r in V["cellules"]}; TC = {c["id"]: c for c in CELLULES}
lis = [r for r in V["cellules"] if r.get("ligne") == "lisible"]
AN = {}
AN["A-1"] = {"evenement": "l'instrument tient", "probabilite": PA["A-1"], "realise": V.get("instrument") == "TIENT"}
tem = [r.get("temoin") for r in V["cellules"]]
tenus = sum(1 for t in tem if t and t.get("tient") is True); non_tenus = [r["id"] for r in V["cellules"] if r.get("temoin") and r["temoin"].get("tient") is False]
indic = {}
for r in V["cellules"]:
    t = r.get("temoin")
    if t and t.get("plus_grande_largeur") is not None:
        indic[r["id"]] = t["plus_grande_largeur"] / math.exp(TC[r["id"]]["ln_G3"])
AN["A-2"] = {"evenement": "le temoin tient aux 28 cellules", "probabilite": PA["A-2"], "temoins_tenus": tenus, "temoins_non_tenus": non_tenus,
             "realise": (True if tenus == 28 else (False if non_tenus else "INDETERMINEE")),
             "indication_plus_grand_rapport_a_la_largeur_predite": (max(indic.values()) if indic else None), "indication_cellules": len(indic)}
nq = sum(1 for r in lis if r.get("lecteur", {}).get("statut") == "QUALIFIE") if all("lecteur" in r for r in lis) and len(lis) == 16 else None
AN["A-3"] = {"evenement": "le lecteur qualifie les seize cellules lisibles ; douze au moins", "probabilites": PA["A-3"], "qualifiees": nq,
             "realise": ({"seize": nq == 16, "douze_au_moins": nq >= 12} if nq is not None else "INDETERMINEE")}
def issue(nom, table, fusion=None):
    if not juge:
        return "instrument"
    i = V[nom]["issue"]
    return fusion if (fusion and i in ("NON LUE", "NON CONCLUANT")) else i
i4 = issue("V1", PA["A-4"]); AN["A-4"] = {"evenement": "issue de V1", "probabilites": PA["A-4"], "realise": i4, "probabilite_de_l_issue": PA["A-4"][i4]}
i5 = issue("VP", PA["A-5"], "NON LUE ou NON CONCLUANT"); AN["A-5"] = {"evenement": "issue de VP", "probabilites": PA["A-5"], "realise": i5, "probabilite_de_l_issue": PA["A-5"][i5]}
lq = [(abs(r["ln_q"]), r["id"]) for r in lis if "ln_q" in r]
AN["A-6"] = {"evenement": "aux cellules lisibles lues, le plus grand |ln q| est sous %s" % PA["A-6"]["seuil"], "probabilite": PA["A-6"]["probabilite"], "cellules_lues": len(lq),
             "plus_grand": (max(lq)[0] if lq else None), "cellule": (max(lq)[1] if lq else None), "realise": ((max(lq)[0] < PA["A-6"]["seuil"]) if lq else "INDETERMINEE")}
mg = [r for r in lis if r["creneau"] == "MG" and "ln_q" in r]; neg = [r["id"] for r in mg if r["ln_q"] < 0]; pos = [r["id"] for r in mg if r["ln_q"] > 0]
i7 = "negatif" if len(neg) >= 3 else ("positif" if len(pos) >= 3 else "ni l'un ni l'autre")
AN["A-7"] = {"evenement": "signe de ln q aux cellules lisibles lues de MG", "probabilites": PA["A-7"], "lues": len(mg), "negatives": neg, "positives": pos, "realise": i7,
             "probabilite_de_l_issue": PA["A-7"][i7], "ln_q": {r["id"]: r["ln_q"] for r in mg}, "bande": {r["id"]: r["bande"] for r in mg},
             "au_dela_de_la_bande": [r["id"] for r in mg if abs(r["ln_q"]) > r["bande"]]}
out["annonces"] = AN; out["verdict_rejoue"] = V.get("verdict")
print("4. ANNONCES (lues sur le verdict rejoue : %s)" % V.get("verdict"))
print("   A-1 (%.2f) l'instrument tient : %s" % (PA["A-1"], AN["A-1"]["realise"]))
print("   A-2 (%.2f) le temoin tient aux 28 cellules : %s (%d tenus ; non tenus : %s) ; indication : plus grand rapport a la largeur predite %s sur %d cellules" % (
    PA["A-2"], AN["A-2"]["realise"], tenus, non_tenus or "aucun", ("%.1e" % max(indic.values())) if indic else "--", len(indic)))
print("   A-3 (%.2f ; %.2f) lecteur QUALIFIE aux cellules lisibles : %s sur 16 -> %s" % (PA["A-3"]["seize"], PA["A-3"]["douze_au_moins"], nq, AN["A-3"]["realise"]))
print("   A-4 V1 : %s (annonce a %.2f)" % (i4, PA["A-4"][i4])); print("   A-5 VP : %s (annonce a %.2f)" % (i5, PA["A-5"][i5]))
print("   A-6 (%.2f) plus grand |ln q| lisible lu : %s -> %s" % (PA["A-6"]["probabilite"], ("%.4f a %s, sur %d cellules" % (max(lq)[0], max(lq)[1], len(lq))) if lq else "--", AN["A-6"]["realise"]))
print("   A-7 MG lisibles lues : %d ; ln q negatif a %s ; positif a %s -> %s (annonce a %.2f) ; au-dela de la bande : %s" % (
    len(mg), neg or "aucune", pos or "aucune", i7, PA["A-7"][i7], AN["A-7"]["au_dela_de_la_bande"] or "aucune"))
json.dump(out, open(os.path.join(SORTIE, "reception_resultat_vide_v1.json"), "w"), indent=1, sort_keys=True)
print("ecrit %s" % os.path.join(SORTIE, "reception_resultat_vide_v1.json"))
