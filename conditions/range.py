# Add numbers between 'a' and 'b' which are multiple of 3 and 5 

a,b = 0,32
i = a
z = 0
while i<b:
    #find number multiple of 3 and 5
    if not (i%3 | i%5):
        z = z + i
    else:
        print("ignoring",i)
    i = i + 1
print("Result is",z)

