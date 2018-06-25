#!/usr/bin/env python3
import tkinter as tk
def distance():
    lab1.configure(text = "label")

def move(lr,ud):
    global x1,y1
    x1,y1 = x1+lr, y1+ud
    can1.coords(a, x1,y1, x1+s1,y1+s1)

def left():
    move(-10, 0)

def right():
    move(10, 0)

def up():
    move(0, -10)

def down():
    move(0, 10)

fen1 = tk.Tk()
fen1.title("Star")
can1 = tk.Canvas(fen1,bg="dark grey")
can1.pack(side = 'top', padx=5, pady=5)
lab1 = tk.Label(fen1)
lab1.pack(side ='bottom', padx=3, pady=3)

x1, y1, x2, y2 = 10, 10, 100, 100
s1,s2 = 70,30
a = can1.create_oval(x1,y1,x1+s1,y1+s1,fill='red')
b = can1.create_oval(x2,y2,x2+s2,y2+s2,fill='blue')

right()
distance()
fen1.mainloop()
