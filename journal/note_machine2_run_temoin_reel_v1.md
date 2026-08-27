# LE TEMOIN NEGATIF CLASSIQUE -- RUN REEL, CERTIFICAT D'EXECUTION
# Machine 2, 28/08/2026. Sur ordre de l'operateur.
# Instrument : banc_qualification_machine1_v3.py  5fae2a8c94cf8685
#              CERTIFIE (baf75f462ab14119), contresigne (146f7dd9d81ace1d),
#              et DEPOSE avant ce run (registre e800c71).
# Gels       : temoin v7 8b083e9f109b5a8e ; alpha v5 045c2435aaf623ce
#              (registre 0485001) ; moteur c8ed357b120352c4.
# Files      : E18, aucun numero pris ; maximum cite E42, N-69, D-M17-45.

VERDICT : **REGLAGE QUALIFIE (bonus T-3 retire) -- branche 6.**
          **LA PORTE D'ALPHA S'OUVRE**, et elle ne s'ouvre que la.

RESUME -- DIX LIGNES

```
    1  verdict REGLAGE QUALIFIE (bonus T-3 retire), branche 6, 30.3 s
    2  comptes 41 + 0 == 41 en forme derivee ; 0 run saute
    3  T-1, etat A : R = 1.9528 2.0300 1.9590 2.0077 ; tol_R/(q-1) 0.0595
    4  T-1, etat B : R = 1.9386 1.9668 1.9372 2.0123 ; tol_R/(q-1) 0.1607
       fenetre de q aux DEUX etats, saturation FAUSSE aux deux
    5  T-1b : seuils 0.9772529766 / 1.9545054057 / 0.4872145458,
       motif OK|pas=6.03e-07, k = 0 ; les DEUX lois : 1.999999 et 0.498555
    6  W-integrales MORD : q_int = 4.0943 (A, H1), 4.1072 et 4.9598 (B)
       contre tol_int 0.00858 et 0.01536 -> bonus retire, RIEN d'autre
    7  LD-16 joue : N a l'etat A sous le plancher machine -> NON LUE
    8  seize gardes sur seize demontrees mordantes DANS ce journal
    9  MANIFEST verifie par sha256sum -c ; ASCII, CR = 0 ; statut REEL
   10  LA PREDICTION DEPOSEE TIENT : 19 cles sur 19, aucun ecart
```

## 1. LA PREDICTION, D'ABORD -- 19/19

La prediction a ete **deposee au registre AVANT ce run** (e800c71, note
e70b639a04b8d136, JSON de pre-vol 786a368878768d4b), contresignee
d3a0d73a3139da3b. Comparaison, cle par cle, du JSON depose contre le
JSON du run reel :

```
    T2, T3b, W_comptes, algorithme_vs_moteur, attendus, attendus_total,
    banc_gardes.ok, banc_gardes.n, banc_gardes.demontrees,
    champ_forces_empreinte, comptes.comptes, comptes.sautes,
    comptes.sautes_noms, mode, ne_joue_pas.gardes_sans_morsure,
    ne_joue_pas.runs_non_joues, reglage, symbolique, transcription_ok
    -> 19 / 19 IDENTIQUES, aucun ecart, aucun.
```

**Rien n'a bouge hors de l'instrument.** Ce qui devait bouger a bouge :
T-1, T-1b, T3a, les lectures non lues, le verdict et la branche -- les
sept cles declarees NON PREDITES, et elles seules.

## 2. CE QUE LE DISCRIMINANT DIT, ET C'ETAIT TOUTE LA QUESTION

**T-1 : LA CROISSANCE EST LINEAIRE.** Aux deux etats initiaux, les
quatre rapports R tombent dans la fenetre de q = 2, et **saturation est
FAUSSE aux deux**. Le temoin devait trancher entre "blow-up en temps
fini" et "croissance sans explosion" ; il tranche pour la seconde. C'est
la lecture pre-declaree du gel (section 12), et c'est celle de
Damour-Smilga : **benin n'est pas borne** -- le fantome monte
lineairement, il n'explose pas.

**T-1b : LE SEUIL DE LA RECHERCHE DEPOSEE EST UN MIRAGE, ET IL SUIT SES
DEUX LOIS AU MILLIEME.**

```
    s*(2 CAP, T) / s*(CAP, T)  =  1.999999      (q = 2 attendu)
    s*(CAP, 2 T) / s*(CAP, T)  =  0.498555      (1/c_T = 0.5 attendu)
```

Sur une croissance lineaire, `s* = CAP/(v T_MAX)` : le seuil rendu ne
mesure pas le systeme, il mesure le plafond et l'horizon. **La recherche
de seuil deposee rend un mirage la ou elle DOIT en rendre un**, et c'est
tout ce que ce banc lui demandait.

Les trois seuils concordent au dernier chiffre avec la mesure hors gel
faite avant ce banc (0.977252977 / 1.954505406 / 0.487214546) : le banc
retrouve, DANS l'instrument certifie, ce qui n'avait ete vu que dehors.

## 3. W-integrales MORD -- ET C'EST LA MEILLEURE NOUVELLE DU RUN

```
    etat A  H1  q_int = 4.094288   tol_int = 0.00858   MORD
    etat A  N   NON LUE (plancher machine, LD-16)
    etat B  H1  q_int = 4.107234   tol_int = 0.01536   MORD
    etat B  N   q_int = 4.959798   tol_int = 0.01536   MORD
```

L'ordre observe est **4.09 a 4.96 au lieu de 4** : la chute de la derive
entre dt et dt/2 n'est pas exactement d'un facteur 16. La tolerance,
elle, vaut 0.0086 et 0.0154. **La garde mord donc, et c'etait ecrit.**

**Machine 1 l'avait annonce mot pour mot** en certifiant le gel v6 :
"b ~ 0.02 donne tol_int ~ 0.015 ; sur une derive maximale prise sur
T_MAX ~ 600, la chute d'un facteur 16 peut s'ecarter de plus que cela
sans faute de schema. Si W-integrales mord, la seule consequence est le
bonus." **J'ai refuse de desserrer la tolerance** -- desserrer sans
derivation aurait ete la faute de LD-4 refaite -- **et j'ai ecrit a la
place, dans le gel v7, que sa morsure mene a la branche 6 et nulle part
ailleurs.**

C'est exactement ce qui s'est passe. Une garde dont on savait la
tolerance serree a mordu, et elle n'a coute que le bonus. **Si nous
l'avions laissee dans une branche letale, la manche mourait ce soir sur
une tolerance dont nous savions d'avance qu'elle etait serree.** C'est
le seul endroit du dossier ou une decision de forme a change une issue.

**LD-16 a joue aussi**, et lui aussi etait annonce : a l'etat A, la
derive de N a dt/2 (2.914e-11) tombe sous le plancher machine, et
l'integrale est declaree **NON LUE** au lieu de rendre une morsure
d'arrondi. Machine 1 avait ecrit cette consequence "ici et non predite"
en livrant la v3 ; elle s'est produite.

## 4. CE QUE CE RUN NE DIT PAS

  - **il ne dit rien d'alpha** : il qualifie le REGLAGE (delta, r, M, k,
    dt_2), pas la prediction alpha = 4/(p-2) ;
  - **il ne prouve pas que le reglage est bon** : il a cherche a le
    refuter et n'y est pas parvenu. C'est ce que rend un temoin negatif,
    et rien de plus ;
  - **le bonus T-3 est retire** : la conservation des integrales n'est
    PAS versee au dossier de cette manche ;
  - il ne dit rien de la fidelite de la transcription de Damour-Smilga a
    l'article : elle ne repose que sur moi, et la double transcription
    reste due ;
  - il ne prend aucun numero.

## 5. PIECES (convention B, NFC + LF)

```
    out_banc/temoin/
      resultats_temoin.json   644240dc894c2733   24208 o   statut REEL
      journal_temoin.txt      d8ac838ce2d1bd48   14831 o
      MANIFEST.sha256         c557a4fa5aa6bd28     444 o   (5 fichiers, verifie)
      + temoin_T1_flot_A.txt, temoin_T1_flot_B.txt,
        temoin_champ_forces_tirage.txt
    m2_run_temoin_reel.log  (ma capture de sortie ; le journal fait foi)
    instrument   5fae2a8c94cf8685  (registre e800c71)
    prediction   e70b639a04b8d136 sur 786a368878768d4b (registre e800c71)
```

## 6. LA SUITE

```
    1. la contresignature de machine 1 sur ce run et sur le 19/19 ;
    2. **ALPHA, AUX TROIS DEGRES** -- la porte est ouverte (le verdict
       commence par REGLAGE QUALIFIE, et la porte lit ainsi) ;
       rappel : le fait 2 etant dissous par le fait 5, les trois degres
       sont exploitables, et P-A est lisible au plancher de 10.3 ;
    3. l'acte de registre (plume machine 1), qui consignera ce run avec
       le reste.
```

-- FIN note_machine2_run_temoin_reel_v1 --
