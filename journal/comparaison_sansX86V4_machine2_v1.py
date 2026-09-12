#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""SON RUN SANS LE NOYAU X86_V4, CONTRE MON REJEU BOCAL4 -- machine 2, v1, 12/09/2026.

Elle annonce 44/44 grandeurs de flot identiques au bit. Cette feuille le refait : une
annonce ne vaut que rejouee. Elle compare aussi, pour memoire, son run NOYAU ACTIF, afin
que le contraste soit dans la meme sortie et non dans une prose.

L'issue qui ferait mordre est ecrite : si une seule des 44 differait, son 44/44 tombe et
sa cause perd sa preuve la plus directe.

Les trois chemins de JSON sont des ARGUMENTS.
"""
import json, sys

if len(sys.argv) < 4:
    sys.exit("usage : comparaison_sansX86V4_machine2_v1.py "
             "<json m1 sans X86_V4> <json m1 noyau actif> <json m2 rejeu1>")
sans = json.load(open(sys.argv[1], encoding="utf-8"))
avec = json.load(open(sys.argv[2], encoding="utf-8"))
moi = json.load(open(sys.argv[3], encoding="utf-8"))

G = ("e", "R_composantes", "plancher_composantes", "ratio_seuil_du_flot", "tau_au_max",
     "err_rel_fin", "e_sur_plancher", "seuil_5_4_du_flot", "dt", "tau_fin", "n_pas")

print("=" * 88)
print("SON RUN SANS X86_V4 CONTRE MON REJEU -- l'annonce est 44/44")
print("=" * 88)
print("      son poste : python %s ; numpy %s ; %s"
      % (sans["plateforme"]["python"], sans["plateforme"]["numpy"],
         sans["plateforme"]["platform"]))
print("      le mien   : python %s ; numpy %s ; %s"
      % (moi["plateforme"]["python"], moi["plateforme"]["numpy"],
         moi["plateforme"]["platform"]))

n = bit = 0
print("\n[1] LES 44 GRANDEURS DE FLOT (11 par pas)")
for k in range(4):
    mauvaises = []
    for q in G:
        a, b = sans["flots"][k][q], moi["flots"][k][q]
        n += 1
        if a == b:
            bit += 1
        else:
            mauvaises.append("%s (%r / %r)" % (q, a, b))
    print("      dt2/%-4d %s" % (2 ** k, "les 11 AU BIT" if not mauvaises
                                 else " | ".join(mauvaises)))
print("      => %d / %d au bit  -- son annonce : 44/44" % (bit, n))

print("\n[2] LE CONTRASTE, DANS LA MEME SORTIE : SON RUN NOYAU ACTIF CONTRE LE MIEN")
for k in range(4):
    a, b = avec["flots"][k]["e"], moi["flots"][k]["e"]
    print("      dt2/%-4d e : %s" % (2 ** k, "AU BIT" if a == b
                                     else "differe %.2e" % abs(b / a - 1)))

print("\n[3] e/seuil A LA PAIRE DU GEL -- LA GRANDEUR DU GESTE")
for nom, j in (("son noyau ACTIF", avec), ("son noyau DESACTIVE", sans),
               ("moi (BOCAL4)", moi)):
    print("      %-22s %.16f" % (nom,
                                 j["paires"][0]["lecture_5_4_sur_flot_fin"]["ratio_seuil"]))

print("\n[4] CE QUI DIFFERE ENCORE, SANS LE NOYAU -- ET QU'ELLE A NOMME ELLE-MEME")
for i in range(3):
    a, b = sans["paires"][i]["p_obs"], moi["paires"][i]["p_obs"]
    if a != b:
        print("      paire %d : p_obs %r contre %r" % (i, a, b))
        print("                 -- sur des e IDENTIQUES : un ulp de log2, glibc contre")
        print("                    UCRT (sa section 4.6). Grandeur de LECTURE.")
print("=" * 88)
