a,b = 0,32
i = a
z = 0
while i<b:
    #add number only if it is a multiple of 3 or 5
    if not (i%3 | i%5):
        z = z + i
    else:
        print("ignoring",i)
    i = i + 1
print("Result is",z)

