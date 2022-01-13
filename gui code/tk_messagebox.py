# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

import os
from tkinter import *
from tkinter import messagebox

os.chdir("PATH")

root = Tk()

# logo
logo_path = ".\\images\\tkinter.png"
logo = PhotoImage(file=logo_path)
root.iconphoto(False, logo)


# showinfo, showarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showerror("this is a popup!", "hello world")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="You clicked yes").pack()
    # else:
    #     Label(root, text="You clicked NO").pack()


Button(root, text='Popup', command=popup).pack()


root.mainloop()

