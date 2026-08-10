JOURNAL DELTA 51 -- CLOTURE DE LA MANCHE M15 (machine 1, 2026-08-08)
====================================================================

51.1 CONSIGNATION E29 (numero attribue A L'ACTE, regle E18 ; dernier
     precedent E28 ; rien d'intercale)
  E29 -- "grossiere mordue" : definition UNIQUE fixee sur la passe
  GROSSIERE ([LO0, 0.90 s*], champ explosion_sous_LO0_0.90s non nul,
  equivalent gros_explosifs >= 1). Texte : m15_erratum_grossiere_
  mordue_v3.md, sha256 16c6d86e389da2a9bd5581c9a4434b31fa342c2eabef14
  d9b865b2a0e4712e70. Fond contre-signe machine 2 (certification v2,
  24f23b75..., section 6 : chiffres re-derives, correction verbatim
  581 car. normalises) ; forme prescrite par machine 2, appliquee par
  patch asserte, sections 1-7 bit-identiques a la v2 (f4a3508b...).
  b_fond = 3/96, k_min = 3, n_eff = 24 : INCHANGES.
  Autorisation de cloture sans tour de re-paraphe : machine 2, ce
  jour, sur transcript ("les resultats ne sont pas compromis").

51.2 VERDICT DE MANCHE -- OPPOSABLE
  M15 (P1-b, site 8/3) : NON CONCLUANT DE GEOMETRIE.
  Un survivant sur six (2.62) ; flanc droit vide ; P-M15a NON LUE
  (aucune clause evaluee) ; P-M15b : k = 0 / n_eff = 24, k_min = 3,
  SIGNATURE NON RESOLUE (P(k=0) = 0.4667 sous le fond seul).
  k contre-verifie sous les trois lectures (0 / 0 / 2), verdict
  invariant sous E29. Chaine : gel v3 e41f4da3 . script v1 d05cf50b
  (execute) . JSON 96d78407 (brut CRLF ; canonique d3b19e51, memoire)
  . log 6af16c16 . remise 6ce6d793 . cert script v1 4a0cfc58 .
  cert script v2 24f23b75 (+ traces 044c426e / 3848c131).

51.3 FAITS CONSIGNES DU CYCLE (aucune porte)
  a) E(2.62) = +0.5022 (s*4 7.224023, s*5 2.331599, s*7 1.410099).
  b) Zone d'exclusion autour de 8/3 : 7 points sur 8 dans
     [2.62, 2.73] ; DEGRE-SELECTIVE (p=4 : 4/7 = 0.571 ;
     impairs : 2/24 = 0.083) ; mecanisme M13b (explosions fines
     0.938-0.968 s*, 4-7 ilots, ZERO morsure grossiere) ; largeur
     ~25 x le rayon R-2' d'ordre 11. N-12 aggrave.
  c) Paysage E consigne : plateau +0.50/+0.56 des deux cotes du
     site ; a geometrie reculee (corde 2.60-2.80) les quatre residus
     archives sont sous-plancher (0.1-0.5 x). Contraste inter-sites :
     5:2 = canyon O(1) resolu (M14) ; 8/3 = plateau + zone tueuse.
     Materiau ITEM 3 ; aucune attente inscrite.
  d) G1' 5/5 a 0.0 EXACT (custody au bit M12->M15, inter-machines) ;
     G3 bit-identique inter-plateformes ; N-14 exerce en reel
     (G2 SAUTEE, 37 + 1 = 38) ; G4 ecart 0.0 (sur ligne G6-exclue,
     selection heritee m12 sur recevable seul -- trait de lignee).
  e) Fait d'environnement : le pow de numpy n'est pas symetrique a
     la negation au dernier ulp, ET ce fait est ENVIRONNEMENT-
     DEPENDANT (False conteneur machine 1, True BOCAL4). Les gardes
     numeriques bitwise sur fonctions de librairie sont proscrites
     de fait : structurel ou mesure, rien entre.

51.4 ATTENTES (aucune reecrite)
  Machine 1 (gel v3, addendum) : FAUSSE par sa condition pre-ecrite
  (k = 0) ; attente centrale (AU-SITE) NON TESTEE. Machine 2 (note
  v2, section 13) : TENUE. Aucune des deux ne revendique (i).

51.5 FAUTES VERSEES
  M1-a  phrase ambigue du gel v3 (redaction D-4).
  M1-b  resolution de la definition par le script SANS declaration
        a la livraison (attrapee par la certification machine 2).
  M1-c  numero d'erratum ecrit au conditionnel, deux fois, malgre
        trois avertissements (remise 7.1, cert v1 sect. 5, journal
        44.6.b "pas meme au conditionnel").
  M2-a  (auto-declaree) : gel v3 certifie par verification
        d'heritage de la definition, sans re-application au registre.
  Pratique de banc (machine 1, sans numero) : trois comparaisons
  cassees par une hypothese d'ORDRE dans le meme cycle --
  canonicaliser avant toute comparaison, toujours.

51.6 LIGNEE DES SCRIPTS
  m15_site83_v1.py d05cf50b : version DU RUN (execute, inchange).
  m15_site83_v2.py 41ddebcd : version D'HERITAGE, certifiee
  (D-2, D-3, scenario Bp, X_survivants ; gel jumeau v3 inchange).
  Aucun verdict de la lignee ne change (effets nuls demontres).

51.7 REGLE CANDIDATE 16 (statut : A L'ARBITRAGE, avec la 15)
  "Le q_L se derive sur le plus PETIT domaine contenant le
  programme, par DEGRE ; si le registre y porte n <= 3 lignes, le
  q_L n'est pas derivable et la faisabilite se juge sur la borne."
  Proposee machine 2 (remise du run, sect. 2), soutenue machine 1
  (precision par-degre). Une manche propose, l'arbitrage adopte.

51.8 DETTES D'EMPREINTES (consignees une fois, sans relance)
  Traces .py/.log completes dues : note v2 (26e7353f.../dbbaee82...),
  note v3 (0b2e5ee2.../5f942c95...), cert script v1
  (7dce0447.../936ec9e0...).

51.9 FILE RESTANTE (hors manche)
  Gel v4 : definition E29 + N-13 + N-15. Arbitrage candidates 15 et
  16. Canaux des vecteurs synthetiques (7.4) si banc rejoue. Bilan
  des fautes M8-M11. Collision S42.3/S43 (arbitrage OUVERT).
  Branche quantique : specification d'estimateur avant toute manche.
  Dossier externe (Held) : decision de contenu.
  Prochaine manche : le trilemme du site (reculer / rendre la zone
  mesurable via le crible 48.3 / reviser la prediction P1 a 8/3),
  ITEM 3 derive sur la fenetre.

MANCHE M15 : CLOSE.
=== FIN DU JOURNAL DELTA 51 ===
