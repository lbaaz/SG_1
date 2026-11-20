# Ecrit la note POUR_MACHINE2 de la premiere partie du gel "pont" ; chaque nombre vient des pieces du lot.
# Usage : python3 -I construction_note_pour_machine2_gel_pont_partie1_machine1_v1.py <dossier des sorties> <texte du gel> <sortie.md> <lisse_chaine_v1.json> <regards_complements_v1.json>
import sys, json, io, hashlib, unicodedata
from fractions import Fraction as F
D, GEL, SORTIE, CHAINE, COMPL = sys.argv[1:6]
CH = json.load(open(CHAINE)); CP = json.load(open(COMPL))
def B(p):
    t = unicodedata.normalize("NFC", open(p, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
T = json.load(open(D + "/eligibilite_pont_MG_PG_v1.json"))
el = {s: [cd for cd in T["creneaux"][s]["candidats"] if cd["eligible"]] for s in ("MG", "PG")}
ine = [cd for cd in T["creneaux"]["MG"]["candidats"] if not cd["eligible"]]
rel = [l for l in open(D + "/releve_gel_pont_partie1_machine1_v1.log") if l.startswith("RELEVE :")][-1].strip()
ce = [l for l in open(D + "/contre_epreuve_releve_gel_pont_partie1_machine1_v1.log") if l.startswith("CONTRE-EPREUVE :")][-1].strip()
t = []; A = t.append
A("# POUR MACHINE 2 -- gel « pont », première partie : la règle de tirage et d'éligibilité, à certifier")
A("")
A("Machine 1, 2026-11-17 (nuit). L'opérateur a écrit « Go rédiger le gel. » (00 h 56), après ma note sur la chaîne d'ordre 3 loin du vide, qui voyage avec ce lot. Aucune 2D à un w2 candidat : tout ce que la pièce calcule est une chaîne.")
A("")
A("## 0. En six phrases")
A("")
A("1. La pièce à certifier est gel_pont_partie1_regle_tirage_pre_enregistrement_v1.md (canon %s, %d lignes). Elle fixe le tirage et l'éligibilité, rien d'autre ; les énoncés viennent après la graine." % (B(GEL), len(open(GEL).read().split("\n")) - 1))
A("2. Deux créneaux (MG, PG : 0.01 < |δ| < 0.02), huit w2 chacun — 1.982 et 2.017, joués par le gel du vide, sont retirés —, trois profondeurs (3, 4, 5 barreaux), soit 48 cellules ; un tirage en donne six.")
A("3. L'éligibilité reprend celle du gel du vide et ajoute deux conditions hors de l'énergie du vide, sur douze écarts : (iv) étendue du lisse d'ordre 3 ≤ 0.03 ; (v) pas de l'ordre 2 à l'ordre 3 ≤ 0.10. Les seuils sont posés après le point sacrifié et avant toute cellule candidate.")
A("4. **La condition (v) trie** : %d w2 du créneau MG tombent (%s) ; il en reste %d sur 8 dans MG et %d sur 8 dans PG. Je n'ai pas retouché le seuil. C'est le point où ta table peut différer de la mienne : dis-le si c'est le cas."
  % (len(ine), ", ".join("%.3f" % float(F(cd["w2"])) for cd in ine), len(el["MG"]), len(el["PG"])))
A("5. Le créneau MG est joué à l'aveugle pour la 2D : rien n'a été regardé à δ < 0, ni boîte fermée ni densité hors du vide. C'est voulu.")
A("6. Mon relevé relit le texte contre les pièces : « %s » ; sa contre-épreuve : « %s »." % (rel, ce))
A("")
A("## 1. Ce que je te demande (section 10 de la pièce)")
A("")
A("- (a) les définitions suffisent-elles sans lire mon code ; (b) ta table des 48 cellules par ta chaîne, densités hors du vide comprises, et la table commune ; (c) ton tirage sur la graine de démonstration ; (d) ton balayage : aucune 2D du système à fantôme à un w2 candidat ; (e) ce que BOCAL4 peut jouer en boîtes fermées jusqu'au côté 300, à 3, 4 et 5 barreaux.")
A("- La densité du 4.5 est une propriété de la matrice : −(1/π) Im[(E − H)⁻¹]₀₀, à E = E_v − x δ. Je la lis par le flux ; ta forme directe lui est égale à %.0e près sur mes pièces." % max(CH["ordres"][o]["direct_contre_flux_max"] for o in "123"))
A("")
A("## 2. Ce que la seconde partie contiendra, pour que tu saches où l'on va")
A("")
A("Trois familles d'énoncés, la cellule pour unité : (L) densité 2D sous absorbeur aux douze écarts contre le lisse d'ordre 3 ; (S) somme des parts en boîte fermée ; (C) croissance du nombre de niveaux avec le côté. Et une question hors verdict : l'excès de la somme (%.3f ± %.3f au point sacrifié), que le lisse n'explique pas. J'écrirai mon instrument de boîte fermée sans recopier le tien, qui reste la seconde feuille." % (CP["E"]["somme"], CP["E"]["erreur"]))
A("")
A("## 3. À l'opérateur")
A("")
A("Attester l'ouverture de 00 h 56. Donner la graine (au moins six chiffres) aux deux machines, après la certification de machine 2 et pas avant.")
io.open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(t) + "\n")
print("note ecrite ; gel %s" % B(GEL))
