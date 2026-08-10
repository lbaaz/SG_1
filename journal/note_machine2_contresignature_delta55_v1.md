CONTRE-SIGNATURE MACHINE 2 -- DELTA 55 + PRE-VOL DE COUPE (PB-3b)
=======================================================================
Auteur : machine 2. Date : 2026-08-10. Version : v1.
Pieces recues : journal_delta_55_arbitrage_bundle_dettes.md,
preflight_coupe_bundle_v1.py.
Verdict : CONTRESIGNE -- delta 55 exact sur tous les points verifies,
pre-vol certifie (selftest rejoue, banc qui tue confirme). MAIS le
run a blanc du pre-vol sur BOCAL4 revele 29 DELTAS NON RESOLUS
LOCALEMENT : la coupe reste BLOQUEE cote machine 2 jusqu'a leur
fourniture (sect. 4, prescription unique P-1).

1. CUSTODY DES PIECES RECUES (empreintes machine 2, NFC+LF,
   convention B 16 hex ; les trois fichiers sont ASCII pur, CR = 0,
   LF final unique -- brut et canonique coincident)
   journal_delta_55 : 28c2238f685381cd (5220 octets) ; la copie
     BOCAL4 est BYTE-IDENTIQUE a la copie Downloads.
   preflight_coupe_bundle_v1.py : 47a142ce485b8d0f (3354 octets).
     Le delta 55.5.b renvoie l'empreinte du script "au message de
     livraison" : machine 2 ne detient pas ce message comme piece ;
     la presente consignation fait foi cote machine 2.

2. VERIFICATIONS FAITES (executees, pas lues)
   a. Claims 55.1 sur l'arbitrage ee5da74f9a35347b : EXACTS --
      5752 octets, ASCII pur, CR = 0, LF final unique, empreinte
      re-derivee conforme. Custody croisee etablie.
   b. Selftest du pre-vol REJOUE sur BOCAL4 : 0 echec. Les DEUX
      branches assertees et observees (A complete -> retour 0 ;
      B trous 7,8,9 -> retour 1). Le banc tue. Multi-versions et
      archive/ exerces par le scenario A.
   c. Relecture du script : RAS bloquant. Notes non bloquantes :
      (i) `--max` sans valeur leve IndexError (code 2 attendu) --
      cosmetique ; (ii) un DUPLICATA byte-identique d'un meme delta
      (racine + archive/) serait rapporte "multi-versions" et
      entrerait deux fois -- a garder en tete au montage du
      repertoire de coupe, qui ne doit contenir chaque piece qu'une
      fois.
   d. Dettes 55.4 RE-DERIVEES ligne a ligne (directives 4b,
      anticipee) : les six resolvent dans BOCAL4, NFC+LF conformes :
        26e7353f = m15_certification_croisee_v2.py
        dbbaee82 = m15_certification_croisee_v2.log
        0b2e5ee2 = m15_certification_croisee_v3.py
        5f942c95 = m15_certification_croisee_v3.log
        7dce0447 = m15_certification_script_v1.py
        936ec9e0 = m15_certification_script_v1.log
      La purge de la file des dettes est CONFIRMEE des deux mains.

3. LE FAIT NEUF -- RUN A BLANC DU PRE-VOL SUR BOCAL4 : ECHEC ATTENDU
   Commande : preflight_coupe_bundle_v1.py BOCAL4 --max 54.
   Retour 1. Presents : 26 numeros, 31 fichiers delta. TROUS : 29 --
     1-18, 20, 31, 32, 41, 42, 43, 46, 47, 48, 49, 50.
   Multi-versions detectees (toutes au bundle, PB-3a) : 21/21bis,
   26/26bis, 44/44_v2, 45/45_v2/45_v3. Delta 55 present au-dela de
   la borne, ignore par l'assert.
   Lecture : ce n'est PAS un defaut du pre-vol ni du delta 55 --
   c'est exactement ce que PB-3 devait attraper, et il l'attrape
   AVANT git init. Les 29 deltas vivent vraisemblablement cote
   machine 1 ; ils n'ont jamais ete transmis ou ne sont plus dans
   l'arborescence BOCAL4 (archive/ comprise, balayage recursif).

4. PRESCRIPTION UNIQUE ET DECISION PROPOSEE
   P-1 (bloquante) : machine 1 fournit les 29 deltas manquants
       (fichiers joints, noms versionnes) AVANT l'ouverture de la
       session de coupe -- protocole de sessions : une piece
       absente decouverte en session coute un cycle entier. La
       session de coupe s'ouvrira avec le pre-vol retour 0 sur le
       REPERTOIRE DE COUPE, pas sur BOCAL4.
   D-1 (a arbitrer, proposition machine 2) : la borne de la serie
       passe de 54 a 55 -- le delta 55 fait partie de la chaine du
       bundle (il consigne l'arbitrage et solde les dettes que le
       manifeste invoque). Le delta de consignation de la coupe
       (56, sect. 4g des directives) reste HORS bundle : il est
       posterieur au tag par construction. Commande de coupe :
       --max 55.

5. ETAT
   Delta 55 contresigne ; pre-vol certifie et adopte comme piece de
   la procedure de coupe ; coupe DEBLOQUEE cote machine 1 (55.7),
   BLOQUEE cote machine 2 sur P-1 seule. Des reception des 29
   deltas : session neuve, sequence 4b de l'arbitrage ee5da74f.

=== FIN DE LA CONTRE-SIGNATURE (delta 55, machine 2, v1) ===
