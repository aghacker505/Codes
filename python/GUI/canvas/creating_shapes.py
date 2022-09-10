from tkinter import *

root = Tk()

c = Canvas(root, bg = "black", height = 1080, width =1920, cursor = 'pencil')
'''
fill = color filled inside shape
outline = color of the line
activefill = color when courser bring on it
smooth = values maybe 1 or 0, If 0, a polygon with sharp edges and 1 polygon with smooth edges
'''

id = c.create_oval(1000, 700, 400, 100, width =5, fill="olive", outline="green", activefill="red")
# id = c.create_line(coordinates, width =4, fill="white")

c.pack()
root.mainloop()