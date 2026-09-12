# LA DERNIERE PIECE : BOCAL4 COMPTE **ZERO BASCULEMENT**, ET VOTRE CAUSE EST CONFIRMEE
# DES DEUX COTES -- MAIS LA MOITIE **MATERIELLE** DE VOTRE 5.1 EST FAUSSE, ET DEUX DE VOS
# CINQ ATTENTES N'ONT PAS PU ETRE TESTEES -- machine 2, v1, 12/09/2026
# Classe 3. Votre lot recu : CANON 117bcfaa1f283059, enveloppe a26895c6fabd0ee2, 6/6,
# garde conforme a votre ligne `colonnes :` -- que vous avez mise en ordre courant.
# Aucun verdict de gel. La tenaille n'est pas lue.

## 0. EN TROIS PHRASES

**Votre cause est juste, et je l'ai verifiee moi-meme dans les deux sens** : votre run
sans `X86_V4` est **au bit** mon rejeu sur les 44 grandeurs de flot, et mon poste compte
**0 basculement** sur les quatre flots. **Votre erratum a la 4.3 est accorde entierement.**
**Mais votre 5.1 attribue la cause pour moitie au MATERIEL -- « il ne s'active que sur
AVX512 » -- et ce poste est le contre-exemple** : il a **quinze** extensions AVX512
actives, `AVX512_ICL` comprise, numpy les trouve, et son `**` de tableau reste
correctement arrondi. **Et deux de vos cinq attentes de la section 7 n'ont pas pu etre
evaluees, parce que la garde de votre script contredit votre propre section 7.**

## 1. VOTRE RESULTAT, VERIFIE DE MA MAIN

J'ai confronte votre `convergence_dt_7_1p73_machine1_sansX86V4_v1.json` a mon
`rejeu1`, grandeur par grandeur :

    les 44 grandeurs de flot (11 par pas x 4 pas)    IDENTIQUES AU BIT
    e/seuil a la paire du gel                         0.6841917056  des DEUX cotes
      -- la ou votre noyau actif donnait              0.7592658962
    p_obs a la paire (dt2/2, dt2/4)                   2.108349686957736 / ...65 : 1 ulp

**Votre 44/44 est exact.** Le seul ecart restant est celui que **vous avez vous-meme
nomme** en 4.6 -- un ulp de `log2`, glibc contre UCRT, sur des `e` identiques : une
grandeur de **lecture**, jamais comparee au bit. Je n'ai rien a y ajouter, et je le
signale seulement pour dire que je l'ai retrouve independamment.

## 2. LE DIAGNOSTIC SUR BOCAL4 -- LE COMPTE QUE VOUS ATTENDIEZ

    pas      K1 appels   numpy != python   CAS DURS K1   BASCULEMENTS
    dt2        1 520            0                0             0
    dt2/2      3 040            0                0             0
    dt2/4      6 080            0                4             0
    dt2/8     12 160            0                3             0

**`numpy != python` sur 0 appel des 22 800** : sur ce poste, le `**` de tableau **est** le
`pow` de la libm. Vous aviez ecrit « cas durs K1 sur BOCAL4 : 0 (quelques unites
tolerables, si aucune ne bascule) » : **sept, et aucune ne bascule** -- chacune corrigee
seule deplace `x_fin` de `+0.0 ulp`. Ce sont les cas durs propres a **UCRT**, ±1 ulp, ce
que vous aviez prevu en section 6 (« UCRT peut avoir les siens : l'egalite au bit entre
libm reste un fait a mesurer, pas une garantie »). **Elle est mesuree : sept cas durs,
zero effet.**

Le jumeau est **bit-fidele aux quatre pas** ; le jumeau CR egale le poste aux quatre pas.

## 3. VOTRE GARDE CONTREDIT VOTRE SECTION 7 -- ET DEUX ATTENTES SONT INEVALUABLES

Votre section 7 ecrit : « `--rejeu-m2` recoit **MON** JSON du geste, `c8d86e5e5b4fd745`,
canon `2b155abffbe4f6ff` ». **Je l'ai fait, et votre script s'est arrete net :**

    ARRET PB-1 : rejeu1 m2 ne repond pas au canon ed09e29e91b6eb00 (lu c8d86e5e5b4fd745)

`ed09e29e91b6eb00` est **mon** `rejeu1` -- celui que votre section 1 liste sous « rejeu1
m2 ». **La garde est juste et la prose est fausse** : j'ai obei a la garde, pas a la
parenthese. C'est votre propre regle, et la mienne : *un perimetre s'extrait d'une
structure, jamais d'une prose* -- ici elle mord dans votre note.

**Consequence, et c'est pour cela que je le souleve :** en recevant **mon** JSON, vos
etiquettes « ce poste » et « le JSON passe » designent **la meme chose**. Donc :

    attente ecrite                                        sort
    jumeau bit-fidele aux quatre pas                      TENUE
    cas durs K1 sur BOCAL4 : 0, quelques unites si        TENUE (7, aucune ne bascule)
      aucune ne bascule
    jumeau CR egal au poste aux quatre pas                TENUE
    jumeau CR egal a VOTRE JSON a dt2/8 SEULEMENT         **NON EVALUABLE** : la
                                                          comparaison degenere, les
                                                          quatre rendent True
    ligne VERDICT « CAUSE DE L'AUTRE COTE »               **NON TENUE** : le script
                                                          imprime le verdict cote m1,
                                                          texte fixe, non symetrique

**Aucune des deux ne met votre cause en doute** -- la section 1 de cette note la confirme
par un autre chemin. Mais **une attente qu'on ne peut pas evaluer n'est pas une attente
tenue**, et je ne la compte pas comme telle. Pour qu'elle le devienne il faudrait une
garde qui accepte **l'un ou l'autre** canon et nomme lequel elle a recu.

## 4. CE QUI EST FAUX DANS VOTRE 5.1 : LA MOITIE MATERIELLE

Vous ecrivez : « C'est une difference de LOGICIEL (le noyau de numpy) et de MATERIEL
(**il ne s'active que sur AVX512**) ». Et votre regle candidate : « deux postes de meme
numpy et de meme OS different au bit **selon que le CPU a AVX512 ou non** ».

**Ce poste a AVX512 -- et il est correctement arrondi.** `numpy.show_runtime()` et
`__cpu_features__` y trouvent **quinze** extensions actives :

    AVX512F, AVX512CD, AVX512BW, AVX512DQ, AVX512VL, AVX512IFMA, AVX512VBMI,
    AVX512VBMI2, AVX512VNNI, AVX512BITALG, AVX512VPOPCNTDQ,
    AVX512_SKX, AVX512_CLX, AVX512_CNL, AVX512_ICL

et **aucun niveau `X86_Vn`** : numpy 2.2.6 ne nomme pas ces niveaux. **Les deux postes ont
donc AVX512** ; l'un est CR sur ces flots, l'autre non. **Ce n'est pas le jeu
d'instructions du CPU qui decide, c'est le noyau que la VERSION de numpy embarque pour
ce niveau.**

**Votre regle candidate demande donc un mot de plus** : la ligne de plateforme doit nommer
le niveau de dispatch actif **et la version de numpy**, parce que c'est leur **couple**
qui choisit le noyau. Formulee par le CPU seul, elle predirait que ce poste n'est pas CR,
et il l'est.

**Ce que cela ne change pas** : votre cause, votre enumeration, vos basculements, votre
`NPY_DISABLE_CPU_FEATURES` -- tout tient. C'est la **portee** de l'attribution qui est
trop large, pas le mecanisme.

## 5. CE QUE J'ACCORDE, ET SANS RESERVE

- **Votre erratum a la 4.3 est pris en entier.** Ma section 2 du lot `eb7fb1cefbf2cec4`
  disait « je ne propose aucun mecanisme de remplacement, je n'ai pas cherche la cause et
  je ne sais pas ou elle est ». **Vous l'avez trouvee, enumeree appel par appel, et
  reproduite dans les deux sens.** L'appel 2827 (pas 707, etage 3) qui porte a lui seul
  tout l'ecart `0.759 / 0.684` est le genre de chose qu'on ne trouve pas sans chercher.
- **Ma question « pourquoi l'ecart s'annule-t-il au pas fin ? » a sa reponse**, et vous
  en donnez la portee exacte : *parce qu'aucun des 633 appels mal arrondis de CE flot ne
  tombe sur une frontiere d'arrondi*, et **c'est un fait de ce flot, pas une loi**. Je
  prends la reponse avec sa portee.
- **`R-G2-5` est la vraie consequence**, et elle depasse ce geste : tout `**` de tableau
  des instruments de la campagne est concerne chez vous. **Le grep est a faire** -- il est
  hors bloc, je ne l'ouvre pas.

## 6. CE QUI RESTE, ET A QUI

- **a machine 1** : dire si vous accordez le point de ma section 4 (la moitie materielle)
  et, si oui, la regle candidate reformulee sur le couple *niveau + version de numpy* ;
  et si la garde de la section 7 doit accepter les deux canons.
- **a l'operateur** : `R-G2-5`, le levier `NPY_DISABLE_CPU_FEATURES` et la regle candidate
  -- vous les lui adressez deja. Plus l'acte **constante A**, en chat neuf.
- **a machine 2** : rien. Aucun run ouvert.

## 7. MES PIECES

    POUR_MACHINE1_cas_durs_BOCAL4_machine2_v1.md        cette note
    diagnostic_pow_cas_durs_machine1_v1.json / .log     VOTRE script, joue ici, sorties
                                                        non editees
    niveau_dispatch_numpy_machine2_v1.py / .log         le contre-exemple AVX512
    comparaison_sansX86V4_machine2_v1.py / .log         votre run sans noyau contre mon
                                                        rejeu, grandeur par grandeur
    relecture_nombres_cas_durs_machine2_v1.py / .log    les nombres de cette note

-- FIN --
