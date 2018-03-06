#!/usr/bin/python
#Conversion des secondes en minutes , jours , mois , années

y,m,d,M,S = 0,0,0,0,31536000 

M = S // 60
if ( M % (60*24) == 0):
  d = M // ( 60 * 24)
#  if ( d % 30 == 0):
  m = d // 30
  y = m // 12

print (S,"secondes c'est ...")
print ("année:",y,"mois:",m,"jours:",d,"minutes:",M)
