# Based on the beautiful tutorial by John from Codemy.com (https://www.youtube.com/c/Codemycom)
# freeCodeCamp.org (2019) Tkinter Course - Create Graphic User Interfaces in Python Tutorial https://www.youtube.com/watch?v=YXPyB4XeYLA

from tkinter import *
from PIL import ImageTk, Image
import sqlite3

geometry = "400x600"

root = Tk()
root.geometry(geometry)

# Database

# Create a database or connect to one
conn = sqlite3.connect('address_book.db')

# Cursor instance
cursor = conn.cursor()

'''
# Create table
cursor.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
)""")
'''

database = 'address_book.db'

# Record submit function
def submit():
    #  Create a database or connect to one
    conn = sqlite3.connect(database)
    # Create a cursor
    c = conn.cursor()

    # Inser into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


def edit():
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
    record_num = int(edit_box.get())

    if (record_num > len(records)):
        print("Record number doesn't exist.")
        print(len(records))

    edit_window = Tk()
    edit_window.geometry(geometry)
    edit_window.title('Update a record')

    # Create global variables for text boxes
    global f_name_edit_window
    global l_name_edit_window
    global address_edit_window
    global city_edit_window
    global state_edit_window
    global zipcode_edit_window

    # Entry box
    f_name_edit_window = Entry(edit_window, width=30)
    f_name_edit_window.grid(row=0, column=1, padx=20)
    l_name_edit_window = Entry(edit_window, width=30)
    l_name_edit_window.grid(row=1, column=1)
    address_edit_window = Entry(edit_window, width=30)
    address_edit_window.grid(row=2, column=1)
    city_edit_window = Entry(edit_window, width=30)
    city_edit_window.grid(row=3, column=1)
    state_edit_window = Entry(edit_window, width=30)
    state_edit_window.grid(row=4, column=1)
    zipcode_edit_window = Entry(edit_window, width=30)
    zipcode_edit_window.grid(row=5, column=1)

    # Label
    f_name_edit_label = Label(edit_window, text="First name")
    f_name_edit_label.grid(row=0, column=0, ipadx=10)
    l_name_edit_label = Label(edit_window, text="Last name")
    l_name_edit_label.grid(row=1, column=0)
    address_edit_label = Label(edit_window, text="Address")
    address_edit_label.grid(row=2, column=0)
    city_edit_label = Label(edit_window, text="City")
    city_edit_label.grid(row=3, column=0)
    state_edit_label = Label(edit_window, text="State")
    state_edit_label.grid(row=4, column=0)
    zipcode_edit_label = Label(edit_window, text="Zipcode")
    zipcode_edit_label.grid(row=5, column=0)

    for record in records:
        f_name_edit_window.insert(0, record[0])
        l_name_edit_window.insert(0, record[1])
        address_edit_window.insert(0, record[2])
        city_edit_window.insert(0, record[3])
        state_edit_window.insert(0, record[4])
        zipcode_edit_window.insert(0, record[5])

    # Button
    save_btn = Button(editor, text="Edit record")
    save_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

def query():
    #  Create a database or connect to one
    conn = sqlite3.connect(database)
    # Create a cursor
    c = conn.cursor()

    # record_id = delete_box.get()

    # Query the database
    c.execute(f"SELECT * FROM addresses")

    records = c.fetchall()
    for record in records:
        f_name_edit_window.insert(0, "placeholder")
        l_name_edit_window.insert(0, record[1])
        address_edit_window.insert(0, record[2])
        city_edit_window.insert(0, record[3])
        state_edit_window.insert(0, record[4])
        zipcode_edit_window.insert(0, record[5])

    # Loop through results
    print_records = ''
    for record in records:
        print_records += f"{record[6]} {record[0]} {record[1]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=13, columnspan=2)

    # Commit changes
    conn.commit()

    # Close connection
    conn.close()





def update():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
            first_name = :first,
            last_name = :last,
            address = :address,
            city = :city,
            [state = :state,
            zipcode = :zipcode              
              WHERE iod = :oid""", {
        'first': f_name_edit_window.get(),
        'last': l_name_edit_window.get(),
        'address': address_edit_window.get(),
        'city': city_edit_window.get(),
        'state': state_edit_window.get(),
        'zipcode': zipcode_edit_window.get(),

        'oid': record_id
    })


def delete():
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute(f"DELETE FROM addresses WHERE oid={delete_box.get()};")

    conn.commit()
    conn.close()


# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)


# Create Text box labels
f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Record ID to delete")
delete_box_label.grid(row=9, column=0)

# Create submit buttons
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=5, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=20, ipadx=127)

# Create a delete button
delete_btn = Button(root, text="Delete record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

edit_label = Label(root, text="Record ID to edit")
edit_label.grid(row=11, column=0)
edit_box = Entry(root, width=30)
edit_box.grid(row=11, column=1)

# Create an edit button
edit_btn = Button(root, text="Edit record", command=edit)
edit_btn.grid(row=12, column=0, columnspan=2, padx=10, pady=10, ipadx=127)


# Commit Changes
conn.commit()

# Close connection
conn.close()

root.mainloop()