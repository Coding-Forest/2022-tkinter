# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA



# features
# 1. Takes in two variables and performs four arithmetic operations on them.


from tkinter import *


root = Tk()
root.geometry("400x300")
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Functional operations
def click(number):
    current = e.get()
    e.delete(0, 'end')
    e.insert('end', str(current) + str(number))

def clear():
    e.get()
    e.delete(0, 'end')


# Math operations
def add():
    num1 = e.get()
    global gnum1
    global current_operator
    current_operator = "adder"
    gnum1 = int(num1)

    e.delete(0, END)


def subtract():
    num1 = e.get()
    global gnum1
    global current_operator
    current_operator = "subtractor"
    gnum1 = int(num1)

    e.delete(0, END)


def multiply():
    num1 = e.get()
    global gnum1
    global current_operator
    current_operator = "multiplier"
    gnum1 = int(num1)

    e.delete(0, END)


def divide():
    num1 = e.get()
    global gnum1
    global current_operator
    current_operator = "divider"
    gnum1 = int(num1)

    e.delete(0, END)


def equal():
    num2 = e.get()
    global gnum2
    gnum2 = int(num2)

    operation = {'adder': gnum1 + gnum2,
                 'subtractor': gnum1 - gnum2,
                 'multiplier': gnum1 * gnum2,
                 'divider': gnum1 / gnum2}

    e.delete(0, END)
    e.insert(0, operation[current_operator])

# Define buttons
num_padx = 30
num_pady = 10

b1 = Button(root, text="1", padx=num_padx, pady=num_pady, command=lambda: click(1))
b2 = Button(root, text="2", padx=num_padx, pady=num_pady, command=lambda: click(2))
b3 = Button(root, text="3", padx=num_padx, pady=num_pady, command=lambda: click(3))
b4 = Button(root, text="4", padx=num_padx, pady=num_pady, command=lambda: click(4))
b5 = Button(root, text="5", padx=num_padx, pady=num_pady, command=lambda: click(5))
b6 = Button(root, text="6", padx=num_padx, pady=num_pady, command=lambda: click(6))
b7 = Button(root, text="7", padx=num_padx, pady=num_pady, command=lambda: click(7))
b8 = Button(root, text="8", padx=num_padx, pady=num_pady, command=lambda: click(8))
b9 = Button(root, text="9", padx=num_padx, pady=num_pady, command=lambda: click(9))
b0 = Button(root, text="0", padx=num_padx, pady=num_pady, command=lambda: click(0))

# Operators
b_add = Button(root, text="+", padx=num_padx, pady=num_pady, command=add)
b_subtract = Button(root, text="-", padx=num_padx, pady=num_pady, command=subtract)
b_multiply = Button(root, text="×", padx=num_padx, pady=num_pady, command=multiply)
b_divide = Button(root, text="÷", padx=num_padx, pady=num_pady, command=divide)

b_fpoint = Button(root, text=".", padx=num_padx, pady=num_pady, command=lambda: click("."))
b_fraction = Button(root, text="1/x", padx=num_padx, pady=num_pady, command=lambda: click("/"))
b_squared = Button(root, text="x²", padx=num_padx, pady=num_pady, command=lambda: square)
b_sqrt = Button(root, text="2√x", padx=num_padx, pady=num_pady, command=lambda: sqrt)

b_equal = Button(root, text="=", padx=num_padx, pady=num_pady, command=equal)
b_clear = Button(root, text="C", padx=num_padx, pady=num_pady, command=clear)

#  Put the buttons on the screen
r1 = 1
b_fraction.grid(row=r1, column=0)
b_squared.grid(row=r1, column=1)
b_sqrt.grid(row=r1, column=2)
b_divide.grid(row=r1, column=3)

r2 = 2
b7.grid(row=r2, column=0)
b8.grid(row=r2, column=1)
b9.grid(row=r2, column=2)
b_multiply.grid(row=r2, column=3)

r3 = 3
b4.grid(row=r3, column=0)
b5.grid(row=r3, column=1)
b6.grid(row=r3, column=2)
b_subtract.grid(row=r3, column=3)

r4 = 4
b1.grid(row=r4, column=0)
b2.grid(row=r4, column=1)
b3.grid(row=r4, column=2)
b_add.grid(row=r4, column=3)

r5 = 5
b_clear.grid(row=r5, column=0)
b0.grid(row=r5, column=1)
b_fpoint.grid(row=r5, column=2)
b_equal.grid(row=r5, column=3)


# button = Button(root, text='Enter your stock quote', command=click)
# button.pack()

root.mainloop()