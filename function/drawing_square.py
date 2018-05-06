from turtle import *

def carre(csize,ccolor,cangle):
  "function which draws a square with a choosen color and size"
  color(ccolor)
  c=0
  while c < 4:
      forward(csize)
      right(90)
      c = c +1

