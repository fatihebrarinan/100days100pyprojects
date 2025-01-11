from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    title_text.config(text="Timer", fg=GREEN)
    checkmark_text.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        countdown(WORK_MIN * 60)
        title_text.config(text="Work", fg=GREEN)
    elif reps == 8:
        countdown(LONG_BREAK_MIN * 60)
        title_text.config(text="Break", fg=RED)
    else:
        countdown(SHORT_BREAK_MIN * 60)
        title_text.config(text="Break", fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    if count == 0 and reps < 8:
        if reps % 2 == 1:
            checkmark_text["text"] += "✔"
        start_timer()



    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
time_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", width=7, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=7, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

title_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_text.grid(column=1, row=0)

checkmark_text = Label(bg=YELLOW, fg=GREEN)
checkmark_text.grid(column=1, row=3)

window.mainloop()