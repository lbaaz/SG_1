# ERRATUM AU GEL TEMOIN v11 -- CLAUSE 7 (i) : SA TOLERANCE
# Plume : machine 2. Cible : temoin_negatif_pre_enregistrement_v11.md
#         a2e7ef3e237c5acf, CERTIFIE (note machine 1 v2
#         7fc5f2412b99ad50), gel du volet T.
# Forme : ERRATUM. Il COMPLETE le gel, il ne l'EDITE PAS (PB-1) --
#         meme forme que l'arbitrage de l'operateur du 28/08/2026
#         deja porte a sa lignee. Le gel reste a2e7ef3e237c5acf.
# E18 : aucun numero pris, aucun propose ; le numero d'erratum se
#       prend A L'ACTE, par l'operateur, comme le veut la discipline.
#
# POURQUOI IL EXISTE. La clause 7 (i) exige que les deux
# transcriptions "rendent le meme champ de forces sur un tirage
# declare" -- SANS DIRE A QUELLE TOLERANCE. Tant que le controle
# n'etait pas instrumente, l'omission ne se voyait pas. Elle s'est vue
# a la premiere instrumentation, et elle a coute trois versions
# d'instrument (D-I-5, D-I-6, D-I-7) : une comparaison d'EMPREINTE ne
# peut rendre que "different", et une borne posee sans son regime
# rend un FAUX ECHEC. **"Le meme champ" n'est pas une exigence
# verifiable ; elle le devient ici.**
#
# CE QU'IL NE FAIT PAS. Il ne rouvre rien : ni le reglage, ni T-1,
# T-1b, T-2, T-3, ni le perimetre 9bis, ni aucun verdict. Il ne
# touche pas a `x ** 3` (voir 5). Il n'ajoute aucun nombre pur au
# gel : la borne est MESUREE, et sa mesure est citee.

=======================================================================
1. LE TEXTE
=======================================================================

La clause **7 (i)** du gel v11 se lit desormais ainsi :

```
    (i)   le systeme (2.10)-(2.13) est transcrit DEUX FOIS,
          independamment, et les deux transcriptions doivent rendre le
          meme champ de forces sur un tirage declare -- **ce qui se
          lit ainsi, et pas autrement** :

          -- le TIRAGE (colonnes x, D) : IDENTIQUE AU BIT. Aucune
             tolerance. Il est bit-reproductible par specification
             (PCG64), il est donc OPPOSABLE tel quel, et son
             empreinte se consigne SEPAREMENT de celle du champ.

          -- le CHAMP (colonnes x'', D'') : compare SUR LES NOMBRES,
             en PAS REPRESENTABLES, et non par empreinte.

                 x''  <=  2 ulp
                 D''  <=  2 ulp

          -- au-dela de l'une ou l'autre borne, ou si le tirage
             n'est pas au bit : **W-transcription MORD, et 8
             s'applique : BANC NON JOUE, avant tout run.**
```

=======================================================================
2. POURQUOI 2, ET POURQUOI PAS LA MEME RAISON DES DEUX COTES
=======================================================================

Les deux bornes valent 2 ; **elles ne valent pas 2 pour la meme
raison**, et c'est ce qui interdit de les confondre :

```
    x''  =  -( w^2 x + lambda * **x^3** )
           sa chaine contient l'unique appel a la bibliotheque
           mathematique de tout le champ. `pow` n'est pas normalise au
           bit : deux plates-formes conformes en donnent des resultats
           qui different. **x'' n'est donc PAS bit-reproductible ENTRE
           MACHINES ; il est exact a machine egale.**

    D''  =  -( w^2 + 3 lambda x^2 ) * D
           sa chaine n'a que des additions, soustractions et
           multiplications : elle est IEEE-exacte, donc **identique
           entre MACHINES**. Mais l'ORDRE D'ASSOCIATION d'un produit a
           trois facteurs n'est pas impose par les equations :
           (3x)*x et 3*(x*x) sont deux transcriptions egalement justes
           et ne rendent pas le meme flottant. **D'' est donc deplace
           entre PLUMES.**
```

**LES DEUX EFFETS SONT ORTHOGONAUX** -- l'un separe les machines,
l'autre les plumes -- **et le regime que 7 (i) decrit les CUMULE** :
"transcrit deux fois, independamment" veut dire deux plumes, et deux
plumes vivent sur deux machines. La borne unique 2 couvre les trois
regimes et leur cumul.

=======================================================================
3. LA MESURE -- ET SA PORTEE, DANS LA MEME PHRASE
=======================================================================

```
    REGIME                          x''                D''
    meme machine, deux plumes    432 ec., max 2     801 ec., max 2
    deux machines, meme plume     27 ec., max 2       0 ec., max 0
    **deux machines ET deux      427 ec., max 2     801 ec., max 2
      plumes -- le CUMUL**
```

Sur **4096 points declares** (tirage `default_rng(20260826)`,
`uniform(-2, 2)`), **deux plates-formes** (Linux, Windows), **deux
plumes** independantes, **les trois regimes**, et la ligne
inter-machines mesuree **des deux bords, par deux instruments
distincts**.

**BORNE MESUREE, NON PROUVEE. Elle se declare telle.** Aucune
majoration analytique n'est offerte ici : ni l'erreur de `pow`, ni
celle de la re-association, n'est bornee par une demonstration dans ce
texte. Ce qui est ecrit, c'est ce qui a ete mesure, avec l'etendue
exacte de la mesure. **Une borne dont on tait la portee se fait
reprendre pour une borne generale, et c'est exactement ce qui s'est
produit une fois dans cette campagne** : une mesure faite sur UNE
machine a ete lue comme valant ENTRE machines, et la garde qu'elle
fondait a rendu un faux echec a sa premiere utilisation reelle.

=======================================================================
4. LE COMPTEUR -- IL FAIT PARTIE DE LA CLAUSE
=======================================================================

L'ecart se compte en **PAS REPRESENTABLES** entre les deux flottants
(distance sur la representation entiere, et somme des deux distances a
zero si les signes different).

**Il ne se compte PAS comme une fraction de `ulp(max(|a|, |b|))`** :
au bord bas d'une binade, cette forme SOUS-COMPTE d'un facteur 2 --
quatre pas representables sous 1.0 s'y lisent 2.00 et passeraient une
borne de 2. La forme est permissive, jamais faussement mordante ; le
defaut est donc silencieux, ce qui est la pire espece.

*(Sur les champs de cette campagne l'ecart etait hors d'atteinte : la
valeur la plus proche d'une frontiere de binade en est a 3.65 x 10^11
pas. Le compteur est fixe ici non pour ecarter un risque mesure, mais
pour que **deux instruments qui doivent coincider comptent avec la
meme regle, bords compris**.)*

=======================================================================
5. CE QUE CET ERRATUM LAISSE OUVERT, ET LE DECLARE
=======================================================================

**`x ** 3` n'est pas touche.** Le remplacer par `x*x*x` rendrait le
champ bit-reproductible entre machines et permettrait `x'' = 0`. Mais
il DEPLACE les nombres de T-1b et de T-2 -- c'est une question de GEL
d'un autre ordre, qui rouvrirait des mesures deja certifiees, et elle
ne se tranche pas dans un erratum de tolerance. **Elle est nommee ici
pour qu'elle ne se perde pas, et elle reste OUVERTE.**

**Ce que la clause ne garantit toujours pas.** Deux transcriptions qui
concordent a 2 ulp sont CONCORDANTES, pas FIDELES : 7 (iv) tient
inchangee -- machine 1 n'a pas l'article, la fidelite repose sur la
seule machine 2, et le gel le declare au lieu de le masquer. **Cet
erratum rend 7 (i) VERIFIABLE ; il ne la rend pas suffisante.**

=======================================================================
6. CE QUI CHANGE, ET CE QUI NE CHANGE PAS
=======================================================================

```
    CHANGE   : 7 (i) porte sa tolerance, son compteur, sa portee, et
               dit ou sa morsure mene (8, BANC NON JOUE).
    NE CHANGE PAS : le reglage ; T-1, T-1b, T-2, T-3 ; 5.4 et le
               plancher de composition ; le perimetre 9bis et ses
               exemptions ; 7 (ii), (iii), (iv) ; 8 ; tout verdict
               deja rendu. Aucun run n'est a rejouer.
    L'EMPREINTE DU GEL RESTE a2e7ef3e237c5acf : cet erratum se cite
               a cote, il ne s'y substitue pas.
```

-- FIN erratum_temoin_v11_clause_7i_tolerance_v1 --
