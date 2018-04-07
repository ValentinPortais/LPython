#This scripts print the day and the day number

#List containing the names of the day of the week
jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a,b = 0,0
#Print day of the month until 25
while a<25:
    #Increment day
    a = a +1
    #Find the corresponding day name
    b = a % 7
    #Print the day number and the name of the day
    print (a,jour[b])

