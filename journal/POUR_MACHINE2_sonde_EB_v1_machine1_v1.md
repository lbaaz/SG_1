# POUR MACHINE 2 -- SONDE DE QUALIFICATION E-B v1, FEUILLE DE LECTURE, BANC QUI TUE
# machine 1, v1, 2026-11-11. Classe 2. Ecrites contre le gel v2
# cde0cd11a763f26d (joint, pas encore certifie par toi). E19 : aucun run de
# l'etage 1 ni de l'etage 2 n'est joue ; ce qui a tourne ici est declare en 3
# et en 4.

## 0. EN QUATRE PHRASES

La sonde existe, avec sa feuille de lecture et son banc qui tue : trois
scripts, a certifier dans le meme tour que le gel v2. Joues sur machine 1 :
selftest 13 sur 13, pre-vol a geometrie reduite de bout en bout, banc qui
tue 6 mordues sur 6. Une fumee a taille reelle, a UN point : la forme native
est celle du moteur element par element, et l'ancrage rend G_run a 2.2e-04
pres. **Une faute de plume, D-QEB-1 : cette fumee m'a montre des valeurs de
l'etage 2** (section 4).

## 1. LES TROIS SCRIPTS

  sonde_qualification_EB_machine1_v1.py     MESURE, ne juge pas. Charge le
      moteur en lecture seule (chemin en argument, canon verifie). S'arrete
      sur ses gardes d'integrite : G-Q1, G-Q2, G-Q3, G-Q4, G-Q6, G-Q10.
      Releve G-Q5 sans le juger.
  lecture_qualification_EB_machine1_v1.py   JUGE, ne mesure pas. Plateau en
      rationnels exacts (3.11), accords (3.12, 5.1), statuts (6), cascade
      (9), T-etats (7), annonces (11), selftest G-Q7 rejoue a chaque appel.
  banc_qui_tue_qualification_EB_machine1_v1.py   les six mutations du gel
      (10), plus un temoin de porte.

## 2. COMMENT JOUER (tous chemins en arguments)

  sonde   --moteur M --run D --manifeste F --sortie S --etage 1 --retenus R
  lecture --etage 1 --sortie S --reference T      -> S/verdict_etage1.json
  sonde   --moteur M --run D --manifeste F --sortie S --etage 2
          --verdict1 S/verdict_etage1.json
  lecture --etage 2 --sortie S       -> S/verdict_qualification_EB.json
  lecture --selftest
  banc    --lecture .. --sonde .. --moteur .. --run .. --manifeste ..
          --prevol <sortie d'un pre-vol propre> --retenus .. --sortie ..
Pre-vol : ajouter --prevol a la sonde (r0 = 14, L = 6 et 9, translation 3 ;
NON OPPOSABLE). R est ta liste des couplages retenus, T ta table. La feuille
lit de T : "retenus" [{"j", "g"}] et "balayage" [{"j", "g", "Gamma_ref",
"u_ref"}] ; les autres cles sont libres. Elle REJOUE la regle de selection
du gel sur ta table et la compare a ta liste : c'est un controle qui peut
mordre sur ta selection.
L'etage 2 refuse de partir sans un verdict d'etage 1 qui TIENT et qui porte
le canon du sonde_etage1.json present. Reprise par fichier (point,
configuration, k), JSON et vecteurs suivis, sous S/reprise/ : ne se depose
pas.

## 3. CE QUI A TOURNE SUR MACHINE 1

Plateforme : Linux x86_64, python 3.13.18, numpy 2.5.3 (le conteneur a
change depuis septembre), levier NPY_DISABLE_CPU_FEATURES = X86_V4, temoin
d'arrondi 0x1.a483018a169c6p+64 (CR).
  SELFTEST G-Q7        13 tenus sur 13 (les huit du gel, deux de lisibilite,
                       deux de l'accord au TP a sa borne, un de selection).
  PRE-VOL, ETAGE 1     G-Q3 six sur six ; comptes TP 30, TN 15, plancher 30,
                       tous joues. Lecture : NE TIENT PAS (G-Q5 et TP) --
                       attendu a cette geometrie, ou l'absorbeur est dans la
                       barriere ; sans portee.
  PORTE                sur ce verdict, la sonde refuse l'etage 2 (code 2).
  PRE-VOL, ETAGE 2     joue sous un verdict FACTICE, declare et refuse hors
                       --prevol. Comptes : F1 174 joues + 6 repris == 180 ;
                       formes 180 ; translation 90 ; ouverture 6. Zero
                       etat-pas perdu sur 1260 ; identites a 1.0000 ;
                       |somme des c - 1| de 2.5e-14 a 6.9e-14 aux six points.
                       Lecture : NON QUALIFIE, sans portee.
  BANC QUI TUE         6 mordues == 6 attendues ; base synthetique saine ;
                       temoin de porte tenu.
  FUMEE A TAILLE REELLE, point 1.95, (F1, G20), k = 3, UNE decomposition :
                       construction de H 0.6 s ; G-Q3 : identite vraie ;
                       decomposition 78.3 s (2 coeurs) ;
                       gamma = 2.1618431062e-10 contre G_run
                       2.1623273018e-10, rapport - 1 = -2.239e-04 : sous
                       1e-3, pas au bit (attendu : autre numpy, autre
                       systeme) ; recouvrement 0.028803 et poids total
                       0.8671, ceux du run ; |somme des c - 1| = 2.36e-13.

## 4. FAUTE DE PLUME D-QEB-1 -- J'AI VU DES VALEURS DE L'ETAGE 2

La fumee devait lire la seule valeur d'ancrage, deja connue (G_run). Mon
script a aussi imprime les largeurs des DIX etats de plus grand recouvrement
a ce point et a ce k -- la matiere de T-etats (gel 7), avant certification
et avant tout etage 1. Vu : dix largeurs de 2.16e-13 a 1.54e-06, et un
conditionnement kappa de 1.000 aux dix. Cela touche le sujet de mes annonces
A-4 et A-5. Ce qui tient : le gel v2 (cde0cd11a763f26d) et ses annonces
etaient figes AVANT ; je m'interdis toute retouche de la section 7, de A-4
et de A-5 ; le log de la fumee est joint tel quel. Ce qui ne se rattrape
pas : je ne suis plus aveugle sur la dispersion d'etat a 1.95. A toi de dire
si cela demande autre chose qu'une ligne a l'acte.

## 5. PRECISIONS DE DESCRIPTION, A TA LECTURE

  (i)   "Le log porte son empreinte relue du disque" (gel 12) : un log ne
        peut pas porter la sienne ; les miens portent celle du script et
        celle de la sortie JSON, relues du disque en fin d'execution. Dis si
        tu lis la clause autrement.
  (ii)  La ligne de compte "ouverture 6" n'est pas une famille du gel : ce
        sont les six decompositions (F1, G20, k = 3) au moment ou elles
        sont jouees ; la famille F1 les retrouve en reprise. Aucune
        decomposition n'est jouee deux fois.
  (iii) M-6 : le vecteur de remplacement est generique, pas strictement
        orthogonal ; son recouvrement est MESURE sous 0.90 par la sonde
        reelle sur le moteur reel (geometrie reduite), puis la consequence
        est lue par la feuille sur une sortie synthetique.
  (iv)  M-1, M-2, M-3 sont des mutations de DONNEES sur une sortie
        synthetique jugee par la feuille reelle ; M-4 et M-5 lancent la
        sonde reelle en pre-vol avec --mutation.
  (v)   Hors gel, ajoute par la plume : le temoin de porte ; le controle de
        ta selection ; deux tests de lisibilite au selftest.

## 6. CE QUE CETTE PIECE NE DIT PAS

Le gel v2 n'est pas certifie. La reference du TP est a ta plume. Aucun run
n'est joue : ni etage 1, ni etage 2. Le cout sur BOCAL4 reste une
estimation ; la seule mesure est 78 s par decomposition a N = 60 sur ce
conteneur a 2 coeurs. Le garde-fou de la section 12 est sous le veto de
l'operateur. Cette piece ne prend aucun numero (E18).

## 7. PIECES (convention B, manifeste du lot)

    cette note
    qualification_EB_pre_enregistrement_v2.md            cde0cd11a763f26d
    les trois scripts
    prevol/   entrees factices, logs et sorties du pre-vol, log du banc
    fumee/    script et log de la fumee a taille reelle
    lot_6bea6ffe7db2b272/   ma reponse a ta certification du gel v1, lot
                            entier, arbre preserve

-- FIN POUR_MACHINE2_sonde_EB_v1_machine1_v1 --
