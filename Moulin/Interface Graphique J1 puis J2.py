##-----Importation des Modules-----##
from tkinter import *
from tkinter.ttk import *

##----- Définition des Variables globales -----##
inters = []
moulins = []
etape = 0


J1 = True                              # True pour J1, False pour J2
n = 1                                       # Numéro du tour de jeu


class Damier:

    def __init__(self):
        self.area = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 1, 0, 0, 1, 0, 0, 1],
                     [0, 0, 1, 0, 1, 0, 1, 0],
                     [0, 0, 0, 1, 1, 1, 0, 0],
                     [0, 1, 1, 1, 0, 1, 1, 1],
                     [0, 0, 0, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 1, 0, 1, 0],
                     [0, 1, 0, 0, 1, 0, 0, 1]]

    def __str__(self):
        res = ""
        for i in range(len(self.area)):
            if i > 0:
                for j in range(len(self.area[i])):
                    if j > 0:
                        res += str(self.area[i][j]) + " "
                res += "\n"
        return res

grille = Damier()

class Joueur:

    def __init__(self, nom, pionsRestants, reprPion):
        self.nom = nom
        self.pionRestants = pionsRestants
        self.listePionsEnJeu = []
        self.ReprPion = reprPion

    def pose(self, x, y):
        for inter in inters:
            if x == inter.X and y == inter.Y and inter.Occupee == False:
                pion = Pion(x, y, self.nom)
                inter.Occupee=True
                inter.pion = pion
                grille.area[x][y] = self.ReprPion
                self.listePionsEnJeu.append(pion)
                self.pionRestants -= 1
                return True
        return False

class Pion:

    def __init__(self, x, y, nom):
        self.X = x
        self.Y = y
        self.color = nom
        self.InMoulin = False


joueur1 = Joueur("Joueur 1", 9, 'X')
joueur2 = Joueur("Joueur 2", 9, '#')

class Intersection:
    def __init__(self, nom, x, y,igx, igy):
        self.Nom = nom
        self.X = x
        self.Y = y
        self.Igx = igx
        self.Igy = igy
        self.pion=None
        self.Occupee = False
        self.Voisins = {'inter1': ('inter2', 'inter10'),
                        'inter2': ('inter1', 'inter3', 'inter5'),
                        'inter3': ('inter2', 'inter15'),
                        'inter4': ('inter5', 'inter11'),
                        'inter5': ('inter2', 'inter4', 'inter6', 'inter8'),
                        'inter6': ('inter5', 'inter14'),
                        'inter7': ('inter8', 'inter12'),
                        'inter8': ('inter5', 'inter7', 'inter9'),
                        'inter9': ('inter8', 'inter13'),
                        'inter10': ('inter1', 'inter11', 'inter22'),
                        'inter11': ('inter4', 'inter10', 'inter12', 'inter19'),
                        'inter12': ('inter7', 'inter11', 'inter16'),
                        'inter13': ('inter9', 'inter14', 'inter18'),
                        'inter14': ('inter6', 'inter13', 'inter15', 'inter21'),
                        'inter15': ('inter3', 'inter14', 'inter24'),
                        'inter16': ('inter12', 'inter17'),
                        'inter17': ('inter16', 'inter18', 'inter20'),
                        'inter18': ('inter13', 'inter17'),
                        'inter19': ('inter11', 'inter20'),
                        'inter20': ('inter17', 'inter19', 'inter21', 'inter23'),
                        'inter21': ('inter14', 'inter20'),
                        'inter22': ('inter10', 'inter23'),
                        'inter23': ('inter20', 'inter22', 'inter24'),
                        'inter24': ('inter15', 'inter23')}

class Moulin:
    def __init__(self,inter1,inter2,inter3):
        self.Inter1=inter1
        self.Inter2=inter2
        self.Inter3=inter3

def init_game():

    inters.append(Intersection("inter1", 1, 1 , 10,10))
    inters.append(Intersection("inter2", 1, 4 ,249,10))
    inters.append(Intersection("inter3", 1, 7 ,490,10))
    inters.append(Intersection("inter4", 2, 2, 80,80))
    inters.append(Intersection("inter5", 2, 4,249,80))
    inters.append(Intersection("inter6", 2, 6,420,80))
    inters.append(Intersection("inter7", 3, 3,150,150))
    inters.append(Intersection("inter8", 3, 4,249,150))
    inters.append(Intersection("inter9", 3, 5,349,150))
    inters.append(Intersection("inter10", 4, 1,10,249))
    inters.append(Intersection("inter11", 4, 2,80,249))
    inters.append(Intersection("inter12", 4, 3,150,249))
    inters.append(Intersection("inter13", 4, 5,350,249))
    inters.append(Intersection("inter14", 4, 6,420,249))
    inters.append(Intersection("inter15", 4, 7,490,249))
    inters.append(Intersection("inter16", 5, 3,150,350))
    inters.append(Intersection("inter17", 5, 4,249,350))
    inters.append(Intersection("inter18", 5, 5,350,350))
    inters.append(Intersection("inter19", 6, 2,80,420,))
    inters.append(Intersection("inter20", 6, 4,249,420,))
    inters.append(Intersection("inter21", 6, 6,420,420,))
    inters.append(Intersection("inter22", 7, 1,10,490,))
    inters.append(Intersection("inter23", 7, 4,249,490,))
    inters.append(Intersection("inter24", 7, 7,490,490))

    moulins.append(Moulin(inters[0],inters[1],inters[2]))
    moulins.append(Moulin(inters[3],inters[4],inters[5]))
    moulins.append(Moulin(inters[6],inters[7],inters[8]))

    moulins.append(Moulin(inters[15],inters[16],inters[17]))
    moulins.append(Moulin(inters[18],inters[19],inters[20]))
    moulins.append(Moulin(inters[21],inters[22],inters[23]))

    moulins.append(Moulin(inters[0],inters[9] ,inters[21]))
    moulins.append(Moulin(inters[3],inters[10],inters[18]))
    moulins.append(Moulin(inters[6],inters[11],inters[15]))

    moulins.append(Moulin(inters[8],inters[12],inters[17]))
    moulins.append(Moulin(inters[5],inters[13],inters[20]))
    moulins.append(Moulin(inters[2],inters[14],inters[23]))

    moulins.append(Moulin(inters[1],inters[4],inters[7]))
    moulins.append(Moulin(inters[14],inters[13],inters[12]))
    moulins.append(Moulin(inters[22],inters[19],inters[16]))
    moulins.append(Moulin(inters[9],inters[10],inters[11]))



def posevisuel(event) :
    """ Entrées : Un événement de la souris
        Sortie : Affiche en temps réel les coordonnées de la case du clic de souris"""
    global J1, cases, n
    l = event.y                 # Ligne du clic
    c = event.x                  # Colonne du clic

    print("Pion à poser par le joueur 1 : ", joueur1.pionRestants)
    print("Pion à poser par le joueur 2 : ", joueur2.pionRestants, "\n")
    print(l,c)
    if J1:  # J1 == True
        if (4 < l < 16 and 4 < c < 16): #incrementer la condition position grille vide
            print("ok 1.1 J1")

            lignes.append(dessin.create_oval(3, 3, 17, 17, fill='blue'))
            message.configure(text='Tour du joueur 2')
            #incrementer la grille
            print(grille)
            J1 = not (J1)
        if (4 < l < 16 and 243 < c < 255):
            print("ok 1.4 J1")
            lignes.append(dessin.create_oval(242, 3, 256, 17, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (4 < l < 16 and 484 < c < 496):
            print("ok 1.7 J1")
            lignes.append(dessin.create_oval(483, 3, 497, 17, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)

        if (74 < l < 86 and 74 < c < 86):
            print("ok 2.2 J1")
            lignes.append(dessin.create_oval(73, 73, 87, 87, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (74 < l < 86 and 243 < c < 255):
            print("ok 2.4 J1")
            lignes.append(dessin.create_oval(242, 73, 256, 87, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (74 < l < 86 and 414 < c < 426):
            print("ok 2.6 J1")
            lignes.append(dessin.create_oval(413, 73, 427, 87, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)


        if (144 < l < 156 and 144 < c < 156):
            print("ok 3.3 J1")
            lignes.append(dessin.create_oval(143, 143, 157, 157, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (144 < l < 156 and 243 < c < 255):
            print("ok 3.4 J1")
            lignes.append(dessin.create_oval(243, 143, 257, 157, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (144 < l < 156 and 344 < c < 356):
            print("ok 3.5 J1")
            lignes.append(dessin.create_oval(343, 143, 357, 157, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)


        if (243 < l < 255 and 4 < c < 16):
            print("ok 4.1 J1")
            lignes.append(dessin.create_oval(3, 242, 17, 256, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (243 < l < 256 and 74 < c < 86):
            print("ok 4.2 J1")
            lignes.append(dessin.create_oval(73, 242, 87, 257, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (243 < l < 255 and 144 < c < 156):
            print("ok 4.3 J1")
            lignes.append(dessin.create_oval(143, 242, 157, 257, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (243 < l < 255 and 344 < c < 356):
            print("ok 4.4J1")
            lignes.append(dessin.create_oval(343, 242, 357, 257, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (243 < l < 255 and 414 < c < 426):
            print("ok 4.5 J1")
            lignes.append(dessin.create_oval(413, 242, 427, 257, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (243 < l < 255 and 484 < c < 496):
            print("ok 4.6 J1")
            lignes.append(dessin.create_oval(483, 242, 497, 257, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)

        if (344 < l < 355 and 144 < c < 156):
            print("ok 5.3 J1")
            lignes.append(dessin.create_oval(143, 343, 157, 357, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (344 < l < 356 and 243 < c < 255):
            print("ok 5.4 J1")
            lignes.append(dessin.create_oval(242, 343, 256, 357, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (344 < l < 356 and 344 < c < 356):
            print("ok 5.5 J1")
            lignes.append(dessin.create_oval(343, 343, 357, 357, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)

        if (414 < l < 426 and 74 < c < 86):
            print( "ok 6.2J1")
            lignes.append(dessin.create_oval(73, 413, 87, 427, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (414 < l < 426 and 243 < c < 255):
            print("ok 6.4 J1")
            lignes.append(dessin.create_oval(242, 413, 256, 427, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (414 < l < 426 and 414 < c < 426):
            print("ok 6.6 J1")
            lignes.append(dessin.create_oval(413, 413, 427, 427, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)

        if (484 < l < 496 and 4 < c < 16):
            print("ok 7.1 J1")
            lignes.append(dessin.create_oval(3, 483, 17, 497, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (484 < l < 496 and 243 < c < 255):
            print("ok 7.4 J1")
            lignes.append(dessin.create_oval(242, 483, 256, 497, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)
        if (484 < l < 496 and 484 < c < 496):
            print("ok 7.7 J1")
            lignes.append(dessin.create_oval(483, 483, 497, 497, fill='blue'))
            message.configure(text='Tour du joueur 2')
            J1 = not (J1)

    else:
        if (4 < l < 16 and 4 < c < 16):
            print("ok 1.1 J1")
            lignes.append(dessin.create_oval(3, 3, 17, 17, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (4 < l < 16 and 243 < c < 255):
            print("ok 1.4 J1")
            lignes.append(dessin.create_oval(242, 3, 256, 17, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (4 < l < 16 and 484 < c < 496):
            print("ok 1.7 J1")
            lignes.append(dessin.create_oval(483, 3, 497, 17, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (74 < l < 86 and 74 < c < 86):
            print("ok 2.2 J1")
            lignes.append(dessin.create_oval(73, 73, 87, 87, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (74 < l < 86 and 243 < c < 255):
            print("ok 2.4 J1")
            lignes.append(dessin.create_oval(242, 73, 256, 87, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (74 < l < 86 and 414 < c < 426):
            print("ok 2.6 J1")
            lignes.append(dessin.create_oval(413, 73, 427, 87, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (144 < l < 156 and 144 < c < 156):
            print("ok 3.3 J1")
            lignes.append(dessin.create_oval(143, 143, 157, 157, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (144 < l < 156 and 243 < c < 255):
            print("ok 3.4 J1")
            lignes.append(dessin.create_oval(243, 143, 257, 157, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (144 < l < 156 and 344 < c < 356):
            print("ok 3.5 J1")
            lignes.append(dessin.create_oval(343, 143, 357, 157, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (243 < l < 255 and 4 < c < 16):
            print("ok 4.1 J1")
            lignes.append(dessin.create_oval(3, 242, 17, 256, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (243 < l < 256 and 74 < c < 86):
            print("ok 4.2 J1")
            lignes.append(dessin.create_oval(73, 242, 87, 257, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (243 < l < 255 and 144 < c < 156):
            print("ok 4.3 J1")
            lignes.append(dessin.create_oval(143, 242, 157, 257, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (243 < l < 255 and 344 < c < 356):
            print("ok 4.4J1")
            lignes.append(dessin.create_oval(343, 242, 357, 257, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (243 < l < 255 and 414 < c < 426):
            print("ok 4.5 J1")
            lignes.append(dessin.create_oval(413, 242, 427, 257, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (243 < l < 255 and 484 < c < 496):
            print("ok 4.6 J1")
            lignes.append(dessin.create_oval(483, 242, 497, 257, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (344 < l < 355 and 144 < c < 156):
            print("ok 5.3 J1")
            lignes.append(dessin.create_oval(143, 343, 157, 357, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (344 < l < 356 and 243 < c < 255):
            print("ok 5.4 J1")
            lignes.append(dessin.create_oval(242, 343, 256, 357, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (344 < l < 356 and 344 < c < 356):
            print("ok 5.5 J1")
            lignes.append(dessin.create_oval(343, 343, 357, 357, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (414 < l < 426 and 74 < c < 86):
            print("ok 6.2J1")
            lignes.append(dessin.create_oval(73, 413, 87, 427, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (414 < l < 426 and 243 < c < 255):
            print("ok 6.4 J1")
            lignes.append(dessin.create_oval(242, 413, 256, 427, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (414 < l < 426 and 414 < c < 426):
            print("ok 6.6 J1")
            lignes.append(dessin.create_oval(413, 413, 427, 427, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

        if (484 < l < 496 and 4 < c < 16):
            print("ok 7.1 J1")
            lignes.append(dessin.create_oval(3, 483, 17, 497, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (484 < l < 496 and 243 < c < 255):
            print("ok 7.4 J1")
            lignes.append(dessin.create_oval(242, 483, 256, 497, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)
        if (484 < l < 496 and 484 < c < 496):
            print("ok 7.7 J1")
            lignes.append(dessin.create_oval(483, 483, 497, 497, fill='red'))
            message.configure(text='Tour du joueur 1')
            J1 = not (J1)

def reinit():
    """Cette fonction ré-initialise les variables globales."""
    global drapeau, cases, n
    grille = Damier()
    J1 = True          # True J1, False pour J2
    n = 1

    message.configure(text='Séléctionné un mode de jeu')
    dessin.delete(ALL)      # Efface toutes les figures
    lignes = []

    # cadre exterieure
    lignes.append(dessin.create_line(10, 10, 490, 10, fill='black'))
    lignes.append(dessin.create_line(10, 490, 490, 490, fill='black'))
    lignes.append(dessin.create_line(10, 10, 10, 490, fill='black'))
    lignes.append(dessin.create_line(490, 10, 490, 490, fill='black'))
    # cadre intermediaire

    lignes.append(dessin.create_line(80, 80, 420, 80, fill='black'))
    lignes.append(dessin.create_line(80, 420, 420, 420, fill='black'))
    lignes.append(dessin.create_line(80, 80, 80, 420, fill='black'))
    lignes.append(dessin.create_line(420, 80, 420, 420, fill='black'))

    # cadre interieure

    lignes.append(dessin.create_line(150, 150, 350, 150, fill='black'))
    lignes.append(dessin.create_line(150, 350, 350, 350, fill='black'))
    lignes.append(dessin.create_line(150, 150, 150, 350, fill='black'))
    lignes.append(dessin.create_line(350, 150, 350, 350, fill='black'))

    # ligne croisé

    lignes.append(dessin.create_line(249, 10, 249, 150, fill='black'))
    lignes.append(dessin.create_line(249, 350, 249, 490, fill='black'))
    lignes.append(dessin.create_line(10, 249, 150, 249, fill='black'))
    lignes.append(dessin.create_line(350, 249, 490, 249, fill='black'))

    # ligneInter 1
    lignes.append(dessin.create_oval(5, 5, 15, 15, fill='black', tags="inter1"))
    lignes.append(dessin.create_oval(244, 5, 254, 15, fill='black', tags="inter2"))
    lignes.append(dessin.create_oval(485, 5, 495, 15, fill='black', tags="inter3"))
    # ligneInter 2
    lignes.append(dessin.create_oval(75, 75, 85, 85, fill='black', tags="inter4"))
    lignes.append(dessin.create_oval(244, 75, 254, 85, fill='black', tags="inter5"))
    lignes.append(dessin.create_oval(415, 75, 425, 85, fill='black', tags="inter6"))
    # ligneInter 3
    lignes.append(dessin.create_oval(145, 145, 155, 155, fill='black', tags="inter7"))
    lignes.append(dessin.create_oval(244, 145, 254, 155, fill='black', tags="inter8"))
    lignes.append(dessin.create_oval(345, 145, 355, 155, fill='black', tags="inter9"))
    # ligneInter 4
    lignes.append(dessin.create_oval(5, 244, 15, 254, fill='black', tags="inter10"))
    lignes.append(dessin.create_oval(75, 244, 85, 254, fill='black', tags="inter11"))
    lignes.append(dessin.create_oval(145, 244, 155, 254, fill='black', tags="inter12"))
    lignes.append(dessin.create_oval(345, 244, 355, 254, fill='black', tags="inter13"))
    lignes.append(dessin.create_oval(415, 244, 425, 254, fill='black', tags="inter14"))
    lignes.append(dessin.create_oval(485, 244, 495, 254, fill='black', tags="inter15"))
    # ligneInter 5
    lignes.append(dessin.create_oval(145, 345, 155, 355, fill='black', tags="inter16"))
    lignes.append(dessin.create_oval(244, 345, 254, 355, fill='black', tags="inter17"))
    lignes.append(dessin.create_oval(345, 345, 355, 355, fill='black', tags="inter18"))
    # ligneInter 6
    lignes.append(dessin.create_oval(75, 415, 85, 425, fill='black', tags="inter19"))
    lignes.append(dessin.create_oval(244, 415, 254, 425, fill='black', tags="inter20"))
    lignes.append(dessin.create_oval(415, 415, 425, 425, fill='black', tags="inter21"))
    # ligneInter 7
    lignes.append(dessin.create_oval(5, 485, 15, 495, fill='black', tags="inter22"))
    lignes.append(dessin.create_oval(244, 485, 254, 495, fill='black', tags="inter23"))
    lignes.append(dessin.create_oval(485, 485, 495, 495, fill='black', tags="inter24"))

def fctSousMenu1():  # Action associée au sous-menu 1 du menu 1
    print('J vs J')
    #init_game()


def fctSousMenu2():  # Action associée au sous-menu 1 du menu 1
    print('J vs IA')

def fctSousMenu3():  # Action associée au sous-menu 1 du menu 1
    print('Sauver')

def fctSousMenu4():  # Action associée au sous-menu 1 du menu 1
    print('Charger')

##-----Création de la fenêtre-----##
FenêtreP = Tk()
FenêtreP.title("Jeu du Moulin®")
FenêtreP.geometry('1100x595+400+100')
FenêtreP.config(bg='lightgray')
FenêtreP.option_add('*tearOff', FALSE)  # Nécessaire avec windows

# ----------------------------------------Menu------------------------------------------
menubar = Menu(FenêtreP)  # Création d'un objet "barre de menus"
FenêtreP['menu'] = menubar  # Association de l'objet à la fenêtre

# Ajout de menus
menu1 = Menu(menubar)
menu2 = Menu(menubar)
menu3 = Menu(menubar)
# Ajout de sous-menus
menubar.add_cascade(menu=menu1, label='Démarrer une partie')
menubar.add_cascade(menu=menu2, label='Sauvegarder la partie')
menubar.add_cascade(menu=menu3, label='Charger une partie...')
# Association de fonctions aux menus et sous-menus de démarrage de parties
menu1.add_command(label='Joueur vs Joueur', command=fctSousMenu1)
menu1.add_separator()  # Barre de séparation
menu1.add_command(label='Joueur vs IA', command=fctSousMenu2)
# Association de fonctions aux menus et sous-menus de sauvegarde
menu2.add_command(label='Sauvegarder sous', command=fctSousMenu3)
# Association de fonctions aux menus et sous-menus charge de partie
# for save in storage...
menu3.add_command(label='nom de la partie', command=fctSousMenu4)
# menu3.add_separator()  # Barre de séparation aprés





##-----Création des zones de texte-----##
message=Label(FenêtreP, text='Séléctionnez un mode de jeu')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


##-----Création des boutons-----##
bouton_quitter = Button(FenêtreP, text='Quitter', command=FenêtreP.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)

bouton_reload = Button(FenêtreP, text='Recommencer', command=reinit)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)


##-----Création des canevas-----##


dessin=Canvas(FenêtreP, bg="white", width=501, height=501)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)

info=Canvas(FenêtreP, bg="white", width=501, height=501)
info.grid(row = 1, column = 2, columnspan = 2, padx=5, pady=5)

s = Style()
s.configure('TFrame', background='gray')

s2 = Style()
s2.configure('new.TFrame', background='lightgray')

sousframe1 = Frame(info, relief=SUNKEN, style='new.TFrame')
sousframe1.grid(row=0, column=0, sticky=(W, E), padx=10, pady=25)
sousframe2 = Frame(info, relief=SUNKEN, style='new.TFrame')
sousframe2.grid(row=0, column=1, sticky=(N, E), padx=10, pady=25)

texte = ' Chaque joueur dispose de 9 pions de sa couleur.  L\'objectif du jeu est de \n retirer les pions de l\'adversaire sur le damier ou de le bloquer afin qu\'il \n ne puisse plus jouer.'
Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
    row=0, column=0, padx=10, pady=10, sticky=(W, E))

texte = ' PHASE 1 - La pose : Tant qu\'il en possède encore, chaque joueur place\n à tour de rôle un pion sur une intersection libre. La phase 2 débute après\n que les joueurs ont placé tous leurs pions. \n\n PHASE 2 - Le mouvement : Lorsqu\'il n\'a plus de pion à poser, chaque joueur fait\n glisser l\'un de ses pions vers une intersection voisine libre en suivant un\n chemin prévu. La phase 3 débute dès que l\'un des joueurs est réduit à 3 pions. \n\n PHASE 3 - Le saut : Celui qui ne possède plus que trois pions peut alors se \n déplacer en sautant où il veut. Le jeu s\'achève quand un joueur n\'a plus que\n deux pions ou ne peut plus jouer, il est alors le perdant.'
Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
    row=1, column=0, padx=10, pady=10, sticky=W)

canPion = Canvas(sousframe2, width=506, heigh=70, bg='grey')
canPion.grid(row=2, column=0, sticky=(W), padx=10, pady=10)



##-----La grille-----##
lignes = []





##-----Evenements-----##



dessin.bind("<Button-1>",posevisuel)






##-----Programme principal-----##
init_game()
reinit()
FenêtreP.mainloop()                      # Boucle d'attente des événements