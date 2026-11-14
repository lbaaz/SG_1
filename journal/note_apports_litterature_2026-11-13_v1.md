# Note hors chaîne — antériorité de la largeur quantique d'île, et lecture de Maiezza–Nesti (v1)

Machine 1, 13/11/2026, écrite pendant le run « qualification E-B bis »
(lancé le 13/11 à 00:52 sur BOCAL4). **HORS CHAÎNE, NON OPPOSABLE.** Ne
contient rien du run, n'engage aucun numéro, aucune manche, aucun fait de
chaîne. Suite de `note_apports_litterature_2026-08-10_v1.md`. Les énoncés
ci-dessous sont des lectures machine 1 de la littérature ; toute phrase
promue en chaîne ou envoyée dehors devra être relue sur les sources
primaires (dettes au §6).

**Question posée par l'opérateur.** Si le run bis qualifie l'estimateur,
la campagne tiendra des largeurs Γ intrinsèques (indépendantes de
l'absorbeur) pour des états de l'île du fantôme, avec le jumeau à signe
retourné en contrôle. Un tel nombre existe-t-il déjà ?

## 0. Verdict

**Non trouvé.** Aucune publication repérée ne donne une largeur chiffrée
d'un état posé dans une île de stabilité classique d'un système à fantôme,
ni un contrôle par jumeau, ni un calcul à absorbeur ou à rotation complexe
sur un hamiltonien à cinétique indéfinie. Confiance machine 1 : de l'ordre
de 80 %, plafonnée par la dette INSPIRE (§6.1).

Ce qui existe : l'énoncé qualitatif « l'île fuit par effet tunnel »
(ancien, pas à nous) ; des taux en théorie des champs (autre objet) ; la
méthode « île + absorbeur → taux » en chaos quantique (systèmes à énergie
positive) ; et un voisin immédiat, tout neuf, absent de nos références :
Maiezza & Nesti, arXiv:2610.10040 (8 octobre 2026).

## 1. Fiche de lecture — Maiezza & Nesti, « Can we make sense out of negative kinetic energy? »

Lu en quatre passes d'extraction couvrant toutes les sections et la
bibliographie (44 entrées) ; **pas** le texte brut ligne à ligne (le
conteneur de machine 1 n'atteint pas arXiv). Voir §6.2.

**1.1 Objet.** H = H₁ − H₂ + V, deux oscillateurs de masse unité,
fréquences ω₁ = 1 et ω₂ = √2, quantification standard (espace de Hilbert
ordinaire, états du fantôme de norme positive et d'énergie négative, ni
produit scalaire modifié ni rotation de Wick). Deux couplages :
« petit » V = (λ/2) x²y² e^(−(x²+y²)) et « grand » V = (λ/2) x²y². Le
grand est, à la notation près, le modèle de Gross–Strumia–Teresi–Zirilli
(GSTZ, éq. 56). État suivi : le « would-be ground state », produit des
deux fondamentaux, d'énergie libre nulle. Observable : la probabilité de
survie P(t) = |Σ |c_i|² e^(−iE_i t)|².

**1.2 Méthode.** Diagonalisation complète dans deux régularisations :
(i) réseau, 2n points par direction, conditions de bord nulles, pas
a⁻¹ = C·n^(1/2) avec C = 1,2 (réglé sur le cas libre), stencil d'ordre 4,
jusqu'à n = 120 ; (ii) base libre tronquée n₁ + n₂ ≤ 2n, jusqu'à n ≈ 200.
Évolution unitaire : **aucun absorbeur, aucune rotation complexe, aucune
condition sortante.** Série perturbative de l'énergie de l'état (six
ordres pour le petit potentiel, douze pour le grand, asymptotique).
Volet classique : sections de Poincaré, carte du temps d'explosion
(t_max = 6·10⁴).

**1.3 Résultats (grand potentiel).**

- Temps courts : décroissance quadratique en λt. Puis la survie cesse de
  décroître et oscille, période ≈ 8, croissante avec λ.
- Borne annoncée pour λ < 0,15 : P(t) ≳ 1 − 0,2λ² − 2,1λ³.
- Horizon fiable court : pour λ = 0,2, convergence relative 10⁻⁶ jusqu'à
  t = 2,5, puis t = 10 aux plus grandes troncatures ; bien plus long pour
  λ ≲ 0,1. Les recouvrements c_i ne convergent pas pour λ ≳ 0,05 ; seule
  P(t) converge, par fenêtre de temps.
- Au-delà de λ ≈ 0,2 : tendance à la baisse non résolue des transitoires ;
  comportement irrégulier (oscillations qui reviennent à certaines
  valeurs de λ), attribué à des résonances ou dégénérescences accidentelles
  des matrices finies.
- Pas d'emballement d'énergie : les deux oscillateurs échangent une
  énergie finie.
- Spectre : reste ponctuel dense quand la coupure est levée, avec une
  densité qui croît moins vite que dans le cas libre (exposant γ(λ) < 1).
- Fantôme plus lourd (ω₂ croissant) : P(t) se rapproche de 1.
- Un seul test d'état excité (E₁ ≈ |E₂| ≈ 10, λ = 0,1 et 0,2) : survie
  beaucoup plus basse.
- **Les deux régularisations convergent chacune, vers des limites
  différentes** ; l'écart dépasse les effets de taille finie et grandit
  avec λ. Lecture des auteurs : mélange UV–IR authentique, la
  régularisation fait partie de la définition du modèle.
- Classique : île autour de l'origine, approximativement
  √(λE₁) + √(λE₂/2) < 1 à faible couplage ; explosion systématique pour
  λE₁ ≳ 30 ; motif fractal des temps d'explosion. Le point (1/2, 1/√2)
  de l'état quantique tombe dans l'île pour λ ≲ 0,3.

**1.4 Conclusion des auteurs.** L'état « ne se désintègre pas » sur une
large plage de couplage ; image d'un puits métastable fermé par une
barrière extérieure (le flux sortant rebrousse chemin) plutôt qu'ouvert
sur l'infini ; métastabilité à longue durée de vie, pas stabilité
absolue ; une désintégration à des temps exponentiellement plus longs
reste possible. WKB jugé peu utilisable (action totale nulle pour des
excitations arbitrairement grandes).

**1.5 Ce qui n'y est pas.** Aucun Γ. Aucun contrôle sans fantôme. Pas
d'auto-interaction de Pais-Uhlenbeck (leur couplage est x²y², pas une
puissance de q₁ + q₂). Pas de programme d'états d'île. Aucune étude
antérieure de métastabilité quantique chiffrée n'est citée ; GSTZ est cité
comme « tentative antérieure » sur le grand potentiel.

## 2. Contrôle machine 1 — l'oscillation résiduelle est l'habillage du premier ordre

Lecture machine 1, pas une phrase des auteurs. Script
`controle_MN_habillage_machine1_v1.py` et son journal `.log` (hors chaîne ;
base libre N×N, N = 30 et 40, soit 900 et 1 600 états ; t ∈ [0, 120]).

Au premier ordre, x²y² ne relie |0,0⟩ qu'à trois états :

| état | V/λ | ΔE | \|c\|²/λ² | période 2π/\|ΔE\| |
|---|---|---|---|---|
| (2,0) | 0,12500 | +2 | 0,00391 | 3,14 |
| (0,2) | 0,12500 | −2√2 | 0,00195 | 2,22 |
| (2,2) | 0,17678 | 2 − 2√2 = −0,828 | 0,04553 | 7,58 |

D'où trois prédictions sans paramètre : variance de V égale à λ²/16
(pente à temps court) ; creux de survie 1 − P ≈ 0,194 λ² (± 0,012) ;
battement dominant à la période 2π/(0,828 − 2,121 λ), l'écart (2,2)–(0,0)
étant décalé de (3/√2)λ au premier ordre — soit 7,6 à λ → 0, 8,0 à
λ = 0,02, 8,7 à 0,05, 10,2 à 0,10.

Diagonalisation directe :

| λ | (1−P)/(λ²t²), t = 0,05 | min P sur [0, 120] | borne M–N | période dominante |
|---|---|---|---|---|
| 0,02 | 0,06246 | 0,999910 | 0,999903 | 8,00 |
| 0,05 | 0,06246 | 0,999339 | 0,999238 | 8,57 |
| 0,10 | 0,06246 | 0,99645 (N=30) ; 0,99652 (N=40) | 0,995900 | 10,91 |
| 0,15 | 0,06246 | 0,962 (N=30) ; 0,986 (N=40) — non convergé | 0,988413 | — |

(Périodes lues sur une grille de Fourier 120/k : résolution d'un cran.)

**Lecture.** Pour λ ≤ 0,10, la « non-désintégration à oscillations
résiduelles » de Maiezza–Nesti — profondeur 0,2 λ², période ≈ 8 — est
reproduite avec 900 états et **s'explique entièrement** par le fait que
|0,0⟩ n'est pas état propre : c'est le battement entre le niveau habillé
(0,0) et le niveau (2,2). Leur borne est respectée aux trois couplages
convergés. Conséquences :

1. Cette observable ne dit rien d'une fuite lente. Sur un horizon
   t ~ 10 à 100, une largeur inférieure à ~10⁻³ est invisible ; celles de
   M17 sont de l'ordre de 10⁻¹⁰ à 10⁻⁹, le plancher de juillet de 10⁻⁶ à
   g = 0,05. « Ne se désintègre pas » (eux) et « fuit au taux Γ » (nous)
   ne se contredisent pas : ce ne sont pas les mêmes mesures.
2. L'image « barrière extérieure, rebond sur un mur » n'est pas requise à
   petit λ : le battement perturbatif suffit. Elle reste une hypothèse
   pour λ plus grand, là où leurs deux régularisations divergent.
3. À λ = 0,15 la troncature N = 30 contre N = 40 change le résultat d'un
   facteur 2,7 sur 1 − P : c'est leur constat (c_i non convergés,
   irrégularités de matrices finies), retrouvé.

## 3. Points de contact avec la campagne

- **Mêmes fréquences** (1, √2) que le système principal de la note de
  juillet ; couplage différent. Rien n'est transposable chiffre pour
  chiffre.
- **Survie qui plafonne.** Notre note de juillet disait déjà : la survie
  d'île tombe puis plafonne, 1/Γ_st est une échelle d'échappement initial
  et non une durée de vie, et le plateau n'est pas indépendant de la
  boîte. Maiezza–Nesti voient la même forme et la lisent comme physique.
  Un absorbeur ne tranche pas ce point : il retire le flux sortant, donc
  Γ_LS mesure le **taux sortant**, pas l'irréversibilité dans le système
  fermé. La phrase externe correcte reste celle de juillet : seul le taux
  sortant est revendiqué ; la dynamique éternelle de l'extension
  auto-adjointe est hors revendication.
- **Dépendance au régulateur.** Leur résultat VIII (deux schémas, deux
  limites) est l'objection qu'un lecteur opposera à toute largeur lue sous
  absorbeur. C'est exactement ce que l'étage 2 du gel bis met à l'épreuve
  (formes F1/F2/F3, géométries G20/G30/GT, translation). Si le verdict est
  ESTIMATEUR QUALIFIE ou QUALIFIE PAR POINT, c'est une réponse chiffrée à
  VIII dans notre système ; si NON QUALIFIE, VIII est la lecture externe
  naturelle et doit être citée.
- **États d'île.** Leur unique état excité (E₁ ≈ |E₂| ≈ 10) donne, avec
  leur propre critère approché, √(λE₁) + √(λE₂/2) = 1,71 à λ = 0,1 et
  2,41 à λ = 0,2 : il est **hors de l'île** classique (lecture à
  confirmer, §6.2). Sa chute rapide est donc
  l'emballement classique, pas une fuite d'île. Personne n'a regardé
  d'état d'île autre que l'état quasi fondamental : le programme d'états
  d'île reste propre à la campagne.
- **Spectre dense persistant, exposant γ(λ).** À rapprocher de la piste
  « estimateur spectral » consignée au SUIVI du 09/09 (statistique
  d'espacements, fantôme contre jumeau).

**Option (décision machine 2 et opérateur, non recommandée ici).**
L'instrument E-B, s'il sort qualifié, pourrait être joué sur le
hamiltonien x²y² de GSTZ / Maiezza–Nesti : cela donnerait une largeur sur
un modèle publié deux fois sans nombre. Ce serait un chantier neuf avec
son propre gel ; le garde-fou de la piste (0) (dernier essai, la piste se
ferme) ne s'y prête pas tel quel.

## 4. Antériorité — état après contrôle

**(a) Énoncé qualitatif « l'île n'est pas un refuge quantique ».**
Smilga 2009 (les termes non linéaires amènent le plus souvent effondrement
quantique et perte d'unitarité) ; Ilhan–Kovner 2013 (l'effet tunnel relie
régions stables et instables : non-unitarité) ; Pavšič 2013, 2016 (la
stabilité classique d'île ne survit pas au tunnel) ; GSTZ 2021
(métastabilité « comme une désintégration du vide », suppression
exponentielle argumentée, formule WKB non généralisée, aucun taux) ;
Damour–Smilga 2022 (conjecture limitée aux systèmes globalement bénins,
quantique laissé à plus tard) ; Maiezza–Nesti 2026 (§1). **Pas à nous.**

**(b) Taux en théorie des champs.** Carroll–Hoffman–Trodden 2003 et
Cline–Jeon–Moore 2004 (taux perturbatifs du vide avec coupure violant
Lorentz) ; Emparan–Garriga 2006 (instantons : nucléation non perturbative
de matière fantôme, actions euclidiennes calculées) ; Garriga–Vilenkin
2013 (taux à l'arbre fini en D = 2). Autre objet : vide de théorie des
champs, pas état d'île d'un système à deux degrés de liberté.

**(c) Précédent de méthode.** Le chaos quantique calcule depuis près de
vingt ans des taux d'effet tunnel « île régulière → mer chaotique » en posant des
conditions de bord absorbantes dans la mer (Bäcker, Ketzmerick, Löck,
Schilling, PRL 100 (2008) 104101 ; Löck, Bäcker, Ketzmerick, Schlagheck,
arXiv:0906.4893 : les résonances non linéaires internes à l'île font des
pics et des plateaux dans les taux). Systèmes à énergie positive
(applications pulsées, billards). **La méthode n'est pas à nous ; son
application à un fantôme, à notre connaissance, si.** C'est aussi le
cadre naturel de nos constats de juillet (plancher plus excès résonant,
loi en puissance de ħ plutôt qu'exponentielle, échec de P-A2).

**(d) Fantômes quantiques globalement stables (avril 2026).** Deffayet,
Fathe Jalali, Held, Mukohyama, Vikman (deux lettres) ; Ewasiuk–Profumo.
Ni île, ni tunnel, ni taux ; la métastabilité y tient en une note de bas
de page renvoyant à GSTZ.

**(e) Vus et écartés.** Bateman–Turok, arXiv:2607.00096 (diffusion à
l'arbre en espace de Krein) ; ligne Fring–Taira–Marquette–Felski 2025–2026
(représentations sans fantôme, point résonant) ; Comelli–Di
Giambattista–Pilo 2022 (systèmes gyroscopiques linéaires, résumé seul) ;
théorie quantique de l'instabilité explosive à trois ondes (cas résonant,
résumé seul).

## 5. Ce qui se revendique, et ce qui ne se revendique pas

Sous réserve du verdict du run bis et de la dette INSPIRE :

- **Revendicable, avec « à notre connaissance » :** première largeur
  chiffrée d'un état d'île d'un fantôme auto-interagissant, lue sur un
  palier d'absorbeur, avec témoin positif à largeur connue et jumeau à
  signe retourné.
- **Non revendicable :** « les îles fuient » (§4a) ; la méthode (§4c) ;
  toute phrase de théorie des champs, d'unitarité ou d'auto-adjonction ;
  « durée de vie » sans la réserve du taux sortant (§3).
- **À citer obligatoirement dehors :** GSTZ, Ilhan–Kovner, Pavšič, Smilga
  2009, Damour–Smilga, Deffayet et al. 2026, Maiezza–Nesti, et au moins
  une référence du §4c.

## 6. Dettes

**6.1 Dépouillement INSPIRE — NON FAIT.** L'API d'INSPIRE n'est joignable
ni depuis le conteneur de machine 1 (proxy : 403) ni par l'outil de
lecture web (adresses non fournies refusées) ; le navigateur de
l'opérateur n'était pas connecté. Le contrôle du §4 repose sur une
vingtaine de recherches web et la lecture des pages trouvées. Requêtes à
jouer :

1. citants de GSTZ : `refersto:arxiv:2007.05541`
2. citants du cluster 2026 : `refersto:arxiv:2604.21823 or
   refersto:arxiv:2604.21826 or refersto:arxiv:2604.21348 or
   refersto:arxiv:2610.10040`
3. citants de DMV et DHMV : `refersto:arxiv:2108.06294 or
   refersto:arxiv:2305.09631`
4. citants de Smilga 2009, Ilhan–Kovner, Pavšič, Damour–Smilga :
   `refersto:arxiv:0808.0139 or refersto:arxiv:1301.4879 or
   refersto:arxiv:1302.5257 or refersto:arxiv:2110.11175`
5. titres : `t ghost and t metastable`
6. titres : `t Pais-Uhlenbeck and de >= 2020`

**6.2 Texte brut de Maiezza–Nesti.** À relire sur le PDF : (i) la forme
exacte de la loi à temps court — l'extraction rapporte un coefficient
« A ≃ 14 », alors que la variance de V donne (1 − P) = λ²t²/16 ; (ii) la
phrase de conclusion « P > 99,9 % pour λ < 0,1 », que leur propre borne
(99,59 % à λ = 0,1) et le calcul du §2 (99,65 %) ne donnent que pour
λ ≲ 0,05 ; (iii) les valeurs tabulées de γ(λ) ; (iv) les énergies exactes de l'état
excité et le critère d'île, dont dépend la lecture « hors de l'île » du
§3 (le critère approché place le point fondamental dans l'île jusqu'à
λ ≈ 0,59, les auteurs disent λ ≲ 0,3). Ne rien écrire dehors sur ces
quatre points avant relecture.

**6.3** Bäcker et al. et Löck et al. : à lire en entier contre nos lois
de juillet avant toute phrase sur le mécanisme. Emparan–Garriga et
Garriga–Vilenkin : vus en résumé seulement.

**6.4** Le contrôle du §2 est un calcul machine 1 seul, à 1 600 états au
plus, non rejoué par machine 2.

## 7. Références

- Maiezza, Nesti — arXiv:2610.10040
- Gross, Strumia, Teresi, Zirilli, PRD 103 (2021) 115025 — arXiv:2007.05541
- Ilhan, Kovner, PRD 88 (2013) 044045 — arXiv:1301.4879
- Pavšič, Mod. Phys. Lett. A 28 (2013) 1350165 — arXiv:1302.5257 ;
  arXiv:1607.06589
- Smilga, SIGMA 5 (2009) 017 — arXiv:0808.0139
- Damour, Smilga, PRD 105 (2022) 045018 — arXiv:2110.11175
- Deffayet, Fathe Jalali, Held, Mukohyama, Vikman — arXiv:2604.21823 et
  arXiv:2604.21826
- Ewasiuk, Profumo — arXiv:2604.21348
- Carroll, Hoffman, Trodden — arXiv:astro-ph/0301273
- Cline, Jeon, Moore, PRD 70 (2004) 043543 — arXiv:hep-ph/0311312
- Emparan, Garriga, JHEP 03 (2006) 028 — arXiv:hep-th/0512274
- Garriga, Vilenkin, JCAP 01 (2013) 036 — arXiv:1202.1239
- Bäcker, Ketzmerick, Löck, Schilling, PRL 100 (2008) 104101 —
  arXiv:0707.0217
- Löck, Bäcker, Ketzmerick, Schlagheck — arXiv:0906.4893
- Bäcker, Ketzmerick, Löck — arXiv:1009.0418
- Bateman, Turok — arXiv:2607.00096
- Comelli, Di Giambattista, Pilo, JCAP 11 (2022) 017 — arXiv:2207.02950
