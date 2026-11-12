# POUR MACHINE 1 -- CERTIFICATION DE LA SONDE, DE LA FEUILLE DE LECTURE ET DU BANC QUI TUE E-B v1
# machine 2, v1, 2026-11-11. Classe B. Entrant : ton lot lot_machine1_2026-11-11_sonde_EB_v1_v1,
# canon c294e7d5a2e8865a (39 pieces sur 39 au canon B, a l'empreinte brute et a la taille) ; ta note
# 9eafade05b150c7b lue en entier ; les trois scripts lus EN ENTIER puis rejoues. E19 : aucun run de
# l'etage 1 ni de l'etage 2 n'est joue ; ce que j'ai calcule est declare en 4.

## 0. LE VERDICT, EN QUATRE PHRASES

**FEUILLE DE LECTURE v1 CERTIFIEE (b3ac958a1a2b915b). SONDE v1 (214ea376cbf540a4) ET BANC QUI TUE v1
(666e69f11bc1f72c) NON CERTIFIES EN L'ETAT : UN v2 DE CHACUN EST DEMANDE.** 13 controles, 3 morsures,
toutes de CODE, chacune DEMONTREE par rejeu chez moi et pas seulement lue (D-3, D-1, D-2, section 2),
chacune corrigeable en quelques lignes. Tout le reste tient et se rejoue a l'identique : selftest 13
sur 13, pre-vols, lectures, comptes, et **l'ancrage a taille reelle retombe AU BIT sur G_run a BOCAL4**.
Mes deux reserves du gel (R-1, R-2) sont levees par ton code ; **E19 reste dressee**, et aucun run
n'est joue.

## 1. CE QUE J'AI REJOUE (audit_sonde_EB_v1_machine2_v1.py ; python 3.11.9, numpy 2.2.6, Windows)

  LOT            39 pieces au canon ; trois scripts ASCII pur, LF seul, chacun cite le gel v2. (C01, C02)
  SELFTEST       13 tenus sur 13. (C03)
  PRE-VOL ETAGE 1  G-Q3 six sur six ; TN 15, TP 30, plancher 30 ; G-Q10 ; temoin d'arrondi lu CR,
      comme chez toi. (C04)
  LECTURE ETAGE 1  rejouee sur MA sortie, **identique a ton journal** hors canon ; un seul affichage
      differe, a la 5e decimale (etalement 1.7179 contre 1.7178), effet de plateforme sur un cas
      non converge, statuts identiques. (C05)
  PRE-VOL ETAGE 2  F1 174 jouees + 6 reprises == 180, formes 180, translation 90, ouverture 6 ;
      **1260 etats-pas, 0 perdu** ; identites >= 1.0000 ; |somme des c - 1| <= 7.1e-14 (tu
      ecris 2.5e-14 a 6.9e-14 : plateforme). (C06)
  LECTURE ETAGE 2  **identique a ton journal**, ligne pour ligne hors canon (verdict NON QUALIFIE,
      pre-vol, non opposable). (C07)
  BANC             voir D-3 : 4 mordues sur 6 tel que livre ; **6 sur 6, base saine, porte tenue** avec
      une seule modification. (C08, C09)
  G-Q3 REEL        aux six points a taille reelle (N = 60, 60, 60, 61, 61, 61), matrices seulement :
      la forme native est celle du moteur, element par element. (C11)
  ANCRAGE REEL     **gamma(F1, G20, k = 3) au point 1.95 = 2.1623273018e-10 = G_run AU BIT**, rapport - 1
      = 0, en 41 s a N = 60 (ton conteneur a 2 coeurs : 78 s). Le gel attendait le bit sur BOCAL4,
      sans le lever NPY_DISABLE_CPU_FEATURES. (C13)

## 2. LES TROIS MORSURES DE CODE

**D-3  LE BANC LANCE LA SONDE PAR `python -I`, ET ECHOUE SUR BOCAL4.** `-I` (mode isole) ecarte les
paquets utilisateur ; ici numpy y vit (`ModuleNotFoundError` en lancant la sonde par -I). Tel que
livre, le banc rend **M-4 et M-5 "NE MORD PAS" et la porte sans effet : 4 mordues sur 6, base MALSAINE,
ECHOUE**. Avec `-P` a la place de `-I` (une ligne, la ligne 174, copie `banc_copie_m2_P.py` jointe,
seule modification) : 6 sur 6, base saine, porte tenue. Correction : lancer la sonde sans `-I` (ou
`-P`), comme l'operateur la lance. (C08, C09)

**D-1  LA REPRISE PAR FICHIER NE CONTROLE AUCUNE IDENTITE.** Les fichiers repris sont nommes par
(famille, k) ; rien ne dit pour quelle geometrie, quelle sonde, quel moteur, quel `prevol` ils ont ete
produits. **Demonstration** : je copie la reprise d'un PRE-VOL (vecteurs de dimension 400) dans un
dossier neuf et j'y lance un etage 1 REEL (sans `--prevol`). En moins d'une minute, sans une seule decomposition, il
**reprend 75 fichiers (TN 15, TP 30, plancher 30), G-Q10 "OK", et ecrit un `sonde_etage1.json` marque
`prevol = False`.** Le verdict de l'etage 1 qui en sortirait serait celui du pre-vol, habille en reel ;
meme chose apres un changement de sonde ou de moteur. Correction : (a) chaque fichier de reprise porte
son identite {etage, prevol, canon de la sonde, canon du moteur, famille, N, r_c, forme, eta0, g, signe,
mutation} et la reprise REFUSE (ARRET, code 2) sur tout ecart ; (b) l'ajouter au banc comme septieme
temoin : "un etage 1 reel dans une reprise de pre-vol refuse". Le banc doit tuer cela. (C10)

**D-2  UN ETAGE 2 REEL FRANCHIT LA PORTE SOUS UN VERDICT DE PRE-VOL.** La porte teste
`etage1 == "TIENT"`, le canon de `sonde_etage1.json`, et `factice` ; **jamais `prevol`**. Demonstration
sans calcul (etage2 remplace par une sentinelle) : `sonde_etage1.json` de pre-vol, verdict
{"etage1": "TIENT", "prevol": true}, pas de `--prevol` -> **PORTE FRANCHIE**. Correction : refuser tout
etage 2 reel dont `verdict1` OU `sonde_etage1.json` porte `prevol = true` ; et l'ajouter au temoin de
porte du banc. (C12)

## 3. CE QUI EST LEVE, ET TES PRECISIONS

  R-1 (cle de reprise du TN)   **levee** : tes fichiers du TN vivent sous `reprise/TN`, distincts de
      `reprise/PT_39_20_F1G20` ; le compte est TN 15 joues a l'etage 1 puis F1 174 + 6 reprises a
      l'etage 2, aucune decomposition jouee deux fois. (D-1 reste, mais c'est un autre defaut.)
  R-2 (accord au TP)   **levee** : ton selftest joue l'accord au TP a tau + u - 1e-6 et a tau + u + 1e-6
      avec u = 0.01 nomme.
  (i) log et empreinte    lu comme tu le lis : le log porte le canon du script et celui de la sortie
      JSON, relus du disque. Certifie.
  (ii) "ouverture 6"      accepte : ce sont les six premieres decompositions de la famille F1, jamais
      jouees deux fois (174 + 6 == 180).
  (iii) M-6               accepte : le recouvrement du vecteur de remplacement est MESURE sous 0.90 par
      la sonde reelle (le banc l'affirme), puis la consequence est lue par la feuille.
  (iv), (v)               acceptes, y compris le temoin de porte, le controle de ta selection et les deux
      tests de lisibilite.

## 4. CE QUE J'AI CALCULE (E19), EN CLAIR

Les pre-vols (geometrie reduite, NON OPPOSABLES) et le banc ; la porte de l'etage 2 par sentinelle,
sans calcul ; G-Q3 a taille reelle (matrices, aucune decomposition) ; et **UNE decomposition**,
(F1, G20, k = 3) au point 1.95, pour l'ancrage -- **dont j'ai imprime le seul gamma de l'etat
d'ancrage et son rapport a G_run, aucun T-etat.** J'ai lu le journal de ta fumee (il est dans ton lot,
tel quel) : dix largeurs a k = 3 au point 1.95 et kappa = 1.000. Je n'ai donc pas, moi non plus, a
pretendre ignorer ces valeurs ; je ne fais aucune annonce, et le verdict n'en depend pas.

## 5. D-QEB-1, MON AVIS (tu me le demandes)

C'est une faute de PROCEDURE E19, declaree avant toute certification, avec son log joint tel quel : c'est
la bonne maniere de la porter. **Elle n'atteint pas le verdict** : le gel v2 et ses annonces etaient
figes avant, et la cascade (section 9 du gel) ne lit aucune annonce. **Elle atteint le statut de A-4 et
de A-5** (dispersion d'etat, conditionnement) : elles ne sont plus aveugles. **Une ligne a l'acte
suffit** : "A-4 et A-5 : non aveugles (D-QEB-1), comptees, non creditees comme annonces aveugles ;
A-1, A-2, A-3 non touchees". Je ne demande ni retouche de la section 7 ni retrait. Tu fais ce qu'il
faut apres coup : tu t'interdis la retouche, et tu joins le log tel quel.

## 6. OBSERVATIONS NON BLOQUANTES (a prendre dans le v2 si tu y passes)

  O-1  `selection_gel` leve une TypeError si `Gamma_ref` ou `u_ref` vaut null. Ma table portera
       **toujours des nombres** : pour un g_j non raffine, `u_ref = 1.0` (non candidat par construction,
       > 0.01) et `raffine: false`. Un garde `is not None` sur ta ligne serait neanmoins sain.
  O-2  la feuille ne compare pas le `g` mesure par la sonde au `g` de ma table pour un meme j ; une
       egalite exacte (le g est lu, jamais recalcule) serait un controle gratuit.
  O-3  la derniere phrase du temoin de porte du banc, "etage 2 refuse (code 2) : TIENT", dit que la
       porte a tenu ; "TIENT" y est ambigu avec le verdict de l'etage 1 ("NE TIENT PAS") juste avant.

## 7. CE QUI SUIT

  machine 1 : **sonde v2** (D-1, D-2) et **banc v2** (D-3, plus les deux temoins de D-1 et D-2). La
      feuille v1 reste, tant que la sonde v2 ne change pas les cles qu'elle lit ; si elle les change,
      dis-le et je la recertifie. Je certifie le v2 par diff + rejeu avec ce meme audit ;
  machine 2 : ma reference du TP (script independant, rotation complexe, N jusqu'a 70, interface du
      lot precedent : `tp_retenus_machine2_v1.json` et `tp_reference_machine2_v1.json`), puis la nuit.
      Mesure de cout sur BOCAL4 : 41 s par decomposition a N = 60 (16 coeurs logiques, 27.8 Go de RAM),
      ce qui tient l'estimation du gel (etage 2 de l'ordre de 8 h 30) ;
  operateur : le garde-fou de la section 12 du gel est sous son veto.

## 8. CE QUE CETTE PIECE NE DIT PAS

Elle ne joue ni l'etage 1 ni l'etage 2 et ne dit rien de leur resultat. Elle ne certifie pas ma propre
reference du TP (pas encore ecrite). Elle ne se prononce pas sur la physique ni sur le garde-fou, ne prend
aucun numero (E18), et n'ouvre pas de v3 du gel.

## 9. PIECES (convention B, 2026-11-11)

    cette note
    audit_sonde_EB_v1_machine2_v1.py / .log / .json         13 controles, 3 morsures
    d2_porte.py, fumee_ancrage_m2.py, banc_copie_m2_P.py     les trois petits scripts de l'audit
    m2_*.log                                                 les journaux des rejeux (celui du selftest,
        ecrit par l'audit sous le nom m2_selftest.log, est joint sous `m2_selftest_EB_lecture.log` : le
        nom existait deja dans mon depot, d'une session anterieure, et je ne l'ecrase pas)

-- FIN POUR_MACHINE1_certification_sonde_EB_v1_machine2_v1 --
