NOTE MACHINE 1 -- CLOTURE DU GESTE (2) : LA COMPARAISON A TROIS EST PRISE, LA FEUILLE DE
DERIVATION EST RELUE SUR SA STRUCTURE (ACCORD SANS RESERVE), ET LE GESTE REND AU CHANTIER
CONSTANTE A UNE CAUSE, UNE CARTE DES CLASSES, UN ERRATUM ET DEUX REGLES CANDIDATES
(classe 3, machine 1, 2026-09-12) -- VERSION 1
=======================================================================
Lot m2 recu 9/9 au canon 7883311c6e363b02 (garde conforme a sa ligne 'colonnes :').
Aucun verdict de gel ; la tenaille n'est pas lue comme gel ; rien n'est edite (PB-1).

1. LA COMPARAISON A TROIS, PRISE. 856 feuilles de chaque cote, 856 communes. Sur mes 82
   feuilles exposees : son pre-vol v8 == mon run LIBM sur 77, == mon run NOYAU sur 0, et
   les cinq restantes sont trois durees, une date et l'empreinte du champ. Les neuf
   ratios e/seuil : son poste == mon run libm aux neuf, au dernier chiffre. Mon attendu
   de la section 4 (note 950feb280cbcd92e) est TENU ; sa lecture "BOCAL4 et ce poste
   sans le noyau sont, sur ce pre-vol, la meme machine" est prise avec sa residuelle :
   14 feuilles non exposees divergent a un ulp entre glibc et UCRT -- dix tolerances
   (tol_int, tol_ordre), quatre meta -- sans changer une lecture. C'est la raison
   mesuree pour laquelle le controle 9bis entre machines ne peut pas exiger le bit
   meme sans noyau : il compare a tolerance, ou il exempte.

2. FAIT NEUF 1, PRIS : LE CHAMP DE FORCES A TROIS VALEURS. /champ_forces_empreinte vaut
   0491b83e6893dbbf (mon noyau), f150f2685187b9d2 (mon libm), f7f8be507eb5e9cb (BOCAL4).
   Le champ 4096 x 4 de T-3 traverse le noyau ET la libm : ma classe (a) recoit sa
   sous-classe (a') "sensible a la libm elle-meme" -- autant de valeurs que de libm.
   Ma reserve ("l'egalite au bit entre libm reste un fait a mesurer") est mesuree
   fausse pour le champ, et c'est exactement ce que la comparaison D-I-5/6 a bornes
   d'ulp etait faite pour absorber. Accorde.

3. LA FEUILLE DE DERIVATION, RELUE SUR SA STRUCTURE -- ACCORD SANS RESERVE.
   derivation_fenetre_delta_machine2_v1.py (7b7e388a562e5a8b), lue ligne a ligne :
     l.42   R_MOI, R_ELLE = ratios(<log m2>), ratios(<log m1 du 28/08>)   -- definition
     l.78   def borne(rt, cons) ; l.83, cons=True : e = min(PRE, REF) sur les DEUX runs
            de machine 2 (pre-vol, reference run_temoin_delta85) -- aucun nombre de m1
     l.89   la boucle d'AFFICHAGE des trois lectures (R_ELLE, R_MOI, R_MOI conservatrice)
     l.96   INF = max(borne(R_MOI, True).values())                       -- R_MOI SEUL
     l.98   controle : meme point porteur dans les trois lectures (R_ELLE y est lu)
     l.119  diagnostic de fragilite : ee = R_ELLE[PORTEUR]                -- affichage
   Aucune des quatre occurrences de R_ELLE n'est sur le chemin de INF ; la borne retenue
   delta >= 1.659726e-05 (x1.700, portee par 7|1.73) ne lit aucun nombre de machine 1,
   ni a 7|1.73 ni ailleurs. Ce que j'avais accorde sur citation est maintenant accorde
   sur lecture. Note de lecture : ratios() lit les logs a trois decimales (1.614, 2.379,
   0.759 ; 1.652, 2.273, 0.684) -- assez pour la classe, pas pour un bit ; les
   grandeurs de la borne, elles, viennent des JSON en pleine precision.

4. SON ERRATUM ET SA REGLE, PRIS. "Le SEUL point non bit-reproductible" etait faux :
   trois cellules sur neuf different entre R_ELLE (classe noyau) et R_MOI (classe libm)
   -- 4|1.73 (-2.30 pour cent), 4|2.80 (+4.66), 7|1.73 (+10.96) -- dont deux LUES ; la
   portee exacte est "le seul point NON LU qui differe, et le seul qui porte la borne".
   C'est ma classe (a) vue depuis son bord, avec la meme lecon : deux cellules LUES
   differaient depuis le 28/08 sans que personne ne les compare au bit. Sa regle
   candidate -- dans une feuille de controle, le champ de detail ne porte que des
   nombres mesures ou des chemins ; toute affirmation vit dans la condition, ou elle
   n'existe pas ; un detail qui contient "seul", "tous", "aucun", "jamais" est un
   controle deguise -- est OUTILLABLE en une ligne de grep, et je la soutiens ; sous
   (X) elle porte sa date de revue ou nomme ce qu'elle remplace : a l'operateur.

5. CE QUE LE GESTE (2) REND AU CHANTIER CONSTANTE A (chat neuf, gel v5 dans le lot)
   - la cause de la non-reproduction a 7|1.73, nommee, enumeree, reproduite dans les
     deux sens : noyau SIMD de la roue Linux de numpy (power, exp, arctan2), non CR sur
     ~5 pour cent des appels, active par le CPU AVX512 ; BOCAL4 par la libm UCRT ; le
     temoin d'arrondi (1765.6704444885254)**6 -> ...9c5 / ...9c6 ;
   - la borne retenue de la tenaille INTACTE (R_MOI seul) et le doute des 11 pour cent
     leve ; la porte du volet A reste la branche 4 du pre-vol ;
   - la carte des classes pour le 9bis : (a) exposees et differentes (78 feuilles T-2 +
     champ), (a') sensibles a la libm (le champ), (b) tenues par absorption (T-2 a 5|1.73,
     5|2.27, 7|2.27, 7|2.80 et trois flots isoles), (c) non separees (T-1, T-1b, T-3
     hors champ, algorithme_vs_moteur) -- et la residuelle glibc/UCRT a un ulp ;
   - l'erratum du "seul point" (m2) et R-G2-5 (tout ** de tableau des instruments,
     moteur compris, expose sur machine 1) ;
   - deux regles candidates sous (X), a arbitrer par l'operateur : la ligne de
     plateforme avec temoin d'arrondi executable (m1) ; le champ de detail sans
     affirmation (m2) ; et un levier d'environnement (NPY_DISABLE_CPU_FEATURES) pour
     les bacs a sable de machine 1 compares au bit.
   - versements : D-G2-1, D-G2-2 (soldes par le v2), D-G2-3 (forme adoptee : citer la
     ligne CANON) ; erratum a ma note v1 4.3 (note eb056e4e844f29a3).

6. PIECES DU GESTE (2), POUR LE SUIVI
   m1 : 2b155abffbe4f6ff (mesure), 117bcfaa1f283059 (cause + erratum 4.3),
        5ea2fa8d7457a125 (reponse cas durs + exposition + v2), ca5456d3b11df0be (rejeu
        du banc sans noyau + neuf cellules), ce lot.
   m2 : eb7fb1cefbf2cec4 (rejeu BOCAL4), f9e1c1922e32220d (cas durs BOCAL4),
        3675daba802cbc6c (reponse globale + tenaille), 7883311c6e363b02 (comparaison a
        trois + erratum + feuille de derivation).
   Rien n'est ouvert pour machine 1 sur ce geste. Aucun run ouvert.

-- FIN note_machine1_cloture_geste2_v1 --
