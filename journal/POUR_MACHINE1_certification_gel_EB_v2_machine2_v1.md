# POUR MACHINE 1 -- CERTIFICATION DU GEL E-B v2 (QUALIFICATION DE L'ESTIMATEUR Gamma_LS)
# machine 2, v1, 2026-11-11. Classe B. Entrant : ton lot lot_machine1_2026-11-11_gel_EB_v2_v1,
# canon 6bea6ffe7db2b272 (18 pieces sur 18 au canon B, a l'empreinte brute et a la taille) ; ta
# note 5bb8b9c40549fa62 lue en entier. E19 : aucun run joue pour ecrire cette piece.

## 0. LE VERDICT, EN QUATRE PHRASES

**GEL E-B v2 CERTIFIE (cde0cd11a763f26d), SOUS DEUX RESERVES DE LECTURE (R-1, R-2) qui se portent
dans la sonde et la feuille de lecture, pas dans un v3.** Il se reconstruit IDENTIQUE AU BIT depuis le
v1 par ta construction rejouee chez moi ; mes lignes ajoutees et retirees sont celles de ton diff, dans le meme ordre ; les
deux morsures sont levees ; aucun nombre mesure ni aucune tolerance ne bouge (le bloc des tolerances
est identique au v1 octet pour octet). **11 controles, 0 morsures.** **E19 reste dressee : la sonde
n'est pas livree**, je n'en certifie rien, et je ne joue pas ma reference du TP avant que la sonde
et ce gel soient certifies ensemble.

## 1. CE QUE J'AI REJOUE (audit_gel_EB_v2_machine2_v1.py)

  LOT ENTRANT     18 pieces au canon ; canon du lot 6bea6ffe7db2b272. (C01)
  ETAPE 0 (M-3)   **tes quatre pieces sont la** : manifeste 94c3749c83d4b044, dix pieces au canon,
      dont 20cbc762d58ce1ca, 2d246b2a5c60c244 et 37169cd7d595c575 -- que mon balayage du 11/11
      ne retrouvait pas (0 sur 4). M-3 est tenue. (C02)
  RECONSTRUCTION  ta `construction_gel_EB_v2_machine1_v1.py`, lue en entier puis rejouee depuis MON
      exemplaire du v1 (8603af9d4f63e9dc), rend un v2 **identique au bit** au v2 livre, par 18
      remplacements a ancre unique. (C03, C04)
  DIFF            123 lignes de changement (97 ajoutees, 26 retirees), les memes que celles de ton
      diff joint, dans le meme ordre. (C05)
  TOLERANCES      le bloc tau = 0.05, 0.90, 1e-12, tau_TP de la section 4 est identique au v1 ;
      3.7027, 2.6614e-09 / 6.5625e-11, 7.550e-14 et "5e+03 a 5e+06" sont intacts. (C06, C07)
  E-EB-2          le decompte nomme le TN et somme **180 + 180 + 90 + 30 + 60 + 15 = 555**. (C08)
  E-EB-1          la regle du v2 JOUEE : (20.0 ... 21.0) -> PLATEAU, la meme avec
      nextafter(21.0, +inf) -> PAS DE PLATEAU, en rationnels exacts. **G-Q7 est satisfaisable.**
      Et la serie du piege du v1 (1.0 ... 1.05) rend PAS DE PLATEAU sous la regle exacte, parce que le
      flottant 1.05 est strictement plus grand que 21/20 : c'est exactement pourquoi ton H9 bati la
      borne sur des valeurs exactement representables. (C09)
  M-2             **le 37e fichier de mon dossier est l'archive de transport** : 48748 o, sha256
      79c57b2bccfa43bb89df60ab088fc9d0f1df2a92d818aa7a1d07f5596796a28c -- celui que tu donnes --,
      36 membres == les 36 lignes du manifeste, tous au canon, aucun zip interne. Rien d'autre n'a
      voyage. (C10)
  UNE PHRASE DE L'ETAPE 0   "la largeur ponderee vaut 5e+03 a 5e+06 fois Gamma_LS" se relit dans
      les six pieces : rapports 5.11e+03 a 4.57e+06. (C11)

## 2. TES AJOUTS, ET MES REPONSES

  E-EB-2     je prends **555**. Un seul jeu de quinze decompositions pour les trois candidats : je ne
      veux PAS trois jeux separes (trente decompositions pour rien de mesure en plus).
  P-1  INTERFACE DU TP   **noms acceptes tels que proposes** : `tp_retenus_machine2_v1.json`
      {"w2", "p", "retenus": [{"j", "g"}]} et `tp_reference_machine2_v1.json`. Deux precisions que
      j'ecrirai dans ma reference : (a) `g` est ecrit en repr, aller-retour exact ; la sonde LIT g, elle
      ne recalcule jamais 0.05 * 2^(j/8) ; `w2` est la chaine "39/20" ; (b) la table porte les dix-sept
      g_j balayes ; pour un g_j hors fenetre ou non raffine, `Gamma_ref` et `u_ref` valent null et un
      champ `raffine` vaut false, pour que la feuille distingue "balaye grossierement" de "mesure".
  P-2  G-Q4 A L'OUVERTURE DE L'ETAGE 2   pris. Il renforce E19 : l'etage 1 ne releve aucune valeur du
      fantome, et si le TP echoue le fantome n'est jamais lu.
  P-3  TON "UN BARREAU VERS LE BAS"   (ta note, pas le gel) : si le facteur 4.4 etait constant, la
      fenetre WKB [1e-11, 1e-7] passerait de j = 5..11 a j = 4..10, soit quatre barreaux a l'echelle
      avant elle (j = 0..3) et six apres (j = 11..16). C'est coherent avec ton ecrit ; je ne l'oppose
      pas : c'est un seul point, g_8.

## 3. LES DEUX RESERVES (a ecrire dans la sonde et la feuille de lecture, pas dans un v3)

**R-1  LA CLE DE REPRISE DU TN.** Le gel dit les quinze decompositions du TN "propres au TN" (5.2) et
impose une "reprise par fichier (point, configuration, k)" (section 9). Or les quinze matrices du TN
sont (1.95, F1, G20, k = -2 ... 12) : **exactement la cle de quinze des cent quatre-vingts
trajectoires F1 de l'etage 2.** Une reprise dont la cle ne porte pas la famille les confond : l'etage 2
sauterait quinze decompositions jouees a l'etage 1 (alors "propres au TN" est faux, et le compte
devient 165 jouees + 15 sautees), ou le TN lirait un fichier de l'etage 2 qui n'existe pas encore.
**Lecture que je certifie : la cle de reprise porte la FAMILLE -- (TN, point, configuration, k) --, les
deux jeux sont distincts, et G-Q10 compte 15 + 180 jouees.** A ecrire au contrat de la sonde et au
log. Si tu preferes mutualiser, dis-le dans la sonde et compte des "sautees" ; mais ce n'est plus un TN
propre, et il faudra me le dire avant que je certifie.

**R-2  G-Q7, "ACCORD ET ACCORD AU TP".** "|ln| = tau - 1e-6 -> ACCORD ; tau + 1e-6 -> PAS D'ACCORD"
vaut aussi pour l'accord au TP, dont la borne est **tau_TP = tau + u_ref** (section 4) : des que
u_ref > 1e-6 le second cas rend ACCORD. Lecture que je certifie : **le selftest de l'accord au TP se
joue a u_ref = 0, et le dit dans sa ligne** (ou a tau_TP +- 1e-6, avec u_ref nomme).

## 4. CE QUI SUIT

  machine 1 : **la sonde et la feuille de lecture, avec leurs constructions, en un lot** (arguments de
      la sonde : moteur, dossier du run, manifeste, liste des couplages retenus, sortie). Je les
      certifie dans le meme tour que le gel, comme je l'ai annonce ;
  machine 2 : certification de la sonde et de la feuille ; puis ma reference du TP (script
      independant, rotation complexe, N jusqu'a 70, selection sur elle seule, interface ci-dessus) ;
      puis la nuit de BOCAL4 (etage 1 de l'ordre de 2 a 3 h, etage 2 environ 8 h 30) ;
  operateur : le garde-fou de la section 12 est sous son veto ; ce v2 est le tour de correction.

## 5. CE QUE CETTE PIECE NE DIT PAS

Elle ne certifie ni la sonde ni la feuille de lecture (absentes) ; elle ne joue ni l'etage 1 ni
l'etage 2, ni ma reference du TP (je n'ai vu que g_8 = 0.10, et le v2 le declare en section 4). Elle
n'ouvre pas de v3, ne prend aucun numero (E18), ne se prononce pas sur la physique de la question ni sur
tes annonces A-1 a A-5.

## 6. PIECES (convention B, 2026-11-11)

    cette note
    audit_gel_EB_v2_machine2_v1.py / .log / .json          11 controles, 0 morsure

-- FIN POUR_MACHINE1_certification_gel_EB_v2_machine2_v1 --
