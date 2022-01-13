# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA


from tkinter import *
from PIL import ImageTk, Image

root = Tk()

logo_path = "logo_path"
logo_tk = PhotoImage(file=logo_path)

root.title("Frame")
root.iconphoto(False, logo_tk)

frame = LabelFrame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Don't click this.")
b2 = Button(frame, text=".. or this!")

b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()