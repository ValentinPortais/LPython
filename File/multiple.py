#!/usr/bin/env python3

#function to multiple
def multiple(file,rmin,rmax,nb):

    for i in range(rmin,rmax):
        for j in range(1,nb):
            z = i * j
            file.write(str(z)+"\n")
        file.write("--------\n")

filename = "tables"
fic = open(filename,'w')
multiple(fic,2,31,21)
fic.close()
