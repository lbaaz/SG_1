# POUR MACHINE 1 -- RESULTAT DE L'ETAGE 1 DE LA NUIT E-B (BOCAL4)
# machine 2, v1, 2026-11-12. Classe B. Entrants : gel v2 cde0cd11a763f26d,
# moteur v17 82a0be882568fe0c, sonde v2 facc7536ba4637cb, feuille
# b3ac958a1a2b915b, ma reference TP certifiee (liste 69b3bab3bb8480b7, table
# 4d51dd58ef456fe9, retenus j = 6 et j = 8). Rien n'a ete modifie, aucun
# seuil touche, aucun numero E18 pris.

## 0. LE RESULTAT, EN QUATRE PHRASES

**VERDICT DE L'ETAGE 1 : NE TIENT PAS**, lu par ta feuille certifiee sur ma
table, avec les deux motifs 'TP ne tient pas a j06' et
'TP ne tient pas a j08'. La sonde a joue
sans erreur (code 0, 03h00 -> 04h15, 1 h 15) et tous ses garde-fous G-Q1 a
G-Q5 et G-Q10 sont tenus. Le temoin positif TIENT en G30 (plateau, accord a
0.6 % et 0.8 %) et NE TIENT PAS en G20 (pas de plateau de cinq valeurs) ; la
regle du gel exige les deux. **L'etage 2 n'a PAS ete lance** (regle du gel ;
la sonde le refuse sans verdict TIENT) ; la commande 4 de la feuille non
plus : il n'y a pas de sonde_etage2.json.

## 1. CE QUI A TOURNE (E19)

  Etage 1 de la sonde v2, taille reelle (r0 = 40, G20 : N = 60, G30 : N = 70),
  avec ma liste P-1 (j = 6, g = 0.08408964152537146 ; j = 8, g = 0.1), puis
  la feuille v1 --etage 1 sur ma table. Plateforme : Windows AMD64, python
  3.11.9, numpy 2.2.6 (la ligne `plateforme` est dans le journal). Ton
  pre-vol (Linux, numpy 2.5.3, geometrie reduite, non opposable) n'est pas
  comparable a ce run. Aucun etage 2, aucune mesure M17.

## 2. LES GARDE-FOUS

  G-Q1 moteur 82a0be882568fe0c OK ; G-Q2 manche : 36 au canon et a la taille
  == 36 lignes du manifeste, hors manifeste 'pt_39_20_f100.zip' (attendu, ni
  ouvert ni compte) ; G-Q3 six matrices OK ; G-Q5 plancher : 30 valeurs, max
  |Gamma(H+)| = 1.330e-13 contre 1e-12 ; G-Q10 : TP 60 joues, plancher 30
  joues, TN 3 joues + 12 sautes == 15 ; G-Q7 selftest de la feuille 13 sur 13 ;
  selection : sonde [6, 8], reference [6, 8], regle du gel rejouee [6, 8].

## 3. LE TEMOIN POSITIF (la feuille, au chiffre)

  j = 6, g = 0.08409, Gamma_ref 5.3688e-10, u_ref 2.1e-03 (seuil 0.0521)
    G20 : PAS DE PLATEAU, etalement 0.3847, k0 = -2        -> NE TIENT PAS
    G30 : PLATEAU, Gamma_pl 5.4009e-10, etalement 0.0276,
          |ln| = 0.0060                                    -> TIENT
  j = 8, g = 0.10000, Gamma_ref 6.4279e-09, u_ref 1.6e-04 (seuil 0.0502)
    G20 : PAS DE PLATEAU, etalement 0.4214, k0 = -2        -> NE TIENT PAS
    G30 : PLATEAU, Gamma_pl 6.3775e-09, etalement 0.0344,
          |ln| = 0.0079                                    -> TIENT

## 4. CE QUE LES TRAJECTOIRES BRUTES MONTRENT (lecture, pas decision)

Lu dans sonde_etage1.json, Gamma(k), k = -2 ... 12, etat de vide suivi.

  j = 6, G20 : k = -2, -1, 0, 1 : 5.373, 5.389, 5.473, 5.264 e-10 ; k = 2 :
    3.953e-10 (-25 %) ; ensuite Gamma divise par ~2 a chaque k (3.9e-10
    -> 2.3 -> 1.2 -> 6.3e-11 ...), c'est-a-dire Gamma proportionnel a eta.
    Les QUATRE premieres valeurs sont a 3.97 % les unes des autres, et le
    premier point (5.373e-10) est a +0.08 % de Gamma_ref ; la fenetre de
    cinq (k0 = -2 : k = -2 ... 2) englobe la chute de k = 2.
  j = 8, G20 : k = -2, -1, 0 : 6.429, 6.442, 6.486 e-9 (a 0.9 %) ; k = 1 :
    6.085e-9 (-6.2 %) ; k = 2 : 4.563e-9 ; puis ~ eta. Le premier point est
    a +0.02 % de Gamma_ref.
  j = 6, G30 : k = -2 ... 2 : 5.398, 5.365, 5.378, 5.359, 5.506 e-10
    (plateau de cinq, 2.8 %) ; puis une BOSSE : k = 3 ... 6 : 6.71, 9.35,
    11.25, 9.29 e-10 (jusqu'a 2.1 fois le plateau) avant la chute en eta.
  j = 8, G30 : k = -2 ... 2 : 6.429, 6.428, 6.427, 6.392, 6.215 e-9
    (plateau de cinq, 3.4 %) ; k = 3 : 5.73e-9 puis chute en eta.

En clair : en G20 la valeur de Gamma aux petits k est celle de la reference a
0.1 % pres ; ce qui manque est la LONGUEUR du plateau (quatre valeurs
au lieu de cinq pour j = 6, trois pour j = 8), la chute en eta commencant a
k = 2 (j = 6) ou k = 1 (j = 8) a N = 60 ; a N = 70 elle est repoussee d'au
moins un k pour j = 8 et, pour j = 6, precedee d'une bosse. Je n'ai teste aucun autre k ni aucune autre geometrie : la grille K_ECH et le
critere de cinq valeurs sont ceux du gel. Je ne tire de cela aucune
correction ; toute suite (lecture, v3, geometrie) est ta decision et celle de
l'operateur, et le gel interdit d'assouplir apres lecture.

## 5. LE TEMOIN NEGATIF (observation, sans motif dans la feuille)

La sonde a suivi les trois candidats [50, 25], [55, 27], [45, 22] au point
de reference k = 3 (Gamma = 0.898, 2.449, 0.669) ; a k = 2 et k = 4 aucun
candidat n'est suivi par recouvrement, donc les douze autres k sont SAUTES
(G-Q10 le compte : 3 + 12 == 15). La feuille lit AUCUNE FENETRE aux trois et
rend 'TN : NON JOUE' ; son code ne leve pas de motif dans ce cas (seul
'TN rend PLATEAU' en leve un). Je le consigne tel quel : la question de savoir
si 'NON JOUE' est le comportement attendu du temoin negatif a taille reelle est
a ton gel, pas a moi.

## 6. CE QUE CETTE PIECE NE DIT PAS

Elle ne dit pas que la sonde est fausse ni qu'elle est juste : elle dit ce
que la regle du gel rend sur ma reference. Elle ne dit rien de M17 (etage 2
non joue). Selon le code de la feuille (cascade), un etage 1 qui ne tient pas
rend NON CONCLUANT D'INSTRUMENT ; je n'ai pas emis ce statut (la commande 4
n'a pas ete jouee). A porter a l'acte : D-QEB-1, O-A, O-C, O-D (de la
certification de la reference), plus les observations des sections 4 et 5.

## 7. REJEU

Depuis BOCAL4, dossier de sortie NEUF, `python -P` (jamais -I : numpy est en
user-site) :
  python -P sonde_qualification_EB_machine1_v2.py --moteur m17_chaine_v17.py
    --run manche_m17_v17 --manifeste manche_m17_v17_MANIFEST_machine2.txt
    --sortie S --etage 1 --retenus tp_retenus_machine2_v1.json
  python -P lecture_qualification_EB_machine1_v1.py --etage 1 --sortie S
    --reference tp_reference_machine2_v1.json
Duree mesuree sur BOCAL4 au repos : 1 h 15 (j'avais annonce ~2 h). Sur une
autre plateforme les Gamma bougent au niveau du bruit dense (zgeev) ; les
etalements de 0.38 et 0.42 de la section 3 sont loin de ce niveau.

## 8. PIECES (convention B ; le manifeste du lot porte les empreintes brutes)

    cette note
    nuit_EB_etage1/sonde_etage1.json     ab31334aea5c444a   (sortie de la sonde)
    nuit_EB_etage1/sonde_etage1.log      edafd162f58f9720   (journal de la sonde)
    nuit_EB_etage1/console_etage1.log    baaccd2b3cad5a5b   (idem + code de sortie 0 + heure de fin)
    nuit_EB_etage1/verdict_etage1.json   aef856818424689a   (verdict de la feuille)
    nuit_EB_etage1/lecture_etage1.log    94e008b420e3ba38   (journal de la feuille)
    fabrique_lot_resultat_etage1_nuit_EB_machine2_v1.py

Non joint : le dossier sortie/reprise/ (279 petits fichiers de reprise, dont
les vecteurs propres .npy) : leur contenu utile est consolide dans
sonde_etage1.json.

-- FIN POUR_MACHINE1_resultat_etage1_nuit_EB_machine2_v1 --
