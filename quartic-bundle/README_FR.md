# Le fantôme en bocal — paquet de reproductibilité (19/07/2026)

Campagne : PU en interaction, classique + quantique. Résultats et contexte : note_bocal_2026-07-19.md (avec erratum du même jour sur le positionnement Damour-Smilga).

## Environnement
python3, numpy, scipy, sympy, matplotlib. Aucune graine aléatoire (dynamique déterministe, RK4 pas fixe).

## Ordre de reproduction (temps indicatifs sur conteneur standard)
1. pu_test.py — bénin/malin de base, (1,√2), grilles g et s. (~2 min)
2. bocal_dictionnaire.py — dictionnaire linéaire PU↔dimère PT (sympy) + théorème RWA. (~1 min)
3. bocal_phases.py — cartes de phase PU générique / PU 3:1 / dimère Kerr. ATTENTION : le scan (1,3) y est confondu en raideur — corrigé par le suivant. (~5 min)
4. bocal_ab.py — test A/B à raideur appariée (4 systèmes) → bocal_ab_data.npz, figure bocal_ab.png. (~8 min)
5. bocal_critere.py — décalages multi-échelles (répulsion), vérification FFT, loi K=g·s*², prédictions hors échantillon. Lit bocal_ab_data.npz. (~10 min)
6. bocal_paysage.py — paysage s*(ω₂), théorème de parité en contexte → bocal_paysage.npz, figure bocal_critere.png. (~4 min)
7. bocal_normale.py — forme normale 1:1, vallée d'invisibilité (vérif E₁/E₂ et ρ), plateau K₀(ε). (~6 min)
8. bocal_q_build.py puis bocal_q_run.py puis bocal_q_salvage.py — quantique : construction/diag (N=44,36 puis 64,52), évolutions, contrôle de troncature. Les caches propres bq_*.npz (lourds, ~30 s à régénérer chacun) ne sont PAS inclus. Figure bocal_quantum.png. (~5 min)
9. bocal_g_build72.py puis bocal_g_run.py — taux de fuite Γ(s), leviers N=44/64/72, ansatz. (bocal_gamma.py = version monolithique qui dépasse les timeouts : conservée pour référence.) → bocal_gamma.npz. (~3 min)

## Réserves à garder en tête (détaillées dans la note)
- Classique : T=400, une famille de CI (s,0,0,s), frontières ±1 cellule ; C=0.254 empirique.
- Quantique : un système (1,√2), g=0.05, ħ=1 ; « fuite » = flux à travers n=34, convergé entre N=64 et 72 (ratios 0.89–1.09) ; continuum = extrapolation ; fenêtres de fit invalides pour s≥1.3 ; forme de Γ(s) non tranchée [MISE A JOUR bundle 3 : tranchee par les tirs 1-2, voir addendum — plancher + exces, pas de loi unique].
- Porte de lecture restante avant toute rédaction : section quantique de Smilga, arXiv:1710.11538.

## Addendum kill (meme soir)
kill_k1.py (K1a temps long + K1b bord mobile), k2_run.py (K2 mur vs capuchon), k3_build.py+k3_run.py (K3 chaine hbar a point classique fixe, caches bq72_g* regenerables ~30s chacun). Donnees : kill_k*.npz. Verdicts dans note_bocal (sec. 4bis).

## Addendum K4 (meme soir)
kill_k4.py : familles d'etats (coupes au rivage, comprimes, Fock) + recensement spectral des etats lies. Verdict : survecu, fuite structurelle (0 etat propre lie dans l'ile). Donnees : kill_k4.npz. Note v2 mise a jour (sec. 4).

## Addendum K5-K6 (meme soir, tard)
kill_k6.py : taux uniformes immunises au front (bord adaptatif + survie insulaire) + re-fit de C. Verdicts : K6 repare (monotone ; quantique plus lent que classique au-dela du seuil), C=0.272+/-0.035 (1/4 candidat). K5 : revue 2408.16832 = complement ; GSTZ 2007.05541 lu en integralite = blessure conceptuelle et repositionnement, voir note sec. 9.

## Erratum d'empaquetage (attrape par verification externe -- premiere execution de la porte 1)
pu_test.py et pu_plot.py manquaient du tarball : la copie originale utilisait '2>/dev/null' et les fichiers de la premiere session avaient disparu du repertoire ephemere avant l'empaquetage. Sources originales irrecuperables (transcripts verifies) : les deux scripts sont des RECONSTRUCTIONS du meme jour, en miroir exact du systeme canonique de bocal_ab.py, validees contre les ancres archivees (s* dans (1.25,1.30] ; t_blow(1.30)=111 ; t_blow(1.50)=17 -- reproduites). Au passage, la ligne de CI de la note outreach ((x,x',x'',x''')(0)) etait erronee et a ete corrigee : le jet correct est (s,0,s,0), tuple canonique (s,0,0,s). Lecon gravee : plus jamais de cp silencieux ; l'empaquetage est desormais verifie fichier par fichier.

Addendum a l'erratum : en cascade, la colonne classique de kill_k6 (tclas) lisait bocal_ab_data au plus proche voisin (g=0.0516, s=1.333/1.533) en zone frontaliere fractale ; corrigee par integration directe aux vrais points (t_blow(0.05; 1.3/1.4/1.5/1.6) = 54/25/52/14). Notes FR et EN mises a jour ; le claim 'quantique plus lent au-dela du seuil' en sort renforce (x4 a x14) avec une observation neuve : la duree de vie quantique est lisse la ou le classique fluctue (frontiere criblee).

## Addendum tirs 1-2 (forme de Gamma tranchee)
tir1_gammas/partB2/plancher + tir2_gcut/fin : protocole anti-hallucination G1-G9 (integrite, checksum <H0>=-s^2/2, ancres d'abord, norme, moities, invariance de boite N64/72, deux observables, residu oscillant, predictions pre-enregistrees + exclusion mecanique). Verdicts : les trois formes candidates de Gamma(s) sont EXCLUES comme lois globales ; decouverte d'un plancher Gamma0~1.4e-6 (largeur du cluster fondamental, tau~7e5 ; systematique x2, invariance N marginale 0.58 avouee) regenere par la dynamique (coupe n<=4 : 1.05x) ; le plancher est NON-PERTURBATIF en g (x1590 pour g->g/2 ; g^2 et g^4 morts ; compatible e^{-c/g}, c~0.37 ; borne a g=0.0125) -- premiers points quantitatifs du regime GSTZ, deux mecanismes desormais mesures separement (fondamental non-perturbatif vs iles resonantes hbar^4-5). Deux artefacts fabriques puis executes par le protocole en cours de route (fenetre longue saturee ; fenetre fraction-de-plateau trop tardive) : voir transcript.

## Combles d'empaquetage (run externe #2, verificateur humain)
- build64.py AJOUTE : construit bq_64.npz (requis par k2_run, bocal_g_run, tir1_partB2, tir1_plancher). Invocation : python3 build64.py (~15 s).
- k3_build.py : invocations explicites requises : python3 k3_build.py 0.05 ; 0.025 ; 0.0125 (bq72_g*.npz, ~30 s chacun).
- pu_test.py : etiquette 'ancres' corrigee (111/17 = plus proche voisin g=0.0516 de l'archive ; ancres directes g=0.05 : 54/25/52/14).
Etat de verification : bundles 1 et 2 re-executes integralement par l'auteur humain (~14 min), accord <=5e-10 sauf 5 cellules C/D en zone frontaliere criblee (<=11 pas RK4, ~0.03%, A/B bit-identiques) ; scripts tirs 1-2 posterieurs, re-run humain en attente.

Correctif chemins (attrape par la validation de build64) : tous les scripts du bundle utilisaient des chemins ABSOLUS herites de l'environnement d'origine (/home/claude pour les caches, /mnt/user-data/outputs pour les figures) -- casses hors de cet environnement. Tout est passe en chemins RELATIFS (caches et figures ecrits dans le repertoire courant). Ancre fonctionnelle re-verifiee sur le cache reconstruit (K2 : 7.67e-5 / 1.20e-3 reproduits).

Addendum reformulation : la loi de seuil equivaut a g*A2^2*(w1+w2) = 4C (aveugle au detuning) le long de la famille de CI ; decomposition par bord : droit C=0.269+/-0.011 (le point A/B (1,2.85) tombe a 0.996 de la forme 1/4), gauche limite par resolution (~20-40 pourcent par point, quantification Delta_s=0.2) -- remplace le "5-15 pourcent" global des versions anterieures. Statut mono-rayon des CI promu question centrale ; juge annonce : la frontiere de blow-up dans le plan (A1,A2) complet.

## Bundle 3 (changelog)
- AJOUTES : spotcheck_reformulation.py + .npz (test point par point de la forme equivalente aveugle au detuning ; bord droit C = 0.269 +/- 0.011, point-phare (1, 2.85) a 0.996 de la forme 1/4) ; references tir1_partA.npz et tir2_gcut.npz (retour verificateur, point 0) ; note_outreach_EN_2026-07.md ; requirements.txt ; LICENSE (MIT, nom en placeholder) ; README_EN.md, devenu README.md, EN par defaut (page d'accueil du depot : etapes 15-20, sept figures, resultats de tete a jour des tirs).
- REPARE : tir2_gcut.py etait un vrai bug — il crashait avant son savez (None a g = 0.0125), donc tir2_gcut.npz n'existait pas ; desormais None-robuste, et ne produit plus de figure (la synthese finale appartient a tir2_fin — point 4 du retour).
- COHERENCE : la mention initiale "forme de Gamma(s) non tranchee" est annotee (point 2 du retour) ; les notes FR et EN portent la reformulation et la decomposition par bord.
- REPARE (run externe #3) : compare_worst.py (outil de verification, ajoute avec ce bundle) portait deux faux negatifs : empoisonnement NaN par les cellules inf des grilles t_blow (inf-inf=NaN neutralisait d.max()>0 -> "bit-exact" errone sur bocal_ab_data, l'inverse de sa mission) et crash ValueError sur les archives a dicts (kill_k1 et suivantes, 10 fichiers sur 15 jamais compares). Corrige : motifs inf/NaN compares a part (NaN==NaN via equal_nan), ecarts calcules sur les seules entrees finies, dicts imbriques aplatis en feuilles. Table du run externe #3 (20 etapes, 24 min, zero intervention) : 3 bit-exact, 9 a <=1e-9, 3 a <=1e-6 (quantites plancher comparees en absolu : <=9e-16), pire ecart global 3.49e-4 = tbD cellule frontaliere connue.
