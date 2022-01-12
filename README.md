# 2022 tkinter
 Python GUI learn forest

<br>


**root**

  - `root = Tk()`
    - `root.title("gui title")`
    - `root.geometry("width x height")`

<br>

**grid**

  - `entity.grid(row=int, column=int, columnspan=int, padx=int, pady=int)`

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

**Label**

  - `label = Label(image=img_object, bd=border_width, sticky=W+E, anchor=)`
    - `sticky=W+E`: stretches all the way across the window.
    - `anchor=DIRECTION`: anchor the entity. `E` for East, `W`, `S`, `N`.
    - `label.grid(row, column, columnspan)`
    - `label.grid_forget()`
    - `label.pack()`

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

**quit**

  - `b_quit = Button(root, text='message', command=root.quit)`

<br>

****

<br>

****

<br>