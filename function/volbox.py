
def volbox(x1=-1, x2=-1, x3=-1):
    "Calcul volume of a box"
    if(x1 == -1):
      result= x1
    elif(x2 ==-1):
      result= x1**3
    elif(x3 ==-1):
      result= x1 * x1 * x2
    else:
      result= x1 *  x2 * x3
    return result

print(volbox())
print(volbox(5.2))
print(volbox(5.2, 3))
print(volbox(5.2, 3, 7.4))
