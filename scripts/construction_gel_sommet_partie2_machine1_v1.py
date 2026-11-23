# -*- coding: ascii -*-
"""CONSTRUCTION DE LA SECONDE PARTIE DU GEL "SOMMET" (instrument, enonce, tolerances) -- machine 1, v1, 2026-11-22.
Aucun calcul : assemble le texte de la piece et y porte les nombres lus dans la table gelee et dans les journaux du lot.
Les lignes font 100 colonnes au plus, en ASCII, sans signe pour cent.
Usage : python3 -I -B construction_gel_sommet_partie2_machine1_v1.py <dossier du lot> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
LOT, SORTIE = sys.argv[1:3]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
ch = lambda nom: os.path.join(LOT, nom)
T = json.load(open(ch("table_cellules_gel_sommet_v1.json"))); C = T["cellules"]; TP = T["temoins_positifs"]; R = T["regle"]
assert canon_B(ch("table_cellules_gel_sommet_v1.json")) == "4238e2b262119f83" and len(C) == 56 and len(TP) == 9 and T["graine"] == "114565"
banc_f = open(ch("banc_feuille_gel_sommet_machine1_v1.log")).read(); banc_p = open(ch("banc_pilote_gel_sommet_machine1_v1.log")).read()
mf = re.search(r"BANC DE LA FEUILLE : (\d+) cas, (\d+) tenus", banc_f); mp = re.search(r"BANC DU PILOTE : (\d+) cas, (\d+) tenus", banc_p)
garde = open(ch("garde_sur_les_sorties_de_Q_et_Q2_machine1_v1.log")).read(); mg = re.search(r"TEMOINS POSITIFS : TIENNENT \((\d+) sur (\d+)\)", garde)
assert mf and mp and mg and mf.group(1) == mf.group(2) and mp.group(1) == mp.group(2) and "L'INSTRUMENT NE TIENT PAS" in garde
W = 100
def par(texte, indent="  ", suite=None):
    t = re.sub(r" ([:;?!])(?= |$)", lambda m: chr(1) + m.group(1), " ".join(texte.split()))
    return textwrap.fill(t, width=W, initial_indent=indent, subsequent_indent=indent if suite is None else suite, break_long_words=False, break_on_hyphens=False).replace(chr(1), " ")
out = []
def P_(texte, indent="  ", suite=None): out.append(par(texte, indent, suite))
def L_(ligne): out.append(ligne)
def I_(texte): out.append(par(texte, "  ", "      "))          # article numerote
def B_(texte): out.append(par(texte, "  ", "    "))            # puce
kappas = sorted(set(c["kappa"] for c in C), key=float); w2s = []
for c in C:
    if c["w2"] not in w2s: w2s.append(c["w2"])
G = [math.exp(c["ln_G3"]) for c in C]; et_max = max(c["etendue"] for c in C)
d31 = max(abs(c["ln_G3"] - c["ln_G1"]) for c in C); d32 = max(abs(c["ln_G3"] - c["ln_G2"]) for c in C)
haut = [c["id"] for c in C if math.exp(c["ln_G3"]) > 1.08861e-04]; bas = [c["id"] for c in C if math.exp(c["ln_G3"]) < 2.05518e-09]
ph = {(F(c["w2"]), c["kappa"]): c for c in C}
miroirs = [(k, ph[(w, k)]["id"], ph[(4 - w, k)]["id"], ph[(w, k)]["ln_Phi"] - ph[(4 - w, k)]["ln_Phi"]) for (w, k) in sorted(ph, key=lambda z: float(z[1])) if w < 2 and (4 - w, k) in ph]
assert len(miroirs) == 7 and set(m[1][:3] for m in miroirs) == {"MPa"} and set(m[2][:3] for m in miroirs) == {"PPb"}
etal = {k: max(c["ln_Phi"] for c in C if c["kappa"] == k) - min(c["ln_Phi"] for c in C if c["kappa"] == k) for k in kappas}
dec = lambda w: "%.5f" % float(F(w))

L_("GEL \"SOMMET\" -- SECONDE PARTIE : L'INSTRUMENT, L'ENONCE, LES TOLERANCES")
L_("PRE-ENREGISTREMENT v1 -- machine 1, 2026-11-22.")
L_("A CERTIFIER PAR MACHINE 2 AVANT TOUTE LECTURE 2D A L'UNE DES CELLULES.")
L_("")
L_("0. STATUT")
P_("""Cette piece complete la premiere partie (1e5039cade55d13f, lot 3ba4618d7976c6ea), que machine 2 a certifiee telle
quelle, sans refus (lot 21e9bddfe5db83b2) : sa table des 560 cellules candidates, ecrite du texte, est celle de machine 1,
et la table commune est ce meme fichier (77ce2a6c7e867011). Cette piece fixe les cellules tirees, l'instrument du run,
l'enonce juge, ses tolerances, ce que chaque issue engage, et les annonces de la plume. Rien n'est joue.""")
P_("""Graine. L'operateur a ecrit a machine 1 "graine 114565" (22/11/2026, 23 h 21), apres lui avoir remis la
certification de machine 2 (22 h 55) et apres que machine 1 l'a authentifiee et a recoupe la table commune par son code.
Machine 1 n'avait calcule aucun tirage sur une graine faite de chiffres avant de la recevoir ; elle avait rappele a
l'operateur que la graine lui revenait ; elle n'en a propose ni commente aucune. Elle ne sait pas si machine 2 l'a recue :
machine 2 le dit a la certification.""")
P_("""Tirage. Par le script de machine 1 (816ac4d298e82f16), sur la table commune : chaque creneau rend ses deux w2 aux
rangs 0 et 1, aucun rang n'est saute ; huit w2, cinquante-six cellules. Machine 2 dit son tirage a la certification ; si
ses cellules ou leurs trois nombres ecrits different, PAS DE GEL (premiere partie, section 6).""")
P_("""E19. Aucune des deux machines ne fait de calcul 2D, du systeme a fantome ou du jumeau, a l'un des huit w2 tires,
avant la certification croisee de cette piece et le feu vert ecrit de l'operateur. Tout ce que cette piece calcule aux
cellules est une chaine a une dimension, faite avant la graine. Machine 1 n'a fait AUCUN calcul 2D pour cette piece : sa
feuille a ete essayee sur des dossiers synthetiques et sur les sorties que machine 2 a deja produites aux neuf points
sacrifies, lues comme des donnees ; son pilote n'a joue que des scripts factices (sections 4.3 a 4.5).""")
L_("")
L_("1. QUESTION ET PERIMETRE")
P_("""Le gel "largeur du vide" (delta 102) a montre que la chaine a une dimension rend la largeur de l'etat que porte le
site (0, 0) aux ailes, a trois barreaux de barriere et plus. Ce gel demande si elle la rend encore au SOMMET, de deux
barreaux jusqu'a la fenetre sans barriere, la ou le saut au pied de l'echelle vaut jusqu'au desaccord lui-meme, a des
cellules que personne n'a choisies.""")
P_("""Perimetre : huit w2 (%s) et sept kappa (%s). L'objet juge est la chaine d'ordre 3 des blocs deposes sous
l'absorbeur adapte (bloc 49a40d9098b55361), telle quelle : son plateau G3* sur dix-huit variantes, calcule avant la
graine. La reference est la largeur de plateau sous l'absorbeur A, lue par le lecteur creux du depot avec le eta0 et le
r_c ecrits de la cellule.""" % (", ".join(dec(w) for w in w2s), ", ".join(kappas)))
P_("""Ce que le gel SEPARE et ne separe pas. Aux cinquante-six cellules l'ordre 3 differe du premier ordre de %.5f au plus
en logarithme, et de l'ordre 2 de %.5f au plus : sous une tolerance de 0.01, l'enonce n'oppose pas les ordres. Il eprouve
ceci : "le mecanisme de l'echelle et la chaine rendent la largeur du vide a 0.01 pres, de kappa = 0.0363 a kappa = 1". La
loi d'echelle et le signe de delta ne sont pas juges : ils sont consignes (section 6).""" % (d31, d32))
L_("")
L_("2. SOURCES (convention B)")
for canon, quoi in (("82a0be882568fe0c", "scripts/m17_chaine_v17.py (registre 055be58), le moteur"),
                    ("d5cc48f48e37af99", "scripts/sonde_lecteur_gel_loi_machine1_v1.py (registre) : la sonde du lecteur, jouee telle quelle a l'etage A, et dont le bloc LECTEUR CREUX est execute par le pilote de lecture"),
                    ("83701094e6a2b965", "scripts/lecture_lecteur_gel_loi_machine1_v1.py (registre) : la feuille du lecteur, jouee telle quelle a l'etage A, et dont juger_etat est appele par la feuille de ce gel"),
                    ("10887c60d5f55bcf", "journal/sonde_ordre2.json (registre), le depot du delta 98 : les ancres"),
                    ("69b3bab3bb8480b7", "journal/tp_retenus_machine2_v1.json (registre) : couplages du temoin positif du depot"),
                    ("4d51dd58ef456fe9", "journal/tp_reference_machine2_v1.json (registre) : sa reference"),
                    ("6600fb8418c79930", "journal/reference_ancres_ter_machine1_v1.json (registre) : reference des ancres"),
                    ("35fa7b73f2b7f8eb", "journal/table_points_gel_loi_ordre3_v1.json (registre) : la table que la sonde deposee exige a l'etage A"),
                    ("a38b1550f8f5e3cf", "scripts/pilote_gel_vide_machine1_v1.py (registre) : le pilote dont celui de ce lot derive"),
                    ("ac39a24def6c7420", "scripts/feuille_vide_machine1_v1.py (registre) : la feuille dont celle de ce lot derive"),
                    ("eebd979f18d8db48", "gels/gel_largeur_vide_partie2_instrument_enonces_pre_enregistrement_v1.md (registre) : la piece dont celle-ci reprend la forme"),
                    ("1e5039cade55d13f", "gel_sommet_partie1_regle_tirage_pre_enregistrement_v1.md (lot 3ba4618d7976c6ea) : la premiere partie"),
                    ("816ac4d298e82f16", "tirage_sommet_machine1_v1.py (meme lot) : le tirage"),
                    ("882f55d07d03dfff", "eligibilite_sommet_v1.json (meme lot) : la table complete de machine 1, d'ou viennent les predictions"),
                    ("77ce2a6c7e867011", "la table commune (lots 3ba4618d7976c6ea et 21e9bddfe5db83b2)"),
                    ("47a84eae6052f006", "lecteur_2D_pilote_machine2_v1.py (lots c58c2b3f533c516b et 295b2b1549b076c2 de machine 2) : le pilote de lecture qui a lu Q et Q2 ; ECRIT PAR MACHINE 2, joue ici tel quel")):
    out.append(par(canon + " " + quoi, "    ", "                     "))
P_("""Les lots de machine 1 et de machine 2 du 22/11 ne sont pas au registre (055be58) : les deux machines les
detiennent. Le pilote de lecture de machine 2 n'est pas dans ce lot : machine 1 ne l'a jamais execute, elle l'a lu.""")
L_("")
L_("3. LES CELLULES")
P_("""Table gelee : table_cellules_gel_sommet_v1.json, canon 4238e2b262119f83. Elle porte la graine, le journal du tirage,
les 56 cellules, leurs trois nombres ecrits, leurs predictions et leur tolerance, et les neuf temoins positifs avec leur
plateau de reference. La feuille et le pilote portent son canon en dur. Par cellule : w2, delta = w2 - 2, kappa,
profondeur m de la barriere, couplage ecrit g, echelle ecrite eta0, rayon r_c, plateau predit G3* et etendue de la chaine
sous ses dix-huit variantes. La tolerance est T = 0.01 a toutes ; la plus grande boite du lecteur est r_c + 100.""")
L_("    cellule  w2              delta      kappa   m  g            eta0         r_c  G3*        etendue")
for c in C:
    L_("    %-7s  %-14s  %+.5f  %s  %d  %s  %s  %-3d  %.3e  %.4f" % (c["id"], c["w2"], c["delta"], c["kappa"], c["m"], c["g"], c["eta0"], c["r_c"], math.exp(c["ln_G3"]), c["etendue"]))
P_("""Aux 56 cellules la barriere du moteur finit a la profondeur cible, et G3* et l'etendue sont ceux de la table de
machine 1 calculee avant la graine, que machine 2 a retrouves par sa methode (ecart de 2.3e-11 au plus sur le logarithme
du plateau, lot 21e9bddfe5db83b2). Couplages de %s a %s ; plateaux predits de %.3e a %.3e ; etendue de %.4f a %.4f.""" % (
    min((c["g"] for c in C), key=float), max((c["g"] for c in C), key=float), min(G), max(G), min(c["etendue"] for c in C), et_max))
P_("""Le tirage a sorti une paire de w2 MIROIRS, 1.99989 et 2.00011 (meme |delta|, signes opposes) : sept paires de
cellules a kappa egal y lisent le signe de delta seul. C'est le hasard de la graine ; rien n'en est juge.""")
P_("""Les neuf TEMOINS POSITIFS DU SOMMET : les points sacrifies de Q et de Q2, a w2 = 2, 20001/10000 et 19999/10000,
qui ne sont pas candidats. Leur reference est le plateau que le lecteur y a rendu, relu par juger_etat de la feuille
deposee dans les sorties de machine 2 :""")
L_("    temoin  w2           m  g        eta0         r_c  plateau de reference")
for t in TP:
    L_("    %-6s  %-11s  %d  %-7s  %s  %-3d  %.5e" % (t["id"], t["w2"], t["m"], t["g"], t["eta0"], t["r_c"], math.exp(t["ln_Gamma_pl_reference"])))
L_("")
L_("4. L'INSTRUMENT : UN RUN, QUATRE ETAGES ET UNE GARDE")
L_("  4.1 Les pieces (convention B)")
for nom, quoi in (("table_cellules_gel_sommet_v1.json", "la table gelee ; ecrite par predictions_sommet_machine1_v1.py (%s)" % canon_B(ch("predictions_sommet_machine1_v1.py"))),
                  ("pilote_gel_sommet_machine1_v1.py", "NOUVEAU ; il enchaine et tient le journal ; derive du pilote depose du gel \"largeur du vide\""),
                  ("feuille_gel_sommet_machine1_v1.py", "NOUVELLE ; elle appelle juger_etat de la feuille deposee, garde et juge ; derivee de la feuille deposee du gel \"largeur du vide\""),
                  ("jobs_gel_sommet_v1.txt", "les 112 lectures des cellules, au format du pilote de lecture de machine 2"),
                  ("jobs_temoins_sommet_v1.txt", "les 18 lectures des temoins positifs, meme format")):
    out.append(par(canon_B(ch(nom)) + " " + nom + " : " + quoi, "    ", "                     "))
out.append(par("47a84eae6052f006 lecteur_2D_pilote_machine2_v1.py : le pilote de lecture, de machine 2, hors de ce lot (section 2)", "    ", "                     "))
P_("""Aucune piece deposee n'est editee : la sonde et la feuille du lecteur sont jouees telles quelles a l'etage A, et
leurs routines sont executees depuis leurs fichiers, au canon controle, aux autres etages. Les deux fichiers de travail ne
commandent rien : le pilote tire ses appels de la table ; le banc verifie qu'ils sont ces lignes (4.5).""", "    ")
L_("  4.2 Le deroulement du run (le pilote)")
for t in ("""Etage A. L'instrument du lecteur, tel qu'aux gels "ordre 3" et "largeur du vide" : la sonde deposee en modes etage0,
ancres et etage1 (les deux ancres du depot, le temoin positif, le temoin negatif des ancres), puis la feuille deposee,
etape "instrument". Si elle ne rend pas TIENT, le run s'arrete : rien d'autre n'est lu.""",
          """Etage A'. Les neuf temoins positifs du sommet, par le pilote de lecture de machine 2 : le jumeau sans fantome (signe
+1) puis le fantome (signe -1), au site (0, 0), depuis l'energie 0, sous les quatre absorbeurs du depot (A : F2, 80
couches ; B : F2, 100 ; C : F1, 100 ; D : F2, bord r_c + 10, 80), a douze barreaux (k = -3 a 8, eta_k = eta0 2^(-k)),
avec le eta0 et le r_c de la table.""",
          """Garde. La feuille de ce gel, etape --temoins : instrument et temoins positifs (section 5). Si elle ne rend pas
TIENT, le run s'arrete : AUCUNE cellule n'est lue. Elle refuse un dossier ou une cellule a deja un fichier.""",
          """Etage B. Les 56 cellules, par le meme pilote de lecture, de la meme facon : 112 lectures.""",
          """Etage C. La feuille de ce gel : sections 5 et 6."""):
    out.append(par(t, "    ", "    "))
L_("  4.3 Le banc de la feuille")
P_("""Le banc fabrique des dossiers de run SYNTHETIQUES pour la table gelee (des plateaux poses a la main autour de la
prediction : ils ne disent rien des cellules), change une chose a la fois, avec l'effet attendu ecrit avant : %s cas, %s
tenus au premier passage. Ils couvrent : une cellule qui tombe, d'un cote et de l'autre ; deux ; la cellule non jugeable ;
trop de non jugeables ; un w2 sans quatre cellules tenues ; le desaccord d'un absorbeur ; l'absence de plateau ; un
absorbeur sans cinq barreaux lisibles ; une lecture non suivie sans consequence ; le jumeau trop large ; le jumeau non
suivi ; l'instrument qui ne tient pas ou qui manque ; un temoin positif hors de sa reference, non qualifie, ou juste sous
le seuil ; le fichier absent ; le canon du pilote de lecture ; le couplage ; eta0 ; la geometrie ; une autre table ; la
bande qui depasse la tolerance ; la portee qui perd un kappa ; l'etape de garde dans ses quatre issues.""" % (mf.group(1), mf.group(2)), "    ")
L_("  4.4 La feuille sur des sorties reelles, sans aucune mesure nouvelle")
P_("""L'etape de garde a ete jouee sur les dix-huit fichiers que machine 2 a produits a Q et a Q2, lus comme des donnees :
les %s temoins positifs y sont QUALIFIES, leur jumeau tient, et ils rendent leur reference a 0 pres (ce sont les memes
fichiers : cela eprouve la lecture de la feuille, pas le lecteur). L'instrument de l'etage A y manque, et la garde rend
"L'INSTRUMENT NE TIENT PAS", comme elle le doit.""" % mg.group(1), "    ")
L_("  4.5 Le banc du pilote")
P_("""Le pilote n'a JAMAIS joue une lecture reelle chez machine 1 : les calculs 2D sont chez machine 2. Son banc le joue
sur des scripts FACTICES qui notent leurs arguments ; le pilote eprouve est une copie dont seules les lignes des canons en
dur sont remplacees. %s cas, %s tenus : le run entier dans l'ordre des etages ; les 18 puis les 112 appels de lecture
egaux, argument pour argument, aux lignes des deux fichiers de travail ; l'arret si l'instrument ne tient pas ; l'arret si
la garde ne tient pas, sans une cellule lue ; le pre-vol ; le refus d'un dossier deja la ; l'arret sur un code de sortie
non nul ; l'arret du pilote non modifie devant une piece qui n'est pas au canon. Ce que ce banc ne dit pas : rien de ce
que font les vrais scripts.""" % (mp.group(1), mp.group(2)), "    ")
L_("  4.6 Le pre-vol, chez machine 2")
P_("""Avec --prevol le pilote joue l'etage A, l'etage A' et la garde, puis s'arrete : AUCUNE cellule n'est lue. Les neuf
points relus sont des points sacrifies, deja lus sur le mot de l'operateur. Ce sera la premiere execution reelle du
pilote. Machine 2 demande a l'operateur ce qu'elle estime devoir lui demander.""", "    ")
L_("")
L_("5. POINT LU, BANDE, JUGEMENT (ce que fait la feuille)")
P_("""LECTEUR. La feuille appelle juger_etat de la feuille deposee sur les quatre trajectoires du fantome. Il exige un
plateau sous CHACUN des quatre absorbeurs (cinq barreaux lisibles consecutifs, plus grande valeur <= 1.05 fois la plus
petite ; lisible = suivie, finie, strictement positive), et les plateaux sous B, C et D a 0.05 pres du plateau sous A, en
logarithme. Statut : QUALIFIE ; NON QUALIFIE si un absorbeur a une fenetre de cinq barreaux lisibles mais pas de plateau,
ou si un accord manque ; NON LISIBLE si, sans autre echec, un absorbeur n'a pas cinq barreaux lisibles consecutifs. Une lecture non suivie
hors de la fenetre retenue ne change rien. Gamma_pl est le plateau sous A.""")
P_("""ETALEMENT DU LECTEUR, s : le plus grand de ln(1 + etalement du plateau sous A) et des trois |ln(plateau X / plateau
A)|, X = B, C, D.""")
P_("""TEMOIN. Le jumeau sans fantome au meme point. Il TIENT si ses 48 lectures sont suivies et si sa plus grande largeur
vaut au plus 1e-6 Gamma_pl.""")
P_("""POINT LU : QUALIFIE et temoin tenu. Sinon NON LU, avec son motif. Une cellule dont B, C ou D n'a pas de plateau,
ou s'ecarte de A de plus de 0.05, est donc NON LUE : elle n'est pas "lue sans accord".""")
P_("""TEMOIN POSITIF. Un point sacrifie TIENT s'il est lu et si |ln(Gamma_pl / plateau de reference)| <= 0.001. Les
temoins positifs TIENNENT si les neuf tiennent.""")
P_("""JUGEMENT d'une cellule lue. ln q = ln(G3* / Gamma_pl). BANDE b = etendue de la chaine a la cellule (table) + s. La
cellule TIENT si |ln q| <= T - b ; elle TOMBE si |ln q| > T + b ; elle est NON JUGEABLE sinon. La tolerance pour tenir est
donc plus serree que T ; une cellule dont la bande atteint T ne peut pas tenir : elle tombe ou n'est pas jugeable.""")
L_("")
L_("6. L'ENONCE ET SES ISSUES (la cellule est l'unite)")
P_("""S1, cinquante-six cellules, huit w2, T = 0.01. TOMBE si deux cellules ou plus tombent ; sinon NON CONCLUANT si moins de
%d cellules sont jugees (tenues ou tombees), ou si un w2 a moins de %d cellules tenues sur sept ; sinon TENU SAUF UNE
CELLULE si une tombe ; sinon TENU. C'est l'enonce V1 du gel "largeur du vide", porte de seize cellules a cinquante-six
(trois quarts jugees) et de quatre creneaux a huit w2 (plus de la moitie tenues).""" % (R["s1_jugees_min"], R["s1_tenues_par_w2_min"]))
P_("""PORTEE. La feuille donne les kappa ou %d cellules au moins sur huit tiennent. Si S1 tient, l'acte n'ecrit sa
phrase que pour ces kappa.""" % R["portee_tenues_par_kappa_min"])
P_("""Ce qui est consigne sans etre juge, par cellule lue : le signe de ln q et celui de delta ; ln q pour l'ordre 2 et
pour le premier ordre ; ln(Gamma_pl / |delta|), et son etalement a kappa egal d'un w2 a l'autre (la loi d'echelle) ; aux
sept paires de cellules miroirs, ln[Phi(delta < 0) / Phi(delta > 0)] lu et celui de la chaine ; la largeur rapportee au
saut au pied de l'echelle ; les barreaux plats a 0.005 pres sous A. Aucun enonce ne porte sur le signe du residu, sur le
signe de delta ni sur la loi d'echelle.""")
L_("")
L_("7. LES TOLERANCES, ET CE QUE LA PLUME A VU AVANT DE LES ECRIRE")
I_("""7.1 T = 0.01. Elle vient de la demolition de l'esquisse par machine 2 (0.02 valait 250 fois le pire ecart lu), prise
par machine 1 avant Q2. Ce que la plume avait vu : aux neuf points sacrifies le lecteur est a 0.00034 au plus de G3* en
logarithme, son etalement s vaut 0.0018 au plus, et la chaine a une etendue de %.4f au plus aux 56 cellules. Si le
lecteur s'etale aux cellules comme a ces points, la bande est de %.4f au plus et une cellule tient jusqu'a |ln q| = %.4f :
%d fois le pire ecart lu. Aucune largeur 2D n'existe a une cellule.""" % (et_max, et_max + 0.0018, 0.01 - et_max - 0.0018, int((0.01 - et_max - 0.0018) / 0.00034)))
I_("""7.2 La tolerance des temoins positifs, 0.001, est posee a la main. Le meme code sur la meme machine doit rendre le
meme plateau a bien mieux ; 0.001 laisse passer un changement de bibliotheque, pas un changement d'instrument.""")
I_("""7.3 Les seuils de S1 (%d cellules jugees sur 56, %d tenues sur sept par w2) et de la portee (%d sur huit par kappa)
sont poses ici, apres le tirage et avant toute lecture. Ils ne dependent d'aucune prediction.""" % (R["s1_jugees_min"], R["s1_tenues_par_w2_min"], R["portee_tenues_par_kappa_min"]))
I_("""7.4 Ce que la plume sait du defaut de sa chaine. Aux deux points de barriere lus (Q2-a, Q2-b) le lecteur est a
0.00019 et 0.00034 AU-DESSUS de G3*. Refait a une dimension, variante par variante : cet ecart vient de la mediane de
l'absorbeur adapte, pas des ordres de la chaine. Il est sous l'etendue. La tolerance vaut %d fois le plus grand ; l'acte ne
pourra pas ecrire que la chaine est exacte.""" % int(0.01 / 0.00034))
I_("""7.5 Ce que le lecteur n'a jamais lu. Quatre cellules (%s) ont un plateau predit au-dessus du plus grand plateau
qualifie (1.08861e-04, Q-d), jusqu'a %.2f fois, a des couplages de plus de 2e-03 ; quatre (%s) sont sous le plus petit
plateau qualifie au sommet (2.05518e-09, Q2-b), jusqu'a %.3f fois. Aucune borne n'est posee : si le lecteur n'y qualifie
pas, la cellule est non lue et se compte comme telle.""" % (", ".join(haut), max(G) / 1.08861e-04, ", ".join(bas), min(G) / 2.05518e-09))
L_("")
L_("8. CE QUE CHAQUE ISSUE ENGAGE")
for t in ("""L'INSTRUMENT NE TIENT PAS (etage A), ou LES TEMOINS POSITIFS NE TIENNENT PAS (garde) : aucune cellule n'est lue,
rien n'est juge ; l'acte le dit ; une suite demande un autre gel, ou les cellules, restees vierges, peuvent etre
reprises telles quelles.""",
          """S1 TENU. L'acte peut ecrire : "a cinquante-six cellules tirees au sort, en huit tirages, pour |delta| de 0.00007 a
0.00048 et kappa de 0.0363 a 1 [les kappa de la portee], la chaine d'ordre 3 sous absorbeur adapte rend la largeur de
l'etat porte par (0, 0) a 0.01 pres en logarithme, au-dela de sa propre etendue et de l'etalement du lecteur". Avec le
delta 102, la loi d'echelle de la largeur du vide est alors eprouvee des ailes au sommet. Il NE peut PAS ecrire : que la
chaine est exacte (7.4) ; que l'ordre 3 fait mieux que le premier ordre (section 1) ; quoi que ce soit de la duree de vie
du systeme ferme ; quoi que ce soit de w2 = 2 exactement ni au-dela de kappa = 1 ; "cinquante-six cellules" sans dire
"huit tirages", ni sans dire que ce que la graine a fait varier est le couplage, le signe et l'echelle du desaccord.""",
          """S1 TENU SAUF UNE CELLULE. La meme phrase, la cellule nommee, avec son ln q, sa bande, son w2 et son kappa.""",
          """S1 TOMBE. L'acte ecrit que la chaine ne rend pas la largeur du vide au sommet a cette tolerance, cellules nommees.
Aucune autre chaine, aucun autre absorbeur de chaine, aucune autre tolerance, aucun autre eta0 n'est essaye sur ces
cellules.""",
          """S1 NON CONCLUANT. L'acte donne les comptes et dit lequel des deux a manque : le lecteur (cellules non lues) ou la
resolution (cellules non jugeables). Ce n'est ni une refutation ni une confirmation. Pas de rejeu, pas de nouveau
seuil.""",
          """Dans tous les cas : la table par cellule est publiee (statut du lecteur, plateaux et ecarts des quatre absorbeurs,
temoin, Gamma_pl, s, bande, ln q, jugement, et les grandeurs consignees), les cellules non lues avec leur motif, et les
neuf temoins positifs."""):
    B_(t)
L_("")
L_("9. GARDES (chaque journal dit ce qu'il ne joue pas)")
for t in ("""G-1 canons en dur : moteur, sonde et feuille deposees du lecteur, depot, couplages et references du temoin et des
ancres, table deposee du gel "ordre 3", table gelee, pilote de lecture de machine 2, feuille ; un ecart arrete.""",
          """G-2 le pilote de lecture lit le bloc du lecteur dans le fichier depose, au canon controle ; chaque fichier de lecture
porte l'empreinte du texte du bloc (5b835ce079ce2cf4), que la feuille exige.""",
          """G-3 forme de chaque fichier, controlee par la feuille avant tout jugement : canons, point egal a celui de la table
(w2, m, couplage ecrit, r_c, eta0), absorbeurs et boites, quatre trajectoires de douze barreaux, signe, site, energie
de depart. Un fichier de cellule manquant ou non conforme : RUN INCOMPLET, rien n'est juge.""",
          """G-4 instrument du lecteur : etage 0, ancres, etage 1, par les pieces deposees, tolerances inchangees.""",
          """G-5 temoin : le jumeau a la geometrie de chaque point.""",
          """G-6 temoins positifs du sommet : ils disent que l'instrument, le jour du run, rend au sommet ce qu'il y a rendu a Q
et a Q2. Ils ne disent pas qu'il y lit juste : c'est le meme code.""",
          """G-7 la garde est jouee AVANT toute lecture de cellule, et refuse un dossier ou une cellule a deja un fichier ; le
pre-vol s'arrete apres elle.""",
          """G-8 une seule execution : le pilote exige un dossier neuf et joue chaque appel une fois ; un code de sortie non nul
l'arrete.""",
          """G-9 ce que l'accord des quatre absorbeurs eprouve : l'independance de la largeur a la boite et a la forme de
l'absorbeur. Il n'eprouve PAS l'exactitude de la largeur : une erreur commune aux quatre lui echappe, et une erreur
commune au lecteur et a la chaine echapperait au gel entier."""):
    I_(t)
L_("")
L_("10. ANNONCES DE LA PLUME (ecrites apres le tirage ; aucune 2D a une cellule)")
P_("""Ce sont des jugements, pas des calculs. Probabilites :""")
for t in ("""A-1 (0.95) l'instrument du lecteur tient (etage A).""",
          """A-2 (0.97) les neuf temoins positifs tiennent.""",
          """A-3 (0.95) le temoin tient aux 56 cellules.""",
          """A-4 (0.70) le lecteur qualifie les 56 cellules ; (0.90) au moins cinquante.""",
          """A-5 S1 : TENU 0.80 ; TENU SAUF UNE CELLULE 0.02 ; TOMBE 0.02 ; NON CONCLUANT 0.08 ; le reste (0.08) est
l'instrument ou les temoins positifs.""",
          """A-6 (0.75) aux cellules lues, le plus grand |ln q| est sous 0.001.""",
          """A-7 (0.70) aux seize cellules de barriere (kappa = 0.0363 et 0.0530), ln q est negatif, le lecteur au-dessus de la
chaine comme a Q2-a et Q2-b, a douze cellules au moins.""",
          """A-8 (0.65) aux sept paires miroirs, le rapport lu est a 0.0001 pres de celui de la chaine a cinq paires au moins. La
chaine donne, de kappa = 0.0363 a 1 : %s.""" % " ; ".join("%+.5f" % m[3] for m in miroirs),
          """A-9 (0.75) a chaque kappa, l'etalement de ln(Gamma_pl / |delta|) sur les w2 lus est sous 0.001 ; la chaine donne de
%.5f a %.5f.""" % (min(etal.values()), max(etal.values()))):
    I_(t)
P_("""La plume annonce donc que S1 tient a quatre chances sur cinq. Ce qu'elle craint n'est pas un desaccord : c'est une
cellule non lue au bord de ce que le lecteur a deja qualifie, ou un instrument qui ne se rejoue pas. Elle le gele ainsi.""")
L_("")
L_("11. DEROULEMENT, E19, ET CE QUI EST PERMIS")
P_("""ORDRE. (1) Machine 2 dit son tirage et certifie cette piece, la table, la feuille et son banc, le pilote et son
banc ; un seul tour de correction. (2) Feu vert ecrit de l'operateur. (3) Machine 2 joue le pilote UNE fois, dans un
dossier neuf. (4) Lot de resultat : les fichiers de l'etage A, les 130 fichiers de lecture, la garde, le verdict, les
journaux, le journal du pilote. (5) Machine 1 authentifie et rejoue la feuille. (6) Acte.""")
P_("""PRE-VOL. Avant le feu vert, machine 2 peut jouer le pilote avec --prevol : section 4.6. Son pilote peut deriver du
mien s'il le faut, et elle le dit ; --drapeau -P et un fil BLAS par appel y sont deja.""")
P_("""UNE SEULE EXECUTION. Un pilote arrete par une panne se relance ENTIER dans un dossier neuf, et l'acte le dit ; aucun
appel n'est rejoue apres lecture de sa sortie.""")
P_("""DEUX MACHINES. Le verdict est celui de la feuille jouee par machine 2 dans le run. Machine 1 la rejoue sur les
fichiers du lot : la feuille ne calcule aucune chaine, les predictions sont dans la table ; les deux verdicts doivent etre
les memes. S'ils different, l'acte donne les deux et retient la lecture la MOINS favorable a l'enonce.""")
P_("""E19. Aucune des deux machines ne lit une cellule avant le feu vert ; machine 1 n'y lit rien en 2D, ni avant ni
apres : elle relit le lot de resultat. Ce gel ne se rejoue pas sous d'autres seuils, d'autres gardes, une autre chaine ou
d'autres cellules apres lecture.""")
L_("")
L_("12. COUTS (a mesurer au pre-vol de machine 2, pas a promettre)")
P_("""Etage A : 1365 s de calcul en trois appels sur le conteneur de machine 1 au gel "largeur du vide" ; BOCAL4 l'a joue
aux deltas 100 et 102. Etages A' et B : 130 lectures dans des boites de 122 au plus ; d'apres machine 2, les dix lectures
de Q ont pris 2 min 35 s et les huit de Q2 2 min 28 s sur seize coeurs logiques. Etage C : quelques secondes.""")
L_("")
L_("13. LIMITES DECLAREES")
for t in ("""L-1 S1 ne separe pas l'ordre 3 des ordres inferieurs (section 1).""",
          """L-2 Huit tirages, pas cinquante-six epreuves : a kappa egal la chaine ne varie que de %.5f au plus d'un w2 tire a
l'autre. Ce que la graine fait varier est le couplage, le signe et l'echelle du desaccord (reserve de machine 2).""" % max(etal.values()),
          """L-3 Aucun des sept kappa n'a ete lu en 2D avant le run ; ils sont encadres par les neuf points sacrifies et, pour
0.0363, par les cellules de trois barreaux du delta 102.""",
          """L-4 La regle de eta0 est une convention dans une zone que Q et Q2 ont trouvee plate ; le gel ne l'eprouve pas : il
consigne, par cellule, les barreaux plats sous A.""",
          """L-5 La chaine et la 2D partagent le moteur ; une erreur commune au lecteur et a la chaine ne se verrait pas (G-9).""",
          """L-6 La largeur est celle d'un etat sous absorbeur, stable sous les variations jouees. Rien n'est dit de la duree de
vie du systeme ferme.""",
          """L-7 Le pilote de ce gel n'a jamais joue une lecture reelle avant le pre-vol de machine 2 (4.5).""",
          """L-8 Les seuils de S1, la tolerance des temoins positifs et les probabilites de la section 10 sont de la plume de
machine 1, posees a la main.""",
          """L-9 Une definition du hamiltonien effectif : celle des blocs deposes (forme symetrique)."""):
    I_(t)
L_("")
L_("14. ECARTS DECLARES, ET REPONSES AUX REMARQUES DE MACHINE 2 (lot 21e9bddfe5db83b2)")
for t in ("""E-1 La premiere partie annoncait, pour temoins, "le jumeau a chaque cellule, les ancres et le temoin positif du
depot". S'y AJOUTENT les neuf temoins positifs du sommet et la garde qui les lit avant toute cellule : l'etage A eprouve
l'instrument aux ailes, sous la regle du depot ; rien n'y eprouvait la regle de eta0 du sommet le jour du run.""",
          """E-2 Le pilote de lecture est celui de machine 2, celui qui a lu Q et Q2, et non une sonde neuve de machine 1 : c'est
l'instrument qualifie, et machine 1 ne joue aucune 2D. La premiere partie disait "le lecteur creux du depot" : c'est son
bloc qui est execute, depuis son fichier.""",
          """E-3 La portee par kappa (section 6) n'etait pas annoncee. Elle ne change pas l'issue de S1 : elle borne la phrase de
l'acte.""",
          """E-4 Le pre-vol se joue sur la table du gel et s'arrete avant les cellules, au lieu d'une table de pre-vol a part :
les temoins positifs sont dans la table gelee.""",
          """R-1 (T et la bande) : la formule est en section 5 ; c'est celle du gel "largeur du vide". "Tient jusqu'a 0.005
environ" voulait dire T moins la bande : la tolerance pour tenir est plus serree que T.""",
          """R-2 (ce qu'on exige de B, C et D) : section 5. Une cellule sans plateau sous B, C ou D, ou en desaccord avec A, est
NON LUE. Une lecture non suivie hors de la fenetre retenue ne change rien : le banc le montre (cas b11).""",
          """R-4 (le signe de delta) : consigne, non juge ; les sept paires miroirs le liront a kappa et |delta| egaux.""",
          """R-5 (le cout) : section 12.""",
          """Sa reserve sur les huit tirages est en L-2 et dans ce que l'acte ne peut pas ecrire (section 8)."""):
    I_(t)
L_("")
L_("15. CE QUE MACHINE 2 CERTIFIE")
for t in ("""(a) SON tirage sur la graine 114565, par son code : les memes 56 cellules, avec les memes trois nombres ecrits ;
sinon PAS DE GEL ;""",
          """(b) que les predictions de la table gelee sont celles de sa propre table aux 56 cellules ;""",
          """(c) la feuille : qu'elle fait ce que disent les sections 5 et 6 ; son banc rejoue ;""",
          """(d) le pilote : qu'il enchaine ce que dit la section 4.2 ; son banc rejoue ; son pre-vol si elle le joue ;""",
          """(e) que le pilote de lecture au canon 47a84eae6052f006 est bien le sien, inchange depuis Q et Q2, et que les
plateaux de reference des neuf temoins sont ceux de ses sorties ;""",
          """(f) qu'elle accepte, ou refuse, ce qui est pose ici : les temoins positifs du sommet et leur tolerance, les seuils
de S1, la portee, les ecarts E-1 a E-4."""):
    I_(t)
L_("")
L_("16. PIECES DE CE LOT (convention B)")
PIECES = ("table_cellules_gel_sommet_v1.json", "predictions_sommet_machine1_v1.py", "predictions_sommet_machine1_v1.log", "tirage_sommet_graine_114565_machine1_v1.log",
          "jobs_gel_sommet_v1.txt", "jobs_temoins_sommet_v1.txt", "feuille_gel_sommet_machine1_v1.py", "banc_feuille_gel_sommet_machine1_v1.py", "banc_feuille_gel_sommet_machine1_v1.log",
          "garde_sur_les_sorties_de_Q_et_Q2_machine1_v1.log", "pilote_gel_sommet_machine1_v1.py", "banc_pilote_gel_sommet_machine1_v1.py", "banc_pilote_gel_sommet_machine1_v1.log")
for nom in PIECES:
    L_("    %s  %s" % (canon_B(ch(nom)), nom))
L_("    (ce script)       construction_gel_sommet_partie2_machine1_v1.py")
P_("""Le lot porte aussi le controle de cette piece contre ces sorties et son journal, ecrits apres elle : le manifeste du
lot fait foi.""")
texte = "\n".join(out) + "\n"
assert all(ord(c) < 128 for c in texte), "non ASCII"
longues = [l for l in texte.split("\n") if len(l) > W]; assert not longues, longues
assert chr(37) not in texte, "signe pour cent"
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit : %s ; %d lignes ; plus longue ligne %d ; canon B %s" % (SORTIE, len(texte.split("\n")) - 1, max(len(l) for l in texte.split("\n")), canon_B(SORTIE)))
