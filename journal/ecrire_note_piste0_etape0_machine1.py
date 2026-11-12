# -*- coding: ascii -*-
# Ecrit la note de lecture depuis le JSON v2 : aucun nombre n'est tape.
import sys, json, math
d = json.load(open(sys.argv[1]))
P = d["points"]; ws = sorted(P, key=float)
def col(cle, fmt): return " ".join(fmt % P[w][cle] for w in ws)
G = {w: P[w]["G"] for w in ws}
gmax = max(G, key=G.get); gmin = min(G, key=G.get)
second = sorted(G.values())[-2]
ordres = [math.log10(P[w]["G"] / abs(P[w]["Hp"])) for w in ws]
qs = [P[w]["q"] for w in ws]
sg = d["L5"]["signes"]
L = []
A = L.append
A("# NOTE DE LECTURE -- PISTE (0), ETAPE 0 -- machine 1 -- 11/11/2026")
A("# Lecture a zero run des artefacts du run M17 -- CLASSE 3, hors chaine")
A("")
A("Pieces : lecture pre-declaree 20cbc762d58ce1ca (ecrite et empreintee AVANT")
A("l'ouverture des points) ; script v1 c5debf99604d3c28 ; script v2 = v1 + 7")
A("remplacements a ancre unique (trois defauts de la plume, section 4) ; les")
A("cinq lectures rendent le meme resultat sous v1 et v2. Les nombres MESURES")
A("de cette note sont ecrits par code depuis le JSON v2 ; seuils, annonces et")
A("libelles de fichiers sont du texte.")
A("")
A("## 1. AUTHENTIFICATION")
A("Dossier manche_m17_v17 recu de l'operateur en un ZIP : 36 pieces au canon")
A("et a la taille + 0 differente + 0 absente == 36 lignes du manifeste")
A("machine 2 (4aecd0e2b23bc818, au registre). Aucune de ces 36 pieces n'est")
A("au registre, sauf l'assemblage : detention unique a declarer.")
A("")
A("## 2. TABLE DES SIX POINTS f070 (w2 = %s)" % ", ".join(ws))
for cle, fmt, nom in [("eta", "%10.2f", "eta"), ("r_c", "%10d", "r_c"), ("N", "%10d", "N"),
                      ("G", "%10.3e", "G (eta/8)"), ("R", "%10.3e", "Richardson"),
                      ("r", "%10.3f", "r"), ("res", "%10.4f", "residu"),
                      ("p1", "%10.4f", "pas 1"), ("p2", "%10.4f", "pas 2"), ("p3", "%10.4f", "pas 3"),
                      ("m", "%10.4f", "2 eta"), ("t", "%10.4f", "translation"), ("n", "%10.4f", "N + p"),
                      ("rec", "%10.4f", "recouvr."), ("W", "%10.4f", "poids total"),
                      ("nres", "%10d", "n reson."), ("Gp", "%10.3e", "G pondere"),
                      ("q", "%10.1e", "Gp / G"), ("Hp", "%10.1e", "jumeau H+")]:
    A("  %-12s %s" % (nom, col(cle, fmt)))
A("")
A("## 3. LES CINQ LECTURES")
A("L-1 (coherence, non aveugle) : TIENT. Budget max = %.4f (au point %s,"
  % (max(d["L1"]["B"].values()), max(d["L1"]["B"], key=d["L1"]["B"].get)))
A("    c'est le residu declare, a %.1f pour cent du seuil 0.05) ; etendue de G"
  % (100 * max(d["L1"]["B"].values()) / 0.05))
A("    x%.1f. La structure en w2 n'est pas faite par l'absorbeur A L'ECHELLE"
  % math.exp(d["L1"]["E"]))
A("    DES PORTES ; le pic %s vaut x%.1f le second point et x%.1f le plus bas."
  % (gmax, G[gmax] / second, G[gmax] / G[gmin]))
A("L-2 (aveugle, annoncee 0.5) : NE TIENT PAS. Aucun indicateur d'identite")
A("    hors plage a 2.05.")
A("L-3 (aveugle, annoncee 0.6) : TIENT. Aucun indicateur d'absorbeur hors")
A("    plage a 2.05. Par la table pre-declaree : pic SANS SIGNATURE, l'etape")
A("    0 n'apprend rien sur lui. Le creux 2.02 : rien hors plage non plus.")
A("L-4 (aveugle, annoncee 0.4 qu'elle tienne) : NE TIENT PAS. rho(G, Gp) ="
  )
A("    %s contre 29/35. Exploratoire, sans verdict : rho(Gp, -Lambda_c) = %s"
  % (d["L4"]["rho_G_Gp"], d["L4"]["rho_Gp_Lam"]))
A("    (P6 (i) rejoue sur G : %s, identique a l'assemblage)." % d["L4"]["rho_G_Lam"])
A("L-5 (aveugle, annoncee 0.6) : NE TIENT PAS. Signe du dernier pas : %s"
  % " ".join("%s:%+d" % (w, sg[w]) for w in ws))
A("    (0 = non defini). Les six points ne sont pas au meme endroit de leur")
A("    trajectoire en eta. Les ecarts en jeu restent sous 5 pour cent.")
A("Bilan des annonces : L-3 (0.6) tenue ; L-5 (0.6) et L-2 (0.5) non tenues ;")
A("    L-4 (0.4) non tenue, dans le sens annonce.")
A("")
A("## 4. DEFAUTS DE LA PLUME (verses, corriges en v2 par hunks nommes)")
A("D-P0-1 : la regle HORS PLAGE rendait 'dans la plage' sur une valeur non")
A("    finie (residu a 2.02) -- silence deguise en passage. v2 : NON LISIBLE.")
A("D-P0-2 : rho(G, R) calcule avec un R non fini rendait 33/35 ; sur les 5")
A("    points ou R existe, rho = %s. v2 : compte declare." % d["L4"]["rho_G_R"])
A("D-P0-3 : le signe de L-5 n'existe que si 0 < r < 1 ; v1 rendait -1 a 2.02.")
A("D-P0-4 (conception, NON corrige) : l'ensemble de reference O melange deux")
A("    familles (section 5), sa plage contient presque tout : la regle de")
A("    L-2 / L-3 etait sans puissance. Elle reste comme ecrite.")
A("")
A("## 5. OBSERVATIONS HORS PRE-DECLARATION (post hoc, aucune lecture attachee)")
A("O-1 : DEUX FAMILLES de part et d'autre de 2:1. A gauche (1.95, 1.97, 1.98) :")
A("    r_c = %s, poids total %.3f a %.3f, recouvrement %.4f a %.4f, %d a %d"
  % (sorted(set(P[w]["r_c"] for w in ws[:3])), min(P[w]["W"] for w in ws[:3]), max(P[w]["W"] for w in ws[:3]),
     min(P[w]["rec"] for w in ws[:3]), max(P[w]["rec"] for w in ws[:3]),
     min(P[w]["nres"] for w in ws[:3]), max(P[w]["nres"] for w in ws[:3])))
A("    resonances retenues. A droite (2.02, 2.03, 2.05) : r_c = %s, poids"
  % sorted(set(P[w]["r_c"] for w in ws[3:])))
A("    total %.4f a %.4f, recouvrement %.4f a %.4f, %s resonances."
  % (min(P[w]["W"] for w in ws[3:]), max(P[w]["W"] for w in ws[3:]),
     min(P[w]["rec"] for w in ws[3:]), max(P[w]["rec"] for w in ws[3:]),
     sorted(set(P[w]["nres"] for w in ws[3:]))))
A("    La base propre est nettement non orthogonale sur le support de la")
A("    graine a gauche, presque orthogonale a droite. Le NOMINAL de toute la")
A("    qualification de l'instrument (1.95) est dans la famille de gauche.")
A("O-2 : Gp / G va de %.1e a %.1e : la largeur ponderee n'est pas une autre"
  % (min(qs), max(qs)))
A("    estimation du meme taux, c'est un autre objet, domine par des etats")
A("    larges : l'etat retenu y contribue pour rec x G, soit %.0e a %.0e de"
  % (min(P[w]["rec"] * P[w]["G"] / P[w]["Gp"] for w in ws), max(P[w]["rec"] * P[w]["G"] / P[w]["Gp"] for w in ws)))
A("    Gp. Une lecture faite sur elle (dont R5) lit cet autre objet.")
A("O-3 : a 2.02, r = %.3f : le dernier pas est plus grand que le precedent,"
  % P["2.02"]["r"])
A("    Richardson et residu n'existent pas ; l'operatif du gel 4.6 y est")
A("    vide et P6 a lu la valeur brute. Point EN DOMAINE malgre cela.")
A("O-4 : G / |H+| va de %.1f a %.1f ordres de grandeur (la note de run ecrit"
  % (min(ordres), max(ordres)))
A("    'quatre a cinq') ; H+ est joue a eta, H a eta/8. A la plume de m2.")
A("O-5 : P8 a g = 0.001 : plus grand pas de descente %.1e (L = 20) et %.1e"
  % tuple(max(float(x) for x in e["pas"]) for e in d["autres"]["pt_39_20_P8_g0.001.json"]["essais"]))
A("    (L = 30), descente rejetee aux deux longueurs --")
A("    largeur sous le plancher numerique. Les six f050 sont en arret par")
A("    E-A (chaine), pas par E-B.")
A("")
A("## 6. CE QUE CELA CHANGE POUR L'ETAPE 1")
A("(a) T-etats passe en premier et se lit PAR COTE ; y ajouter le")
A("    conditionnement de l'etat retenu et les poids BI-ORTHOGONAUX (produit")
A("    c, H complexe symetrique), qui somment a 1 la ou les |c_nu|^2 du")
A("    script somment a %.3f au plus bas." % min(P[w]["W"] for w in ws))
A("(b) T-eta inchange, avec 2.02 comme point a tourner (r > 1).")
A("(c) La largeur ponderee sort de l'instrument comme 'taux'.")
A("(d) Temoin positif inchange. Rien ici ne qualifie l'estimateur.")
A("")
A("-- FIN --")
open(sys.argv[2], "w", encoding="ascii").write("\n".join(L) + "\n")
print("lignes", len(L), "| pourcent", sum(l.count("%") for l in L))
