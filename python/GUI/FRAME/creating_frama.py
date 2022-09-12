'''
creating an empty frame window
'''
from tkinter import *

#creating root window
root = Tk()

#give title to the root window
root.title("AG window")

#creating frame as a child to root window
f = Frame(root, height = 1080, width = 1920, bg = "black", cursor = "cross")

#attach frame to the root
f.pack()

root.mainloop()