from tkinter import *
from tkinter.ttk import * 


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Record spending/earning", command=donothing)
filemenu.add_command(label="View Finances", command=donothing)
filemenu.add_command(label="Quit", command=quit)

filemenu.add_separator()


root.config(menu=menubar)
root.mainloop()