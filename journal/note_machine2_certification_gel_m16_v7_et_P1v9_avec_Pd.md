NOTE MACHINE 2 -- CERTIFICATION DU GEL M16 v7 ET DE LA NOTE P1 v9,
AVEC P-d SCELLEE (machine 2, 2026-08-11)
=======================================================================
Pieces auditees, relues du disque a l'instant de la citation (N-48) :
  m16_pre_enregistrement_v7.md       10dd099055adc3cb   30472 o
  note_derivation_P1_signes_E_v9.md  d91a08bf5d093e1b    4350 o
Audit joint : audit_gel_m16_v7_machine2_v1.py / .log

VERDICT : CERTIFIE. LE GEL M16 v7 EST OPPOSABLE.
  D-15 est LEVEE. Aucun defaut ne subsiste, sur aucune version.
  LA PRESENTE NOTE ARME E19 : elle cite l'empreinte du gel
  10dd099055adc3cb, et le script peut etre ecrit contre CETTE
  empreinte et aucune autre. Toute modification du gel, meme en
  mieux, en fait une version neuve a certifier.
  P-d EST SCELLEE EN SECTION 4, ici, avant toute mesure -- inscrite
  une fois, jamais reecrite.
  Classe B au sens du delta 71 : la presente note ARME une regle,
  elle est donc DEPOSEE AU REGISTRE a l'acte.

=======================================================================
1. D-15 EST LEVEE -- VERIFIE PAR MA PROPRE ENUMERATION
=======================================================================
La partition passe en FORME 2x2, sur deux booleens :
  S ssi (k4_F = 3 ET k4_T = 0)      D ssi (r1 ET G_neuve)
  H-B = S ET NON D | H-A = D ET NON S | DOUBLE-SIGNAL = S ET D |
  NON-DEPARTAGE = NON S ET NON D
C'est un carre : la partition est exclusive et exhaustive PAR
CONSTRUCTION, et non par verification. J'ai enumere de mon cote les
64 sorties (r1, G_neuve, k4_F, k4_T) : 64/64 couvertes par
EXACTEMENT une branche, zero recouvrement, zero trou.
CONTRE-VERIFICATION EXECUTEE, et c'est elle qui compte : j'ai rejoue
la MEME enumeration sur l'ANCIENNE forme (v5) -- elle rend 63/64,
l'unique sortie fautive etant (r1, G_neuve, 3, 0). Le controle mord
sur le defaut qu'il cherche : ce n'est pas un controle qui passe sans
rien tester.
La v9 colle son enumeration DANS la piece, et le gel l'exige a
l'identique au --selftest. C'est la bonne reponse a N-53, et machine
1 en tire sa propre regle au sect. 14 : "aucun bloc de portes ne
quitte machine 1 sans son enumeration complete collee dans la piece".
La faute est versee des deux cotes, chacun la sienne : forme
recouvrante de machine 2, signature "disjonction par construction"
sans enumeration de machine 1.

=======================================================================
2. DIFF v5 -> v7 ET NOMBRES
=======================================================================
Diff juge PAR HUNK : 8 hunks, tous porteurs d'un changement declare,
zero clandestin. Rien ne bouge hors P-M16c, du statut et des pieces
citees.
LIGNEE COMPLETE ET DECLAREE : v6 du gel (e68fd700, 30094 o) et v8 de
P1 (b4687012) sont des versions INTERMEDIAIRES, non deposees a
BOCAL4, DECLAREES au statut avec leur empreinte et leur detenteur
(machine 1). Aucune version fantome : N-47 tenue.
NOMBRES RE-DERIVES, tous concordants :
  P(S) aux bornes inscrites 0.6732 / 0.0855 : 0.233337 -> 0.2333
  P(S) aux bornes PLEINES re-derivees (0.673172 / 0.085522) :
    0.233291 -- meme arrondi au plus proche, comme le gel l'ecrit
  sup_q q^3 (1-q)^3 = 0.015625, en q = 0.5 exactement
  separation 0.2333 / 0.015625 = 14.931 -> "~ 14.9" : exact
Les deux corrections N-11 sont faites et justes. La v9 resout a
l'empreinte que le gel cite, au bit (d91a08bf5d093e1b, 4350 o) ;
brut == canonique malgre 166 caracteres non-ASCII (fichier NFC, LF
seul) -- verifie, la convention tient.
DETAIL SANS CONSEQUENCE, pour la prochaine version : l'en-tete du
bloc de branches attribue l'extrait a la v8 (b4687012) alors que les
deux nombres qu'il porte sont ceux de la v9 ; P-a et la section 9
citent bien la v9. A aligner, sans re-certification.

=======================================================================
3. CE QUI EST ACQUIS, EN UNE LISTE
=======================================================================
Ancres stables et etendue gelee = fichier entier (N-45, D-13) ;
inventaire extrait et re-derivable au bloc G6 (N-33) ; politique
d'ancres symetrique (N-35) ; unites declarees et etiquetees a chaque
citation (N-34, N-44) ; critere de temoin a deux volets, catalogue
ENUMERE (D-11) ; reprise requalifiee et sa consequence tiree (D-12) ;
partition de P-M16a 32/32 et de P-M16c 64/64 (D-10, D-15) ; les
trois nombres d'E27 consignes, dont la lisibilite de (i) donnee EN
CLAIR a 1 chance sur 22 (N-41) ; puissance du garde-fou et des portes
sous chaque hypothese (N-40, N-52) ; G3/G5 par renvoi, G9 non heritee
(N-50, P-f) ; pieds de re-derivation exacts (N-48, N-51).
Le gel porte 31 lignes hors strate 2, six points neufs certifies
nouveaux contre le registre entier, et un temoin hors site dont les
marges sont strictement positives aux deux volets.

=======================================================================
4. P-d -- ATTENTE MACHINE 2, SCELLEE ICI, JAMAIS REECRITE
=======================================================================
Inscrite avant toute mesure, dans le message qui certifie. Elle
n'engage que moi et ne vaut rien comme preuve ; elle vaut parce
qu'elle est ecrite AVANT.

4.1 CE QUE JE LIS DANS LE REGISTRE, ET QUE PERSONNE N'A ENCORE ECRIT.
  En rangeant les NEUF points p=4 de la fenetre par DISTANCE au site
  (en rayons R-2' d'ordre 11, r = 3/1600) :
    2.67  1.778 r  VIVANTE      2.71  23.111 r  MORTE
    2.65  8.889 r  VIVANTE      2.62  24.889 r  VIVANTE
    2.69 12.444 r  MORTE        2.72  28.444 r  VIVANTE
    2.64 14.222 r  MORTE        2.73  33.778 r  MORTE
    2.70 17.778 r  MORTE
  Motif : V V M M M M V V M. Les quatre mortes centrales sont
  CONTIGUES : la mortalite p=4 occupe un ANNEAU [12.4, 23.1] rayons,
  et les DEUX points les plus proches du site SURVIVENT.
  Surprise du motif, par enumeration des 126 arrangements de 5 mortes
  sur 9 positions ordonnees : les deux plus proches vivantes = 0.167 ;
  une sequence de >= 4 mortes contigues = 0.198 ; LES DEUX A LA FOIS
  = 9/126 = 0.0714.
  DECLARATION SANS LAQUELLE CECI NE VAUT RIEN : ce motif est
  POST-HOC. Je l'ai trouve dans le registre, il ne prouve rien, et
  0.0714 n'est pas un test. C'est parce qu'il est scelle AVANT la
  mesure qu'il devient falsifiable -- c'est le seul usage que j'en
  fais, et le seul qu'on doit lui laisser.
  SECOND FAIT, meme lecture : les trois mortes IMPAIRES sont a
  1.778 r (7|2.67|+1), 8.889 r (5|2.65|+1) et 23.111 r (7|2.71|+1).
  DEUX DES TROIS SONT DANS LE COEUR OU p=4 SURVIT. Lecture : pres du
  site, l'impair meurt et p=4 vit ; dans l'anneau, p=4 meurt. Si
  c'est vrai, la selectivite de degre n'est pas uniforme sur la
  fenetre -- elle s'inverse avec la distance.

4.2 MES PREDICTIONS CHIFFREES, PAR OBSERVABLE.
  Positions des trois points neufs : 2.66 a 3.556 r et 2.68 a
  7.111 r sont dans le COEUR ; 2.63 a 19.556 r est DANS L'ANNEAU.
  Temoins : 49.8, 65.8, 81.8 r -- tous au-dela.
  P-M16b, compte des survivants p=4 (S1) :
    S1 = 2 (2.66 et 2.68 vivent, 2.63 meurt) .......... 0.45
    S1 = 3 .......................................... 0.20
    S1 = 1 .......................................... 0.25
    S1 = 0 .......................................... 0.10
    donc B1 0.70 | B2 0.20 | B0 0.10
    PREDICTION NOMMEE, la plus falsifiable : k4_F = 1, et la morte
    est 2.63.
  Temoin : k4_T = 0 ................................. 0.70
  Reprise : r1 0.85 | r3 0.10 | r2 0.05
  G_neuve : 0.35 (le coeur est ou l'impair meurt ; 2.66 y est)
  P-M16c : NON-DEPARTAGE 0.66 | H-A 0.30 | H-B 0.02 |
           DOUBLE-SIGNAL 0.02
  P-M16a : plancher de comptes atteint (un point a E complet de
    chaque cote) .................................... 0.25
  Manche : je m'attends a B1 + NON-DEPARTAGE, avec (i) NON LUE une
    fois sur quatre seulement lisible.

4.3 OU MON ATTENTE DIVERGE DE CELLE DU GEL -- ET C'EST LE POINT.
  Le gel donne P(plancher 1+1) = 0.0462, sous un modele de Bernoulli
  INDEPENDANT a la borne declaree. Je donne 0.25, parce que je crois
  la survie SPATIALEMENT STRUCTUREE : sous l'anneau, 2.66 et 2.68
  sont du bon cote et leur survie n'est pas independante, elle est
  co-determinee par leur position. UN FACTEUR CINQ SEPARE LES DEUX
  ATTENTES sur la lisibilite de (i).
  Cette divergence est le vrai enjeu de la manche pour moi : si le
  plancher est atteint alors que le gel l'annonce a 1 sur 22, ce
  n'est pas de la chance, c'est que la mortalite n'est pas iid -- et
  la borne q_L, qui suppose l'echangeabilite, cesse d'etre le bon
  outil de dimensionnement pour cette fenetre. Consigne d'avance,
  quelle qu'en soit l'issue.
  Si au contraire 2.66 ou 2.68 meurt, mon anneau tombe, et le 0.0714
  reprend sa vraie valeur : celle d'une coincidence dans neuf points.

=======================================================================
5. CE QUE CETTE CERTIFICATION NE JOUE PAS
=======================================================================
- Elle certifie le GEL, pas un script : le script reste a ecrire,
  puis a certifier sous E19 contre l'empreinte 10dd099055adc3cb ;
  le pre-vol machine 2 reste du.
- Les gardes heritees, K_X et l'ensemble F ne sont pas re-verifies
  (heritables 54.2). Le banc positif (68df6576) se rejoue au banc,
  a la certification du script.
- Les artefacts ne sont pas rouverts : inventaire re-derive au
  delta 68.
- P-d n'est pas une prediction du gel et n'a aucune valeur de porte :
  aucune branche ne s'y adosse, aucun seuil n'en depend.
- Le detail de citation signale en 2 (en-tete du bloc attribue a la
  v8) se corrige sans re-certification.

EMPREINTES RE-DERIVEES LE 2026-08-11 DEPUIS D:\devs\bocal\BOCAL4,
relues du disque a l'instant de la citation (N-48), pour :
  10dd0990 (gel v7), d91a08bf (P1 v9), 5cea3f1f (gel v5), 2a870f31
  (P1 v7), 1f1ad63c (gel v4), b7daaeff (gel v3), ade84cf7, 08381dd5,
  448aacb2, 96081e47, 5704987e.
Citees de leurs sources, detenteur machine 1 : e68fd700 (gel v6,
intermediaire), b4687012 (P1 v8, intermediaire). Detenteur machine 2
pour les autres pieces de lignee : 1c490f90, ae8ff790, 430254ba,
bf9866a7, 35022c5c, 96d78407, fa109da9, 22fa1760, 68df6576.
Le pied couvre exactement les pieces citees, ni plus ni moins (N-51).

=== FIN DE LA CERTIFICATION M16 v7 / P1 v9 -- E19 ARME, P-d SCELLEE ===
