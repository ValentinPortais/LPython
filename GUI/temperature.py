#!/usr/bin/env python3
import tkinter as tk

def conv_far(event):

  "Convert temperature to degrees Fahrenheit"
  fvalue = int(eval(entr1.get()) * 1.80 + 32)
  #Clear entry and insert converted result
  entr2.delete(0, tk.END)
  entr2.insert(0, fvalue)

def conv_cel(event):
  "Convert temperature to degrees Celsius"
  cvalue = int((eval(entr2.get()) - 32) // 1.80)
  #Clear entry and insert converted result
  entr1.delete(0, tk.END)
  entr1.insert(0, cvalue)


fen1 = tk.Tk()
fen1.title("Temperature")

#Interface definition
tk.Label(fen1, text= 'Celsius').grid(sticky=tk.E)
tk.Label(fen1, text= 'Farentheit').grid(sticky=tk.E)
entr1 = tk.Entry(fen1)
entr2 = tk.Entry(fen1)
entr1.grid(row=0, column=1)
entr2.grid(row=1, column=1)
#Link Return to the convert function
entr1.bind("<Return>", conv_far)
entr2.bind("<Return>", conv_cel)

#Start Event receiver
fen1.mainloop()
