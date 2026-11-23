# -*- coding: ascii -*-
"""CONSTRUCTION DU PROJET D'ACTE DU RUN DU GEL "SOMMET" -- machine 1, v1, 2026-11-23. Aucun calcul de physique.
Assemble le texte de l'acte et y porte les nombres lus dans : la table gelee ; le verdict REJOUE par machine 1 (sa
feuille, au canon, sur les fichiers du lot de resultat) ; le verdict du run et les fichiers du run de machine 2, lus
comme des donnees (rien de ses lots n'est execute) ; le journal du pilote du run. Lignes de 100 colonnes au plus, ASCII,
sans signe pour cent.
Usage : python3 -I -B construction_journal_delta_nn_sommet_machine1_v1.py <table gelee.json> <verdict rejoue.json>
        <dossier du run de machine 2> <note de resultat de machine 2.md> <note de certification de machine 2.md> <sortie.md>"""
import sys, os, re, json, math, hashlib, unicodedata, textwrap
from fractions import Fraction as F
TABLE, VM, RUN, NOTE_R, NOTE_C, SORTIE = sys.argv[1:7]
def canon_B(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
T = json.load(open(TABLE)); B = json.load(open(VM)); A = json.load(open(os.path.join(RUN, "verdict_sommet.json")))
assert canon_B(TABLE) == "4238e2b262119f83" and B["table_canon"] == A["table_canon"] == "4238e2b262119f83" and B["feuille_canon"] == A["feuille_canon"] == "ac934e0caaa59c08"
C = {c["id"]: c for c in T["cellules"]}; R = B["cellules"]; RA = {r["id"]: r for r in A["cellules"]}
assert A["verdict"] == B["verdict"] == "S1 TENU" and A["S1"]["comptes"] == B["S1"]["comptes"] and all(RA[r["id"]]["jugement"] == r["jugement"] for r in R)
ecart_rejeu = max(max(abs(RA[r["id"]][k] - r[k]) for r in R) for k in ("ln_q", "ln_Gamma_pl", "bande", "etalement_du_lecteur"))
# --- le journal du pilote
jp = open(os.path.join(RUN, "pilote_gel_sommet.log")).read(); lj = jp.strip().split("\n")
codes = re.findall(r"code=(\d+) duree=(\d+) s", jp); assert all(c == "0" for c, d in codes)
debut, fin = lj[0][:19], lj[-1][:19]; duree = int(re.search(r"duree totale (\d+) s", lj[-1]).group(1))
nproc = int(re.search(r"(\d+) processus", lj[0]).group(1)); assert "drapeau -P" in lj[0] and "PRE-VOL" not in lj[0]
dur = lambda motif: [int(d) for (n, d) in re.findall(r"  (%s)\s+code=0 duree=(\d+) s" % motif, jp)]
d_cell = dur(r"lecture (?:MP|PP|MG|PG)\w+ (?:jumeau|fantome)"); d_tem = dur(r"lecture Q\w+ (?:jumeau|fantome)"); assert len(d_cell) == 112 and len(d_tem) == 18
# --- les lectures non suivies et les poids, relus dans les fichiers de lecture
non_suivies = []; poids_suivis = []; n_fan = n_jum_ns = 0
for c in T["cellules"]:
    f = json.load(open(os.path.join(RUN, "lect2D_%s_fantome.json" % c["id"]))); j = json.load(open(os.path.join(RUN, "lect2D_%s_jumeau.json" % c["id"])))
    for a in "ABCD":
        for k in T["regle"]["barreaux"]:
            x = f["lecture"]["traj"][a][str(k)]; n_fan += 1
            if x.get("suivi"): poids_suivis.append(x["poids_site"])
            else: non_suivies.append((c["id"], a, k))
            n_jum_ns += not j["lecture"]["traj"][a][str(k)].get("suivi")
plats = sorted(set.intersection(*[set(r["consigne"]["barreaux_plats_sous_A"]) for r in R]))
kappas = sorted(set(r["kappa"] for r in R), key=float); w2s = []
for r in R:
    if r["w2"] not in w2s: w2s.append(r["w2"])
lq = [r["ln_q"] for r in R]; pire = max(R, key=lambda r: abs(r["ln_q"])); juste = min(R, key=lambda r: r["tolerance"] - r["bande"] - abs(r["ln_q"]))
sous_etendue = sum(1 for r in R if abs(r["ln_q"]) < r["etendue"])
mir = B["consigne"]["paires_miroirs"]; ech = B["consigne"]["loi_d_echelle"]
dec = lambda w: "%.5f" % float(F(w))
W = 100
def par(texte, indent="  ", suite=None):
    t = re.sub(r" ([:;?!])(?= |$)", lambda m: chr(1) + m.group(1), " ".join(texte.split()))
    return textwrap.fill(t, width=W, initial_indent=indent, subsequent_indent=indent if suite is None else suite, break_long_words=False, break_on_hyphens=False).replace(chr(1), " ")
out = []
def P_(texte, indent="  ", suite=None): out.append(par(texte, indent, suite))
def L_(ligne): out.append(ligne)
def I_(texte): out.append(par(texte, "  ", "    "))

L_("DELTA nn -- LARGEUR DU VIDE AU SOMMET DU PROFIL, DE KAPPA = 0.0363 A KAPPA = 1 :")
L_("RUN DU 23/11/2026 SOUS LE GEL EN DEUX PARTIES 1e5039cade55d13f (REGLE DE TIRAGE) ET")
L_("81a2febcfce49007 (INSTRUMENT, ENONCE).")
L_("VERDICT : S1 TENU.")
L_("-- PROJET, VERSION 1")
L_("(plume machine 1 ; certifications, run et juge independant machine 2 ; a contresigner par machine 2)")
L_("=======================================================================")
L_("")
L_("nn.0 POSITION")
P_("""Ce delta rend le run unique du gel "sommet". Le delta 102 avait montre que la chaine a une dimension rend la largeur
de l'etat que porte le site (0, 0), le vide, aux ailes de la resonance 2:1 : trois a seize barreaux de barriere, |delta|
de 0.003 a 0.018, kappa au plus 0.0262. La question de ce gel : la rend-elle encore au sommet, de deux barreaux jusqu'a la fenetre sans barriere, la
ou le saut au pied de l'echelle vaut jusqu'au desaccord lui-meme, a des cellules que personne n'a choisies ? Cinquante-six
cellules ont ete tirees par une graine de l'operateur (114565) : huit w2 (%s), sept kappa chacun (%s). Les predictions
etaient gelees dans une table (4238e2b262119f83) avant toute lecture.""" % (", ".join(dec(w) for w in w2s), ", ".join(kappas)))
P_("""Reponse de la feuille du run : S1 TENU. Cinquante-six cellules lues, cinquante-six tenues ; aucune n'est tombee,
aucune n'est non jugeable, aucune n'est non lue ; sept tenues sur sept a chaque w2, huit sur huit a chaque kappa ; la
portee est les sept kappa. Machine 1 a rejoue la feuille sur les fichiers du run : meme verdict, memes 56 jugements.""")
P_("""A savoir avant tout le reste. (1) L'ecart de la chaine au plateau lu, |ln q|, vaut %.5f au plus (%s), pour une
tolerance de 0.01, a des largeurs de %.2e a %.2e et des couplages de %s a %s. (2) Cet ecart est sous l'etendue de la
chaine a %d cellules sur 56 : le gel est tenu a sa tolerance, et il ne MESURE pas l'erreur de la chaine en dessous de ce
que son absorbeur laisse indetermine. (3) Il n'oppose pas les ordres de la chaine. (4) Cinquante-six cellules sont HUIT
tirages, tous a |delta| de 0.00048 au plus : ce gel et le delta 102 ne se recouvrent pas (nn.8). (5) La largeur jugee est
celle d'un etat sous absorbeur ; cet acte ne dit rien de la duree de vie du systeme ferme.""" % (max(abs(v) for v in lq), pire["id"], math.exp(min(r["ln_Gamma_pl"] for r in R)), math.exp(max(r["ln_Gamma_pl"] for r in R)),
             min((r["g"] for r in R), key=float), max((r["g"] for r in R), key=float), sous_etendue))
L_("")
L_("nn.1 CE QUI A ETE JOUE, ET DANS QUEL ORDRE")
P_("""Ouverture. L'operateur a ecrit a machine 1 "je dis oui on ouvre. Par contre tous les calculs couteux, c'est sur
machine 2 ok ?" (22/11/2026, 20 h 09) : declaration de machine 1. A l'operateur de l'attester. Depuis, machine 1 n'a fait
aucun calcul a deux dimensions.""")
P_("""Qualifications. Avant le gel, machine 2 a lu le vide en 2D a neuf points declares sacrifies avant toute lecture (w2 =
2 a trois couplages ; w2 = 20001/10000 et 19999/10000), sur des mots de l'operateur qu'elle rapporte ("Oui GO !", "oui ces
4 pts") ; machine 1 avait ecrit ses attendus avant ; ils ont tenu (lots c58c2b3f533c516b et 295b2b1549b076c2 de machine 2,
423ec0fd24240977 et 074b131287ad2b6f de machine 1). Ces neuf points ne sont pas des cellules ; ils sont les temoins
positifs du run.""")
P_("""Premiere partie du gel (1e5039cade55d13f, regle de tirage et d'eligibilite, lot 3ba4618d7976c6ea) : certifiee par
machine 2 sans refus (lot 21e9bddfe5db83b2, 22 pieces) ; sa table des 560 cellules candidates, ecrite du texte, est celle
de machine 1 octet pour octet (table commune 77ce2a6c7e867011).""")
P_("""Graine. L'operateur a ecrit a machine 1 "graine 114565" (22/11, 23 h 21), apres lui avoir remis cette
certification. Machine 2 rapporte qu'il lui a ecrit la meme graine apres son compte rendu de certification. Les deux
machines ont tire chacune par son code, sans avoir lu le tirage de l'autre : memes huit w2, memes 56 cellules, memes
trois nombres ecrits par cellule (lot 3db782eea5023b31 de machine 2 ; comparaison de machine 1, 56 sur 56).""")
P_("""Seconde partie (81a2febcfce49007, instrument, enonce, tolerances, lot a2dc5cb2b9c3da0d) : certifiee par machine 2
(lot b7f328b916ba720d, 62 pieces) aux six points demandes, sans correction demandee, avec cinq remarques non bloquantes
(nn.9) ; AVANT le run d'apres ses pieces (son pre-vol finit a 00:05:47, le run part a 00:16:01) ; machine 1 ne l'a lue
qu'apres (ci-dessous). Son propre juge, ecrit du texte des sections 5 et 6, rend les memes resultats que la feuille du gel a
38 scenarios sur 38 ; les deux bancs de machine 1 rejouent chez elle (30 cas sur 30, 12 sur 12). Elle a joue le PRE-VOL
sur un mot de l'operateur qu'elle rapporte ("GO") : etage A, neuf temoins, garde ; aucune cellule lue ; l'instrument
tient, les neuf temoins rendent leur reference, 1120 s. C'etait la premiere execution reelle du pilote de machine 1.""")
P_("""Feu vert. Machine 2 rapporte qu'apres sa certification elle a dit a l'operateur que le run attendait son feu vert
ecrit, et qu'il a ecrit : "RUn". Machine 1 n'a pas vu ce message. A l'operateur de l'attester.""")
P_("""Un fait de deroulement. La seconde partie (section 11) prevoyait, apres la certification de machine 2, un tour de
correction, puis le feu vert. La certification n'est parvenue a machine 1 que le 23/11 a 1 h 37, APRES le lot de resultat
(1 h 15) : le tour n'a pas ete attendu. Il n'avait rien a porter : la certification ne demandait aucune correction,
machine 1 n'en avait aucune, et le run a joue les pieces du gel a leurs empreintes (nn.2). Machine 2 le dit elle-meme
dans sa note de resultat.""")
P_("""Run. UN run, dans un dossier neuf, lance le %s et fini a %s (heure de BOCAL4) ; duree totale %d s ; %d appels,
tous au code 0 ; aucun arret, aucune relance. Pilote joue : celui du gel, tel quel (ed4c3886b17fcdc3), %d processus,
drapeau -P, sans --prevol. Les canons que le pilote imprime au depart sont ceux du gel. Durees : etage A 20 s, 846 s et
897 s (etage 0, ancres, etage 1, en parallele) ; les dix-huit lectures des temoins de %d a %d s ; les 112 lectures des
cellules de %d a %d s, %d a la fois.""" % (debut, fin[11:], duree, len(codes), nproc, min(d_tem), max(d_tem), min(d_cell), max(d_cell), nproc))
P_("""E19. Machine 1 n'a lu en 2D le systeme a fantome ni le jumeau a aucune cellule ni a aucun w2 tire, ni avant ni
apres le run : son rejeu ne joue que la feuille. Machine 2 declare n'avoir lu aucune cellule avant la fin du pilote.""")
L_("")
L_("nn.2 L'INSTRUMENT")
P_("""Celui de la seconde partie, section 4, sans changement : etage A (la sonde et la feuille deposees du lecteur,
d5cc48f48e37af99 et 83701094e6a2b965, sur les pieces du depot) ; etage A' (les neuf temoins positifs du sommet) ; la garde
(la feuille du gel, etape --temoins, AVANT toute cellule) ; etage B (les 56 cellules, le jumeau sans fantome puis le
fantome, par le pilote de lecture de machine 2, 47a84eae6052f006, qui execute le bloc du lecteur depose) ; etage C (la
feuille du gel, ac934e0caaa59c08). Table jouee : 4238e2b262119f83.""")
P_("""Etage A : l'instrument du lecteur TIENT (verdict %s). Garde : TIENT (%s), jouee a %s, avant la premiere lecture de
cellule. Les neuf temoins positifs TIENNENT, chacun a 0 de son plateau de reference : c'est le meme code sur la meme
machine ; ils disent que l'instrument du jour est celui des qualifications, pas qu'il lit juste.""" % (
    canon_B(os.path.join(RUN, "verdict_ter_instrument.json")), canon_B(os.path.join(RUN, "garde_sommet.json")), re.search(r"(\d\d:\d\d:\d\d) GARDE : TIENT", jp).group(1)))
L_("    temoin  w2           g        plateau lu   reference    ln(lu / reference)")
for t, c in zip(B["temoins_positifs"]["points"], T["temoins_positifs"]):
    L_("    %-6s  %-11s  %-7s  %.5e  %.5e  %+.1e" % (t["id"], t["w2"], t["g"], math.exp(t["ln_Gamma_pl"]), math.exp(c["ln_Gamma_pl_reference"]), t["ecart_reference"]))
L_("")
L_("nn.3 LE VERDICT DE LA FEUILLE DU RUN")
P_("""Verdict du run : %s (canon %s). Par cellule : le plateau lu sous l'absorbeur A, l'etalement s du lecteur,
l'etendue de la chaine (table), la bande b = etendue + s, ln q = ln(G3* / plateau lu), le jugement. Tolerance T = 0.01 a
toutes : la cellule TIENT si |ln q| <= T - b. Les 56 cellules sont QUALIFIEES et leur temoin tient.""" % (A["verdict"], canon_B(os.path.join(RUN, "verdict_sommet.json"))))
L_("    cellule  w2       kappa   g            plateau lu   s       etendue  bande   ln q      jugement")
for r in R:
    L_("    %-7s  %s  %s  %s  %.5e  %.4f  %.4f   %.4f  %+.5f  %s" % (r["id"], dec(r["w2"]), r["kappa"], r["g"], math.exp(r["ln_Gamma_pl"]), r["etalement_du_lecteur"], r["etendue"], r["bande"], r["ln_q"], r["jugement"]))
P_("""S1 : %s. Tenues %d, tombees %d, non jugeables %d, non lues %d. Tenues par w2 (sur sept) : %s. Tenues par kappa (sur
huit) : %s. Portee : %s.""" % (B["S1"]["issue"], B["S1"]["comptes"]["TIENT"], B["S1"]["comptes"]["TOMBE"], B["S1"]["comptes"]["NON JUGEABLE"], B["S1"]["comptes"]["NON LUE"],
    " ; ".join("%s %d" % (dec(w), B["S1"]["par_w2"][w]["TIENT"]) for w in w2s), " ; ".join("%s %d" % (k, B["S1"]["par_kappa"][k]["TIENT"]) for k in kappas), " ".join(B["S1"]["portee_kappa"])))
ns_txt = " ; ".join("%s %s k = %+d" % x for x in non_suivies)
P_("""Lectures. Fantome : %d lectures suivies sur %d ; les %d non suivies (%s) sont hors des fenetres retenues et n'ont
rendu aucune cellule non qualifiee. Jumeau : %d non suivie sur %d ; sa plus grande largeur vaut %.1e du plateau au plus
(seuil 1e-6). Plus petit poids du site (0, 0) sur les lectures suivies du fantome : %.4f. Sous A, la largeur est plate a
0.005 pres aux barreaux k = %d a %d a toutes les cellules.""" % (n_fan - len(non_suivies), n_fan, len(non_suivies), ns_txt, n_jum_ns, n_fan,
    max(r["temoin"]["rapport_au_plateau"] for r in R), min(poids_suivis), plats[0], plats[-1]))
L_("")
L_("nn.4 LE REJEU DE MACHINE 1 (etape 5 du gel)")
P_("""Machine 1 a authentifie le lot de resultat (735b9394013b02db, 284 pieces, aucun ecart) et rejoue la feuille du gel,
a son canon, sur les 130 fichiers de lecture et le verdict de l'instrument, lus comme des donnees ; rien du lot n'est
execute. Verdict rejoue : %s (canon %s) ; meme issue, memes comptes, meme portee, memes 56 jugements et statuts ; plus
grand ecart sur ln q, le plateau, la bande et l'etalement : %.1e (deux bibliotheques de calcul ; les deux fichiers ne sont
donc pas identiques a l'octet). Les nombres de cet acte sont ceux du verdict rejoue.""" % (B["verdict"], canon_B(VM), ecart_rejeu))
P_("""Le juge independant de machine 2, ecrit du texte du gel avant le run, rejoue par elle sur les memes fichiers, rend le
meme verdict, la meme portee et les memes jugements cellule par cellule (sa note de resultat). Trois lectures du meme run
s'accordent ; il n'y a qu'UNE mesure 2D.""")
L_("")
L_("nn.5 LECTURE DE L'ENONCE")
P_("""S1 tient largement a sa tolerance : la plus grande bande est %.4f, et la cellule la plus pres de sa limite (%s) garde
%.4f entre |ln q| et T - b. Ce que cela ne dit pas : |ln q| est sous l'etendue de la chaine a %d cellules sur 56, et sous
l'etalement du lecteur a %d. L'accord a quelques dix-milliemes n'est donc pas resolu par ce gel ; il est compatible avec
ce que l'absorbeur de la chaine laisse indetermine. Et a kappa egal les huit w2 rendent le meme Phi a 0.0003 pres (nn.6) :
ce gel a lu sept valeurs de Phi(kappa), chacune a huit echelles du desaccord et du couplage, et non cinquante-six largeurs
independantes.""" % (max(r["bande"] for r in R), juste["id"], juste["tolerance"] - juste["bande"] - abs(juste["ln_q"]), sous_etendue,
    sum(1 for r in R if abs(r["ln_q"]) < r["etalement_du_lecteur"])))
L_("")
L_("nn.6 CE QUI ETAIT CONSIGNE SANS ETRE JUGE")
P_("""Le residu par kappa. ln q n'est pas un bruit : a kappa donne il a le meme signe aux huit w2 a %d kappa sur sept.
C'est une fonction de kappa de l'ordre de 2e-04, sous l'etendue de la chaine. Rien n'en est juge, et cet acte n'en donne
pas la cause.""" % sum(1 for k in kappas if len(set(r["ln_q"] > 0 for r in R if r["kappa"] == k)) == 1))
L_("            ln q aux huit w2              negatifs  Phi lu = plateau / |delta|  etalement, ln Phi")
L_("    kappa   minimum   maximum   moyenne   sur huit  minimum      maximum      lu       chaine")
for k in kappas:
    v = sorted(r["ln_q"] for r in R if r["kappa"] == k); ph = sorted(r["consigne"]["ln_Phi_lu"] for r in R if r["kappa"] == k)
    L_("    %s  %+.5f  %+.5f  %+.5f  %d         %.5e  %.5e  %.5f  %.5f" % (k, v[0], v[-1], sum(v) / 8, sum(x < 0 for x in v), math.exp(ph[0]), math.exp(ph[-1]),
       ech[k]["etalement_lu"], ech[k]["etalement_chaine"]))
P_("""La superposition en kappa. A kappa egal, la largeur lue rapportee au desaccord varie de %.5f au plus en logarithme
entre les huit w2, pour des desaccords de 0.00007 a 0.00048 et les deux signes ; la chaine donne %.5f au plus. A ces
desaccords la loi d'echelle nue, Gamma = |w2 - 2| Phi(kappa), se lit donc a quelques dix-milliemes. Ce n'etait PAS le cas
aux ailes : au delta 102, a profondeur egale, les quatre w2 (|delta| de 0.003 a 0.018) s'ecartaient de 0.0098 a trois
barreaux jusqu'a 0.1262 a seize, et c'est la chaine qui rendait ces ecarts. Consigne, pas juge.""" % (max(e["etalement_lu"] for e in ech.values()), max(e["etalement_chaine"] for e in ech.values())))
P_("""Le signe de delta. Le tirage a sorti une paire de w2 miroirs (1.99989 et 2.00011). A kappa egal, ln[Phi(delta < 0) /
Phi(delta > 0)] lu, et celui de la chaine entre parentheses : %s. L'effet du signe est sous 1e-04 ; le lecteur et la
chaine s'y accordent a %.5f pres.""" % (" ; ".join("%s %+.5f (%+.5f)" % (m["kappa"], m["ln_rapport_lu"], m["ln_rapport_chaine"]) for m in mir),
    max(abs(m["ln_rapport_lu"] - m["ln_rapport_chaine"]) for m in mir)))
P_("""Les ordres. L'ordre 3 est plus pres du plateau lu que le premier ordre a %d cellules sur 56 : le gel ne les separe
pas, comme sa section 1 l'ecrivait. ln q est negatif (le lecteur au-dessus de la chaine) a %d cellules, et du signe de
delta a %d.""" % (B["consigne"]["ordre3_plus_pres_que_ordre1"], B["consigne"]["ln_q_negatif"], B["consigne"]["ln_q_du_signe_de_delta"]))
t0 = {k: [math.exp(r["consigne"]["ln_Gamma_pl_sur_t0"]) for r in R if r["kappa"] == k] for k in kappas}
gk1 = {r["w2"]: float(r["g"]) for r in R if r["kappa"] == "1.0000"}; assert F("199989/100000") - 2 == -(F("200011/100000") - 2) == F(-11, 100000)
PsX2 = (gk1["199989/100000"] + gk1["200011/100000"]) / (2 * 0.00011)          # P / X(w2) a w2 = 2, interpole entre les deux w2 miroirs
res = [math.exp(t["ln_Gamma_pl"]) / float(t["g"]) * PsX2 for t in B["temoins_positifs"]["points"] if t["w2"] == "2"]; assert len(res) == 3
P_("""La largeur rapportee au saut au pied de l'echelle, moyenne par kappa : %s. A la resonance exacte, lue aux trois temoins
positifs de w2 = 2 et non aux cellules, elle vaut %s (le saut y est interpole entre les deux w2 miroirs).""" % (
    " ; ".join("%s %.4f" % (k, sum(t0[k]) / 8) for k in kappas), "%.4f" % min(res) if "%.4f" % min(res) == "%.4f" % max(res) else "%.4f a %.4f" % (min(res), max(res))))
L_("")
L_("nn.7 LES ANNONCES DE LA PLUME, CONFRONTEES AU RUN (gel, section 10)")
bar = [r for r in R if r["kappa"] in ("0.0363", "0.0530")]; nneg = sum(1 for r in bar if r["ln_q"] < 0)
pres = sum(1 for m in mir if abs(m["ln_rapport_lu"] - m["ln_rapport_chaine"]) <= 0.0001)
for t in ("""A-1 (0.95) l'instrument tient : oui. A-2 (0.97) les neuf temoins positifs tiennent : oui. A-3 (0.95) le temoin tient
aux 56 cellules : oui. A-4 (0.70) le lecteur qualifie les 56 cellules : oui.""",
          """A-5 S1 TENU (0.80) : c'est l'issue.""",
          """A-6 (0.75) plus grand |ln q| sous 0.001 : oui (%.5f).""" % max(abs(v) for v in lq),
          """A-7 (0.70) ln q negatif a douze cellules de barriere au moins sur seize : NON. Il l'est a %d : aux huit de kappa =
0.0530 et a %d des huit de kappa = 0.0363, ou il est de part et d'autre de zero. La plume avait generalise les deux points
de barriere des qualifications.""" % (nneg, sum(1 for r in bar if r["kappa"] == "0.0363" and r["ln_q"] < 0)),
          """A-8 (0.65) aux paires miroirs, rapport lu a 0.0001 de celui de la chaine a cinq paires au moins : oui (%d sur 7).""" % pres,
          """A-9 (0.75) a chaque kappa, etalement de ln(plateau / |delta|) sous 0.001 : oui (%.5f au plus).""" % max(e["etalement_lu"] for e in ech.values())):
    I_(t)
P_("""Huit annonces sur neuf sont du cote annonce ; A-7 tombe. Ce sont des jugements de plume, pas des enonces juges. La
crainte ecrite, une cellule non lue au bord de ce que le lecteur avait qualifie, ne s'est pas realisee.""")
L_("")
L_("nn.8 CE QUE CET ACTE ECRIT, ET CE QU'IL N'ECRIT PAS (gel, section 8)")
P_("""Il ecrit : a cinquante-six cellules tirees au sort, en huit tirages, pour |delta| de 0.00007 a 0.00048 et kappa de
0.0363 a 1, la chaine d'ordre 3 des blocs deposes, sous absorbeur adapte, rend la largeur de l'etat porte par (0, 0) a
0.01 pres en logarithme, au-dela de sa propre etendue et de l'etalement du lecteur.""")
P_("""Le gel permettait d'ajouter : "avec le delta 102, la loi d'echelle de la largeur du vide est alors eprouvee des
ailes au sommet". Cet acte ecrit moins, et autrement. (i) Ce que les deux gels eprouvent est la CHAINE : aux ailes la loi
d'echelle nue s'ecarte du plateau, et c'est la chaine qui rend l'ecart (nn.6). (ii) Les deux domaines ne se touchent
pas : le delta 102 est a |delta| de 0.003 a 0.018 et kappa au plus 0.0262 ; ce gel est a |delta| de 0.00048 au plus. Au
sommet a |delta| plus grand, donc a couplage plus fort (kappa = 1 a |delta| = 0.01 demande g voisin de 0.1), rien n'est
lu.""")
P_("""Il N'ecrit PAS : que la chaine est exacte (l'ecart est sous son etendue, et il a une structure en kappa) ; que
l'ordre 3 fait mieux que le premier ordre ; quoi que ce soit de la duree de vie du systeme ferme ; quoi que ce soit de w2 =
2 exactement, lu aux seuls temoins positifs, ni au-dela de kappa = 1 ; quoi que ce soit du
sommet a |delta| au-dela de 0.0005 ; "cinquante-six cellules" sans dire "huit tirages" :
a kappa egal la chaine ne varie que de 0.0005 d'un w2 a l'autre, et ce que la graine a fait varier est le couplage, le
signe et l'echelle du desaccord ; que la regle de eta0 est la bonne : c'est une convention dans une zone plate.""")
L_("")
L_("nn.9 REMARQUES DE MACHINE 2, DEFAUTS DE LA PLUME, ECARTS")
for t in ("""Remarques de machine 2 a sa certification, non bloquantes, sans correction : R-1, devant un fichier de cellule
malforme la feuille rend "RUN INCOMPLET" avec le code 0 et le pilote ecrit sa fin : le verdict se lit dans le fichier, pas
a la fin du pilote (c'est ce que fait cet acte) ; R-2, le cout ; R-3, le dossier neuf ; R-4, l'etage A eprouve
l'instrument aux ailes et sert peu au sommet ; R-5, eta0 se reduit a (kappa / 0.0262) |w2 - 2| aux 560 cellules.""",
          """Ecarts du gel, declares dans sa seconde partie et acceptes par machine 2 : E-1 (les neuf temoins positifs et la garde
s'ajoutent a ce que la premiere partie annoncait) ; E-2 (le pilote de lecture est celui de machine 2) ; E-3 (la portee) ;
E-4 (le pre-vol sur la table gelee).""",
          """Defauts de la plume de machine 1. D-REL-29 : a la qualification Q, son attendu Q-4 ne pouvait pas mordre ; vu par
machine 2. D-REL-30 : son esquisse portait deux w2 ou machine 2 avait lu le jumeau en 2D le
16/11 ; trouves par balayage et retires AVANT la premiere partie. Son annonce A-7 (nn.7). Le champ "poids_min" de sa
feuille prend aussi les lectures non suivies (il vaut %.4f) : il ne sert a aucun jugement ; le poids dit en nn.3 est relu
sur les lectures suivies. Son pilote n'avait jamais joue une lecture reelle avant le pre-vol de machine 2 : dit dans le
gel.""" % min(r["lecteur"]["poids_min"] for r in R),
          """Le tour de correction non attendu : nn.1.""",
          """Erreurs que machine 2 dit a sa certification : trois criteres de son propre test etaient faux a ses deux premiers
passages ; la feuille du gel n'avait rien a corriger."""):
    I_(t)
L_("")
L_("nn.10 LIMITES")
for t in ("""Celles du gel, section 13, restent (L-1 a L-9) : S1 ne separe pas les ordres ; huit tirages ; aucun des sept kappa
n'avait ete lu en 2D avant le run ; eta0 est une convention ; une seule definition du hamiltonien effectif.""",
          """Le domaine : |delta| de 0.00007 a 0.00048, couplages de 2.5e-05 a 4.7e-03. Ce gel et le delta 102 ne se recouvrent
pas (nn.8).""",
          """La 2D des cellules a ete calculee sur une seule machine (BOCAL4), une seule fois, par un pilote de lecture ecrit par
machine 2. Machine 1 n'en a rejoue aucune. Trois juges ont lu les memes fichiers.""",
          """La chaine et la 2D partagent le moteur (82a0be882568fe0c). L'accord eprouve la reduction a une dimension et les
absorbeurs, pas le moteur ; une erreur commune au lecteur et a la chaine ne se verrait pas.""",
          """Les temoins positifs sont le meme code sur la meme machine : ils eprouvent la reproduction, pas l'exactitude.""",
          """La largeur est celle d'un etat sous absorbeur, stable sous quatre absorbeurs. Rien n'est dit du systeme ferme.""",
          """Les mots de l'operateur a machine 2 (qualifications, pre-vol, feu vert) sont rapportes par elle ; l'ouverture et la
graine donnee a machine 1 sont des declarations de machine 1."""):
    I_(t)
L_("")
L_("nn.11 SUITE")
P_("""Contreseing de machine 2. Depot : a la decision de l'operateur, numero pris au depot. Ce run s'appuie sur des pieces
qui ne sont pas au registre : les deux parties du gel et leurs lots (table gelee, feuille, pilote, tirage), les lots des
qualifications, des certifications, du tirage et du resultat, et le pilote de lecture de machine 2. Ce gel ne se rejoue
pas.""")
L_("")
L_("nn.12 PIECES (convention B)")
for canon, quoi in (("1e5039cade55d13f", "gel, premiere partie (lot 3ba4618d7976c6ea)"), ("81a2febcfce49007", "gel, seconde partie (lot a2dc5cb2b9c3da0d)"),
                    ("4238e2b262119f83", "table gelee des 56 cellules et des neuf temoins"), ("77ce2a6c7e867011", "table commune d'eligibilite"),
                    ("49a40d9098b55361", "bloc de l'absorbeur adapte (registre)"), ("ac934e0caaa59c08", "feuille du gel"), ("ed4c3886b17fcdc3", "pilote du gel, joue tel quel"),
                    ("47a84eae6052f006", "pilote de lecture de machine 2"), ("c58c2b3f533c516b", "lot de machine 2 : qualification Q"), ("295b2b1549b076c2", "lot de machine 2 : qualification Q2"),
                    ("21e9bddfe5db83b2", "lot de machine 2 : certification de la premiere partie"), ("3db782eea5023b31", "lot de machine 2 : son tirage"),
                    ("b7f328b916ba720d", "lot de machine 2 : certification de la seconde partie, pre-vol"), ("735b9394013b02db", "lot de machine 2 : resultat du run"),
                    (canon_B(NOTE_C), "sa note de certification de la seconde partie"), (canon_B(NOTE_R), "sa note de resultat"),
                    (canon_B(os.path.join(RUN, "pilote_gel_sommet.log")), "journal du pilote du run"), (canon_B(os.path.join(RUN, "verdict_ter_instrument.json")), "verdict de l'instrument du lecteur"),
                    (canon_B(os.path.join(RUN, "garde_sommet.json")), "verdict de la garde"), (canon_B(os.path.join(RUN, "verdict_sommet.json")), "verdict de la feuille du run"),
                    (canon_B(VM), "verdict rejoue par machine 1")):
    L_("    %s %s" % (canon, quoi))
L_("")
L_("-- FIN journal_delta_nn_sommet_v1 --")
texte = "\n".join(out) + "\n"
assert all(ord(c) < 128 for c in texte), "non ASCII"
longues = [l for l in texte.split("\n") if len(l) > W]; assert not longues, longues
assert chr(37) not in texte, "signe pour cent"
open(SORTIE, "w", encoding="ascii", newline="\n").write(texte)
print("ecrit : %s ; %d lignes ; plus longue ligne %d ; canon B %s" % (SORTIE, len(texte.split("\n")) - 1, max(len(l) for l in texte.split("\n")), canon_B(SORTIE)))
print("nombres : appels %d ; duree %d s ; non suivies %d ; poids suivi min %.4f ; sous l'etendue %d ; plats %s ; ecart de rejeu %.1e" % (len(codes), duree, len(non_suivies), min(poids_suivis), sous_etendue, plats, ecart_rejeu))
