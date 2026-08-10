PRE-ENREGISTREMENT M7 -- LE TEST QUANTIQUE DE H-PROFONDEUR A p=7
(gele avant l'ecriture de toute ligne de code ; bloc ASCII, canonique NFC+LF)

HISTORIQUE DU GEL
  v1, sha256 f477246ecfa53e127cedcb2ef29d146906a68be07fc36770f85058119f09a14a
  RETIRE avant toute ligne de code et toute donnee. Motif, releve a la
  certification machine 2 : la consequence retroactive de (b) chiffrait la
  tranche p=6 de M1 sur la nulle a n=4, alors que cette tranche compte n=3
  points -- (6, sqrt2) ayant ete EXCLU par la regle d'invariance. Correction
  en v2 : nulle a n=3 enumeree, l'argument en sort RENFORCE. Deux etiquettes
  de provenance ajoutees (reperes K4, exclusion de N=72). Aucune porte
  P-M7a/b/c/d ni aucun seuil n'est modifie.
  v2. Aucun autre gel anterieur pour M7. Le present bloc DURCIT une prediction
  deja gelee : S17-bis avait enregistre "si D(7) < D(5), H-PROFONDEUR predit
  rho(T,K7) > 0", et M6 a mesure D(7,0.10) = 1.633 < 2.229, ce qui arme la
  prediction. L'audit pre-gel de M7 montre que le critere de SIGNE seul n'est
  pas testable (voir DERIVATION (b)). Resserrer un critere AVANT mesure est
  licite ; le desserrer apres ne l'est pas. Le critere opposable a M7 est celui
  du present bloc, et la version faible de S17-bis est declaree perimee.

QUESTION
--------
H-PROFONDEUR (post-hoc, etiquetee depuis S17) : le signe de rho(T, K_p) sur la
carte en w2 est fixe par ce qui ORDONNE la carte de K -- canyon profond (p=3)
=> K ordonne par les resonances, que T alimente => anti-correlation ; canyon
plat (p>=4) => K ordonne par le fond => correlation positive.
M6 a ferme les deux jambes classiques : loi des porteurs (D ~ 1 aux pairs) et
decroissance de la profondeur (15.37 -> 2.23 -> 1.63). Reste la jambe
QUANTIQUE, qui est la seule ou l'hypothese engage une prediction risquee.

DERIVATIONS PREALABLES (verifiees AVANT le gel, ce sont des faits)
------------------------------------------------------------------
(a) CALIBRATION hbar_eff. Etat coherent apparie aux CI classiques :
    alpha_i = A_i sqrt(Delta w_i / 2), A1 = s(1+w2^2)/Delta, A2 = -s(1+w1^2)/Delta
    => nbar1(s) = s^2 (1+w2^2)^2 w1 / (2 Delta).
    Verification sur ancre : systeme canonique (1, sqrt2), rivage s* = 1.27
    -> nbar1 = 7.26, la note annonce "n1 ~ 7". ACCORD.
    Inversion gelee : s*_cible = sqrt(2 n_cible Delta) / (1 + w2^2), n_cible = 7.
    Puis g_cal = K7 / s*_cible^(p-2) avec p = 7, K7 mesure a g de reference.
(b) PUISSANCE DE rho. Distribution nulle exacte de Spearman, obtenue par
    enumeration des permutations (combinatoire, aucune donnee) :
      n = 3 : P(rho > 0) = 0.500 ; P(rho >= +1.00) = 0.167 ; P(>= +0.50) = 0.500
      n = 4 : P(rho > 0) = 0.458 ; P(rho >= +1.00) = 0.042 ; P(>= +0.80) = 0.167
      n = 6 : P(rho > 0) = 0.500 ; P(rho >= +1.00) = 0.0014 ;
              P(>= +0.90) = 0.0083 ; P(>= +0.80) = 0.029 ; P(>= +0.70) = 0.068
    (A n = 6, Somme d^2 est toujours paire, donc rho = 0 est inatteignable et
     P(rho > 0) vaut exactement 0.500.)
    CONSEQUENCE GELEE : un critere de SIGNE est un tirage a pile ou face et ne
    peut pas etre une porte. M7 mesure sur SIX points et exige une MAGNITUDE.
    CONSEQUENCE RETROACTIVE, a consigner, CORRIGEE EN v2 :
      - p=3 (n=4) : rho = -1.00 -> p = 0.042. Marginal, mais informatif.
      - p=4 (n=4) : rho = +0.20 -> en plein dans la nulle. Aucune information.
      - p=6 (n=3, car (6,sqrt2) EXCLU par l'invariance) : rho = +0.50 ->
        p = 0.500 EXACTEMENT. Information strictement nulle. Et a n=3 meme
        rho = +1.00 ne vaudrait que p = 0.167.
      - p=5 (M3) : rho = +1.00, mais la TAILLE de sa grille n'est pas etablie
        dans ce bloc. Si n=3, p = 0.167 et non 0.042. A VERIFIER sur les
        artefacts M3 avant toute citation de ce chiffre comme significatif.
        Aucune valeur de p n'est affirmee ici pour p=5.
(c) COQUILLE FIXE. S = {35 <= max(n1,n2) <= 45} a pour cardinal 46^2 - 35^2 =
    891 etats, identique a toute troncature N >= 46. Verifie.
(d) LE TEMOIN BORNE N'EXISTE PAS AUX DEGRES IMPAIRS. NULL+ tire sa valeur de
    "borne inferieurement donc aucune fuite possible par construction". Or
    +w1 n1 + w2 n2 + (g/p) x^p avec p IMPAIR est NON BORNE inferieurement
    (x^p -> -inf). Le controle NULL+ est donc STRUCTURELLEMENT indisponible a
    p = 3, 5, 7 -- ce qui explique apres coup pourquoi la campagne ne l'a jamais
    fait tourner qu'a p = 6. M7 ne pretendra pas l'avoir. Il utilise a la place
    le null FREE (g = 0), qui teste le pipeline mais PAS la dynamique, et le
    declare comme tel.

ETAGE 1 -- CLASSIQUE : QUI ORDONNE LA CARTE K7 ?
------------------------------------------------
Mesure de s*(p=7) puis K7 = g s*^5 sur SIX valeurs de w2 :
  {1.35, sqrt(2), 1.80, 2.00, 2.40, 2.85}
Les quatre premieres cases canoniques {1.35, sqrt2, 2.00, 2.85} sont celles de
M1/M3 : le sous-ensemble est conserve pour comparabilite. 1.80 et 2.40 sont
ajoutees pour la PUISSANCE de rho, et fixees ici, avant toute mesure.
Reperes, avec PROVENANCE ETIQUETEE (comparaison croisee entre codes, meme
regle qu'en G1 de M6) :
  K3 = 0.093 / 0.124 / 0.024 / 1.617   [code B, seance M1] -> argmin AU RESONANT
  K6 = 0.0011 / exclu / 0.053 / 2.148  [code B, seance M1] -> argmin BORD GAUCHE
  K4, DEUX jeux qui different jusqu'a 6 % :
      0.065 / 0.079 / 0.337 / 3.595    [machine 1, seance]
      0.0647 / 0.0840 / 0.3375 / 3.388 [machine 2, calib.json]
  Les deux donnent le MEME argmin (bord gauche) et le meme ordonnancement.
  Ces reperes servent d'ordonnancement uniquement ; aucune porte de M7 ne
  depend de leur valeur numerique.

P-M7a  ORDONNANCEMENT DE LA CARTE (porte prealable)
  K7(2.00) n'est PAS le minimum des six -> LIEN CONFIRME : canyon plat =>
    carte ordonnee par le fond. La prediction rho > 0 conserve sa derivation.
    [derivation : H-PROFONDEUR fait dependre le signe de ce qui ordonne K ;
     un canyon a D = 1.63 ne peut pas reordonner la carte, donc le point
     resonant ne doit pas etre le minimum, contrairement a p=3.]
  K7(2.00) EST le minimum des six -> LIEN REFUTE.
    [derivation de CETTE branche : la resonance ordonnerait la carte malgre un
     canyon plat, donc "la profondeur ordonne la carte" est faux. L'etage 2
     TOURNE QUAND MEME -- la mesure vaut d'etre faite -- mais sa prediction est
     declaree NON DERIVEE et le resultat est consigne SANS attente
     pre-enregistree. Il est INTERDIT de re-deriver une prediction de signe
     apres avoir vu l'etage 1 : ce serait la faute E15 a l'envers.]
  Position de l'argmin : consignee comme donnee dans tous les cas.

ETAGE 2 -- QUANTIQUE : LE SIGNE ET LA FORCE DE rho(T, K7)
---------------------------------------------------------
H = -w1 n1 + w2 n2 + (g/p) x^p , x = x1 + x2 , x_i = (a_i + a_i^dag)/sqrt(2 Delta w_i)
Diagonalisation exacte, troncatures N = 56 et 64. N = 72 est exclu POUR
COMPARABILITE avec les tranches M1/M3, qui sont mesurees a N = 56 et 64 ;
ce n'est PAS une contrainte machine -- machine 2 a diagonalise N = 72 sans
encombre pendant bundle5 (pic ~4 Go). L'exclusion est un choix de design.
Etat initial : coherent apparie, s = 0.7 s*_cible (rho_amp = 0.7, convention M1).
Observable : T_shell(psi0) = somme_k |<k|psi0>|^2 w_S(k), coquille FIXE de (c).

P-M7b  PORTE PRINCIPALE -- rho de Spearman entre T_shell et K7 sur les 6 points
  rho >= +0.80 AUX DEUX troncatures -> PREDICTION DE H-PROFONDEUR CONFIRMEE
    (p unilateral <= 0.029 par la nulle exacte de (b)).
    [derivation : canyon plat => carte de K ordonnee par le fond => T suit le
     fond et non les resonances => correlation positive forte.]
  rho <= -0.80 AUX DEUX troncatures -> REFUTEE.
    [derivation de CETTE branche : une anti-correlation forte signalerait une
     carte ordonnee par les resonances, ce qui exigerait un canyon profond a
     p=7 ; or M6 mesure D(7) = 1.633 < D(5) = 2.229. L'hypothese serait alors
     internement incoherente, et c'est le coeur de H-PROFONDEUR qui tombe,
     pas seulement sa jambe quantique.]
  Tout le reste, y compris des signes discordants entre N = 56 et N = 64, ou
  |rho| < 0.80 -> NON CONCLUANT.
  ANTI-ARRET-OPTIONNEL, gele : si rho tombe dans [0.60, 0.80), la manche N'EST
  PAS prolongee. Ajouter des points apres avoir vu le resultat serait de
  l'arret optionnel. Toute extension devra etre une manche nouvelle et gelee.
  Le p unilateral exact sera reporte dans tous les cas, calcule sur la nulle
  enumeree de (b), y compris quand la porte est NON CONCLUANTE.

P-M7c  COMPARABILITE (SECONDAIRE, AUCUNE PORTE)
  rho sur le sous-ensemble canonique 4 points, pour se comparer a M1/M3.
  Declare non testable en soi : a n = 4, P(rho >= +1) = 0.042 au mieux.

P-M7d  OPERATIONNALISATION (SECONDAIRE, AUCUNE PORTE)
  rho(T, C7) avec C7 = K7 / [(w2-1)^2 (1+w2)], rapporte a cote de rho(T,K7).
  Motif : M1 a montre que le choix de l'operationnalisation de la "robustesse
  classique" change rho au sein d'une meme tranche (rho(T,K4) = +0.20 contre
  rho(T,C) = +0.89). Les deux sont donc rapportes ; UN SEUL est une porte, et
  c'est K7, choisi ici pour comparabilite avec le titre de M1. Choisir apres
  coup celui qui arrange serait du double-dipping.

P-M7-null  PIPELINE (porte)
  FREE (g = 0) a w2 = 1.35 et 2.85, N = 64 : T_shell < 1e-12 -> PASSE.
  Sinon -> ARRET, le pipeline fabrique du poids de coquille.
  DECLARE : ce null teste la base, la coquille et les recouvrements, PAS la
  dynamique. Le null dynamique (temoin borne) n'existe pas a p impair, cf. (d).

SECONDAIRE SANS PORTE : comparaison a signe de fantome retourne
  +w1 n1 + w2 n2 + (g/p) x^p a w2 = 1.35 et 2.85, N = 64. Ce systeme n'est PAS
  borne (cf. (d)) : le rapport GHOST/retourne est consigne comme donnee brute,
  son interpretation n'est PAS fixee par ce gel, et aucune conclusion ne sera
  tiree de lui dans M7.

GARDES
  G1 REGRESSION (bloquante) : s*(p=7, w2=2.00, g=0.05) doit reproduire la
     valeur M6 0.39227 a <= 2 %. Meme code, meme definition : un ecart signale
     une rupture, pas une physique.
  G2 INVARIANCE : K7 a 2g sur w2 = 1.35 et 2.85, tolerance 10 %, reprise dense
     n = 96 sinon la ligne est EXCLUE de rho (regle M1, appliquee sans exception).
  G3 IDENTITE DE FORCE : somme des monomes = g(x1+x2)^(p-1), mesuree en erreur
     BACKWARD (ecart / echelle des termes sommes), tolerance 1e-12. La metrique
     backward est obligatoire : la somme explicite est mal conditionnee pres de
     x1 + x2 = 0 (defaut trouve au pre-vol de M6, ecart relatif 9.3e-1 a p=7
     pour une identite exacte a 5e-16 en backward).
  G4 PAS DE TEMPS : applique a la ligne la PLUS RAIDE, definie a priori comme
     celle qui maximise g * s*^(p-1), c'est-a-dire l'echelle de force -- et NON
     comme "le plus grand s*". Correction directe du defaut M6 : la garde y
     avait ete appliquee a p=4 alors que sa derivation invoquait p=7. Une garde
     s'applique la ou sa derivation la motive. dt/2, ecart <= 2 %, sinon ligne
     marquee NON FIABLE.
  G5 CALIBRATION : apres g_cal, re-mesurer s* ; |s* - s*_cible|/s*_cible <= 5 %
     sinon le point est EXCLU de rho (regle mecanique, aucune exception).
  G6 REPRESENTABILITE : poids de l'etat coherent initial hors base < 1e-8,
     sinon le point est EXCLU de rho.
  G7 TRONCATURE : rapport T_shell(56)/T_shell(64) consigne pour chaque point.
     AUCUNE porte dessus : S8 a etabli que la magnitude n'est pas convergee au
     fond de l'ile (x1.6-1.9 connus). Seul le SIGNE de rho est revendique, et
     P-M7b exige deja l'accord des deux troncatures.

PROGRAMME FIGE
  Classique (15 recherches) : 6 points a g = 0.05 ; 2 invariances a 2g ;
    6 re-mesures a g_cal ; 1 re-run G4 a dt/2.
  Quantique (16 diagonalisations) : 6 points x {N=56, N=64} GHOST = 12 ;
    FREE a 2 points, N=64 = 2 ; signe retourne a 2 points, N=64 = 2.
  Cout annonce : classique ~6 min ; quantique 20-40 min selon la machine.
  C'est la manche la plus lourde de la campagne.

MES ATTENTES (pour pouvoir avoir tort de mon propre fait)
  K7 argmin au bord gauche (1.35), K7(2.00) non minimal -> P-M7a confirmee.
  rho(T,K7) entre +0.4 et +0.9 : je m'attends a une confirmation, mais je
  considere NON CONCLUANT comme l'issue la plus probable apres elle, et je
  l'ecris avant la mesure pour ne pas pouvoir m'en plaindre apres.
  rho(T,C7) plus eleve que rho(T,K7), par analogie avec p=4 en M1.
  T_shell de l'ordre de 1e-3 a 1e-1 ; FREE a la limite de la representation.

LIMITATIONS DECLAREES
  - x^7 couple jusqu'a Delta n = 7 : les effets de troncature sont plus durs
    qu'a p = 3 ou 4. C'est la raison de l'exigence d'accord entre N = 56 et 64.
  - n = 6 reste un petit echantillon. La porte a 0.80 est calibree sur la nulle
    exacte, mais la puissance contre une alternative faible reste basse.
  - g varie d'un point a l'autre par construction (calibration a nbar fixe) :
    la degenerescence C / g_eff signalee en M1 n'est pas levee ici, et M7 ne
    pretend pas identifier le mediateur. Il teste un SIGNE, pas un mecanisme.
  - Aucun temoin dynamique borne (cf. (d)) : c'est la faiblesse structurelle de
    tout resultat quantique a degre impair, et elle vaut aussi pour M1 (p=3)
    et M3 (p=5) retroactivement.

IMPLEMENTATION
  m7_profondeur_v1.py (nom versionne), moteur classique repris de
  m6_porteurs_v1.py sans modification, moteur quantique autonome, ecrit
  uniquement out/m7_results.json (incremental, une ecriture apres chaque point).
  Gel jumeau dans le docstring : bloc de "PRE-ENREGISTREMENT M7" jusqu'a
  "=== FIN DU GEL M7 ===