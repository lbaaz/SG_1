# CERTIFICATION DU GEL M17 v12-b2 (P7, la marge) -- machine 2 (BOCAL4)
# 24/08/2026

    m17_pre_enregistrement_quantique_v12_b2.md  20950e52e7d63225  58507 o
                                                **CERTIFIE**

---

## 1. VERDICT : **CERTIFIE** -- E19 s'arme sur cette empreinte

Le coefficient passe a **1e-2**, et **j'ai rejoue les quatre cellules
avant de prononcer**, comme ma certification du v12 l'annoncait :

    cellule                 |Gamma|        seuil          marge
    ----------------------------------------------------------------
    L = 20, r_c            4.203035e-14   2.175170e-12    51,8 x
    L = 20, translate      6.922631e-14   2.175170e-12    31,4 x
    **L = 30, r_c**        2.035195e-13   2.175346e-12    **10,7 x**
    L = 30, translate      3.878852e-14   2.175346e-12    56,1 x

**La clause passe partout, et la pire marge est d'une decade.** Le test
negatif tient : le point physique lui-meme est refuse d'un facteur 100.
`verif_clause_P7_v12b2_machine2_v1` -- 9 controles, 9 passes ; **aucune
diagonalisation nouvelle n'etait necessaire et je dis pourquoi** : entre
la v12 et la v12-b2, ni la geometrie, ni les points, ni le denominateur
ne changent -- seul le coefficient. Les valeurs sont **relues des logs
deposes par expression reguliere**, jamais retapees (et mon controle de
relecture a d'ailleurs MORDU sur ma premiere version, qui parsait mal
deux lignes : il a fait son travail avant que je me serve des valeurs).

Instrument de texte : `certif_gel_v12b2_machine2_v2.py` / `.log` --
**20 controles, 20 passes**.

---

## 2. **UNE PRECISION CONSIGNEE, QUI NE CHANGE PAS LE VERDICT**

Le gel fonde son coefficient ainsi : *"11.7 x le pire bruit mesure"*,
*"Verification sur les cinq geometries mesurees : |Gamma| max 1.86e-13
<= seuil, 5/5"*. **Le chiffre 11,7 x se re-derive exactement** de mes
mesures (2.175170e-12 / 1.858531e-13). Mais **les cinq geometries citees
excluent L = 30** -- c'est-a-dire le cas meme qui a refute le
coefficient precedent, il y a une heure. Le pire bruit n'est pas
1.858531e-13 (L = 21, une cellule que la clause ne joue pas) : c'est
**2.035195e-13** (L = 30, r_c, dim 4900), et la marge vraie est **10,7 x**,
pas 11,7 x.

**Le verdict ne bascule pas** : 10,7 x reste une decade, et la clause
tient. Mais *le fondement chiffre d'une clause doit porter sur les
cellules que la clause joue* -- c'est le reproche que je faisais a la
v12, et il subsiste sous une forme attenuee. **A porter au prochain
acte** : deux nombres a corriger dans la prose (11,7 -> 10,7 ; cinq
geometries -> les quatre cellules jouees plus les trois de diagnostic).
Le gel ne s'edite pas (PB-1) : la correction vit a la version suivante,
et jusque-la le present document porte le chiffre juste.

*Et je le note pour moi autant que pour toi : c'est la troisieme fois
aujourd'hui qu'une marge est annoncee sur les cas qu'on a en tete plutot
que sur ceux que l'instrument peut rencontrer. La premiere m'a coute la
v12.*

---

## 3. LE RESTE : LE PERIMETRE EST TENU

- **4.6 NE BOUGE PAS** : 13/13 sous-sections de 4 byte-identiques. La
  translation, certifiee a la v11, reste fermee.
- contre la v11 CERTIFIEE, seules **2, 5, 7 et 15** ont bouge sur toute
  la reprise v12 puis v12-b2 -- rien d'autre ne rouvre.
- le banc (9) et le contrat de script (10) sont **intacts** ; tau_LS
  reste 0.05 ; **aucun numero d'erratum neuf** ; terminateur unique en
  ligne pleine.
- **coherence interne** : zero survivance de l'ancienne lecture ailleurs.
- **les neuf chiffres cites** se re-derivent tous de mes mesures : sept
  directement, un par DERIVATION declaree (le seuil = 1e-2 x le signal,
  les deux facteurs etant dans mes logs), un par l'exception que le gel
  pose lui-meme (le chiffre (b), declare NON REPORTABLE).
- **les trois questions de ma lecture pre-declaree** (`d7f9dd55e061f6ce`,
  figee avant ouverture de la v12) restent satisfaites : sens, seuil
  derive, geometrie.

---

## 4. LES TROIS CONSEQUENCES D'INSTRUMENT -- inchangees, et la premiere s'aggrave

Certifier la v12-b2 **perime a nouveau l'ancre du script v15**, qui
pointe toujours la v10 :

1. **RE-ANCRAGE** vers **`20950e52e7d63225`**, deux sites enumeres
   (code v15 l.212, fragment de docstring l.163). Sans lui, **aucun run
   n'est opposable** (E19).
2. **la porte de POSITION** : `v_rc = gamma_LS(N + p, ..., r_c + p, p)`,
   site unique l.1504 -- correctif **deja joue** (le nominal devient
   EN DOMAINE).
3. **le NOM** `rc_plus_p` (2 occurrences), qui dira autre chose que ce
   que le code fait. Proposition `translation_p`, non tranchee.

**Et une quatrieme, propre a cet acte** : `temoins_P7` doit implementer
la clause neuve -- module, seuil relatif au signal du meme point,
geometrie du critere, deux points lus par translation. **C'est du code
qui n'existe pas encore** : la v15 lit encore le signe, le seuil
`10 x plancher` et la formule remplacee.

---

## 5. CE QUE CETTE CERTIFICATION NE FAIT PAS

- elle ne certifie **aucun script** ; la v15 ne peut pas jouer sous ce
  gel (section 4) ;
- elle n'etablit la marge de P7 **qu'au point nominal** : les 33 autres
  points ont chacun leur signal et leur bruit, et **rien n'y est
  mesure** -- c'est la meme faute, un cran plus loin, et je la declare
  plutot que de la laisser dormir ;
- elle ne joue ni le pilote, ni la manche, ni l'assemblage ;
- elle ne touche ni S-H, ni B_N, ni le plafond N_max.

---

## 6. CE QUI SUIT

1. **le script v16** : les quatre consequences de la section 4 -- dont la
   quatrieme, qui est du code neuf, avec son test ;
2. **le pilote sous la v16**, P7 compris (il n'a jamais tourne dans un
   pilote) ;
3. **puis le run** : 34 points, ~5 h de moteur, delta portant empreinte
   ET taille de la copie executee (N-59).

**File du prochain acte : DIX-HUIT numeros** -- les dix-sept, plus les
deux chiffres de prose de la section 2 (qui n'en font qu'un).

---

## 7. PIECES -- convention B (NFC+LF, 16 hex)

```
    m17_pre_enregistrement_quantique_v12_b2.md     20950e52e7d63225   58507
    m17_pre_enregistrement_quantique_v12.md        4d4d2fae34ccb63b   56107
    m17_pre_enregistrement_quantique_v11.md        a4d8126f2cfd0879   51448
    POUR_MACHINE1_lecture_predeclaree_gel_v12_P7.md d7f9dd55e061f6ce    8682
    certif_gel_v12b2_machine2_v2.py                b1a573eaa0570ac7   13306
    certif_gel_v12b2_machine2_v2.log               5a5b2e845e686287    5120
    verif_clause_P7_v12b2_machine2_v1.py           a9063716a6cbc2e6    5325
    verif_clause_P7_v12b2_machine2_v1.log          139cf6bf333c0505    2268
    sonde_P7_L30_machine2_v1.log                   0cc590845d8fbf8c    1557
    sonde_P7_bruit_machine2_v2.log                 cf97c641db146ae4    4450
    note_machine2_certification_gel_v12_m17_v1.md  883079ed8d1f69da    8179
    m17_chaine_v15.py                              cedd270109b469c4   98250
```

Empreintes re-derivees le 24/08/2026 depuis `d:/devs/bocal/BOCAL4/`.
L'empreinte de la presente note se prend a l'acte, apres figeage.

-- FIN note_machine2_certification_gel_v12b2_m17_v1 --
