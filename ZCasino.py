# -*-coding:utf-8 -*
# Ce fichier est un jeu de roulette 1

import os
from random import randrange
from math import ceil

argent_total = int(input("Combien voulez vous deposer ? "))

continue_partie = True
print("Vous vous installez a une table")
print(" - Faites entrer pour quitter le casino.")
print(" - Bonjour Monsieur")

while continue_partie:
    nombre_miser = -1
    while nombre_miser < 0 or nombre_miser > 49:
        nombre_miser = input(" - Sur quelle nombre misez vous ? ")

        try:
            nombre_miser = int(nombre_miser)
        except ValueError:
            print(" - Excucez moi , vous n avez pas misez sur un nombre.")
            nombre_miser = int(nombre_miser)
            continue
        if nombre_miser < 0:
            print(" - Vous ne pouvez misez que sur des nombres entre 0 et 49")
        if nombre_miser > 49:
            print(" - Vous ne pouvez misez que sur des nombres entre 0 et 49")
            

    mise = 0
    while mise <= 0 or mise > argent_total:
        mise = input(" - Quelle est votre mise monsieur ? ")
        try:
            mise = int(mise)
        except ValueError:
            print(" - Excucez moi , vous n avez pas misez.")
            mise = -1
            continue
        if mise <= 0:
            print(" - Vous ne pouvez pas misez une somme negative ou nulle.")
        if mise > argent_total:
            print(" - Vous ne pouvez miser autant, vous n avez que", argent_total, "$")
    
    nombre = randrange(50)
    print("La balle tourne et tombe sur", nombre,".")
    if nombre == nombre_miser:
        print(" - Bravo, vous avez gagne ", mise * 3)
        argent_total += mise*3
    
    elif nombre %2 == nombre_miser %2:
        print(" - Bravo vous avez choisie la bonne couleur, vous gagnez", mise * 0.5)
        argent_total += mise * 0.5

    else:
        print(" - Dommage vous avez perdu ")
        argent_total -= mise
        print("Vous avez a present", argent_total, "$")

    if argent_total <= 0:
        print("Vous etes ruine !")
        restart = input("Souhaitez vous recommencer ? O/N ")
        if restart == "N" or restart == "n":
            continue_partie = False

       # if restart == "Oui":
           # continue_partie = True


    
os.system("pause")








