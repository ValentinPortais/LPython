
def volbox(x1=10, x2=10, x3=10):
    "Calcul volume of a parallelepiped"
    result= x1 * ( x2 * x3)
    return result

x1 = float(input("Enter the first vector size"))
x2 = float(input("Enter the second vector size"))
#x3 = float(input("Enter the third vector size"))

print("Volume is : ",volbox(x1,x2))#,#x3))

