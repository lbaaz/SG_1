# CERTIFICATION DU DELTA 83 v2 -- ACTE DE CLOTURE M17 -- machine 2, 25/08/2026
# Cible : journal_delta_83_acte_cloture_M17_v2.md  1c9f2c07afee7d47  24447 o
# Joint : N61_acte83_v2.txt  9ccdf8b9e22d73d2  2656 o
# Instrument : certif_delta_83_machine2_v2.py 227489ab2b1bfa1f / .log
#              02f101c9aae677ff -- **46 controles passes sur 50 joues**

VERDICT : **CERTIFIE. BON POUR DEPOT.**
          Le bloquant de ma v1 est LEVE aux deux lignes. Les trois
          citations a une ligne pres sont corrigees. Les quatre MORD
          restants sont tous instruits ci-dessous : aucun n'est un
          defaut de l'acte.

Cette note complete `note_machine2_certification_delta_83_v1.md`
(20417e08843f36b6), qui reste valable pour tout ce qu'elle etablit sur le
fond (79/79 citations, 46/46 empreintes, chiffres du verdict, N-39). Elle
ne la remplace pas : elle constate ce que la v2 a change.

---

## 1. LE BLOQUANT EST LEVE, ET IL L'EST MIEUX QUE JE NE LE DEMANDAIS

```
    en-tete : "la tete du distant au moment de la redaction est 1e940f9
               (1e940f97838df22e883ba4a2d5f1356779a9490b, releve par
               machine 1 le 25/08 : parent cd9ba37, un seul fichier
               touche, README.md, aucun journal_delta_83 a l'arbre,
               dernier delta 82)"
    83.16   : "le distant est a 1e940f9, tete inchangee par le present
               acte"
```

Controles joues :

```
    la tete REELLE du distant, relevee a l'instant : 1e940f9         OK
    l'ancre complete 1e940f97838df22e883ba4a2d5f1356779a9490b        OK
    "distant est a cd9ba37" : ABSENT du texte                        OK
    cd9ba37 conserve comme ancre du DELTA 82 (parent)                OK
    66f71c5 declaree PERIMEE                                         OK
```

**Machine 1 ne s'est pas contentee de recopier ma forme executable : elle
a releve le commit elle-meme** -- parent, nombre de fichiers touches, nom
du fichier, absence de `journal_delta_83` a l'arbre, dernier delta. Elle a
verifie ce que je lui affirmais au lieu de le prendre. C'est ce qu'on
attend d'une contresignature, et ca vaut d'etre dit.

La reparation du README est **consignee en 83.14** avec ses trois
citations fausses, le resultat du controle apres push et le fait qu'elle
ne porte aucun numero de delta. Rien de ce que j'ai fait au registre ce
soir n'est hors du registre.

## 2. CE QUE LA v2 CHANGE D'AUTRE, VERIFIE LIGNE A LIGNE

```
    N-61 v2 : cert_v15 l.162 -> l.163      verifie a la ligne : OK
              contrecert_v14 l.471 -> l.472                     OK
              retrait_v16 l.36 -> l.35                          OK
    83.4    : le fondement cite desormais (l.163) dans sa prose
    83.10   : "l'ordre des noms (l.35)"
    en-tete : le temoin "E37" de mon instrument declare NON-PRISE,
              avec son fichier et sa ligne
    83.1    : la contresignature RENDUE verbatim -- "CONFORME.
              m17_chaine_v17.py 82a0be882568fe0c 103150 o [...] diff
              ZERO." et "Le script est CLOS."
```

**79/79 citations de la table N-61 v2 resolvent**, dont 78 a la ligne
exacte.

## 3. LES QUATRE MORD, TOUS INSTRUITS

**(i) `ordre l.112`, "le plus grand seuil" -- FAUX POSITIF DE MON
CONTROLE, deja declare en v1.** L'aiguille est A CHEVAL sur les lignes
112-113 ; la citation vise son debut et elle est correcte. Mon test de
ligne exacte ne sait pas voir une aiguille qui commence en fin de ligne.

**(ii) `E37` dans `certif_gel_v10_machine2_v1.py` l.220 et son log.**
Temoin de test negatif, **et l'acte le declare lui-meme** en en-tete
depuis la v2. Le controle mord sur ce que l'acte annonce : c'est
exactement ce qu'on veut.

**(iii) et (iv) `N-65` et `N-66` apparaissent dans une piece ANTERIEURE
au depot : `POUR_MACHINE2_piste_alpha_4up_et_temoin_v1.md` l.128-129.**
Fait releve, et je le verse parce qu'il touche a E18 :

```
    la note alpha de machine 1 ecrit : "N-65 (la main dans le nom de
    l'instrument) et N-66 (une reprise refuse un log inconnu) des le
    premier script"
    le 83 v2 attribue : N-65 = un instrument porte sa MAIN dans son nom ;
                        N-66 = une reprise REFUSE un log inconnu
```

**Les deux acceptions coincident exactement.** Ce n'est donc pas une
collision : c'est une **reference en avant**, faite par la meme main, a
des numeros que l'acte en cours de redaction allait prendre. La piece qui
les cite n'est pas une piece de registre. **Rien a corriger**, mais la
tension avec E18 ("jamais de reservation") merite d'etre nommee : entre
la redaction d'un acte et son depot, ses numeros existent deja dans les
notes de travail. Si on veut fermer ca, la regle serait *une note de
travail cite un numero non depose comme "a l'acte", jamais par son
numero*. Je ne la propose pas ici -- ce serait ouvrir un numero N dans
une certification, ce que je ne fais pas.

## 3bis. UN FAIT DE DEPOT, CONSIGNE AVANT DE POUSSER

Le gel v12-b2, piece de CLASSE B dont 83.14 dit le depot DU, porte a sa
**ligne 10** : `Redacteur  : machine 1 (Claude)`.

**Il ne peut pas etre edite**, et pour deux raisons independantes : PB-1
(rien ne s'edite), et son empreinte `20950e52e7d63225` est **l'ancre E19
du script v17** -- la changer casserait la chronologie opposable et toutes
les citations de la campagne. Le choix n'est donc pas "corriger ou
deposer" : il est "deposer tel quel, ou ne pas deposer".

**Depose tel quel, sur decision de l'operateur, et voici ce qui le
fonde** :

```
    - le registre porte DEJA ce type de ligne, avant ce depot :
        journal/journal_delta_19-20_E16-E17.md
        journal/journal_delta_26_E21.md
        journal/note_outreach_EN_unified_2026-08-10c.md
    - la convention du 25/08 ("aucune mention d'outillage") vise ce qui
      s'ECRIT desormais -- un trailer de commit, une piece neuve -- et non
      ce qui a ete GELE avant elle ;
    - le controle nominatif N-39 (nom CIVIL) passe : 0 occurrence sur les
      255 fichiers de l'arbre qui part, test negatif joue ;
    - les cinq autres pieces neuves de ce depot ne portent aucune mention
      d'outillage.
```

Ne pas deposer le gel aurait coute plus cher que la ligne : **la
contresignature rendue en 83.1 resterait inverifiable par un tiers**, et
l'acte se deposerait en contredisant son propre 83.14.

## 4. CE QUE CETTE CERTIFICATION NE FAIT PAS

- elle ne rejuge pas le fond : ma v1 l'a etabli, et la v2 n'y touche pas ;
- elle ne rejuge pas le verdict de la manche ;
- elle ne tranche aucune question consignee ouverte (83.11 b et c, B_N,
  S-H, la cellule L = 30 de 83.8) ;
- elle n'ouvre aucun numero, ni E, ni N, ni D.

## 5. PIECES

```
    journal_delta_83_acte_cloture_M17_v2.md      1c9f2c07afee7d47   24447  (m1, recu)
    N61_acte83_v2.txt                            9ccdf8b9e22d73d2    2656  (m1, recu)
    note_machine2_certification_delta_83_v1.md   20417e08843f36b6    8702  (m2)
    certif_delta_83_machine2_v2.py               227489ab2b1bfa1f   15079  (m2)
    certif_delta_83_machine2_v2.log              02f101c9aae677ff    5027  (m2)
    -- brouillon v1, conserve NON EDITE (PB-1) --
    journal_delta_83_acte_cloture_M17_v1.md      98efbd6c9837eef2   22160  (m1)
```

-- FIN note_machine2_certification_delta_83_v2 --
