name ,  lshort, llong= ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'],[],[]

i=0
while(i< len(name)):
    if(len(name[i]) < 6):
        lshort.append(name[i])
    else:
        llong.append(name[i])
    i = i + 1
print("short list:",lshort)
print("long list:",llong)
print(type(llong))
