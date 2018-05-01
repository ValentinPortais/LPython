n = 0
lmark = []
while(n >= 0):
    n = int(input('Enter studen mark : '))
    if(n > 0):
      lmark.append(n)
    else:
        print('Finished')
nummark = len(lmark)
maxmark = max(lmark)
minmark = min(lmark)
average = sum(lmark) / nummark
print('Number of Mark : ',nummark,' Highest : ',maxmark,' Lowest : ',minmark,' Average : ',average) 
