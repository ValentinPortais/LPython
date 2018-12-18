#!/usr/bin/env python3

def rspace(ifile):
    """Return lines and replace whitespaces by *-*"""
    newline = ''
    for line in ifile:
        for i in line:
            if i == " ":
                newline+="*-*"
            else:
                newline+=i
    return newline


latfilename=input('Source file in latin')
utffilename=input('Destination file in UTF8')

latfile=open(latfilename,'r', encoding='Latin-1')
utfile=open(utffilename,'w', encoding='UTF8')

utfile.write(rspace(latfile.read()))

latfile.close()
utfile.close()
