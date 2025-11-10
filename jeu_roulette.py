

import os
import random
import time

rouge = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
noir = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
vert = [0]


nombre = rouge + noir + vert
nombre.sort()
print (f"{nombre}\n")

couleur = [[noir], [rouge], [vert]]

print ("Bienvenue dans le jeu de la Roulette\n")
# Le joueur va devoir choisir s'il veut miser les couleurs uniquement
# ou s'il veut miser sur les chiffres uniquement
# ou s'il veut miser sur les deux en meme temps 

argent_joueur = 50
print(f"Vous disposez en début de partie de {argent_joueur}\n")

strategie = ["Couleur", "Chiffres", "Mixte"]

print ("voici les différentes stratégies :")
print ("\033[31mCouleur\033[0m (vous misez que sur les couleurs)")
print("\033[31mChiffre\033[0m (vous misez sur les chiffres de 0 à 36)")
print("\033[31mMixte\033[0m (combinaison des deux stratégies) \n")


def couleur_ansi(c):
    if c == "rouge": return "\033[31m"   # rouge
    if c == "noir":  return "\033[90m"   # gris clair (lisible partout)
    if c == "vert":  return "\033[32m"   # vert
    return ""
RESET = "\033[0m"

def fmt_tirage(n):
    if n in rouge: c = "rouge"
    elif n in noir: c = "noir"
    else: c = "vert"
    return f"{couleur_ansi(c)}{n} ({c}){RESET}"



while argent_joueur >0 : 
    try : 


        tirage = random.choice(nombre)
        if tirage in rouge :
            couleur_tirage = "rouge"
        elif tirage in noir :
            couleur_tirage = "noir"
        elif tirage in vert : 
            couleur_tirage = "vert"
        
        historique_tirage = []
        historique_tirage.append(tirage)


        strat_choisi = input("Quelle stratégie choisissez vous ? : ").lower()
        if strat_choisi == "couleur" : 
            print ("Vous avez choisi couleur\n")
            couleur_choisi = input("rouge ou noir ? : \n").lower()
            mise = int(input (f"Quelle somme voulez vous miser sur : {couleur_choisi} ? : "))
            if 0<= mise <= argent_joueur :    
                print ("Plus rien ne va plus :\n")
                time.sleep(3)
                print(f"Résultat de la roulette : {fmt_tirage(tirage)}\n")
                time.sleep(1)
                if couleur_tirage == couleur_choisi  :   
                    print (f"bravo vous avez gagné {mise}")
                    argent_joueur += mise
                    print (f"Solde : {argent_joueur}")
                
                else : 
                    print (f"Dommage vous avez perdu {mise}")
                    argent_joueur -= mise
                    print (f"Solde : {argent_joueur}")
            else : 
                print (f"Vous n'avez pas assez d'argent, il vous reste {argent_joueur}")


        elif strat_choisi == "chiffre" :
            print ("Vous avez choisi chiffre")
            choix_num = input("Sur quel(s) chiffre(s) voulez-vous miser ? (ex : 7 ou 7 12 25) : ")
            liste_numeros = [int(x) for x in choix_num.replace(",", " ").split()]
            nombre_de_numero = len(liste_numeros)
            mise = int(input (f"Quelle somme voulez vous miser sur {liste_numeros} : "))
            if 0<= mise <= argent_joueur :
                print ("Plus rien ne va plus :\n")
                time.sleep(3)
                print(f"Résultat de la roulette : {fmt_tirage(tirage)}\n")
                if tirage in liste_numeros : 
                    print (f"Bravo vous avez gagné {35 * mise}")
                    argent_joueur += 35* mise 
                    print (f"Solde : {argent_joueur}")
                else : 
                    print (f"Dommage vous avez perdu {int(nombre_de_numero) * (mise)} ")
                    argent_joueur -= nombre_de_numero*mise 
                    print (f"Solde : {argent_joueur}")
            else : 
                print (f"Vous n'avez pas assez d'argent, il vous reste {argent_joueur}")

        elif strat_choisi == "mixte" :
            print ("Vous avez choisi la stratégie mixte")
            couleur_choisi = input("rouge ou noir ? : ").lower()
            mise_couleur = int(input (f"Quelle somme voulez vous miser sur : {couleur_choisi} ? : "))
            choix_num = input("Sur quel(s) chiffre(s) voulez-vous miser ? (ex : 7 ou 7 12 25) : ")
            liste_numeros = [int(x) for x in choix_num.replace(",", " ").split()]
            nombre_de_numero = len(liste_numeros)
            mise_numero = int(input (f"Quelle somme voulez vous miser sur {liste_numeros} : "))
            if 0<= mise_couleur + mise_numero <= argent_joueur : 
                
                print ("Plus rien ne va plus :\n")
                time.sleep(3)
                print(f"Résultat de la roulette : {fmt_tirage(tirage)}\n")
                if tirage in liste_numeros and couleur_choisi ==couleur_tirage  :
                    print (f"bravo vous avez gagné : {35*mise_numero + mise_couleur}")
                    argent_joueur += 35*mise_numero + mise_couleur
                    print (f"Solde : {argent_joueur}")
                elif tirage in liste_numeros and couleur_tirage != couleur_choisi  :
                    print (f"bravo vous avez gagné : {35*mise_numero - mise_couleur}")
                    argent_joueur += 35*mise_numero - mise_couleur
                    print (f"Solde : {argent_joueur}")
                elif couleur_tirage == couleur_choisi and tirage not in liste_numeros :
                    print (f"bravo vous avez gagné : {-nombre_de_numero*mise_numero + mise_couleur}")
                    argent_joueur += - nombre_de_numero*mise_numero + mise_couleur
                    print (f"Solde : {argent_joueur}")
                elif couleur_tirage != couleur_choisi and tirage not in liste_numeros : 
                    print (f"Dommage vous avez perdu : {-nombre_de_numero* mise_numero - mise_couleur}")
                    argent_joueur -= nombre_de_numero*mise_numero + mise_couleur
                    print (f"Solde : {argent_joueur}")    
            else : 
                print (f"Vous n'avez pas assez d'argent, il vous reste {argent_joueur}")
        else : 
            print ("Veuillez rentrer votre stratégie")
    except ValueError : 
        print ("Veuillez entrez un nombre")
else : 
    print ("Le jeu est fini, vous n'avez plus d'argent (cheh). Merci d'avoir joué, et de me rendre riche")















