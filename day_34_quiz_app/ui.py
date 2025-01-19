from tkinter import Button, Label, Canvas, Tk, PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title = "Quiz Game"
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", bg=THEME_COLOR, highlightthickness=0, fg="white", font=("Arial", 14, "bold"), padx=10, pady=10)
        self.score_text.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, highlightthickness=0)
        self.text = self.canvas.create_text(150, 125, text="THIS IS A TEXT", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="images/true.png")
        self.false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.true_image, bg=THEME_COLOR, highlightthickness=0, command=self.correct_answer)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, bg=THEME_COLOR, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.text, text=self.quiz.next_question())
            self.score_text.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("true"))
    def wrong_answer(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

