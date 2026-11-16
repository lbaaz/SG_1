# -*- coding: ascii -*-
"""VERIFICATION DES DEUX CORRECTIONS DE TEXTE DE MACHINE 2 (C-1, C-2) ET DE SA PRECISION SUR A-7 -- machine 1, v1, 2026-11-16.
Aucun calcul de physique nouveau : relit la table gelee, la verification des etats joues et la superposition.
C-1 : la forme fermee de la table est calculee avec M0 = (2 lambda)^(-2/3), lambda = kappa X_c / (P tau_0), tau_0 etant le saut au
      pied de l'echelle a w2 = 2 pour un couplage unite ; kappa est celui de la cellule. Avec lambda = g X_c / (P |delta|), la
      definition ecrite dans la note sur la loi d'echelle, de combien differe-t-elle ?
C-2 : la part manquee f = (r - r de la chaine) / r aux etats joues : combien sont positives, entre 0 et 1, au-dessus de 1, negatives.
A-7 : a combien de cellules lisibles les lectures (a) et (b) du signe du residu different.
Usage : python3 -I -B verifie_C1_C2_machine1_v1.py <table gelee.json> <verifie_variantes_joues_v1.json> <superposition_v1.json> <sortie.json>"""
import sys, json, math
TABLE, VERIF, SUPER, SORTIE = sys.argv[1:5]
T = json.load(open(TABLE)); FF = T["forme_fermee"]; P = 5
out = {}
# C-1
pire = 0.0; pire_id = None; refait = 0.0; rapport = []
for c in T["cellules"]:
    d = abs(c["delta"]); g = float(c["g"])
    M0 = c["M0"]; l_table = math.log(d) - FF["B"] * M0 + FF["c"] * math.log(M0) + FF["d"]; refait = max(refait, abs(l_table - c["ln_forme_fermee"]))
    lam_note = g * FF["X_c"] / (P * d); M0n = (2.0 * lam_note) ** (-2.0 / 3.0); l_note = math.log(d) - FF["B"] * M0n + FF["c"] * math.log(M0n) + FF["d"]
    lam_table = 0.5 * M0 ** (-1.5); rapport.append((c["id"], lam_table / lam_note))
    if abs(l_note - c["ln_forme_fermee"]) > pire:
        pire = abs(l_note - c["ln_forme_fermee"]); pire_id = c["id"]
out["C1"] = {"forme_refaite_depuis_M0_ecart_max": refait, "ecart_max_avec_la_definition_de_la_note": pire, "cellule": pire_id,
             "rapport_lambda_min": min(x[1] for x in rapport), "rapport_lambda_max": max(x[1] for x in rapport)}
print("C-1 la forme fermee de la table se refait depuis son M0 a %.1e pres ; avec lambda = g X_c / (P |delta|) elle differe de %.2f au pire (a %s)" % (refait, pire, pire_id))
print("    rapport des deux lambda (celui de la table sur celui de la note) : de %.4f a %.4f ; c'est X(0, 0 ; w2) / X(0, 0 ; 2)" % (out["C1"]["rapport_lambda_min"], out["C1"]["rapport_lambda_max"]))
# C-2
SU = {(e["source"], e["id"], e["rang"]): e for e in json.load(open(SUPER))["etats"] if e["domaine"]}
VE = json.load(open(VERIF))["etats"]; f = []
for e in VE:
    s = SU[(e["source"], e["id"], e["rang"])]; f.append((-e["q_mediane"] / s["r"], e["id"], e["rang"], s["r"], e["delta"]))
pos = [x for x in f if x[0] > 0]; entre = [x for x in f if 0 < x[0] < 1]; plus = [x for x in f if x[0] >= 1]; neg = [x for x in f if x[0] <= 0]
oppose = sum(1 for x in f if x[3] * x[4] < 0); meme = [(x[1], x[2], x[3], x[4], x[0]) for x in f if x[3] * x[4] >= 0]
out["C2"] = {"etats": len(f), "part_positive": len(pos), "entre_0_et_1": len(entre), "au_dessus_de_1": [(x[1], x[2], x[3]) for x in plus], "negative": [(x[1], x[2], x[0]) for x in neg], "r_oppose_a_delta": oppose, "r_du_signe_de_delta": meme}
print("C-2 %d etats ; part manquee positive : %d ; entre 0 et 1 : %d ; au-dessus de 1 : %d %s ; negative : %d %s ; r de signe oppose a delta : %d" % (
    len(f), len(pos), len(entre), len(plus), ["%s rang %d (r = %+.4f)" % (x[1], x[2], x[3]) for x in plus], len(neg), ["%s rang %d (part %.2f)" % (x[1], x[2], x[0]) for x in neg], oppose))
print("    r du signe de delta : %s" % ["%s rang %d (r = %+.4f, delta = %+.3f, part %.2f)" % x for x in meme])
# A-7
dif = [c["id"] for c in T["cellules"] if c["ligne"] == "lisible" and c["attente"]["sous_correction_mediane"] * c["attente"]["signe_de_delta"] < 0]
mem = [c["id"] for c in T["cellules"] if c["ligne"] == "lisible" and c["attente"]["sous_correction_mediane"] * c["attente"]["signe_de_delta"] > 0]
pp = max(abs(c["attente"]["sous_correction_pire"]) for c in T["cellules"] if c["id"] in ("PP3", "PP4", "PP5", "PP6"))
par = {}
for cr in ("MG", "MP", "PP", "PG"):
    L = [c for c in T["cellules"] if c["creneau"] == cr and c["ligne"] == "lisible"]; assert len(L) == 4
    par[cr] = {"mediane": max(abs(c["attente"]["sous_correction_mediane"]) for c in L), "pire": max(abs(c["attente"]["sous_correction_pire"]) for c in L),
               "etendue_min": min(c["etendue"] for c in L)}
out["A7"] = {"lectures_differentes": dif, "lectures_de_meme_signe": mem, "residu_b_pire_a_PP": pp, "residu_b_par_creneau": par}
print("A-7 les lectures (a) et (b) different a %d cellules lisibles : %s ; elles coincident a %d : %s" % (len(dif), " ".join(dif), len(mem), " ".join(mem)))
print("    au creneau PP le residu attendu sous (b) vaut %.4f au plus, pour la plus grande part manquee" % pp)
for cr in ("MG", "MP", "PP", "PG"):
    print("    %s : plus grand residu attendu sous (b), part manquee mediane %.4f, plus grande part %.4f ; plus petite etendue de la chaine %.4f" % (
        cr, par[cr]["mediane"], par[cr]["pire"], par[cr]["etendue_min"]))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
