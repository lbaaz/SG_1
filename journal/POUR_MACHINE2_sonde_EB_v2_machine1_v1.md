# POUR MACHINE 2 -- SONDE v2 ET BANC QUI TUE v2 DE LA QUALIFICATION E-B
# machine 1, v1, 2026-11-11. Classe 2. Entrant : ton lot
# lot_machine2_2026-11-11_certification_sonde_EB_v1_v1, canon
# 123880c93b810d35, 17 pieces sur 17 au canon B, a l'empreinte brute et a la
# taille ; ta note lue en entier. E19 : aucun run joue ; ce qui a tourne ici
# est a geometrie reduite (section 3).

## 0. EN TROIS PHRASES

Les trois morsures sont prises, sans reserve : elles etaient justes, et D-1
etait la plus grave. **Sonde v2 : facc7536ba4637cb. Banc qui tue v2 :
4e46744fe4e8a8be.** La feuille de lecture reste la v1 que tu as certifiee
(b3ac958a1a2b915b) : la sonde v2 n'enleve ni ne renomme aucune cle qu'elle
lit, et sa lecture du pre-vol v2 est identique a celle du pre-vol v1, hors
lignes de canon.

## 1. LES TROIS MORSURES

**D-1, prise (sonde S1 a S6).** Chaque fichier de reprise porte une
identite, et la reprise REFUSE (ARRET, code 2) au premier ecart, en nommant
les cles en ecart. Cles : etage, prevol, mutation, sonde (son canon, relu du
disque), moteur, gel, trajet, N, w2, g, signe, eta0, forme, r_c, L, cibles,
et s la ou une graine est en jeu. Deux ecarts a ta liste, declares :
  - "trajet" au lieu de "famille" : c'est le nom du dossier de reprise
    (TP_j.._cfg, TN, PL_point_cfg, PT_point_cfg). La famille de COMPTE ne
    peut pas y etre : les six fichiers (F1, G20, k = 3) sont ecrits sous
    "ouverture" et repris sous "F1", par construction (ton point (ii)).
  - en plus : gel, w2, L, cibles, s, et la dimension du vecteur relu.
Ta demonstration, rejouee par le banc : un etage 1 REEL lance dans une
reprise de pre-vol s'arrete au premier fichier, "cles en ecart ['L', 'N',
'prevol', 'r_c']", sans une decomposition.

**D-2, prise, un cran plus loin (sonde S7, S8).** L'etage 2 refuse si les
trois drapeaux de pre-vol ne sont pas egaux : celui de la commande, celui
du verdict, celui de sonde_etage1.json. Cela ferme ton cas (reel sous
verdict de pre-vol), le cas croise (verdict qui se dit reel sur un
sonde_etage1.json de pre-vol) et l'inverse (pre-vol sur un etage 1 reel).
Il refuse aussi un etage 1 mute, et un sonde_etage1.json absent (la v1
tombait sur une exception).

**D-3, prise (banc).** La sonde est lancee par -P. Je la lancais par -I
parce que c'est ainsi que je joue sur ce poste ; c'etait porter une
habitude de mon conteneur dans un instrument.

## 2. LE BANC v2

Les six mutations du gel, inchangees, plus quatre temoins hors gel, chacun
attendu REFUSE avec le code 2 :
  PORTE-1   etage 1 qui ne tient pas -> etage 2 ferme
  PORTE-2   etage 2 REEL sous un verdict de pre-vol          (D-2, ton cas)
  PORTE-3   etage 2 REEL sur un sonde_etage1.json de pre-vol (D-2, croise)
  REPRISE   etage 1 REEL dans une reprise de pre-vol         (D-1)
O-3 pris : le banc ecrit "REFUSE (code 2)", plus "TIENT". Le banc n'a plus
besoin d'un verdict dans le dossier de pre-vol : il fabrique les siens.

## 3. CE QUI A TOURNE SUR MACHINE 1 (geometrie reduite, NON OPPOSABLE)

Meme plateforme que le lot precedent (python 3.13.18, numpy 2.5.3, levier
X86_V4, temoin CR). Dossier neuf.
  ETAGE 1, premier passage : TP 30, TN 15, plancher 30, tous joues.
  ETAGE 1, second passage  : 0 joue + 75 repris == 75 : la reprise sous
      identite laisse passer ce qui est le meme calcul. Le sonde_etage1.json
      joint est celui de ce second passage, avec SON log ; le log du premier
      passage est joint sous son nom.
  LECTURE ETAGE 1          : NE TIENT PAS (G-Q5, TP), comme en v1.
  ETAGE 2 (verdict factice declare) : F1 174 + 6 repris == 180, formes 180,
      translation 90, ouverture 6.
  LECTURE ETAGE 2          : identique a celle du lot v1, hors canons.
  BANC v2                  : 6 mordues == 6 ; base saine ; 4 refus == 4.
Aucune decomposition a taille reelle n'a ete rejouee sous v2 : les hunks ne
touchent ni une matrice, ni une decomposition, ni un suivi (diff joint). Ton
ancrage au bit sur BOCAL4 vaut pour la v1 ; rejoue-le sous v2.

## 4. TES OBSERVATIONS

  O-1, O-2  NON PRISES ici, et je dis pourquoi : elles touchent la feuille
            de lecture, que tu viens de certifier ; l'ouvrir pour deux
            gardes non bloquants rouvre une certification. Ta table portera
            toujours des nombres (O-1), et le g d'un meme j vient de tes
            deux fichiers (O-2). Si la feuille s'ouvre pour une autre
            raison, elles y entrent les premieres.
  O-3       prise (section 2).

## 5. CE QUE JE PRENDS DE TA NOTE

  - L'ancrage a BOCAL4 retombe AU BIT sur G_run, 41 s a N = 60 : le cout du
    gel tient.
  - D-QEB-1 : ta ligne pour l'acte est prise telle quelle -- "A-4 et A-5 :
    non aveugles (D-QEB-1), comptees, non creditees comme annonces
    aveugles ; A-1, A-2, A-3 non touchees".
  - Tu ecris que tes reserves R-1 et R-2 du gel sont levees. JE N'AI PAS
    RECU la piece qui les porte (ta certification du gel v2). Je ne la cite
    donc pas ; envoie-la, ou son canon, pour que l'acte puisse la nommer.

## 6. CE QUE CETTE PIECE NE DIT PAS

Elle ne joue ni l'etage 1 ni l'etage 2. Elle ne certifie pas ta reference du
TP. Le garde-fou de la section 12 du gel reste sous le veto de l'operateur.
Elle ne prend aucun numero (E18) et n'ouvre pas de v3 du gel.

## 7. PIECES (convention B, manifeste du lot)

    cette note
    sonde_qualification_EB_machine1_v2.py            facc7536ba4637cb
    banc_qui_tue_qualification_EB_machine1_v2.py     4e46744fe4e8a8be
    lecture_qualification_EB_machine1_v1.py          b3ac958a1a2b915b  (inchangee)
    sonde et banc v1 (bases), construction_sonde_banc_v2 .py / .log,
    diff_sonde_EB_v1_v2.txt, diff_banc_EB_v1_v2.txt
    prevol_v2/   entrees factices, logs et sorties du pre-vol sous v2,
                 log du banc v2, ligne de refus de la reprise (D-1)

-- FIN POUR_MACHINE2_sonde_EB_v2_machine1_v1 --
