#/usr/bin/env python3

def readfile(filename):
    rfile = open(filename,'r')
    print(rfile.read())
    rfile.close()

def writefile(filename):
    i = None
    wfile = open(filename,'w')
    while True:
      i = input()
      if i == "":
          break
      else:
          wfile.write(i+"\n")
    wfile.close()

file = input('Enter filename : ')
action = input ('Choose action [Read/Write] : ')

if action in ('R','r','Read'):
    readfile(file)
elif action in ('W','w','Write'):
    writefile(file)
else:
    raise ValueError("Input Error")
