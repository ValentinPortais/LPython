i,j,b = 0,0,0
d='*'
mch=''
ch='charognard'
a=len(ch)
while(i<a):

  if i==a-1:
    mch = mch + ch[i] 
  else:
    mch = mch + ch[i] + d 

  i = i + 1
print(mch)


