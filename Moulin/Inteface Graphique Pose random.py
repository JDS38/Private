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


# A Modifier

def rouge(event):
    clic = event.x, event.y
    item = can.find_closest(*clic)
    if(len(canPion.find_withtag('pionRouge'))) > 0:  # pose
        if can.type(item) == 'oval' and can.gettags(item)[0] != 'rouge' and can.gettags(item)[0] != 'bleu':
            # récupération du tag de l'inter permettant de faire le lien avec le GE
            inter = can.gettags(item)[0]
            print(inter)
            #Position et taille du point
            x1, y1, x2, y2 = can.coords(item[0])
            x1 -= 4
            y1 -= 4
            x2 += 4
            y2 += 4
            can.create_oval(x1, y1, x2, y2, fill='red',
                            outline='lightgrey', tags='rouge')
            canPion.delete(canPion.find_withtag('pionRouge')[
                len(canPion.find_withtag('pionRouge'))-1])
        else:
            print('wouaf')
    elif can.type(item) == 'oval' and str(canPion.find_withtag('pionRouge')) == '()' and len(can.find_withtag('rouge'))-1 > 3:  # mouvement
        print('miam')


def bleu(event):
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


texte = ' Chaque joueur dispose de 9 pions de sa couleur.  L\'objectif du jeu est de \n retirer les pions de l\'adversaire sur le damier ou de le bloquer afin qu\'il \n ne puisse plus jouer.'
Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
    row=0, column=0, padx=10, pady=10, sticky=(W, E))

texte = ' PHASE 1 - La pose : Tant qu\'il en possède encore, chaque joueur place\n à tour de rôle un pion sur une intersection libre. La phase 2 débute après\n que les joueurs ont placé tous leurs pions. \n\n PHASE 2 - Le mouvement : Lorsqu\'il n\'a plus de pion à poser, chaque joueur fait\n glisser l\'un de ses pions vers une intersection voisine libre en suivant un\n chemin prévu. La phase 3 débute dès que l\'un des joueurs est réduit à 3 pions. \n\n PHASE 3 - Le saut : Celui qui ne possède plus que trois pions peut alors se \n déplacer en sautant où il veut. Le jeu s\'achève quand un joueur n\'a plus que\n deux pions ou ne peut plus jouer, il est alors le perdant.'
Label(sousframe2, text=texte, font='impact', background='white', relief=GROOVE).grid(
    row=1, column=0, padx=10, pady=10, sticky=W)

canPion = Canvas(sousframe2, width=506, heigh=70, bg='grey')
canPion.grid(row=2, column=0, sticky=(W), padx=10, pady=10)

##-----Création des zones de texte-----##
message=Label(FenêtreP, text='Tour du joueur 1')
message.grid(row = 0, column = 0, columnspan=1, padx=215, pady=3, sticky = N+W)


##-----Création des boutons-----##
bouton_quitter = Button(FenêtreP, text='Quitter', command=FenêtreP.destroy)
bouton_quitter.grid(row = 0, column = 0, padx=458, pady=3, sticky = S+W)

bouton_reload = Button(FenêtreP, text='Recommencer', command=reinit)
bouton_reload.grid(row = 0, column = 0, padx=222, pady=3, sticky = S+W)

# A rendre dynamique avec le GE
nbPion = 9
x1 = 10
y1 = 10
x2 = 30
y2 = 30
for i in range(nbPion):
    canPion.create_oval(x1, y1, x2, y2, fill='red',
                        outline='lightgrey', tags=('pionRouge'))

    x1 += 30
    x2 += 30
x1 = 10
y1 = 40
x2 = 30
y2 = 60
for i in range(nbPion):
    canPion.create_oval(x1, y1, x2, y2, fill='blue',
                        outline='lightgray', tags=('pionBleu'))
    x1 += 30
    x2 += 30


can.bind("<Button-1>",bleu)
can.bind("<Button-3>",rouge)


##-----Programme principal-----##



FenêtreP.mainloop()                      # Boucle d'attente des événements

