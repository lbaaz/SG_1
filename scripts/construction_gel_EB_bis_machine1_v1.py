# -*- coding: ascii -*-
# CONSTRUCTION DU GEL "QUALIFICATION E-B BIS v1" (PB-1 : le gel v2, depose et
# joue, n'est pas edite). Gel bis v1 = gel v2 (cde0cd11a763f26d, au registre)
# + des remplacements a ANCRE UNIQUE, nommes comme a la section 15 du gel bis.
# Chaque nombre que les hunks tapent est AFFIRME contre sa source avant
# l'ecriture ; un ancre absent ou double arrete tout.
# Arguments : <registre> <sortie nuit sonde_etage1.json> <table TP> <dossier du
#             diagnostic m2> <lecture etape 0 .json> <sortie> <journal>
import sys, os, re, json, math, hashlib, unicodedata
from fractions import Fraction

REG, NUIT, TABLE, DIAG, E0, SORTIE, JOURNAL = sys.argv[1:8]
F = open(JOURNAL, "w", encoding="ascii", newline="\n")


def dire(s):
    print(s)
    F.write(s + "\n")


def cB(chemin):
    t = unicodedata.normalize("NFC", open(chemin, "rb").read().decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


H = [
("B0", r'''# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- v2
# Banc de qualification, CLASSE 2 -- plume machine 1 -- 11/11/2026
# Piste (0) de la branche quantique, etape 1. Ce n'est PAS une manche.''',
r'''# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- BIS, v1
# Banc de qualification, CLASSE 2 -- plume machine 1 -- 13/11/2026
# Piste (0) de la branche quantique, etape 1 bis : REPRISE apres le
# delta 94. Ce n'est PAS une manche, et ce n'est PAS un v3 du gel
# cde0cd11a763f26d.'''),

("B1", r'''du FICHIER ENTIER, de la premiere ligne au saut de ligne final apres le
terminateur -- "titre a terminateur" ne designait rien d'autre (M-4).
v2 = v1 (8603af9d4f63e9dc) + les hunks de la section 15 : c'est LE tour
de correction de la section 12.''',
r'''du FICHIER ENTIER, de la premiere ligne au saut de ligne final apres le
terminateur.
NOUVEAU GEL. Le gel v2 (cde0cd11a763f26d) est JOUE : etage 1 du 12/11,
verdict NON CONCLUANT D'INSTRUMENT, delta 94 (fe10bfe), qui ecrit "sous
ce gel, pas de v3". Ce gel-ci en est la REPRISE, decidee par
l'operateur (relais du 13/11 ; a confirmer par lui a machine 2 avant
le run), et le DERNIER ESSAI (section 12). Il est construit du gel v2
par les hunks de la section 15, avec UNE difference de fond : l'echelle
en eta (3.6) est prolongee du cote de l'absorbeur fort, de k = -2 a
k = -5. Le reste est soit consequence de cette difference (comptes,
couts), soit etat des lieux (sources, ce qui a ete vu, annonces), soit
precision sans effet sur un statut ; la section 15 dit lequel.'''),

("B2a", r'''  registre  lbaaz/SG_1, HEAD 2ec6775, plafond 93 (clone frais du 11/11)''',
r'''  gel v2    gels/qualification_EB_pre_enregistrement_v2.md
                                                    cde0cd11a763f26d  JOUE
  acte 94   journal/journal_delta_94_qualification_EB_v2.md
                                                    569ccbd0d1adb927
  la nuit   lot m2 72f65ad8a898fbb5 ; sortie de la sonde
                                                    ab31334aea5c444a
  TP        liste des couplages retenus (j = 6 et j = 8)
                                                    69b3bab3bb8480b7
            table des references (m2 ; certifiee par m1, lot
            7b64b1b7d86c0591)                       4d51dd58ef456fe9
            REPRISES TELLES QUELLES : aucune reference n'est recalculee.
  reglage   diagnostic du TP a barreaux forts, lot m2 762a89e8ad7d498a
            (HORS GEL, NON OPPOSABLE ; section 4)
  registre  lbaaz/SG_1, HEAD fe10bfe, plafond 94 (releve du 13/11)'''),

("B2b", r'''Le lot de l'etape 0 n'etait pas detenu par m2 au 11/11 (M-3) : il est
JOINT au lot de ce gel. Tout nombre que ce gel en tire se relit dans
les six pieces f070 du run, sans lui.''',
r'''Le lot de l'etape 0 est au registre depuis le delta 94. Tout nombre que
ce gel en tire se relit dans les six pieces f070 du run, sans lui.'''),

("B3", r'''3.6 ECHELLE EN eta. eta_k = eta0 * 2^(-k), k = -2, -1, 0, ..., 12 :
quinze valeurs, quatre decades et un quart. Les quatre valeurs du run
sont k = 0, 1, 2, 3. La multiplication par une puissance de deux est
exacte : eta se porte en cette seule forme.''',
r'''3.6 ECHELLE EN eta. eta_k = eta0 * 2^(-k), k = -5, -4, ..., 12 :
dix-huit valeurs, cinq decades et un dixieme. Les quatre valeurs du run
sont k = 0, 1, 2, 3 ; les quinze du gel v2 sont k = -2 a 12 ; les trois
barreaux AJOUTES sont k = -5, -4, -3 (eta = 32, 16 et 8 fois eta0).
Aucun barreau du gel v2 n'est retire. La multiplication par une
puissance de deux est exacte : eta se porte en cette seule forme.
ORDRE DE PARCOURS : k = 3, puis 4 a 12, puis 2, 1, 0, -1, ..., -5.'''),

("B5", r'''Ce que la plume a vu avant d'ecrire : les trois pas de descente du run
par point (k = 0 a 3, quatre valeurs). Une fenetre demande cinq
valeurs : aucune issue de ce gel n'est calculable sur ce qui a ete vu.
Vu DEPUIS le v1 (note m2 0d11d6866e3c5f37) : un essai de formule de m2
a UN point de l'echelle du TP, g_8 = 0.10, largeur 6.428e-09 par
rotation complexe. Ce n'est pas la reference et aucune valeur de la
sonde n'existe ; la plume connait donc l'ordre de grandeur a ce g.
Si le temoin positif lui-meme ne tient pas tau, le banc rend NON
CONCLUANT D'INSTRUMENT et NE LIT PAS le fantome ; tau ne se desserre
pas sur les donnees du fantome.''',
r'''Ce que la plume a vu avant d'ecrire, DU FANTOME : les trois pas de
descente du run par point (k = 0 a 3, quatre valeurs) et, au seul
point 1.95, les largeurs de dix etats a k = 3 (faute D-QEB-1 du delta
94). Une fenetre demande cinq valeurs : aucune issue de l'etage 2
n'est calculable sur ce qui a ete vu.
Ce que la plume a vu DU TEMOIN, et qui fait de lui un temoin REGLE et
non plus un test aveugle : (i) l'etage 1 du 12/11 sous le gel v2, les
soixante largeurs du TP, k = -2 a 12 ; (ii) le rejeu ponctuel de m1,
six decompositions ; (iii) le diagnostic de m2 du 13/11, vingt
decompositions du jumeau H+, k = -6 a -2, G20 et G30, j = 6 et 8, par
un code qui n'est pas la sonde. (ii) et (iii) sont HORS GEL et NON
OPPOSABLES ; aucun ne touche au fantome. Sur les series (i) + (iii)
restreintes a k = -5 a 12, la regle 3.11 rend PLATEAU aux quatre
(g, geometrie) et l'accord a la reference tient a 0.0012 au pire,
recalcule par m1 sur les sorties de m2. La tenue du TP est donc
ATTENDUE ; elle doit etre REFAITE par la sonde certifiee dans le run
juge, et son echec garde toute sa force : NON CONCLUANT D'INSTRUMENT,
le fantome n'est pas lu. C'est l'echelle qui a ete reglee sur le
temoin, a taille reelle, par un run qui ne lit rien de l'objet
(candidate 22 du delta 94) ; aucune tolerance ne l'a ete.
tau ne se desserre pas sur les donnees du fantome.'''),

("B6", r'''  MESURE par la sonde, forme F1, r_c = 40, G20 et G30, eta0 = 0.05,
    meme echelle, meme plateau.''',
r'''  MESURE par la sonde, forme F1, r_c = 40, G20 et G30, eta0 = 0.05,
    meme echelle (3.6, dix-huit valeurs), meme plateau.
  ETAT AU 13/11. La reference est faite et certifiee ; la regle
    ci-dessus rend j = 6 (g = 0.08409, Gamma_ref 5.3688e-10, u_ref
    2.1e-03) et j = 8 (g = 0.10000, Gamma_ref 6.4279e-09, u_ref
    1.6e-04). Liste et table sont reprises a l'octet. j = 5 (Gamma_ref
    1.384e-10) reste HORS liste : son u_ref depasse le plafond de
    1.96e-05, et le plafond ne bouge pas (section 14).'''),

("B7", r'''JOUE, consigne au verdict. Les trois candidats sont suivis dans les
MEMES quinze decompositions, jouees a l'etage 1 et propres au TN :
aucune valeur de l'etat d'ile n'y est relevee.''',
r'''JOUE, consigne au verdict. Les trois candidats sont suivis dans les
MEMES dix-huit decompositions, jouees a l'etage 1 et propres au TN :
aucune valeur de l'etat d'ile n'y est relevee.
  ATTENDU A TAILLE REELLE : TN NON JOUE. Le 12/11 aucun des trois
  candidats n'a ete suivi de k = 3 a k = 2 ni a k = 4 (recouvrements
  0.766 a 0.884, sous 0.90 : D-QEB-3 du delta 94). Le TN est garde TEL
  QUEL -- le changer serait une seconde difference -- et sa limite est
  declaree en section 14. EN CONSIGNE, sans effet sur le verdict :
  l'acte releve qu'au TP aucune fenetre de depart k0 >= 4 ne rend
  PLATEAU (la largeur y est proportionnelle a eta, ou sous le
  plancher) ; c'est le seul temoin a taille reelle que le critere mord
  sur une largeur faite par l'absorbeur.'''),

("B8", r'''  (e) CONSIGNE, pas une condition : |ln(G_run / Gamma_pl(F1, G20))|
      <= tau. Sinon : "M17 a lu hors plateau a ce point".''',
r'''  (e) CONSIGNE, pas une condition : |ln(G_run / Gamma_pl(F1, G20))|
      <= tau. Sinon : "M17 a lu hors plateau a ce point".
      Le depart k0 de la fenetre retenue est consigne a chaque
      configuration ; "la fenetre retenue contient k = 3", le barreau
      de lecture de M17, se lit de k0 : -1 <= k0 <= 3.'''),

("B9b", r'''valeurs lisibles seulement -> AUCUNE FENETRE. BORNE, a un ulp de''',
r'''valeurs lisibles seulement -> AUCUNE FENETRE ; plateau des cinq
        barreaux les plus forts (k = -5 a -1) puis chute -> PLATEAU,
        k0 = -5 (ce cas mord sous l'echelle du gel v2). BORNE, a un ulp de'''),

("B9a", r'''trajectoires F1 180 (6 x 2 x 15), formes 180 (6 x 2 x 15), translation
90 (6 x 15), plancher 30 (6 x 5), TP au plus 60 (2 x 2 x 15), TN 15
(E-EB-2 ; un seul jeu de quinze pour les trois candidats, 5.2) : au
plus 555. Hors de ce compte, et declarees comme telles : les
decompositions a geometrie reduite du banc qui tue, et celles du script
de reference de m2.''',
r'''trajectoires F1 216 (6 x 2 x 18), formes 216 (6 x 2 x 18), translation
108 (6 x 18), plancher 30 (6 x 5), TP 72 (2 x 2 x 18), TN 18 (un seul
jeu de dix-huit pour les trois candidats, 5.2) : 660, dont 120 a
l'etage 1 et 540 a l'etage 2. Hors de ce compte, et declarees comme
telles : les decompositions a geometrie reduite du banc qui tue. La
reference de m2 est deja faite.'''),

("B11", r'''  A-1  verdict : QUALIFIE PAR POINT 0.5 ; ESTIMATEUR QUALIFIE 0.3 ;
       NON QUALIFIE 0.1 ; NON CONCLUANT D'INSTRUMENT 0.1.
  A-2  2.02 n'est pas QUALIFIE : 0.6 (le dernier pas du run y est plus
       grand que le precedent).
  A-3  la famille de droite (2.02, 2.03, 2.05) compte au moins autant
       de points QUALIFIES que celle de gauche : 0.65 (base propre
       presque orthogonale a droite, poids total 0.998 contre 0.85).
  A-4  T-etats : FLUCTUATION D'ETAT DOMINANTE : 0.7.
  A-5  kappa de l'etat retenu : plus petit des trois de gauche > plus
       grand des trois de droite : 0.6.''',
r'''  Les annonces du gel v2 n'ont pas ete jugees sur le fantome (etage 2
  non joue) ; son A-1 portait 0.1 sur l'issue du 12/11. Celles-ci les
  remplacent. La feuille compte A-1 a A-5 ; A-6 a A-8 se comptent a
  l'acte.
  A-1  verdict : QUALIFIE PAR POINT 0.50 ; NON QUALIFIE 0.27 ;
       ESTIMATEUR QUALIFIE 0.13 ; NON CONCLUANT D'INSTRUMENT 0.07 ;
       NON LISIBLE 0.03.
  A-2  2.02 n'est pas QUALIFIE : 0.6 (reconduite ; le dernier pas du
       run y est plus grand que le precedent).
  A-3  la famille de droite (2.02, 2.03, 2.05) compte au moins autant
       de points QUALIFIES que celle de gauche : 0.5 (ramenee de 0.65 :
       le premier pas de descente du run vaut 0.090 et 0.115 a 2.02 et
       2.03, 0.026 au plus aux quatre autres points).
  A-4  T-etats : FLUCTUATION D'ETAT DOMINANTE : 0.7. NON AVEUGLE
       (D-QEB-1 du delta 94) : comptee, non creditee.
  A-5  kappa de l'etat retenu : plus petit des trois de gauche > plus
       grand des trois de droite : 0.6. NON AVEUGLE (D-QEB-1) :
       comptee, non creditee.
  A-6  le TP tient : 0.93. NON AVEUGLE (temoin regle, section 4).
  A-7  a (F1, G20), a tout point qui a un PLATEAU, la fenetre retenue
       ne commence pas avant k = -1 (k0 >= -1) : 0.7. Raison : l'etat
       du fantome s'etend jusqu'au bord r_c, celui du temoin non ; un
       absorbeur fort doit deplacer le premier et laisser le second.
  A-8  la consigne 6 (e) tient a tout point qui a un PLATEAU a
       (F1, G20) : 0.55.'''),

("B12a", r'''COUT (estimation, loi cubique sur la mesure 93 a 94 s par
decomposition a N = 70 du delta 80) : etage 1 de l'ordre de 2 a 3 h,
reference comprise si m2 la balaie d'abord grossierement (un theta,
N = 50) avant de raffiner ; etage 2 environ 8 h 30 ; une nuit de BOCAL4.''',
r'''COUT (sur les durees mesurees a BOCAL4 la nuit du 12/11 : 30.1 s par
decomposition a N = 60, 68.2 s a N = 70) : etage 1 environ 1 h 30,
etage 2 environ 7 h ; une nuit de BOCAL4. Aucune reference a refaire.'''),

("B12b", r'''en (F1, G20) sur l'echelle entiere (15 decompositions), compare a
BOCAL4 a 1e-3, avec le levier NPY_DISABLE_CPU_FEATURES. Le reste n'est
pas rejoue par m1 : repetition non opposable.''',
r'''en (F1, G20) sur l'echelle entiere (18 decompositions), compare a
BOCAL4 a 1e-3, avec le levier NPY_DISABLE_CPU_FEATURES, et seulement
APRES un etage 1 qui tient. Le reste n'est pas rejoue par m1 :
repetition non opposable.'''),

("B12c", r'''GARDE-FOU (proposition de la plume, sous le veto de l'operateur) : un
gel, UN tour de correction,
un run, un acte. Si le TP ne qualifie pas l'instrument apres ce
tour, on l'ecrit et on s'arrete. Aucun rejeu des donnees du fantome sous
d'autres seuils.''',
r'''GARDE-FOU : un gel, UN tour de correction, un run, un acte, et c'est
le DERNIER ESSAI de la piste (0) sous cette forme. Ce sont les trois
conditions de m1 au delta 94, nn.10 (iv) : l'acte d'abord (fait), une
seule difference de fond (3.6), dernier essai. Quelle que soit l'issue
-- y compris un TP qui ne tiendrait pas -- on l'ecrit et on s'arrete :
ni troisieme gel, ni autre echelle, ni autre temoin. L'operateur peut
lever ce garde-fou ; les machines, non. Aucun rejeu des donnees du
fantome sous d'autres seuils.'''),

("B13a", r'''  ESTIMATEUR QUALIFIE : Gamma_LS est une largeur sortante, citable avec
      sa valeur et son etalement ; "PAS DE SIGNAL" de M17 reste, comme
      reponse a une question de rang. Suite PROPOSEE : le plancher en
      g (c de juillet) remesure avec cet instrument, puis sa
      derivation.''',
r'''  ESTIMATEUR QUALIFIE : aux six points il existe une largeur sortante,
      citable avec sa valeur Gamma_pl et son etalement. Ce que cela
      engage pour les nombres de M17 depend de la consigne 6 (e) : la
      ou elle tient, la valeur lue par M17 (G_run) est citable et vaut
      Gamma_pl a tau pres ; la ou elle ne tient pas, M17 a lu hors
      plateau, G_run n'est pas citable et c'est Gamma_pl qui l'est.
      "PAS DE SIGNAL" de M17 reste, comme reponse a une question de
      rang, SI la consigne tient aux six points ; sinon la question de
      rang est a reposer sur les Gamma_pl, hors de ce gel. Suite
      PROPOSEE : le plancher en g (c de juillet) remesure avec cet
      instrument, puis sa derivation.'''),

("B13b", r'''  QUALIFIE PAR POINT : seules les largeurs des points listes sont
      citables ; aucune phrase de grille.''',
r'''  QUALIFIE PAR POINT : seules les largeurs des points listes sont
      citables, avec la meme distinction entre Gamma_pl et G_run ;
      aucune phrase de grille.'''),

("B14", r'''un TP tenu ne prouve pas que la methode vaut pour lui, il prouve
qu'elle sait mesurer une largeur connue.''',
r'''un TP tenu ne prouve pas que la methode vaut pour lui, il prouve
qu'elle sait mesurer une largeur connue.

Limites propres a cette reprise. (1) Le TP est REGLE (section 4) : sa
tenue ne dit plus que l'instrument est juste a un reglage choisi a
l'aveugle ; elle verifie que la sonde certifiee refait ce que le
diagnostic a vu. (2) Le plus bas temoin est a 5.369e-10 ; cinq des six
largeurs lues par M17 sont en dessous, d'un facteur 2.5 a 8.2. Le TP
qualifie la METHODE a 5e-10 et 6e-09 ; c'est la garde G-Q5 -- au plus
1.330e-13 le 12/11 -- qui porte la PRECISION numerique a l'echelle de
7e-11, pas le temoin. j = 5 n'est pas ajoute : il faudrait ou relever
le plafond de u_ref sur une valeur vue, ou refaire et recertifier la
reference, et ce serait une seconde difference. (3) Au barreau k = 3,
celui ou M17 lit, le temoin est HORS de son palier a G20 (0.435 et
0.422 de la largeur connue) et la porte de descente de M17 y refuse le
temoin : le palier du temoin et le point de lecture de M17 ne
coincident pas. Rien n'en est deduit pour le fantome ; la consigne
6 (e) est la pour le lire. (4) Le TN est attendu NON JOUE (5.2) : le
critere n'a de temoin negatif a taille reelle que la consigne sur les
barreaux faibles du TP.'''),
]

# la section 15 est remplacee en bloc : de son titre a la derniere ligne avant le terminateur
DEBUT15, FIN15 = "## 15. Journal v1 -> v2 (certification m2 du 11/11, lot 113e5b84238203de)", "\n\n-- FIN --\n"
S15 = r'''## 15. Journal gel v2 -> gel bis v1

Le journal v1 -> v2 du gel v2 se lit dans le gel v2, au registre ; il
n'est pas recopie. Ce gel = gel v2 (cde0cd11a763f26d) + les hunks
ci-dessous, a ancre unique (script de construction et diff joints).
DIFFERENCE DE FOND, une seule :
  B3    3.6 : l'echelle passe de k = -2 a 12 a k = -5 a 12.
CONSEQUENCES de B3, sans choix :
  B7    5.2, premiere phrase : le jeu du TN passe a dix-huit.
  B9a   8 : decompte 660 (120 + 540) au lieu de 555.
  B9b   8 : G-Q7 gagne un cas, le plateau au bord fort.
  B12a  12 : cout, sur les durees mesurees.
  B12b  12 : rejeu de m1 a dix-huit decompositions, apres l'etage 1.
ETAT DES LIEUX, rien qui touche un statut :
  B0, B1  titre et statut : nouveau gel, reprise, dernier essai.
  B2a   2 : gel v2, delta 94, la nuit, la reference reprise, le
        diagnostic, le registre a fe10bfe.
  B2b   2 : le lot de l'etape 0 est au registre.
  B5    4 : ce que la plume a vu ; le TP est un temoin regle.
  B6    5.1 : les deux couplages retenus, nommes ; j = 5 hors liste.
  B7    5.2, suite : le TN est attendu NON JOUE ; consigne sur les
        barreaux faibles du TP.
  B11   11 : annonces refaites.
  B12c  12 : garde-fou, dernier essai.
  B14   14 : quatre limites propres a la reprise.
PRECISIONS, sans effet sur un statut :
  B8    6 (e) : k0 consigne ; "la fenetre contient k = 3" s'en lit.
  B13a, B13b  13 : ce que QUALIFIE engage pour les nombres de M17,
        selon la consigne 6 (e) -- question de m2 (note du diagnostic,
        3 (c)).
  B15   cette section.
INSTRUMENT (hors gel, pour memoire). Sonde v3 = v2 + l'echelle et ses
comptes. Feuille v2 = v1 + les bornes de fenetre, le cas de G-Q7 et
deux refus a l'entree : gel de la sortie different du sien ; g de la
sonde different du g de la table (observation O-2 de m2). Banc v3 =
v2 + l'echelle de ses series.
NON PRIS. L'echelle decalee k = -6 a 8, d'abord proposee par m1 : elle
retirait quatre barreaux du gel v2, donc deux differences au lieu
d'une, et reglait l'echelle du fantome sur le cote faible du temoin.
j = 5 (section 14). Tout changement du TN.
Aucune tolerance ne change : tau, 0.90, 1e-12, tau_TP, la fenetre de
cinq, le plafond de u_ref, la selection des couplages.'''

# ---------------------------------------------------------------- les nombres tapes, affirmes contre leurs sources
s1 = json.load(open(NUIT))
bal = {r["j"]: r for r in json.load(open(TABLE))["balayage"]}
diag = {g: json.load(open(os.path.join(DIAG, "diag_%s.json" % g), encoding="utf-8")) for g in ("G20", "G30")}
e0 = json.load(open(E0))
assert sum(len(v) for v in diag.values()) == 20 and {r["k"] for v in diag.values() for r in v} == {-6, -5, -4, -3, -2}


def serie(j, g):
    tr = s1["TP"]["j%02d" % j]["traj"]["F1" + g]
    s = {}
    for k in range(-2, 13):
        e = tr[str(k)]["etats"][0]
        s[k] = e["gamma"] if e["suivi"] and e["gamma"] > 1e-12 else None
    for r in diag[g]:
        if r["j"] == j and -5 <= r["k"] < -2:
            s[r["k"]] = r["gamma"]
    return s


pire = 0.0
for j in (6, 8):
    for g in ("G20", "G30"):
        s, best = serie(j, g), None
        for k0 in range(-5, 9):
            v = [s[k] for k in range(k0, k0 + 5)]
            if any(x is None for x in v):
                continue
            mx, mn = Fraction(max(v)), Fraction(min(v))
            c = (not (mx <= Fraction(21, 20) * mn), mx / mn, k0, math.exp(sum(math.log(x) for x in v) / 5))
            best = c if best is None or c[:3] < best[:3] else best
        assert best[0] is False, (j, g)
        ec = abs(math.log(best[3] / bal[j]["Gamma_ref"]))
        assert ec <= 0.05 + bal[j]["u_ref"]
        pire = max(pire, ec)
        for k0 in range(4, 9):                              # consigne de B7 : aucune fenetre de depart k0 >= 4 ne rend PLATEAU
            v = [s[k] for k in range(k0, k0 + 5)]
            assert any(x is None for x in v) or Fraction(max(v)) > Fraction(21, 20) * Fraction(min(v)), (j, g, k0)
assert "%.4f" % pire == "0.0012", pire
assert sum(len(s1["TP"][c]["traj"][f]) for c in s1["TP"] for f in s1["TP"][c]["traj"]) == 60
assert ("%.5f" % bal[6]["g"], "%.4e" % bal[6]["Gamma_ref"], "%.1e" % bal[6]["u_ref"]) == ("0.08409", "5.3688e-10", "2.1e-03")
assert ("%.5f" % bal[8]["g"], "%.4e" % bal[8]["Gamma_ref"], "%.1e" % bal[8]["u_ref"]) == ("0.10000", "6.4279e-09", "1.6e-04")
assert ("%.3e" % bal[5]["Gamma_ref"], "%.2e" % (bal[5]["u_ref"] - 0.01)) == ("1.384e-10", "1.96e-05")
assert ("%.3e" % bal[6]["Gamma_ref"], "%.0e" % bal[6]["Gamma_ref"], "%.0e" % bal[8]["Gamma_ref"]) == ("5.369e-10", "5e-10", "6e-09")
ov = [e["ov"] for k in ("2", "4") for e in s1["TN"]["traj"][k]["etats"]]
assert ("%.3f" % min(ov), "%.3f" % max(ov)) == ("0.766", "0.884") and not any(
    e["suivi"] for k in ("2", "4") for e in s1["TN"]["traj"][k]["etats"])
PT = ["1.95", "1.97", "1.98", "2.02", "2.03", "2.05"]
p1 = {w: e0["points"][w]["essais"][0]["pas"][0] for w in PT}
assert ("%.3f" % p1["2.02"], "%.3f" % p1["2.03"]) == ("0.090", "0.115")
assert "%.3f" % max(p1[w] for w in PT if w not in ("2.02", "2.03")) == "0.026"
assert e0["points"]["2.02"]["essais"][0]["pas"][2] > e0["points"]["2.02"]["essais"][0]["pas"][1]
G = [e0["points"][w]["G"] for w in PT]
sous = sorted(bal[6]["Gamma_ref"] / x for x in G if x < bal[6]["Gamma_ref"])
assert len(sous) == 5 and ("%.1f" % sous[0], "%.1f" % sous[-1]) == ("2.5", "8.2") and "%.0e" % min(G) == "7e-11"
assert "%.3e" % max(abs(x) for d in s1["GQ5"].values() for x in d.values()) == "1.330e-13"
k3 = [s1["TP"][c]["traj"]["F1G20"]["3"]["etats"][0]["gamma"] / bal[j]["Gamma_ref"] for c, j in (("j06", 6), ("j08", 8))]
assert ["%.3f" % x for x in k3] == ["0.435", "0.422"]
dur = {f: [r["duree_s"] for c in s1["TP"] for r in s1["TP"][c]["traj"][f].values()] for f in ("F1G20", "F1G30")}
assert ("%.1f" % (sum(dur["F1G20"]) / 30), "%.1f" % (sum(dur["F1G30"]) / 30)) == ("30.1", "68.2")
n = 18
assert (6 * 2 * n, 6 * n, 2 * 2 * n, n, 6 * 5) == (216, 108, 72, 18, 30)
assert (2 * 2 * n + n + 30, 2 * (6 * 2 * n) + 6 * n, 2 * 2 * n + n + 30 + 2 * (6 * 2 * n) + 6 * n) == (120, 540, 660)
assert abs(math.log10(2.0 ** 17) - 5.1) < 0.05 and (2 ** 5, 2 ** 4, 2 ** 3) == (32, 16, 8)
t1h = (36 * 30.1 + 36 * 68.2 + 18 * 30.1 + 18 * 30.1 + 12 * 68.2) / 3600.0      # TP, TN au plus, plancher
t2h = (324 * 30.1 + 216 * 68.2) / 3600.0
assert 1.4 < t1h < 1.8 and 6.5 < t2h < 7.1, (t1h, t2h)
# les pieces citees par leur canon sont bien celles-la
for chemin, att in ((REG + "/gels/qualification_EB_pre_enregistrement_v2.md", "cde0cd11a763f26d"),
                    (REG + "/journal/journal_delta_94_qualification_EB_v2.md", "569ccbd0d1adb927"),
                    (NUIT, "ab31334aea5c444a"), (TABLE, "4d51dd58ef456fe9"),
                    (os.path.join(os.path.dirname(TABLE), "tp_retenus_machine2_v1.json"), "69b3bab3bb8480b7"),
                    (os.path.join(os.path.dirname(DIAG), "MANIFEST_lot_machine2_diagnostic_TP_echelle_forte_v1.txt"), "762a89e8ad7d498a"),
                    (REG + "/journal/lecture_predeclaree_piste0_etape0_machine1_v1.md", "20cbc762d58ce1ca")):
    assert cB(chemin) == att, (chemin, cB(chemin))
man = [f for f in os.listdir(REG + "/journal") if f.startswith("MANIFEST_lot_")]
assert any(cB(os.path.join(REG, "journal", f)) == "72f65ad8a898fbb5" for f in man)
assert any(cB(os.path.join(REG, "journal", f)) == "7b64b1b7d86c0591" for f in man)
dire("nombres tapes dans les hunks : affirmes contre la nuit, la table, le diagnostic, l'etape 0 et le registre")

# ---------------------------------------------------------------- la construction
v2 = open(REG + "/gels/qualification_EB_pre_enregistrement_v2.md", encoding="ascii").read()
t = v2
for h, vieux, neuf in H:
    assert t.count(vieux) == 1, "%s : ancre trouve %d fois" % (h, t.count(vieux))
    t = t.replace(vieux, neuf)
    dire("  %-5s %4d -> %4d caracteres ; ancre %r" % (h, len(vieux), len(neuf), vieux.split("\n")[0][:46]))
assert t.count(DEBUT15) == 1 and t.endswith(FIN15)
i = t.index(DEBUT15)
dire("  %-5s %4d -> %4d caracteres ; section 15 remplacee en bloc" % ("B15", len(t) - len(FIN15) - i, len(S15)))
t = t[:i] + S15 + FIN15
noms = [h for h, _, _ in H] + ["B15"]
for h in set(noms):                                  # le journal de la section 15 nomme chaque hunk, et rien d'autre
    assert re.search(r"(?m)^  (?:B\d+[a-c]?, )?%s[ ,]" % h, S15), h
assert set(re.findall(r"\bB\d+[a-c]?\b", S15)) == set(noms)
assert max(len(l) for l in t.split("\n")) <= max(len(l) for l in v2.split("\n")), [l for l in t.split("\n") if len(l) > 79]
o = t.encode("ascii")
assert b"%" not in o and b"\t" not in o and not any(l != l.rstrip() for l in t.split("\n"))
open(SORTIE, "wb").write(o)
dire("remplacements : %d (+ la section 15) ; gel bis v1 : canon %s, %d o, %d lignes ; gel v2 : %d o, %d lignes" % (
    len(H), cB(SORTIE), len(o), t.count("\n"), len(v2), v2.count("\n")))
dire("-- FIN construction_gel_EB_bis_machine1_v1 --")
