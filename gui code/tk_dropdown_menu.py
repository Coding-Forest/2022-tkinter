# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")

# Functions

def show():
    label = Label(root, text=clicked.get()).pack()

options = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# Drop down boxes
clicked = StringVar()
clicked.set(options[0])

dropdown = OptionMenu(root, clicked, *options)
dropdown.pack()

btn = Button(root, text='Show selection', command=show).pack()

root.mainloop()