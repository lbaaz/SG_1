NOTE MACHINE 2 -- CONTROLE DU DOSSIER TRILEMME v2 ET DU DELTA 65
(machine 2, 2026-08-10)
=======================================================================
Objet : controle des deux pieces recues ce jour --
  dossier_trilemme_site_v2.md        347f25daf1046c43  16690 o
  journal_delta_65_fusion_d_v3.md    e5931c94518916ce   4380 o
Aucune mesure rejouee, aucun gel redige, aucun numero de delta ni
d'erratum attribue (E18). Fichier ASCII pur, LF seul : brut =
canonique (N-10). Audit executable joint :
  audit_controle_v2_delta65_machine2_v1.py / .log

VERDICT EN UNE LIGNE
  LA SCIENCE PASSE, LE REGISTRE NE PASSE PLUS. Le dossier v2 est
  CERTIFIE sur son arithmetique (22/22 re-derivees, zero ecart) et
  sur l'execution de D-1 a D-5 ; il porte deux defauts opposables au
  gel, non bloquants pour la branche (D-6, D-7). Mais le REGISTRE a
  FOURCHE : le numero de delta 65 a ete pris DEUX FOIS le meme jour,
  par deux pieces distinctes, dans deux registres qui ne se voient
  pas. Consequence operatoire immediate : E18 ("le numero se prend a
  l'acte") n'est plus EXECUTABLE -- il n'existe pas de suite unique
  ou le prendre. Le gel de branche peut s'ecrire ; le delta de
  decision ne peut pas etre consigne avant que l'autorite de
  numerotation soit tranchee (C-1, N-29).

=======================================================================
1. CE QUI EST CERTIFIE
=======================================================================
1.1 CUSTODY DES SOURCES. Sept pieces citees par le dossier v2
resolvent localement, empreintes re-derivees, brut == canonique :
  dossier v1        f8e1f257ea9541cb  13347 o  INCHANGE (PB-1 tenue)
  note d'arbitrage  1c490f90fafcf8ff  16106 o
  delta 65 (m1)     e5931c94518916ce   4380 o  RESERVE R-1 LEVEE
  delta 64          f4552c5f6fe40446   4357 o
  note P1 v5        5704987e7d6ff7a6  14007 o
  note d (envoi)    74950a6b6912699c  55485 o  demande 65.6 SATISFAITE
  dossier v2        347f25daf1046c43  16690 o  (empreinte a citer)
Une seule mismatch, la mienne : voir C-4.

1.2 R-1 EST LEVEE. Le delta 65 machine 1 resout a BOCAL4 a
l'empreinte annoncee, au bit. La copie re-deposee est conforme.

1.3 L'ARITHMETIQUE DE LA v2, RE-DERIVEE INDEPENDAMMENT -- 22/22.
Estimateur re-implemente depuis sa DEFINITION (P(Bin(n,q) <= k) =
0.20, bisection 200 pas), jamais depuis les valeurs du dossier :
  calibration    1/12 -> ecart 2.8e-17 au registre (sous la
                 resolution du double) ; 1/34 -> 0.0855 ; 3/80 -> 0.0679
  section 3.2    p=4 fenetre 4/7 -> 0.7717 ; impair 2/24 -> 0.1700
  section 3.3    p=4 5/9 -> 0.7325 ; impair 3/28 -> 0.1882
  D-1            0.9725 / 0.9074 / 0.9686 / 0.8956, amplitude 0.0769
                 -- les quatre lectures et l'amplitude confirmees
  rendements     8/8 aux deux colonnes ; P(strate 1) = 0.5405
  geometrie      EN FRACTION EXACTE : 133/45000, 2/225, 14/5625 ;
                 ratios 400/133 = 3.0075 et 16/19 = 0.8421
Aucun ecart. La contre-verification 4/4 et 8/8 que machine 1
s'attribue est reelle.

1.4 D-1 A D-5 SONT EXECUTES.
  D-1  le 0.9725 est RETIRE du dimensionnement (3.2 le dit) ; il ne
       subsiste que dans le bloc qui le retire -- lecture correcte,
       sous reserve D-7 ci-dessous.
  D-2  N = 9 retire, dessin en DEUX STRATES, P(strate 1) = 0.5405
       consignee d'avance avec la clause "zero n'est PAS une
       refutation". Conforme au correctif, en forme.
  D-3  clause d'ancres inscrite en 4.B2, formulation conforme.
  D-4  composition du "8" ECRITE EN EXTENSION en section 2 et
       confirmee des deux cotes. Ma deduction est validee ; ce n'est
       plus une deduction.
  D-5  coherence 2.67 declaree en 3.3.
  Les trois valeurs interieures jamais essayees au centieme sont
  bien 2.63, 2.66, 2.68 et seulement elles : recompte a partir de
  l'interieur de [2.62, 2.73] prive de {2.64, 2.65, 2.67, 2.69,
  2.70, 2.71, 2.72}. La strate 1 est exacte.

=======================================================================
2. LES DEUX DEFAUTS DE LA v2 (opposables au gel, non bloquants)
=======================================================================
D-6 -- L'INVENTAIRE COMPLEMENTAIRE DE 3.3 N'EST PAS ECRIT EN
EXTENSION, ET IL PORTE UNE COLONNE DE DIMENSIONNEMENT.
  La phrase de 3.3 nomme TROIS apports (2.70 p=4 mort ; 2.67 p=4
  vivant ; 2.72 lignes vivantes) puis conclut "p=4 : 5/9". Or
  7 + 1 + 1 = 9 : le compte n'atteint 9 que si la ligne p=4 de 2.72
  n'est PAS comptee -- alors que la meme phrase la nomme vivante.
  Les deux lectures ne sont pas equivalentes :
      2.72 hors compte     k=5 n= 9  ->  q_L = 0.7325
      2.72 comptee vivante k=5 n=10  ->  q_L = 0.6732
      amplitude 0.0593
  C'est la MEME maladie que D-1 (0.0769), a la MEME place (un compte
  dont la composition n'est pas ecrite), sur une quantite qui figure
  en colonne de la table des rendements de 4.B2. Le cote impair est
  dans le meme etat : 24 -> 28 lignes, +4, dont UNE SEULE attribuee
  (7|2.67|+1) ; les trois autres ne sont nommees nulle part
  (0.1882 / 0.1820 / 0.1762 selon le compte).
  Ce n'est pas une faute de calcul : 5/9 et 3/28 rendent bien 0.7325
  et 0.1882, je les ai re-derives. C'est un compte AFFIRME, pas
  COMPTE -- la regle que la campagne a deja payee, et le correctif
  D-4 que la v2 vient d'appliquer au "8" sans l'appliquer au
  complement.
  CORRECTIF EN FORME EXECUTABLE. La section 3.3 du gel s'ecrit en
  extension, une entree par LIGNE comptee :
      {point, degre, verdict, manche, artefact}
  n de chaque degre = CARDINAL de cette liste, imprime, verifie par
      assert len(lignes_p4) == n_p4 and sum(v == 'mort') == k_p4
  Si la ligne p=4 de 2.72 est mesuree vivante, elle compte (n = 10,
  q_L = 0.6732). Si elle est ECARTEE comme ancre de custody,
  l'exclusion est declaree avec son motif ET 2.72 sort de la phrase
  d'apport. Une des deux, ecrite, pas les deux.

D-7 -- LE PIEGE D'EXTRACTION DE N-20 : LE GEL IMPORTERAIT CE QUE
N-20 INTERDIT.
  La v2 declare (bloc ARBITRAGE RENDU) que le gel EXTRAIT par
  structure les textes verbatim de la note 1c490f90, blocs D-1, D-2,
  D-3 -- et la section 6 renvoie N-20 au "texte verbatim : note,
  D-1". Or le bloc D-1 de ma note CONTIENT les quatre valeurs
  0.9725 / 0.9074 / 0.9686 / 0.8956. Extraction verbatim ==> le gel
  de branche porte en clair quatre q_L de NIVEAU-POINT, dont un
  compare aux trois autres, c'est-a-dire exactement ce que la
  premiere ligne de N-20 interdit ("aucun q_L de niveau-point
  derive, CITE ni COMPARE").
  Le risque n'est pas theorique : la journee du 10/08 a paye QUATRE
  fois la faute "chiffre transporte sans re-derivation" (65.2). Un
  0.9725 pose dans le texte d'un gel est un chiffre disponible.
  CORRECTIF EN FORME EXECUTABLE. Le gel extrait de D-1 la CLAUSE,
  pas ses chiffres :
    - texte porte au gel : "aucun q_L de niveau-point n'est derive,
      cite ni compare ; le dimensionnement se fait par degre
      exclusivement (regle 16)" ;
    - justification : renvoi par empreinte a note 1c490f90, bloc
      D-1, et dossier v2 347f25da, section 3.2 -- les quatre valeurs
      vivent LA, et seulement la ;
    - controle mecanique au --selftest, sur le bloc de portes :
        for lit in ("0.9725","0.9074","0.9686","0.8956"):
            assert lit not in bloc_de_portes
      avec son TEST NEGATIF (le selftest exhibe qu'il mord sur une
      chaine temoin contenant "0.9725").
  Meme forme a appliquer a D-2 et D-3, qui sont extractibles sans
  reserve : eux ne portent pas de chiffre interdit.

Note de portee : ces deux defauts ne changent NI la branche adoptee,
NI la strate 1 (2.63, 2.66, 2.68), NI P(strate 1) = 0.5405, qui
repose sur la colonne fenetre 0.7717 -- laquelle est, elle, ecrite
en extension et certifiee. B2 vehicule / B3 lecture tient.

=======================================================================
3. CUSTODY -- CE QUI NE PASSE PAS
=======================================================================
C-1 -- COLLISION DE NUMERO DE DELTA 65. DEUX PIECES DISTINCTES,
DEUX REGISTRES, LE MEME JOUR, LE MEME NUMERO.
  machine 1  journal_delta_65_fusion_d_v3.md
             e5931c94518916ce  4380 o  "machine 1, 2026-08-10"
             "S'insere apres journal_delta_64_revue_note_c.md"
  depot      journal/journal_delta_65_pseudonymisation_baaz.md
             5ad0561e14ec563e  3003 o  "machine 2, 2026-08-10"
             "S'insere apres journal_delta_64_revue_note_c.md"
  Releve : gh api repos/lbaaz/SG_1/contents/journal, ce jour ; copie
  du second deposee a BOCAL4 sous
  depot_journal_delta_65_pseudonymisation_baaz_COPIE.md (5ad0561e),
  nommee COPIE parce qu'elle n'est pas une piece BOCAL4 d'origine.
  Les deux revendiquent la meme position dans la chaine. Ce n'est
  pas une collision de nom (famille E13, deja payee deux fois) :
  c'est une collision sur l'EPINE DORSALE du registre, la suite des
  numeros par laquelle toutes les pieces se citent entre elles.
  CE QU'ELLE CASSE, CONCRETEMENT : "Borne : 65" (65.7) et le
  mecanisme E18 "le numero se prend a l'acte". Le delta de decision
  du trilemme doit prendre son numero a l'acte -- et il n'y a
  aujourd'hui aucune suite unique ou le prendre : 66 selon machine 1,
  66 aussi selon le depot, pour deux chaines differentes.

C-2 -- LES DELTAS 61, 62, 63 N'EXISTENT DANS AUCUN DES DEUX
REGISTRES. 65.5 les declare "re-derives ce jour == registre
(18ad843d, 183ab8a1, 6b647dfa) et RE-PRESENTES pour integration".
Recherche exhaustive : absents de d:\devs\bocal (arborescence
entiere) ; absents du journal/ du depot public, dont les deltas
releves sont 50..60, 64, 65. Ils ne resolvent que dans la copie
projet de machine 1. Un trou de trois numeros dans la seule suite
qui ordonne la campagne.

C-3 -- LA SCISSION DE REGISTRE EST AVEREE. C'est la constatation que
la v2 me confie explicitement (section 1, reserve R-1 : "a declarer
si averee"). JE LA DECLARE, et C-1 + C-2 en sont la preuve, pas
l'indice : il existe deux registres actifs -- BOCAL4 (echange de
fichiers machine 1 <-> machine 2) et journal/ au depot (ecrit par la
session de re-coupe) -- qui numerotent independamment et ne se
lisent pas. Le delta 65 n'a pas ete "oublie" : il a ete consigne
d'un cote pendant qu'un autre 65 etait consigne de l'autre. La
re-depose de ce jour repare la PIECE, pas la CAUSE.

C-4 -- MA FAUTE, VERSEE : revue_pre_envoi_2026-08-10b_machine2_v1.md
a ete EDITEE EN PLACE apres avoir ete citee par empreinte.
  64.1  9234984c  14960 o  (v1, consignee machine 1)
  65.1  310e2171  18341 o  (v1.1, addendum H, consignee machine 1)
  ce jour, a BOCAL4 : 342f7cc97d04a7b4  20461 o  (v1.2, addendum I,
  re-coupe pseudonyme + note e)
  Trois etats sous UN nom ; les deux premiers ne resolvent plus
  localement. C'est la regle "un document deja cite par empreinte ne
  s'edite pas, la correction vit dans la version suivante" -- que je
  connais et que j'ai enfreinte, et c'est la troisieme instance E13
  du jour apres les deux versions c. Machine 1 detient 310e2171 ;
  9234984c est perdu localement. Correctif : N-31.

C-5 -- LE DELTA 65 MACHINE 1 EST DESYNCHRONISE DE L'ETAT REEL. Ce
n'est pas une faute de machine 1 (elle ne pouvait pas savoir : c'est
le symptome de C-3), mais c'est un fait de registre a declarer, car
la piece sera relue :
  65.4 "Tags immuables : v1 88ed9158... ; v2 9db2afa4... ; v3
       2f898234..." -- l'historique public a ete REECRIT et
       force-push le meme soir ; le tag v1-held a ete re-emis
       (0ace0d19) et le manifeste 88ed9158 N'EST PLUS SERVI par le
       depot. Le mot "immuables" est faux au moment ou on le lit.
  65.7 "UNE SEULE CHOSE BLOQUE ENCORE L'ENVOI : A3 (depot prive)
       ... Puis : ENVOI" -- le depot est PUBLIC et LE MAIL EST
       PARTI le 2026-08-10, avec la note d en piece jointe, AVANT la
       re-coupe. A3 est sans objet, l'envoi est fait.
  65.6 la demande de depot du .md de la version d est SATISFAITE :
       note_outreach_EN_unified_2026-08-10d.md resout a BOCAL4,
       74950a6b6912699c, 55485 o, verifiee au bit. RESERVE : la d ne
       doit plus JAMAIS etre re-circulee -- la version de
       circulation future est la note e (copie signee f03ca623). La
       d reste la piece d'envoi HISTORIQUE, celle que Held a en
       main.

=======================================================================
4. PRESCRIPTIONS (suite de N-20 a N-26 ; N-27 a N-31)
=======================================================================
N-27  (D-6) Section 3.3 du gel ecrite EN EXTENSION, une entree par
      ligne comptee {point, degre, verdict, manche, artefact} ; n =
      cardinal de la liste, verifie par assert ; statut de la ligne
      p=4 de 2.72 tranche et declare (comptee -> n=10, q_L=0.6732 ;
      ecartee -> motif ecrit et 2.72 hors de la phrase d'apport).
      Tant que ce n'est pas fait, la colonne "complement" ne sert a
      AUCUN dimensionnement : la strate 1 se dimensionne sur la
      seule colonne fenetre (0.7717).
N-28  (D-7) Le gel extrait de D-1 la CLAUSE, pas ses chiffres ;
      renvoi par empreinte pour la justification ; --selftest
      asserte l'absence des quatre litteraux dans le bloc de portes,
      avec son test negatif. D-2 et D-3 s'extraient verbatim sans
      reserve.
N-29  (C-1, BLOQUANT POUR TOUTE CONSIGNATION) Une seule autorite de
      numerotation, declaree avant le prochain acte. Recommandation
      machine 2 : le journal/ du DEPOT est le registre ordonnant --
      il est public, ordonne, immuable par construction, et il porte
      deja le 65 dans un historique reecrit qu'on ne rouvre pas une
      seconde fois. En consequence : la piece machine 1 e5931c94
      reste INTACTE a BOCAL4 (PB-1) et est RE-EMISE en v4 sous le
      numero 66, contenu inchange hors numero et borne ; le delta de
      decision du trilemme prend 67 A L'ACTE, au depot. Toute autre
      resolution convient si elle est UNIQUE et ecrite -- mais
      aucune consignation ne part avant qu'elle le soit.
N-30  (C-2) Les deltas 61, 62, 63 sont deposes (BOCAL4 + journal/)
      ou leur trou est CONSTATE par ecrit avec les trois empreintes
      annoncees (18ad843d, 183ab8a1, 6b647dfa) et le motif. Une
      constatation apres coup n'est pas une reservation de numero
      (E18 tient).
N-31  (C-4) Aucun fichier machine 2 deja cite par empreinte n'est
      re-ouvert en ecriture. La revue est renommee en
      revue_pre_envoi_2026-08-10b_machine2_v1_2.md (contenu
      342f7cc9 inchange), 310e2171 est re-depose par machine 1 sous
      son nom v1_1, et le nom nu "v1" est retire de l'usage.
N-32  Rappel de portee : N-20 a N-26 restent opposables tels quels ;
      N-23 (attribution par degre de 2.71 / 2.73 depuis le JSON
      96d78407) et N-25 (temoin hors site) sont les deux que le gel
      ne peut pas sous-traiter.

=======================================================================
5. CE QUE CE CONTROLE NE JOUE PAS
=======================================================================
- AUCUN artefact de mesure ouvert : 96d78407, 22fa1760, fa109da9,
  ad275870, 7cf3624b, ed0e27b1, 70fe5611, 68df6576. Je certifie que
  l'estimateur applique aux couples (k, n) rend les valeurs
  annoncees ; je ne certifie PAS les couples eux-memes -- c'est
  precisement l'objet de D-6 et de N-27.
- Les rangs (6,2) / (3,1) / (3,1) de la section 2 sont cites du gel
  v4, non re-derives ici.
- L'etat du depot est un RELEVE par API a un instant, pas une
  contre-epreuve par clone frais. La correspondance sha16 ancien ->
  nouveau interne au delta 65 du depot n'est pas verifiee ; le clone
  local d:\devs\bocal_coupe est desynchronise (force-push) et n'a
  pas ete utilise.
- La note e (f03ca623), le PDF d et la chaine Held ne sont pas
  re-verifies ici : seule la demande 65.6 l'est.
- Aucun numero de delta ni d'erratum n'est attribue. Les q_L sont
  des bornes de PLANIFICATION, pas des consignations de garde
  (discipline E27).

PIECES CITEES (16 hex, brut == canonique sauf mention)
  dossier v2 347f25da (16690 o, empreinte de la piece controlee) ;
  dossier v1 f8e1f257 ; note d'arbitrage 1c490f90 ; delta 65 m1
  e5931c94 ; delta 65 depot 5ad0561e (copie) ; delta 64 f4552c5f ;
  note P1 v5 5704987e ; note d 74950a6b ; revue v1.2 342f7cc9
  (contre 310e2171 et 9234984c, non resolus localement) ; gel v4
  35022c5c ; audit joint .py / .log.

=== FIN DE LA NOTE DE CONTROLE -- machine 2, v1 ===
