BACKGROUND_COLOR = "#B1DDC6"
from random import choice
from tkinter import Tk, Canvas, Button, PhotoImage

import pandas
try:
    with open("words_to_learn.csv", "r", encoding="utf8") as file:
        data = pandas.read_csv(file)
except FileNotFoundError:
    with open("en_tr_top_100_words.csv", "r", encoding="utf8") as file:
        data = pandas.read_csv(file)
data_dict_list = data.to_dict(orient="records")
random_dict = {}


def correct_answer():
    global random_dict
    data_dict_list.remove(random_dict)
    pandas.DataFrame(data_dict_list).to_csv("words_to_learn.csv", index=False)
    next_card()


def next_card():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    random_dict = choice(data_dict_list)
    canvas.itemconfig(title_text, text="English", fill="black")
    canvas.itemconfig(word_text, text=random_dict["en"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global random_dict
    canvas.itemconfig(title_text, text="Turkish", fill="white")
    canvas.itemconfig(word_text, text=random_dict["tr"], fill="white")
    canvas.itemconfig(canvas_image, image=card_back_image)


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_image)
title_text = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_image, highlightthickness=0, command=correct_answer)
right_button.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)
next_card()

window.mainloop()
