from cgitb import text
from tkinter import *

root = Tk()
c = Canvas(root, 
bg='black',
height =1080,
width = 1920,
cursor = 'pencil')

#creating a line in the canvas
id = c.create_line(100,100,100,300,250,300, width = 4, fill="white")

#creating a oval shape in the canvas
id = c.create_oval(100,100,400,300, 
width=5, 
fill="black", 
outline="red", 
activefill="green")

#creating a polygon in the canvas
id = c.create_polygon(500, 500, 100, 510, 100, 200,
width = 4,
fill = "lightblue",
outline= "white",
smooth=1,
activefill="lightblue")

#creating some text in the canvas
fnt = ('Courier', 50, 'bold italic underline')
id = c.create_text(1000,500,
text = "Learning python",
font = 'fnt',
fill = "yellow",
activefill="lightblue")
c.pack()
root.mainloop()