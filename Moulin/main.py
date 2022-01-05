"""
Usage:
======
    main.py corp principale de notre jeu du moulin

"""

__authors__ = "Jean-Daniel SPADAZZI & Tedi KPOGNON & GAY Guillaume "
__date__ = "2021/11/17"
__version__ = "1.1"

# L'importation de l’ensemble des éléments du paquet tkinter :

from tkinter import *

import Joueur
import Intersection

# Variable globale

# global Nbrpion1, Nbrpion2, Restepion1, Restepion2, grille, grillepast

'''class Intersection:
    def __init__(self,nom,x,y):
        self.nom = nom
        self.x = x
        self.y = y
        self.vide = True'''

'''class Joueur:
    def __init__(self):
        self.Nbrpion = 9 #Définition attribut nombre de pion à poser
        self.Restepion = 9 #Définition attribut nombre de pion restant'''





def phase_jeu(status):
    match status:

        case 1:
            init_game()

        # humain vs humain
        case 2:
            print()
            print("Phase de Pose Joueur vs Joueur")

            # while Nbrpion2 > 0 :
            # Pose

            # Moulin?

            phase_jeu(3)

        case 3:
            print()
            print("Phase de Mouvement Joueur vs Joueur")

            # while RestePion1 > 2 or Restepion2 > 2 :
            # Mouvement

            # Moulin?

            phase_jeu(4)

        case 4:
            print()
            print("Fin de partie")

            # if Restepion1 == 2:
            # print("Joueur 2 Win)

            # if Restepion2 == 2:
            # print("Joueur 1 Win)



        # avec l'IA
        case 20:
            print()
            print("Phase de Pose Joueur vs Ordinateur")

            # while Nbrpion2 > 0 :
            # Pose avec l'ia

            # Moulin?

            phase_jeu(30)

        case 30:
            print()
            print("Phase de Mouvement Joueur vs Ordinateur")

            # while RestePion1 > 2 or Restepion2 > 2 :
            # Mouvement avec l'ia

            # Moulin?

            phase_jeu(4)


def init_game():

    inters = []
    inters.append(Intersection("inter1", 1, 1))
    inters.append(Intersection("inter2", 4, 1))
    inters.append(Intersection("inter3", 7, 1))
    inters.append(Intersection("inter4", 2, 2))
    inters.append(Intersection("inter5", 4, 2))
    inters.append(Intersection("inter6", 6, 2))
    inters.append(Intersection("inter7", 3, 3))
    inters.append(Intersection("inter8", 4, 3))
    inters.append(Intersection("inter9", 5, 3))
    inters.append(Intersection("inter10", 1, 4))
    inters.append(Intersection("inter11", 2, 4))
    inters.append(Intersection("inter12", 3, 4))
    inters.append(Intersection("inter13", 5, 4))
    inters.append(Intersection("inter14", 6, 4))
    inters.append(Intersection("inter15", 7, 4))
    inters.append(Intersection("inter16", 3, 5))
    inters.append(Intersection("inter17", 5, 5))
    inters.append(Intersection("inter18", 5, 5))
    inters.append(Intersection("inter19", 2, 6))
    inters.append(Intersection("inter20", 4, 6))
    inters.append(Intersection("inter21", 6, 6))
    inters.append(Intersection("inter22", 1, 7))
    inters.append(Intersection("inter23", 4, 7))
    inters.append(Intersection("inter24", 7, 7))

    print("Choix du mode de jeu :")
    print("1. Humain vs Humain")
    print("2. Humain vs Ordinateur")
    mode = int(input("Indiquez votre choix : "))
    if mode == 1:
        phase_jeu(2)  # phase de pose j vs j

    if mode == 2:
        phase_jeu(20)  # phase de pose j vs ordinateur
    if mode != 1 and mode != 2:
        print("Choix impossible, entrez un choix possible")
        init_game()

#------------------------------------------------------------

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    joueur1 = Joueur("noir", 9)
    joueur2 = Joueur("blanc", 9)

    print()
    phase_jeu(1)

'''    # Définition des deux joueurs
    un = Joueur()
    deux = Joueur()

    print("J1 : Nombre de pion à poser =", un.Nbrpion, "Nombre de pion restant =", deux.Restepion)
    print("J2 : Nombre de pion à poser =", un.Nbrpion, "Nombre de pion restant =", deux.Restepion)'''