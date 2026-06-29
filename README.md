# Espace de recherche académique

Cet espace est configuré pour la **recherche académique assistée par IA** (Academic Research Skills, ARS v3.13.0). Vous n'avez besoin d'écrire aucun code : décrivez simplement ce que vous voulez faire et l'assistant s'en charge.

> **Vos préférences** : réponses en **français**, articles rédigés en **anglais**, sorties au format **LaTeX et Word** (au choix à chaque fois).

## Comment démarrer

Dites simplement, en langage naturel :

- « Je veux écrire un article sur _[sujet]_ » → planification de l'article
- « Fais une revue de littérature sur _[thème]_ » → recherche bibliographique
- « Rédige un article complet sur _[sujet]_ » → rédaction de bout en bout
- « Évalue cet article » (+ votre texte) → relecture simulée par des pairs
- « Aide-moi à répondre aux relecteurs » (+ leurs commentaires) → révision
- « Convertis mon article en Word » / « génère le LaTeX de mon article » → export

Des commandes existent aussi (ex. `/ars-plan`, `/ars-full`, `/ars-lit-review`, `/ars-reviewer`).

## Les dossiers

| Dossier | À quoi il sert |
|---------|----------------|
| `articles/` | Vos manuscrits en cours de rédaction. |
| `data/raw/` | Données brutes, **à ne jamais modifier** (sources d'origine). |
| `data/processed/` | Données nettoyées et prêtes à l'analyse. |
| `code/` | Vos scripts d'analyse (R, Python, etc.). |
| `figures/` | Graphiques et illustrations. |
| `figures/svg/` | Versions vectorielles `.svg` — qualité publication. |
| `figures/png/` | Versions bitmap `.png` (300 dpi min) — pour Word et le web. |
| `references/` | Vos fichiers `.bib` et PDF d'articles. |
| `outputs/latex/` | Fichiers `.tex` et `.bib` prêts pour Overleaf. |
| `outputs/word/` | Fichiers `.docx` pour Word. |
| `outputs/submitted/` | Versions soumises aux revues (archive). |
| `lab/` | Cahier de laboratoire et journal de bord (tenus à jour automatiquement). |
| `.claude/` | Le système ARS lui-même (skills, commandes, modèles). À ne pas modifier. |

## Cahier de laboratoire

Le dossier `lab/` garde la trace de votre recherche, mis à jour automatiquement :

- « Montre-moi mon cahier de labo » → affiche `lab/lab_notebook.md`
- « Montre-moi mon journal de bord » → affiche `lab/prompt_log.md`
- « Fais une synthèse de ma recherche » → résumé à partir du cahier

## Export vers Overleaf (LaTeX)

1. Les fichiers de départ sont dans `outputs/latex/`.
2. Sur [overleaf.com](https://overleaf.com) → **Nouveau projet** → importez `overleaf_starter.tex` et `exemple.bib`.
3. Cliquez **Recompile** : votre PDF apparaît.

## Export en Word

Dites « Convertis mon article en Word » : le fichier `.docx` apparaît dans `outputs/word/`.
