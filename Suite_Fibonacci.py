#!/usr/bin/python

a,b,c = 1,1,1

while (c < 24):
    print(b, end=" ")
    a,b,c = b , a+b , c+1
