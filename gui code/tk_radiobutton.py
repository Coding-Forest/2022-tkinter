# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

logo_path = "./tkinter.png"

from tkinter import *

root = Tk()
root.geometry("300x150")
root.title("RadioButton")
icon = PhotoImage(file=logo_path)
root.iconphoto(False, icon)

r = IntVar()
r.set("2")

MENU = [
    ("Margherita", "Margherita"),
    ("Prosciutto", "Prosciutto"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("")


for text, choice in MENU:
    Radiobutton(root, text=text, variable=pizza, value=choice).pack(anchor=W)


def clicked(value):
    label = Label(root, text=value)
    label.pack()     #grid(row=2, column=0)

#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda :clicked(r.get())).grid(row=0, column=0)
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda :clicked(r.get())).grid(row=1, column=0)

label = Label(root, text=pizza.get())
label.pack()    #grid(row=2, column=0)

button = Button(root, text='Click here', command=lambda : clicked(pizza.get()))
button.pack()   #grid(row=4, column=0)

root.mainloop()