DELTA nn -- COMPLEMENT AUX DEPOTS 99 ET 100 : SEPT LOTS QUI MANQUAIENT AU REGISTRE
(plume machine 2 ; releve de machine 1 et releve independant de machine 2 ; non contresigne : machine 1 le lit)
=======================================================================

nn.0 POSITION
  Ce delta ne rend aucun run et ne juge rien. Il complete deux depots deja faits. Le delta 99 (l'acte du gel ter, tete 91dd503) et le delta 100 (l'acte du run du gel loi de la largeur, ordre 3, version 2 avec la
  version 1 a cote, tete 54da87a) ont ete deposes le 16/11/2026 sur l'ordre de l'operateur ("Tu peux deposer !"). Machine 1 les a releves sur un clone neuf : quatorze controles, onze tiennent, trois mordent (lot
  de machine 1 860c0ca980977935). Machine 2 a refait le constat sans lire le script de machine 1 (lot c65d193217e44101) : memes comptes. Sept lots que ces deux depots auraient du contenir ne sont pas au registre. L'operateur a repondu "Ok pour moi" a la proposition d'un
  delta de complement. Registre a l'ecriture : origin/main 54da87a, plafond 100. Aucun numero n'est tape ici : il se derive du registre au depot (E18).

nn.1 LES SEPT LOTS (pieces de table : total, deja au registre par canon, absentes)
    26b3912297b31713  machine 1  acte du gel ter, version 1 (delta 99)                                        30    8   22
    d9250297bf7d2f77  machine 1  acte du run de la loi, version 1 (delta 100)                                 23    5   18
    0a5741ff95e7136c  machine 1  acte du run de la loi, version 2 (delta 100)                                 10    1    9
    e93f1898dcd78a8f  machine 1  note sur la loi de la largeur (origine du bloc d'ordre 3)                    21    2   19
    1e8413aed149429f  machine 1  note de la carte (origine de l'eligibilite des cellules)                     16    1   15
    889fe9b4c1c1c60a  machine 2  mon bloc d'ordre 3 rederive                                                  11    1   10
    548fb2ba8793ecfe  machine 2  ma reponse a la carte (regle de tirage, quatre conditions)                    8    0    8
  Soit 101 pieces absentes, et les sept manifestes. Aucun des sept manifestes n'est au registre. Les trois premiers lots sont les lots d'acte de machine 1 ; les quatre autres sont cites par les gels de la loi deposes
  (543d8b33e5c9afb8 cite 26b3912297b31713, 548fb2ba8793ecfe, 889fe9b4c1c1c60a et e93f1898dcd78a8f ; b56ca5cb2dd25da1 cite 1e8413aed149429f, 548fb2ba8793ecfe, 889fe9b4c1c1c60a et e93f1898dcd78a8f).

nn.2 LA CAUSE, DE MACHINE 2
  La feuille de perimetre de machine 2 n'enumere que les lots CITES par l'acte, ou dont l'en-tete de manifeste porte le canon de l'acte. Au delta 98 l'en-tete du lot d'acte de machine 1 le portait ; ici non, et
  les empreintes citees par les actes, resolues par canon, n'obligeaient a deposer aucun de ces lots. Les controles de depot de machine 2 verifiaient les lignes de son manifeste (208 sur 208, puis 275 sur 275), pas que tous les lots
  extraits pour ce depot y etaient entres. Son enveloppe ecrivait a machine 1 "tes lots et les miens" : c'etait inexact pour les trois lots d'acte. Le controle qui manquait est ecrit (controle_lots_entrants_machine2_v1.py,
  dans le lot c65d193217e44101) : rejoue sur les deux depots, il mord a 1 lot au delta 99 et a 2 lots au delta 100.

nn.3 CE QUE CE DELTA DEPOSE, ET CE QU'IL NE DEPOSE PAS
  Il depose : les sept lots ci-dessus avec leurs manifestes et leurs pieces de table ; le lot de releve de machine 1 (860c0ca980977935) ; le lot de reponse de machine 2 (c65d193217e44101) ; cette note, numerotee.
  Il ne depose pas : les ZIP des lots, ni les enveloppes (qui ne sont pas des lots). Il ne retire, ne modifie ni ne renomme rien : le commit n'ajoute que des fichiers sous gels/, scripts/ et journal/.
  Une piece qui porte le meme nom qu'une piece du registre sous d'autres octets (des journaux de rejeu, par exemple) entre sous le prefixe de son lot, comme dans les deltas precedents ; le compte est dans le journal du perimetre.

nn.4 CE QUE CE DELTA NE FAIT PAS
  Il ne touche aucun nombre d'aucun acte (ter, run v1, run v2), aucun verdict, aucun gel. Il n'adopte aucune regle : trente-quatre restent sous la revue (X). Il ne resout pas une dette anterieure, qu'il dit : la note hors chaine
  "d'anteriorite" que citent les gels des deltas 97 et 98 (empreinte 119f4e...) ne repond a rien au registre et machine 2 ne la detient pas (treize mille cent soixante-douze fichiers du poste indexes par canon B et brut, aucun ne la porte) ;
  la piece 1f6cfb... citee par le gel de la loi, partie 1, est une piece du lot 1e8413aed149429f et entre avec lui. Deux empreintes que le releve de machine 1 compte comme non resolues ne sont pas des fichiers : 4b2a1d... est le debut
  d'un sha256 donne en exemple dans ce gel, et 794344... un morceau d'un nombre ecrit 2.79434...e-09 dans le gel du delta 98.

nn.5 LES LOTS CITES (canons)
  Les sept lots du nn.1 ; 860c0ca980977935 (releve de machine 1, 8 pieces) ; c65d193217e44101 (reponse de machine 2, 10 pieces). Les trois actes auxquels ces lots se rattachent sont deja au registre : 751165a3eee613d9 (delta 99),
  a3f7d5d6809dcfe5 et b205b14cdfc23ba3 (delta 100, versions 1 et 2).

-- FIN journal_delta_nn_complement_lots_deposes_99_100_v1 --
