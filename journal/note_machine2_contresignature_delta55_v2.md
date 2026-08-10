CONTRE-SIGNATURE MACHINE 2 -- DELTA 55 + PRE-VOL DE COUPE (PB-3b)
=======================================================================
Auteur : machine 2. Date : 2026-08-10. Version : v2.
REMPLACE la v1 (db3b17e2) : sa prescription P-1 (29 deltas manquants)
etait SURESTIMEE -- l'enquete de resolution locale menee apres coupe
de la v1 reduit le manque reel a SIX deltas et etablit la
correspondance des numeros 1..20. La v1 n'est pas editee (piece citee
par empreinte) ; tout son contenu de certification (sect. 1, 2)
reste valide et n'est pas re-signe ici, seules les sect. 3-5 sont
remplacees.
Pieces recues : journal_delta_55_arbitrage_bundle_dettes.md
(28c2238f685381cd), preflight_coupe_bundle_v1.py (47a142ce485b8d0f).
Verdict : CONTRESIGNE (inchange) -- delta 55 exact sur tous les
points verifies, pre-vol certifie (selftest rejoue, banc qui tue
confirme, dettes 55.4 re-derivees 6/6). Voir v1 sect. 1-2.

3. RESOLUTION LOCALE DE LA SERIE -- ENQUETE ET ETAT REEL
   3.1 LES "DELTAS 1..17" N'ONT JAMAIS ETE DES FICHIERS. La serie
       des deltas continue la numerotation des SECTIONS du journal
       maitre de la seance bundle 5 (25/07) : le journal
       `journal_bundle5_v2026-07-25h.md` (archive/journal_maitre/,
       version finale h, sommaire declare "0-16, ERRATA E1-E14,
       pre-enregistrements M2/M3/M4/M5") porte les sections 0..16 ;
       le premier delta autonome est `journal_delta_section18.md`
       (archive/deltas_clos/), qui s'ouvre par "## 18.". Preuve de
       continuite : numerotation, date, renvois (le 18 ferme les
       "Ouverts" du par. 6 du maitre).
   3.2 CORRESPONDANCE DECLAREE (a faire foi au bundle) :
         1..17 -> journal_bundle5_v2026-07-25h.md (+ les versions
                  anterieures seance/e/f/g, toutes au bundle,
                  PB-3a) -- archive/journal_maitre/
         18    -> journal_delta_section18.md -- archive/deltas_clos/
         19,20 -> journal_delta_19-20_E16-E17.md (fichier COMBINE ;
                  le motif du pre-vol v1 ne capte que "19")
         21+   -> fichiers journal_delta_NN* (BOCAL4 racine et
                  archive/deltas_clos/)
   3.3 QUATRE DELTAS RAPATRIES Downloads -> BOCAL4 le 10/08,
       copies BYTE-IDENTIQUES verifiees, empreintes brutes
       (fichiers ASCII a confirmer au pre-vol de coupe ; brut
       cite ici en custody de canal) :
         journal_delta_31_L1.md               c53953a79407ab3d
         journal_delta_32_M10.md              a95473e5a12168f7
         journal_delta_43_E27.md              a94fd607d656a8e0
         journal_delta_46_run_M12_ponctuel_v2.md  344e7730a1168dbb
       Recoupement de registre : a94fd607 = l'empreinte que le
       delta 52 cite pour le texte canonique S43 -- la piece
       rapatriee EST la piece du registre, custody croisee.
   3.4 ETAT DU PRE-VOL APRES RAPATRIEMENT (--max 55, BOCAL4) :
       trous restants = 1..18, 20 (RESOLUS par la correspondance
       3.2, invisibles au motif seulement) + 41, 42, 47, 48, 49,
       50 (REELLEMENT ABSENTS). Recherche etendue machine 2
       (Downloads, Desktop, Documents, d:\devs recursif) : les six
       n'existent nulle part cote machine 2. Le registre les
       atteste pourtant (S42.3 au delta 52 ; "crible 48.3" ;
       "deltas 47-54 font foi" des directives D-B6) : ils vivent
       cote machine 1.

4. PRESCRIPTIONS (remplacent P-1/D-1 de la v1)
   P-1' (bloquante, REDUITE) : machine 1 fournit les SIX deltas
        41, 42, 47, 48, 49, 50 (fichiers joints, noms versionnes)
        AVANT l'ouverture de la session de coupe.
   P-2' (bloquante) : le pre-vol passe en v2 avec la CORRESPONDANCE
        DECLAREE 3.2 : table numero -> fichier(s) porteur(s) pour
        1..20, assert par fichier present (pas par motif), le motif
        journal_delta_NN restant la regle pour 21+. Le selftest v2
        ajoute un scenario "fichier combine" (19-20) et un scenario
        "correspondance manquante" qui ECHOUE. Machine 1 autore
        (PB-3b reste sa piece) ; machine 2 certifiera.
   D-1' (a arbitrer, proposition machine 2, reprise de la v1) :
        borne de serie 54 -> 55 (--max 55) ; le delta 56 de
        consignation de la coupe reste HORS bundle, posterieur au
        tag par construction. Le run 3.4 est deja joue a 55.
   D-2' (a arbitrer) : les versions anterieures du journal maitre
        (seance, e, f, g) entrent au bundle avec la h (PB-3a,
        pieces datees distinctes) -- proposition machine 2 : OUI,
        memes motifs que les deltas multi-versions.

5. ETAT
   Delta 55 contresigne (v1) ; pre-vol v1 certifie, revision v2
   prescrite (P-2') ; QUATRE des dix manques reels combles par
   rapatriement local, SIX restent a fournir par machine 1 (P-1') ;
   correspondance 1..20 etablie (3.2). Des reception des six deltas
   et du pre-vol v2 : session neuve, sequence 4b de l'arbitrage
   ee5da74f, pre-vol retour 0 exige sur le REPERTOIRE DE COUPE.

=== FIN DE LA CONTRE-SIGNATURE (delta 55, machine 2, v2) ===
