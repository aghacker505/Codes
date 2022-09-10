from tkinter import *
from tkinter import font

#creating root window
root = Tk()

#get all support font families

font_lst = list(font.families())

print(font_lst)