# Journal des prompts — Projet de recherche
> Dernière mise à jour : 2026-06-29

## 2026-06-29 — Installation du système
**Prompt :** Installation et configuration initiale d'ARS v3.13.0
**Résultat :** Système installé, préférences enregistrées (communication : français, articles : anglais, format : LaTeX + Word)
**Fichiers produits :** `.claude/user_preferences.md`, `README.md`, `.gitignore`, structure de projet (`articles/`, `data/`, `code/`, `figures/`, `references/`, `outputs/`, `lab/`), `lab/lab_notebook.md`, `lab/prompt_log.md`, `outputs/latex/overleaf_starter.tex`, `outputs/latex/exemple.bib`, `outputs/word/modele_article.md`, et 616 fichiers du système ARS dans `.claude/`

---

## 2026-06-29 — Test fonctionnel (Étape 7)
**Prompt :** Générer un plan de 3 chapitres pour un article fictif sur « l'impact de l'IA générative sur les pratiques d'évaluation dans l'enseignement supérieur »
**Résultat :** Plan en 3 chapitres rédigé en anglais (langue des articles)
**Fichiers produits :** `articles/test_installation.md`

---

## 2026-06-29 — Lecture du corpus logistique urbaine (5 PDF)
**Prompt :** Lire 5 PDF (diagnostic 2018, foncier logistique 2024, projets IE 2021/2024/2025-26) ; installer poppler si besoin.
**Résultat :** poppler-utils installé ; texte extrait ; synthèse du corpus (fil rouge : décarbonation du dernier km à La Rochelle).
**Fichiers :** lab/ (mises à jour)

## 2026-06-29 — Brouillon extended abstract City Logistics 2027
**Prompt :** Préparer 3 pages pour City Logistics (Faro) sur le siting des lockers et son impact sur le schéma logistique urbain local ; SoA (diagnostics) + expérimentation La Rochelle (projets IE).
**Résultat :** Extended abstract (3 p., anglais) rédigé. Références externes marquées [verify] (intégrité). pandoc installé → DOCX généré.
**Fichiers produits :** articles/citylogistics2027_lockers_larochelle.md, outputs/latex/citylogistics2027_extended_abstract.tex, outputs/word/citylogistics2027_extended_abstract.docx

## 2026-06-29 — Carte des points de collecte (données projet IE 49)
**Prompt :** Zip du code/cartographie lockers ; montrer la carte (ou une plus belle version) dans l'article.
**Résultat :** Données réelles exploitées (148 pts de collecte dont 9 lockers, 1414 arrêts Yélo, population par quartier). Carte de qualité publication générée (SVG + PNG 300 dpi). Coordonnées de lockers « proposés » NON fabriquées (étaient dérivées dans un espace transformé).
**Fichiers produits :** figures/png/larochelle_collection_points.png, figures/svg/larochelle_collection_points.svg, code/make_locker_map.py

## 2026-06-29 — Bascule de la rédaction sur le pipeline ARS
**Prompt :** « Utilise bien les agents et skills du pipeline ARS, notamment pour la rédaction. »
**Résultat :** Extended abstract v2 produit via le pipeline academic-paper (intake → structure → argument → draft → citation_compliance → peer_reviewer → formatter). Titre retravaillé, figure intégrée (md + LaTeX + DOCX), statements ajoutés (Data availability, CRediT, AI disclosure), anti-patterns ARS appliqués, auto-revue 5 dimensions. Références externes [verify], aucun DOI fabriqué.
**Fichiers modifiés :** articles/citylogistics2027_lockers_larochelle.md, outputs/latex/citylogistics2027_extended_abstract.tex, outputs/word/citylogistics2027_extended_abstract.docx (figure embarquée)

---

## 2026-06-29 — Ajout du volet foncier micro-hubs (Figure 2 + texte)
**Prompt :** Cartographie mise à jour avec le foncier compatible micro-hubs (DATA/Parkings.xlsx + notebook) + rapport VerDelivery DOCX ; figure et texte anglais pour la conf.
**Résultat :** 95 parkings classés par compatibilité véhicules (74 surface ≥3 m = candidats micro-hub, 9 conditionnels, 12 ouvrages exclus ; Espace Encan = pilote). Figure 2 générée (SVG+PNG 300 dpi). Article enrichi (abstract, méthode P3, résultats « Land for consolidation », discussion, table) via le pipeline academic-paper. LaTeX + DOCX régénérés (2 figures embarquées).
**Fichiers produits/modifiés :** figures/png|svg/larochelle_microhub_parkings.*, code/make_microhub_map.py, data/raw/Parkings.xlsx, articles/…md, outputs/latex/…tex, outputs/word/…docx

---
*(Les prochains échanges seront ajoutés ici automatiquement)*
