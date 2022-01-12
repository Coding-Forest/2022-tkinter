# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA


# Features
# 1. Adjust the image size automatically so the app window's height doesn't change.
# (regular height maintains the navigation buttons on the same vertical location.)
# 2. There is a bug with the img_num, which affects both 1) the navigation and 2) the status bar update.
#    On launch, the first click doesn't increment the img_num so have to click it twice. 
#    This happens with the back button at the last image. 


from tkinter import *
from PIL import ImageTk, Image


root = Tk()
gw, gh = 750, 500
root.geometry(f"{gw+100}x{gh+100}")
root.title('Gallery App')


# Image handling functions

def scale_image(img):
    width, height = img.size[0], img.size[1]
    scaler = gh / height
    scaled_img = img.resize((int(width * scaler), gh))
    return scaled_img


# Images
pimg1 = Image.open("./test_image 1.png")
pimg1 = scale_image(pimg1)

pimg2 = Image.open("./test_image 2.png")
pimg2 = scale_image(pimg2)

pimg3 = Image.open("./test_image 3.png")
pimg3 = scale_image(pimg3)

pimg4 = Image.open("./test_image 4.png")
pimg4 = scale_image(pimg4)

pimg5 = Image.open("./test_image 5.png")
pimg5 = scale_image(pimg5)

pimg6 = Image.open("./test_image 6.png")
pimg6 = scale_image(pimg6)

pimg7 = Image.open("./test_image 7.png")
pimg7 = scale_image(pimg7)


img1 = ImageTk.PhotoImage(pimg1)
img2 = ImageTk.PhotoImage(pimg2)
img3 = ImageTk.PhotoImage(pimg3)
img4 = ImageTk.PhotoImage(pimg4)
img5 = ImageTk.PhotoImage(pimg5)
img6 = ImageTk.PhotoImage(pimg6)
img7 = ImageTk.PhotoImage(pimg7)

img_list = [img1, img2, img3, img4, img5, img6, img7]


label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)


# Status
status = Label(root, text=f"Image 1 of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)


# Labels
label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)


# Button navigation functions

def forward(img_num):
    global label
    global b_next
    global b_prev

    label.grid_forget()
    # define the image all over again.
    label = Label(image=img_list[img_num])
    b_next = Button(root, text=">>", command=lambda: forward(img_num+1))
    b_prev = Button(root, text="<<", command=lambda: backward(img_num-1))

    if img_num == len(img_list) - 1:
        b_next = Button(root, text=">>", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    b_prev.grid(row=1, column=0)
    b_next.grid(row=1, column=2)

    # Update status bar
    status = Label(root, text=f"Image {img_num} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def backward(img_num):
    global label
    global b_next
    global b_prev

    label.grid_forget()
    # define the image all over again.
    label = Label(image=img_list[img_num])
    b_next = Button(root, text=">>", command=lambda: forward(img_num+1))
    b_prev = Button(root, text="<<", command=lambda: backward(img_num-1))

    if img_num == 0:
        b_prev = Button(root, text="<<" ,state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    b_prev.grid(row=1, column=0)
    b_next.grid(row=1, column=2)

    # Update status bar
    status = Label(root, text=f"Image {img_num+1} of {len(img_list)}", bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


# Button
b_prev = Button(root, text="<<", command=lambda: backward(0))
b_next = Button(root, text=">>", command=lambda: forward(2))
b_quit = Button(root, text="Quit", command=root.quit)

b_prev.grid(row=1, column=0)
b_quit.grid(row=1, column=1)
b_next.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()