#Draw the olympics logo on a window
from tkinter import *

def olympics():
  "Draw the olympics circles"
  i=0
  coord=[[20,30], [120,30], [220, 30], [70,80], [170,80]]
  colors=['blue','black','red','yellow','green']

  while(i<len(colors)):
    x1, y1 = coord[i][0],coord[i][1]
    can1.create_oval(x1,y1,x1+90,y1+90,width =2, outline =colors[i])
    i+=1

#----Main Program----

fen1 = Tk()
can1 = Canvas(fen1,bg='white',height=200,width=350)
can1.pack(side=LEFT)
but1 = Button(fen1,text='Close',command=fen1.quit)
but1.pack(side=BOTTOM)
but2 = Button(fen1,text='Draw Olympics',command=olympics)
but2.pack()


fen1.mainloop()

fen1.destroy()

