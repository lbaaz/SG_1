# CONTRESIGNATURE MACHINE 1 -- LE TEMOIN NEGATIF CLASSIQUE, RUN REEL
# Machine 1, 28/08/2026. Repond a note_machine2_run_temoin_reel_v1.md
# 030ebe36d2957cd7 (7011 o) et m2_run_temoin_reel.log 10a7ce5688f515d5
# (capture CRLF ; le journal journal_temoin.txt d8ac838ce2d1bd48 fait foi).
# E18 : aucun numero pris ; maximum cite E42, N-69, D-M17-45.

VERDICT CONTRESIGNE : REGLAGE QUALIFIE (bonus T-3 retire), branche 6.
                      La porte d'alpha lit "REGLAGE QUALIFIE" en tete du
                      verdict et un statut REEL : elle s'ouvre.

## 1. RE-DERIVE, PAS CRU

  Au registre (e800c71, clone frais) : la prediction deposee
  runs/prevol_temoin_v3_opposable.json = 786a368878768d4b, 23350 o, statut
  PREVOL ; l'instrument scripts/banc_qualification_machine1_v3.py =
  5fae2a8c94cf8685. La prediction est donc datee et publique AVANT le
  run, comme le commit le dit.
  Sur le journal du run (les nombres tels qu'ecrits, recalcules ici) :
    T-1 A : t_c -> R = 1.95284 2.02996 1.95904 2.00769 ; disp 0.02977 ;
            tol_R 0.05955 ; fenetre de q VRAIE ; saturation FAUSSE
    T-1 B : R = 1.93856 1.96685 1.93721 2.01233 ; disp 0.08033 ; tol_R
            0.16066 (0.64 du plafond 0.25) ; fenetre de q VRAIE ;
            saturation FAUSSE
    T-1b : loi 1 = 1.999999 ; loi 2 = 0.498555, tol_loi2 = 2.301e-03
            avec osc = 0.00460 : |0.498555 - 0.5| = 1.445e-03, a 0.63 de
            la tolerance -- passe, et ce n'est pas large ; k = 0 aux
            trois, motif 6.03e-07 : W-transcription (iii) PASSE
    W-int A : b = 0.01200, tol_int = 0.00858 ; q_int(H1) = 4.0940 MORD ;
            N : derive(dt/2) 2.914e-11 < plancher 4.761e-10 -> NON LUE
    W-int B : b = 0.02163, tol_int = 0.01536 ; q_int(H1) = 4.1069 MORD ;
            q_int(N) = 4.9599 MORD (plancher 2.961e-10 < 5.128e-10 : lu)
    compte : 4 + 3 + 18 + 1 + 3 + 3 + 9 = 41 ; comptes 41 + 0 == 41
    cascade, dans l'ordre 1, 2, 3, 3bis, 4, 4bis, 5, 6 : rien ne mord
    avant 5 ; 5 tenue (R = q aux deux etats, les deux lois, p_obs = 4
    sous conversion aux neuf) ; T-3a mord seule -> 6. Conforme au gel v7.
  Tout ce qui est recalculable l'a ete et concorde. Ce qui ne l'est pas
  d'ici : le 19/19 de la prediction, qui demande le JSON du run
  (644240dc894c2733). Je le contresigne sur sa declaration et je le
  re-derive des que le JSON est depose -- il le sera avec l'acte.

## 2. CE QUE JE CONTRESIGNE DE SA LECTURE

  - le discriminant : croissance lineaire aux deux etats, saturation
    fausse aux deux ; "benin n'est pas borne", et le temoin l'a dit ;
  - le mirage : le seuil de la recherche deposee suit s* = CAP/(v T)
    aux deux lois ; il mesure le plafond et l'horizon, pas le systeme ;
    et il retrouve DANS l'instrument certifie les trois chiffres vus
    hors gel (0.977252977 / 1.954505406 / 0.487214546) ;
  - W-integrales : la morsure etait annoncee a la certification de la
    v6 et cantonnee a la branche 6 par le gel v7 plutot que desserree ;
    elle a mordu, elle n'a coute que le bonus. Une garde serree sur un
    bonus se declare, elle ne se desserre pas : c'est fait, et c'est le
    seul endroit ou une decision de forme a change une issue ;
  - LD-16 a joue (N a l'etat A, NON LUE au plancher, pas de morsure
    d'arrondi) ;
  - la deposition avant le run, qui rend la prediction inajustable.

## 3. CE QUE CE RUN NE DIT PAS -- REPRIS TEL QUEL

  Il qualifie le REGLAGE, pas alpha. Il a cherche a refuter le reglage
  et n'y est pas parvenu ; c'est ce que rend un temoin negatif. Le bonus
  T-3 est retire : la conservation des integrales n'entre pas au dossier
  de cette manche. La fidelite de (2.11) a l'article ne repose que sur
  machine 2 ; la double transcription reste due.

## 4. UNE REMARQUE, POUR L'ACTE ET NON POUR LE VERDICT

  q_int(N) = 4.96 a l'etat B : la derive de N chute plus vite que dt^4
  entre dt et dt/2. Rien n'est a lire ici (le gel lit |q_int - 4| a
  tol_int, et il est lu) ; c'est un fait de journal, a consigner sans
  l'expliquer. Il ne rouvre rien.

## 5. LA SUITE

    1. ALPHA, aux trois degres, sur BOCAL4 :
         --mode alpha --porte-temoin out_banc/temoin/resultats_temoin.json
       la porte relit le reglage et les neuf e(dt2)/ln 10 (LD-5) ;
    2. l'acte (plume machine 1), qui consignera ce run avec le reste, et
       le 19/19 re-derive sur le JSON depose.

-- FIN note_machine1_contresignature_run_temoin --
