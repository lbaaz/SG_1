# Revue pré-envoi de la note unifiée 2026-08-10b — findings consolidés

Revue indépendante (machine 2, 2026-08-10), à la demande de baaz, avant envoi à A. Held.
Périmètre : la note `note_outreach_EN_unified_2026-08-10b (1).md`, le dépôt public
`github.com/lbaaz/SG_1` au tag `bundle-v1-held` (clone frais, contre-vérifié), les artefacts
locaux BOCAL4, la littérature en ligne. Posture : referee hostile, aucun crédit accordé aux
deltas ni au protocole.

**Verdict global : le fond tient. Aucun chiffre recomputable ne s'est révélé faux dans les
artefacts. Mais la note ne doit PAS partir en l'état : 4 bloquants pratiques, 2 coquilles
factuelles, 2 reformulations théoriques prudentes, et des décisions de consignation côté dépôt.**

---

## A. BLOQUANTS (avant tout envoi)

- [ ] **A1 — Placeholders non remplis.** La note contient encore `[YOUR NAME]`,
  `[your.email@example.com]`, `[GITHUB LINK]`. Telle quelle, le destinataire ne peut pas
  trouver le dépôt.
- [ ] **A2 — Pied de page interne présent.** « *PROPOSAL, for review by Baaz (machine 2)…
  before any circulation. Intended first recipient: A. Held (ENS), then Deffayet, Vikman,
  Pisa* » + le bloc de notes de révision. Révèle la liste de circulation complète au premier
  destinataire et étiquette le document non-approuvé. Supprimer intégralement.
- [ ] **A3 — Dépôt privé.** `lbaaz/SG_1` est privé (consigné, note de coupe §3). Rendre
  public ou inviter le destinataire avant l'envoi, sinon lien mort.
- [ ] **A4 — PDF à régénérer** après corrections. Polices CID, contenu non vérifiable
  directement ; à traiter comme contenant le même pied de page que le .md.

Nota : la copie de la note DANS le dépôt est verrouillée par hash (`ede00d94…`, 53439 octets,
au registre de coupe, vérifié). Corriger la note du mail sans toucher au dépôt est cohérent
(le mail précise que la version bundle est l'archive figée). Corriger aussi la copie du dépôt
= bundle v2 (décision de protocole).

---

## B. ERREURS FACTUELLES DANS LA NOTE (corrections exactes)

- [ ] **B1 — §3(d) « mode energies grow ×500 » : FAUX.** Ce sont les **amplitudes** (×458
  mesuré, instrumenté sur le runaway (1, 1.05) du bundle). Les énergies croissent ×2.1×10⁵.
  La note FR d'origine disait « les amplitudes ×500 » ; la traduction EN a glissé.
  → Correction : "mode **amplitudes** grow ×500".
- [ ] **B2 — §5(a) « extrapolating 1/Γ_st = 1.8×10⁵ predicts P(2×10⁴) = 0.82 » :
  INCOHÉRENT.** 1.8×10⁵ (= 1/5.6e−6, taux reimplementation) donne exp(−2e4/1.8e5) = 0.895.
  C'est 1/Γ = 1.02×10⁵ (taux bundle 9.8e−6, celui de la table juste au-dessus) qui donne
  0.822. Bug hérité verbatim du journal bundle-5 (§1). → Correction recommandée :
  "extrapolating 1/Γ_st ≈ 1.0×10⁵ predicts P(2×10⁴) = 0.82" (cohérent avec la table).
- [ ] **B3 — §5(e) Γ₀ ≈ 1.4×10⁻⁶ puis Γ₀ = 1.6×10⁻⁶ deux phrases plus loin.** Résolu dans
  les données (`tir1_plancher`) : même estimateur, deux états sondes — 1.4157e−6 = cohérent
  s=0.15 ; 1.6206e−6 = Fock |0,0⟩ (ancre du cut en g de tir2). → Attribuer chacun :
  "coherent-probe floor ≈1.4×10⁻⁶; Fock-ground-state value 1.6×10⁻⁶, the anchor of the g-cut".
- [ ] **B4 — §2.1 « exciting the two modes with amplitudes A₁ = 3s, A₂ = −2s » : vrai
  seulement à Δ = ω₂²−ω₁² = 1, c.-à-d. (1, √2).** Sur les grilles en ω₂ de §2.1, c'est faux
  tel quel — et §3(a) écrit correctement A₂ = −2s/Δ. → Donner la forme générale
  (A₂ = −2s/Δ, A₁ = s − A₂) ou scoper « at the main system (1, √2) ».
- [ ] **B5 — §4.6(iv) « M12 and M13b scripts a month apart » : contredit les artefacts.**
  Horodatages : M12 2026-08-01T23:52Z, M13b 2026-08-02T15:12Z → ~15 heures. (Si l'intention
  était la lignée du moteur M9 de juillet, aucune preuve datée dans le clone.) → Reformuler.
- [ ] **B6 — §4.1 « 13 catalog-registered points in [1.73, 2.82] » :** les points mesurés
  s'arrêtent à 2.80 ; 2.82 est le bord de la fenêtre déclarée du gel. → "within the declared
  window [1.73, 2.82]" ou "[1.73, 2.80]".
- [ ] **B7 — §8 logistique :** « ≈ 1.1 MB » → le bundle public fait **1 294 240 octets ≈
  1.3 MB** (le manifeste quartique consigne lui-même l'écart) ; « ~14 min » = re-runs
  bundles 1–2 de l'auteur, le run externe n°3 du pipeline complet (20 étapes) a pris
  **24 min**. → Scoper : "14–24 min depending on machine; ≈1.3 MB".
- [ ] **B8 — §4.4 résidu « +0.0188 » sous-spécifié :** c'est en **ln s\*** contre la corde
  des voisins (2.89, 3.06) ; en s\* brut c'est +0.160. Irréproductible sans le préciser.
  → Ajouter "(in ln s\*, against the neighbour chord)".
- [ ] **B9 — §5(a) prose de source reimplementation non marquée :** le diagnostic de forme
  (0.994 mesuré, ratios de pente 1/50–1/100, plateau ×1.5–4 de N=48→64) vient du journal
  bundle-5 (reimplementation), or le contrat du préambule ne marque que les *tables*.
  → Ajouter le marqueur *(reimplementation)* à ce passage.

---

## C. REFORMULATIONS THÉORIQUES (objections prévisibles d'un référé)

- [ ] **C1 — K = g·s\*² est EXACT par changement d'échelle, pas une découverte.**
  x → s·y transforme l'EOM en y⁗ + … = (g s²)·y³ : la dynamique ne dépend que de g·s²,
  identiquement (idem K = g·s^{p−2} à tout degré). La note le sait (§6.2 : "elementary and
  not claimed") mais **l'abstract et §3(a) le présentent comme un résultat** ("we find: an
  invariant K = g·s\*²" ; exposant mesuré −0.47…−0.50). → Reformuler : invariance exacte par
  scaling ; la mesure de l'exposant est un contrôle du pipeline (l'écart à −0.5 = résolution
  de grille), pas une loi empirique.
- [ ] **C2 — Homogénéité dimensionnelle des lois.** [K] ~ ω⁴ mais (ω₂−ω₁)²(ω₁+ω₂) ~ ω³ ;
  « g·A₂\*² = 1/(ω₁+ω₂) » est pire. Tout est cohérent en unités ω₁ = 1, mais ce n'est pas dit
  là où les lois sont énoncées, et l'exposant de ω₁ n'est PAS contraint par les données
  (ω₁ = 1 partout, seuls des ratios ω₂/ω₁ ont été balayés). → Une ligne : "in units ω₁ = 1;
  the ω₁ power needed to homogenize the law is unconstrained by our data."
- [ ] **C3 — Objection « NULL+ trivial »** (« évidemment qu'un système borné n'a pas de poids
  à haute occupation — la séparation ×10¹² est de l'énergétique, pas une surprise »). La
  parade est déjà dans le texte (le contrôle fixe le *critère* du census et prouve que
  l'instrument détecte le binding quand il existe) ; une demi-phrase frontale la renforcerait.
- [ ] **C4 — Réf [12] fourre-tout :** cinq références sans rapport (Bender–Mannheim, Pais–
  Uhlenbeck, Avendaño-Camacho, Deffayet PRL, Deffayet JCAP) sous un seul numéro, citées en
  texte pour des choses différentes. → Éclater en références individuelles.
  Idem [17] : deux arXiv nus sans auteurs ; compléter ou retirer.

---

## D. CÔTÉ DÉPÔT PUBLIC (décisions)

- [ ] **D1 — Hash `641dbe3e` (clôture canonique m13L) cité en §2.3 : aucun fichier ne le
  porte, et la recette publique de rejeu est FAUSSE.** Le delta 59 (R-6) dit CRLF→LF de
  `a38b8967` → `641dbe3e` ; le calcul réel donne `15efb410` (l'étape de normalisation des
  labels n'est pas shippée ; delta 49 consigne d'ailleurs `15efb410` comme hash LF). Un
  lecteur qui trace ce hash tombe sur le « Si different : STOP » de R-6 lui-même.
  → Options : (i) ne citer que `a38b8967` dans la note ; (ii) shipper le script de
  canonisation ; (iii) erratum delta 59. Minimum pour l'envoi : (i).
- [ ] **D2 — « baaz » dans 4 fichiers publics** (delta 59 l.72, delta 60 l.95, registre de
  coupe l.100-101, en-tête du manifeste quartique l.2) alors que la note est anonymisée et le
  git pseudonyme (`Baaz`, noreply). Prénom seul, pas de nom/email/chemins. → Décision :
  signer la note (l'écart disparaît) ou purger (= bundle v2).
- [ ] **D3 — README « journal/ integral deltas 1..60 » inexact :** le journal maître couvrant
  §17/§17-bis/E15 (`journal_bundle5_v2026-07-25j.md`), cité comme état de référence par
  `journal_delta_19-20_E16-E17.md:6`, n'est pas dans le dépôt (les bundle5 shippés s'arrêtent
  à §16). → Adoucir « integral » ou ajouter le fichier (v2).
- [ ] **D4 — Chiffres hors-échantillon de §4.2 invérifiables publiquement :** « 5/5 »,
  « minimum at exactly 2.00 », « ×41 », « 0.004 vs 0.49–0.80 », « ~0.61 » tracent vers
  `note_derivation_P1_signes_E_v5.md` et les balayages M5/M6 archivés — présents dans BOCAL4,
  absents du clone. Idem scripts de mesure M13 (`1cb38518`), M13b (`536c897b`), M14
  (`a43d046d`) : hashés dans les JSON, non shippés. → Soit les ajouter (v2), soit marquer ces
  chiffres "archived sweeps, available on request" dans la note.
- [ ] **D5 — Seconde base de code (reimplementation) non shippée** — seuls ses journaux le
  sont. §8 promet "Code, data, journals". → Une phrase en §8 : "the reimplementation codebase
  is documented in journal/… and available on request; the bundle ships the primary pipeline."
- [ ] **D6 — README racine, deux lignes à ajouter :** (i) vérifier le second manifeste
  *depuis* `quartic-bundle/` (lancé à la racine : 2 FAIL parasites LICENSE/README + 55
  "not found") ; (ii) bannière de supersession — `README_EN.md` du bundle quartique affirme
  encore "truncation-converged rates", claim que la note unifiée retire sous mi-île
  (§5(b)(i)) ; un lecteur hostile peut citer l'ancien claim.
- [ ] **D7 — Cosmétique :** `build64.py` / `bocal_g_build72.py` / `k3_build.py` codent en dur
  D=1.0 (exact à (1,√2) seulement) — un commentaire éviterait de mordre un ré-utilisateur à
  autre ω₂ ; README_EN "PDF to be generated at repo creation" périmé ; une ligne README
  signalant que journal/gels sont en français.

---

## E. LITTÉRATURE

- [ ] **E1 — Papier manqué par la revue §6.2 :** Wysong, Overvaag, Lim, Kimn, *Numerical
  Investigations of Stable Dynamics in the Presence of Ghosts*, arXiv:2604.25635 (28 avril
  2026, v2 11 mai). Champs scalaires fantômes 1+1/2+1, éléments finis espace-temps, stabilité
  dépendant de l'amplitude et du contenu spectral, régimes métastables transitoires en φ⁶.
  **Ne recoupe aucun claim de la note** (pas de PU, pas de cartes s\*, pas de rationnels, pas
  de quantique) mais c'est exactement le genre adjacent que Held attendra en §6. → Une ligne
  dans les "adjacent works".
- **E2 — Vérifiées exactes en ligne :** [5] arXiv:2604.21826 (auteurs + titre conformes,
  soumis 23/04/2026) ; Held bien à l'ENS (LPENS, chaire junior Philippe Meyer) ; [10]
  Boulanger et al. EPJC 2019 ; [13] arXiv:2509.18049 (Held seul, stabilité globale,
  interactions polynomiales — usage conforme) ; [14] arXiv:2504.11437 (auteurs conformes) ;
  JCAP 11 (2023) 031 = arXiv:2305.09631 conforme. NB : la page arXiv de [14] n'affiche pas
  la réf. journal PRD 112 065011 — à re-vérifier avant envoi.

---

## F. CE QUI A ÉTÉ VÉRIFIÉ ET QUI TIENT (contre-vérification hostile, exhaustif)

**Intégrité dépôt** : MANIFEST 180/180 OK sur clone frais ; empreinte du manifeste =
`88ed9158…d09c5a` exacte ; manifeste quartique 57/57 OK ; 18/19 hashes cités en §2.3 tracent
et vérifient (seul `641dbe3e` → D1) ; git author pseudonyme ; aucune fuite chemins/emails ;
licences cohérentes (CC BY 4.0 / MIT collectif) ; spot-checks registre (`cf9cc484`,
`8081a032`, `ede00d94`) OK.

**§4 recomputé depuis les s\* bruts** (pas les champs E stockés ; accord < 1e−12) :
annihilateur (−9/4, 5/4) unique ✓ ; M12 : 13 points, 11 évaluables, pertes {7|2.38, 7|2.67},
min −0.48334 à 2.55, max +1.01568 à 1.86, |E| ≥ 0.147 partout ✓ ; M14 : les 7 E de la table
exacts, 39/36 comptes, perte unique 5|2.50|−1 à 0.79038·s\* (fine vide), 7 verrous
bit-identiques (E(2.55) = −0.4833354897982503 bit à bit M12↔M14), portes 2398.20× /
37151.58× / 16994.5× / 1429.1× ✓ ; M13/M13b/M13-L : listes morts/vivants exactes, 11
survivants strictement monotones, 22 recherches, résidu ln +0.01880 à 3.02, borne D ≲ 0.08
(facteurs 6.1–34) ✓ ; M15 : 6 points, 5 tués (fine), survivant 2.62, E = +0.502239 recomputé,
k=0/n_eff=24/k_min=3, puissance ~40 % verbatim dans la cert ✓ ; plateau E recomputé :
2.60 : +0.5554, 2.62 : +0.5022, 2.72 : +0.5174, 2.75 : +0.5251, 2.78 : +0.5193,
2.80 : +0.5426 ✓ ; règle de sélection : 15/15 cases + p=6→(1,2) par force brute ✓ ;
« coarse vide p=4 » : 47/47 recomputé ✓ ; 2.78 bit-identique M12↔M13b ✓.

**§3/§5 tracés au bundle** : s\*=1.27 (1,√2) ✓ ; C = 0.2718 ± 0.0349 sur exactement 17
points de bord (recomputé avec le masque kill_k6) ✓ ; 8.100/9.578 à 2.85/3.00, égaux à
g=0.15 (5.14/5.14) ✓ ; s\*(0)=0.70 et K₀=0.0245 (re-run live de bocal_normale.py) ✓ ;
flagship 0.996 de la forme 1/4 ✓ ; table Γ_st 9 entrées ✓ ; t_blow 54/25/52/14 (ré-intégré) ✓ ;
chaîne ħ ×16.0/×26.5 à g·s²=0.0245 exact ✓ ; indépendance de coquille ×1.54–1.59 ✓ ; taper
0.782/0.910 ✓ ; amputation +1.4 % ✓ ; squeezing ×1.36–5.59 ✓ ; Fock ×3.32/×31.0 ✓ ;
exclusions §5(e) ×1083/×55/×8.3 ✓ ; chaîne Γ₀ 1.62e−6→1.02e−9→2.88e−15, c = ln(1600)/20 =
0.369 ✓ ; tables reimplementation de §5(a′)/(c) : chiffre à chiffre conformes au journal
bundle-5 ✓.

**Théorie redérivée indépendamment** : forme normale 1:1 → coefficient (3g/2)|κ₁ᾱ+κ₂β|⁴
exact, conjugaison sur le mode fantôme correcte, M = J_A−J_B conservé par les termes de
paires ✓ ; mode BAS d'énergie négative (dérivé de l'Ostrogradsky, E₁ = −½A²ω₁²Δ) ✓ ;
κᵢ = 1/√(2Δωᵢ) et ⟨H₀⟩ = E_class à Δ=1 ✓ ; tuple Ostrogradsky (s,0,0,s) ↔ jet (s,0,s,0) ✓ ;
balance dominante α = 4/(p−2), A par α(α+1)(α+2)(α+3) = g·A^{p−2} ✓ ; ħ⁴⁻⁵ (2⁴/2^4.75) et
×256 attendu pour e^{−S/ħ} ✓ ; |δ₇|/|δ₅| < 9/5 et |δ₅|/|δ₇| < 5/9 exacts ✓ ; n₁ = 9s²/2 =
7.26 à s=1.27 ✓ ; coquille 35–45 = 891 états ✓ ; 190 niveaux distincts à ω₂=2, N=64 ✓ ;
σ de C (+0.6/+0.9/+1.7/+2.7) ✓ ; ε_c = croisement K₀/loi (0.216) ✓ ; médiane census
×4.7e12 (« twelve to thirteen orders ») ✓.

---

## G. ORDRE D'ATTAQUE PROPOSÉ

1. A1–A2 (note du mail : identité, lien, purge du pied de page) + B1–B9 (mêmes fichier).
2. Décisions D1 (recommandé : ne citer que `a38b8967`) et D2 (signature vs purge).
3. A3 (visibilité du dépôt) — et si v2 du bundle : D3–D6 dans la même coupe.
4. E1 + C1–C2 (une phrase chacun) ; C4 si le temps.
5. A4 : régénérer le PDF depuis le .md corrigé ; relire le rendu.
6. Envoi.

=== FIN DE LA REVUE PRÉ-ENVOI (machine 2, v1) ===
