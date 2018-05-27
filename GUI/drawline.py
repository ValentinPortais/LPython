#Exercise using tkinter 
from tkinter import *
from random import randrange

#Event function definition
def drawline(x1,y1,x2,y2):
    "Draw a line in the canevas can1"
    global col
    can1.create_line(x1,y1,x2,y2,width=2,fill=col)

    #Change coordinates for the next line :
    y2, y1 = y2+10, y1-10

def drawline2():
    'Draw a cross in the canevas'
    x3 , y3, x4, y4 = 0 , 325 , 500, 325 #Cross coordinates
    can1.create_line(x3,y3,x4,y4)
    x3,y3,x4,y4 = 250, 0 , 250, 650
    can1.create_line(x3,y3,x4,y4)

def changecolor():
    "Random color change"
    global col
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8)    #get a random number from 0 to 7
    col = pal[c]

#----Main Program----

x1, y1, x2, y2 = 10, 190, 190, 10

col = 'dark green'      #Line color

#Building Main widget(master)
fen1 = Tk()
#Building Slaves widgets
can1 = Canvas(fen1,bg='dark grey',height=650,width=500)
can1.pack(side=LEFT)
but1 = Button(fen1,text='Close',command=fen1.quit)
but1.pack(side=BOTTOM)
but2 = Button(fen1,text='Draw a line',command=lambda: drawline(x1,y1,x2,y2))
but2.pack()
but3 = Button(fen1,text='Change Color',command=changecolor)
but3.pack()
but4 = Button(fen1,text='Scope',command=drawline2)
but4.pack()

fen1.mainloop() #Starting Event receptioner

fen1.destroy() # Destroying window
