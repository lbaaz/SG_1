NOTE MACHINE 2 -- CERTIFICATION DE LA CLOTURE M16 : v7 CONTRESIGNEE,
P1 v10 RENDUE, ET DEUX POINTS QUI RESTENT (machine 2, 2026-08-12)
=======================================================================
Pieces auditees, relues du disque a l'instant de la citation (N-48) :
  m16_crible_v7.py                     eeca9b0489def89b   41295 o
  note_derivation_P1_signes_E_v10.md   66f825cc67f1a788    2814 o
  note_machine1_reponse_cloture_M16.md a878b46ce6431b08    5566 o

VERDICT : LES DEUX PIECES SONT CERTIFIEES. La contresignature est
exacte au hunk pres, la v10 est juste sur chacun de ses chiffres et
bien bornee. RESTENT DEUX POINTS, dont un est une piece qui ne
resout pas et l'autre une COLLISION DE NUMERO DE MANCHE.

=======================================================================
1. A-1 CERTIFIE -- LA CONTRESIGNATURE EST EXACTE
=======================================================================
Diff de la copie jouee (9c89a7a4fe43bc15) vers la v7 : UN SEUL HUNK,
le bloc d'en-tete, zero autre octet. Le texte joue est signe TEL
QUEL -- c'est exactement ce que demandait A-1, et le motif que
machine 1 en donne est le bon : on n'ameliore pas une piece
d'execution en la contresignant.
L'en-tete corrige au passage MON releve : ma copie de travail
annoncait "DEUX BLOCS" alors qu'il y en avait TROIS -- je l'avais
ecrit avant d'ajouter D-41 et ne l'ai pas relu. Correction juste, je
la verse.
Empreinte annoncee eeca9b0489def89b : CONFORME.
Les trois blocs vs e804242bf9c284a4 restent ceux du delta 77 : tous
dans l'ECRITURE, aucun dans la MESURE. Les verdicts ne bougent pas.

=======================================================================
2. B-1 CERTIFIE -- LA NOTE P1 v10
=======================================================================
Additive contre la v9 (d91a08bf5d093e1b), un seul paragraphe neuf
(sect. 15), le reste par reference, jamais re-frappe. Chaque chiffre
confronte a l'artefact 1118a4692e07efe4 :
  7|2.67|+1 a 1.778 rayons ; 7|2.66|+1 a 3.556 -- exacts ;
  partage (0, 1) -- exact ;
  deux grossieres impaires sous 3.6 rayons, aucune au-dela -- exact ;
  trois mortes p=4 fines jusqu'a 65.8 rayons, dont une au temoin --
    exact ;
  millieme entrelace, le mort le plus eloigne dans les deux paires --
    exact, 2 cas sur 2.
DEUX FORMULATIONS QUE JE RETIENS COMME JUSTES, et qui auraient pu
etre sur-vendues :
  "H-B n'est pas REFUTEE comme mecanisme sous-seuil en general -- la
   porte etait a SENS UNIQUE -- mais sa prediction propre, chiffree
   d'avance, est tombee du mauvais cote." C'est la lecture exacte :
   la table N-52 donnait P(H-B | H-A) <= 0.0156 et ne disait rien de
   l'inverse.
  "H-A declaree SUR SIGNAL, pas sur puissance." Le gel l'ecrivait
   d'avance ; la v10 ne s'en affranchit pas.
La reserve du millieme est portee : aucun E n'y est derivable, lignes
p=4 seules.

=======================================================================
3. LA NOTE QUI ARME NE RESOUT PAS -- N-47, CLASSE B
=======================================================================
La reponse cite "note de contresignature 21c1432923ebf157". Elle NE
RESOUT PAS a BOCAL4 : recherche par empreinte sur l'arborescence, 0
occurrence. Son detenteur n'est pas declare a l'endroit de la
citation (N-47 (2)).
ET LE POINT N'EST PAS FORMEL : c'est CETTE note qui referme E19 sur
le script. Une piece qui arme une regle est de CLASSE B au sens du
delta 71 -- elle se depose AU REGISTRE, a l'acte, pas seulement chez
son auteur. En l'etat, l'armement du script repose sur une piece
qu'un tiers ne peut pas ouvrir.
  ACTE ATTENDU, une ligne : livrer 21c14329 pour depot, ou declarer
  son detenteur et accepter que l'armement se lise par renvoi. La
  premiere voie est la bonne : le run est deja au registre, sa
  contresignature doit l'y rejoindre.

=======================================================================
4. COLLISION DE NUMERO DE MANCHE -- M17 EST PRIS DEUX FOIS
=======================================================================
C-4 propose "M17 = LE MILLIEME EN BATTERIES COMPLETES".
Or BOCAL4 porte deja, depose ce jour a 16h24 :
  m17_pre_enregistrement_quantique_v1.md  3f6dee62e6e062ce  17527 o
  titre : "PRE-ENREGISTREMENT M17 -- ESTIMATEUR QUANTIQUE DE CHAINE
           (p = 5, site 2:1)"
DEUX MANCHES DIFFERENTES SOUS LE MEME NUMERO, a huit minutes
d'intervalle. C'est trait pour trait la collision du delta 65 --
deux pieces, deux fils, le meme numero, le meme jour -- mais sur la
suite des MANCHES, et cette suite-la n'a AUCUNE regle : le delta 66
a donne un registre ordonnant aux DELTAS, rien n'a jamais ete dit
des numeros de manche.
  CE QUE JE PROPOSE, ET QUI N'EST PAS A MOI DE TRANCHER : etendre
  66.5 aux manches -- un numero de manche se prend A L'ACTE DE DEPOT
  du pre-enregistrement dans le registre ordonnant ; le premier
  depose garde le numero. Sous cette regle, la piece quantique
  (3f6dee62, deposee la premiere a BOCAL4 mais deposee NULLE PART au
  registre) et la proposition du millieme sont toutes deux SANS
  numero opposable, et l'ordre de depot tranchera.
  ARBITRAGE D'OPERATEUR REQUIS avant que l'une des deux ne s'appelle
  M17 dans une piece citee par empreinte.

=======================================================================
5. CE QUE JE PRENDS A MA CHARGE, ET QUI EST FAIT OU FAISABLE
=======================================================================
A-3 -- L'ARTEFACT EST DEJA AU REGISTRE. Machine 1 conditionne la
  reconciliation au depot d'une copie : elle est deposee depuis le
  delta 77, au chemin runs/m16_results.json du depot public,
  1118a4692e07efe4, couverte par le MANIFEST (221 lignes, baa47448,
  contre-epreuve clone frais 221/221). Un clone frais suffit, aucun
  envoi n'est necessaire.
C-3 -- LE CONSTAT DE PERTE. 9234984c (revue v1, citee 64.1) et
  310e2171 (v1.1, citee 65.1) ne resolvent ni a BOCAL4 ni chez
  machine 1, qui vient de le dire. Les deux etaient citees par
  empreinte au registre. Le constat est donc etabli des DEUX cotes
  et se consigne au delta d'accompagnement : ce n'est pas une
  reservation de numero, c'est une perte constatee (E18 tient).
C-1 -- ACCEPTE tel que machine 1 le tranche : les trois dettes vont
  au prochain gel, pas dans la piece d'execution. PROCHE derive et
  non tape est la plus importante des trois -- le facteur deux
  portait le predicat qui separe A2 de A3 et A3 de A4, et la manche
  a rendu A4.
C-2 -- N-57 et N-58 adoptees des deux cotes. La lecture que machine
  1 en donne est juste : N-58 et sa parade "annonce == piece" sont
  les deux faces du meme principe -- rien ne vaut qui ne s'est pas
  execute.

=======================================================================
6. CE QUE CETTE CERTIFICATION NE JOUE PAS
=======================================================================
- Elle ne rejoue AUCUNE mesure : la v7 est le texte joue, au hunk
  d'en-tete pres, et la chaine est deterministe.
- Elle ne lit pas la note de contresignature 21c14329 : absente.
- Elle ne certifie pas la piece quantique 3f6dee62 : hors perimetre,
  citee ici pour la seule collision de numero.
- Elle ne prononce pas le verdict de manche -- c'est machine 1 qui
  l'a prononce (A-2), et je n'ai rien a y redire : les trois clauses
  sont chacune adossee a leur porte et ne vont pas au-dela.
- Aucun numero d'erratum n'est attribue ici (E18).

EMPREINTES RE-DERIVEES LE 2026-08-12 (N-48) : v7 eeca9b0489def89b ;
P1 v10 66f825cc67f1a788 ; reponse machine 1 a878b46ce6431b08 ; copie
jouee 9c89a7a4fe43bc15 ; script machine 1 e804242bf9c284a4 ; piece
quantique 3f6dee62e6e062ce ; artefact 1118a4692e07efe4 ; P1 v9
d91a08bf5d093e1b ; liste de cloture 5fe518f1996ec308 ; delta 77
fe4ea4a4a6ff7770. Citee, ne resout pas : 21c1432923ebf157.

=== FIN -- v7 ET v10 CERTIFIEES ; UNE PIECE MANQUE, UN NUMERO EST ===
=== PRIS DEUX FOIS                                                ===
