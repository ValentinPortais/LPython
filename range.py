a,b = 0,32
i = a
z = 0
while i<b:
  #add number if it is a multiple of 3 or 5
  if not (i%3 | i%5):
    z = z + i
  #add number if multiple of 3
  elif not (i%3):
    z = z + i
  elif not (i%5):
    z = z + i
  i = i + 1
print("Result is",z)

