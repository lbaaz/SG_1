# -*- coding: ascii -*-
"""LE PONT : les parts sont-elles de type Porter-Thomas ? -- machine 1, v1, 2026-11-16. Hors chaine, classe 3. AUCUN NOUVEAU CALCUL
de physique : relecture des sorties existantes (pont_2d_force_m*_v2.json, pont_2d_grand_m*_v1.json, pont_2d_sacrifie_*_v1.json).
Hypothese de machine 2 (lue sur les tableaux de la note v3, 23 h 00) : la participation ne suit plus le compte parce que les
parts deviennent aleatoires ; a parts de Porter-Thomas (amplitudes gaussiennes), l'inverse de la participation vaut en moyenne
3 / (n + 2) pour n niveaux. Ici : (1) rapport R = IPR observe / (3 / (n + 2)), par tranche de cotes -- R = 1 : Porter-Thomas ;
R < 1 : parts plus egales que le hasard ; R > 1 : plus inegales ; (2) quantiles des parts normalisees y / moyenne de la boite,
contre un tirage de Porter-Thomas traite de la meme facon ; (3) ce que vaudrait une boite de 22 ou de 29 niveaux, et sa dispersion ;
(4) les croisements de la section 2 de la note : la part du niveau croise, contre les parts des niveaux de la boite nue de meme cote.
Usage : python3 -I -B pont_porter_thomas_regard_machine1_v1.py <dossier des sorties> <sortie.json>"""
import sys, os, json, math, random
D, SORTIE = sys.argv[1:3]
def J(n): return json.load(open(os.path.join(D, n)))
B = []                                    # (barreaux, cote, [y_k])
for m in (3, 4, 5):
    F = J("pont_2d_force_m%d_v2.json" % m); B += [(m, b["N"], [v[2] for v in b["niveaux_2d"]]) for b in F["boites"]]
    G = J("pont_2d_grand_m%d_v1.json" % m); B += [(m, b["N"], [v[1] for v in b["niveaux"]]) for b in G["boites"]]
B += [(3, b["N"], [v[1] for v in b["niveaux"]]) for b in J("pont_2d_grand_m3_cote200_v1.json")["boites"]]
random.seed(20261116); out = {"piece": "pont_porter_thomas_regard_machine1_v1", "tranches": [], "quantiles": {}, "tirage": {}, "croisements": []}
def ipr(ys): s = sum(ys); return sum((y / s) ** 2 for y in ys)
def pt(n): return [random.gauss(0.0, 1.0) ** 2 for _ in range(n)]
print("(1) par tranche de cotes, toutes profondeurs : boites, niveaux par boite, participation moyenne, IPR moyen, 3/(n+2) moyen, R = IPR / (3/(n+2)), et R d'un tirage de Porter-Thomas aux memes n (moyenne +- ecart type de la moyenne de tranche)")
for a, b in ((21, 27), (28, 34), (35, 45), (46, 64), (72, 81), (96, 113), (128, 129), (150, 151), (200, 201)):
    bs = [x for x in B if a <= x[1] <= b and len(x[2]) >= 2]
    if not bs:
        continue
    n = [len(x[2]) for x in bs]; io = [ipr(x[2]) for x in bs]; ref = [3.0 / (k + 2) for k in n]; R = (sum(io) / len(io)) / (sum(ref) / len(ref))
    sim = []
    for _ in range(2000):
        s = [ipr(pt(k)) for k in n]; sim.append((sum(s) / len(s)) / (sum(ref) / len(ref)))
    ms = sum(sim) / len(sim); es = math.sqrt(sum((v - ms) ** 2 for v in sim) / len(sim)); egal = (sum(1.0 / k for k in n) / len(n)) / (sum(ref) / len(ref))
    rec = {"cotes": [a, b], "boites": len(bs), "niveaux": sum(n) / len(n), "participation": sum(1.0 / v for v in io) / len(io), "R": R, "R_PT": ms, "R_PT_ecart": es, "R_parts_egales": egal}; out["tranches"].append(rec)
    print("   cotes %3d a %3d : %2d boites  n = %5.2f  participation %5.2f  R = %.2f   (Porter-Thomas : %.2f +- %.2f ; parts egales : %.2f)" % (a, b, len(bs), rec["niveaux"], rec["participation"], R, ms, es, egal))
print("(2) parts normalisees y / moyenne de la boite, boites d'au moins 9 niveaux : fraction sous 0.01, sous 0.1, mediane, fraction au-dessus de 3 ; puis le meme traitement sur un tirage de Porter-Thomas aux memes n")
gr = [x for x in B if len(x[2]) >= 9]
def stat(listes):
    s = sorted(y / (sum(ys) / len(ys)) for ys in listes for y in ys); k = len(s)
    return {"niveaux": k, "sous_0.01": sum(1 for v in s if v < 0.01) / k, "sous_0.1": sum(1 for v in s if v < 0.1) / k, "mediane": s[k // 2], "au_dessus_de_3": sum(1 for v in s if v > 3) / k}
so = stat([x[2] for x in gr]); sims = [stat([pt(len(x[2])) for x in gr]) for _ in range(2000)]
out["quantiles"]["observe"] = so; out["quantiles"]["boites"] = len(gr)
for cle in ("sous_0.01", "sous_0.1", "mediane", "au_dessus_de_3"):
    v = [t[cle] for t in sims]; mv = sum(v) / len(v); ev = math.sqrt(sum((q - mv) ** 2 for q in v) / len(v)); out["quantiles"][cle] = {"PT": mv, "ecart": ev}
    print("   %-15s observe %.3f   Porter-Thomas %.3f +- %.3f   (%d niveaux, %d boites)" % (cle, so[cle], mv, ev, so["niveaux"], len(gr)))
print("(3) une boite de n niveaux a parts de Porter-Thomas : participation moyenne +- ecart type d'UNE boite")
for n in (11, 14, 22, 29):
    v = [1.0 / ipr(pt(n)) for _ in range(20000)]; mv = sum(v) / len(v); ev = math.sqrt(sum((q - mv) ** 2 for q in v) / len(v)); out["tirage"][str(n)] = {"moyenne": mv, "ecart": ev}
    print("   n = %2d : %.2f +- %.2f" % (n, mv, ev))
print("(4) croisements de la section 2 : y du niveau croise = 2 pi V^2 / (Gamma |delta|), u du croisement, et les niveaux de la boite NUE de meme cote dans la fenetre (ecart en |delta| : y)")
for nom in ("pont_2d_sacrifie_v1.json", "pont_2d_sacrifie_m3_v1.json", "pont_2d_sacrifie_m4_v1.json", "pont_2d_sacrifie_m5_v1.json"):
    S = J(nom); m = S["m_bord"]; G = S["Gamma_chaine_ordre3"]; ad = 0.02; F = J("pont_2d_force_m%d_v2.json" % m)
    assert S["w2"] == "101/50"
    for x in S["boites"]:
        c = x["boite_2d"][0]; yc = 2 * math.pi * c["V"] ** 2 / (G * ad); nus = [b for b in F["boites"] if b["N"] == x["N"]][0]["niveaux_2d"]
        rec = {"barreaux": m, "N": x["N"], "y_croise": yc, "u": c["u"], "theta": c["theta"], "ln_V2T_sur_G": math.log(c["V"] ** 2 * x["T"] / G), "nus": [(v[0], v[2]) for v in nus], "voisins_nus_en_delta": [v / ad for v in x["boite_nue"]["voisins"]]}
        out["croisements"].append(rec)
        print("   %d barreaux, cote %2d : y croise %7.3f (ln V^2T/G %+.2f)  u = %+8.3f  voisins nus du vide a %+.2f et %+.2f |delta|  ; niveaux nus : %s" % (
            m, x["N"], yc, rec["ln_V2T_sur_G"], c["u"], rec["voisins_nus_en_delta"][0], rec["voisins_nus_en_delta"][1], "  ".join("%.2f : %.3g" % (v[0], v[2]) for v in nus)))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
