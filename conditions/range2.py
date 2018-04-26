# Add numbers between 'a' and 'b' which are multiple of 3 or 5 

a,b = 0,32
i = a
z = 0
while i<=b:
    #check if number is multiple of 3 or 5
    if not(i%3) or not(i%5):
        z = z + i
    else:
        print("ignoring",i)
    i = i + 1
print("Result is",z)

