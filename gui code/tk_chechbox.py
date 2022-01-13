# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

def show_selection():
    label = Label(root, text=var.get()).pack()

#var = IntVar()
var = StringVar()
c = Checkbutton(root, text="Check if you want it super size", variable=var, onvalue="Supersize", offvalue="Regular")
c.deselect()
c.pack()

button = Button(root, text="show selection", command=show_selection).pack()

root.mainloop()