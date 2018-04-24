ch,mch = "kayak",""
l=len(ch)
i=l-1
#On part du dernier charactere jusqu au premier
while(i>=0):
    #On recupere charactere
    mch=mch+ch[i]
    i = i - 1

print(mch)
if mch==ch:
    print("C'est un palindrome")
