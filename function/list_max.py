def indexMax(vlist):
  "Find index of the higher element in the list"
  z=max(vlist)
  res=vlist.index(z)
  return res

serie=[5,8,2,1,9,3]
print(indexMax(serie))

