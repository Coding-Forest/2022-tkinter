# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.geometry("300x300")
root.title('Slider')

vertical = Scale(root, from_=0, to=300)
vertical.pack()

def slide():
    slide_label = Label(root, text=horizontal.get()).pack()
    root.geometry(f"{horizontal.get()}x{vertical.get()}")


horizontal = Scale(root, from_=0, to=300, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()


button = Button(root, text='Click', command=slide).pack()
close_button = Button(root, text="Close", command=root.destroy).pack()

root.mainloop()