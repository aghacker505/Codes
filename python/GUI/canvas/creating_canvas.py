from tkinter import *

root = Tk()

c = Canvas(root, bg = "black", height = 500, width =600, cursor = 'pencil')

id = c.create_line(50, 50, 200, 50, 200, 150, width =4, fill="white")
# id = c.create_line(coordinates, width =4, fill="white")

c.pack()
root.mainloop()