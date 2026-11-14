# -*- coding: ascii -*-
# CONSTRUCTION DE L'ACTE DE LA QUALIFICATION E-B BIS, PROJET v2 = PROJET v1 + HUIT HUNKS A ANCRE UNIQUE.
# machine 1, 2026-11-13. Repond au contreseing de machine 2 (lot 05f8eed219631f63) : M-1, R-1, R-3.
# Arguments : <acte v1> <acte v2 a ecrire> <diff a ecrire>.  Aucun nombre mesure de la v1 n'est touche.
import sys, hashlib, unicodedata, difflib
V1, V2, DIFF = sys.argv[1:4]
CANON_V1 = "c396a00095a0b9e3"
def canon(t):
    return hashlib.sha256(unicodedata.normalize("NFC", t).replace("\r\n", "\n").encode("utf-8")).hexdigest()[:16]
t = open(V1, encoding="ascii", newline="").read()
assert canon(t) == CANON_V1, "la v1 lue n'est pas au canon"
HUNKS = [
 ("H1 forme, version",
  "-- PROJET, VERSION 1\n",
  "-- PROJET, VERSION 2\n"),
 ("H2 M-1, nn.4",
  "  jointe, non citee). Rien d'autre.\n",
  "  jointe, non citee). Apres la nuit, et apres la remise du projet v1 de cet acte a l'operateur,\n"
  "  machine 1 a joue aussi, hors chaine, classe 3, post hoc, une plume, non contresigne : des\n"
  "  diagonalisations du H 2D aux six points de M17 (lot 2b211d51fb8eb3f0) et une seconde note de\n"
  "  lecture avec son jouet (lot e58d01567a46b86a, qui porte aussi la note de litterature de la\n"
  "  nuit). Ces calculs ne relisent aucun fichier de sortie de la nuit ; ils en reprennent un nombre,\n"
  "  le plancher du jumeau 1.330e-13 (nn.5), comme seuil de lecture (dix planchers), et la note du\n"
  "  premier lot cite le verdict de la nuit. L'acte n'en tire rien.\n"),
 ("H3 R-1, nn.7 (d)",
  "      separent ensuite : a k = 4, de 0.011 a 0.097. G30 a un plateau a cinq points, G20 a un seul.\n",
  "      separent ensuite : a k = 4, de 0.011 a 0.097 (ecarts lus comme |G20/G30 - 1|). G30 a un\n"
  "      plateau a cinq points, G20 a un seul.\n"),
 ("H4 R-3, nn.10 O-BIS-2",
  "    sur le meme code. Cause non recherchee. L'essai a blanc de machine 1 joint au lot du gel bis,\n"
  "    fait sur les valeurs du diagnostic, donnait |ln| <= 0.0012 ; le run donne 0.0015. Sans effet :\n"
  "    le seuil est a plus de 0.05.\n",
  "    sur le meme code. Cause trouvee par machine 2 (lot du contreseing 05f8eed219631f63) : le nombre\n"
  "    de fils BLAS. Sur la meme matrice, 16 fils (defaut) rendent la valeur de la sonde, 4 fils celle\n"
  "    du diagnostic, a treize chiffres ; 2 fils en rendent une troisieme. Machine 1 a lu les deux\n"
  "    journaux et retrouve les deux valeurs dans ses copies de la sonde et du diagnostic ; elle n'a\n"
  "    pas rejoue. L'essai a blanc de machine 1 joint au lot du gel bis, fait sur les valeurs du\n"
  "    diagnostic, donnait |ln| <= 0.0012 ; le run donne 0.0015. Sans effet : le seuil est a plus de\n"
  "    0.05.\n"),
 ("H5 M-1, nn.14",
  "  a01598ec24237921. Machine 1 -- gel bis et instrument 25276846153bacff ; cet acte. Le lot de\n",
  "  a01598ec24237921. Machine 1 -- gel bis et instrument 25276846153bacff ; cet acte. Depuis le\n"
  "  projet v1, le 13/11 : machine 1, hors chaine, remis a l'operateur -- la chaine E-A par etat\n"
  "  2b211d51fb8eb3f0, l'envoi et les notes de lecture e58d01567a46b86a ; machine 2 -- contreseing du\n"
  "  projet v1 05f8eed219631f63, rejeu hors chaine de la chaine E-A df01461fc9b2b099. Le lot de\n"),
 ("H6 forme, nn.16 nom de l'acte",
  "  journal_delta_nn_qualification_EB_bis_v1.md           cet acte\n",
  "  journal_delta_nn_qualification_EB_bis_v2.md           cet acte\n"),
 ("H7 forme, nn.16 paragraphe de version",
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.\n",
  "  Version 2 : le projet v1 (c396a00095a0b9e3) plus huit hunks poses par\n"
  "  construction_acte_qualification_EB_bis_v2_machine1_v1.py ; quatre repondent au contreseing de\n"
  "  machine 2 (M-1 en nn.4 et nn.14, R-1 en nn.7, R-3 en nn.10), quatre sont de forme (version,\n"
  "  nom de l'acte, ce paragraphe, ligne de fin). Le diff et le releve de la v2 sont au lot de la v2 ;\n"
  "  les autres pieces ci-dessus sont celles du lot ff93d708547f8ec0, inchangees.\n"
  "  Perimetre : la feuille du contresignataire, sur ce texte ; les entrants sont ceux de nn.1.\n"),
 ("H8 forme, ligne de fin",
  "-- FIN journal_delta_nn_qualification_EB_bis_v1 --",
  "-- FIN journal_delta_nn_qualification_EB_bis_v2 --"),
]
u = t
for nom, vieux, neuf in HUNKS:
    assert t.count(vieux) == 1, "ancre non unique dans la v1 : " + nom
    assert u.count(vieux) == 1, "ancre non unique en cours : " + nom
    u = u.replace(vieux, neuf)
assert all(ord(c) < 128 for c in u) and "%" not in u, "ASCII ou pour cent"
long_ = [i + 1 for i, l in enumerate(u.split("\n")) if len(l) > 100]
assert not long_, "lignes de plus de 100 colonnes : %s" % long_
open(V2, "w", encoding="ascii", newline="\n").write(u)
d = list(difflib.unified_diff(t.splitlines(), u.splitlines(), "journal_delta_nn_qualification_EB_bis_v1.md",
                              "journal_delta_nn_qualification_EB_bis_v2.md", lineterm="", n=1))
open(DIFF, "w", encoding="ascii", newline="\n").write("\n".join(d) + "\n")
blocs = sum(1 for l in d if l.startswith("@@"))
print("v1 %s (%d lignes) -> v2 %s (%d lignes, %d octets) ; %d hunks poses ; %d blocs au diff ; lignes -%d +%d" % (
    CANON_V1, len(t.split("\n")) - 1, canon(u), len(u.split("\n")) - 1, len(u.encode()), len(HUNKS), blocs,
    sum(1 for l in d[2:] if l.startswith("-")),      # l'en-tete s'exclut par position (D-CERT-5) :
    sum(1 for l in d[2:] if l.startswith("+"))))      # la ligne de FIN commence par "--"
