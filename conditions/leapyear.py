# Enter a year and detect if its a leapyear

a=int(input("Enter a year\n"))

if not(a%4):
  if (a%100) or not(a%400):
      print(a,"is a leapyear!")
