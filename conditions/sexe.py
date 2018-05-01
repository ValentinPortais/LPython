name = input("What is your name ?")
sex = input("Are you a lady or a guy?(M/F)")
if(sex == 'M' or sex == 'm'):
    genre='sir'
elif(sex == 'F' or sex == 'f'):
    genre='lady'
else:
    print("Unknown sex , are you human ?")
    quit()

print("Hello",genre,name)
