# Jeu-de-roulette-europ-en
# Jeu de Roulette – Python

Ce projet propose une simulation simple d’un jeu de roulette en ligne de commande. Le joueur commence avec une somme initiale et peut choisir parmi trois stratégies de mise : **Couleur**, **Chiffres** ou **Mixte**. Chaque tour génère un tirage aléatoire et met à jour le solde du joueur en fonction du résultat.

## Fonctionnalités

- Gestion des couleurs (rouge, noir, vert) avec rendu ANSI dans le terminal.
- Trois types de stratégie :
  - **Couleur** : miser uniquement sur rouge ou noir.
  - **Chiffres** : miser sur un ou plusieurs numéros.
  - **Mixte** : combinaison d’une mise couleur et de numéros.
- Vérification des mises selon le solde disponible.
- Affichage du résultat du tirage et mise à jour automatique du solde.
- Boucle de jeu jusqu’à ce que le joueur n’ait plus d’argent.

## Prérequis

- Python 3.x
- Aucun module externe requis (utilise uniquement `random`, `time`, `os`).

## Installation et exécution

```bash
git clone https://github.com/maitre-oda/Jeu-de-roulette-europ-en.git
cd jeu_roulette.py
python jeu_roulette.py
```

## Structure du fichier

- `jeu_roulette.py` : script principal contenant l’ensemble de la logique du jeu.

## Améliorations possibles

- Ajout d’un menu graphique (TKinter ou autre).
- Système d’historique des tirages.
- Gestion d’un mode « casino » avec limites de mises ou bonus.
- Ajout de tests unitaires.

## Licence

Projet libre d’utilisation et de modification.
