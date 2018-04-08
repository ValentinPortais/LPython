#Calcul perimeter and area of a triangle
#Import math functions
from math import *

side1=int(input("Enter first mesure: "))
side2=int(input("Enter second mesure: "))
side3=int(input("Enter last mesure: "))

perim= side1 + side2 + side3
s = 1/2*perim
area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
print("The perimeter is:", perim)
print("The area is:", area)
