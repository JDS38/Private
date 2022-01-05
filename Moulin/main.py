inters = []

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

    def str(self):
        res = ""
        for i in range(len(self.area)):
            for j in range(len(self.area[i])):
                res += str(self.area[i][j]) + " "
            res += "\n"
        return res


grille = Damier()


class Joueur:

    def __init__(self, couleur, pionsRestants):
        self.couleur = couleur
        self.pionRestants = pionsRestants
        self.listePionsEnJeu = []

    def pose(self, x, y):
        for inter in inters:
            if x == inter.X and y == inter.Y and inter.Occupee == False:
                inter.Occupee = True
                pion = Pion(x, y, self.couleur)
                grille.area[x][y] = pion
                self.listePionsEnJeu.append(pion)
                self.pionRestants -= 1
                return True
        return False

    def deplacement(self, depart, pion, destination):
        pion.X = destination.X
        pion.Y = destination.Y
        destination.pion = pion
        destination.Occupee = True
        depart.pion = None
        depart.Occupee = False




class Pion:

    def __init__(self, x, y, couleur):
        self.X = x
        self.Y = y
        self.couleur = couleur
        self.InMoulin = False


class Intersection:
    def __init__(self, nom, x, y):
        self.Nom = nom
        self.X = x
        self.Y = y
        self.Occupee = False
        self.pion = None
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


def init_game():

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

    print("\nChoix du mode de jeu :")
    print("1. Humain vs Humain")
    print("2. Humain vs Ordinateur")
    mode = input("Indiquez votre choix : ")
    if mode == '1':
        phase_jeu(2)  # phase de pose j vs j

    if mode == '2':
        phase_jeu(20)  # phase de pose j vs ordinateur
    if mode != '1' and mode != '2':
        print("Choix impossible, entrez un choix possible")
        init_game()

def phase_jeu(status):
    match status:

        case 1:
            init_game()

        # humain vs humain
        case 2:
            print()
            print("Phase de Pose Joueur vs Joueur")
            print("Pion à poser par le joueur 1 : ", joueur1.pionRestants)
            print("Pion à poser par le joueur 2 : ", joueur2.pionRestants)
            while joueur2.pionRestants > 0:

                ok = False
                while ok == False:
                    coo = input("\n Joueur 1 Entrez les coordonnées de pose sous la forme x,y: ")
                    if int(coo[0]) and int(coo[2]):
                        if (joueur1.pose(int(coo[0]), int(coo[2])) == True):
                            ok = True
                        else:
                            print("Intersection ocupée")
                    else:
                        print("coordonnees invalides")
                print(joueur1.pionRestants)
                ok = False
                while ok == False:
                    coo = input("\n Joueur 2 Entrez les coordonnées de pose sous la forme x,y: ")
                    if int(coo[0]) and int(coo[2]):
                        if (joueur2.pose(int(coo[0]), int(coo[2])) == True):
                            ok = True
                        else:
                            print("Intersection ocupée")
                    else:
                        print("coordonnees invalides")
                print(joueur2.pionRestants)
            phase_jeu(3)

        case 3:
            voisinDipo = []
            selectedPion = None
            depart = None
            coopion = ""
            print("\nPhase de Mouvement Joueur vs Joueur")
            print("Joueur 1 sélectionnez un pion parmi:")
            for pion in joueur1.listePionsEnJeu:
                print(pion.X, pion.Y)
            cooValide = False
            while cooValide == False:
                coopion = input("Entrez les coordonées du pion sous la forme X,Y")
                if int(coopion[0]) and int(coopion[2]):
                    for pion in joueur1.listePionsEnJeu:
                        if pion.X == int(coopion[0]) and pion.Y == int(coopion[2]):
                            cooValide == True
                            selectedPion = pion
                            break
                else:
                    print("Entrez des coordonnées valides")

                if cooValide == False:
                    print("Vous n'avez aucun pion sur ces coordonnées")

            for inter in inters:
                if selectedPion.X == inter.X and selectedPion.Y == inter.Y:
                    depart = inter
                if inter.X == int(coopion[0]) and inter.y == int(coopion[2]):
                    voisins = inter.Voisins[inter.Nom]

                    print("Intersections voisines disponibles: ")
                    for intersec in inters:
                        for voisin in voisins:
                            if intersec.Nom == voisin:
                                if intersec.Occupee == False:
                                    print(intersec.X, intersec.Y)
                                    voisinDipo.append(intersec)

            destValide = False
            while destValide == False:
                destCoo = input("Entrez la destination sous la forme X,Y")
                if int(destCoo[0]) and int(destCoo[2]):
                    for v in voisinDipo:
                        if v.X == destCoo[0] and v.Y == destCoo:
                            joueur1.deplacement(depart, selectedPion, v)
                            destValide = True
                else:
                    print("coordonnees invalides")


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




if __name__ == '__main__':

    joueur1 = Joueur("noir", 9)
    joueur2 = Joueur("blanc", 9)

    phase_jeu(1)