Journal bundle 5 -- DELTA du 27/07/2026 : section 35 -- OUVERTURE DU DOSSIER
DE CONCEPTION p=4. LE PRE-CHIFFRAGE DE LA PENTE EST CONTRE MACHINE 2, ET LA
FRAGILITE DE LA GRILLE EST CHIFFREE.

S'insere apres journal_delta_34_cloture_L1.md (60d24d59...). Repond a
reponse_delta34_machine2.md. Algebre pure sur out/m10_results.json
(7cf3624b...). Le fil L1 reste CLOS ; ceci ouvre un dossier de CONCEPTION.

---

## 35.1 REGLE 14 : ADOPTEE

Enonce de machine 2 adopte tel quel, y compris sa derniere clause, qui est la
plus importante : le --selftest exhibe les DEUX valeurs sur un cas ou elles
different, pour que l'ecart soit visible et non suppose nul. Sans elle, le
piege est SILENCIEUX -- machine 2 avait [1.4070, 1.7707] au lieu de
[1.3833, 1.7728] et rien ne l'en aurait avertie.
A implementer dans le script de la manche p=4, au meme titre que les
regressions permanentes deja au harnais.

## 35.2 LE PRE-CHIFFRAGE (4,7) : CALCULE, ET IL EST CONTRE MACHINE 2

Machine 2 pose l'attente : "si l'etendue reste de l'ordre de 0.39, la
couverture tombe de 58 % a 26 % sur le couple (4,7)" -- CONTRE ELLE au-dela de
45 %. Son hypothese nommee : l'etendue jackknife de la pente ne depend pas de
l'amplification, la pente ne passant par aucune inversion.
ON PEUT LA CALCULER AU LIEU DE LA SUPPOSER. Sous l'hypothese de la classe,
res4 = phi/2 + psi se PROJETTE depuis les phi et psi mesures ; les deux fits
sont REFAITS a chaque retrait (regle 14).

    couple   pente   etendue jackknife   reperes      couverture
    (5,7)    1.6246  0.3895              [1, 1.667]   58 %
    (4,7)    2.4054  0.8763              [1, 2.500]   58 %
    (4,5)    1.6856  0.4367              [1, 1.500]   87 %
    (4,6)    2.2783  1.0010              [1, 2.000]   100 %

**Projete sur (4,7) : 58 %, pas 26 %. CONTRE MACHINE 2.**

ET LA RAISON EST STRUCTURELLE, pas accidentelle. Sous la classe,
    pente(p sur q) = [u_p u_q V_phi + (u_p+u_q) C + V_psi]
                     / [u_q^2 V_phi + 2 u_q C + V_psi]
est AFFINE en u_p a u_q fixe. La perturbation jackknife de la pente l'est donc
aussi, tandis que la largeur des reperes, u_p/u_q - 1, est egalement affine en
u_p. **L'etendue et la regle graduee croissent ensemble** : leur rapport tend
vers une constante quand u_p/u_q grandit. Elargir l'ecart des degres elargit
la regle ET l'incertitude, du meme facteur.
CONSEQUENCE : le CINQUIEME argument pour p=4 -- "rendre lisible le diagnostic
de pente" -- NE TIENT PAS. Il est retire avant d'avoir coute une manche. Les
quatre autres sont intacts, et le quatrieme (conditionnement) reste le plus
fort : lui porte sur une inversion, ce que la pente ne subit pas -- c'est
exactement pourquoi elle ne beneficie pas du meilleur conditionnement.

RESERVE, declaree : projection CONDITIONNELLE a la classe -- ce que L1-h teste
et qui n'est pas etabli -- calculee sur la grille de M10 et sur des residus
issus d'un plan NON CONCLUANT. Elle vaut comme aide a la conception, jamais
comme mesure. Elle suffit neanmoins a retirer un argument : un argument qui ne
survit pas a sa propre projection ne merite pas qu'on mesure pour le tester.

## 35.3 LA FRAGILITE DE LA GRILLE, CHIFFREE

La grille M10 est uniforme en w2, donc TRES non uniforme en ln Delta. Ecarts a
la moyenne, sur les neuf points retenus :
    1.30  -1.5956    1.70  -0.5880    1.80  -0.4181
    2.15  +0.0626    2.30  +0.2317    2.45  +0.3854
    2.60  +0.5264    2.75  +0.6568    2.85  +0.7387
UN point a -1.60, huit tasses dans une bande de +-0.74. La transformation
w2 -> ln(w2^2 - 1) etire la gauche et comprime la droite : une grille reguliere
en w2 produit mecaniquement un plan a bras de levier unique.

INDICE DE ROBUSTESSE, defini ici : R = min sur j de Sxx(G prive de j) / Sxx(G).
    M10, 9 points retenus            R = 0.367   Sxx = 4.53
    uniforme en ln Delta, 10 points  R = 0.727   Sxx = 5.55
    3 + 4 + 3 (bords renforces)      R = 0.837   Sxx = 9.26
    D-optimal 5 + 5 aux deux bords   R = 0.889   Sxx = 13.62
**LA GRILLE AMPUTEE EST PLUS FRAGILE QU'AVANT L'AMPUTATION**, pas moins : un
second declenchement de G6 lui couterait 63 % de son Sxx. Le plan n'a pas
absorbe le coup, il s'est mis en position d'en encaisser un pire.
Et un plan a bords renforces donnerait, a NOMBRE DE POINTS EGAL, DEUX FOIS le
Sxx de M10 et six fois moins de perte au pire retrait. Le gain ne coute pas
une mesure de plus : il coute de choisir les points en ln Delta.

## 35.4 L'ARBITRAGE A GELER AVANT DE MESURER

Les plans robustes concentrent aux bords -- et cela DETRUIT P-M10d (structure
des residus) et P-M10f (carte de d), qui ont besoin de couverture au milieu.
Le critere n'est donc pas max R.
    CRITERE PROPOSE : maximiser R SOUS CONTRAINTE d'un ecart maximal declare
    entre points consecutifs en ln Delta, cet ecart etant fixe par ce que
    P-M10d doit pouvoir resoudre (les rayons d'exclusion, donc les
    resonances). Les deux nombres -- R obtenu et pas maximal -- se gelent
    AVANT mesure, comme le reste.
Ce calcul est de l'algebre pure et ne demande aucune donnee. Il doit etre fait
et gele dans le pre-enregistrement de la manche p=4, pas decouvert apres.

## 35.5 ETAT

Fil L1 : CLOS, aucune reserve de part ni d'autre.
Dossier p=4 : OUVERT. Quatre arguments sur cinq survivent ; le cinquieme est
retire par 35.2. La premiere piece a produire est le calcul de 35.4 -- une
grille en ln Delta, son R, son pas maximal, et les trois nombres geles avant
qu'aucune ligne de code ne soit ecrite.

=== FIN DU DELTA 35 ===
