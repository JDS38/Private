def scope_test():
    def do_local():
        spam ="local spam"

    def do_nonlocal():
        nonlocal spam
        spam ="nonlocal spam"

    def do_global():
        global spam
        spam ="global spam"


    spam ="test spam"

    do_local()
    print("After local assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print()
    #scope_test()



class Grille:
    def __init__(self,m):
        self.plateau = [[0] * m for i in range(m)]

    def init_grille(self):
        for i in range(len(self.plateau)):
            for j in range(len(self.plateau[i])):
                # cadre extérieure
                if (i == 1 or i == 4 or i == 7) and (j == 1 or j == 4 or j == 7):
                    self.plateau[i][j] = '9'
                # cadre intermédiaire
                if (i == 2 or i == 4 or i == 6) and (j == 2 or j == 4 or j == 6):
                    self.plateau[i][j] = '9'
                # cadre intérieure
                if (i == 3 or i == 4 or i == 5) and (j == 3 or j == 4 or j == 5):
                    self.plateau[i][j] = '9'
                # supprimer le centre
                if i == 4 and j == 4:
                    self.plateau[i][j] = '0'

    def __str__(self):
        res = ""
        for h in range(len(self.plateau)):
            for i in range(len(self.area[h]))

c = Grille(8)

print(c.plateau)
c.init_grille()
print(c.plateau)
