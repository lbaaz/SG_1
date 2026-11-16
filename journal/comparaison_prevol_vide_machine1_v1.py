# -*- coding: ascii -*-
"""LECTURE DU PRE-VOL DU GEL "LARGEUR DU VIDE" -- machine 1, v1, 2026-11-16. Aucune mesure : elle lit le dossier du pre-vol.
P1 l'instrument du lecteur, joue par le pilote avec les pieces deposees, TIENT ;
P2 a la cellule PV8, le jumeau lu par sonde_vide rend les largeurs de la piece de faisabilite de la premiere partie (meme
   w2, meme couplage, meme geometrie, absorbeurs A et B, barreaux -3, 3, 8) ;
P3 aux deux cellules, les 48 lectures du jumeau sont suivies, le fantome n'est PAS lu, les fichiers sont marques pre-vol ;
P4 la feuille, en pre-vol, ne juge rien ;
P5 les durees.
Usage : python3 -I -B comparaison_prevol_vide_machine1_v1.py <dossier du pre-vol> <faisabilite_profondeur_jumeau_v1.json> <sortie.json>"""
import sys, os, re, json
RUN, FAIS, SORTIE = sys.argv[1:4]
J = lambda nom: json.load(open(os.path.join(RUN, nom)))
out = {}; tenus = []
inst = J("verdict_ter_instrument.json"); out["P1"] = {"instrument": inst["instrument"], "motifs": inst["motifs"]}
ok = inst["instrument"] == "TIENT"; tenus.append(ok)
print("P1 instrument du lecteur (pieces deposees, par le pilote) : %s %s" % (inst["instrument"], inst["motifs"]))
S8 = J("sonde_vide_PV8.json"); F8 = [c for c in json.load(open(FAIS))["cas"] if c["m_bord_du_vide"] == 8][0]
meme = ("%.5e" % F8["g"]) == S8["cellule"]["g"] and F8["w2"] == S8["cellule"]["w2"] and F8["r_c"] == S8["cellule"]["r_c"]
pire = 0.0; n = 0
for a in ("A", "B"):
    for k, g_ref in zip((-3, 3, 8), F8["absorbeurs"][a]["gamma"]):
        g = S8["jumeau"]["traj"][a][str(k)]["gamma"]; pire = max(pire, abs(g / g_ref - 1.0)); n += 1
ok = meme and n == 6 and pire <= 1e-6; tenus.append(ok); out["P2"] = {"meme_cellule": meme, "lectures": n, "pire_ecart_relatif": pire}
print("P2 PV8, jumeau : meme w2, couplage et r_c que la piece de faisabilite : %s ; %d lectures comparees, pire ecart relatif %.1e (tolerance 1e-6) : %s" % (
    "oui" if meme else "non", n, pire, "TIENT" if ok else "NE TIENT PAS"))
out["P3"] = {}; ok3 = True
for i in ("PV3", "PV8"):
    S = J("sonde_vide_%s.json" % i); tr = S["jumeau"]["traj"]; lect = [tr[a][str(k)] for a in "ABCD" for k in range(-3, 9)]
    r = {"suivies": sum(1 for x in lect if x["suivi"]), "lectures": len(lect), "plus_grande_largeur": max(x["gamma"] for x in lect), "plus_petite_largeur": min(x["gamma"] for x in lect),
         "fantome_lu": S["fantome"] is not None, "prevol": S["prevol"], "duree_s": S["duree_s"], "boites": sorted(v["N"] for v in S["jumeau"]["absorbeurs"].values())}
    out["P3"][i] = r; ok3 = ok3 and r["suivies"] == r["lectures"] == 48 and not r["fantome_lu"] and r["prevol"] is True
    print("P3 %s : %d lectures du jumeau suivies sur %d ; largeurs de %.1e a %.1e ; boites %s ; fantome lu : %s ; marque pre-vol : %s ; %.0f s" % (
        i, r["suivies"], r["lectures"], r["plus_petite_largeur"], r["plus_grande_largeur"], r["boites"], "OUI" if r["fantome_lu"] else "non", "oui" if r["prevol"] else "NON", r["duree_s"]))
tenus.append(ok3)
V = J("verdict_vide.json"); ok = V["verdict"] == "PRE-VOL, RIEN N'EST JUGE" and "V1" not in V and V["prevol"] is True; tenus.append(ok)
out["P4"] = {"verdict": V["verdict"]}; print("P4 feuille en pre-vol : %s ; aucune issue rendue : %s" % (V["verdict"], "oui" if "V1" not in V else "NON"))
journal = open(os.path.join(RUN, "pilote_gel_vide.log")).read()
durees = {m.group(1).strip(): float(m.group(2)) for m in re.finditer(r"  (\S.*?\S)\s+code=0 duree=(\d+) s", journal)}
total = float(re.search(r"FIN DU PILOTE ; duree totale (\d+) s", journal).group(1)); out["P5"] = {"durees_s": durees, "total_s": total}
print("P5 durees sur machine 1 (deux processus, un fil chacun) : %s ; total %.0f s" % (" ; ".join("%s %.0f s" % kv for kv in durees.items()), total))
out["tient"] = all(tenus)
print("PRE-VOL : %d controles tenus sur %d" % (sum(tenus), len(tenus)))
json.dump(out, open(SORTIE, "w"), indent=1, sort_keys=True)
