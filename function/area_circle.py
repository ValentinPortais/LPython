from math import *
def areacircle(r):
    result = pi * r**2
    return result

Radius = int(input('Enter Radius'))
print('The area of the circle is ',areacircle(Radius))
