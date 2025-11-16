
import random
import time
import sys
from pathlib import Path

# Le joueur va devoir choisir s'il veut miser les couleurs uniquement
# ou s'il veut miser sur les chiffres uniquement
# ou s'il veut miser sur les deux en meme temps

rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
vert = [0]
nombre = rouge + noir + vert
nombre.sort()
couleur = [[noir], [rouge], [vert]]
historique = []
argent_joueur = 50



FICHIER_HISTORIQUE = Path(__file__).parent / "historique_tirages.txt"


if FICHIER_HISTORIQUE.exists():
    for ligne in FICHIER_HISTORIQUE.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if ligne:
            try:
                historique.append(int(ligne))
            except ValueError:
                continue

mess_depart = [
    "\033[31mCouleur\033[0m (vous misez que sur les couleurs)",
    "\033[31mChiffre\033[0m (vous misez sur les chiffres de 0 à 36)",
    "\033[31mMixte\033[0m (combinaison des deux stratégies)",
    "Quittez la partie\n"
]

def couleur_ansi(c):
    if c == "rouge": return "\033[31m"   # rouge
    if c == "noir":  return "\033[90m"   # gris clair
    if c == "vert":  return "\033[32m"   # vert
    return ""
RESET = "\033[0m"

def fmt_tirage(n):
    if n in rouge: c = "rouge"
    elif n in noir: c = "noir"
    else: c = "vert"
    return f"{couleur_ansi(c)}{n} {RESET}"


print (f"{nombre}\n")
print ("Bienvenue dans le jeu de la Roulette\n")

if historique:
    print("Historique global des tirages (50 derniers) :")
    print(" | ".join(fmt_tirage(n) for n in historique[-50:]))
    print("-" * 60)
else:
    print("Pas encore d'historique global, vous êtes le premier joueur !")
    print("-" * 60)


rejouer = False 
dernier_choix = None
derniere_couleur = None
derniere_mise_couleur = None
derniere_liste_numero = None
derniere_mise_numero = None


while argent_joueur > 0:
    if not rejouer :
        print(f"Vous disposez de {argent_joueur}\n")
        print("Voici les différentes stratégies : \n")
        for i, element in enumerate(mess_depart, 1):
            print(f"{i}. {element}")

        choix = input("Quelle stratégie choisissez-vous ? (1)(2)(3)(4) : ").strip()

        if choix not in {"1", "2", "3", "4"}:
            print("Choix invalide, veuillez entrer 1, 2, 3 ou 4.\n")
            continue

        if choix == "4":
            print("Au revoir !")
            sys.exit()
    else : 
        choix = dernier_choix
    

    if choix == "1" : 
        print ("Vous avez choisi couleur\n")
        if rejouer:
            couleur_choisie = derniere_couleur
            mise = derniere_mise_couleur
            if mise > argent_joueur:
                print(f"Mise précédente ({mise}) > solde ({argent_joueur}), impossible de rejouer identique.")
                rejouer = False
                continue
        else : 
            while True :
                couleur_choisie = input("Rouge ou Noir ? : ").strip().lower()
                if couleur_choisie in {"rouge", "noir"}:
                    break
                print("Tapez 'rouge' ou 'noir'.")
            while True :
                try : 
                    mise = int(input (f"Quelle somme voulez vous miser sur : {couleur_choisie} ? : "))
                    if mise <= 0:
                            print("La mise doit être > 0.")
                            continue
                    if mise > argent_joueur:
                        print(f"Pas assez d'argent. Solde : {argent_joueur}")
                        continue
                    break
                except ValueError : 
                    print("Entrez un nombre valide.")
            dernier_choix = "1"
            derniere_couleur = couleur_choisie
            derniere_mise_couleur = mise

    elif choix == "2" :
        print ("Vous avez choisi chiffre\n")
        if rejouer:
            liste_numeros = derniere_liste_numero
            nombre_de_numero = len(liste_numeros)
            mise = derniere_mise_numero
            mise_totale = nombre_de_numero * mise
            if nombre_de_numero == 0 or mise_totale > argent_joueur:
                print("Paramètres pour rejouer invalides (liste vide ou mise trop élevée).")
                rejouer = False
                continue
        else:
            while True :
                choix_num = input("Sur quel(s) chiffre(s) voulez-vous miser ? (ex : 7 ou 7 12 25) : ")
                try : 
                    liste_numeros = [int(x) for x in choix_num.replace(",", " ").split()]
                    if len(liste_numeros) == 0:
                        print("Vous devez saisir au moins un numéro.")
                        continue
                    if all(0 <= x <= 36 for x in liste_numeros):
                        break
                    else:
                        print("Les numéros doivent être compris entre 0 et 36.")
                except ValueError:
                    print("Entrez uniquement des nombres séparés par des espaces ou des virgules.")

            nombre_de_numero = len(liste_numeros)
            while True :
                try:
                    mise = int(input(f"Quelle somme voulez-vous miser sur {liste_numeros} : "))
                    if mise <= 0:
                        print("La mise doit être > 0.")
                        continue
                    if mise > argent_joueur:
                        print(f"Pas assez d'argent. Solde : {argent_joueur}")
                        continue
                    break
                except ValueError:
                    print("Entrez un nombre valide.")
        dernier_choix = "2"
        derniere_liste_numero = liste_numeros
        derniere_mise_numero = mise

    elif choix == "3":
        print("\nStratégie Mixte")
        if rejouer:
            couleur_choisie = derniere_couleur
            liste_numeros = derniere_liste_numero
            nombre_de_numero = len(liste_numeros)
            mise_couleur = derniere_mise_couleur
            mise_numero = derniere_mise_numero
            mise_totale = mise_couleur + nombre_de_numero * mise_numero

            if (nombre_de_numero == 0) or (mise_totale > argent_joueur):
                print("Paramètres pour rejouer invalides (liste vide ou mise trop élevée).")
                rejouer = False
                continue
        else:
            while True:
                couleur_choisie = input("Rouge ou Noir ? : ").strip().lower()
                if couleur_choisie in {"rouge", "noir"}:
                    break
                print("⚠️ Tapez 'rouge' ou 'noir'.")

            while True:
                try:
                    mise_couleur = int(input(f"Quelle somme voulez-vous miser sur {couleur_choisie} ? : "))
                    if mise_couleur <= 0:
                        print("La mise doit être > 0.")
                        continue
                    break
                except ValueError:
                    print("Entrez un nombre valide.")

            while True:
                choix_num = input("Sur quel(s) chiffre(s) voulez-vous miser ? (ex : 7 ou 7 12 25) : ").strip()
                try:
                    liste_numeros = [int(x) for x in choix_num.replace(",", " ").split()]
                    liste_coloree = [fmt_tirage(n) for n in liste_numeros]
                    if len(liste_numeros) == 0:
                        print("Vous devez saisir au moins un numéro.")
                        continue
                    if all(0 <= x <= 36 for x in liste_numeros):
                        break
                    else:
                        print("Les numéros doivent être entre 0 et 36.")
                except ValueError:
                    print("Entrez uniquement des nombres valides.")

            nombre_de_numero = len(liste_numeros)
            while True:
                try:
                    mise_numero = int(input(f"Quelle somme voulez-vous miser sur {', '.join(liste_coloree)} : "))
                    if mise_numero <= 0:
                        print("La mise doit être > 0.")
                        continue
                    mise_totale = mise_couleur + nombre_de_numero * mise_numero
                    if mise_totale > argent_joueur:
                        print(f"Pas assez d'argent. Solde : {argent_joueur}")
                        continue
                    break
                except ValueError:
                    print("Entrez un nombre valide.")
            dernier_choix = "3"
            derniere_couleur = couleur_choisie
            derniere_mise_couleur = mise_couleur
            derniere_liste_numero = liste_numeros
            derniere_mise_numero = mise_numero

    tirage = random.choice(nombre)
    if tirage in rouge:
        couleur_tirage = "rouge"
    elif tirage in noir:
        couleur_tirage = "noir"
    elif tirage in vert:
        couleur_tirage = "vert"
    else:
        # Sécurité: si le tirage n'est dans aucune liste, considérer comme vert
        couleur_tirage = "vert"
    historique.append(tirage)

    with FICHIER_HISTORIQUE.open("a", encoding="utf-8") as f:
        f.write(f"{tirage}\n")
                
    print("\nPlus rien ne va plus ! ...")
    time.sleep(1)
    print(f"Résultat de la roulette : {fmt_tirage(tirage)}\n")
    time.sleep(0.5)

    #résultat des gains ou pertes

    if choix == "1":
        if couleur_tirage == couleur_choisie:
            print(f"Bravo ! Vous gagnez {mise} euros.")
            argent_joueur += mise
        else:
            print(f"Dommage ! Vous perdez {mise} euros.")
            argent_joueur -= mise

    elif choix == "2":
        if tirage in liste_numeros:
            net = (36 - nombre_de_numero) * mise
            print(f"Numéro touché ! Gain net : {net}")
        else:
            net = - nombre_de_numero * mise
            print(f"Raté. Perte : {-net}")
        argent_joueur += net

    elif choix == "3":
        if tirage in liste_numeros and couleur_tirage == couleur_choisie:
            net = (36 - nombre_de_numero) * mise_numero + mise_couleur
            print(f"Numéro + Couleur ! Gain net : {net}")
        elif tirage in liste_numeros and couleur_tirage != couleur_choisie:
            net = (36 - nombre_de_numero) * mise_numero - mise_couleur
            print(f"Numéro seulement. Gain net : {net}")
        elif tirage not in liste_numeros and couleur_tirage == couleur_choisie:
            net = - nombre_de_numero * mise_numero + mise_couleur
            print(f"Couleur seulement. Gain net : {net}")
        else:
            net = - nombre_de_numero * mise_numero - mise_couleur
            print(f"Rien… Perte : - {-net}")
        argent_joueur += net

    print(f"Nouveau solde : {argent_joueur}")
    print(" | ".join(fmt_tirage(n) for n in historique[-26:]))
    print("-" * 60)


    if argent_joueur <= 0:
        break

    reponse = input("Voulez Vous rejouer la meme chose ? (o/n)").strip().lower()
    if reponse == "o":
        if dernier_choix == "1":
            ok = derniere_mise_couleur is not None and derniere_mise_couleur <= argent_joueur
        elif dernier_choix == "2":
            ok = (derniere_liste_numero and derniere_mise_numero is not None 
                and derniere_mise_numero * len(derniere_liste_numero) <= argent_joueur)
        elif dernier_choix == "3":
            k = len(derniere_liste_numero or [])
            total = (derniere_mise_couleur or 0) + (derniere_mise_numero or 0) * k
            ok = (k > 0 and total <= argent_joueur)
        else:
            ok = False

        if ok:
            rejouer = True
        else:
            print("Solde insuffisant pour rejouer à l’identique.")
            rejouer = False
    else:
        rejouer = False

print("\nVous n'avez plus d'argent... Fin de partie.")

    






