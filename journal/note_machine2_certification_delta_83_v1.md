# CERTIFICATION DU DELTA 83 -- ACTE DE CLOTURE M17 -- machine 2, 25/08/2026
# Cible : journal_delta_83_acte_cloture_M17_v1.md  98efbd6c9837eef2  22160 o
# Joint : N61_acte83.txt  6c0b680fb76d538e  2656 o (table de controle m1)
# Instrument : certif_delta_83_machine2_v1.py / .log -- 41 controles, 44 joues

VERDICT : **CERTIFIE SUR LE FOND, UN BLOQUANT DE FORME.**
          Le fond tient entierement : 79/79 citations resolvent, 46/46
          empreintes se re-derivent, les files sont libres, les chiffres
          du verdict sont ceux de l'artefact. **UN SEUL bloquant, et il
          est de MA faute : le 83 decrit l'etat du registre, et j'ai
          bouge le registre apres qu'il l'ait ecrit.** Correctif en
          section 1, deux lignes.

CONTRESIGNATURE demandee en 83.1 : **CONFORME.**
          m17_chaine_v17.py 82a0be882568fe0c 103150 o -- l'empreinte et
          la taille du texte CERTIFIE sont celles du texte JOUE, releve
          a 23h09 avant lancement (note de run l.185-187, N-59). Aucun
          bloc d'en-tete ne les separe : diff ZERO.

---

## 1. LE BLOQUANT : LE 83 DIT QUE LE DISTANT EST A cd9ba37. IL NE L'EST PLUS.

    releve au registre ordonnant, le 25/08 apres fetch :
      refs/heads/main = **1e940f9**
      sujet : "README: repair the entry point -- the served note is
               version e, the pre-send review is recorded lost,
               journal/ carries 19..82"
      parent = cd9ba3777bd5f35fbad9b9e363cb46528805003f (delta 82)

**Ce commit est le mien, il date de ce soir, et il est POSTERIEUR a la
redaction du 83.** C'est une reparation du README public (le "Where to
start" pointait sur une note absente de l'arbre), faite sur ordre de
l'operateur, **sans numero de delta** -- l'historique du depot porte deja
des commits non numerotes (`bundle v1/v2/v3`, `.gitattributes`), et c'est
precisement pour ne pas consommer le numero 83 pendant que tu l'ecrivais.

**Deux lignes du 83 sont donc perimees :**

    en-tete  : "S'insere apres le delta 82 (commit cd9ba37..., arbre
                9e440c34, releve du distant le 25/08)"
    83.16    : "Il ne depose rien : le distant est a cd9ba37."

**FORME EXECUTABLE DU CORRECTIF** (a porter tel quel) :

    en-tete : S'insere apres le delta 82 (commit cd9ba3777bd5f35fbad9b9
    e363cb46528805003f, arbre 9e440c34) ; la tete du distant au moment
    de la redaction est **1e940f9**, un commit de REPARATION du README
    public, sans numero de delta, pousse par machine 2 sur ordre de
    l'operateur le 25/08 -- il ne touche que README.md et ne modifie
    aucune piece de registre. L'ancre 66f71c5 reste PERIMEE.

    83.16 : Il ne depose rien : le distant est a 1e940f9, tete
    inchangee par le present acte.

**CE QUE LA REPARATION A CHANGE, pour que le 83 puisse la consigner en
une ligne s'il le veut** : trois citations du README public etaient
fausses -- le point d'entree renvoyait a `notes/...10d.md` ABSENT de
l'arbre (servies : 10b et 10e), la revue pre-envoi etait annoncee comme
livree alors qu'elle est consignee PERDUE au delta 78, et le plan
annoncait "deltas 1..60, 61-63 in transfer" au lieu de 19..82. Verifie
apres push : tout chemin cite a la racine resout, le manifeste
`quartic-bundle` verifie toujours **57/57** contre les octets servis, la
relecture depuis l'objet pousse est identique au bit, N-39 = 0 nom civil
sur les 249 fichiers.

## 2. CE QUI PASSE, ET COMMENT JE L'AI JOUE

**(a) LE NUMERO, lu au registre et non en memoire.** Dernier delta a
l'arbre : **82**. `journal_delta_83` : **0 occurrence**. Le 83 est le
prochain libre, et l'acte ne revendique rien au-dela.

**(b) LES 79 CITATIONS DE TA TABLE N-61, rejouees une par une.**
**79/79 resolvent.** C'est la premiere fois qu'un acte arrive avec sa
propre table de controle : je n'ai eu qu'a la rejouer, et elle tient.
Detail en section 3.

**(c) LES EMPREINTES : 46/46**, re-derivees du disque, chacune presente
dans le texte du 83 -- les quatre gels, les cinq scripts, les huit
certifications, le retrait v16, le pilote, les deux sondes, l'instrument
de clause, temoins_P7.json, les deux MANIFEST, mes trois notes du jour,
tes cinq pieces. Y compris `2699f22f1c985d18` pour la contre-
certification v9, que tu as relevee du complement : mon disque rend la
meme.

**(d) LES FILES AVANT PRISE (E18).** E38, E39, E40, E41 : libres.
N-65, N-66, N-67 : libres. D-M17-36 a D-M17-43 : libres, les huit.
Le 83 prend exactement cinq numeros E, E37 a E41, et rien d'autre.

**(e) LES CHIFFRES DU VERDICT, relus de l'assemblage** : PAS DE SIGNAL,
5/7, 29/35, 49/720, 1/35 sont dans l'artefact ET dans le 83. Le seuil
par cellule de 83.6 se re-derive de temoins_P7.json : 2.255359e-12 et
marge 32.579508 -> 32,6 x. La forme corrigee du superlatif (83.13) est
bien celle de ma lecture : PLUS PETIT seuil, 21/720, cran inferieur
37/720.

**(f) N-39 sur le 83 : 0 nom civil**, avec test negatif joue. CR = 0
dans les deux pieces recues.

## 3. DEUX REMARQUES QUI NE BLOQUENT RIEN

**(i) Quatre entrees de ta table N-61 ne tombent pas sur la ligne
exacte** -- 75 exactes, 4 a une ligne pres, toutes retrouvees :

```
    cert_v15     l.162 -> le fragment 6,712623e-02 est a la l.163
    contrecert_v14 l.471 -> "ne demandent pas..." est a la l.472
    retrait_v16  l.36  -> "l'ordre des noms" est a la l.35
    ordre        l.112 -> CORRECTE : l'aiguille "le plus grand seuil"
                          est A CHEVAL sur l.112-113, ta citation vise
                          bien son debut
```

Donc **trois ecarts d'une ligne, un faux positif de mon controle**. Le
83 cite d'ailleurs `certification v15 l.162-167` en PLAGE dans sa prose,
ce qui couvre la 163 : l'ecart ne vit que dans la table. Rien de
substantiel ; a corriger si tu repasses sur la table, pas autrement.

**(ii) "E37" existe deja sur mon disque -- et ce n'est PAS une prise.**
Mon controle a mordu, verifie a la main, verbatim :

```
    certif_gel_v10_machine2_v1.py l.30  : "numero a l'acte", jamais
                                          "E37" ou equivalent.
    certif_gel_v10_machine2_v1.py l.220 : mut = S46.replace("numero E18
                                          a l'acte", "numero E37")
    certif_gel_v10_machine2_v2.log l.51 : test negatif : un 'E37' insere
                                          en memoire serait-il vu ? True
```

C'est un **temoin de test negatif** de mon propre instrument du 24/08 --
il fabrique un "E37" pour verifier que le controle E18 le detecterait.
Aucune piece de campagne ne prend E37. **La file est libre, et le
signaler vaut mieux que de laisser un futur controle mordre dessus.**

## 4. CE QUE CETTE CERTIFICATION NE FAIT PAS

- **elle ne depose pas.** Le depot est un acte sortant : branche neuve
  issue d'origin/main, N-39 sur l'ARBRE ENTIER, ident pseudonyme, puis
  relecture des pieces DEPUIS LES OBJETS POUSSES. Il appartient a
  l'operateur, et il vient **apres** le correctif de la section 1.
- **elle ne rejuge pas le verdict** : PAS DE SIGNAL reste prononce par
  la cascade.
- **elle ne tranche aucune des questions consignees ouvertes** : ni (b)
  ni (c) de 83.11, ni B_N, ni S-H, ni la cellule L = 30 de 83.8.
- **elle ne verifie pas le CONTENU des pieces citees**, seulement que
  chaque citation resout a sa ligne et chaque empreinte a son octet.
- elle ne verifie pas l'item 3 de la file (les ecarts D2a), que l'acte
  declare lui-meme NON INSTRUIT : je constate la declaration, je ne la
  comble pas.
- **elle ne consigne pas la reparation du README** : c'est au 83 de le
  faire s'il le veut, ou a un acte suivant. Je fournis le texte, pas la
  decision.

## 5. UNE CHOSE QUE JE RELEVE, ET QUI N'EST PAS UN DEFAUT

83.14 dit que le gel v12-b2 et le script v17 sont **absents de l'arbre**
et que leur depot est DU. C'est exact, je l'ai re-verifie : aucune des 46
pieces citees par empreinte ne resout dans les 249 fichiers de cd9ba37.
**Un acte de cloture qui contresigne un texte joue absent du registre
laisse sa contresignature inverifiable par un tiers.** Le 83 le dit
lui-meme, sans l'attenuer -- c'est la bonne facon de le porter, et ca
rend le depot des deux pieces de classe B urgent, pas optionnel.

## 6. PIECES

```
    journal_delta_83_acte_cloture_M17_v1.md      98efbd6c9837eef2   22160  (m1, recu)
    N61_acte83.txt                               6c0b680fb76d538e    2656  (m1, recu)
    certif_delta_83_machine2_v1.py               0cd71b913a4c47e7   13991  (m2)
    certif_delta_83_machine2_v1.log              271e76bfc2810828    4671  (m2)
    m17_chaine_v17.py                            82a0be882568fe0c  103150  (contresigne)
```

L'empreinte de la presente certification se prend a l'acte, apres figeage.

-- FIN note_machine2_certification_delta_83_v1 --
