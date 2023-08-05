from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from password_generator import generate_password

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def new_random_password():
    password_entry.delete(0, END)
    password_entry.insert(0, generate_password())
    pyperclip.copy(password_entry.get())
    print(password_entry.get())

# ---------------------------- SAVE, DELETE, UPDATE PASSWORD ------------------------------- #

def save():
    # collect data in JSON format
    list = [website_entry.get(), username_entry.get(), password_entry.get()]
    new_data = {
        list[0]: {
            "username": list[1],
            "password": list[2],
        }
    } 
    # check for empty fields
    check_for_empty(list)       
    # confirmation message box
    is_ok = messagebox.askokcancel(
        title="New password", message=f"Entered data: \nWebsite: {list[0]} \nUsername/Email: {list[1]} \nPassword: {list[2]} \nDo you wnat to proceed?")
    #save in Json db
    if is_ok:
        try:
            with open("db.json", "r") as db:
                # load old data
                data = json.load(db)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("db.json", "w") as db:
                json.dump(new_data, db, indent=4)
        else:
            data.update(new_data)        
            with open("db.json", "w") as db:
                json.dump(data, db, indent=4)
        finally:
            messagebox.showinfo(
                title="Success", message="Password successfully added") 
            clear()                                       
                
def check_for_empty(list):
    for i in list:
        if i == "":
            print("Fill all fields")
            messagebox.showwarning(
                title="Retry", message="Fill all the fields")
            return        

def search():
    website = website_entry.get()
    try:
        with open("db.json", "r") as db:
            data = json.load(db)
    except FileNotFoundError:
        messagebox.showwarning(title="Data file not found", message="Data file not found. Try inserting a new record.")
    else:
        if website in data:
            messagebox.showinfo(title="Results", message=f"Results for {website}:\nUsername: {data[website]['username']}\nPassword: {data[website]['password']}")
        elif len(website_entry.get()) == 0:
            messagebox.showwarning(title="Field is empty", message="Please fill the website field")
        else:
            messagebox.showinfo(title="Not Found", message=f"No matches for {website}")
            
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
logo = PhotoImage(file="logo.png")
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
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=EW)

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

search_btn = Button(text="Search website", width=15, command=search)
search_btn.grid(column=2, row=1)

window.mainloop()
