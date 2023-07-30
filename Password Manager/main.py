from tkinter import *
from tkinter import messagebox
import csv
import pyperclip
from password_generator import generate_password


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def new_random_password():
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())
    pyperclip.copy(password_entry.get())
    print(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    list = [website_entry.get(), username_entry.get(), password_entry.get()]
    # check for empty fields
    for i in list:
        if i == "":
            print("Fill all fields")
            messagebox.showwarning(
                title="Retry", message="Fill all the fields")
            return
    is_ok = messagebox.askokcancel(
        title="New password", message=f"Entered data: \nWebsite: {list[0]} \nUsername/Email: {list[1]} \nPassword: {list[2]} \nDo you wnat to proceed?")

    if is_ok:
        with open(r"Tkinter\Password Manager\db.csv", "a", newline='') as db:
            # write on csv database
            writer = csv.writer(db, delimiter=",")
            writer.writerow(list)
            messagebox.showinfo(
                title="Success", message="Password successfully added")
            db.close()
            clear()


def clear():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")

window.config(padx=50, pady=50)

# canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file=r"Tkinter\Password Manager\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:")
website.grid(column=0, row=1)

username = Label(text="Username/Email:")
username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# entries
website_entry = Entry(width=53)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry(width=53)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3, sticky=EW)

# buttons
generate_password_btn = Button(
    text="Generate Password", command=new_random_password)
generate_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=45, command=save)
add_btn.grid(column=1, row=4, columnspan=2)


window.mainloop()
