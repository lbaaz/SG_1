NOTE MACHINE 2 -- LA MANCHE M16 EST JOUEE : RESULTATS, LECTURE, ET
P-d CONFRONTEE (machine 2, 2026-08-12)
=======================================================================
Artefact : out/m16_results_run.json  1118a4692e07efe4  55953 o
  35 lignes, bloc G6 COMPLET sur chacune, 19 rebinds journalises,
  gel cite 75bc4020b5bd560f.
Script execute : m16_crible_v6_M2.py, COPIE DE TRAVAIL MACHINE 2
  (voir section 6 : trois blocs de diff, tous dans l'ECRITURE).

=======================================================================
1. LES VERDICTS
=======================================================================
  P-M16b = B2   SURVIE TOTALE DES NEUVES (k4_F = 0)
  P-M16c = H-A  le coeur impair resonant est DECLARE
  P-M16a = A4   STRUCTURE-RESOLUE-CENTRAGE-NON-DISCRIMINE
  reprise = r1  la grossiere de M12 se REPRODUIT
  mode NORMAL (k4_T = 1, le garde-fou exige 2)
  S = faux ; D = vrai ; G_neuve = vrai
  q4_fen re-derive = 0.5394 (a, fenetre seule) ; strate 2 JOUABLE
  comptes : 35 lancees = 31 + 4 (strate 2), G1' 2, N-3 6 asserts,
    G2 sautees 0 -- comptes + sautes == attendu

=======================================================================
2. LES CINQ MORTES SUR TRENTE-CINQ, ET LEUR GEOMETRIE
=======================================================================
Toutes les lignes, rangees par DISTANCE AU SITE (rayons R-2' d'ordre
11, r = 3/1600) :
   2.67    1.778 r   p=4 vivante   7|+1 MORTE grossiere   <- reprise
   2.661   3.022 r   p=4 vivante                          <- millieme
   2.66    3.556 r   p=4 vivante   7|+1 MORTE grossiere   <- G_neuve
   2.659   4.089 r   p=4 MORTE fine                       <- millieme
   2.679   6.578 r   p=4 vivante                          <- millieme
   2.68    7.111 r   p=4 vivante
   2.681   7.644 r   p=4 MORTE fine                       <- millieme
   2.63   19.556 r   p=4 vivante
   2.76   49.778 r   p=4 vivante                          <- temoin
   2.79   65.778 r   p=4 MORTE fine                       <- temoin
   2.82   81.778 r   p=4 vivante                          <- temoin
LECTURE, ET ELLE EST FRANCHE :
  LES DEUX GROSSIERES SONT IMPAIRES ET TOUTES DEUX A MOINS DE 3.6
  RAYONS -- 1.778 et 3.556. Aucune grossiere au-dela. C'est un COEUR,
  etroit, et c'est exactement la portee que H-A annoncait ("~2 rayons,
  echappatoire jusqu'a ~4").
  LES TROIS MORTES p=4 SONT FINES ET DISPERSEES -- 4.089, 7.644 et
  65.778 rayons. La derniere est un TEMOIN, a soixante-six rayons du
  site : elle ne peut pas etre un effet de site. C'est l'arriere-plan
  REGIONAL, et c'est la seconde moitie de ce que H-A predit.
  Les deux mecanismes ne se melangent pas : l'impair grossier vit dans
  le coeur, le p=4 fin est partout.

=======================================================================
3. LE MILLIEME -- PREMIERE MESURE D'ENTRELACEMENT DE LA CAMPAGNE
=======================================================================
Strate 2 ouverte en forme derivee (N_2 x (1 - q4_fen) = 1.842 >= 1),
quatre lignes p=4 autour des deux survivants les plus proches :
   2.661  3.022 r  VIVANTE      2.659  4.089 r  MORTE (fine)
   2.679  6.578 r  VIVANTE      2.681  7.644 r  MORTE (fine)
DEUX MORTS AU MILLIEME, CHACUN ENCADRE DE VIVANTS. Le crible a donc
une structure SOUS le centieme : la maille de 48.3 n'est pas la
resolution du phenomene, seulement celle a laquelle on l'avait
regarde. C'est le resultat que la strate 2 existait pour rendre, et
il tombe du bon cote -- "quelle qu'en soit l'issue" etait la
consignation ; l'issue est positive.
Fait de geometrie a consigner sans lecture : les deux morts du
millieme sont les deux points les PLUS ELOIGNES du site de leur
paire (4.089 contre 3.022 ; 7.644 contre 6.578). Deux cas sur deux.
Aucune porte ne s'y adosse -- c'est une observation, et la manche
suivante saura ou regarder.

=======================================================================
4. POURQUOI H-A EST DECLAREE, ET CE QUE CELA NE DIT PAS
=======================================================================
La porte 2x2 : D = r1 ET G_neuve = VRAI ; S = (k4_F = 3 ET k4_T = 0)
= FAUX, car k4_F vaut ZERO. H-A ssi D et non S : declaree.
H-B N'A PAS PU TIRER, et pas par accident : sa prediction propre
etait un partage maximal (3, 0) -- trois morts p=4 dans la fenetre,
zero au temoin. On a mesure ZERO mort p=4 dans la fenetre et UNE au
temoin. C'est le contraire exact de sa prediction. La selectivite de
rang (6,2) ne se manifeste pas au centieme sur des valeurs neuves.
CE QUE H-A NE DIT PAS : la porte n'etait pas probabilisable
d'avance (le gel l'ecrit : "injouable en probabilite, jouable en
signal"). H-A est donc declaree sur un SIGNAL, pas sur un test de
puissance. Elle repose sur deux faits : la reproduction de la
grossiere de M12 sous un instrument DIFFERENT (la liste des
differences est le diff P-f, delta 74), et une grossiere NEUVE dans
le coeur. Le second est le fait neuf ; le premier est une
reproductibilite.

=======================================================================
5. P-d CONFRONTEE -- CE QUE J'AI EU JUSTE, CE QUE J'AI EU FAUX
=======================================================================
Mon attente est scellee au delta 73, section 4, avant toute mesure.
Je la confronte ligne a ligne, sans rien reecrire.
  JUSTE. La reprise : r1 donne a 0.85 -- r1. G_neuve : donnee a 0.35
    quand le gel la disait "porte etroite" -- elle est vraie, et par
    2.66, l'unique candidat que j'avais nomme.
  JUSTE, ET CONTRE LE GEL. La lisibilite de (i) : le gel donnait le
    plancher de comptes a 0.0462 sous Bernoulli independant, je le
    donnais a 0.25 en invoquant une survie SPATIALEMENT STRUCTUREE.
    LE PLANCHER EST ATTEINT (A4 l'implique). Un facteur cinq separait
    nos deux attentes ; l'evenement est tombe du cote du mien.
  FAUX, ET C'ETAIT MA PREDICTION NOMMEE. "k4_F = 1, et la morte est
    2.63" : k4_F = 0, et 2.63 VIT. Je le placais a 19.556 rayons, en
    plein dans l'anneau de mortalite [12.4, 23.1] que je lisais dans
    le registre M15. Il survit.
  FAUX AUSSI. S1 = 2 donne a 0.45 et B1 a 0.70 : c'est B2, que je
    donnais a 0.20. Et k4_T = 0 donne a 0.70 : c'est 1.
  FAUX SUR LA BRANCHE. NON-DEPARTAGE 0.66, H-A 0.30 : c'est H-A, mon
    second choix.
L'ANNEAU EST REFUTE, ET JE LE VERSE. Le motif V V M M M M V V M des
neuf points p=4 de M15, que j'avais chiffre a p = 0.0714 en le
declarant POST-HOC et sans valeur de preuve, ne se reproduit pas :
2.63 devait mourir, il vit ; et les morts p=4 de cette manche sont a
4.1, 7.6 et 65.8 rayons, sans bande contigue. Le 0.0714 reprend
exactement la valeur que je lui avais assignee d'avance : celle d'une
coincidence dans neuf points.
CE QUE JE MAINTIENS : la survie n'est PAS iid a la borne q_L. Le
plancher est tombe la ou le gel l'annoncait a une chance sur
vingt-deux, et zero mort p=4 sur trois valeurs neuves quand la borne
en prevoyait deux. Mais le mecanisme que j'avais propose pour cette
structure -- un anneau en distance -- est faux. Structure, oui ;
anneau, non.

=======================================================================
6. STATUT DU RUN, SANS ATTENUATION
=======================================================================
EXECUTE SOUS COPIE DE TRAVAIL MACHINE 2, NON CONTRESIGNEE.
m16_crible_v6_M2.py differe de m16_crible_v6.py (e804242bf9c284a4,
machine 1) par TROIS blocs, tous dans l'ECRITURE, aucun dans la
MESURE :
  (1) D-40 : serialiseur certifie du pilote au lieu de json.dump nu ;
  (2) le test negatif du serialiseur sur le bloc G6 REEL du point
      fixe -- il mord a chaque execution ;
  (3) D-41 : FondReel.ancres_XB lit le pas par pas_final(note du cote
      retenu), patron EXTRAIT de m15_site83_v2 l.1699-1706, au lieu
      d'un champ "pas" qui n'existe pas dans la carte.
Les verdicts sont donc ceux que la version contresignee reproduira :
la chaine est deterministe, le point fixe le prouve au bit, et aucun
des trois blocs ne touche la mesure. MACHINE 1 CONTRESIGNE, et la
contresignature referme E19 sur le script.
DEUX ARRETS PAYES AVANT CE RUN, tous deux miens :
  le premier run a mesure ses 31 lignes puis est mort sur
  KeyError 'pas' dans ancres_XB -- defaut que j'avais DIAGNOSTIQUE au
  pre-vol de la v3 (D-27c) et OMIS de porter dans mon patch. Quinze
  minutes perdues, aucun artefact.
  le second arret, hors ligne : v["sM"] vaut None chez M12 la ou M15
  OMET la cle. Difference de CONVENTION entre deux artefacts, jamais
  relevee -- et elle vaut regle : lire des ancres a travers deux
  manches demande de gerer les deux conventions.
LECON, ET ELLE EST A MOI : j'ai teste le chemin d'apres-mesure HORS
LIGNE avant la seconde tentative, et il a rendu ses deux defauts en
trente secondes. Je ne l'avais pas fait avant la premiere. Un chemin
qui ne s'execute qu'apres la mesure se teste AVANT la mesure, avec
des donnees fabriquees -- c'est la meme lecon que M11 v2 et M14, sous
un troisieme visage.

=======================================================================
7. CE QUE CE RUN N'ETABLIT PAS
=======================================================================
- Il ne falsifie PAS l'etage B : A4 est une CONSIGNATION, le centrage
  n'est pas discrimine (n_disc = 0).
- H-A est declaree sur signal, pas sur puissance : la porte n'etait
  pas probabilisable, le gel l'avait dit d'avance.
- Le millieme n'a que quatre lignes, toutes a p=4 : aucune batterie
  impaire n'y a ete jouee, donc aucun E n'y est derivable.
- La reproduction de la grossiere de M12 vaut sous l'instrument M16,
  dont les differences avec M12 sont listees au diff P-f (delta 74) ;
  elle ne dit rien de plus.
- Aucune re-derivation des artefacts anterieurs n'est faite ici :
  l'inventaire N-33 a ete re-derive PAR LE RUN, asserts passes.
- Aucun numero d'erratum n'est attribue ici (E18).

EMPREINTES RE-DERIVEES LE 2026-08-12 (N-48) : artefact 1118a4692e07efe4 ;
gel v10 75bc4020b5bd560f ; script machine 1 e804242bf9c284a4 ; copie de
travail machine 2 (au pied du delta) ; couche manche 41ddebcd72b96e64 ;
pilote 663b17e2955c79c0 ; moteur c8ed357b120352c4 ; artefacts sources
96d78407, fa109da9, 22fa1760, 7cf3624b, ad275870.

=== FIN -- M16 JOUEE : B2, H-A, A4, r1 ; LE MILLIEME EST ENTRELACE ===
