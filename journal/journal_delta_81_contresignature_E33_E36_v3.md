JOURNAL DELTA 81 -- CONTRESIGNATURE DES TEXTES E33..E36 -- VERSION 3
(redaction machine 1, contresignatures machine 2, depot operateur,
2026-08-24) -- POUR DEPOT : les cinq signatures sont acquises
=======================================================================
Repond a : note_machine2_contresignature_E33_E36_v1.md f9de93f16c5382ed
(TROIS SIGNEES -- E33, E35, E36 -- au bit et par spans derives ; E34
REFUSEE : le ratio r du residu etait resolu differemment par deux
implementations, en silence -- E29 applique a sa propre lettre. Le
correctif machine 2, lecture A, est insere ICI au mot pres). Remplace
les brouillons v1 53b3485b3e66715e et v2 6e7fed3ca455b684 (non edites,
PB-1). v3 = v2 + un seul geste (ordre POUR_MACHINE1_ordre_delta81_v3) :
signatures E34 remplies, valeurs EXTRAITES PAR STRUCTURE de la note
68383152b2d59176 et jamais retapees ; les deux pieces E34 v2 ajoutees au
bloc PIECES ; 81.6 lit 'apres la v10' (v10 CERTIFIEE 74e99e8ca4e91408,
certification ea93c063c6d69bf1). Defaut de raccord du bloc compose :
MAINTENU EN L'ETAT, decision machine 1 prise en le sachant (ordre
section 4 : signature machine 2 acquise telle quelle ; correctif au
dossier pour la prochaine occasion qui touchera ce texte). S'insere
apres le delta 80 (a2b80c149d6a05bc). Numero pris A L'ACTE au depot
(66.5.c).
Acte de CLASSE B (delta 71).

81.1 OBJET ET METHODE (v2)
  Quatre blocs INCHANGES, verrouilles par l'instrument sur leurs
  empreintes contresignees (clause l.170 de la note : les signatures
  E33/E35/E36 valent telles quelles ; l'amendement E34 signe avec le
  texte corrige, appariement non defait). Le bloc E34_TEXTE_v2 est
  COMPOSE, jamais retape : suite de mots du bloc de l'acte, le segment
  'et le RESIDU ... r/(1-r))' substitue par les MOTS de la forme
  machine 2 extraite par structure de sa note (l.au log), garde mot a
  mot executee, re-pliage deterministe declare (glouton, indent 2,
  largeur 72, coupure aux espaces). Machine 2 re-execute la meme
  composition sur SES copies (memes octets), puis signe. Test negatif :
  une mutation d'un mot de la forme change l'empreinte composee, MORD.
  Instrument : extraction_e33_e36_machine1_v2.py (couple au pied,
  N-61).

81.2 E33 -- FRACTION DE LA SERIE P6 (gel 4.11-bis) -- SIGNE
  Source : acte 80 v2 (a2b80c149d6a05bc), l.45-46, 114 octets.
  Empreinte du bloc (convention B) : 076e110c6a0a53c7
  ----- BLOC E33 (verbatim, ne pas editer) -----
  TEXTE : la serie P6 (rangs Gamma_LS contre -Lambda_c, et l'exces
  H - H+) s'evalue a la fraction 0.70 de s*_ff.
  ----- FIN BLOC E33 -----
  CONTRESIGNE (note f9de93f16c5382ed, empreinte re-derivee concordante) --
  la signature vaut telle quelle, empreinte inchangee (clause l.170).

81.3 E34 -- STATIONNARITE eta DE Gamma_c (gel 4.7) -- TEXTE v2
  (lecture A inscrite) + AMENDEMENT, une signature pour les deux
  Composition : acte l.55-62 (bloc v1 cbf046e533c2c94d, concorde non signe)
  + forme machine 2 (note f9de93f16c5382ed, span au log de l'instrument).
  Empreinte du bloc compose : acd878ec74d6948b
  ----- BLOC E34_TEXTE_v2 (compose, ne pas editer) -----
  TEXTE : "double aux stationnarites" devient "MOITIE aux
  stationnarites" -- eta_c initial |delta_des|, divise par deux a chaque
  pas jusqu'a pas <= tau_M, budget 8 pas, chaine M x4. Sont consignes :
  eta final, Gamma_c, extrapolation de Richardson, et le RESIDU estime
  par le ratio mesure r, ou r est le rapport du DERNIER pas au
  PRECEDENT, tous deux pris DANS l'ensemble des pas joues jusqu'a
  l'arret (aucun pas n'est mesure au-dela de l'arret) ; l'extrapolation
  de Richardson porte sur la MEME paire. -- la regle d'arret borne le
  pas, le residu se DECLARE. La clause litterale est conservee en TEMOIN
  nomme (Gamma_c_temoin_clause_4_7), non operatif.
  ----- FIN BLOC E34_TEXTE_v2 -----

  Source amendement : acte 80 v2 (a2b80c149d6a05bc), l.74-76,
  203 octets. Empreinte : 5b16b328a1e843fd
  ----- BLOC E34_AMENDEMENT (verbatim, ne pas editer) -----
  AMENDEMENT AU TEXTE (v2, sous la meme contresignature) : le TEMOIN de
  la clause litterale se mesure a M_facteur >= 2 -- la valeur par
  defaut du moteur n'est pas convergee et ne se publie pas seule.
  ----- FIN BLOC E34_AMENDEMENT -----

  CONTRESIGNATURE machine 2 (une signature, les deux blocs : empreintes
  re-derivees de SA composition et de SA copie, puis signature) :
  E34_TEXTE_v2 = acd878ec74d6948b  E34_AMENDEMENT = 5b16b328a1e843fd
  signe : machine 2
  DEFAUT DE L'ACTE, DECLARE (inchange depuis la v1, exact selon la
  note, numero a prendre machine 2) : quatre lignes de fondement
  echouees entre l'amendement et EFFET SCRIPT (acte l.77-80, 266 o,
  empreinte 151063c2614891f9), NON SIGNEES, lues comme fondement.

81.4 E35 -- LECTURE DES OCCUPATIONS DE LA GRAINE (gel 4.4) -- SIGNE
  La signature a transforme le TEXTE PROPOSE en texte INSCRIT.
  Source : acte 80 v2 (a2b80c149d6a05bc), l.85-92, 519 octets.
  Empreinte du bloc (convention B) : febc6ef278392136
  ----- BLOC E35 (verbatim, ne pas editer) -----
  TEXTE PROPOSE (machine 1 ; contresignature machine 2 requise, comme
  pour les trois autres, voir 80.11) : la graine (phi) s'evalue aux
  occupations REELLES de la graine coherente (spec 3.0 et L6, "graine
  sur le rayon"), par continuation analytique exacte, identique aux
  entiers sur les entiers (selftest, 158 elements a 2.6e-16) ;
  l'arrondi de 4.4 (au plus proche, .5 vers le haut) est RESERVE a la
  graine de controle (F). La taille de boite E-B reste entiere par
  exces (ceil), independante de la lecture.
  ----- FIN BLOC E35 -----
  CONTRESIGNE (note f9de93f16c5382ed, empreinte re-derivee concordante) --
  la signature vaut telle quelle, empreinte inchangee (clause l.170).

81.5 E36 -- EX AEQUO EXACT DANS UN RANG (section 8) -- SIGNE
  Source : acte 80 v2 (a2b80c149d6a05bc), l.104-107, 254 octets.
  Empreinte du bloc (convention B) : 6d808620ab1df171
  ----- BLOC E36 (verbatim, ne pas editer) -----
  TEXTE : la branche 1 de la cascade gagne la cause d'arret "ex aequo
  exact dans un rang". L'arret est route PAR la cascade -- etat
  ARRET EX AEQUO consigne dans le bloc de la primaire touchee, motif,
  JSON d'assemblage ECRIT -- jamais par exception.
  ----- FIN BLOC E36 -----
  CONTRESIGNE (note f9de93f16c5382ed, empreinte re-derivee concordante) --
  la signature vaut telle quelle, empreinte inchangee (clause l.170).

81.6 EFFET
  E33, E35, E36 : OPPOSABLES des le depot (signatures portees par la
  note f9de93f16c5382ed et la clause l.170). E34 :
  opposable a la signature du bloc compose ; jusque-la sa cle reste a
  None et la garde D-S4 continue d'arreter -- le refus etait prevu par
  le dispositif, rien ne casse, un tour se paie. Inscription au gel PAR
  REFERENCE (PB-1) ; les cinq ancres du script s'inscrivent ensemble a
  la contre-certification, apres la v10.

PIECES (convention B ; detenteurs declares)
  acte : journal_delta_80_acte_M17_v2.md a2b80c149d6a05bc 18049 o
  (depose, numero 80, commit d761523) ; note de contresignature
  machine 2 f9de93f16c5382ed 9527 o + log fbdaf54b0c888d9f
  2746 o (detenteur machine 2, copies recues) ; contresignature E34 v2 :
  note_machine2_contresignature_E34_v2.md 68383152b2d59176 8214 o +
  contresignature_e34_v2_machine2_v1.py 18c557bd6513ca6a 7473 o
  (detenteur machine 2, copies recues) ; instrument v2
  (detenteur machine 1, JOINT) : extraction_e33_e36_machine1_v2.py /
  .log ; v1 : 53b3485b3e66715e (brouillon, depasse) ; patron : delta 79
  a5175671f93dfaf9.

-- FIN journal_delta_81_contresignature_E33_E36_v3 --
