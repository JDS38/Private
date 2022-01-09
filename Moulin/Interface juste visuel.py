from tkinter import *
from tkinter.font import names
from tkinter.ttk import *

inters = []
moulins = []




def fctSousMenu1():  # Action associée au sous-menu 1 du menu 1
    print('J vs J')

def fctSousMenu2():  # Action associée au sous-menu 1 du menu 1
    print('J vs IA')

def fctSousMenu3():  # Action associée au sous-menu 1 du menu 1
    print('Sauver')

def fctSousMenu4():  # Action associée au sous-menu 1 du menu 1
    print('Charger')

def reinit():
    """Cette fonction ré-initialise les variables globales."""

def visuel():
    #----------------------------------------Initialisation fenêtre Graphique------------------------------------------
    FenêtreP = Tk()
    FenêtreP.title("Jeu du Moulin®")
    FenêtreP.geometry('1220x595+400+100')
    FenêtreP.config(bg='lightgray')
    FenêtreP.option_add('*tearOff', FALSE)  # Nécessaire avec windows

    #----------------------------------------Menu------------------------------------------
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
    #menu3.add_separator()  # Barre de séparation aprés




    mainframe = Frame(FenêtreP)
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    FenêtreP.columnconfigure(0, weight=1)
    FenêtreP.rowconfigure(0, weight=1)

    s = Style()
    s.configure('TFrame', background='gray')

    s2 = Style()
    s2.configure('new.TFrame', background='lightgray')

    sousframe1 = Frame(mainframe, relief=SUNKEN, style='new.TFrame')
    sousframe1.grid(row=0, column=0, sticky=(W, E), padx=10, pady=25)
    sousframe2 = Frame(mainframe, relief=SUNKEN, style='new.TFrame')
    sousframe2.grid(row=0, column=1, sticky=(N, E), padx=10, pady=25)


    can = Canvas(sousframe1, width=500, heigh=500, bg='white')
    can.grid(row=0, column=0, sticky=(W, N), padx=10, pady=5)

    #cadre ext
    can.create_line(10, 10, 490, 10)
    can.create_line(10, 490, 490, 490)
    can.create_line(10, 10, 10, 490)
    can.create_line(490, 10, 490, 490)

    #cadre millieu
    can.create_line(80, 80, 420, 80)
    can.create_line(80, 420, 420, 420)
    can.create_line(80, 80, 80, 420)
    can.create_line(420, 80, 420, 420)

    #cadre intérieure
    can.create_line(150, 150, 350, 150)
    can.create_line(150, 350, 350, 350)
    can.create_line(150, 150, 150, 350)
    can.create_line(350, 150, 350, 350)

    #croix
    can.create_line(249, 10, 249, 150)
    can.create_line(249, 350, 249, 490)
    can.create_line(10, 249, 150, 249)
    can.create_line(350, 249, 490, 249)


    # ligneInter 1
    can.create_oval(5, 5, 15, 15, fill='black', tags="inter1")
    can.create_oval(244, 5, 254, 15, fill='black', tags="inter2")
    can.create_oval(485, 5, 495, 15, fill='black', tags="inter3")
    # ligneInter 2
    can.create_oval(75, 75, 85, 85, fill='black', tags="inter4")
    can.create_oval(244, 75, 254, 85, fill='black', tags="inter5")
    can.create_oval(415, 75, 425, 85, fill='black', tags="inter6")
    # ligneInter 3
    can.create_oval(145, 145, 155, 155, fill='black', tags="inter7")
    can.create_oval(244, 145, 254, 155, fill='black', tags="inter8")
    can.create_oval(345, 145, 355, 155, fill='black', tags="inter9")
    # ligneInter 4
    can.create_oval(5, 244, 15, 254, fill='black', tags="inter10")
    can.create_oval(75, 244, 85, 254, fill='black', tags="inter11")
    can.create_oval(145, 244, 155, 254, fill='black', tags="inter12")
    can.create_oval(345, 244, 355, 254, fill='black', tags="inter13")
    can.create_oval(415, 244, 425, 254, fill='black', tags="inter14")
    can.create_oval(485, 244, 495, 254, fill='black', tags="inter15")
    # ligneInter 5
    can.create_oval(145, 345, 155, 355, fill='black', tags="inter16")
    can.create_oval(244, 345, 254, 355, fill='black', tags="inter17")
    can.create_oval(345, 345, 355, 355, fill='black', tags="inter18")
    # ligneInter 6
    can.create_oval(75, 415, 85, 425, fill='black', tags="inter19")
    can.create_oval(244, 415, 254, 425, fill='black', tags="inter20")
    can.create_oval(415, 415, 425, 425, fill='black', tags="inter21")
    # ligneInter 7
    can.create_oval(5, 485, 15, 495, fill='black', tags="inter22")
    can.create_oval(244, 485, 254, 495, fill='black', tags="inter23")
    can.create_oval(485, 485, 495, 495, fill='black', tags="inter24")


    texte = ' Chaque joueur dispose de 9 pions de sa couleur.  L\'objectif du jeu est de \n retirer les pions de l\'adversaire sur le damier ou de le bloquer afin qu\'il \n ne puisse plus jouer.'
    Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
        row=0, column=0, padx=10, pady=10, sticky=(W, E))

    texte = ' PHASE 1 - La pose : Tant qu\'il en possède encore, chaque joueur place\n à tour de rôle un pion sur une intersection libre. La phase 2 débute après\n que les joueurs ont placé tous leurs pions. \n\n PHASE 2 - Le mouvement : Lorsqu\'il n\'a plus de pion à poser, chaque joueur fait\n glisser l\'un de ses pions vers une intersection voisine libre en suivant un\n chemin prévu. La phase 3 débute dès que l\'un des joueurs est réduit à 3 pions. \n\n PHASE 3 - Le saut : Celui qui ne possède plus que trois pions peut alors se \n déplacer en sautant où il veut. Le jeu s\'achève quand un joueur n\'a plus que\n deux pions ou ne peut plus jouer, il est alors le perdant.'
    Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
        row=1, column=0, padx=10, pady=10, sticky=W)

    canPion = Canvas(sousframe2, width=506, heigh=70, bg='grey')
    canPion.grid(row=2, column=0, sticky=(W), padx=10, pady=10)

    ##-----Création des zones de texte-----##
    message=Label(FenêtreP, text='Tour du Joueur 1')
    message.grid(row = 0, column = 0, columnspan=1, padx=215, pady=3, sticky = N+W)


    ##-----Création des boutons-----##
    bouton_quitter = Button(FenêtreP, text='Quitter', command=FenêtreP.destroy)
    bouton_quitter.grid(row = 0, column = 0, padx=458, pady=3, sticky = S+W)

    bouton_reload = Button(FenêtreP, text='Recommencer', command=reinit)
    bouton_reload.grid(row = 0, column = 0, padx=222, pady=3, sticky = S+W)

    can.bind("<Button-1>")
    can.bind("<Button-3>")

    phase_jeu(1)

    mainloop()

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


    def deplacement(self, depart, pion, destination):
        pion.X = destination.X
        pion.Y = destination.Y
        pion.InMoulin = False
        grille.area[depart.X][depart.Y] = 1
        grille.area[destination.X][destination.Y] = self.ReprPion
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
        if moulin.Inter1.Occupee == True and moulin.Inter1.pion.color == joueurencours.nom:
            if moulin.Inter2.Occupee == True and moulin.Inter2.pion.color == joueurencours.nom:
                if moulin.Inter3.Occupee == True and moulin.Inter3.pion.color == joueurencours.nom:
                    if moulin.Inter1.pion.InMoulin == False or moulin.Inter2.pion.InMoulin == False or moulin.Inter3.pion.InMoulin == False :
                        print("Moulin réalisé par ", joueurencours.nom, "capturez un pion adverse. Moulin réalisé :",moulin.Inter1.X,moulin.Inter1.Y,",",moulin.Inter2.X,moulin.Inter2.Y,",",moulin.Inter3.X,moulin.Inter3.Y)
                        moulin.Inter1.pion.InMoulin = True
                        moulin.Inter2.pion.InMoulin = True
                        moulin.Inter3.pion.InMoulin = True
                        if joueurencours.nom =="Joueur 1":
                            PionLibreJ2=0
                            for pion in joueur2.listePionsEnJeu:
                                if pion.InMoulin == False:
                                    print(pion.X, pion.Y)
                                    PionLibreJ2 +=1
                            PionMoulinJ2 = 0
                            for pion in joueur2.listePionsEnJeu:
                                if pion.InMoulin == True:
                                    print(pion.X, pion.Y)
                                    PionMoulinJ2 += 1
                            print("Il y a donc : ",PionLibreJ2, "pions hors d'un moulin")
                            if PionLibreJ2 != 0:
                                Capture(joueur2)
                            else:

                                print("Il y a donc : ", PionMoulinJ2, "pions dans un moulin")
                                CaptureInMoulin(joueur2)

                        if joueurencours.nom == "Joueur 2":
                            PionLibreJ1=0
                            for pion in joueur1.listePionsEnJeu:
                                if pion.InMoulin == False:
                                    print(pion.X, pion.Y)
                                    PionLibreJ1 +=1
                            PionMoulinJ1 = 0
                            for pion in joueur1.listePionsEnJeu:
                                if pion.InMoulin == True:
                                    print(pion.X, pion.Y)
                                    PionMoulinJ1 += 1
                            print("Il y a donc : ",PionLibreJ1, "pions hors d'un moulin")
                            if PionLibreJ1 !=0:
                                Capture(joueur1)
                            else:

                                print("Il y a donc : ", PionMoulinJ1, "pions dans un moulin")
                                CaptureInMoulin(joueur1)

def Capture(joueuradverse):

    capturee = False

    while capturee == False :
        capture = input("\n Faite votre choix parmi les moulins précédement cité : Entrez les coordonnées du pion à capturer x,y: ")
        if len(capture) < 3:
            print("Choix impossible, entrez un choix possible")
        elif capture[0].isnumeric() and capture[2].isnumeric():
            for pion in joueuradverse.listePionsEnJeu :
                if int(capture[0])==pion.X and int(capture[2])==pion.Y and pion.InMoulin == False :
                    for inter in inters:
                        if inter.X == pion.X and inter.Y == pion.Y:
                            inter.Occupee = False
                            grille.area[inter.X][inter.Y] = 1
                    joueuradverse.listePionsEnJeu.remove(pion)
                    capturee = True
                    print("Pion supprimé")
                    print("Pion hors moulin restant à ",joueuradverse.nom,":")
                    for pion in joueuradverse.listePionsEnJeu:
                        if pion.InMoulin == False:
                            print(pion.X, pion.Y)
                    print("Pion dans moulin restant à ", joueuradverse.nom, ":")
                    for pion in joueuradverse.listePionsEnJeu:
                        if pion.InMoulin == True :
                            print(pion.X, pion.Y)
                else:
                    print("Intersection inexistante")
        else:
            print("Intersection inexistante ou incorrecte")

def CaptureInMoulin(joueuradverse):

    capturee = False

    while capturee == False :
        capture = input("\n Faite votre choix parmi les moulins précédement cité : Entrez les coordonnées du pion à capturer x,y: ")
        if len(capture) >= 3:
            if capture[0].isnumeric() and capture[2].isnumeric():
                for pion in joueuradverse.listePionsEnJeu :
                    if int(capture[0])==pion.X and int(capture[2])==pion.Y and pion.InMoulin == True :
                        joueuradverse.listePionsEnJeu.remove(pion)
                        capturee = True
                        print("Pion supprimé")
                        print("Pion hors moulin restant à ",joueuradverse,":")
                        for pion in joueuradverse.listePionsEnJeu:
                            if pion.InMoulin == False:
                                print(pion.X, pion.Y)
                        print("Pion dans moulin restant à ", joueuradverse, ":")
                        for pion in joueuradverse.listePionsEnJeu:
                            if pion.InMoulin == True :
                                print(pion.X, pion.Y)
                    else:
                        print("Pas de pion dans cette intersection ou intersection inexistante")
            else:
                print("Intersection incorrecte")
        else:
            print("Intersection incorrecte")

def joue(event):
    clic = event.x, event.y
    item = can.find_closest(*clic)
    if(len(canPion.find_withtag('pionBleu'))) > 0:  # pose
        if can.type(item) == 'oval' and can.gettags(item)[0] != 'rouge' and can.gettags(item)[0] != 'bleu':
            # récupération du tag de l'inter permettant de faire le lien avec le GE
            inter = can.gettags(item)[0]
            print(inter)
            x1, y1, x2, y2 = can.coords(item[0])
            x1 -= 4
            y1 -= 4
            x2 += 4
            y2 += 4
            can.create_oval(x1, y1, x2, y2, fill='blue',
                            outline='lightgrey', tags='bleu')
            canPion.delete(canPion.find_withtag('pionBleu')[
                len(canPion.find_withtag('pionBleu'))-1])
        else:
            print('wouaf')
    elif can.type(item) == 'oval' and str(canPion.find_withtag('pionBleu')) == '()' and len(can.find_withtag('bleu'))-1 > 3:  # mouvement
        print('miam')

def PhasePose(joueuractuel):
    ok = False
    print("intersections disponibles:")
    count = 0
    for inter in inters:
        if inter.Occupee == False:
            if count < 5:
                print(inter.X, inter.Y, end="    ")
                count += 1
            else:
                print(inter.X, inter.Y)
                count = 0
    while ok == False:

        coo = event.x, event.y
        if len(coo) < 3:
            print("Choix impossible, entrez un choix possible")
        elif coo[0].isnumeric() and coo[2].isnumeric():
            if (joueuractuel.pose(int(coo[0]), int(coo[2])) == True):
                ok = True
            else:
                print("Intersection ocupée ou inexistante")
        else:
            print("coordonnees invalides")
    print(f"\npions restant à poser pour le {joueuractuel.nom}: {joueuractuel.pionRestants}\n")
    VerifMoulin(joueuractuel)

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

    moulins.append(Moulin(inters[8],inters[12],inters[17]))
    moulins.append(Moulin(inters[5],inters[13],inters[20]))
    moulins.append(Moulin(inters[2],inters[14],inters[23]))

    moulins.append(Moulin(inters[1],inters[4],inters[7]))
    moulins.append(Moulin(inters[14],inters[13],inters[12]))
    moulins.append(Moulin(inters[22],inters[19],inters[16]))
    moulins.append(Moulin(inters[9],inters[10],inters[11]))
    print("init faite")

'''    print("\nChoix du mode de jeu :")
    print("1. Humain vs Humain")
    print("2. Humain vs Ordinateur")
    mode = input("Indiquez votre choix : ")
    if mode == '1':
        phase_jeu(2)  # phase de pose j vs j

    if mode == '2':
        phase_jeu(20)  # phase de pose j vs ordinateur
    if mode != '1' and mode != '2':
        print("Choix impossible, entrez un choix possible")
        init_game()'''

def Get_Info_Deplacement(joueurEnCours):
    voisinDipo = []
    selectedPion = None
    depart = None

    while len(voisinDipo) == 0:
        print(f"{joueurEnCours.nom} sélectionnez un pion parmi:")
        affiche_pion_mvt_possible(joueurEnCours)
        cooValide = False
        while cooValide == False:
            coopion = input("Entrez les coordonées du pion sous la forme x,y: ")
            if len(coopion) >= 3:
                if coopion[0].isnumeric() and coopion[2].isnumeric():
                    for pion in joueurEnCours.listePionsEnJeu:
                        if pion.X == int(coopion[0]) and pion.Y == int(coopion[2]):
                            cooValide = True
                            selectedPion = pion
                            break
                    if cooValide == False:
                        print("Vous n'avez aucun pion sur ces coordonnées")
                else:
                    print("Coordonées invalides")
            else:
                print("Coordonées invalides")

        for inter in inters:
            if selectedPion.X == inter.X and selectedPion.Y == inter.Y:
                depart = inter
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
        if len(destCoo) >=3:
            if destCoo[0].isnumeric() and destCoo[2].isnumeric():
                for v in voisinDipo:
                    if v.X == int(destCoo[0]) and v.Y == int(destCoo[2]):
                        print(f"pion({selectedPion.X}, {selectedPion.Y}) déplacé en ({v.X}, {v.Y})")
                        joueurEnCours.deplacement(depart, selectedPion, v)
                        destValide = True
            else:
                print("coordonnees invalides")
        else:
            print("coordonnees invalides")
    VerifMoulin(joueurEnCours)

def Get_Info_Saut(joueurEnCours):
    interDispo = []
    selectedPion = None
    depart = None

    print(f"{joueurEnCours.nom} sélectionnez un pion parmi:")
    affiche_liste_pion_en_jeu(joueurEnCours)
    cooValide = False
    while cooValide == False:
        coopion = input("Entrez les coordonées du pion sous la forme x,y: ")
        if len(coopion) >= 3:
            if coopion[0].isnumeric() and coopion[2].isnumeric():
                for pion in joueurEnCours.listePionsEnJeu:
                    if pion.X == int(coopion[0]) and pion.Y == int(coopion[2]):
                        cooValide = True
                        selectedPion = pion
                        break
                if cooValide == False:
                    print("Vous n'avez aucun pion sur ces coordonnées")
            else:
                print("Coordonées invalides")
        else:
            print("Coordonées invalides")

    for inter in inters:
        if selectedPion.X == inter.X and selectedPion.Y == inter.Y:
            depart = inter

            print("Intersections voisines disponibles: ")
            for intersec in inters:
                if intersec.Occupee == False:
                    print(intersec.X, intersec.Y)
                    interDispo.append(intersec)

    destValide = False
    while destValide == False:
        destCoo = input("Entrez la destination sous la forme x,y: ")
        if len(destCoo) >=3:
            if destCoo[0].isnumeric() and destCoo[2].isnumeric():
                for i in interDispo:
                    if i.X == int(destCoo[0]) and i.Y == int(destCoo[2]):
                        print(f"pion({selectedPion.X}, {selectedPion.Y}) déplacé en ({i.X}, {i.Y})")
                        joueurEnCours.deplacement(depart, selectedPion, i)
                        destValide = True
            else:
                print("coordonnees invalides")
        else:
            print("coordonnees invalides")
    VerifMoulin(joueurEnCours)

def affiche_liste_pion_en_jeu(joueur):
    for pion in joueur.listePionsEnJeu:
        print(pion.X, pion.Y)

def affiche_pion_mvt_possible(joueurEnCours):
    for pion in joueurEnCours.listePionsEnJeu:
        for intersec in inters:
            if pion.X == intersec.X and pion.Y == intersec.Y:
                voisins = intersec.Voisins[intersec.Nom]
                for voisin in voisins:
                    found = False
                    for inter in inters:
                        if inter.Nom == voisin:
                            if inter.Occupee == False:
                                print(intersec.X, intersec.Y)
                                found = True
                        if found == True:
                            break
                    if found == True:
                        break

def phase_jeu(status):
    match status:

        case 1:
            init_game()



        # humain vs humain
        case 2:
            print(grille)
            print(f"Dans la grille de jeu:\nles pions du joueur 1 son représentés par {joueur1.ReprPion}\nles pions du joueur 2 sont représentés par {joueur2.ReprPion}\net les intersections sont représentées par des 1")
            print("\nPhase de Pose Joueur vs Joueur")
            print("Pion à poser par le joueur 1 : ",joueur1.pionRestants)
            print("Pion à poser par le joueur 2 : ",joueur2.pionRestants, "\n")
            while joueur2.pionRestants > 0:
                PhasePose(joueur1)
                print(grille)
                PhasePose(joueur2)
                print(grille)

            phase_jeu(3)

        case 3:
            print()
            print("Phase de Mouvement Joueur vs Joueur")

            #while len(joueur1.listePionsEnJeu)>2 or len(joueur2.listePionsEnJeu)>2 :


            print("\nPhase de Mouvement Joueur vs Joueur")
            while len(joueur1.listePionsEnJeu) > 2 and len(joueur2.listePionsEnJeu) > 2:
                if len(joueur1.listePionsEnJeu) > 3:
                    Get_Info_Deplacement(joueur1)
                else:
                    print("joueur 1 n'a plus que 3 pion. Phase de saut pour joueur 1")
                    Get_Info_Saut(joueur1)
                print(grille)
                if len(joueur2.listePionsEnJeu) > 3:
                    Get_Info_Deplacement(joueur2)
                else:
                    print("joueur 2 n'a plus que 3 pion. Phase de saut pour joueur 2")
                    Get_Info_Saut(joueur2)
                print(grille)

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


##-----Programme principal-----##


if __name__ == '__main__':

    joueur1 = Joueur("Joueur 1", 9, 'X')
    joueur2 = Joueur("Joueur 2", 9, '#')

    visuel()