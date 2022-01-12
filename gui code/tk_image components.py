# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("500x600")
root.title('Image components')

icon = PhotoImage(file="path")
root.iconphoto(False, icon)

img_path = "path"
img = ImageTk.PhotoImage(Image.open(img_path))
label = Label(image=img)
label.pack()

b_quit = Button(root, text='Quit', command=root.quit)
b_quit.pack()

root.mainloop()