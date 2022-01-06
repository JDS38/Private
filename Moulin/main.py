inters = []
moulins = []

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

    def __init__(self, nom, pionsRestants):
        self.nom = nom
        self.pionRestants = pionsRestants
        self.listePionsEnJeu = []

    def pose(self, x, y):
        for inter in inters:
            if x == inter.X and y == inter.Y and inter.Occupee == False:
                pion = Pion(x, y, self.nom)
                inter.Occupee=True
                inter.pion = pion
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

    def __init__(self, x, y, nom):
        self.X = x
        self.Y = y
        self.color = nom
        self.InMoulin = False


class Intersection:
    def __init__(self, nom, x, y):
        self.Nom = nom
        self.X = x
        self.Y = y
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

def VerifMoulin(joueurencours):
    for moulin in moulins :
        # les 4 centres de moulins possibles à l'extérieure
        #print("for")
        if moulin.Inter1.Occupee == True and moulin.Inter1.pion.color == joueurencours.nom:
            #print("if1")
            if moulin.Inter2.Occupee == True and moulin.Inter2.pion.color == joueurencours.nom:
                #print("if2")
                if moulin.Inter3.Occupee == True and moulin.Inter3.pion.color == joueurencours.nom:
                    if moulin.Inter1.pion.InMoulin == False or moulin.Inter2.pion.InMoulin == False or moulin.Inter3.pion.InMoulin == False :
                        print("Moulin réalisé par ", joueurencours.nom, "capturez un pion adverse",moulin.Inter1.X,moulin.Inter1.Y,",",moulin.Inter2.X,moulin.Inter2.Y,",",moulin.Inter3.X,moulin.Inter3.Y)
                        moulin.Inter1.pion.InMoulin = True
                        moulin.Inter2.pion.InMoulin = True
                        moulin.Inter3.pion.InMoulin = True
                        if joueurencours.nom =="Joueur 1":
                            for pion in joueur2.listePionsEnJeu:
                                if pion.InMoulin == False:
                                    print(pion.X, pion.Y)
                            Capture(joueur2)
                        if joueurencours.nom == "Joueur 2":
                            for pion in joueur1.listePionsEnJeu:
                                if pion.InMoulin == False:
                                    print(pion.X, pion.Y)
                            Capture(joueur1)

def Capture(joueuradverse):

    capturé = False

    while capturé == False :
        capture = input("\n Bravo vous avez fait un moulin : Entrez les coordonnées du pion à capturer x,y: ")
        if int(capture[0]) and int(capture[2]):
            for pion in joueuradverse.listePionsEnJeu :
                if int(capture[0])==pion.X and int(capture[2])==pion.Y and pion.InMoulin == False :
                    joueuradverse.listePionsEnJeu.remove(pion)
                    capturé = True
                    print("Pion supprimé")
                    for pion in joueuradverse.listePionsEnJeu:
                        print(pion.X, pion.Y)
                #else:
                    #print("Pas de pion ou c'est votre pion")


def init_game():

    inters.append(Intersection("inter1", 1, 1))
    inters.append(Intersection("inter2", 1, 4))
    inters.append(Intersection("inter3", 1, 7))
    inters.append(Intersection("inter4", 2, 2))
    inters.append(Intersection("inter5", 2, 4))
    inters.append(Intersection("inter6", 2, 6))
    inters.append(Intersection("inter7", 3, 3))
    inters.append(Intersection("inter8", 3, 4))
    inters.append(Intersection("inter9", 3, 5))
    inters.append(Intersection("inter10", 4, 1))
    inters.append(Intersection("inter11", 4, 2))
    inters.append(Intersection("inter12", 4, 3))
    inters.append(Intersection("inter13", 4, 5))
    inters.append(Intersection("inter14", 4, 6))
    inters.append(Intersection("inter15", 4, 7))
    inters.append(Intersection("inter16", 5, 3))
    inters.append(Intersection("inter17", 5, 4))
    inters.append(Intersection("inter18", 5, 5))
    inters.append(Intersection("inter19", 6, 2))
    inters.append(Intersection("inter20", 6, 4))
    inters.append(Intersection("inter21", 6, 6))
    inters.append(Intersection("inter22", 7, 1))
    inters.append(Intersection("inter23", 7, 4))
    inters.append(Intersection("inter24", 7, 7))

    moulins.append(Moulin(inters[0],inters[1],inters[2]))
    moulins.append(Moulin(inters[3],inters[4],inters[5]))
    moulins.append(Moulin(inters[6],inters[7],inters[8]))

    moulins.append(Moulin(inters[15],inters[16],inters[17]))
    moulins.append(Moulin(inters[18],inters[19],inters[20]))
    moulins.append(Moulin(inters[21],inters[22],inters[23]))

    moulins.append(Moulin(inters[0],inters[9] ,inters[21]))
    moulins.append(Moulin(inters[3],inters[10],inters[18]))
    moulins.append(Moulin(inters[6],inters[11],inters[15]))

    moulins.append(Moulin(inters[17],inters[16],inters[15]))
    moulins.append(Moulin(inters[20],inters[19],inters[18]))
    moulins.append(Moulin(inters[23],inters[22],inters[21]))

    moulins.append(Moulin(inters[1],inters[4],inters[7]))
    moulins.append(Moulin(inters[14],inters[13],inters[12]))
    moulins.append(Moulin(inters[22],inters[19],inters[16]))
    moulins.append(Moulin(inters[9],inters[10],inters[11]))

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
            print("Pion à poser par le joueur 1 : ",joueur1.pionRestants)
            print("Pion à poser par le joueur 2 : ",joueur2.pionRestants)
            while joueur2.pionRestants > 0:

                ok = False
                while ok  == False:
                    coo = input("\n Joueur 1 Entrez les coordonnées de pose sous la forme x,y: ")
                    if coo[0].isnumeric() and coo[2].isnumeric():
                        if(joueur1.pose(int(coo[0]), int(coo[2])) == True):
                            ok = True
                        else:
                            print("Intersection ocupée")
                    else:
                        print("coordonnees invalides")
                print(joueur1.pionRestants)
                #VerifMoulin(joueur1)
                ok = False
                while ok == False:
                    coo = input("\n Joueur 2 Entrez les coordonnées de pose sous la forme x,y: ")
                    if coo[0].isnumeric() and coo[2].isnumeric():
                        if (joueur2.pose(int(coo[0]), int(coo[2])) == True):
                            ok = True
                        else:
                            print("Intersection ocupée")
                    else:
                        print("coordonnees invalides")
                print(joueur2.pionRestants)
                #VerifMoulin(joueur2)


            phase_jeu(3)

        case 3:
            print()
            print("Phase de Mouvement Joueur vs Joueur")

            #while len(joueur1.listePionsEnJeu)>2 or len(joueur2.listePionsEnJeu)>2 :

            voisinDipo = []
            selectedPion = None
            depart = None
            coopion = ""
            print("\nPhase de Mouvement Joueur vs Joueur")

            while len(voisinDipo) == 0:
                print("Joueur 1 sélectionnez un pion parmi:")
                for pion in joueur1.listePionsEnJeu:
                    print(pion.X, pion.Y)
                cooValide = False
                while cooValide == False:
                    coopion = input("Entrez les coordonées du pion sous la forme X,Y")
                    if coopion[0].isnumeric() and coopion[2].isnumeric():
                        for pion in joueur1.listePionsEnJeu:
                            if pion.X == int(coopion[0]) and pion.Y == int(coopion[2]):
                                cooValide = True
                                selectedPion = pion
                                break
                    else:
                        print("Entrez des coordonnées valides")

                    if cooValide == False:
                        print("Vous n'avez aucun pion sur ces coordonnées")

                for inter in inters:
                    if selectedPion.X == inter.X and selectedPion.Y == inter.Y:
                        depart = inter
                    if inter.X == int(coopion[0]) and inter.Y == int(coopion[2]):
                        voisins = inter.Voisins[inter.Nom]

                        print("Intersections voisines disponibles: ")
                        for intersec in inters:
                            for voisin in voisins:
                                if intersec.Nom == voisin:
                                    if intersec.Occupee == False:
                                        print(intersec.X, intersec.Y)
                                        voisinDipo.append(intersec)
                if len(voisinDipo) == 0:
                    print("ce pion n'a pas de mouvement possible sélectionnez un autre pion")

            destValide = False
            while destValide == False:
                destCoo = input("Entrez la destination sous la forme X,Y")
                if destCoo[0].isnumeric() and destCoo[2].isnumeric():
                    for v in voisinDipo:
                        if v.X == int(destCoo[0]) and v.Y == int(destCoo[2]):
                            print(f"pion({selectedPion.X}, {selectedPion.Y}) déplacé en ({v.X}, {v.Y})")
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

    joueur1 = Joueur("Joueur 1", 9)
    joueur2 = Joueur("Joueur 2", 9)

    phase_jeu(1)





