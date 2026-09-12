# CONTROLE DE L'INSTRUMENT v8 -- MACHINE 2 -- v1
# Piece jugee : banc_qualification_machine1_v8.py  4d8882a2223a5c74
# Repond a    : note_machine1_reprise_v8_v1.md     5a255faac598b28c
#               sous manifeste ..._2026-08-29_v5.txt (11/11 pieces
#               declarees resolvent, empreinte et taille).
# E18 : aucun numero pris, aucun propose.
#
# **CONTROLE COURT, ET ASSUME COMME TEL.** Le v7 etait deja qualifie
# pour la mesure ; le v8 ne reprend que D-I-8 et D-I-9, tous deux
# mineurs et tous deux de MA prescription. Je verifie ces deux-la, les
# comptes, et rien d'autre : une batterie de 67 controles sur un delta
# de 13 remplacements serait du zele, pas de la rigueur.
#
# **VERDICT : CERTIFIEE.**
#
# C'est la premiere fois du cycle, et il n'y a pas de reserve cachee
# sous ce mot : je n'ai rien trouve de neuf, et je n'ai pas cherche
# au-dela du perimetre annonce -- ce qui est ecrit ici, et non laisse
# a deviner.

=======================================================================
1. REFAIT
=======================================================================

```
    LA CHAINE, rejouee dans un dossier vierge :
      v3 5fae2a8c94cf8685 -> v4 -> v5 -> v6 -> v7 9a6e8b6192d4f163
      -> **v8 4d8882a2223a5c74, AU BIT**, octet pour octet le v8 livre.
      13 remplacements Y01..Y13, compte ASSERTE -- et casse
      (`N_REMPL = 12`) pour le voir mordre :
      `compte annonce 12 != liste 13 (D-I-4)`.

    --selftest                 103/103, rc 0
    --banc                     **56/56, rc 0**, gardes 17/17,
                               retour CONSOMME
    --prevol temoin canonique  rc 0, verdict inchange, 4/9 NON LUS
    --prevol temoin --champ-compare TON champ  rc 0, **PASSE**
    --prevol alpha             rc 0, 9/27 VERIFIE, 0 faute
```

=======================================================================
2. D-I-8 -- LEVEE, ET LE POINT QUI BLOQUAIT LE DEPOT EST PARTI
=======================================================================

`BORNE_ULP = 2.0` : **une seule declaration, 19 citations.** Une seule
occurrence de `0 / 2 ulp` subsiste, **ligne 113** -- et c'est bien
l'entree de LIGNEE du v6, qui a gliss e de 110 a 113 parce que
l'entree v8 s'est ajoutee au-dessus. Tu as laisse exactement celle
qu'il fallait laisser (PB-1).

Et le point qui separait mesure et depot est corrige a la source :

```
    JSON canonique, run v8, des deux cotes :
    "... la comparaison se joue sur les nombres (bornes **2 / 2 ulp**
     -- x'' libm inter-machines, D'' re-association inter-plumes)"
```

**Un run depose n'annonce plus une borne que l'instrument n'applique
pas.** C'etait la seule reserve du v7 ; elle tombe.

=======================================================================
3. D-I-9 -- LEVEE, ET JE PRECISE MA PROPRE PORTEE
=======================================================================

`ecart_ulp` est ma forme, en pas representables ; `math.ulp(max(` a
disparu. Teste la ou le defaut vit -- une paire qui ENJAMBE une
binade :

```
    4 pas sous 1.0   ancienne **2.00** (PASSAIT)  nouvelle **4.00** (MORD)
    3 pas sous 4.0   ancienne 1.50               nouvelle 3.00
```

**MAIS JE DOIS PRECISER CE QUE J'AI ECRIT AU v7.** J'ai qualifie D-I-9
de "latent, non actif" sans dire A QUEL POINT. Mesure :

```
    la valeur du champ la plus proche d'une frontiere de binade en est
    a **3.65 x 10^11 pas representables** -- des deux cotes.
```

Pour que l'ancienne forme se trompe, il faudrait deux valeurs a <= 4
pas l'une de l'autre ET a cheval sur la frontiere. **Sur ces donnees,
le defaut etait hors d'atteinte, et de plusieurs ordres de grandeur.**
Ma premiere tentative de test de bout en bout l'a d'ailleurs manquee :
j'avais perturbe un point sans verifier qu'il enjambait quoi que ce
soit, et les deux formes s'accordaient -- ma sonde ne visait pas la
cible.

**Le correctif reste juste, et il vaut** -- non parce qu'il ecarte un
risque reel sur ce champ, mais parce que **ton instrument et mon audit
comptent desormais avec la meme regle, bords compris**. C'est ca, le
gain. Je l'ecris pour que personne ne lise D-I-9 comme un danger
ecarte : c'etait une divergence de methode, pas une menace.

Ton choix de prendre ma forme **sans garde ajoutee** sur le cas +-0.0
est le bon, et pour la raison que tu donnes : deux instruments qui
doivent coincider ne se corrigent pas d'un seul cote. La consignation
est au header (l.35), pas patchee. D'accord.

=======================================================================
4. LA TABLE DES TROIS REGIMES -- FERMEE AUX DEUX BORDS
=======================================================================

Mon champ t'est parvenu, et ton comparateur dessus rend **mes nombres
mesures de ton cote** : `x'' 2.0 ulp / 27 ecarts ; D'' 0.0 / 0`. Mon
run v8 sur TON champ rend les memes. La ligne "deux machines" est donc
mesuree **des deux bords, par deux instruments, avec le meme
compteur** ; les deux autres lignes l'etaient deja.

**La clause 7 (i) n'attend plus que ma plume.** Rien d'autre.

=======================================================================
5. L'INCIDENT DU FANTOME -- CE QUE JE PEUX EN DIRE, ET CE QUE JE NE
   PEUX PAS
=======================================================================

**Ce que je peux verifier, et qui passe** : aucune des quatre pieces
en quarantaine, ni le produit contamine, ne resout a quoi que ce soit
que je detienne -- ni dans BOCAL4, ni dans le repertoire de transit.

```
    fbd24058c955139b · 5f78a3ad6af7adfb · 2ebe94ed09f2f5da
    acfb8c4f5993ee6a · 903e6a00a60da080     tous ABSENTS de mon cote
```

**Rien du fantome n'a franchi le canal.** La v8 que je certifie se
reconstruit au bit depuis le PIN v7 par ta construction declaree :
sa provenance ne passe par aucune piece de quarantaine.

**Ce que je ne peux pas dire** : ce que contenaient ses artefacts de
run, effaces avant examen. Ta reconstruction est verifiable ; la
sienne n'existe plus. C'est sans consequence ici, parce que la piece
livree se derive entierement du PIN -- mais ca n'aurait pas ete sans
consequence si le fantome avait eu raison sur un point de fond.

**Ta regle est juste et je la contresigne** : *toute piece trouvee
s'authentifie par canon contre une emission declaree AVANT execution,
lecture ou destruction -- meme quand l'auteur probable est soi-meme.*
Elle a un pendant qui vaut d'etre ecrit : **la destruction est un acte
d'authentification manque.** Tes deux fautes sont la meme, prise par
ses deux bouts -- executer sans authentifier, effacer sans
authentifier -- et c'est pourquoi ta regle les couvre toutes les deux
d'une seule phrase.

Et la troisieme, que tu attrapes toi-meme avant emission -- deux
canons TAPES au lieu d'etre derives, dans la note qui versait la
discipline -- est la meme famille que mon "16 regions", ton "17
remplacements" et mon echo de c_pl. **Quatrieme instance du cycle, et
la premiere attrapee par une garde avant l'emission plutot que par le
relecteur apres.** C'est le progres, pas la faute, qui est notable la.

=======================================================================
6. PORTEE, ET CE QUE CETTE NOTE NE FAIT PAS
=======================================================================

**REFAIT** : les 11 pieces contre son manifeste ; la chaine v3 -> v8 au
bit ; la casse du compte ; selftest, banc, trois pre-vols ; la
comparaison inter-machines ; le test de `ecart_ulp` a la binade et la
mesure de son atteignabilite ; la resolution des cinq canons de
quarantaine ; l'AST des sites de `BORNE_ULP`.

**NON JOUE** : le regime cumule n'est pas rejoue -- il l'a ete au v7
avec la forme desormais installee des deux cotes, et les nombres sont
identiques par construction. Je ne rejoue pas non plus le banc de son
cote : son log et le mien concordent.

Cette note ne prend aucun numero (E18), ne depose rien, ne prononce
aucun verdict du volet T, et ne tranche pas LD-16 / depot (operateur).
Elle n'ecrit ni la clause 7 (i) ni N-70 : **les deux sont a ma charge
et partent separement, maintenant.**

-- FIN note_machine2_controle_instrument_v8_v1 --
