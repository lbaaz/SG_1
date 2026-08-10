## 18. PATCHS DE NOTE Q1/Q2/Q3 APPLIQUES (25/07, apres M5)

*Ferme les points 1, 2 et 3 de la liste « Ouverts » du §6. Livrables :
`note_outreach_EN_2026-07-25p.md`, `note_grand_public_FR_2026-07-25p.md`.
Ligne de version inseree dans chaque en-tete (leçon E11) ; sha256 imprime a
la livraison. Script de patch deterministe (`apply_patches.py`, `apply_patches2.py`)
avec assertion d'unicite sur chaque ancre : aucune substitution silencieuse
possible, et le patch est rejouable sur la note d'origine.*

**Q1 — Gamma renomme.** `Gamma` -> `Gamma_st`, « short-time escape rate », dans
l'abstract, le titre et la table de §4(a), le titre de §4(e). Ajout d'un
paragraphe « What Gamma_st is, and is not » (transitoire + palier, pente
tardive/initiale 1/50-1/100, le contre-exemple s=0.5 : 0.82 predit contre 0.994
mesure). « lifetimes tau ~ 1e5 -> 1e2 » -> « 1/Gamma_st spans... , an initial
escape time scale ». Le palier passe en second observable declare NON
box-independant (x1.5-4 de N=48 a 64). §4(e) : `tau ~ 7e5` -> `1/Gamma_0 ~ 7e5`.

**Q1-bis — la convergence non uniforme est PUBLIEE, pas arbitree.** §4(b)(i)
porte desormais le desaccord entre les deux implementations en toutes lettres
(1.10 / 0.95 au-dessus du milieu d'ile ; 2.0 a s=0.9 avec la reserve E10 sur le
critere pre-enregistre Gamma_48/Gamma_72 = 1.39 dans la bande ; 6.2 a s=0.5),
avec la mention « protocol or physics is undecided » (E5 non tranche). Table
revendiquee au-dessus du milieu d'ile, indicative en dessous ; l'EXISTENCE de
la fuite a petit s est explicitement rebasee sur NULL+ et la coquille fixe,
pas sur le taux.

**Q2 — NULL+ entre dans la note**, en nouvelle sous-section **§4(a')** (label
prime choisi expres : aucun renumerotage, la chaine d'errata et le README qui
citent §4(a)/(b)/(c) restent valides). Deux tables : dynamique (1.0e7 / 1.4e4 /
46 / 5.9 + W34, avec l'aveu de la zone grise a s=1.6) et coquille fixe
(7 etats initiaux, 4.7e4 a 1.8e12, croissant avec la profondeur). Null FREE
1.3e-18 cite. Enonce de §8 repris quasi tel quel : separation robuste,
magnitude non convergee au fond, petites boites SURESTIMENT donc taux a petit s
= majorants probables.

**Q3 — recensement harmonise.** 67 etats / min 9.7e-6 / seuil absolu 1e-9 ->
51 etats / min 1.9e-8 / mediane 4.2e-3 en coquille fixe a N=72, **et surtout
critere RELATIF au temoin au lieu d'absolu** : c'est la lecture qui survit au
1.38e-9 releve par le replicateur sur 3/2 (statistique d'extreme). Robustesse
publiee : x2 non monotone sur N=48..72, argmin qui change de N en N, n<=6
identique a tous les chiffres, rationnel w2=2 a 1.5e-7 avec densite /21.
Controle positif 74/74 et 80/80 en table. L'ecart x500 est declare en clair
comme un changement d'observable, pas comme une correction.

**Q0 — provenance.** La disclosure disait « All numerical results come from the
attached bundle » : faux des que les tables de la reimplementation entrent.
Reecrite : exception explicite pour les tables marquees *(reimplementation)*,
mention de la re-derivation de zero et de l'execution croisee sur une 3e machine,
et engagement a publier le desaccord plutot qu'a l'arbitrer.
**A trancher par l'humain : dire ou non que `bundle5.py` est joint au bundle.**
Le texte actuel ne le promet pas.

**Defaut de ma passe 1, rattrape avant livraison (logue, pas efface).** Ma
premiere version du tableau de recensement mettait sous une seule etiquette la
coquille fixe (fantome) et la region hors-bord croissante (NULL+) : **exactement
le defaut d'homogeneite du §11**, reproduit deux sections plus loin. Corrige en
passe 2 par une colonne `region measured` explicite, la comparaison like-for-like
reportee a N=64 sur les deux systemes, et un argument a fortiori (coquille fixe
INCLUSE dans le hors-bord => le temoin borne aussi ses poids de coquille).
Lecon : toute table qui juxtapose fantome et temoin doit porter la definition
de region en colonne, pas en note de bas de page.

**Non fait, volontairement, en attente d'arbitrage :**
1. Reordonner physiquement §4 pour mettre le recensement en tete (fait dans
   l'abstract seulement ; le corps garde l'ordre (a) taux -> (a') controle ->
   (b) fiabilite -> (c) recensement).
2. Note FR §5 : « la note d'archive en avoue cinq [erreurs] » et « refait tourner
   deux fois » sont des chiffres de l'ere bundle 3ter. E1-E15 et la 3e execution
   appartiennent a la seance 5, qui n'est pas dans le bundle joint. Mettre a jour
   supposerait de decider ce que le bundle expedie contient.
3. « six campagnes de tirs » et « deux faux resultats » (FR §5) : idem, sous-estime
   l'etat actuel (7 cadavres, M1-M5), mais decrit fidelement le bundle expedie.
