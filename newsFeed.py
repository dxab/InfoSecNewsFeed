#!/usr/bin/python3

###lines defining tkinter are prewritten 

import tkinter as tk
import krebscraper

root = tk.Tk()
deli = 100           # milliseconds of delay per character
svar = tk.StringVar()
labl = tk.Label(root, textvariable=svar, height=10 )
def shif():
    shif.msg = shif.msg[1:] + shif.msg[0]
    svar.set(shif.msg)
    root.after(deli, shif)
    root.title("InfoSec News")
#must create a list so that your inputFile can be fed to it
krebscraper.main()
x = []
inputFile = open("newskreb.txt", 'r')
for text in inputFile:
	x.append(text)
inputFile.close()
#####################
shif.msg = x[0]
shif()
labl.pack()
root.mainloop()