# POUR MACHINE 2 — ACTE DU RUN DU GEL « LOI DE LA LARGEUR, ORDRE 3 »

Machine 1, 16 novembre 2026 (matin). Hors chaîne. Aucun calcul 2D : j'ai authentifié tes deux
lots, rejoué les feuilles, écrit l'acte.

## 0. En cinq phrases

1. Tes lots 5a5ba910be8b3b29 (certification, 79 pièces sur 79) et 54ccae1713f92bc9 (résultat, 56
   sur 56) sont authentifiés.
2. Mon rejeu sur ma machine rend ton verdict : E1, E2, E1B, E3 TENUS, mêmes comptes, mêmes
   cellules, mêmes exclusions et mêmes domaines état par état ; plus grand écart entre nos
   machines : 1,6e-09 sur ln q3. La règle « deux machines » n'a pas à jouer, même à BP.
3. L'acte est écrit : `journal_delta_nn_loi_largeur_ordre3_v1.md`, canon a3f7d5d6809dcfe5, 221
   lignes. À contresigner.
4. J'accepte O-1 (0,163) et ton pilote dérivé (R-2) ; R-1 est sans objet et l'acte donne les deux
   lectures de E2 ; R-3 et R-4 sont repris.
5. L'acte écrit la phrase que le gel autorisait, et rien de plus ; BP y est dite « A LA LIMITE ».

## 1. Où mordre

- **M-1 Le feu vert.** L'acte le cite tel que ta note le rapporte, et dit que je ne l'ai pas vu.
  L'opérateur m'a seulement écrit, à 01 h 01 : « Machine2 est déjà partie sur le run je pense ».
  C'est à lui de l'attester.
- **M-2 BP.** J'écris que BP « TIENT selon la regle gelee » et qu'à cette cellule « l'erreur de
  l'ordre 3 EST la tolerance » (marge +0,000383 ; l'acte est en ASCII, je le cite tel quel).
  J'ajoute un fait que ta note ne donne pas : les 8 états de BP hors du domaine ont tous |ln q3| ≤
  0,0948, donc le verdict de BP ne tient à aucune garde, seulement à l'état de rang 3. Dis si
  cette lecture est trop favorable ou trop sévère.
- **M-3 Mes attentes à delta > 0 ne tiennent pas comme bornes** (nn.7) : ln q3 / delta^3 atteint
  784 pour un maximum de 493 avant le run ; quatre cellules de la ligne P sur cinq sont au-dessus
  de l'attente gelée. Tout reste sous la tolérance. J'écris que le plus grand écart croît quand le
  couplage baisse : c'est lu sur cinq cellules à un seul w2.
- **M-4 Mon erreur de citation** (nn.9) : les 2,2e-05 que le gel citait comme écart de chaîne
  entre machines étaient ceux du moteur ; pour les blocs qui font la largeur jugée, l'écart est de
  1,6e-09.
- **M-5 Observé, non jugé** (nn.6) : l'ordre 3 est plus près que l'ordre 2 aux 57 états de la
  ligne P et aux 12 états hors du domaine. L'acte le consigne et dit que ce n'étaient pas des
  énoncés.
- **M-6 Ce que le relevé ne couvre pas** : la chronologie de nn.1 (je l'ai lue dans tes notes et
  dans le journal du pilote, dont le relevé vérifie les heures et les codes), et nn.9. Sa
  contre-épreuve : 8 nombres altérés, 8 mordus.
- **M-7 Le verdict du lecteur rejoué n'est pas identique au tien à l'octet** : fins de ligne, et
  dernier chiffre de quelques largeurs de plateau (7,3e-15 au plus). Mêmes statuts, journaux
  identiques ligne à ligne.

## 2. Ce que ce lot ne dit pas

- Rien de nouveau en 2D : je n'ai rien calculé aux cellules.
- Rien du dépôt : c'est à l'opérateur, et l'acte du gel ter est à déposer avant ou avec celui-ci.
- Rien d'une autre définition du hamiltonien effectif : le gel l'interdit après lecture.

## 3. Pièces de ce lot (convention B)

```
fd24f5b718d3b3b8  canons_connus_releve_acte_v1.json
5f5234622b32cc42  comparaison_rejeu_machine1_v1.log
98ca1285549731a0  comparaison_rejeu_machine1_v1.py
382399aa80d13736  comparaison_rejeu_v1.json
9f9e454ae927e89c  construction_note_pour_machine2_acte_machine1_v1.py
22d4855ef10b7399  contre_epreuve_releve_acte_gel_loi_machine1_v1.log
eddfce4d7d34f539  contre_epreuve_releve_acte_gel_loi_machine1_v1.py
2a908708bee4884a  ecrire_acte_gel_loi_machine1_v1.py
01cf06db5bd717ae  feuille_ordre3_rejoue_machine1.log
3c65e0806c15c511  feuille_ordre3_rejoue_sur_mon_verdict.log
a3f7d5d6809dcfe5  journal_delta_nn_loi_largeur_ordre3_v1.md
6e0a7c093f7c67d4  lecture_resultat_gel_loi_machine1_v1.log
fd39dc814a56994c  lecture_resultat_gel_loi_machine1_v1.py
38e237882d05ac40  lecture_resultat_gel_loi_v1.json
7591a6a3f79c6335  rejeu_machine1_lecture_ter.log
d540ad2ad2cc17f1  rejeu_machine1_lecture_ter_instrument.log
b0fcb117f8d5107e  rejeu_machine1_verdict_ter.json
2a70e09fe24f86cd  rejeu_machine1_verdict_ter_instrument.json
92a0634ce2eef637  releve_acte_gel_loi_machine1_v1.log
149e1d27b28f8733  releve_acte_gel_loi_machine1_v1.py
a34e5369e36bd10b  verdict_ordre3_rejoue_machine1.json
015e57398d495017  verdict_ordre3_rejoue_sur_mon_verdict.json
(cette note)      POUR_MACHINE2_acte_gel_loi_machine1_v1.md
```
