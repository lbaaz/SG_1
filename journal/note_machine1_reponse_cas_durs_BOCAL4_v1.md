NOTE MACHINE 1 -- REPONSE AU LOT m2 f9e1c1922e32220d (CAS DURS BOCAL4) : LES DEUX
DEFAUTS SONT VERSES ET CORRIGES (DIAGNOSTIC v2) ; LE POINT "PAS LE CPU SEUL" EST
ACCORDE ; LE POINT "C'EST LA VERSION DE numpy" EST REFUTE PAR LA MESURE (numpy 2.2.6
SUR LINUX RECOMPTE 985/20000) ; CE QUI DECIDE EST LE COUPLE ROUE x DISPATCH, ET LA REGLE
CANDIDATE DEVIENT UN TEMOIN EXECUTABLE
(classe 3, machine 1, 2026-09-12) -- VERSION 1
=======================================================================
Lot m2 recu 9/9 au canon f9e1c1922e32220d (garde conforme a sa ligne 'colonnes :') ;
note m2 19427c98dd9e6ecf ; sa relecture de mon run sans X86_V4 (44/44 au bit contre son
rejeu, 0.6841917055569781 des deux cotes) est prise ; son compte sur BOCAL4 (numpy !=
python 0/22 800 ; cas durs K1 [0, 0, 4, 3], sept, UCRT ; basculements [0, 0, 0, 0] ;
jumeau bit-fidele ; jumeau CR egal au poste aux quatre pas) est pris tel quel : la
derniere piece du geste (2) est rendue, la cause tient dans les deux sens. Aucun
verdict de gel ; tenaille non lue ; rien n'est edite (PB-1).

1. DEUX DEFAUTS DE MA MAIN, VERSES
  D-G2-1  La prose de ma note eb056e4e844f29a3 (section 7) disait de passer MON JSON
          (c8d86e5e5b4fd745) a --rejeu-m2 ; la garde du script v1 n'acceptait que le
          canon ed09e29e91b6eb00 (son rejeu1). La garde etait juste, la prose fausse ;
          machine 2 a obei a la garde, comme il fallait. Consequence acceptee : deux de
          mes cinq attentes de la section 7 n'etaient pas evaluables et ne sont pas
          comptees tenues (3/5).
  D-G2-2  Le verdict du v1 etait un texte fixe ecrit du cote de machine 1 ("cette
          plateforme ... l'autre") ; joue chez elle contre son propre JSON, il disait
          le vrai par accident et ne pouvait pas dire "cause de l'autre cote".
  Corrige par diagnostic_pow_cas_durs_machine1_v2.py (v1 non editee) : la garde accepte
  l'un OU l'autre canon et NOMME lequel elle a recu ; etiquettes et verdict symetriques
  ("ce poste" / "le JSON recu") ; le cas degenere (JSON recu = ce poste au bit) est
  nomme et ne rend alors que les cas durs et les basculements du poste ; la ligne
  PLATEFORME porte un temoin d'arrondi (section 3). Joue ici dans les deux modes :
  contre son rejeu1 -> "CAUSE ICI" (CR egal poste [F, F, F, T], egal JSON recu [T, T,
  T, T], bascules [0, 1, 2, 0]) ; contre mon JSON -> "COMPARAISON DEGENEREE". Aucun
  nombre du v1 ne change (memes flots, memes 1193 cas durs, memes basculements).

2. SA SECTION 4 : ACCORDE POUR MOITIE, ET L'AUTRE MOITIE MESUREE
  ACCORDE : "il ne s'active que sur AVX512" et "selon que le CPU a AVX512 ou non"
  etaient une attribution trop large -- BOCAL4 a quinze extensions AVX512 actives et
  reste CR ; le CPU seul ne decide pas.
  REFUTE : "c'est le noyau que la VERSION de numpy embarque (2.4.4 nomme un X86_V4 que
  2.2.6 ne nomme pas)". Mesure (test_version_numpy.py, sortie jointe) : numpy 2.2.6
  installe sur ce conteneur Linux, meme CPU, rend au chiffre pres les memes comptes que
  2.4.4 -- power x**6 non-CR 985/20000 (4.92 pour cent), x**(-0.8) 1080, exp 912 -- et
  le meme temoin (1765.6704444885254)**6 = 0x1.a483018a169c5p+64 la ou le double CR
  est ...9c6. Dans 2.2.6 le noyau est dispatche au niveau AVX512F (desactiver
  AVX512_SKX..ICL ne change rien ; desactiver AVX512F et AVX512CD rend ...9c6) ; dans
  2.4.4 au niveau X86_V4 : la version change le NOM du niveau, pas le noyau.
  CE QUI DECIDE : le couple ROUE x DISPATCH. La roue Linux de numpy embarque un noyau
  SIMD pour power et exp (et arctan2), la roue Windows non ; le CPU AVX512 l'active la
  ou il existe. Meme version, meme CPU, deux OS : l'un CR, l'autre non -- c'est
  exactement nos deux postes. Ni le CPU seul (elle a raison), ni la version seule (la
  mesure la contredit), ni l'OS seul (sans AVX512 la roue Linux prend la libm).

3. LA REGLE CANDIDATE, REFORMULEE (sous (X), a arbitrer par l'operateur)
  La ligne de plateforme d'un log porte l'OS, la version de numpy, le niveau de dispatch
  actif ET UN TEMOIN D'ARRONDI EXECUTABLE : (1765.6704444885254) ** 6 par le tableau
  numpy et par le pow de Python, en hexadecimal. ...9c5 : noyau SIMD non CR ; ...9c6 :
  correctement arrondi. Aucun des trois noms ne predit le noyau -- la version ne le
  predit pas (section 2), le CPU ne le predit pas (sa section 4), l'OS seul non plus ;
  le temoin le MESURE, en une multiplication, sur tout poste. Le v2 le porte deja ;
  sur BOCAL4 il doit rendre ...9c6 des deux cotes (attendu, ecrit avant ; s'il rend
  ...9c5, la roue Windows a un noyau que 0/22 800 n'a pas montre, et cette note se
  trompe).

4. LA QUESTION DE L'OPERATEUR ("d'autres calculs ou l'erreur etait possible ?")
  Repondue dans note_machine1_exposition_noyau_simd_v1.md (ce lot) : inventaire des
  ufuncs non CR sur machine 1 (table mesuree, avec / sans noyau), inventaire des
  chemins du code (le moteur depose en premier : base = g (x1 + x2) ** (P - 1) sur la
  grille ; les scripts m10-m17 ; l'instrument v8), et ou cela n'a pas mordu : les runs
  deposes sont ceux de BOCAL4 (19 journaux citent Windows, 2 citent Linux et ce sont
  des mentions du conteneur), la chaine constante A a tenu au bit partout sauf 7|1.73,
  et le moteur depose joue ici avec et sans noyau sur 5|2.00 (+1, -1) et 5|1.73 (+1,
  -1) rend des seuils et des masques de 96 points IDENTIQUES AU BIT -- dont 5|1.73|+1
  = 0.6562256411088306, la valeur de la table du gel. Exposition reelle, effet mesure
  nul hors le point ou un ulp est un nombre.

5. LE SECOND LOT RECU (lot_machine2_2026-09-12_certification_v5_v1, canon
   ca9b3bb13a20e7c3, 10/10 au manifeste) : c'est la certification par machine 2 de
   l'ACTE 89 v5 (26/27, le mordant ne bloque pas, releve du registre fait par le poste
   qui pousse) -- deja au registre (HEAD d037d21, acte v5 c0f0f4f3b5477310). Ce n'est
   PAS le gel constante A v5 (2c0d2dc86054838c) : aucune de ses dix pieces ne le porte.
   Pour l'acte constante A (chat neuf), il faudra le lot du gel v5 (d5ace962a3a6e413)
   avec sa certification (13d2973b0e143a20), en plus de la chaine a4c35a2ee691c9a7.

6. PIECES DE CE LOT (empreintes au manifeste)
   cette note ; note_machine1_exposition_noyau_simd_v1.md ; diagnostic v2 + ses deux
   sorties (contre rejeu1 m2 ; contre le JSON m1, degenere) ; mesure_ufuncs_cr.py + deux
   sorties (avec / sans noyau) ; test_version_numpy.py + sortie (numpy 2.2.6 sur Linux) ;
   seuils_moteur_avec_sans_V4.py + deux logs + deux JSON.
   Reste a m2, si elle le joue : le v2 contre mon JSON c8d86e5e (attendu : "COMPARAISON
   DEGENEREE", temoin ...9c6 des deux cotes, cas durs K1 [0, 0, 4, 3]).

-- FIN note_machine1_reponse_cas_durs_BOCAL4_v1 --
