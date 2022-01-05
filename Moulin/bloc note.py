def fenetre_graph():
    # Creation d'une fenêtre avec la classe Tk :

    fenetre = Tk()
    # Ajout d'un titre à la fenêtre principale :
    fenetre.title("Moulin")
    # Définir les dimensions par défaut la fenêtre principale :
    fenetre.geometry("600x600")
    # Limiter les dimensions d’affichage de la fenêtre principale :
    fenetre.maxsize(900, 900)
    fenetre.minsize(500, 500)
    fenetre.config(bg="#ffe680")

    # Canvas
    canvas = Canvas(fenetre)
    canvas.pack()
    canvas.config(width=450, height=450)

    n = 7
    for i in range(n):
        for j in range(n):
            # cadre exterieure
            line = canvas.create_line(50, 50, 50, 400, fill='black', width=5)
            line = canvas.create_line(400, 50, 400, 400, fill='black', width=5)
            line = canvas.create_line(50, 50, 400, 50, fill='black', width=5)
            line = canvas.create_line(50, 400, 400, 400, fill='black', width=5)
            # cadre intermediaire

            line = canvas.create_line(100, 100, 100, 350, fill='black', width=5)
            line = canvas.create_line(350, 100, 350, 350, fill='black', width=5)
            line = canvas.create_line(100, 100, 350, 100, fill='black', width=5)
            line = canvas.create_line(100, 350, 350, 350, fill='black', width=5)

            # cadre interieure

            line = canvas.create_line(150, 150, 150, 300, fill='black', width=5)
            line = canvas.create_line(300, 150, 300, 300, fill='black', width=5)
            line = canvas.create_line(150, 150, 300, 150, fill='black', width=5)
            line = canvas.create_line(150, 300, 300, 300, fill='black', width=5)

            # ligne croisé

            line = canvas.create_line(225, 50, 225, 150, fill='black', width=5)
            line = canvas.create_line(225, 300, 225, 400, fill='black', width=5)
            line = canvas.create_line(50, 225, 150, 225, fill='black', width=5)
            line = canvas.create_line(300, 225, 400, 225, fill='black', width=5)

            fenetre.mainloop()


def phase_pose(tableau_jeu):
    for row in tableau_jeu:
        print(' '.join([str(elem) for elem in row]))


global Nbrpion1, Nbrpion2, Restepion1, Restepion2, grille, grillepast

def init_game():
    n = 8
    global Nbrpion1, Nbrpion2, Restepion1, Restepion2, grille
    grille = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):

            # cadre extérieure
            if (i == 1 or i == 4 or i == 7) and (j == 1 or j == 4 or j == 7):
                grille[i][j] = '9'
            # cadre intermédiaire
            if (i == 2 or i == 4 or i == 6) and (j == 2 or j == 4 or j == 6):
                grille[i][j] = '9'
            # cadre intérieure
            if (i == 3 or i == 4 or i == 5) and (j == 3 or j == 4 or j == 5):
                grille[i][j] = '9'
            # supprimer le centre
            if i == 4 and j == 4:
                grille[i][j] = '0'
    for row in grille:
        print(' '.join([str(elem) for elem in row]))

    Nbrpion1 = 9  # diminue à chaque pose pour Joueur 1
    Nbrpion2 = 9  # diminue à chaque pose  Joueur 2
    Restepion1 = 9  # diminue à chaque capture  Joueur 1
    Restepion2 = 9  # diminue à chaque capture  Joueur 2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init_game()