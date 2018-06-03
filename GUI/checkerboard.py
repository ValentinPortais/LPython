#Checkboard in a Canvas
from tkinter import *
from math import *

def square(x,y,s,coul):
  can.create_polygon(x,y,x,y+s,x+s,y+s,x+s,y,fill=coul,outline='black')


#Draw checkboard function
def checkboard():
    i,x,s = 0, 0, 200/10
    y = x
    while i<10:
      if (i % 2 == 0 ):
        square(x,y,s,'blue')

      x+=20
      i+=1



  
x=200
fen = Tk()
can = Canvas(fen, width = x, height = x,bg='ivory')
can.pack(side=TOP,padx=5,pady=5)
b1 = Button(fen,text='checkboard',command=checkboard)
b1.pack(side=LEFT,padx=3,pady=3)
#b2 = Button(fen,text='pawn',command=pawn)
#b2.pack(side=RIGHT,padx=3,pady=3)
fen.mainloop()
