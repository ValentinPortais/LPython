from drawing_triangle import *
up()
goto(-150, 50)
 
scolor,ssize,space = 'yellow', 30, 40
i = 0
while i < 9:
  down()
  stars5(scolor,ssize)
  up()
  forward(space)

  if(i<4):
   ssize+=10
   space+=10
  else:
   ssize-=10
   space-=10

  i+=1

a = input()	

