from tkinter import *
import tkinter

windows = tkinter.Tk()

L1 = Label(windows, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(windows, bd =5)
E1.pack(side = RIGHT)

w = tkinter.Button(windows, text = "Button")
w.grid( side = BOTTOM)
# w.grid()

# # w1.grid()
# # w1.pack()
# w.pack()
windows.mainloop()