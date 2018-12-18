#!/usr/bin/env python3
# -*- coding: Utf8 -*-

#Loop over ASCII table number, starting at 32, ending at 128
for i in range(32,128):
    #Print ASCII number and corresponded character
    print(i,' : ',chr(i))

#Loop over accent character table
for j in range(128,256):
    print(j,' : ',chr(j))
