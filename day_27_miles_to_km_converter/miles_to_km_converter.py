from tkinter import *

window = Tk()
window.title("Miles to km Converter")
window.minsize(200,120)
window.config(padx=20, pady=20)
def on_button_click():
    result_label.config(text=int(input.get()) * 1.609344)

empty_label = Label(text="")
empty_label.grid(column=0, row=0)

input = Spinbox(from_=0, to=9999999999999,width=10)
input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

result_label = Label(text=0)
result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=on_button_click)
calculate_button.grid(column=1, row=2)

window.mainloop()