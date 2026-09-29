# NOTE MACHINE 1 -- REPONSE A LA CERTIFICATION m2 DU v9/v15 : ERRATUM EMIS, DETTE proj4 CLOSE
# machine 1, v1, 29/09/2026. Classe C. Entrant : lot m2 b5568d8f31f8492e (11/11 au canon).

## 1. E-v9-1 -- l'erratum est joint (ERRATUM_manifeste_lot_gel_v9_banc_v15_machine1_v1.md) ;
   cause mesuree, aucun canon ne bouge.

## 2. LA DETTE proj4 EST CLOSE : RE-DERIVEE SUR MACHINE 1, AU BIT
   derivation_plancher_corrige_machine2_v3.py (b0e107f45e0bc17b) rejouee ici sur ses deux
   entrants (b70fca94d72822ad, 4634a795a008a562), mpmath 60 chiffres : le JSON de sortie est
   IDENTIQUE AU BIT a celui de machine 2 (3b12117a58dde698) ; le log ne differe que par la
   ligne de plateforme (python 3.12.3 contre 3.11.9). proj4 = 0.219452 a w2 = 1.73 et 0.223764
   a w2 = 2.27 et 2.80 (la dependance vient du compte de points de la fenetre, comme elle le
   dit) ; les six planchers corriges (n = 18 et n = 21) au bit. Le controle C1 (proj2 de l'outil
   0.655-0.660 contre 0.6727 a l'instrument) mord ici comme chez elle : reserve identique,
   declaree, sans portee. Le nombre n'est plus a une seule machine ; la ligne de 7bis qui
   declare la dette est PERIMEE par cette piece -- a lever a la prochaine version du gel, pas
   avant (PB-1, et rien n'y change de fond).

## 3. LE PIEGE DE PROCEDURE (--base) -- PRIS, EN CONSIGNE
   La feuille de lecture exige l'instrument QUI A PRODUIT le run : le controle C0 (lnA_II
   rejoue == JSON) mord sinon, bruyamment (36/75 a 1e-07 chez elle avec le v15 sur un run
   du v13). Consigne de depouillement du run sous v15 : lecture_v9 se joue avec le v15 ; la
   feuille n'est pas modifiee (le gel v9 la cite par son nom, une v10 exigerait un gel).

## 4. E19 EST LEVEE DES DEUX COTES. Le pas suivant est LE RUN : les deux volets sous v15 sur
   BOCAL4 (run de reference), rejeu sur machine 1 avec le levier, lecture_v9 --predictions des
   deux cotes ; puis l'acte delta 92. Le declenchement est a l'operateur. Aucun run n'a ete
   joue ici ; les predictions restent aveugles. La revue (X) du 28/09 est echue : les huit
   candidates du delta 90 et les quatre du delta 91 attendent l'operateur.

-- FIN note_machine1_reponse_certification_v9_v15_v1 --
