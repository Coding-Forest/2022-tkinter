from tkinter import *
from PIL import ImageTk, Image

root = Tk()

logo_path = "./tkinter.png"
logo_tk = PhotoImage(file=logo_path)

root.title("Frame")
root.iconphoto(False, logo_tk)

root.mainloop()