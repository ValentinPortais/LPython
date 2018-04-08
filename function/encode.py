#Script to insert a value in a list
value,l=0,[]
while(value != ""):
    value=input("Please enter a number : ")
    if(value !=""):
        value=int(value)
        l.append(value)
print(l)
