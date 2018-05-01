N = int(input('Enter your mark '))
grade = ['A','B','C','D','E']
if(N >= 80):
    res=grade[0]
elif(N < 80 and N >= 60):
    res=grade[1]
elif(N < 60 and N >= 50):
    res=grade[2]
elif(N < 50 and N >= 40):
    res=grade[3]
elif(N < 40 ):
    res=grade[4]
else:
    print("unknown mark")
    quit()
print('Your grade is',res)
