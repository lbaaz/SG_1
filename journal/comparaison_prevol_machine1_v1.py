# -*- coding: ascii -*-
"""COMPARAISON DU PRE-VOL (condition C4) -- machine 1, v1, 2026-11-15. Arithmetique sur des fichiers ; aucun calcul.
Le pre-vol a joue le chemin DERIVE (sonde du lecteur, feuille du lecteur, feuille d'ordre 3, pilote) sur un point DEJA
JOUE, la sortie du depot du delta 98 tenant lieu de sortie dense. Il est compare ici au chemin CERTIFIE :
  P1  etages 0, ancres et 1 : contre les sorties de la sonde certifiee du gel ter jouee sur LA MEME machine (meme code de
      mesure) : les mesures doivent etre IDENTIQUES, en-tete mis a part ;
  P2  mode point : contre le fichier du run certifie (autre machine si le pre-vol est celui de machine 1) : memes etats,
      memes suivis, lectures a 1e-6 pres en relatif (tolerance de rejeu du gel ter, section 12) ;
  P3  verdict du lecteur au point : memes statuts, largeurs de plateau a 1e-6 pres ;
  P4  feuille d'ordre 3 au point : memes comptes et memes verdicts de cellule que la feuille jouee sur le depot et le
      verdict du run certifie (table retrospective) ; ln q3 a 1e-5 pres ;
  P5  sonde dense derivee, rejouee au point : memes etiquettes que le depot ; Gamma_2D(3) a 1e-3 en relatif plus 1e-12 ;
      energie a 1e-9 (tolerances des ancres de la feuille d'ordre 3).
Usage : python3 -I comparaison_prevol_machine1_v1.py <dossier du pre-vol> <dossier certifie meme machine (etages 0, ancres,
        1)> <dossier du run certifie (points)> <id du point> <feuille d'ordre 3 retrospective.json> <sonde dense rejouee.json>
        <depot sonde_ordre2.json> <sortie.json>"""
import sys, os, json, math
PRE, MEME, RUN, PID, RETRO, DENSE, DEPOT, SORTIE = sys.argv[1:9]
ENTETE = ("sonde", "sonde_canon", "table_canon", "dense_canon", "prevol", "duree_s", "plateforme")
res = []
def on(b):
    return "oui" if b else "non"
def ctl(nom, ok, detail):
    res.append({"controle": nom, "tient": bool(ok), "detail": detail}); print("%-3s %-6s %s" % (nom, "TIENT" if ok else "MORD", detail))
def sans_durees(o):
    if isinstance(o, dict):
        return {k: sans_durees(v) for k, v in o.items() if k != "duree_s"}
    if isinstance(o, list):
        return [sans_durees(v) for v in o]
    return o
# P1
det = []
ok1 = True
for m in ("etage0", "ancres", "etage1"):
    a = json.load(open(os.path.join(PRE, "sonde_ter_%s.json" % m))); b = json.load(open(os.path.join(MEME, "sonde_ter_%s.json" % m)))
    ca = sans_durees({k: v for k, v in a.items() if k not in ENTETE}); cb = sans_durees({k: v for k, v in b.items() if k not in ENTETE})
    ident = (ca == cb); ok1 = ok1 and ident; det.append("%s %s" % (m, "identique" if ident else "DIFFERENT"))
ctl("P1", ok1, "mesures des etages 0, ancres et 1 contre la sonde certifiee sur la meme machine (en-tete et durees mis a part) : " + ", ".join(det))
# P2
a = json.load(open(os.path.join(PRE, "sonde_ter_point_%s.json" % PID)))["points"][0]; b = json.load(open(os.path.join(RUN, "sonde_ter_point_%s.json" % PID)))["points"][0]
ea = {e["rang"]: e for e in a["etats"]}; eb = {e["rang"]: e for e in b["etats"]}
memes = sorted(ea) == sorted(eb) and all((ea[r]["n1"], ea[r]["n2"]) == (eb[r]["n1"], eb[r]["n2"]) for r in ea)
pire = 0.0; n = 0; suivis = True
if memes:
    for r in ea:
        for x in ea[r]["traj"]:
            for k in ea[r]["traj"][x]:
                u, v = ea[r]["traj"][x][k], eb[r]["traj"][x][k]
                suivis = suivis and (u["suivi"] == v["suivi"])
                if u["suivi"] and v["suivi"]:
                    n += 1; pire = max(pire, abs(u["gamma"] / v["gamma"] - 1.0))
ctl("P2", memes and suivis and pire <= 1e-6, "point %s : %d etats, memes etiquettes : %s, memes suivis : %s ; %d lectures suivies, pire ecart relatif %.1e (tolerance 1e-6)" % (PID, len(ea), on(memes), on(suivis), n, pire))
# P3
va = json.load(open(os.path.join(PRE, "verdict_ter.json")))["points"][PID]; vb = json.load(open(os.path.join(RUN, "verdict_ter.json")))["points"][PID]
sa = {e["rang"]: e for e in va["etats"]}; sb = {e["rang"]: e for e in vb["etats"]}
st = sorted(sa) == sorted(sb) and all(sa[r]["statut"] == sb[r]["statut"] for r in sa)
pp = max([abs(math.log(sa[r]["plateaux"]["A"]["Gamma_pl"] / sb[r]["plateaux"]["A"]["Gamma_pl"])) for r in sa if "Gamma_pl" in sa[r]["plateaux"]["A"] and "Gamma_pl" in sb[r]["plateaux"]["A"]] or [0.0]) if st else None
ctl("P3", st and pp is not None and pp <= 1e-6, "verdict du lecteur a %s : %d etats, memes statuts : %s (QUALIFIES : %d) ; pire |ln| entre largeurs de plateau A : %s" % (
    PID, len(sa), on(st), sum(e["statut"] == "QUALIFIE" for e in sa.values()), ("%.1e" % pp) if pp is not None else "-"))
# P4
oa = [c for c in json.load(open(os.path.join(PRE, "verdict_ordre3.json")))["cellules"] if c["id"] == PID][0]; ob = [c for c in json.load(open(RETRO))["cellules"] if c["id"] == PID][0]
cles = ("n_lus", "n_juges", "n_domaine", "n_hors", "E1", "E3", "exploitable")
memes4 = all(oa[k] == ob[k] for k in cles)
ja = {e["rang"]: e for e in oa["etats"] if e["exclu"] is None}; jb = {e["rang"]: e for e in ob["etats"] if e["exclu"] is None}
p4 = max(abs(ja[r]["ln_q3"] - jb[r]["ln_q3"]) for r in ja) if sorted(ja) == sorted(jb) and ja else None
ctl("P4", memes4 and p4 is not None and p4 <= 1e-5, "feuille d'ordre 3 a %s : lus %d, juges %d, domaine %d, hors %d, E1 %s, E3 %s ; identiques a la feuille retrospective : %s ; pire ecart sur ln q3 : %s" % (
    PID, oa["n_lus"], oa["n_juges"], oa["n_domaine"], oa["n_hors"], oa["E1"], oa["E3"], on(memes4), ("%.1e" % p4) if p4 is not None else "-"))
# P5
da = [p for p in json.load(open(DENSE))["points"] if p["id"] == PID]; db = [p for p in json.load(open(DEPOT))["points"] if p["id"] == PID][0]
if len(da) != 1:
    ctl("P5", False, "la sonde dense rejouee ne porte pas le point %s" % PID)
else:
    da = da[0]; A = sorted(da["etats"], key=lambda e: e["rang"]); B = sorted(db["etats"], key=lambda e: e["rang"])
    et = [(x["n1"], x["n2"]) for x in A] == [(x["n1"], x["n2"]) for x in B]
    hors = sum(1 for x, y in zip(A, B) if abs(x["Gamma_2D"]["3"] - y["Gamma_2D"]["3"]) > 1e-12 + 1e-3 * abs(y["Gamma_2D"]["3"]) or abs(x["E_re"] - y["E_re"]) > 1e-9)
    pr = max(abs(x["Gamma_2D"]["3"] / y["Gamma_2D"]["3"] - 1.0) for x, y in zip(A, B) if y["Gamma_2D"]["3"] > 1.33e-12)
    pe = max(abs(x["E_re"] - y["E_re"]) for x, y in zip(A, B))
    ctl("P5", et and hors == 0 and da["N"] == db["N"] and da["r_c"] == db["r_c"] and abs(da["g"] / db["g"] - 1.0) <= 1e-12,
        "sonde dense derivee a %s : boite %d (depot %d), ecart relatif de couplage %.0e, 14 etiquettes identiques : %s ; pire ecart relatif de Gamma_2D(3) au-dessus de dix planchers %.1e ; pire ecart d'energie %.1e ; hors tolerance : %d ; duree %s s" % (
            PID, da["N"], db["N"], abs(da["g"] / db["g"] - 1.0) if da["g"] != db["g"] else 0.0, on(et), pr, pe, hors, da.get("duree_s")))
print("PRE-VOL : %d controles, %d tiennent" % (len(res), sum(r["tient"] for r in res)))
json.dump({"point": PID, "controles": res, "tient": all(r["tient"] for r in res)}, open(SORTIE, "w"), indent=1, sort_keys=True)
sys.exit(0 if all(r["tient"] for r in res) else 1)
