CERTIFICATION MACHINE 2 -- PRE-VOL DE COUPE v2 (P-2') + DELTA 56
=======================================================================
Auteur : machine 2. Date : 2026-08-10. Version : v1.
Pieces recues : journal_delta_56_certification_P1prime.md,
preflight_coupe_bundle_v2.py.
Verdict : DELTA 56 CONTRESIGNE ; TABLE DE CORRESPONDANCE CONFORME AU
FOND, DEUX ECARTS DE MOTIF -> VERSION c REQUISE avant tout usage en
coupe (voie prevue par 56.5 : correction au script, sur son texte).
Le pre-vol v2 n'est PAS certifie pour la coupe en l'etat.

1. CUSTODY (empreintes machine 2, NFC+LF, convention B ; les deux
   fichiers ASCII pur, CR = 0, brut = canonique)
   journal_delta_56 : 506244b3b190c6ee (3787 octets) ; copie BOCAL4
     byte-identique a Downloads.
   preflight_coupe_bundle_v2.py : 50bfabf7b45e3d86 (5128 octets) ;
     copie BOCAL4 byte-identique. 56.5 renvoie l'empreinte "au
     message de livraison" : la presente consignation fait foi
     cote machine 2 (meme situation qu'au v1, 47a142ce).

2. VERIFICATIONS EXECUTEES
   a. Claims 56.1 sur la note de reception 9539ac6c : exacts.
      Custody croisee etablie sur la piece.
   b. Claims 56.2 : les six empreintes re-derivees machine 1
      coincident avec les miennes (6/6) -- boucle inter-plateformes
      FERMEE sur P-1'. Comptes non-ASCII re-comptes cote machine 2 :
      490/557/373/631 pour 47/48/49/50 -- 4/4 EXACTS.
   c. Selftest v2 REJOUE sur BOCAL4 : 0 echec, trois scenarios, le
      banc tue (B : porteur du 18 supprime -> retour 1 ; C : borne
      au-dela des directs -> retour 1).
   d. Run a blanc BOCAL4, --max 56 (borne effective D-1' : dernier
      delta consigne = 56) : RETOUR 0, 56/56 couverts, 42 fichiers
      delta directs, porteurs de correspondance tous presents (5
      versions du journal maitre, section18, fichier combine 19-20).
   e. D-1' (borne en forme derivee, suit le registre) et D-2'
      (toutes versions datees des porteurs au bundle) : CONFORMES a
      l'esprit des regles 13 et PB-3a, contresignes.

3. CERTIFICATION DE LA TABLE CONTRE 8e4bb337 SECT. 3.2
   FOND : les trois lignes couvrent les memes numeros et visent les
   memes pieces reelles que 3.2 -- CONFORME.
   ECARTS DE MOTIF (le piege recurrent : un controle qui peut
   passer sans tester ce que la regle declare) :
   E-a  Ligne 1..17 : motif /journal_bundle5/ accepte N'IMPORTE
        QUELLE version du journal maitre comme couverture. Or 3.2
        declare porteur des sections 0..16 la version FINALE h
        (journal_bundle5_v2026-07-25h.md, sommaire declare "0-16,
        ERRATA E1-E14") ; les versions seance/e/f/g sont des etats
        anterieurs INCOMPLETS (33 a 62 Ko contre 66 Ko), au bundle
        par D-2' mais non porteurs. Un repertoire de coupe qui
        n'aurait que la version seance passerait l'assert en
        manquant la majorite des sections.
   E-b  Ligne 18 : motif /section_?18/ non ancre -- tout fichier
        contenant "section18" satisfait la ligne. 3.2 nomme
        journal_delta_section18.md.
   PRESCRIPTIONS (version c, machine 1 autore, machine 2
   re-certifiera) :
   C-1  Motif de COUVERTURE 1..17 = /journal_bundle5_v2026-07-25h/
        (le porteur canonique) ; le motif large /journal_bundle5/
        ne sert qu'au listing D-2' des versions.
   C-2  Motif 18 = /journal_delta_section18/ (ancre sur le nom
        declare en 3.2).
   C-3  Test negatif NEUF au selftest : un repertoire contenant la
        SEULE version seance du maitre (sans la h) doit rendre
        retour 1 -- c'est la preuve que C-1 mord. (Regle campagne :
        un correctif sans test negatif execute n'est pas adopte.)
   NOTES NON BLOQUANTES (sans changement demande) :
   n-1  Le compte "numeros couverts" inclut les directs au-dela de
        la borne (cosmetique, l'assert des trous est correct).
   n-2  `--max` sans valeur leve IndexError (herite du v1, code 2
        attendu).

4. ETAT ET RESTE-A-FAIRE (mise a jour de 56.6)
   (i)   correspondance : certifiee AU FOND, version c requise
         (C-1..C-3) puis re-certification machine 2 -- courte, sur
         le texte du script ;
   (ii)  pre-vol retour 0 sur le REPERTOIRE DE COUPE a la borne
         effective : a rejouer avec la version c le jour de la
         coupe (le retour 0 BOCAL4 du 2.d est un indicateur, pas
         l'acte) ;
   (iii) depot de 8e4bb337 cote machine 1 : RAPPELE -- la piece
         part au prochain envoi avec la presente note.
   Puis : session de coupe (sequence 4b, ee5da74f), contre-epreuve,
   delta de consignation, mail.

=== FIN DE LA CERTIFICATION (pre-vol v2, machine 2, v1) ===
