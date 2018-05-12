from turtle import *

def triangle(tsize,tcolor,tangle):
  color(tcolor)
  i=0
  while (i<3):
    forward(tsize)
    right(120)
    i+=1

def stars5(scolor,ssize):
  i=0
  angle=72
  while (i<5):
    forward(ssize)
    right(144)
    i += 1

