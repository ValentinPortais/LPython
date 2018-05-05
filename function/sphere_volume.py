#Calcul the volume of a sphere
from math import *

def cube(n):
  return n**3

def volumeSphere(r):
  return 4* pi *cube(r) / 3

r = float(input('Enter a value for the radius'))
print('The volume of this sphere is', volumeSphere(r))
