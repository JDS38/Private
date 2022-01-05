class Joueur:

    def init(self, couleur, pionsRestants):
        self.couleur = couleur
        self.pionRestants = pionsRestants
        self.listePionsEnJeu = []

    def pose(self, x, y, ListIntersections):
        for inter in ListIntersections:
            if x == inter[0] and y == inter[1] and inter.occupee == False:
                pion = Pion(x, y, self.couleur)
                self.grille[x][y] = pion
                self.listePionsEnJeu.append(pion)
                self.pionRestants -= 1