#Find the highest number in the a list
num = [32, 5, 12, 8, 3, 75, 2, 15]
i,a = 0,0
#Iterate on each number of the list
while(i < len(num)):
    #Compare the previous value of a and the current number
    if( a < num[i]):
        a = num[i]
    i = i + 1
print(a)
