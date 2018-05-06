from drawing_square import *
from drawing_triangle import *
up()
goto(-150, 50)
 

csize,tsize,ccolor,tcolor,space = 10,10,'red','blue',20
i = 0
while i < 10:
  down()
  carre(csize,ccolor,0)
  up()
  forward(space)
  down()
  triangle(tsize,tcolor,0)
  up()
  forward(space)
  i+=1
  space=space+10
  csize+=10
  tsize+=10

a = input()	

