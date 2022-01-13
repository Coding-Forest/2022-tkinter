# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

import os
from tkinter import *
from PIL import ImageTk, Image

os.chdir("PATH")
logo_path = ".\\images\\tkinter.png"

root = Tk()
root.geometry("300x300")
logo = PhotoImage(file=logo_path)
root.iconphoto(False, logo)

def open():
    global img

    popup = Toplevel()
    popup.title('second window')
    logo_top = PhotoImage(file=logo_path)
    popup.iconphoto(False, logo_top)

    img = Image.open('.\\images\\aws clf-c01.png')
    img = img.resize((int(img.size[0] * 0.35), int(img.size[1] * 0.35)))
    img = ImageTk.PhotoImage(img)
    Label(popup, text="I got this!", image=img).pack()
    Label(popup, text='I earned this!').pack()
    
    btn_close = Button(popup, text='close', command=popup.destroy).pack()

btn = Button(root, text='Check my credential.', command=open).pack()

root.mainloop()