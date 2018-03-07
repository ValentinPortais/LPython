#!/usr/bin/python
i,j=0,0
#How many stars do you wanna count ?
while(i<20):
  #Ok let's start printing these stars
  while(j<=i): 
    print("*",end="")
    j=j+1  
  print(" ") #Carriadge return 
  j=0  #Reset start print counter
  i=i+1
