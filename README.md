# 🎰 Jeu de Roulette (Python, terminal)

## 📍 Aperçu
Petit jeu de **roulette** en Python jouable dans le terminal.  
Le joueur démarre avec un **solde initial** et peut parier selon **trois stratégies** : `Couleur`, `Chiffres`, ou `Mixte`.  
Après chaque manche, il peut **rejouer exactement la même mise** (mêmes paramètres) sans tout ressaisir.

---

## 🚀 Lancer le jeu

### Prérequis
- **Python 3.8+**
- Aucune dépendance externe (utilise `random`, `time`, `sys`).

### Exécution
### 🔹 Cloner le dépôt
#### 💻 macOS / Linux
Ouvrez un terminal et exécutez :
```bash
git clone https://github.com/maitre-oda/Jeu-de-roulette-europ-en.git
cd Jeu-de-roulette-europ-en
python3 jeu_roulette_ameliorer.py
```
🪟 Windows :
Ouvrez PowerShell ou CMD, puis exécutez :
```
git clone https://github.com/maitre-oda/Jeu-de-roulette-europ-en.git
cd Jeu-de-roulette-europ-en
py jeu_roulette_ameliorer.py
```
⚠️ Si la commande py ne fonctionne pas, essayez :
```
python jeu_roulette_ameliorer.py
```
---

## 🎮 Règles & Stratégies

### 1️⃣ Stratégie **Couleur**
- Choisissez **rouge** ou **noir**.
- **Gain** si la couleur tirée correspond : `+ mise`
- **Perte** sinon : `- mise`

### 2️⃣ Stratégie **Chiffres**
- Entrez un ou plusieurs **numéros** (entre 0 et 36).
- La **mise** saisie est **par numéro**.
- Si **un de vos numéros sort** :
  - **Gain net** = `(36 - k) × mise`, où `k` = nombre de numéros joués  
    (car vous gagnez `35 × mise` sur le bon numéro et perdez `mise` sur chacun des autres)
- Sinon :
  - **Perte** = `k × mise`

### 3️⃣ Stratégie **Mixte**
- Combinez **Couleur** + **Chiffres**.
- Mises distinctes : `mise_couleur` et `mise_numero` (par numéro).
- Avec `k` numéros, le **gain net** est :
  - Numéro **et** couleur OK : `(36 - k) × mise_numero + mise_couleur`
  - Numéro OK, couleur KO : `(36 - k) × mise_numero - mise_couleur`
  - Numéro KO, couleur OK : `- k × mise_numero + mise_couleur`
  - Numéro KO, couleur KO : `- k × mise_numero - mise_couleur`

> ℹ️ Les tirages affichent aussi la **couleur** tirée. Le **0** est considéré **vert**.

---

## 🔁 Rejouer la même mise
À la fin d’une manche, le programme propose :
```
Voulez-vous rejouer la même chose ? (o/n)
```

- Si vous tapez **`o`**, le tour suivant réutilise automatiquement :
  - **Couleur** : dernière couleur + dernière mise
  - **Chiffres** : liste de numéros + mise par numéro
  - **Mixte** : couleur, liste de numéros, mise couleur + mise par numéro

Le programme vérifie que **votre solde** permet de rejouer **exactement** la même configuration :
- Couleur : `mise ≤ solde`
- Chiffres : `k × mise ≤ solde`
- Mixte : `mise_couleur + k × mise_numero ≤ solde`

Sinon, retour au menu.

### Variables internes utilisées
- `rejouer` (bool) : indique si on répète la même mise au tour suivant  
- `dernier_choix`, `dernier_couleur`, `dernier_mise_couleur`, `dernier_liste_numeros`, `dernier_mise_numero` : mémoires du dernier tour

---

## 🖥️ Affichage & Couleurs
- Les couleurs **ANSI** (rouge/noir/vert) sont utilisées pour le tirage.
- Sur **Windows**, utilisez un terminal compatible ANSI (Windows Terminal, VS Code, ou activez le support ANSI).

---

## 🧩 Validation des entrées
- Saisie sécurisée des **entiers** (mises/numéros)
- **Bornes** vérifiées (numéros `0..36`, mises **> 0**)
- Vérification du **solde disponible** avant validation d’une mise

---

## 🧪 Exemple rapide 
```
Solde actuel : 50
Stratégie : 1 (Couleur)
Rouge ou Noir ? : rouge
Mise sur rouge : 10

Plus rien ne va plus !
Résultat : 23 (rouge)
Bravo ! Vous gagnez 10
Nouveau solde : 60

Rejouer la même chose ? (o/n) : o
Plus rien ne va plus !
Résultat : 8 (noir)
Dommage ! Vous perdez 10
Nouveau solde : 50
```

---

## ⚠️ Limitations connues
- Programme **100% interactif** (pas de mode non interactif / tests automatisés intégrés).
- **Duplication** de logique entre stratégies (volontaire ici pour rester sans fonctions).
- Les gains/pertes reflètent la **roulette européenne** avec **payout 35:1** pour un numéro plein.

---

## 💡 Idées d’amélioration
- Factoriser en **fonctions** (saisie, tirage, calculs par stratégie).
- **Historique** des tours (journal + export `.txt`).
- Paramètres configurables (solde initial, vitesse `sleep`, activer/désactiver ANSI).
- Mode **simulation** (séries de coups auto pour voir l’espérance de gain).

---

## 📄 Licence
Usage libre pour l’apprentissage. Ajoutez une licence si vous partagez le dépôt (MIT par ex.).
