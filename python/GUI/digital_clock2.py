from tkinter import *
import time

root = Tk()
root.title("DIGITAL CLOCK")
root.geometry("1920x1080")
root.config(bg = "black")

def digiclock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
 
    if int(h) >= 12 and int(h) < 24 and int(m) >= 0:
        meridian.config(text = "PM")
    else:
        meridian.config(text = "AM")
    if int(h) > 12:
        h = str((int(h) - 12))
    elif int(h) == 0:
        h=str(12)

    hour.config(text = h)
    minute.config(text = m)
    second.config(text = s)
    hour.after(200, digiclock)

hour = Label(root, text = "12", font = ("radioland", 100, "bold"), bg = "black", fg = "#39ff14")
hour.place(x = 520, y = 300, width = 200, height = 150)

colon = Label(root, text = ":", font = ("radioland", 80, "bold"), bg = "black", fg = "#39ff14")
colon.place(x = 730, y = 340, width = 50, height = 70)

minute = Label(root, text = "12", font = ("radioland", 100, "bold"), bg = "black", fg = "#39ff14")
minute.place(x = 780, y = 300, width = 200, height = 150)

second = Label(root, text = "12", font = ("radioland", 20, "bold"), bg = "black", fg = "#39ff14")
second.place(x = 943, y = 260, width = 50, height = 50)

meridian = Label(root, text = "PM", font = ("radioland", 20, "bold"), bg = "black", fg = "#39ff14")
meridian.place(x = 967, y = 410, width = 60, height = 30)


digiclock()
root.mainloop()