num,even,odd = [32, 5, 12, 8, 3, 75, 2, 15] , [], []
i = 0

while(i < len(num)):
    if(num[i]%2 == 0):
        even.append(num[i])
    else:
        odd.append(num[i])
    i = i + 1
print("Even numbers:",even)
print("Odd numbers:",odd)

