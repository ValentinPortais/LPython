#!/usr/bin/env python3

def compar(string1,string2):
    if string1 != string2:
        print("> ",string1)
        print("< ",string2)

f1=open('/home/valentin/LPython/File/file1','r')
f2=open('/home/valentin/LPython/File/file2','r')
txt1=f1.readlines()
txt2=f2.readlines()

for i in range(min(len(txt1),len(txt2))):
        compar(txt1[i],txt2[i])
