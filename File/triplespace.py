#!/usr/bin/env python3

def triples(l):
    m = ""
    for i in range(len(l)):
        if l[i] == " ":
            #Insert 3 spaces
            m+=" "*3
        else:
            m+=l[i]
    return m

namefile = input("Enter a filename : ")
ifile = open(namefile,'r+')
lines = ifile.readlines()
for n in range(len(lines)):
    lines[n]= triples(lines[n])
#Go to Begin of file
ifile.seek(0)
ifile.writelines(lines)
ifile.close()
