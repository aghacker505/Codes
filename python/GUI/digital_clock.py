# from ssl import SSLCertVerificationError
from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()
main.title('Digital Clock')


def time():
    tick = strftime('%H:%M:%S %p')
    lbl.config(text=tick)
    lbl.after(1000, time)


lbl = Label(main, font=('arial', 50, 'bold'),
            # height = 1920,
            # width = 15,
            background='white',
            foreground='black')


lbl.pack(anchor='center')
time()

mainloop()
