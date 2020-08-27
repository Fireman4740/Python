# -*- coding: latin-1 -*-
 
from random import randrange

 
partie_continue = 1
 
while partie_continue == True :
 
        nombre_a_trouver = randrange(100, 501)
 
        print("Bienvenue au juste prix !!")
        print("tu dois touver des nombre entre 100 et 500")
        proposition = input("Le jeu commence... Alors quel nombre as-tu choisi? ")
        proposition = int(proposition)
        i = 0
        essais = 10
 
        while proposition != nombre_a_trouver and i < 10 and essais != 1 :
 
            if proposition < nombre_a_trouver :
 
                print("C'est plus!")
                essais -= 1
                print("Il te reste ",essais, " coups")  
                proposition = int(input("Entre un autre nombre : "))
                
 
            elif proposition > nombre_a_trouver :
 
                essais -= 1
                print("C'est moins!")
                print("Il te reste ",essais, " coups") 
                proposition = int(input("Entre un autre nombre : "))
                
            i += 1
 
        if proposition == nombre_a_trouver :
 
            print("Bravo! Tu as gagné!")

if partie_continue == False :
 
        print("Dommage... Au plaisir de te revoir")