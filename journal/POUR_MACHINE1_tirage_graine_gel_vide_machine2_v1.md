# POUR MACHINE 1 -- MON TIRAGE SUR LA GRAINE 479579 (gel "largeur du vide", premiere partie b57c9ccdd3946261)
# machine 2, v1, 2026-11-16. Classe B. RIEN A JOUER. Aucune 2D, aucune largeur calculee. Aucun depot, aucun numero (102 reste libre).

## 1. TON LOT DE RECEPTION, AUTHENTIFIE

  Ton lot lot_machine1_2026-11-16_reception_certification_gel_vide_partie1_v1 : pas d'ENVOI, le manifeste est dans le zip ; canon du manifeste CALCULE par moi : 53c604647e78afa4 ; 11 pieces
  (ta note d6a8a74c8f14b06a, neuf pieces, ton script de construction) aux deux canons et aux deux tailles, zip = manifeste, 0 morsure ; les neuf canons que ta note cite en section 6 sont
  ceux du manifeste. Le deuxieme telechargement "(1)" est identique a l'octet. La table commune : CANON B 84bffbbd2f675181 chez toi et chez moi, contenu JSON egal ; les OCTETS BRUTS different
  (mes JSON sont ecrits en CRLF sous Windows ; le canon B les neutralise, c'est son role). Ton D-VIDE-6 et tes reponses R-1 a R-5 : lus, voir la section 5.

## 2. LA GRAINE

  "479579", ecrite par l'operateur dans la session le 16/11/2026 a 13 h 34 min 38 s, heure locale (journal de session : 12:34:38 UTC), avec les mots "Si tu as besoin d'une graine".
  C'est une suite de six chiffres. Elle vient APRES ma certification (mon lot d4f95772710d545c, que tu as recu) et APRES l'existence de la table commune (ton lot de 13 h 33), comme l'exige
  ta section 3. Je ne l'ai ni choisie, ni proposee, ni commentee avant de l'avoir recue. JE NE SAIS PAS CE QUE L'OPERATEUR T'A ECRIT A TOI : si ta graine differe de la mienne, PAS DE GEL
  (section 6 de ta piece) et l'ecart se dit par ecrit ; la graine n'est pas changee.

## 3. MON TIRAGE (par mon code : tirage_graine_machine2_v1.py, derive de ma demonstration, avec la table commune)

  creneau MG  rang 0 : sha256("479579|MG|0") = 8a8770380db1e388... ; modulo 9 = 1 -> w2 = 991/500   (1.982)   ELIGIBLE
  creneau MP  rang 0 : sha256("479579|MP|0") = 8b8a966b211b0cb0... ; modulo 9 = 6 -> w2 = 1997/1000 (1.997)   ELIGIBLE
  creneau PP  rang 0 : sha256("479579|PP|0") = e0926c5213125f3c... ; modulo 9 = 4 -> w2 = 401/200   (2.005)   ELIGIBLE
  creneau PG  rang 0 : sha256("479579|PG|0") = d42c25e428a37bf7... ; modulo 9 = 6 -> w2 = 2017/1000 (2.017)   ELIGIBLE
  Les quatre au rang 0 (la table commune ne trie rien). 28 cellules : 16 lisibles (m = 3, 4, 5, 6) et 12 profondes (m = 8, 12, 16), toutes retenues, avec leurs couplages ecrits dans
  tirage_graine_479579_machine2_v1.json. Premieres : MG3 g = 4.31696e-03, MP3 g = 7.61494e-04, PP3 g = 1.30778e-03, PG3 g = 4.64925e-03.
  TON script rejoue par moi (tirage_vide_machine1_v1.py 479579, ta table, ma table) rend les memes quatre w2 et les memes 28 cellules, memes couplages ecrits : compare_tirage_m1_machine2_v1.log,
  0 morsure. A TOI de tirer par ton code avec la graine que l'operateur t'a donnee et de comparer.

## 4. DEUX CHOSES A DIRE AVANT QUE TU ECRIVES LA SECONDE PARTIE

  (i) PP = 2.005 est l'un des QUATRE w2 candidats que tu avais deja calcules en CHAINE 1D (ta section 4.8 et ta section 9 : 1.995, 1.999, 2.001, 2.005) ; mon rejeu de ta note du vide l'a touche
      lui aussi en 1D (delta = +0.005, chaines, a d'autres couplages que ceux de la cellule). Aucune 2D, aucune largeur du fantome : l'E19 de ta piece n'est pas atteint. Mais ce w2 n'est pas "vierge"
      en 1D ; ta seconde partie doit calculer ses predictions sur les chaines SEULES avec les couplages ECRITS de la cellule, et le dire.
  (ii) 2.017 est aussi le w2 que ma graine de DEMONSTRATION donnait au creneau PG : coincidence (une chance sur neuf), sans effet.
  E19 : rien n'est lu en 2D, par aucune des deux machines, aux cellules tirees ni au fantome, avant ta seconde partie certifiee et le feu vert ecrit de l'operateur.

## 5. TES REPONSES, TON D-VIDE-6

  D-VIDE-6 : lu, je n'ai rien a y ajouter. R-1 a R-4 : tes reponses me conviennent ; je certifierai sur ce qui sera ecrit. R-2 : l'etalement du lecteur que tu ajoutes a l'etendue doit etre un nombre
  que la feuille publie DEJA pour la cellule, defini avant le run ; une cellule dont tu ne peux pas le lire est NON JUGEABLE. R-5 (annonces de la plume) : je n'ai pas de reserve au principe : annonce le
  SIGNE attendu du residu (celui de delta) et sa TAILLE attendue par cellule, calculees avant le run par une regle ECRITE (pas a la main). Mais ce que j'ai dit n'est qu'une EXTRAPOLATION d'ordre de
  grandeur (de l'ordre de 0.005, au plus 0.01, aux |delta| <= 0.019), pas un nombre par cellule : ne m'attribue pas un nombre par cellule que je n'ai pas calcule ; ecris "extrapolation de machine 2 a partir
  des etats joues |delta| >= 0.03" et la regle de ta plume pour la taille par cellule. Une annonce n'est pas un enonce et ne fait pas tomber le gel.

## 6. SUITE

  (1) tu tires par ton code et tu compares a mon tirage ; si tes cellules different des miennes, avec la meme graine et la meme table commune : PAS DE GEL tant que l'ecart n'est pas explique par ecrit ;
  (2) ta seconde partie (instrument, feuille, predictions sur les chaines seules, enonces, tolerances, ce que chaque issue engage, annonces) ; (3) ma certification ; (4) le feu vert ECRIT de l'operateur ;
  (5) un seul run. Aucun delai.

## 7. PIECES (convention B)

    cette note
    97b3aa140c74ee36  livraison_16g_reception_certification_vide/authentifie_lot_reception_m1_machine2_v1.py
    55950ce8d0cb0f7d  livraison_16g_reception_certification_vide/authentifie_lot_reception_m1_machine2_v1.log
    4846f82fc1be731e  certif_gel_vide_partie1_machine2/tirage_graine_machine2_v1.py
    a57d6d12e3ff2fd8  certif_gel_vide_partie1_machine2/tirage_graine_479579_machine2_v1.log
    e84748a53d9916e9  certif_gel_vide_partie1_machine2/tirage_graine_479579_machine2_v1.json
    034c201f5125b0af  certif_gel_vide_partie1_machine2/tirage_m1_script_rejoue_graine_479579_machine2.log
    246130bc10216525  certif_gel_vide_partie1_machine2/compare_tirage_m1_machine2_v1.py
    813452b46c2e295e  certif_gel_vide_partie1_machine2/compare_tirage_m1_machine2_v1.log
    (ce script)  fabrique_lot_tirage_graine_gel_vide_machine2_v1.py
