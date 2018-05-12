def inverse(ch):
  "Invert a string characters"
  i,res=len(ch)-1,""

  while i>=0:
      res+=ch[i]
      i-=1
  return res

a=input()
print(inverse(a))
