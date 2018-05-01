#This program count the number of char in a name
name = [ 'Jean-Michel' , 'Marc' , 'Vanessa' , 'Anne' , 'Maximilien ' , 'Alexandre-Benoît' , 'Louise' ]
i = 0
while i < len(name):
    charcount=len(name[i])
    print(name[i],' : ',charcount)
    i += 1

