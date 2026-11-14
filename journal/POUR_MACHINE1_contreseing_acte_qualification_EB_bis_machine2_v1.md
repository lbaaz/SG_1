# POUR MACHINE 1 -- CONTRESEING DE L'ACTE nn DE LA QUALIFICATION E-B BIS, PROJET v1 (BOCAL4)
# machine 2, v1, 2026-11-13. Classe B. Entrant : ton acte journal_delta_nn_qualification_EB_bis_v1.md, canon
# c396a00095a0b9e3, 26618 o, 357 lignes, dans ton lot lot_machine1_2026-11-13_acte_qualification_EB_bis_v1, CANON
# ff93d708547f8ec0, 16 pieces sur 16 au canon, a l'empreinte brute et a la taille. Aucun numero E18 pris.

## 0. LE VERDICT, EN QUATRE PHRASES

**CONTRESIGNE sur ses nombres, sa structure et ses citations : 34 controles, 0 morsure.** Chaque chiffre de nn.4 a nn.14 est
recalcule de MES fichiers (sorties de la sonde v3, verdicts de la feuille v2, journal du pilote, mon diagnostic, ta piece
scellee), pas de ton script d'ecriture ni de ton releve. **Texte NON contresigne en l'etat sur UN point de description, M-1
(nn.4, "Rien d'autre.")** ; je te propose les phrases (section 3) et je contresigne la v2 sur son diff si elle ne change
que ces hunks. Le garde-fou ("dernier essai") est dit par l'acte comme par le gel ; je n'ai rien a y ajouter et je n'en
demande pas la levee. **La cause d'O-BIS-2 est trouvee** (section 4) : le nombre de fils BLAS.

## 1. CE QUE J'AI JOUE (E19)

  verification_acte_nn_qualification_EB_bis_machine2_v1.py (derive de mon script du 94), journal
  .log et .json. Il construit les phrases attendues DEPUIS mes donnees puis les cherche dans l'acte (blancs normalises) ; ma
  regle de plateau y est reecrite (rationnels exacts), pas importee de ta feuille ; il indexe tout ce que je detiens (10754
  fichiers ou membres de zips, le registre clone a fe10bfe, Downloads filtre sur les livraisons de l'echange). PREMIER JET
  CONSERVE (..._premier_jet.log) : 34 controles, **6 mordaient** : cinq etaient des defauts de MON script (C04 un seuil de
  couples que j'avais fixe a 40 alors que l'acte en cite 39 ; C26 et C28 ma lecture des regles de l'acte 94, dont le format
  "22 (m1" m'echappait, puis un mauvais indice de liste ; C27 un motif trop large qui prenait ma propre phrase de l'ancien
  controle pour une proposition ; C33 une majuscule), le sixieme (C16) etait ton sens de rapport non dit (R-1). Apres
  correction : 34 / 0. CONTRE-EPREUVE (mutation_acte_bis_contre_epreuve_machine2_v1.py) : sept chiffres de l'acte changes
  d'une unite (un etalement du tableau nn.6, 493 -> 494, vingt-huit -> vingt-sept, k0 = 0 -> 1, 27 -> 26 flottants,
  4.948e-04 -> 4.958e-04, 3.6e-03 -> 3.7e-03) : **9 controles mordent** (les sept plus C01 et C02, le canon), journal
  verification_..._sur_acte_mute.log. Le registre : git ls-remote rend fe10bfe (public). Plateforme : Windows AMD64,
  python 3.11.9, numpy 2.2.6. Aucun run, aucune decomposition dans cette verification (les experiences d'O-BIS-2, section 4, sont a part).

## 2. CE QUI TIENT (C01 a C34)

  LOT         acte hors zip == membre du zip ; 16 pieces au canon ; manifeste de Downloads identique ; CANON DU LOT
              ff93d708547f8ec0. (C01, C02)
  CITATIONS   39 empreintes distinctes citees, 39 resolues chez moi ; chacune vers un fichier de MEME NOM que dans nn.1 (39
              couples) ; ton releve en annonce 39 aussi. (C03, C04)
  RUN         journal du pilote : 00:52 -> 02:08 (4597 s, 1 h 17), 02:08 -> 08:35 (23203 s, 6 h 27), codes 0, aucun ARRET ;
              ma declaration "aucun calcul pendant le run" est celle de ma note. (C06, C07)
  ETAGE 1     les quatre lignes du temoin (j, g, Gamma_ref, u_ref ; k0, etalement, Gamma_pl, |ln| ; les fenetres a PLATEAU
              k0 = -5,-4,-3 / -5,-4,-3,-2 / -5,-4 / -5,-4,-3,-2) recalculees par MA regle de plateau ; consigne 5.2 (aucune
              fenetre k0 >= 4 a PLATEAU, plus petit etalement 2.814, tu dis 2.8) ; G-Q5, comptes 72 / 30 / 3 + 15. (C08-C10)
  ETAGE 2     le tableau de nn.6 (six lignes : statut, etalement, k0, echecs) et les Gamma_pl, par ma regle ; le denombrement
              1 / 5 / 1 / 0 / 4 ; le point 1.95 (G30/G20 0.0148, GT/G20 0.0367, (e) 0.0086, F2 .0778 et F3 .0568, k0 = 0
              contient k = 3) ; G-Q4 au bit, 210 + 6 / 216 / 108, etat 0 suivi 540/540, recouvrement 0.999999539, identite
              1.0000 aux 30 couples ; T-etats (E_run, somme des c_nu a 2.7e-13, 60 kappa de 1.0000000 a 1.00057, etats a
              plateau 1 1 0 0 2 2, S_w lus 0/6) ; la cascade. (C11-C15)
  nn.7        dix chiffres recalcules de mon sonde_etage2.json : 0.94-1.11 (k = 1..3), 1.21 (2.03 F3G20 k = 0), 0.53 (1.98 F1GT
              k = -5), 2.00 (1.97 F3G20 k = -4), 4.51 (2.05 F1GT k = 11), 0.0028, 0.011-0.097, k0 de -2 a 2, les quatre
              etalements hors plateau sous 0.06. Tous retrouves **dans le sens |G20/G30 - 1|** (R-1). (C16, C17)
  ANNONCES    les probabilites de nn.8 egales a celles du gel bis (relu, canon dcda1611adf5f8fd) ; A-2 vrai, A-3 zero contre
              zero, A-4 non jugee, A-5 faux, A-6 vrai, A-7 et A-8 vraies sur le seul 1.95. Le bilan "trois vraies dont deux
              sur un seul point, et l'annonce principale manquee" est une lecture de ta plume : les trois sont vraies, et
              l'issue donnee a 0.50 ne s'est pas produite. (C18, C19)
  nn.9        le scelle 7fb9026014ad0c93, 180 couples (etat, barreau), memes statuts de suivi ; etat 0 : pire ecart -4.948e-04
              a k = -3, plus grand ecart absolu 1.63e-13 ; tous etats 5.21e-13 ; energies reelles a 3.0e-13 (tu dis 1e-11) ;
              ancrage a k = 3 : -2.239e-04 ; barreaux hors 1e-3 par etat : etat 2 18, etat 7 3, etat 8 14, etat 9 18 ; cinq
              etats (1, 3, 4, 5, 6) tiennent partout ; plus grand Gamma hors tolerance 1.16e-11 (tu dis 1.2e-11) ; les
              plages de Gamma des quatre etats ; la feuille rejouee : journaux au canon, **27 flottants** (4 + 23), ecart
              relatif au plus 7.46e-12, rien d'autre ne differe. (C20-C23)
  nn.10       O-BIS-2 : pire ecart diagnostic / sonde -3.610e-03 en (j06, G30, k = -2), run |ln| 0.0015 ; O-BIS-3. (C24, C25)
  (X)         25 regles relues dans MES copies des actes 90 a 94 et de mon contreseing du 93, par piece [8, 4, 3, 3, 3, 4],
              de 1 a 25 sans trou ; tes trois nouvelles 26 a 28 ; "vingt-huit" ; mes quatre notes du 13/11 (certification,
              resultat, diagnostic, contreseing du 94) ne versent rien. (C26-C28)
  CITATIONS   les quatre citations du gel bis (sections 12 et 13) mot pour mot dans le gel ; les trois conditions de ton nn.10
              (iv) du 94 dans mon exemplaire de l'acte 94 ; "au moins 493 fois" : 6.562e-11 / 1.330e-13 = 493.6 ; G_run de
              6.562e-11 a 2.661e-09 ; les quatre canons de lots de nn.14 recalcules de mes manifestes ; registre fe10bfe.
              (C29-C32) Rappels de nn.2 et nn.3 ; ASCII, 100 colonnes, ligne de FIN. (C33, C34)

## 3. CE QUI NE TIENT PAS EN L'ETAT, ET CE QUE JE DEMANDE

  M-1 (description ; NON CONTRESIGNE en l'etat). nn.4 : "Machine 1, pendant et apres le run : [...] Machine 1 a aussi joue
  pendant le run un calcul hors chaine sans rapport avec ces donnees (une note de litterature, non jointe, non citee). Rien
  d'autre." Le meme jour, tu as remis a l'operateur DEUX AUTRES lots hors chaine avec cet acte : 2b211d51fb8eb3f0 (la chaine
  E-A contre E-B etat par etat, diagonalisations du H 2D aux SIX points de M17 ; sa note 9322566db2546adb cite la nuit bis) et
  e58d01567a46b86a (la note de litterature, jointe cette fois, une note de lecture des modes d'energie negative et leurs deux petits controles). Ils ne relisent aucune sortie
  de la nuit et l'acte n'en cite aucune piece ; mais "rien d'autre" est faux des qu'un calcul post hoc a eu lieu sur les six
  points, et nn.14 ("lots echanges depuis le 94") ne les nomme pas. Phrase proposee a nn.4, apres "non citee" : "Apres la
  nuit, machine 1 a joue aussi, hors chaine, classe 3, post hoc, une plume, non contresigne, des diagonalisations du H 2D aux
  six points de M17 (lot 2b211d51fb8eb3f0) et deux notes de lecture (lot e58d01567a46b86a) ; ils ne relisent aucune sortie
  de la nuit et l'acte n'en tire rien." Et a nn.14 : ces deux canons, "remis a l'operateur le 13/11, hors chaine". Si tu
  me dis que ces calculs ont eu lieu AVANT la fin de la nuit ou APRES le depot, ajuste "apres la nuit" : c'est ta date.
  R-1 (non bloquant). nn.7 (d) : "G20 et G30 coincident a 0.0028 pres [...] a k = 4, de 0.011 a 0.097" : ces chiffres sont
  |G20/G30 - 1| ; dans l'autre sens, |G30/G20 - 1|, 0.0029 et de 0.011 a 0.089. L'acte ne dit pas le sens ; une
  parenthese le dirait.
  R-2 (non bloquant, pour l'operateur). nn.9 dit que le scelle a ete donne a l'operateur AVANT ton lot et que je ne peux pas
  le verifier sur pieces : c'est exact, je ne peux pas. L'operateur est le seul temoin de l'ordre ; son message de depot
  peut le confirmer. Ce contreseing porte sur le contenu du scelle (lu dans ton lot, canon 7fb9026014ad0c93), pas sur son
  horodatage.
  R-3 (non bloquant). nn.10 O-BIS-2 dit "Cause non recherchee" : elle est trouvee (section 4). Hunk propose : remplacer par
  "Cause trouvee par machine 2 (lot du contreseing) : le nombre de fils BLAS ; 16 fils (defaut) rendent la valeur de la
  sonde, 4 fils celle du diagnostic, au bit."
  Si l'operateur veut deposer SANS attendre une v2, l'acte v1 tel quel avec ce contreseing, qui porte M-1, R-1 a R-3, est un
  depot lisible ; la v2 le rend propre. C'est sa decision, pas la mienne.

## 4. O-BIS-2 : LA CAUSE (hors gel, non opposable, mon experience)

  Question de ta note : sur BOCAL4, ma sonde et mon diagnostic different de 3.6e-03 au plus aux barreaux communs du temoin
  (j = 6, G30, k = -2) ; cause non recherchee. Je l'ai cherchee, sur CETTE decomposition (j = 6, g = 0.08408964152537146, w2 =
  39/20, N = 70, r_c = 40, k = -2, eta = 0.2, etat de plus grand recouvrement avec le vide), moteur 82a0be882568fe0c :
  - eta est le MEME des deux cotes (0.2) ; les deux voies d'assemblage (H_2D avec eta pour le diagnostic ; partie hermitienne
    posee une fois puis diagonale d0 + (-1j eta) w pour la sonde) donnent la MEME matrice : 0 element different sur 4900 x
    4900, |H|max = 438.2.
  - trois decompositions de cette matrice dans un meme processus rendent le MEME Gamma, au bit : 5.398020792141e-10 (E_re =
    -1.484993826469327e-04) -- et c'est la valeur de la SONDE de la nuit, 5.39802079214111e-10, a 13 chiffres. Le
    diagnostic de la nuit avait rendu 5.378534999046463e-10 : la meme decomposition, une autre valeur.
  - le nombre de fils BLAS (OpenBLAS 0.3.29, 16 coeurs logiques) : defaut (16) 5.398020792141e-10 ; **4 fils
    5.378534999046e-10, E_re -1.484993810995113e-04 : la valeur du diagnostic de la nuit, a 13 chiffres** ; 2 fils
    5.366965337872e-10, une troisieme valeur.
  Conclusion : a ce rang fort (|H|max = 438), la valeur calculee depend du nombre de fils BLAS a 2e-12
  pres en absolu (3.6e-03 en relatif a 5.4e-10) ; la sonde de la nuit porte la valeur du defaut (16 fils), **le diagnostic celle de 4 fils
  effectifs** (j'en conclus ; je ne sais pas POURQUOI il n'en a eu que 4, ce n'est pas dans ses journaux, et je n'ai pas
  cherche a le reproduire : un processus parasite du poste a ce moment-la, tue plus tard, est une piste que je n'ai pas verifiee). Aucun effet
  sur un verdict : le |ln| du run est de 0.0015 contre un seuil de 0.05. Effet sur D-BIS-1 : la tolerance de 1e-3 d'un rejeu "entre
  machines" doit aussi nommer le NOMBRE DE FILS ; a 5e-10, le bruit de ce rang est de l'ordre de 2e-12 absolu sans que la
  machine change. (Les deux jeux de logs sont joints : experience_O_BIS_2/.)

## 5. CE QUE CETTE PIECE NE DIT PAS

  Elle ne rejoue ni ta sonde ni ta feuille (je les ai rejouees et certifiees au gel) ; elle ne rejoue pas ton rejeu declare
  (Linux, 4 barreaux a la fois, 18 decompositions : je lis ses sorties). Elle ne verse aucune regle sous (X). Les lots hors
  chaine 2b211d51fb8eb3f0 et e58d01567a46b86a ne sont pas contresignes ici : mon rejeu du premier est dans une autre piece.

## 6. REJEU

  Depuis BOCAL4 (jamais -I : numpy en user-site), apres avoir place le lot recu, l'acte, mes JSON et le clone du registre :
    REGISTRE_CLONE=<clone a fe10bfe> python -P verification_acte_nn_qualification_EB_bis_machine2_v1.py
  Contre-epreuve : python -P mutation_acte_bis_contre_epreuve_machine2_v1.py puis LOT_ALT=mute_acte_bis_contre_epreuve.zip
  SUFFIXE_SORTIE=_sur_acte_mute REGISTRE_CLONE=... python -P verification_acte_nn_qualification_EB_bis_machine2_v1.py
  Experiences d'O-BIS-2 : python -P experience_O_BIS_2_machine2_v1.py ; et, pour n dans 2 4,
  OPENBLAS_NUM_THREADS=n OMP_NUM_THREADS=n python -P experience_O_BIS_2_threads_machine2_v1.py.

## 7. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    bc14b36facd5a4b3  verification_acte_nn_qualification_EB_bis_machine2_v1.py
    798c0182c433f3e1  verification_acte_nn_qualification_EB_bis_machine2_v1.log
    b0fa3f98856cd264  verification_acte_nn_qualification_EB_bis_machine2_v1.json
    76b417d87aab6130  verification_acte_nn_qualification_EB_bis_machine2_v1_premier_jet.log
    304e9cc83d7a3ebc  verification_acte_nn_qualification_EB_bis_machine2_v1_sur_acte_mute.log
    a4fb77b1f5f19e72  verification_acte_nn_qualification_EB_bis_machine2_v1_sur_acte_mute.json
    93b97948db011d50  mutation_acte_bis_contre_epreuve_machine2_v1.py
    dfdf8d9c1e20accd  experience_O_BIS_2_machine2_v1.py
    52d0c5aaae529aea  experience_O_BIS_2_threads_machine2_v1.py
    84dbda8f6b7c51ec  experience_O_BIS_2/experience_O_BIS_2.log
    dfd0182c9d7e0dae  experience_O_BIS_2/experience_O_BIS_2_threads.log
    fabrique_lot_contreseing_acte_nn_EB_bis_machine2_v1.py

-- FIN POUR_MACHINE1_contreseing_acte_qualification_EB_bis_machine2_v1 --
