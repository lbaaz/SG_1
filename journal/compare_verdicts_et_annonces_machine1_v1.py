# -*- coding: ascii -*-
"""LE VERDICT REJOUE PAR MACHINE 1 CONTRE CELUI DU RUN, ET SES ANNONCES RECOMPTEES -- machine 1, v1, 2026-11-23.
Aucun calcul de physique. Le verdict du run (ecrit par la feuille de machine 1 jouee chez machine 2) est lu comme une
donnee ; le verdict rejoue est celui de la meme feuille, au meme canon, jouee par machine 1 sur les fichiers du lot.
Usage : python3 -I compare_verdicts_et_annonces_machine1_v1.py <verdict du run.json> <verdict rejoue.json> <table gelee.json>"""
import sys, json, math, hashlib, unicodedata
from fractions import Fraction as F
VR, VM, TABLE = sys.argv[1:4]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
A = json.load(open(VR)); B = json.load(open(VM)); T = json.load(open(TABLE)); C = {c["id"]: c for c in T["cellules"]}
print("verdict du run : canon %s ; verdict rejoue : canon %s ; identiques a l'octet : %s" % (canon_B(VR), canon_B(VM), canon_B(VR) == canon_B(VM)))
print("feuille : %s et %s ; table : %s et %s ; graine : %s et %s" % (A["feuille_canon"], B["feuille_canon"], A["table_canon"], B["table_canon"], A["graine"], B["graine"]))
print("VERDICT du run : %s ; VERDICT rejoue : %s" % (A["verdict"], B["verdict"]))
print("instrument : %s et %s ; temoins positifs : %s (%d sur %d) et %s (%d sur %d)" % (A["instrument"], B["instrument"], A["temoins_positifs"]["issue"], A["temoins_positifs"]["tenus"], A["temoins_positifs"]["sur"],
      B["temoins_positifs"]["issue"], B["temoins_positifs"]["tenus"], B["temoins_positifs"]["sur"]))
print("S1 du run : %s %s ; S1 rejoue : %s %s" % (A["S1"]["issue"], A["S1"]["comptes"], B["S1"]["issue"], B["S1"]["comptes"]))
print("portee : %s ; et %s" % (" ".join(A["S1"]["portee_kappa"]), " ".join(B["S1"]["portee_kappa"])))
ca = {r["id"]: r for r in A["cellules"]}; cb = {r["id"]: r for r in B["cellules"]}
ej = sum(1 for i in ca if (ca[i]["jugement"], ca[i]["lecteur"]["statut"], ca[i]["lu"]) != (cb[i]["jugement"], cb[i]["lecteur"]["statut"], cb[i]["lu"]))
ecart = lambda k: max(abs(ca[i][k] - cb[i][k]) for i in ca)
print("cellules : %d et %d ; jugements, statuts ou lectures differents : %d ; plus grands ecarts : ln q %.1e ; ln Gamma_pl %.1e ; bande %.1e ; etalement %.1e" % (
    len(ca), len(cb), ej, ecart("ln_q"), ecart("ln_Gamma_pl"), ecart("bande"), ecart("etalement_du_lecteur")))
memes = (A["verdict"] == B["verdict"] and A["S1"]["issue"] == B["S1"]["issue"] and A["S1"]["comptes"] == B["S1"]["comptes"] and A["S1"]["portee_kappa"] == B["S1"]["portee_kappa"] and ej == 0
         and A["feuille_canon"] == B["feuille_canon"] == "ac934e0caaa59c08" and A["table_canon"] == B["table_canon"] == "4238e2b262119f83")
print("LES DEUX VERDICTS SONT LES MEMES : %s" % ("OUI" if memes else "NON"))
print()
print("=== CE QUE LE RUN DIT, DEPUIS LE VERDICT REJOUE")
R = B["cellules"]; lq = [r["ln_q"] for r in R]
print("cellules lues %d ; plus grand |ln q| %.5f (%s) ; plus grande bande %.5f ; plus grand etalement du lecteur %.5f ; plus petite marge T - b - |ln q| %.5f (%s)" % (
    sum(r["lu"] for r in R), max(abs(v) for v in lq), max(R, key=lambda r: abs(r["ln_q"]))["id"], max(r["bande"] for r in R), max(r["etalement_du_lecteur"] for r in R),
    min(r["tolerance"] - r["bande"] - abs(r["ln_q"]) for r in R), min(R, key=lambda r: r["tolerance"] - r["bande"] - abs(r["ln_q"]))["id"]))
print("lectures suivies du fantome : %d sur %d ; plus petit poids du site : %.4f ; jumeau : plus grand rapport au plateau %.2e" % (sum(r["lecteur"]["suivies"] for r in R), 48 * len(R),
      min(r["lecteur"]["poids_min"] for r in R), max(r["temoin"]["rapport_au_plateau"] for r in R)))
print("par kappa : ln q du plus petit au plus grand, et moyenne")
for k in sorted(set(r["kappa"] for r in R), key=float):
    v = sorted(r["ln_q"] for r in R if r["kappa"] == k); print("    %s   %+.5f a %+.5f   moyenne %+.5f   negatifs %d sur %d" % (k, v[0], v[-1], sum(v) / len(v), sum(x < 0 for x in v), len(v)))
print("plateaux lus : de %.5e a %.5e ; couplages de %s a %s" % (math.exp(min(r["ln_Gamma_pl"] for r in R)), math.exp(max(r["ln_Gamma_pl"] for r in R)), min((r["g"] for r in R), key=float), max((r["g"] for r in R), key=float)))
print()
print("=== MES ANNONCES DE LA SECTION 10, RECOMPTEES (elles ne sont pas des enonces juges)")
print("A-1 (0.95) l'instrument tient : %s" % ("oui" if B["instrument"] == "TIENT" else "NON"))
print("A-2 (0.97) les neuf temoins positifs tiennent : %s" % ("oui" if B["temoins_positifs"]["tenus"] == 9 else "NON"))
print("A-3 (0.95) le temoin tient aux 56 cellules : %s (%d sur 56)" % ("oui" if all(r["temoin"].get("tient") for r in R) else "NON", sum(1 for r in R if r["temoin"].get("tient"))))
nq = sum(1 for r in R if r["lecteur"]["statut"] == "QUALIFIE"); print("A-4 (0.70) le lecteur qualifie les 56 cellules : %s (%d sur 56)" % ("oui" if nq == 56 else "NON", nq))
print("A-5 S1 TENU (0.80) : %s" % B["S1"]["issue"])
print("A-6 (0.75) plus grand |ln q| sous 0.001 : %s (%.5f)" % ("oui" if max(abs(v) for v in lq) < 0.001 else "NON", max(abs(v) for v in lq)))
bar = [r for r in R if r["kappa"] in ("0.0363", "0.0530")]; nneg = sum(1 for r in bar if r["ln_q"] < 0)
print("A-7 (0.70) ln q negatif a douze cellules de barriere au moins sur seize : %s (%d sur %d ; a kappa = 0.0363 : %d sur 8 ; a 0.0530 : %d sur 8)" % ("oui" if nneg >= 12 else "NON", nneg, len(bar),
      sum(1 for r in bar if r["kappa"] == "0.0363" and r["ln_q"] < 0), sum(1 for r in bar if r["kappa"] == "0.0530" and r["ln_q"] < 0)))
mir = B["consigne"]["paires_miroirs"]; pres = sum(1 for m in mir if abs(m["ln_rapport_lu"] - m["ln_rapport_chaine"]) <= 0.0001)
print("A-8 (0.65) aux paires miroirs, rapport lu a 0.0001 de celui de la chaine a cinq paires au moins : %s (%d sur %d ; ecarts : %s)" % ("oui" if pres >= 5 else "NON", pres, len(mir),
      " ".join("%+.5f" % (m["ln_rapport_lu"] - m["ln_rapport_chaine"]) for m in mir)))
ech = B["consigne"]["loi_d_echelle"]; print("A-9 (0.75) a chaque kappa, etalement de ln(Gamma_pl / |delta|) sous 0.001 : %s (%s)" % ("oui" if all(e["etalement_lu"] < 0.001 for e in ech.values()) else "NON",
      " ; ".join("%s %.5f" % (k, ech[k]["etalement_lu"]) for k in sorted(ech, key=float))))
print("consigne : ordre 3 plus pres que le premier ordre a %d cellules sur %d ; ln q du signe de delta a %d ; ln q negatif a %d" % (B["consigne"]["ordre3_plus_pres_que_ordre1"], len(R),
      B["consigne"]["ln_q_du_signe_de_delta"], B["consigne"]["ln_q_negatif"]))
print("le signe de delta aux sept paires miroirs, lu (chaine) : %s" % " ; ".join("%s %+.5f (%+.5f)" % (m["kappa"], m["ln_rapport_lu"], m["ln_rapport_chaine"]) for m in mir))
sys.exit(0 if memes else 1)
