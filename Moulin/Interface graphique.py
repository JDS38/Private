# L'importation de l’ensemble des éléments du paquet tkinter :

from tkinter import *


# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def create_grille():
    n = 7
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):

            # cadre exterieure
            if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6):
                a[i][j] = '1'
            # cadre intermediaire
            if (i == 1 or i == 3 or i == 5) and (j == 1 or j == 3 or j == 5):
                a[i][j] = '1'
            # cadre interieure
            if (i == 2 or i == 3 or i == 4) and (j == 2 or j == 3 or j == 4):
                a[i][j] = '1'
            # supprimer le centre
            if i == 3 and j == 3:
                a[i][j] = '0'
    for row in a:
        print(' '.join([str(elem) for elem in row]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    create_grille()
    print("- - - - - - -")


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