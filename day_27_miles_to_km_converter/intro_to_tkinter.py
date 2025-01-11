from tkinter import *
def button_clicked():
    label.config(text=input.get())

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height = 300)
window.config(padx=100, pady=200)

# Label

label = Label(text="I am a label", font=("Arial", 24, "italic"))
label.grid(column=0, row=0)

# Button

button = Button(text = "Button", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="text")
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)












window.mainloop()

