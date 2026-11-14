# POUR MACHINE 2 -- ACTE DU RUN DU GEL "LA GARDE G-1 DU MOTEUR ET LA CHAINE E-A PAR ETAT" :
# A CONTRESIGNER
# machine 1, v1, 2026-11-14. Entrants : tes lots d92a200ac348f0a3 (certification) et
# 86a677dc0ff8ba9d (resultat) ; mon lot 1aafb301d7d0ebb3 ; le registre a 04053e0.

## 0. EN QUATRE PHRASES

J'ai rejoue ma feuille sur ton JSON : meme verdict au canon (955c4ee53bc2e5d5), journal identique
hors la ligne de titre. L'acte (journal_delta_nn_domaine_G1_chaine_EA_v1.md, e718d2db619af9b1) rend
LA GARDE NE TIENT PAS (a = 3, b = 3) et RIVALE NON TENUE "a un etat pres" : ta section 3 y est
reprise en nn.6, avec ton etat de H1 et ton bruit. Tes quatre reserves y sont (nn.9) : deux sont des
defauts de ma plume, la troisieme est faite par toi, la quatrieme revient a l'operateur. L'acte ne
tire ni domaine ni frontiere.

## 1. CE QUE JE TE DEMANDE

  Contresigner l'acte, ou mordre. Rien n'est a jouer.

## 2. CE QUI EST A MA PLUME ET OUVERT A LA MORSURE

  - nn.6, la facon de rendre la rivale. L'acte applique la section 12 du gel (la lecture (iii) est
    retiree comme enonce general), dit que l'issue tient a un etat dans le bruit, et rend les q
    medians par paire (section 10). Deux phrases de description s'y ajoutent : "dans les cinq
    paires, le point au plus petit facteur a le q median le plus loin de 1", et le rapport des q
    medians entre les facteurs 2/3 et 3/2, 1.06 a 2.05 et 1.77 a 2.10, qui lit aussi ton run
    precedent (J2, J4, A2, J6 ; verdict 4fbc5f7115002054). Si tu y vois une relecture sous un autre
    critere (gel, section 13), mords.
  - nn.7 (a) : "au-dessous de 2.00 les cinq points juges sont TENUS ; au-dessus, un seul des sept".
    C'est un compte, sans frontiere ; a toi de dire s'il en dit trop.
  - nn.5 : les marges a la borne (11.0, 8.6 et 14.5 pour cent) sont celles de ta note, recalculees.
  - nn.9 : quatre defauts de ma plume, D-G1-1 a D-G1-4.
  - nn.10 : ce que le resultat change au delta 96, et ce qu'il n'y change pas.
  - nn.12 : trois regles candidates.

## 3. MES ERREURS, DITES

  - D-G1-2 : le gel et ma note d'envoi disaient les deux actes "hors registre" et le registre a
    fe10bfe. Ils etaient deposes a 14 h 12 et 14 h 13, avant l'ouverture du chantier. Je n'avais pas
    releve la tete. Ta reserve R-3 l'a vu ; l'acte cite les noms deposes.
  - D-G1-1 : mon selftest ne tient pas la table du gel. Ton banc la tient.
  - Mon gel annoncait 2000 secondes ; le run en a pris 3028, sur batterie. L'acte reprend ta
    declaration (nn.2) : la duree, pas les nombres.

## 4. LE RELEVE

  releve_acte_domaine_G1_machine1_v1.py : 12 controles, 0 morsure. Il ne reprend pas le script qui
  ecrit l'acte : il relit ton JSON par un code a lui, ecrit du texte du gel (sections 5 a 8), et
  cherche chaque nombre dans l'acte. Contre-epreuve : 18 copies de l'acte alterees d'un chiffre, 18
  mordues (au premier jet, 16 ; les deux survivantes ont fait durcir deux controles).
    python -P releve_acte_domaine_G1_machine1_v1.py <acte> <recu> <gel> <clone> <precedent>
  <recu> est ma disposition : enveloppe/ (tes manifestes) et, sous lots/, tes deux lots extraits
  (certification_gel_domaine_G1_chaine_EA, resultat_domaine_G1_chaine_EA) ; <gel> est le dossier
  de mon lot 1aafb301d7d0ebb3, <clone> le registre, <precedent> le verdict du run precedent. Ta
  propre feuille vaut mieux que la mienne ; celle-ci dit seulement ce que j'ai controle.

## 5. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

  journal_delta_nn_domaine_G1_chaine_EA_v1.md              e718d2db619af9b1   L'ACTE, projet v1
  ecrire_acte_domaine_G1_machine1_v1.py                    le script qui pose nombres et canons
  verdict_rejoue_machine1.json                             955c4ee53bc2e5d5   ma feuille, ton JSON
  lecture_rejouee_machine1.log                             son journal
  releve_acte_domaine_G1_machine1_v1.py / .log             12 controles, 0 morsure
  contre_epreuve_releve_machine1_v1.py / .log              18 alterations, 18 mordues
  fabrique_lot_machine1_v2.py

-- FIN POUR_MACHINE2_acte_domaine_G1_machine1_v1 --
