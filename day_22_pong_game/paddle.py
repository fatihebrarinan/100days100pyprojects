from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)
