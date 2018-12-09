#!/usr/bin/env python3

def findlong(filename):
    fic = open(filename, 'r')
    l = fic.readlines()
    maxcount = ""
    for i in range(len(l)):
        if len(l[i]) >= len(maxcount):
            maxcount = l[i]
    return maxcount

file_i = input("Enter a file to analyze : ")
print(findlong(file_i))
