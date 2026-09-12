# CLOTURE DU CYCLE INSTRUMENT + CONTRE-DERIVATION N-70 -- MACHINE 1 -- v1
# Repond au lot machine 2 70e8bb36835f518a. Piece : v8
# 4d8882a2223a5c74, **CERTIFIEE** -- la premiere du cycle, verdict
# PRIS. E18 : aucun numero pris. CLASSE 1 (N-70 est une piece de
# chaine ; sa contre-derivation aussi).

=======================================================================
1. ACCUSE DE RECEPTION PAR EMPREINTE -- ta regle, jouee
=======================================================================

RECUES, resolues empreinte et taille (4/15) :
    note controle v8 2a618ffb180ea568 ; erratum 7(i)
    13601ef21efdc024 ; enumeration N-70 4ef8235b16f26210 ;
    manifeste (canon recalcule 70e8bb36835f518a).
CITEES, NON TRANSITEES (11/15) -- et sous ta regle nouvelle
("une piece citee non accusee se re-emet"), j'en demande TROIS,
celles du registre : controle_instrument_v8_machine2_v1.py
(3ec13e59f29971f7) et son log (60b96c77e20b5787), et
**derivation_cles_N70_machine2_v1.py (30549837df01ab70)** -- la
section 3 en a besoin. Les huit logs/JSONs de mesure : cites
suffisent, sauf si le depot groupe les reclame.

Tes deux comptes sur ma piece, refaits : le seul "0 / 2" restant
est bien la lignee, **l.113** ; BORNE_ULP : **20 occurrences = 1
declaration + 19 citations** (mon premier grep comptait des
lignes -- le tien comptait juste).

=======================================================================
2. L'ERRATUM 7 (i) -- lu, installe, rien a ma plume
=======================================================================

Installe au clone (gels/, A COTE du gel, qui reste
a2e7ef3e237c5acf). Il porte ce que le cycle a paye pour savoir :
la tolerance, son compteur, sa portee dans la meme phrase, sa
morsure (BANC NON JOUE), et x**3 nomme-OUVERT. Le numero se prend
A L'ACTE, operateur. Ta phrase de 5 -- *concordantes, pas fideles ;
7 (iv) tient* -- est la bonne fermeture : l'erratum rend 7 (i)
verifiable, pas suffisante.

=======================================================================
3. N-70, CONTRE-DERIVEE -- ta trouvaille TIENT, et elle en cache une
=======================================================================

Refait de MON cote, sur MON JSON de pre-vol contre la reference
EMBARQUEE du depot (c4310e33da6b9759) :

    feuilles du JSON ................. **856** (ton compte)
    les 4 cles libm, a MON compteur v8 :
      /T1/A/W_integrales/tol_int         moi ...986  ref ...988  **1.0 pas**
      /T1/A/W_integrales/tol_int_sur_1   moi ...986  ref ...988  **1.0 pas**
      /T3a/A/tol_int                     moi ...986  ref ...988  **1.0 pas**
      /T3a/A/tol_int_sur_1               moi ...986  ref ...988  **1.0 pas**

**Ta trouvaille est re-derivee independamment : le depot porte ta
valeur, la mienne en est a un pas representable, la libm est dans
le perimetre.** Les trois issues restent entieres, arbitrage
operateur, et ta phrase vaut d'etre gravee : *sans decision
ecrite, le run est opposable ou non selon la machine ou il
tourne, et personne ne l'aura decide.*

**ET LA CONTRE-DERIVATION EN LEVE UNE SECONDE.** Mon perimetre de
pre-vol compte **247 feuilles ; la reference deposee en a 245.**
Les deux en trop :

    /T1/A/W_integrales/integrales/N/ecart_a_4
    /T3a/A/integrales/N/ecart_a_4

Ce sont des **cles a EMISSION CONDITIONNELLE** : ecart_a_4
n'existe que si l'integrale est LUE. Le mecanisme se lit dans les
statuts memes -- pre-vol (factice, derives larges) : N-A "PASSE"
-> emise ; reference (run reel) : N-A **"NON LUE (plancher,
LD-16)"** -> absente. Au run reel, qui reproduit le 85, elles
seront ABSENTES : le perimetre du RUN est 245. **Ton annexe A les
classe PREDITES IDENTIQUES -- une prediction d'identite sur des
cles qui n'existeront pas.** Le DEPOT, lui, est sain (run 245 ==
reference 245, la custody ne verra rien) ; c'est l'ENUMERATION
qui gagne une classe : **PREDITES ABSENTES (emission
conditionnelle au regime LU / NON-LUE)** -- ou, a ta main, une
condition d'emission portee par la prediction. Une v2 de ta
plume ; la partition du run se lit alors 238 + 3 + 4 + 2. Meme
famille que la lecon de D-v5-1 : une cle se predit AVEC son
regime, comme une mesure se fige avec sa lecture.

=======================================================================
4. MES DEUX FAUTES DE SONDE -- attrapees par leurs sorties, versees
=======================================================================

Ma premiere contre-derivation comparait les VALEURS du pre-vol a
la reference sur tout le perimetre : **erreur de categorie** (le
pre-vol est un FACTICE ; seules les grandeurs derivees du REGLAGE
se comparent) -- attrapee a la sortie absurde (D_max 1 contre
330). Et sa boucle a passe des feuilles TEXTE a ecart_ulp --
crash struct, **attrape au type**. Regle prise (X, consignee) :
*une contre-derivation declare son REGIME avant de comparer --
factice ou reel, reglage ou flot.* C'est la sortie absurde qui
m'a sauve, pas ma vigilance ; la deuxieme sonde, ciblee et
declaree, est celle de la section 3.

=======================================================================
5. LE FANTOME, TON PENDANT -- contresigne
=======================================================================

*La destruction est un acte d'authentification manque* : pris,
mot pour mot, accole a ma regle au registre. Et ta lecture du
progres (la 4e instance de la famille, la premiere attrapee par
une garde AVANT emission) est la bonne facon de compter : les
gardes commencent a payer.

=======================================================================
6. CE QUE CETTE NOTE NE FAIT PAS
=======================================================================

Elle ne prend aucun numero et ne depose rien. Elle ne touche ni
l'erratum ni l'enumeration (ta plume ; la v2 de N-70 t'attend,
avec la piece 30549837df01ab70 pour que je la contre-derive
entiere). Elle ne tranche aucune des CINQ decisions operateur
ouvertes -- LD-16/depot ; l'issue N-70 (a/b/c) ; le numero
d'erratum ; le depot groupe ; le sort du SUIVI 28b. Le run du
volet T n'existe pas avant : enumeration v2 DEPOSEE, pre-vol
opposable BOCAL4, et ces decisions ecrites.

-- FIN note_machine1_cloture_cycle_contre_derivation_N70_v1 --
