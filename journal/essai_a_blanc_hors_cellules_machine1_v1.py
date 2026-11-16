# -*- coding: ascii -*-
"""ESSAI A BLANC, HORS CELLULES, du chemin SANS --prevol -- machine 1, v1, 2026-11-16.
Le pre-vol eprouve le chemin derive avec --prevol. Le run, lui, se joue SANS : ses branches propres (table du gel, controles
de provenance, creneaux N, P, BN, BP) ne peuvent pas etre jouees pour de vrai avant le feu vert, puisque ce serait calculer
en 2D aux douze cellules. Cet essai les fait tourner SANS AUCUNE MESURE 2D A UNE CELLULE :
  S1  sonde dense, table du gel, sans --prevol, limitee a l'ancre A1 (point DEJA JOUE) : elle tourne et redonne le depot ;
  S2  sonde dense : la table du gel avec --prevol, et la table de pre-vol sans --prevol, sont refusees ;
  S3  sonde du lecteur, table du gel, sans --prevol, mode etage0 (les ancres, DEJA JOUEES) : memes mesures qu'au pre-vol ;
  S4  sonde du lecteur, mode point, sur une sortie dense FABRIQUEE : elle passe tous les controles de provenance et de forme
      et s'arrete au dernier (point declare infaisable), AVANT toute mesure ; une sortie dense sans canon de table est refusee ;
  S5  feuille du lecteur, etape "verdict", sans --prevol, sur des fichiers FABRIQUES : elle va au bout ;
  S6  feuille d'ordre 3, sans --prevol, sur ces fichiers : elle va au bout et rend une issue pour E1, E2, E1B et E3.
FABRIQUE veut dire : les mesures sont celles de points DEJA JOUES (depot du delta 98, run du gel ter), recopiees sous les
identifiants, w2, facteurs et couplages des cellules, avec les en-tetes que les scripts attendent. Ces fichiers ne disent
RIEN des cellules ; les issues que la feuille en tire n'ont aucun sens et ne sont ni affichees ni gardees : seul compte
que le chemin aille au bout. Les chaines que S6 calcule sont a une dimension.
Usage : python3 -I essai_a_blanc_hors_cellules_machine1_v1.py <dossier de l'instrument (lot extrait)> <moteur> <bloc2>
        <depot sonde_ordre2.json> <tp_retenus.json> <dossier du run du gel ter> <dossier du pre-vol> <dossier de travail (neuf)>
        <sortie.json>"""
import sys, os, json, copy, hashlib, unicodedata, subprocess, importlib.util
from fractions import Fraction as F
INST, MOTEUR, BLOC2, DEPOT, RETENUS, RUN_TER, PREVOL, TRAVAIL, SORTIE = sys.argv[1:10]
os.makedirs(TRAVAIL, exist_ok=False)
def canon_B(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n"); return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
def chemin(n):
    return os.path.join(INST, n)
TABLE, TABLE_PV = chemin("table_points_gel_loi_ordre3_v1.json"), chemin("table_points_prevol_gel_loi_ordre3_v1.json")
S_DENSE, S_LECT, F_LECT, F_O3, BLOC3 = (chemin(n) for n in ("sonde_dense_gel_loi_machine1_v1.py", "sonde_lecteur_gel_loi_machine1_v1.py", "lecture_lecteur_gel_loi_machine1_v1.py",
                                         "feuille_ordre3_machine1_v1.py", "ordre3_bloc_machine1_v1.py"))
CANONS = {os.path.basename(x): canon_B(x) for x in (TABLE, TABLE_PV, S_DENSE, S_LECT, F_LECT, F_O3, BLOC3)}
print("PIECES EPROUVEES (convention B) : " + " ; ".join("%s %s" % (v, k) for k, v in sorted(CANONS.items())), flush=True)
res = []
def ctl(nom, ok, detail):
    res.append({"essai": nom, "tient": bool(ok), "detail": detail}); print("%-3s %-6s %s" % (nom, "TIENT" if ok else "MORD", detail), flush=True)
def lancer(args):
    return subprocess.run([sys.executable, "-I", "-B"] + args, capture_output=True, text=True)
def ecrire(nom, obj):
    ch = os.path.join(TRAVAIL, nom); json.dump(obj, open(ch, "w"), indent=1, sort_keys=True); return ch
DEP = json.load(open(DEPOT)); dep = {p["id"]: p for p in DEP["points"]}; T = json.load(open(TABLE))
# S1
s1 = os.path.join(TRAVAIL, "dense_A1.json"); r = lancer([S_DENSE, MOTEUR, TABLE, s1, "A1"])
ok = r.returncode == 0 and os.path.exists(s1)
if ok:
    d = json.load(open(s1)); a = d["points"][0]; b = dep["A1"]; A = sorted(a["etats"], key=lambda e: e["rang"]); B = sorted(b["etats"], key=lambda e: e["rang"])
    hors = sum(1 for x, y in zip(A, B) if (x["n1"], x["n2"]) != (y["n1"], y["n2"]) or abs(x["Gamma_2D"]["3"] - y["Gamma_2D"]["3"]) > 1e-12 + 1e-3 * abs(y["Gamma_2D"]["3"]) or abs(x["E_re"] - y["E_re"]) > 1e-9)
    ok = (d["prevol"] is False and d["table_canon"] == canon_B(TABLE) and d["points_demandes"] == ["A1"] and len(A) == 14 and hors == 0)
    det = "code 0 ; prevol %s ; canon de la table du gel porte ; 14 etats ; hors tolerance des ancres contre le depot : %d ; duree %s s" % (d["prevol"], hors, a.get("duree_s"))
else:
    det = "code %d : %s" % (r.returncode, (r.stdout + r.stderr)[-200:])
ctl("S1", ok, "sonde dense, table du gel, sans --prevol, ancre A1 seule : " + det)
# S2
r1 = lancer([S_DENSE, MOTEUR, TABLE, os.path.join(TRAVAIL, "x1.json"), "A1", "--prevol"]); r2 = lancer([S_DENSE, MOTEUR, TABLE_PV, os.path.join(TRAVAIL, "x2.json"), "A1"])
ctl("S2", r1.returncode != 0 and r2.returncode != 0 and "REFUS" in r1.stderr + r1.stdout and "REFUS" in r2.stderr + r2.stdout and not os.path.exists(os.path.join(TRAVAIL, "x1.json"))
    and not os.path.exists(os.path.join(TRAVAIL, "x2.json")), "sonde dense : table du gel avec --prevol refusee (code %d) ; table de pre-vol sans --prevol refusee (code %d) ; rien n'est ecrit" % (r1.returncode, r2.returncode))
# --- fabrication d'une sortie dense aux identifiants des cellules, depuis des points deja joues ---
spec = importlib.util.spec_from_file_location("moteur", MOTEUR); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
SOURCE = {"N1": "C2", "N2": "C2", "N3": "M1", "N4": "M2", "N5": "M2", "P1": "C3", "P2": "C3", "P3": "C3", "P4": "C4", "P5": "C4", "BN": "M2", "BP": "M3"}
pts = []
for p in T["points"]:
    if p["role"] == "ancre":
        pts.append(copy.deepcopy(dep[p["id"]])); continue
    q = copy.deepcopy(dep[SOURCE[p["id"]]]); w2 = F(p["w2"]); fac = F(p["facteur"])
    q.update({"id": p["id"], "role": "juge", "w2": p["w2"], "facteur": p["facteur"], "g": float(M.g_du_point(w2)) * float(fac), "faisable": True}); pts.append(q)
entete = {"sonde": "FABRIQUE", "sonde_canon": canon_B(S_DENSE), "moteur_canon": canon_B(MOTEUR), "table_canon": canon_B(TABLE), "prevol": False, "points": pts}
f_dense = ecrire("dense_fabriquee.json", entete); c_dense = canon_B(f_dense)
# S3
d3 = os.path.join(TRAVAIL, "lecteur"); r = lancer([S_LECT, MOTEUR, DEPOT, RETENUS, TABLE, f_dense, c_dense, d3, "etage0"])
ok = r.returncode == 0 and os.path.exists(os.path.join(d3, "sonde_ter_etage0.json"))
if ok:
    a = json.load(open(os.path.join(d3, "sonde_ter_etage0.json"))); b = json.load(open(os.path.join(PREVOL, "sonde_ter_etage0.json")))
    def nu(o):
        if isinstance(o, dict):
            return {k: nu(v) for k, v in o.items() if k != "duree_s"}
        return [nu(v) for v in o] if isinstance(o, list) else o
    ok = a["prevol"] is False and a["table_canon"] == canon_B(TABLE) and nu(a["points"]) == nu(b["points"])
ctl("S3", ok, "sonde du lecteur, table du gel, sans --prevol, mode etage0 (ancres) : code %d ; mesures identiques a celles du pre-vol : %s" % (r.returncode, "oui" if ok else "non"))
# S4
mauvais = copy.deepcopy(entete)
for q in mauvais["points"]:
    if q["id"] == "N1":
        q["faisable"] = False
f_m = ecrire("dense_fabriquee_N1_infaisable.json", mauvais); r1 = lancer([S_LECT, MOTEUR, DEPOT, RETENUS, TABLE, f_m, canon_B(f_m), d3, "point", "N1"])
sans = copy.deepcopy(entete); del sans["table_canon"]; f_s = ecrire("dense_fabriquee_sans_table.json", sans); r2 = lancer([S_LECT, MOTEUR, DEPOT, RETENUS, TABLE, f_s, canon_B(f_s), d3, "point", "N1"])
r3 = lancer([S_LECT, MOTEUR, DEPOT, RETENUS, TABLE, f_dense, "0" * 16, d3, "point", "N1"])
t1, t2, t3 = (x.stderr + x.stdout for x in (r1, r2, r3))
ctl("S4", r1.returncode != 0 and "forme de la sortie dense au point N1" in t1 and r2.returncode != 0 and "n'a pas ete produite sur la table du gel" in t2 and r3.returncode != 0 and "canon passe par le pilote" in t3
    and not os.path.exists(os.path.join(d3, "sonde_ter_point_N1.json")),
    "sonde du lecteur, mode point N1, sans --prevol : arret au controle de forme (point infaisable) apres les controles de provenance ; sortie dense sans canon de table refusee ; canon passe faux refuse ; aucune mesure, aucun fichier")
# --- fabrication des fichiers du lecteur aux identifiants des cellules, depuis le run du gel ter ---
d5 = os.path.join(TRAVAIL, "run_fabrique"); os.makedirs(d5)
for n in ("sonde_ter_etage0.json", "sonde_ter_ancres.json", "sonde_ter_etage1.json", "verdict_ter_instrument.json"):
    open(os.path.join(d5, n), "wb").write(open(os.path.join(PREVOL, n), "rb").read())
for pid, src in SOURCE.items():
    s = json.load(open(os.path.join(RUN_TER, "sonde_ter_point_%s.json" % src)))
    s.update({"sonde": "FABRIQUE", "sonde_canon": canon_B(S_LECT), "table_canon": canon_B(TABLE), "dense_canon": c_dense, "prevol": False, "ids": [pid]}); s["points"][0]["id"] = pid
    json.dump(s, open(os.path.join(d5, "sonde_ter_point_%s.json" % pid), "w"), indent=1, sort_keys=True)
# S5
r = lancer([F_LECT, "verdict", d5, DEPOT, TABLE, f_dense, c_dense]); f_v = os.path.join(d5, "verdict_ter.json"); ok = r.returncode == 0 and os.path.exists(f_v)
if ok:
    v = json.load(open(f_v)); ok = (v["prevol"] is False and v["table_canon"] == canon_B(TABLE) and v["dense_canon"] == c_dense and v["feuille_canon"] == canon_B(F_LECT) and sorted(v["points"]) == sorted(SOURCE)
                                    and v["instrument"] == "TIENT")
ctl("S5", ok, "feuille du lecteur, etape verdict, sans --prevol, fichiers fabriques : code %d ; les douze points lus ; le verdict porte les canons de la table, de la sortie dense et de la feuille : %s" % (r.returncode, "oui" if ok else "non : " + r.stdout[-300:]))
# S6
if os.path.exists(f_v):
    f_o = os.path.join(TRAVAIL, "verdict_ordre3_fabrique.json"); r = lancer([F_O3, MOTEUR, BLOC2, BLOC3, TABLE, DEPOT, f_dense, c_dense, f_v, canon_B(f_v), f_o]); ok = r.returncode == 0 and os.path.exists(f_o)
    if ok:
        o = json.load(open(f_o)); issues = ("TENU", "TENU SAUF UNE CELLULE", "TOMBE", "NON CONCLUANT")
        ok = (o["prevol"] is False and o["instrument"] == "TIENT" and [c["id"] for c in o["cellules"]] == [p["id"] for p in T["points"] if p["role"] == "juge"] and all(o[k]["issue"] in issues for k in ("E1", "E2", "E1B", "E3"))
              and o["E1"]["cellules"] == 10 and o["E2"]["cellules"] == 5 and o["E1B"]["cellules"] == 2 and o["E3"]["cellules"] == 12 and "PRE-VOL" not in r.stdout)
    ctl("S6", ok, "feuille d'ordre 3, sans --prevol, fichiers fabriques : code %d ; douze cellules ; ancres tenues ; une issue rendue pour E1 (10 cellules), E2 (5), E1B (2), E3 (12) : %s (issues non affichees : elles n'ont aucun sens)" % (
        r.returncode, "oui" if ok else "non : " + (r.stdout + r.stderr)[-300:]))
    if os.path.exists(f_o):
        os.remove(f_o)
else:
    ctl("S6", False, "non joue : S5 n'a pas rendu de verdict")
import shutil
shutil.rmtree(os.path.join(TRAVAIL, "run_fabrique")); [os.remove(os.path.join(TRAVAIL, n)) for n in os.listdir(TRAVAIL) if n.startswith("dense_fabriquee")]      # les fichiers fabriques ne sont pas gardes
print("ESSAI A BLANC HORS CELLULES : %d essais, %d tiennent ; les fichiers fabriques sont effaces" % (len(res), sum(x["tient"] for x in res)))
json.dump({"essais": res, "tient": all(x["tient"] for x in res), "canons": CANONS}, open(SORTIE, "w"), indent=1, sort_keys=True)
sys.exit(0 if all(x["tient"] for x in res) else 1)
