# 2022 tkinter
 Python GUI learn forest

<br>


**root**

  - `root = Tk()`
    - `root.title("gui title")`
    - `root.geometry("width x height")`


<br>

**Frame**

  - `frame = LabelFrame(root, text="message", padx=x, pady=y)`
  - `frame.pack(padx=x, pady=y)`: the paddings in `pack` serves as margin. 

<br>

**grid**

  - `entity.grid(row=int, column=int, columnspan=int, padx=int, pady=int)`

<br>

**Image components**

  **Icon**
    - `icon = PhotoImage(file='path')`
    - `root.iconphoto(False, icon)`

  **image**
    - `img_path = 'path'`
    - `img = ImageTk.PhotoImage(Image.open(img_path))`
    - `label = Label(image=img)`

<br>

**Input field**

  - `entry = Entry(root, width=w, fg=fg, bg=bg, borderwidth=bw)`
    - `entry.get()`: take user input.
    - `entry.insert(index: int|str, str)`: input placeholder
    - `entry.delete(0, 'end')` 
    - `entry.pack()`
    

<br>

**Button**

  - `button = Button(root, text="message", command=function, state=DISABLED, padx=x, pady=y, fg='foregound_colour', bg='background_colour', relief=SUNKEN)`
    - `command = function`: without paranthesis for parameterless function 
    - `command = lambda: function(param)`
    - `bd = border_width`
    - `relief = SUNKEN`
    - `button.grid(row, column, columnspan)`
    - `button.bind('Key', function)`
    - `button.pack()`

<br>

**Radiobutton**

  - `Radiobutton(root, text=text, variable=v, value=v).pack(anchor=W)`
  - `var = StringVar()`
  - `var = IntVar()`
    - `var.set()`
    - `var.get()`

<br>

**Checkbutton**

  - `c = Checkbutton(root, text="Supersize order", variable=var, onvalue="Supersize", offvalue="Regular")`
    - `c(onvalue="")`
    - `c(offvalue="")`
    - `var = StringVar()`
    - `c.deselect()`

<br>

**Dropdown menu**

  - `dropdown = OptionMenu(root, StringVar(), *options_list)`

<br>

**Label**

  - `label = Label(image=img_object, bd=border_width, sticky=W+E, anchor=)`
    - `sticky=W+E`: stretches all the way across the window.
    - `anchor=DIRECTION`: anchor the entity. `E` for East, `W` for West.
    - `label.grid(row, column, columnspan)`
    - `label.grid_forget()`
    - `label.pack()`

<br>

**Pop-up**

  - `from tkinter import messagebox`
  - `messagebox`
    - `.showinfo`
    - `.showarning`
    - `.showerror`
    - `.askquestion`
    - `.askokcancel`
    - `.askyesno`

<br>

**Open file dialogue**

  - `root.filename = filedialog.askopenfilename()`
    - `initialdir=ROOT_PATH,`
    - `title='Select a file'`,
    - `filetypes=(('jpg', ".jpg"), ('jpeg', ".jpeg"), ('all files', '*.*'), ('png', ".png")))`

<br>

**Database**

  - `import sqlite3`

<br>

**New window**

  - `top = Toplevel()`

<br>

**quit**

  - `b_quit = Button(root, text='message', command=root.quit)`
  - `conn = sqlite3.connect('address_book.db')`
  - `cursor = conn.cursor()`
  - `conn.commit()`
  - `conn.close()`


<br>

****

  - ``

<br>


****

  - ``

<br>



### References
 
  - Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
  - freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA
