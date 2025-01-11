from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for sym in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if website_entry.get() != "" and username_entry.get() != "" and password_entry.get() != "":
        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered:\nEmail: {username_entry.get()}\n Password: {password_entry.get()}\nSave?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showwarning(title="Oops", message="Please don't leave any of the fields empty.")


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

website_entry = Entry(width=51)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

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
