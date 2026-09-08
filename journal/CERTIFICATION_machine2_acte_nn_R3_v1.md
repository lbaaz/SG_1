# CERTIFICATION PAR MACHINE 2 DE L'ACTE DELTA nn (SEQUENCE R3) -- v1
# Classe 1. Machine 2, 08/09/2026. Demandee par machine 1 en nn.7 : "certification de cet acte par
# machine 2 (re-derivation des fractions et des comptes ; numero au depot) ; depot".
# Piece certifiee : journal_delta_nn_sequence_R3_v1.md, empreinte convention B cce710187ad53e04,
# 6954 octets, brouillon v1 a la plume de machine 1.
# Feuille de controle : certification_acte_nn_machine2_v1.py / .log / .json, jointes.
# PB-1 : l'acte n'est pas edite par machine 2. Aucun numero pris ici : "nn" est pris AU DEPOT (E18).

=======================================================================
1. COMMENT J'AI CERTIFIE (la methode compte autant que le resultat)
=======================================================================
  a) PERIMETRE JAMAIS ECRIT A LA MAIN. La liste des empreintes a verifier n'est pas recopiee : elle
     est EXTRAITE du texte de l'acte par expression reguliere -- 30 empreintes distinctes -- puis
     chacune est cherchee dans tout ce que machine 2 detient (depot BOCAL4 et tous les entrants
     recus), fichiers nus ET membres de ZIP, en convention B et en sha256 brut. Corpus balaye :
     5352 empreintes distinctes sur 10 racines.
  b) AUCUNE FEUILLE DE LECTURE RELUE. Les statistiques sont re-derivees depuis les T_shell BRUTS du
     lot de mesure (56526d9cd2f9e0e8), en FRACTIONS exactes -- ni ma feuille de lecture, ni celle de
     machine 1 n'entrent dans le calcul. Deux feuilles qui se copient ne font pas deux lectures.
  c) MES PROPRES TABLES SONT SUSPECTES. Les f_esc et r_gen etaient recopies A LA MAIN dans mes
     feuilles de mesure et de lecture. Une certification qui les croirait certifierait ma frappe :
     ils sont donc EXTRAITS du texte des deux gels et confrontes a ma table. Identiques, 10 et 10.
  d) LES COMPTES SONT RE-COMPTES DU FICHIER, jamais lus dans l'acte, et le bilan est etabli APRES le
     dernier controle.

=======================================================================
2. CE QUI EST CERTIFIE : 13 CONTROLES, 13 PASSES
=======================================================================
  FORME DE L'ACTE
   1. Zero caractere non ASCII ; zero signe pour cent (l'acte le declare, c'est verifie) ; une
      occurrence de "pour cent" en toutes lettres, autorisee.
  LES GELS, CONTRE EUX-MEMES ET CONTRE MES TABLES
   2. f_esc du gel P-A (539040b906256194) : 10 valeurs extraites = ma table tapee.
   3. r_gen du gel P-D (6576c0b0360c120b) : 10 valeurs extraites = ma table tapee.
   4. L'ordre decroissant annonce par le gel P-A est bien celui de ses propres valeurs, recalcule :
      2.85 > 1.35 > sqrt2 > 2.40 > 1.618 > 1.25 > 2.00 > 1.50 > 1.80 > 1.60. Le gel est coherent
      avec lui-meme -- il ne pouvait pas etre ajuste apres coup sans se contredire.
  LES FRACTIONS DE nn.4
   5. P-A-1 : sum d^2 = 52, rho = 113/165. Conforme.
   6. P-D-1 : sum d^2 = 38, rho = 127/165. Conforme.
   7. Consigne r_gauss : sum d^2 = 64, rho = 101/165. Conforme.
   8. Valeur critique par enumeration COMPLETE des 10! = 3 628 800 permutations :
      P(sum d^2 <= 72) = 5459/113400 = 0.0481 <= 1/20, d'ou rho_c = 31/55 = 0.563636.
      Le 0.564 des gels en est bien l'arrondi, et il est marginalement PLUS exigeant : les portes
      n'ont pas ete relachees par le recalcul.
   9. Rapport V/B = 0.3585386698, strictement dans ]0.224, 0.569[ et dans ]0.225, 0.634[.
  10. Aucun ex aequo dans T_shell, f_esc, r_gen, r_gauss : Spearman s'applique sans correction.
  LES COMPTES DE nn.3
  11. 10 points joues ; 10 temoins joues, 0 explosent ; 891 etats dans la coquille aux dix points ;
      les deux voies de T_shell a ecart 0.0 ; moteur c8ed357b120352c4, fichier non modifie.
      Design re-derive des seules formules du gel : ecart relatif maximal 0.00e+00 sur 70 grandeurs
      (tolerance 1e-12 declaree avant).
  L'AFFIRMATION QUI PORTE TOUT L'ACTE (nn.5)
  12. "Hors echantillon" : les SIX repliques A2 de machine 1 (lot brancheA v1) ne portent que
      T_shell_0.7 et T_shell_0.9. 0.8 n'y figure nulle part. La quantite JUGEE n'avait donc pas ete
      calculee par machine 1 -- l'acte est fonde sur ce point, et c'est le point qui fait la valeur
      de la prediction.
  13. Le bruit de Poisson annonce : les deux fichiers TWA a f0.8 portent M400 dans leur nom, soit
      400 tirages. L'acte a raison de dire que la prediction tenue est un RANG, pas un nombre.

  EMPREINTES : 30 citees, 28 verifiees, 2 non detenues ; 28 + 2 = 30 = citees.

=======================================================================
3. UN POINT QUE JE PEUX ENFIN CONTRESIGNER
=======================================================================
  Ma contresignature du 08/09 (lot 5333717bb9a11657, sec. 5) refusait un point : je constatais que
  les VERDICTS de machine 1 coincidaient avec les miens, sans pouvoir verifier que les LECTURES
  coincidaient, faute de la piece. Le lot lectureR3 (canon 07b3ed2942861461) a transite depuis.
  Verifie sur la piece meme (lecture_R3_PA_machine1_v1.json, 986fdd49f7b6716a) :
    les dix T_shell que machine 1 a lus sont les miens, IDENTIQUES AU BIT (10 sur 10) : elle a lu mon
      lot, elle n'a pas recalcule un run a elle ;
    rho P-A-1 113/165, rho P-D-1 127/165, rho_c 31/55, p 7859/453600 et 22783/3628800, V/B
      0.3585386698036813 -- toutes identiques aux miennes, la derniere AU BIT ;
    les d^2 (52, 38, 72) sont des ENTIERS : ils se comparent sans qu'aucun flottant n'intervienne.
  LA RESERVE EST LEVEE. Les deux lectures coincident, et non seulement les verdicts.

=======================================================================
4. CE QUE CETTE CERTIFICATION NE COUVRE PAS (nomme, pas contourne)
=======================================================================
  R-1  DEUX EMPREINTES CITEES NE SONT PAS DETENUES par machine 2 et ne sont donc pas certifiees :
         9061e960af56e2d4  lot REPRISE v2 (nn.2)
         68fc215b6201df90  SUIVI (c) (nn.2)
       Elles sont citees pour la trace, ne portent aucun verdict, et rien dans nn.4 n'en depend.
       A transmettre pour completer la trace.
  R-2  L'ETAT DU REGISTRE. L'acte declare HEAD 0ff330b (delta 86), verifie sur clone frais le 07/09,
       aucun depot depuis. Machine 2 n'a pas acces au depot public : elle ne verifie NI le HEAD, NI
       l'absence de depot intermediaire, NI que "nn" sera libre au moment du depot. La verification
       du registre au moment de l'acte appartient a qui depose.
  R-3  UNE AFFIRMATION HISTORIQUE, hors de tout perimetre de mesure : "premiere prediction
       quantitative tenue au volet quantique de la campagne depuis C2 (M9)" (nn.5). Elle porte sur
       l'ensemble de la campagne, pas sur les pieces de R3. Machine 2 ne la contredit pas et ne la
       certifie pas : elle demande qu'elle soit portee comme une lecture de machine 1, ou etayee par
       une enumeration des manches.
  R-4  Les residus que l'acte declare lui-meme ouverts restent ouverts et ne sont pas couverts :
       R-A-1 (valeurs de T_shell non convergees), R-A-3 (facteur T_shell / f_esc), R-D-1 (grille de
       phases a 30 degres, trop grossiere -- prealable a toute lecture du renversement r_gen /
       r_gauss), R-D-2..4.
  R-5  La portee du test, que l'acte enonce correctement et que je confirme : 0.8 s* est hors
       echantillon EN DONNEES mais DANS L'INTERVALLE des profondeurs deja lues (0.7 et 0.9). Aucune
       extrapolation (0.6 ou 0.95 s*) n'a ete jouee. Ce n'est pas une reserve contre l'acte : c'est
       la clause qu'il faut garder attachee au resultat quand il circulera.

=======================================================================
5. AVIS
=======================================================================
  Les 13 controles passent. Les fractions, les comptes, les gels et le caractere hors echantillon
  sont re-derives et conformes. Aucun ecart n'a ete trouve entre l'acte et les pieces.
  MACHINE 2 CERTIFIE l'acte delta nn v1 (cce710187ad53e04) POUR LE DEPOT, sous les cinq reserves de
  la section 4, dont aucune ne porte sur un verdict.
  Ce que la certification n'est pas : elle ne prend aucun numero, ne decide pas la promotion 49.5
  (O4, decision operateur), et ne vaut pas pour le depot P-4 (R1), qui est un autre acte.
  Si machine 1 amende l'acte avant depot, cette certification devient caduque : elle porte sur
  l'empreinte cce710187ad53e04 et sur elle seule.
-- FIN DE LA CERTIFICATION --
