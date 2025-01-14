from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for sym in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_data = {
        website_entry.get(): {
            "username": username_entry.get(),
            "password": password_entry.get()
        }
    }
    if website_entry.get() != "" and username_entry.get() != "" and password_entry.get() != "":
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any of the fields empty.")
# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="Warning!", message="This is the first time you open the program. You can't search!")
    else:
        if website_entry.get() in data:
            message = f"Username/Email: {data[website_entry.get()]["username"]}\nPassword: {data[website_entry.get()]["password"]}"
            messagebox.showinfo(title=website_entry.get(), message=message)
        else:
            messagebox.showwarning(title=website_entry.get(), message="Website not found. Try adding it.")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1)
website_entry.focus()

website_search_button = Button(text="Search", width=14, command=search_website)
website_search_button.grid(row=1, column=2)

username_text = Label(text="Email/Username:")
username_text.grid(row=2, column=0)

username_entry = Entry(width=51)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "fatih@gmail.com")

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

generatepassword_button = Button(text="Generate Password", width=14, command=generate_password)
generatepassword_button.grid(row=3, column=2)

add_button = Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
