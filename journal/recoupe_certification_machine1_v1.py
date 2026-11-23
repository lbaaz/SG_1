# -*- coding: ascii -*-
"""RECOUPEMENT, PAR MACHINE 1, DE LA CERTIFICATION DE MACHINE 2 (lot 21e9bddfe5db83b2) -- v1, 2026-11-22. Aucun calcul de
physique : les fichiers de machine 2 sont lus comme des donnees, rien de son lot n'est execute.
  (1) sa table et sa table commune contre la table de machine 1 (canon B et contenu) ;
  (2) son detail contre la table complete de machine 1 : plus grands ecarts par cellule ;
  (3) le tirage de machine 1 sur la graine DEMONSTRATION, avec les DEUX tables, contre son journal de demonstration.
Usage : python3 -I recoupe_certification_machine1_v1.py <dossier certif de machine 2> <table m1> <table complete m1> <journal demonstration m1 a deux tables>"""
import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction as F
C, TAB1, FULL1, DEMO1 = sys.argv[1:5]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
t2 = os.path.join(C, "table_machine2_sommet_v1.json"); tc = os.path.join(C, "table_commune_sommet_machine2_v1.json")
print("(1) canons B : table de machine 1 %s ; table de machine 2 %s ; sa table commune %s" % (canon_B(TAB1), canon_B(t2), canon_B(tc)))
A = json.load(open(TAB1)); B = json.load(open(t2)); Cm = json.load(open(tc))
print("    contenu : table 2 = table 1 : %s ; table commune = table 1 : %s" % (A == B, A == Cm))
n_w = sum(len(A["creneaux"][s]["candidats"]) for s in A["creneaux"]); n_el = sum(c["eligible"] for s in A["creneaux"] for c in A["creneaux"][s]["candidats"])
print("    TABLE COMMUNE (ET des deux) : %d w2 eligibles sur %d ; %d cellules sur %d" % (n_el, n_w, sum(x["eligible"] for s in A["creneaux"] for c in A["creneaux"][s]["candidats"] for x in c["cellules"]), 7 * n_w))
D = json.load(open(os.path.join(C, "detail_machine2_sommet_v1.json"))); M1 = json.load(open(FULL1))
par_w = {F(v["w2"]): v for v in D.values()}
n = des = 0; e = {"ln_G3": 0.0, "etendue": 0.0, "e_bord": 0.0}
for s in ("MP", "PP", "MG", "PG"):
    for c in M1["creneaux"][s]["candidats"]:
        v = par_w[F(c["w2"])]; assert v["creneau"] == s and len(v["cellules"]) == 7
        for x, y in zip(c["cellules"], v["cellules"]):
            n += 1
            des += (x["kappa"], x["g"], x["eta0"], x["eligible"], x["cible"], x["barriere_vide"]) != (y["kappa"], y["g"], y["eta0"], y["eligible"], y["cible"], y["barriere_vide"])
            e["ln_G3"] = max(e["ln_G3"], abs(x["ln_G3"] - math.log(y["G3_plateau"]))); e["etendue"] = max(e["etendue"], abs(x["etendue"] - y["etendue"])); e["e_bord"] = max(e["e_bord"], abs(x["e_bord"] - y["e_bord"]))
print("(2) son detail contre ma table complete : %d cellules ; desaccords (kappa, g, eta0, eligibilite, cible, barriere vide) : %d" % (n, des))
print("    plus grands ecarts : ln du plateau %.2e ; etendue %.2e ; e_bord %.2e" % (e["ln_G3"], e["etendue"], e["e_bord"]))
print("    plus grand ecart, chez elle, entre la lecture par le flux et la valeur propre : %.2e" % max(y["ecart_flux_eig_max"] for v in D.values() for y in v["cellules"]))
mien = [tuple(m.groups()) for m in re.finditer(r"^\s+(\S+)\s+w2 = (\S+)\s+kappa = (\S+)\s+g = (\S+)\s+eta0 = (\S+)\s+r_c = (\d+)", open(DEMO1).read(), re.M)]
sien_txt = open(os.path.join(C, "tirage_demonstration_sommet_machine2_v1.log")).read()
print("(3) mon tirage de demonstration a DEUX tables : %d cellules ; w2 retenus : %s" % (len(mien), " ".join(sorted(set(m[1] for m in mien), key=lambda z: float(F(z))))))
# son journal : "=> MPa : w2 = 99991/50000 = 1.99982" puis sept lignes "MPa1  kappa 0.0363  g = ...  eta0 = ...  r_c = 22"
w_sien = {m.group(1): m.group(2) for m in re.finditer(r"^\s+=> (\w+) : w2 = (\S+) =", sien_txt, re.M)}
sien = {m.group(1): (m.group(2), m.group(3), m.group(4), m.group(5)) for m in re.finditer(r"^\s+(\w+\d)\s+kappa (\S+)\s+g = (\S+)\s+eta0 = (\S+)\s+r_c = (\d+)", sien_txt, re.M)}
trouve = sum(1 for m in mien if sien.get(m[0]) == (m[2], m[3], m[4], m[5]) and w_sien.get(m[0][:3]) == m[1])
print("    cellules de son journal de demonstration : %d ; identiques aux miennes (nom, w2, kappa, g, eta0, r_c) : %d sur %d" % (len(sien), trouve, len(mien)))
ok = (A == B == Cm) and des == 0 and n == 560 and e["ln_G3"] < 1e-9 and e["etendue"] < 1e-9 and trouve == len(mien) == len(sien) == 56
print("VERDICT DU RECOUPEMENT : %s" % ("TIENT" if ok else "NE TIENT PAS")); sys.exit(0 if ok else 1)
