def changeChar(string,ch1,ch2,begin=0,end=-1):
  if(end ==-1):
    end=len(string)
  i,newstring=0,""
  while(i<len(string)):
    if(string[i]==ch1 and i>=begin and i<=end ):
      newstring = newstring+ ch2
    else:
      newstring = newstring + string[i]
    i+=1
  return newstring 
phrase = 'Python is really magic'
print(changeChar(phrase,' ', '*'))
print(changeChar(phrase,' ', '*', 8, 12))
print(changeChar(phrase,' ', '*',12))
print(changeChar(phrase,' ', '*',end=12))

