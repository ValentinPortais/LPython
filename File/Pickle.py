#!/usr/bin/env python3

import pickle

a,b,c = 1,2,3

#Open file pdata in writable binary mode
file = open('pdata','wb')

#Store a value to file
pickle.dump(a,file)
#Store b value to file
pickle.dump(b,file)
#Close file 
file.close()

#Open file pdata in readable binary mode
file = open('pdata','rb')

#Read pickle object representation from file and return original object
a = pickle.load(file)
b = pickle.load(file)

print("a = " ,a,"type :",type(a))
print("b = " ,b,"type :",type(b))

#Close file
file.close()
