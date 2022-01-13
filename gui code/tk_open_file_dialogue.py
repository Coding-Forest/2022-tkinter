# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

ROOT_PATH = ".\\GitHub\\2022-tkinter\\test_gallery2\\"

root = Tk()
root.title('File Open Dialogue')

def open_image():
    global selected_image
    root.filename = filedialog.askopenfilename(initialdir=ROOT_PATH,
                                               title='Select a file',
                                               filetypes=(('jpg', ".jpg"), ('jpeg', ".jpeg"), ('all files', '*.*'), ('png', ".png")))
    label = Label(root, text=root.filename).pack()

    selected_image = Image.open(root.filename)
    ssize = selected_image.size
    selected_image = selected_image.resize((int(ssize[0]*0.35), int(ssize[1]*0.35)))
    selected_image = ImageTk.PhotoImage(selected_image)

    image_label = Label(image=selected_image).pack()

button = Button(root, text='Open image', command=open_image).pack()

root.mainloop()