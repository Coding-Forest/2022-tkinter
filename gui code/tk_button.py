# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
import random

# tkinter is a 2-step process.
# First create,
# then put it on the screen.

# Everything in tkinter is a widget.

root = Tk()

e = Entry(root, width=50, fg="#ffffff", bg="green", borderwidth=5)
e.pack()

def display_message_onClick():

    hello = ['안녕하세요', '안녕', 'Hello', 'Good morning', 'Good afternoon',  'Good evening', 'Hallo', 'Guten Morgen', 'Guten Tag', 'Guten Abend']
    text = e.get()
    i = random.randint(0, len(hello)-1)
    label = Label(root, text=f"{hello[i]}, {text}")
    label.pack()


button = Button(root, text='Click here.', padx=20, pady=2, command=display_message_onClick, fg='#ffffff', bg='#000000')
button.pack()


root.mainloop()