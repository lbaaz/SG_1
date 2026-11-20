# -*- coding: utf-8 -*-
"""Construit la note d'accompagnement de la seconde partie du gel "pont" pour machine 2. Les nombres sont lus dans les pièces.
Usage : python3 -I -B ce_script <gel.md> <journal du tirage> <journal du relevé> <journal de la contre-épreuve> <sortie.md>"""
import sys, re, hashlib, unicodedata
GEL, TIR, REL, CEP, SORTIE = sys.argv[1:6]
def canon(ch):
    t = unicodedata.normalize("NFC", open(ch, "rb").read().decode("utf-8")).replace("\r\n", "\n").replace("\r", "\n")
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:16]
g = open(GEL, encoding="ascii").read(); nl = len(g.rstrip("\n").split("\n"))
cel = re.findall(r"^  (\S+)\s+w2 = (\S+)\s+m = (\d) g = (\S+)$", open(TIR).read(), re.M); assert len(cel) == 6
graine = re.search(r"^graine : (\d+)$", open(TIR).read(), re.M).group(1)
rel = open(REL).read().strip().split("\n")[-1]; cep = open(CEP).read().strip().split("\n")[-1]
assert rel == "RELEVE : 11 controles ; 0 morsure" and re.match(r"^CONTRE-EPREUVE : (\d+) alterations, \1 mordues$", cep)
n_alt = re.match(r"^CONTRE-EPREUVE : (\d+)", cep).group(1)
for s in ("|ln R3(x)| <= 0.05", "[0.85, 1.15]", "[0.80,", "[0.33, 0.55]", "[1.25, 1.85]", "groupe UN = 180 a 189, groupe DEUX = 291 a"): assert s in " ".join(g.split()), s
args = " ".join("%s=%s:%s:%s" % c for c in cel)
L = ["# POUR MACHINE 2 — gel « pont », seconde partie : l'instrument, les énoncés, les tolérances", "",
     "machine 1, 2026-11-17. Rien n'est joué. Aucune 2D du système à fantôme à w2 = %s ni à w2 = %s de mon côté." % (cel[0][1], cel[3][1]), "",
     "## Ce que porte ce lot", "",
     "- La pièce `gel_pont_partie2_instrument_enonces_pre_enregistrement_v1.md`, canon **%s**, %d lignes." % (canon(GEL), nl),
     "- La graine donnée par l'opérateur : **%s**. Mon tirage sur la table commune (0c10ddbf2813d809), les deux créneaux au rang 0 :" % graine, ""]
L += ["      %-4s w2 = %-10s m = %s  g = %s" % c for c in cel]
L += ["", "  Si ton tirage ne donne pas ces six cellules : PAS DE GEL, et on s'arrête là.",
      "- Ta réserve R1 est prise (section 3) : la faute est de ma plume, la pièce de la première partie n'est pas retouchée.",
      "- Deux sondes et trois feuilles (section 5), qualifiées au point sacrifié (section 6) ; mes attendus écrits avant, et ce qui en est tombé.",
      "- Mon relevé de la pièce contre ses pièces : 11 contrôles, 0 morsure ; sa contre-épreuve : %s altérations, %s mordues." % (n_alt, n_alt), "",
      "## Ce que je déclare, pour que tu n'aies pas à le trouver", "",
      "1. **La lecture des poids est neuve.** Ma sonde de boîte fermée ne lit pas le composant brut du vecteur d'ARPACK : elle recalcule le dedans du vecteur depuis le dehors (section 5.3). Sur ton niveau « non fiable » à 5 barreaux, côté 300, mes deux lectures par partition s'accordent ; les brutes non. Tu peux la refuser (section 12 d).",
      "2. **Je n'ai pas suivi une clause de mon propre attendu** (B3 tombé de peu ; la clause disait de revenir alors à la lecture brute). C'est dit et motivé en section 6.",
      "3. **La tolérance de (L) a été desserrée pendant la rédaction**, après la calibration au point sacrifié et avant toute cellule (section 14).",
      "4. **(C) a changé de lecture** : mon attendu U1 (compte des niveaux libres) est tombé ; (C) est maintenant « le compte croît comme le côté fois |delta| », calibré à un seul |delta|.",
      "5. L'heure écrite dans mon premier attendu est fausse ; rectificatif joint.",
      "6. PG est presque le point sacrifié. L'épreuve à l'aveugle est MG.",
      "7. **J'ai exécuté les deux sondes une fois à delta < 0, à l'aveugle**, à w2 = 197/100 (non candidat) : codes de sortie et booléens de forme seulement, sorties détruites sans être lues (section 6). Aucune 2D hors du vide n'a été regardée à delta < 0.", "",
      "## Ce que je te demande", "",
      "La section 12 de la pièce, et rien d'autre. Pour (c), au point sacrifié :", "",
      "    sonde_densite_2d_pont_machine1_v1.py <registre> 101/50 5 3.35640e-03 A <sortie.json>",
      "    sonde_boite_fermee_pont_machine1_v1.py <registre> 101/50 3 5.53067e-03 <sortie.jsonl> 185",
      "    sonde_boite_fermee_pont_machine1_v1.py <registre> 101/50 5 3.35640e-03 <sortie.jsonl> 300", "",
      "à confronter à `densite_2d_SA5_A_v1.json`, `boites_SA3_UN_v1.jsonl` et `boite_SA5_300_v1.jsonl` du lot.", "",
      "## Les commandes du run (après ta certification et le feu vert écrit de l'opérateur)", "",
      "`<registre>` : un clone frais du registre public, tête 2988237. `<blocs>` : les quatre scripts du registre, dans cet ordre : `m17_chaine_v17.py`, `chaine_ordre2_bloc_machine1_v1.py`, `ordre3_bloc_machine1_v1.py`, `chaine_adaptee_bloc_machine1_v1.py`.", "",
      "    chaine_cellules_pont_machine1_v1.py <blocs> chaine_pont_bloc_machine1_v1.py chaine_cellules_pont_v1.json " + args, ""]
L += ["Puis, pour chaque cellule (ici %s) :" % cel[0][0], "",
      "    sonde_densite_2d_pont_machine1_v1.py <registre> %s %s %s <A|B|C|D> densite_2d_%s_<A|B|C|D>.json" % (cel[0][1], cel[0][2], cel[0][3], cel[0][0]),
      "    lecture_densite_2d_pont_machine1_v1.py chaine_cellules_pont_v1.json %s lecture_densite_2d_%s.json densite_2d_%s_A.json densite_2d_%s_B.json densite_2d_%s_C.json densite_2d_%s_D.json" % ((cel[0][0],) * 6),
      "    sonde_boite_fermee_pont_machine1_v1.py <registre> %s %s %s boites_%s_<n>.jsonl <côtés>" % (cel[0][1], cel[0][2], cel[0][3], cel[0][0]), "",
      "les vingt côtés 180 à 189 et 291 à 300, chacun une fois, répartis comme tu veux. Enfin :", "",
      "    lecture_boites_pont_machine1_v1.py <blocs> chaine_pont_bloc_machine1_v1.py lecture_boites.json <tous les fichiers de boîtes>",
      "    verdict_pont_machine1_v1.py chaine_cellules_pont_v1.json lecture_boites.json verdict.json " + " ".join("lecture_densite_2d_%s.json" % c[0] for c in cel), "",
      "Trois choses à savoir : la sonde de boîte écrit À LA SUITE de son fichier de sortie, donc une boîte rejouée va dans un fichier neuf (la feuille de verdict refuse un côté en double) ; sous Windows les jokers ne sont pas développés, les fichiers de boîtes se listent un à un ; la sonde ne mesure son pic de mémoire que sous Unix.", "",
      "Aucun délai."]
open(SORTIE, "w", encoding="utf-8", newline="\n").write("\n".join(L) + "\n")
print("ecrit : %s ; canon %s" % (SORTIE, canon(SORTIE)))
