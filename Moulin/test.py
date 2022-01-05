from tkinter import *
from random import *

def dam():
    global x1,x2,y1,y2,couleur
    ite,i=0,1
    while x1<200 and y1 < 200:
        can.create_rectangle(x1,y1,x2,y2,fill=couleur)
        i,ite,x1,x2 = i+1,ite+1,x1+20,x2+20
        if ite == 10:
            y1,y2=y1+20,y2+20
            i,ite,x1,x2=i+1,0,0,20
        if i%2 == 0:
            couleur='white'
        else: couleur="blue"

x1,y1,x2,y2=0,0,20,20
x3,y3,x4,y4=5,5,15,15
caseChoisie = []
couleur = 'blue'

def pions():
    global x3,x4,y3,y4,caseChoisie
    ite=0
    while x3 < 195 and y3 < 195:
        caseChoisie.append([x3,y3,x4,y4])
        ite, x3, x4 = ite + 1, x3 + 20, x4 + 20
        if ite == 10:
            y3, y4 = y3 + 20, y4 + 20
            ite, x3, x4 = 0, 5, 15


    nbr=choice(caseChoisie)

    can.create_oval(nbr[0],nbr[1], nbr[2], nbr[3], fill='red')




fen = Tk()
can = Canvas (fen,width=200,heigh=200,bg='ivory')
b1 = Button(fen, text='Damier',command=dam)
b2 = Button(fen, text='Pion',command=pions)
can.pack(side=TOP,padx=5,pady=5)
b1.pack(side = LEFT, padx=3,pady=3)
b2.pack(side = RIGHT, padx=3,pady=3)
fen.mainloop()