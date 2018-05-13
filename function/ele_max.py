def eleMax(vlist,begin=0,end=-1):
  "Return maximum number in a given list"
  i,z=0,0
  if (end==-1):
    end=len(vlist)
  while(i<len(vlist)):
    if(i>=begin and i<=end and z<vlist[i]):
      z=vlist[i]
    i+=1
  return z

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie))
print(eleMax(serie, 2, 5))
print(eleMax(serie, 2))
print(eleMax(serie, end =3, begin =1))



