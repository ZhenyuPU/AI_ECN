---
title: TP_Final
auther: Zhenyu PU
date: 27 octobre
numbersections: true
highlight-style: "tango"
papersize: a4
header-includes:
geometry:
- top=30mm
- left=20mm
- right=20mm
- heightrounded
---

## Explication des fichiers dans un package compressé

Le dossier `Mandelbrot_Julia_Plot` est une bibliothèque de modules, qui inclut le code pour le dessin des jeux de points Mandelbrot et Julia. L'explication du code se trouve dans le fichier `.ipynb`.

Le dossier `doc`stocke les documents automatisés. Vous pouvez saisir `make html` sur la ligne de commande via `PAPY/TP_Final/doc/` pour ouvrir la page Web.

Les fichiers `.bat` et `.sh` sont créés pour définir des alias de fonction dans les modules pour les systèmes Windows et Linux respectivement.

Le fichier `setup` est créé pour une implémentation réussie de `pip install .`.

Pour plus d'informations sur le document, veuillez lire le fichier `doc/source/README.rst` ou ouvrir la page Web pour l'afficher.