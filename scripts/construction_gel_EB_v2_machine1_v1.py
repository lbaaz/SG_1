# -*- coding: ascii -*-
# Construit le gel E-B v2 depuis le v1 par remplacements a ancre unique.
# Arguments : <gel v1> <gel v2>. Verifie le canon du v1 avant d'ecrire.
import sys, hashlib, unicodedata


def canon_b(octets):
    t = unicodedata.normalize("NFC", octets.decode("utf-8"))
    t = t.replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]


src_o = open(sys.argv[1], "rb").read()
assert canon_b(src_o) == "8603af9d4f63e9dc", "base : ce n'est pas le gel v1"
s = src_o.decode("ascii")
assert 180 + 180 + 90 + 30 + 60 + 15 == 555          # decompte du hunk H10
assert abs((20 - 1) ** 2 / 20 ** 2 - 0.9025) < 1e-15   # M-1 a L = 20
assert abs(6.428e-09 / 1.46e-09 - 4.4) < 0.01          # facteur cite en H5

H = []
# --- H0 / M-4 : version, sens de "titre a terminateur" ---------------------
H.append(("H0 titre",
"# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- v1\n",
"# GEL -- QUALIFICATION DE L'ESTIMATEUR E-B (Gamma_LS) -- v2\n"))
H.append(("H0 section 0 (M-4)",
"""Le numero de version est dans le nom ; l'empreinte est celle du FICHIER
(titre a terminateur, convention B).""",
"""Le numero de version est dans le nom ; l'empreinte est la convention B
du FICHIER ENTIER, de la premiere ligne au saut de ligne final apres le
terminateur -- "titre a terminateur" ne designait rien d'autre (M-4).
v2 = v1 (8603af9d4f63e9dc) + les hunks de la section 15 : c'est LE tour
de correction de la section 12."""))
# --- H12 / M-3 : lot de l'etape 0 joint ------------------------------------
H.append(("H12 section 2 (M-3)",
"""Ce que l'etape 0 a etabli et que ce gel prend pour acquis : aux six
points,""",
"""Le lot de l'etape 0 n'etait pas detenu par m2 au 11/11 (M-3) : il est
JOINT au lot de ce gel. Tout nombre que ce gel en tire se relit dans
les six pieces f070 du run, sans lui.

Ce que l'etape 0 a etabli et que ce gel prend pour acquis : aux six
points,"""))
# --- H4 / M-1 : F2 ---------------------------------------------------------
H.append(("H4 3.4 (M-1)",
"""       (meme valeur que F1 au bord de boite, autre profil).""",
"""       (meme valeur que F1 a la distance L, c'est-a-dire a l'indice N,
        HORS boite ; sur la derniere ligne reelle, distance L - 1, le
        rapport F2 / F1 vaut (L - 1)^2 / L^2 ; autre profil)."""))
# --- H1 / E-EB-1 : plateau en rationnels -----------------------------------
H.append(("H1 3.11 (E-EB-1)",
"""consecutifs (quatre divisions par deux, un facteur 16 en eta). Son
ETALEMENT est e = max(gamma) / min(gamma) - 1. Il y a PLATEAU si une
fenetre a e <= tau. La fenetre retenue est celle d'etalement minimal ;
a egalite, le plus petit k de depart.""",
"""consecutifs (quatre divisions par deux, un facteur 16 en eta). Il y a
PLATEAU si une fenetre verifie, EN RATIONNELS EXACTS,
    Fraction(max) <= (1 + Fraction(1, 20)) * Fraction(min)
(regle 15 ; E-EB-1 : la forme max / min - 1 <= 0.05 est fausse en
flottants a la borne meme). L'ETALEMENT e = max(gamma) / min(gamma) - 1
n'est plus qu'un affichage. La fenetre retenue est celle de plus petit
rapport max / min, compare lui aussi en rationnels ; a egalite, le plus
petit k de depart."""))
H.append(("H2 3.12 (E-EB-1)",
"""3.12 ACCORD entre deux valeurs de plateau : |ln(Gamma_a / Gamma_b)|
<= tau.""",
"""3.12 ACCORD entre deux valeurs de plateau : |ln(Gamma_a / Gamma_b)|
<= tau. Comparaison en flottants : une borne de logarithme n'a pas de
forme exacte ; elle se teste a tau - 1e-6 et a tau + 1e-6 (G-Q7), pas
a la borne."""))
# --- H3 : ce que la plume a vu depuis le v1 --------------------------------
H.append(("H3 section 4 (P-3)",
"""valeurs : aucune issue de ce gel n'est calculable sur ce qui a ete vu.""",
"""valeurs : aucune issue de ce gel n'est calculable sur ce qui a ete vu.
Vu DEPUIS le v1 (note m2 0d11d6866e3c5f37) : un essai de formule de m2
a UN point de l'echelle du TP, g_8 = 0.10, largeur 6.428e-09 par
rotation complexe. Ce n'est pas la reference et aucune valeur de la
sonde n'existe ; la plume connait donc l'ordre de grandeur a ce g."""))
# --- H5 : interface du TP, lecture du WKB ----------------------------------
H.append(("H5a 5.1 interface (P-1)",
"""  Les deux scripts ne lisent pas la sortie l'un de l'autre ; la
  comparaison est faite par la feuille de lecture.""",
"""  INTERFACE (precision du v2). Le script de reference ecrit deux
  fichiers : la LISTE des couplages retenus (j, g), sans aucune
  largeur, et la table des references. La sonde ne lit que la liste ;
  la feuille de lecture seule ouvre la table et fait la comparaison.
  Aucun des deux scripts de mesure ne lit une largeur de l'autre."""))
H.append(("H5b 5.1 WKB (P-3)",
"""  fausse d'un facteur trois, corrigee avant le gel par le calcul.""",
"""  fausse d'un facteur trois, corrigee avant le gel par le calcul.
  L'essai de formule de m2 a g_8 = 0.10 rend 6.428e-09 la ou ce WKB
  rend 1.46e-09 : un facteur 4.4. La fenetre WKB se lit comme un ordre
  de grandeur ; la selection se fait sur la reference seule."""))
# --- H6 / E-EB-2 : le TN, trois candidats, quinze decompositions -----------
H.append(("H6 5.2 (E-EB-2)",
"""proportionnelle a eta). S'il est non lisible, on essaie a + 5 puis
a - 5 ; trois non lisibles : TN NON JOUE, consigne au verdict.""",
"""proportionnelle a eta). S'il est non lisible, on lit le candidat a + 5
puis a - 5 (b = a // 2 a chaque fois) ; trois non lisibles : TN NON
JOUE, consigne au verdict. Les trois candidats sont suivis dans les
MEMES quinze decompositions, jouees a l'etage 1 et propres au TN :
aucune valeur de l'etat d'ile n'y est relevee."""))
# --- H7 / M-2 : G-Q2 par le manifeste --------------------------------------
H.append(("H7 G-Q2 (M-2)",
"""  G-Q2  dossier du run : 36 au canon et a la taille == 36.""",
"""  G-Q2  dossier du run : les 36 LIGNES DU MANIFESTE au canon et a la
        taille == 36. Le compte se fait par le manifeste, jamais par les
        fichiers du dossier ; tout fichier hors manifeste est nomme au
        log, ni ouvert ni compte (M-2 : le dossier de BOCAL4 en a un)."""))
# --- H8 : G-Q4 a l'ouverture de l'etage 2 ----------------------------------
H.append(("H8 G-Q4 (P-2)",
"""        CONSIGNEE : attendue sur BOCAL4 a plateforme inchangee depuis
        le run, non exigee.""",
"""        CONSIGNEE : attendue sur BOCAL4 a plateforme inchangee depuis
        le run, non exigee. Jouee a l'OUVERTURE de l'etage 2 : les six
        decompositions (F1, G20, k = 3) passent avant toute autre."""))
# --- H9 / E-EB-1 : G-Q7 a un ulp de la borne -------------------------------
H.append(("H9 G-Q7 (E-EB-1)",
"""        de cinq puis chute lineaire -> PLATEAU, fenetre nommee ;
        etalement 0.05 exactement -> PLATEAU ; 0.0501 -> PAS ; quatre
        valeurs lisibles seulement -> AUCUNE FENETRE.""",
"""        de cinq puis chute lineaire -> PLATEAU, fenetre nommee ; quatre
        valeurs lisibles seulement -> AUCUNE FENETRE. BORNE, a un ulp de
        part et d'autre, sur des valeurs exactement representables :
        (20.0, 20.25, 20.5, 20.75, 21.0) -> PLATEAU ; la meme avec
        nextafter(21.0, +inf) -> PAS DE PLATEAU. ACCORD et accord au
        TP : |ln| = tau - 1e-6 -> ACCORD ; tau + 1e-6 -> PAS D'ACCORD."""))
# --- H10 / E-EB-2 : decompte par famille -----------------------------------
H.append(("H10 section 8 (E-EB-2)",
"""Decompositions attendues (declarees avant de compter) : trajectoires
F1 180 (6 x 2 x 15), formes 180 (6 x 2 x 15), translation 90 (6 x 15),
plancher 30 (6 x 5), TP au plus 60 : au plus 540.""",
"""Decompositions attendues (declarees avant de compter), par famille :
trajectoires F1 180 (6 x 2 x 15), formes 180 (6 x 2 x 15), translation
90 (6 x 15), plancher 30 (6 x 5), TP au plus 60 (2 x 2 x 15), TN 15
(E-EB-2 ; un seul jeu de quinze pour les trois candidats, 5.2) : au
plus 555. Hors de ce compte, et declarees comme telles : les
decompositions a geometrie reduite du banc qui tue, et celles du script
de reference de m2."""))
# --- H11 : cascade et ordre d'execution ------------------------------------
H.append(("H11a section 9 (P-2)",
"""     tient pas ou est non concluant ; TN rend PLATEAU. Le fantome n'est
     PAS lu (l'etage 2 n'est pas joue si l'etage 1 echoue).""",
"""     tient pas ou est non concluant ; TN rend PLATEAU. Le fantome n'est
     PAS lu : l'etage 2 n'est pas joue si l'etage 1 echoue, et il
     s'arrete a son ouverture si G-Q4 mord."""))
H.append(("H11b section 9 (P-2)",
"""Ordre d'execution : ETAGE 1 = selftest, banc qui tue, TP, TN, G-Q3 a
G-Q5 ; ETAGE 2 = les six points. Reprise par fichier
(point, configuration, k) obligatoire.""",
"""Ordre d'execution : ETAGE 1 = selftest, banc qui tue, TP, TN, G-Q3,
G-Q5 ; la feuille de lecture ecrit le verdict de l'etage 1 ; ETAGE 2 =
les six points, ouvert par G-Q4, et seulement si ce verdict tient.
Reprise par fichier (point, configuration, k) obligatoire."""))
# --- H13 : sonde = mesure, feuille de lecture = jugement -------------------
H.append(("H13 section 12 (P-1)",
"""SONDE (m1) : arguments = moteur, dossier du run, manifeste, sortie ;""",
"""SONDE (m1) : elle MESURE et ne juge pas ; la FEUILLE DE LECTURE (m1)
juge et ne mesure pas (routine de plateau, statuts, cascade, G-Q7).
Sonde : arguments = moteur, dossier du run, manifeste, liste des
couplages retenus, sortie ;"""))
# --- H14 : journal v1 -> v2 ------------------------------------------------
H.append(("H14 section 15",
"""
-- FIN --
""",
"""
## 15. Journal v1 -> v2 (certification m2 du 11/11, lot 113e5b84238203de)

m2 : NON CERTIFIE EN L'ETAT, 21 controles, 2 morsures de description,
quatre demandes. Tout est pris, sans reserve.
  E-EB-1  3.11 en rationnels exacts ; 3.12 dit sa comparaison ; G-Q7
          rebati a un ulp de la borne (H1, H2, H9).
  E-EB-2  le TN entre au decompte par famille ; total 555 et non 585 :
          les trois candidats partagent quinze decompositions (H6, H10).
  M-1     F2 : "a la distance L" (H4).
  M-2     G-Q2 compte par le manifeste (H7).
  M-3     lot de l'etape 0 joint (H12).
  M-4     canons confirmes -- gel v1 8603af9d4f63e9dc, WKB
          3eeb30328f9c542c ; "titre a terminateur" = convention B du
          fichier entier (H0). Faute de transit de la plume : deux
          pieces a plat sans manifeste ; le v2 part en lot.
De la plume, declares, hors demandes de m2 :
  P-1     interface du TP : la sonde ne lit que la liste des couplages
          retenus ; sonde = mesure, feuille de lecture = jugement
          (H5a, H13).
  P-2     G-Q4 a l'ouverture de l'etage 2 ; verdict de l'etage 1 ecrit
          par la feuille de lecture (H8, H11a, H11b).
  P-3     ce que la plume a vu depuis le v1 : l'essai de m2 a g_8
          (H3, H5b).
Aucune tolerance ne change ; aucun nombre mesure ne change ; le
decompte passe de 540 a 555. Formule de rotation complexe : re-derivee
et validee par m2, inchangee.

-- FIN --
"""))

for nom, vieux, neuf in H:
    if s.count(vieux) != 1:
        sys.exit("ancre non unique : %s (%d occurrences)" % (nom, s.count(vieux)))
    s = s.replace(vieux, neuf)
    print("applique : %s" % nom)
o = s.encode("ascii")
assert o.count(b"%") == 0 and s.endswith("-- FIN --\n")
assert max(len(l) for l in s.split("\n")) <= 80
open(sys.argv[2], "wb").write(o)
assert len(H) == 18 and len(set(n.split()[0] for n, _, _ in H)) == 17
print("remplacements appliques : %d == 18 attendus ; hunks nommes : 17 (H0 en porte deux)" % len(H))
print("gel v2 : canon %s, %d o, %d lignes" % (canon_b(o), len(o), s.count("\n")))
