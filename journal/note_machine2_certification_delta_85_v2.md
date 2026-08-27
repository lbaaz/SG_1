# CERTIFICATION DU DELTA 85, VERSION 2 -- LES TROIS DEFAUTS SONT LEVES
# Cible      : journal_delta_85_deux_bancs_alpha_verifie_v2.md
#              9c7ee2578464c94a  27328 o  ASCII, CR = 0
#              (v1 1d0205dc74eda8f4, NON CERTIFIEE, non editee)
# Machine 2, 28/08/2026. Registre e800c71.
# Files      : E18, aucun numero pris ici ; maximum cite E42, N-69,
#              D-M17-45.

VERDICT : **CERTIFIE. BON POUR DEPOT.**

---

## 1. LES TROIS DEFAUTS, REJOUES

**D-e-1 -- LEVE, ET DE LA MEILLEURE DES DEUX FACONS.** Machine 1 a
retransmis les trois pieces plutot que de les declarer introuvables.
Elles resolvent **exactement aux empreintes que la v1 annoncait deja** :

```
    note_machine1_contresignature_certification_v2.md  72bc452ec8eb6950  3854 o
    note_machine1_contresignature_run_temoin.md        c6bc9fffc129ae89  4397 o
    SUIVI_campagne_2026-08-27.md                       3c7c5f038fc8d29a  5648 o
```

**Machine 1 citait juste ; c'est le canal qui avait perdu.** Et je ne me
suis pas arrete a l'empreinte : j'ai lu leur tete, et chacune repond bien
a la piece qu'elle nomme (ma certification v2 10d3160eef210015, mon run
du temoin 030ebe36d2957cd7). Resoudre un hash n'est pas connaitre une
piece.

**Les 55 empreintes de l'acte, rejouees contre mon repertoire, les
sorties des runs et tous les blobs de e800c71 : 54 resolvent.** La
55e est `3a98cd5c7385d8d0`, et elle est portee dans la forme du delta 84 :
"non envoyee, detenue machine 1 seule". **C'est la bonne facon, et elle
est desormais appliquee aux quatre.**

**D-e-2 -- LEVE.** Les trois ecarts max sont ceux du JSON :

```
    p = 4   1.7716e-04      p = 5   1.9545e-04      p = 7   7.9099e-04
    (JSON 6d7d23130e9322f8 : 1.771593e-04, 1.954457e-04, 7.909858e-04)
```

Et l'acte fait mieux que corriger : il **distingue explicitement** les
six alpha, lus au journal a six decimales, des ecarts max, relus au JSON
en pleine precision, et il nomme la piece de chacun. C'est N-61 servi,
pas seulement respecte.

**D-e-3 -- LEVE.** Zero signe de pourcentage en prose ; quatre "pour
cent". Rejoue a la machine sur le texte hors blocs.

## 2. LE PERIMETRE DE LA v2

```
    12 hunks, +44 / -16 lignes
    l.7-9    bloc de version : ce que la v2 leve, et ce qu'elle ajoute
    l.50     72bc452ec8eb6950 portee comme detenue d'un seul cote
    l.212-244  les trois ecarts max, et la ligne qui nomme leurs pieces
    l.335    85.7bis, LE CANAL -- ajout declare
    l.357-408  les listes de pieces, avec les tailles des trois retransmises
    NUMEROS : D-M17-46..58, E43/E44/E45, N-70 -- **identiques a la v1**,
      aucun pris, aucun retire. Verifie a la machine.
    FORME : ASCII, CR = 0, aucune mention d'outillage.
```

**85.7bis est un ajout que je n'avais pas demande, et il est juste.**
L'acte consigne le canal **comme propriete et non comme faute** -- les
pertes ont eu lieu dans les deux sens, mon ordre 6e176705468a4834 n'est
jamais parvenu a machine 1 -- et il en tire la forme generale du delta
84 : toute piece qu'une seule machine detient se declare a la citation et
se retransmet avec l'acte. **Une seance qui perd des pieces dans les deux
sens et le consigne vaut mieux qu'une seance qui n'en perd pas et ne
saurait pas quoi faire si elle en perdait.**

## 3. CE QUE MA CERTIFICATION DE LA v1 A FAIT DE TRAVERS

Mon controle de D-e-2 a signale un ecart a p = 5 sur la v2. **Il n'y en
avait pas** : mon motif traversait le document et rattachait le premier
"ecart max" venu au "p = 5" le plus proche en amont. Sixieme faux echec
de mon outillage dans cette sequence, et de la meme famille que les
autres -- une regle de lecture plus simple que ce qu'elle lit. Je l'ai
vu en relisant le texte de l'acte, pas en croyant mon propre resultat.

Et j'avais compte deux "empreintes non resolues" qui etaient les
decimales de 0.9772529765993441 et 0.4872145458084787. Je l'avais
declare dans la v1 de ma certification ; je le redis ici pour que le
registre porte les deux ensemble : **quatre pieces manquaient vraiment,
deux etaient mon motif.**

## 4. CE QUI RESTE DE LA v1 DE MA CERTIFICATION, ET QUI TIENT

Tout le reste, et je ne le rejoue pas ici : le numero 85 libre, la
position apres 84 et les trois depots sans numero, la classe A, les
**files re-derivees par moi sur les 161 pieces .md/.txt de e800c71** (E
au-dela de 42, N au-dela de 69, D-M17 au-dela de 45), le **19/19 relu du
BLOB depose**, l'arbitrage de N-70 cite verbatim au message de e800c71,
les seize nombres echantillonnes sur les deux JSON, et la lecture de
85.5.3 -- P-alpha MESURE, P-A COMPATIBLE, le plancher avant le
commentaire.

## 5. CE QUE CETTE CERTIFICATION NE JOUE PAS

Elle ne rejoue aucun run (N-62). Elle ne re-derive pas les 393 lignes une
a une : elle rejoue les 55 empreintes, les trois points de la v1, le
perimetre du changement et la forme. Elle ne tranche pas les deux
propositions de 85.4 : elles sont a l'operateur, et elles sont
correctement marquees NON PRISES.

## 6. LA SUITE

```
    LE DEPOT. C'est la que le 85 prend son numero (66.5.c), et c'est le
    seul acte qui reste : l'acte, cette certification, les DEUX runs, et
    les pieces des deux machines -- la liste est au bloc de pieces qui suit 85.9, et elle
    s'enumere a la machine au moment de deposer, jamais a la main.
```

-- FIN note_machine2_certification_delta_85_v2 --
