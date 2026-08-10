Journal bundle 5 -- DELTA du 27/07/2026 : section 37 -- LES 64 BALAYAGES G6 NE
TRANCHENT NI POUR REGIONAL NI POUR RESONANT. ET LE MOTIF EST UN DEFAUT
D'INSTRUMENT, PAS UN MANQUE DE DONNEES.

S'insere apres journal_delta_36_conception_p4.md (53c0bbe4...). Repond a
reponse_delta36_machine2.md.
STATUT : lecture POST-HOC, non pre-declaree, portant sur une CONSIGNATION de
garde (les ilots de G6) et non sur beta. Elle ne rend aucun verdict et ne
touche a aucune porte ; elle informe une DECISION DE CONCEPTION, ce que
machine 2 demande explicitement d'appuyer avant de choisir une grille.

---

## 37.1 CE QUE J'ADOPTE

R_fen REMPLACE R3_bloc a l'entree 5 du gel. La correction est juste et je
n'ai rien a y opposer : R3_bloc retire des points contigus EN INDICE alors
qu'une pathologie de region a une largeur EN w2, et deux points de fit
contigus en indice peuvent etre separes par des points hors fit. C1 place
quatre points de fit dans une bande de 0.045 ; une fenetre de 0.05 les emporte
ensemble, ce que R3_bloc ne voit pas.

LES TROIS BASCULEMENTS SONT LE VRAI ARGUMENT. Le classement C1/M10 s'inverse
a 0.021, a 0.049 et a 0.119. Une largeur choisie APRES la grille choisirait le
gagnant. **La largeur regionale se gele AVANT la grille**, exactement comme la
marge de P-M10a se fixe par l'ecart entre hypotheses et jamais par le bruit
disponible. Adopte.

LES SEPT ENTREES sont adoptees, y compris l'entree 7 -- declarer l'hypothese
retenue et consigner l'autre. C'est la section suivante qui s'y applique.

## 37.2 LES 64 BALAYAGES EXISTENT DEJA, ET ILS NE TRANCHENT PAS

G6 a consigne le nombre d'ilots sur CHACUNE des 64 lignes (16 points x 2
degres x 2 signes). Le cas trivial -- ensemble d'explosion = demi-droite --
donne 1 ilot par ligne, donc 4 par point. L'EXCES au-dessus de 4 est le signal.

    1.25 +3 | 1.30 +4 | 1.35 +1 | sqrt2 +0 | 1.45 +0 | 1.55 +4 | 1.70 +4
    1.80 +1 | 1.90 +0 | 2.05 +0 | 2.15 +0 | 2.30 +2 | 2.45 +3 | 2.60 +3
    2.75 +0 | 2.85 +1

CONTRE L'HYPOTHESE REGIONALE -- LA MIENNE. Exces moyen au bord gauche
(w2 < 1.45, 4 points) : 2.00. Sur le reste (12 points) : 1.50. Le bord gauche
NE SE DETACHE PAS. Et le maximum d'exces n'est pas a 1.25 (+3) ou G6 a tire,
mais a 1.30 (+4), qui n'a pas ete exclu. Correlation(ilots, w2) = -0.19 sur
16 points : rien.
**L'hypothese regionale, telle que je l'avais formulee au S36.4, n'est pas
soutenue par les donnees qui existaient deja.** Je la retire comme hypothese
privilegiee.

CONTRE L'HYPOTHESE RESONANTE NAIVE -- CELLE DE MACHINE 2. Correlation(ilots,
distance a la resonance la plus proche) = -0.30 : mieux, mais rien non plus.
Et un contre-exemple direct : 1.45 et 1.55 sont a la MEME distance de 3:2
(0.05 des deux cotes) et donnent +0 et +4. La distance a la resonance ne
separe donc pas ces deux points-la.

CE QUI RESTE VRAI, ET QUI EST DEJA AU GEL : le bord d'explosion est CRIBLE
PARTOUT -- les 16 points ont au moins un ilot, sept en ont un exces de 2 ou
plus, et six sont propres. Le criblage n'est ni un phenomene de bord ni un
phenomene de resonance : c'est l'etat general du rivage, comme M10 le disait
avant de mesurer.

## 37.3 POURQUOI ON NE PEUT PAS TRANCHER : UN DEFAUT D'INSTRUMENT

G6 consigne l'amplitude explosive minimale UNIQUEMENT si elle tombe sous
0.98 s*. Sur 64 lignes, **UNE SEULE** porte une marge lisible -- celle qui a
declenche. Les 63 autres ne disent pas si elles ont frole ou si elles etaient
tres loin.
Le nombre d'ilots, lui, est un ENTIER entre 1 et 3 par ligne : quatre valeurs
possibles, sur 16 points. Aucune correlation ne peut sortir de la.

    CORRECTIF POUR LE SCRIPT p=4, COUT MACHINE NUL -- le balayage est deja
    fait, il s'agit de garder un nombre qu'on jette :
        consigner min(s explosif) / s* SUR CHAQUE LIGNE.
    La marge devient lisible aux 64 lignes au lieu d'une, et la question
    regional / resonant se tranche alors sur une variable CONTINUE au lieu
    d'un compte entier a quatre valeurs.

C'est le meme geste que la regle 13 -- rapporter la quantite plutot que le
seul franchissement du seuil -- applique a une garde au lieu d'un seuil. Une
garde qui ne rapporte que son verdict jette la mesure qui l'a produit.

## 37.4 CE QUE CELA FAIT A L'ENTREE 7

Machine 2 demande que le pre-enregistrement DECLARE l'hypothese retenue avant
de choisir la grille. Le S37.2 etablit qu'aucune des deux n'est soutenue :
declarer l'une reviendrait a deviner et a laisser la grille en dependre.
    PROPOSITION, qui remplace le choix par une mesure :
    (a) l'entree 7 declare que les DEUX hypotheses sont ouvertes, et gele la
        LECTURE qui les departagera -- la correlation entre la marge continue
        de 37.3 et, d'une part w2, d'autre part la distance a la resonance la
        plus proche, avec le seuil de decision ecrit d'avance ;
    (b) la grille est choisie sur le critere ROBUSTE AUX DEUX : maximiser
        R_fen a la largeur declaree, ce qui punit l'entassement -- donc se
        premunit du regional -- ET s'ecarter des k/l d'ordre 9 a 12, ce qui
        se premunit du resonant. C5 (lambda 0.317) satisfait le premier ;
        reste a verifier le second, point par point.
Choisir une grille qui survit aux deux hypotheses coute moins cher que de
parier sur l'une, et la manche departagera de toute facon.

## 37.5 CE QUI RESTE A FAIRE, DANS L'ORDRE

  1. geler la LARGEUR regionale (entree 6) -- avant toute grille ;
  2. verifier C5 point par point contre les resonances d'ordre 9 a 12 ;
  3. si C5 y expose des points, chercher la variante qui satisfait les deux
     criteres, et l'enumerer dans les deux coordonnees ;
  4. porter au script p=4 le correctif de 37.3 (marge continue sur 64 lignes)
     et la regle 14 (refit a chaque reechantillonnage) ;
  5. alors seulement, rediger le pre-enregistrement.
Aucune de ces etapes ne demande une mesure. Toutes sont de l'algebre ou de la
redaction, et toutes doivent preceder la premiere ligne de code.

=== FIN DU DELTA 37 ===
