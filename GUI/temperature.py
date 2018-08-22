#!/usr/bin/env python3
import tkinter as tk


fen1 = tk.Tk()
fen1.title("Temperature")

tk.Label(fen1, text= 'Celsius').pack()
tk.Label(fen1, text= 'Farentheit').pack()
Entry(fen1)

#Start Event receiver
fen1.mainloop()
