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
    Plateau(grille)

class Plateau():
    def __init__(self,n):
        self.n = [[0] * n for i in range(n)]

print(Plateau.n)